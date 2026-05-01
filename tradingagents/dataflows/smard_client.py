"""SMARD (Strommarktdaten) client for German electricity data.

SMARD is the German Federal Network Agency's data platform.
It provides detailed generation by type, total load, and residual load.

Base URL: https://www.smard.de/app/chart_data
No authentication required.
No official API docs — reverse-engineered from the website.

The API pattern is:
GET {base_url}/{filter_id}/{resolution}/{timestamp_ms}.json

Where:
filter_id: identifies the data series (see FILTER_IDS below)
resolution: "hour" or "quarterhour"
timestamp_ms: start of the week (Monday 00:00 CET) as Unix timestamp in milliseconds
"""

import requests
import logging
from datetime import datetime, timedelta
from typing import Annotated, Optional, Dict, List
import pandas as pd
try:
    from .energy_utils import CET, format_price_table, get_cache_path
    from .config import get_config
    from . import cache_layer
except ImportError:
    from energy_utils import CET, format_price_table, get_cache_path
    from config import get_config
    import cache_layer

logger = logging.getLogger(__name__)

SMARD_BASE_URL = "https://www.smard.de/app/chart_data"

# SMARD filter IDs for electricity generation by type
FILTER_IDS = {
    # Generation by source
    "generation_total": 410,
    "generation_biomass": 4066,
    "generation_hydro": 1226,
    "generation_wind_offshore": 1225,
    "generation_wind_onshore": 4067,
    "generation_solar": 4068,
    "generation_nuclear": 1224,  # Germany finalized its nuclear phase-out in April 2023
    "generation_lignite": 1223,
    "generation_hard_coal": 4069,
    "generation_gas": 4071,
    "generation_pumped_storage": 4070,
    "generation_other": 1227,

    # Consumption / load
    "total_load": 410,
    "residual_load": 4359,
    "forecast_load": 123,
    "actual_load": 715,

    # Prices (Day-Ahead)
    "price_de_lu": 4169,
    "price_at": 4170,
    "price_fr": 254,
    "price_nl": 256,
    "price_pl": 257,
    "price_cz": 261,
    "price_dk1": 252,
    "price_dk2": 253,
    "price_ch": 259,

    # Forecasts
    "forecast_generation_total": 122,
    "forecast_generation_wind_solar": 3791,
}

_session = None


def _get_session() -> requests.Session:
    global _session
    if _session is None:
        _session = requests.Session()
    return _session


def _get_week_start_timestamp(date_str: str) -> int:
    """Get the Unix timestamp (ms) for the Monday 00:00 CET of the week containing the date."""
    dt = datetime.strptime(date_str, "%Y-%m-%d")

    monday = dt - timedelta(days=dt.weekday())
    monday_cet = CET.localize(datetime(monday.year, monday.month, monday.day, 0, 0, 0))

    return int(monday_cet.timestamp() * 1000)


def _fetch_smard_series(filter_id: int, resolution: str, date_str: str, region: str = "DE") -> pd.DataFrame:
    """Fetch a single SMARD data series."""
    ts_ms = _get_week_start_timestamp(date_str)
    url = f"{SMARD_BASE_URL}/{filter_id}/{region}/{filter_id}_{region}_{resolution}_{ts_ms}.json"

    try:
        response = _get_session().get(url, timeout=30)
        response.raise_for_status()
        data = response.json()

        if "series" not in data or not data["series"]:
            logger.warning(f"No data series found in SMARD response for filter {filter_id} on {date_str}")
            return pd.DataFrame()

        series_data = data["series"]
        if not series_data or len(series_data) < 2:
            logger.warning(f"Unexpected data format in SMARD response for filter {filter_id} on {date_str}")
            return pd.DataFrame()

        records = []
        from datetime import timezone  # add this import at the top of the file if needed
        for point in series_data:
            if point is None:
                logger.warning(f"Encountered null data point in SMARD series {filter_id} for date {date_str}")
                continue
            if isinstance(point, list) and len(point) >= 2:
                ts = datetime.fromtimestamp(point[0] / 1000, tz=timezone.utc).astimezone(CET)
                value = point[1]
                records.append({"timestamp": ts, "value": value})

        if not records:
            logger.warning(f"No valid data points found in SMARD series {filter_id} for date {date_str}")
            return pd.DataFrame()

        df = pd.DataFrame(records)
        df.set_index("timestamp", inplace=True)
        df.index.name = "CET"

        return df
    except Exception as e:
        logger.warning(f"Failed to fetch SMARD filter {filter_id}: {e}")
        return pd.DataFrame()


def _load_or_fetch(source: str, query_type: str, market_area: str, date_str: str, fetch_fn):
    """Cache wrapper for SMARD data."""
    try:
        cached_df = cache_layer.load_cached(source, query_type, market_area, date_str)
        if cached_df is not None:
            logger.debug(f"Cache hit: {source}/{query_type}/{market_area}/{date_str}")
            return cached_df
    except Exception as e:
        logger.warning(f"Cache read error: {e}")

    try:
        df = fetch_fn()
        if df is not None and not df.empty:
            try:
                cache_layer.save_to_cache(df, source, query_type, market_area, date_str)
            except Exception as e:
                logger.warning(f"Cache write error: {e}")
        return df
    except Exception as e:
        logger.error(f"Fetch error for {source}/{query_type}/{market_area}/{date_str}: {e}")
        return pd.DataFrame()


def get_german_generation(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    resolution: Annotated[str, "Resolution: 'hour' or 'quarterhour'"] = "hour",
) -> str:
    """Fetch German generation breakdown by type from SMARD."""
    def fetch():
        generation_types = [
            ("Total", "generation_total"),
            ("Wind Onshore", "generation_wind_onshore"),
            ("Wind Offshore", "generation_wind_offshore"),
            ("Solar", "generation_solar"),
            ("Nuclear", "generation_nuclear"),
            ("Lignite", "generation_lignite"),
            ("Hard Coal", "generation_hard_coal"),
            ("Gas", "generation_gas"),
            ("Pumped Storage", "generation_pumped_storage"),
            ("Hydro", "generation_hydro"),
            ("Biomass", "generation_biomass"),
            ("Other", "generation_other"),
        ]

        dfs = []
        for col_name, filter_name in generation_types:
            filter_id = FILTER_IDS.get(filter_name)
            if filter_id is None:
                logger.warning(f"Filter ID for {filter_name} not found")
                continue

            df = _fetch_smard_series(filter_id, resolution, delivery_date)
            if not df.empty:
                df = df.rename(columns={"value": col_name})
                dfs.append(df)

        if not dfs:
            logger.warning(f"No valid generation data fetched for any type in Germany on {delivery_date}")
            return pd.DataFrame()

        result = dfs[0]
        for df in dfs[1:]:
            result = result.join(df, how="outer")

        result = result.sort_index()

        date_dt = datetime.strptime(delivery_date, "%Y-%m-%d")
        start = CET.localize(date_dt)
        end = CET.localize(date_dt + timedelta(days=1))
        result = result[(result.index >= start) & (result.index < end)]

        return result.fillna(0)

    df = _load_or_fetch("smard", f"generation_{resolution}", "DE-LU", delivery_date, fetch)

    if df is None or df.empty:
        logger.warning(f"No generation data available for Germany on {delivery_date}")
        return f"# No German generation data for {delivery_date}"

    header = f"# German Generation by Type on {delivery_date} ({resolution})\n"
    header += "# Source: SMARD (Bundesnetzagentur)\n"
    header += "# Unit: MW\n\n"

    return header + df.to_csv()


def get_german_residual_load(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    resolution: Annotated[str, "Resolution: 'hour' or 'quarterhour'"] = "hour",
) -> str:
    """Fetch German residual load (total load minus wind and solar) from SMARD."""
    def fetch():
        filter_id = FILTER_IDS.get("residual_load")
        if filter_id is None:
            logger.warning("Filter ID for residual load not found")
            return pd.DataFrame()

        df = _fetch_smard_series(filter_id, resolution, delivery_date)
        if df.empty:
            logger.warning(f"No residual load data fetched for Germany on {delivery_date}")
            return pd.DataFrame()

        df = df.rename(columns={"value": "Residual Load MW"})
        df = df[["Residual Load MW"]]

        date_dt = datetime.strptime(delivery_date, "%Y-%m-%d")
        start = CET.localize(date_dt)
        end = CET.localize(date_dt + timedelta(days=1))
        df = df[(df.index >= start) & (df.index < end)]

        return df

    df = _load_or_fetch("smard", f"residual_load_{resolution}", "DE-LU", delivery_date, fetch)

    if df is None or df.empty:
        logger.warning(f"No residual load data available for Germany on {delivery_date}")
        return f"# No German residual load data for {delivery_date}"

    header = f"# German Residual Load on {delivery_date} ({resolution})\n"
    header += "# Source: SMARD (Bundesnetzagentur)\n"
    header += "# Unit: MW (Load - Wind - Solar)\n\n"

    return header + df.to_csv()


def get_german_total_load(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    resolution: Annotated[str, "Resolution: 'hour' or 'quarterhour'"] = "hour",
) -> str:
    """Fetch German total load from SMARD."""
    def fetch():
        filter_id = FILTER_IDS.get("total_load")
        if filter_id is None:
            logger.warning("Filter ID for total load not found")
            return pd.DataFrame()

        df = _fetch_smard_series(filter_id, resolution, delivery_date)
        if df.empty:
            logger.warning(f"No total load data fetched for Germany on {delivery_date}")
            return pd.DataFrame()

        df = df.rename(columns={"value": "Total Load MW"})
        df = df[["Total Load MW"]]

        date_dt = datetime.strptime(delivery_date, "%Y-%m-%d")
        start = CET.localize(date_dt)
        end = CET.localize(date_dt + timedelta(days=1))
        df = df[(df.index >= start) & (df.index < end)]

        return df

    df = _load_or_fetch("smard", f"total_load_{resolution}", "DE-LU", delivery_date, fetch)

    if df is None or df.empty:
        logger.warning(f"No total load data available for Germany on {delivery_date}")
        return f"# No German total load data for {delivery_date}"

    header = f"# German Total Load on {delivery_date} ({resolution})\n"
    header += "# Source: SMARD (Bundesnetzagentur)\n"
    header += "# Unit: MW\n\n"

    return header + df.to_csv()


def get_smard_prices(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    market_area: Annotated[str, "Bidding zone (e.g., 'DE-LU', 'AT', 'FR', 'CZ')"],
    resolution: Annotated[str, "Resolution: 'hour' or 'quarterhour'"] = "hour",
) -> str:
    """Fetch Day-Ahead Market prices for a specific region from SMARD."""
    def fetch():
        area_map = {
            "DE-LU": "price_de_lu", "AT": "price_at", "FR": "price_fr",
            "NL": "price_nl", "PL": "price_pl", "CZ": "price_cz",
            "DK1": "price_dk1", "DK2": "price_dk2", "CH": "price_ch"
        }
        filter_name = area_map.get(market_area)
        if not filter_name:
            logger.warning(f"Market area {market_area} not supported by SMARD prices.")
            return pd.DataFrame()

        filter_id = FILTER_IDS.get(filter_name)

        # Note: SMARD region code is usually DE for German data, but for prices it handles
        # the specific ID mapping internally, so we can just pass "DE" as the base region parameter.
        df = _fetch_smard_series(filter_id, resolution, delivery_date, region="DE")

        if df.empty:
            logger.warning(f"No price data fetched for {market_area} on {delivery_date}")
            return pd.DataFrame()

        df = df.rename(columns={"value": "Price EUR/MWh"})

        date_dt = datetime.strptime(delivery_date, "%Y-%m-%d")
        start = CET.localize(date_dt)
        end = CET.localize(date_dt + timedelta(days=1))
        df = df[(df.index >= start) & (df.index < end)]

        return df

    df = _load_or_fetch("smard", f"prices_{market_area}_{resolution}", market_area, delivery_date, fetch)

    if df is None or df.empty:
        logger.warning(f"No SMARD price data available for {market_area} on {delivery_date}")
        return f"# No SMARD price data for {market_area} on {delivery_date}"

    header = f"# Day-Ahead Prices for {market_area} on {delivery_date} ({resolution})\n"
    header += "# Source: SMARD (Bundesnetzagentur)\n"
    header += "# Unit: EUR/MWh\n\n"

    return header + df.to_csv()


def get_german_generation_forecast(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    resolution: Annotated[str, "Resolution: 'hour' or 'quarterhour'"] = "hour",
) -> str:
    """Fetch German forecasted generation (Total and Wind/Solar) from SMARD."""
    def fetch():
        forecast_types = [
            ("Forecast Total", "forecast_generation_total"),
            ("Forecast Wind & Solar", "forecast_generation_wind_solar"),
        ]

        dfs = []
        for col_name, filter_name in forecast_types:
            filter_id = FILTER_IDS.get(filter_name)
            df = _fetch_smard_series(filter_id, resolution, delivery_date)
            if not df.empty:
                df = df.rename(columns={"value": col_name})
                dfs.append(df)

        if not dfs:
            logger.warning(f"No valid generation forecast data fetched for any type in Germany on {delivery_date}")
            return pd.DataFrame()

        result = dfs[0]
        for df in dfs[1:]:
            result = result.join(df, how="outer")

        result = result.sort_index()

        date_dt = datetime.strptime(delivery_date, "%Y-%m-%d")
        start = CET.localize(date_dt)
        end = CET.localize(date_dt + timedelta(days=1))
        result = result[(result.index >= start) & (result.index < end)]

        return result.fillna(0)

    df = _load_or_fetch("smard", f"generation_forecast_{resolution}", "DE-LU", delivery_date, fetch)

    if df is None or df.empty:
        logger.warning(f"No generation forecast data available for Germany on {delivery_date}")
        return f"# No German generation forecast data for {delivery_date}"

    header = f"# German Generation Forecast on {delivery_date} ({resolution})\n"
    header += "# Source: SMARD (Bundesnetzagentur)\n"
    header += "# Unit: MW\n\n"

    return header + df.to_csv()


def get_german_load_forecast(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    resolution: Annotated[str, "Resolution: 'hour' or 'quarterhour'"] = "hour",
) -> str:
    """Fetch German load forecast from SMARD."""
    def fetch():
        filter_id = FILTER_IDS.get("forecast_load")
        if filter_id is None:
            logger.warning("Filter ID for load forecast not found")
            return pd.DataFrame()

        df = _fetch_smard_series(filter_id, resolution, delivery_date)
        if df.empty:
            logger.warning(f"No load forecast data fetched for Germany on {delivery_date}")
            return pd.DataFrame()

        df = df.rename(columns={"value": "Load Forecast MW"})
        df = df[["Load Forecast MW"]]

        date_dt = datetime.strptime(delivery_date, "%Y-%m-%d")
        start = CET.localize(date_dt)
        end = CET.localize(date_dt + timedelta(days=1))
        df = df[(df.index >= start) & (df.index < end)]

        return df

    df = _load_or_fetch("smard", f"forecast_load_{resolution}", "DE-LU", delivery_date, fetch)

    if df is None or df.empty:
        logger.warning(f"No German load forecast data available for {delivery_date}")
        return f"# No German load forecast data for {delivery_date}"

    header = f"# German Load Forecast on {delivery_date} ({resolution})\n"
    header += "# Source: SMARD (Bundesnetzagentur)\n"
    header += "# Unit: MW\n\n"

    return header + df.to_csv()


if __name__ == "__main__":
    import sys
    date = sys.argv[1] if len(sys.argv) > 1 else "2026-05-01"

    print("\n=== get_german_generation ===")
    print(get_german_generation(date, resolution="hour"))

    print("\n=== get_german_residual_load ===")
    print(get_german_residual_load(date, resolution="hour"))

    print("\n=== get_german_total_load ===")
    print(get_german_total_load(date, resolution="hour"))

    print("\n=== get_smard_prices ===")
    print(get_smard_prices(date, market_area="DE-LU", resolution="hour"))
    print(get_smard_prices(date, market_area="CZ", resolution="hour"))

    print("\n=== get_german_generation_forecast ===")
    print(get_german_generation_forecast(date, resolution="hour"))

    print("\n=== get_german_load_forecast ===")
    print(get_german_load_forecast(date, resolution="hour"))

"""
Reference output
=== get_german_generation ===
Failed to fetch SMARD filter 1224: 404 Client Error: Not Found for url: https://www.smard.de/app/chart_data/1224/DE/1224_DE_hour_1777240800000.json
# German Generation by Type on 2026-05-01 (hour)
# Source: SMARD (Bundesnetzagentur)
# Unit: MW

CET,Total,Wind Onshore,Wind Offshore,Solar,Lignite,Hard Coal,Gas,Pumped Storage,Hydro,Biomass,Other
2026-05-01 00:00:00+02:00,42780.84,14686.82,5063.76,0.0,5101.39,1666.0,4204.22,2313.69,1339.39,4130.91,1822.19
2026-05-01 01:00:00+02:00,40832.82,14142.98,4978.31,0.0,4638.71,1642.62,3918.82,1708.14,1326.17,4082.65,1808.27
2026-05-01 02:00:00+02:00,39261.01,13490.25,4167.01,0.0,4536.85,1637.41,3919.47,917.8,1300.59,4068.31,1808.34
2026-05-01 03:00:00+02:00,38713.13,12810.96,3511.52,0.0,4582.56,1636.92,3879.52,1881.25,1283.89,4067.04,1803.15
2026-05-01 04:00:00+02:00,38725.42,12204.6,3130.7,0.0,4620.36,1630.67,3978.6,1281.37,1259.85,4115.12,1806.87
2026-05-01 05:00:00+02:00,38622.22,11675.68,2819.9,32.33,4678.7,1627.71,3834.14,849.52,1219.98,4174.88,1802.86
2026-05-01 06:00:00+02:00,31886.75,11516.62,2754.35,2222.46,4654.35,1481.81,3249.28,1931.21,1216.44,4338.85,1810.33
2026-05-01 07:00:00+02:00,37447.25,10558.44,2700.88,10337.67,3904.92,938.01,2830.68,891.89,1221.6,4445.83,1811.67
2026-05-01 08:00:00+02:00,36672.79,7580.1,2859.15,23964.87,2241.2,707.47,1848.74,29.25,1240.15,4421.32,1778.96
2026-05-01 09:00:00+02:00,0.0,5223.56,2208.72,35966.41,2018.37,525.2,1491.69,7.09,1326.54,4296.45,1550.42
2026-05-01 10:00:00+02:00,0.0,3810.31,999.19,43013.37,1915.79,397.16,1471.03,6.0,1147.74,4169.02,1481.51
2026-05-01 11:00:00+02:00,0.0,2517.66,397.14,46058.76,1838.51,385.35,1411.51,6.61,1112.14,4091.91,1429.14
2026-05-01 12:00:00+02:00,0.0,1512.11,181.16,45206.36,1846.37,380.57,1412.72,78.75,1116.54,3986.95,1435.26
2026-05-01 13:00:00+02:00,0.0,1489.27,166.33,44298.15,1839.99,380.27,1415.73,75.17,1106.24,3952.53,1430.39
2026-05-01 14:00:00+02:00,0.0,1595.33,360.2,42441.48,1835.52,374.73,1419.85,41.22,1085.21,3949.83,1414.29
2026-05-01 15:00:00+02:00,0.0,2452.85,534.92,40214.42,1858.85,373.4,1422.85,20.05,1097.25,3957.95,1436.98
2026-05-01 16:00:00+02:00,0.0,3950.41,1304.69,35719.43,2017.72,381.88,1423.92,68.21,1102.32,4029.5,1460.43
2026-05-01 17:00:00+02:00,0.0,6167.53,3199.22,28271.63,2057.22,411.91,1459.69,70.38,1328.03,4161.03,1471.55
2026-05-01 18:00:00+02:00,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
2026-05-01 19:00:00+02:00,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
2026-05-01 20:00:00+02:00,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
2026-05-01 21:00:00+02:00,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
2026-05-01 22:00:00+02:00,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
2026-05-01 23:00:00+02:00,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0


=== get_german_residual_load ===
# German Residual Load on 2026-05-01 (hour)
# Source: SMARD (Bundesnetzagentur)
# Unit: MW (Load - Wind - Solar)

CET,Residual Load MW
2026-05-01 00:00:00+02:00,23030.27
2026-05-01 01:00:00+02:00,21711.53
2026-05-01 02:00:00+02:00,21603.75
2026-05-01 03:00:00+02:00,22390.65
2026-05-01 04:00:00+02:00,23390.12
2026-05-01 05:00:00+02:00,24094.31
2026-05-01 06:00:00+02:00,15393.32
2026-05-01 07:00:00+02:00,13850.27
2026-05-01 08:00:00+02:00,2268.68
2026-05-01 09:00:00+02:00,
2026-05-01 10:00:00+02:00,
2026-05-01 11:00:00+02:00,
2026-05-01 12:00:00+02:00,
2026-05-01 13:00:00+02:00,
2026-05-01 14:00:00+02:00,
2026-05-01 15:00:00+02:00,
2026-05-01 16:00:00+02:00,
2026-05-01 17:00:00+02:00,
2026-05-01 18:00:00+02:00,
2026-05-01 19:00:00+02:00,
2026-05-01 20:00:00+02:00,
2026-05-01 21:00:00+02:00,
2026-05-01 22:00:00+02:00,
2026-05-01 23:00:00+02:00,


=== get_german_total_load ===
# German Total Load on 2026-05-01 (hour)
# Source: SMARD (Bundesnetzagentur)
# Unit: MW

CET,Total Load MW
2026-05-01 00:00:00+02:00,42780.84
2026-05-01 01:00:00+02:00,40832.82
2026-05-01 02:00:00+02:00,39261.01
2026-05-01 03:00:00+02:00,38713.13
2026-05-01 04:00:00+02:00,38725.42
2026-05-01 05:00:00+02:00,38622.22
2026-05-01 06:00:00+02:00,31886.75
2026-05-01 07:00:00+02:00,37447.25
2026-05-01 08:00:00+02:00,36672.79
2026-05-01 09:00:00+02:00,
2026-05-01 10:00:00+02:00,
2026-05-01 11:00:00+02:00,
2026-05-01 12:00:00+02:00,
2026-05-01 13:00:00+02:00,
2026-05-01 14:00:00+02:00,
2026-05-01 15:00:00+02:00,
2026-05-01 16:00:00+02:00,
2026-05-01 17:00:00+02:00,
2026-05-01 18:00:00+02:00,
2026-05-01 19:00:00+02:00,
2026-05-01 20:00:00+02:00,
2026-05-01 21:00:00+02:00,
2026-05-01 22:00:00+02:00,
2026-05-01 23:00:00+02:00,


=== get_smard_prices ===
# Day-Ahead Prices for DE-LU on 2026-05-01 (hour)
# Source: SMARD (Bundesnetzagentur)
# Unit: EUR/MWh

CET,Price EUR/MWh
2026-05-01 00:00:00+02:00,107.23
2026-05-01 01:00:00+02:00,103.09
2026-05-01 02:00:00+02:00,101.39
2026-05-01 03:00:00+02:00,99.25
2026-05-01 04:00:00+02:00,97.98
2026-05-01 05:00:00+02:00,97.5
2026-05-01 06:00:00+02:00,103.77
2026-05-01 07:00:00+02:00,80.34
2026-05-01 08:00:00+02:00,35.33
2026-05-01 09:00:00+02:00,-0.03
2026-05-01 10:00:00+02:00,-21.18
2026-05-01 11:00:00+02:00,-108.62
2026-05-01 12:00:00+02:00,-318.58
2026-05-01 13:00:00+02:00,-499.0
2026-05-01 14:00:00+02:00,-474.97
2026-05-01 15:00:00+02:00,-205.88
2026-05-01 16:00:00+02:00,-26.25
2026-05-01 17:00:00+02:00,5.56
2026-05-01 18:00:00+02:00,92.53
2026-05-01 19:00:00+02:00,154.19
2026-05-01 20:00:00+02:00,173.33
2026-05-01 21:00:00+02:00,142.95
2026-05-01 22:00:00+02:00,113.22
2026-05-01 23:00:00+02:00,96.98

# Day-Ahead Prices for CZ on 2026-05-01 (hour)
# Source: SMARD (Bundesnetzagentur)
# Unit: EUR/MWh

CET,Price EUR/MWh
2026-05-01 00:00:00+02:00,111.53
2026-05-01 01:00:00+02:00,107.5
2026-05-01 02:00:00+02:00,106.64
2026-05-01 03:00:00+02:00,104.58
2026-05-01 04:00:00+02:00,103.47
2026-05-01 05:00:00+02:00,102.38
2026-05-01 06:00:00+02:00,95.16
2026-05-01 07:00:00+02:00,85.06
2026-05-01 08:00:00+02:00,36.48
2026-05-01 09:00:00+02:00,-0.04
2026-05-01 10:00:00+02:00,-21.99
2026-05-01 11:00:00+02:00,-112.83
2026-05-01 12:00:00+02:00,-326.57
2026-05-01 13:00:00+02:00,-500.0
2026-05-01 14:00:00+02:00,-479.1
2026-05-01 15:00:00+02:00,-214.33
2026-05-01 16:00:00+02:00,-27.44
2026-05-01 17:00:00+02:00,2.91
2026-05-01 18:00:00+02:00,93.97
2026-05-01 19:00:00+02:00,139.7
2026-05-01 20:00:00+02:00,162.76
2026-05-01 21:00:00+02:00,137.38
2026-05-01 22:00:00+02:00,119.64
2026-05-01 23:00:00+02:00,100.82


=== get_german_generation_forecast ===
# German Generation Forecast on 2026-05-01 (hour)
# Source: SMARD (Bundesnetzagentur)
# Unit: MW

CET,Forecast Total,Forecast Wind & Solar
2026-05-01 00:00:00+02:00,38496.74,3265.94
2026-05-01 01:00:00+02:00,36119.76,3094.99
2026-05-01 02:00:00+02:00,34683.31,2807.16
2026-05-01 03:00:00+02:00,33693.62,2482.4
2026-05-01 04:00:00+02:00,33466.33,2206.01
2026-05-01 05:00:00+02:00,33585.67,2074.93
2026-05-01 06:00:00+02:00,35602.85,2146.17
2026-05-01 07:00:00+02:00,40933.04,2334.92
2026-05-01 08:00:00+02:00,48583.93,2420.15
2026-05-01 09:00:00+02:00,56654.16,988.51
2026-05-01 10:00:00+02:00,60862.33,1024.58
2026-05-01 11:00:00+02:00,64089.63,979.79
2026-05-01 12:00:00+02:00,65713.52,938.74
2026-05-01 13:00:00+02:00,64547.79,906.38
2026-05-01 14:00:00+02:00,61749.11,908.7
2026-05-01 15:00:00+02:00,58246.1,954.28
2026-05-01 16:00:00+02:00,54491.97,1039.07
2026-05-01 17:00:00+02:00,51642.41,2411.56
2026-05-01 18:00:00+02:00,45184.31,2675.21
2026-05-01 19:00:00+02:00,41560.74,2994.27
2026-05-01 20:00:00+02:00,40623.59,3317.26
2026-05-01 21:00:00+02:00,43197.37,3622.72
2026-05-01 22:00:00+02:00,44462.0,3819.01
2026-05-01 23:00:00+02:00,44053.93,3861.72


=== get_german_load_forecast ===
# German Load Forecast on 2026-05-01 (hour)
# Source: SMARD (Bundesnetzagentur)
# Unit: MW

CET,Load Forecast MW
2026-05-01 00:00:00+02:00,13886.71
2026-05-01 01:00:00+02:00,13098.44
2026-05-01 02:00:00+02:00,12222.88
2026-05-01 03:00:00+02:00,11568.51
2026-05-01 04:00:00+02:00,11199.47
2026-05-01 05:00:00+02:00,11044.54
2026-05-01 06:00:00+02:00,11041.88
2026-05-01 07:00:00+02:00,10511.12
2026-05-01 08:00:00+02:00,8274.09
2026-05-01 09:00:00+02:00,6017.1
2026-05-01 10:00:00+02:00,5510.01
2026-05-01 11:00:00+02:00,5212.44
2026-05-01 12:00:00+02:00,4534.83
2026-05-01 13:00:00+02:00,4114.46
2026-05-01 14:00:00+02:00,4175.42
2026-05-01 15:00:00+02:00,4611.54
2026-05-01 16:00:00+02:00,5279.0
2026-05-01 17:00:00+02:00,6066.1
2026-05-01 18:00:00+02:00,6679.03
2026-05-01 19:00:00+02:00,7321.53
2026-05-01 20:00:00+02:00,9453.48
2026-05-01 21:00:00+02:00,12671.59
2026-05-01 22:00:00+02:00,15160.08
2026-05-01 23:00:00+02:00,16948.19
"""