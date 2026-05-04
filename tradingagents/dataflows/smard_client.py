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
    "forecast_load": 411,        # CORRECTED: 411 is Prognostizierter Stromverbrauch
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
    "forecast_wind_onshore": 123,
    "forecast_wind_offshore": 124,
    "forecast_solar": 125,
    "forecast_generation_wind_solar": 5097,  # CORRECTED: 5097 is Prognostizierte Erzeugung Wind und Photovoltaik
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
        from datetime import timezone
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


def _format_index(df: pd.DataFrame) -> pd.DataFrame:
    """Format DatetimeIndex to save LLM tokens and standardize output."""
    if df is not None and not df.empty and isinstance(df.index, pd.DatetimeIndex):
        df = df.round(3)  # Round to 3 decimals for cleaner display
        df.index = df.index.strftime('%H:%M')
        df.index.name = "Hour"
    return df


def get_german_generation(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    market_area: Annotated[str, "Bidding zone, e.g. 'DE-LU'"] = "DE-LU",
    resolution: Annotated[str, "Resolution: 'hour' or 'quarterhour'"] = "hour",
) -> str:
    """Fetch German generation breakdown by type from SMARD."""
    if market_area.upper() != "DE-LU":
        logger.warning(f"SMARD generation client only supports DE-LU market area. Requested: {market_area}")
        return f"# No generation data available for {market_area} on {delivery_date} (SMARD supports DE-LU only)"

    def fetch():
        generation_types = [
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
                continue

            df = _fetch_smard_series(filter_id, resolution, delivery_date)
            if not df.empty:
                df = df.rename(columns={"value": col_name})
                dfs.append(df)

        if not dfs:
            return pd.DataFrame()

        result = dfs[0]
        for df in dfs[1:]:
            result = result.join(df, how="outer")

        result = result.sort_index()

        date_dt = datetime.strptime(delivery_date, "%Y-%m-%d")
        start = CET.localize(date_dt)
        end = CET.localize(date_dt + timedelta(days=1))
        result = result[(result.index >= start) & (result.index < end)]

        result = result.fillna(0)
        result.insert(0, "Total", result.sum(axis=1))

        return result

    df = _load_or_fetch("smard", f"generation_{resolution}", market_area.upper(), delivery_date, fetch)

    if df is None or df.empty:
        return f"# No {market_area.upper()} generation data for {delivery_date}"

    df = _format_index(df.copy())
    header = f"# {market_area.upper()} Generation by Type on {delivery_date} ({resolution})\n"
    header += "# Source: SMARD (Bundesnetzagentur)\n"
    header += "# Unit: MW\n\n"

    return header + df.to_csv()


def get_german_residual_load(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    market_area: Annotated[str, "Bidding zone, e.g. 'DE-LU'"] = "DE-LU",
    resolution: Annotated[str, "Resolution: 'hour' or 'quarterhour'"] = "hour",
) -> str:
    """Fetch German residual load (total load minus wind and solar) from SMARD."""
    if market_area.upper() != "DE-LU":
        logger.warning(f"SMARD residual load client only supports DE-LU market area. Requested: {market_area}")
        return f"# No residual load data available for {market_area} on {delivery_date} (SMARD supports DE-LU only)"

    def fetch():
        filter_id = FILTER_IDS.get("residual_load")
        if filter_id is None:
            return pd.DataFrame()

        df = _fetch_smard_series(filter_id, resolution, delivery_date)
        if df.empty:
            return pd.DataFrame()

        df = df.rename(columns={"value": "Residual Load MW"})
        df = df[["Residual Load MW"]]

        date_dt = datetime.strptime(delivery_date, "%Y-%m-%d")
        start = CET.localize(date_dt)
        end = CET.localize(date_dt + timedelta(days=1))
        df = df[(df.index >= start) & (df.index < end)]

        return df

    df = _load_or_fetch("smard", f"residual_load_{resolution}", market_area.upper(), delivery_date, fetch)

    if df is None or df.empty:
        return f"# No {market_area.upper()} residual load data for {delivery_date}"

    df = _format_index(df.copy())
    header = f"# {market_area.upper()} Residual Load on {delivery_date} ({resolution})\n"
    header += "# Source: SMARD (Bundesnetzagentur)\n"
    header += "# Unit: MW (Load - Wind - Solar)\n\n"

    return header + df.to_csv()


def get_german_total_load(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    market_area: Annotated[str, "Bidding zone, e.g. 'DE-LU'"] = "DE-LU",
    resolution: Annotated[str, "Resolution: 'hour' or 'quarterhour'"] = "hour",
) -> str:
    """Fetch German total load from SMARD."""
    if market_area.upper() != "DE-LU":
        logger.warning(f"SMARD total load client only supports DE-LU market area. Requested: {market_area}")
        return f"# No total load data available for {market_area} on {delivery_date} (SMARD supports DE-LU only)"

    def fetch():
        filter_id = FILTER_IDS.get("total_load")
        if filter_id is None:
            return pd.DataFrame()

        df = _fetch_smard_series(filter_id, resolution, delivery_date)
        if df.empty:
            return pd.DataFrame()

        df = df.rename(columns={"value": "Total Load MW"})
        df = df[["Total Load MW"]]

        date_dt = datetime.strptime(delivery_date, "%Y-%m-%d")
        start = CET.localize(date_dt)
        end = CET.localize(date_dt + timedelta(days=1))
        df = df[(df.index >= start) & (df.index < end)]

        return df

    df = _load_or_fetch("smard", f"total_load_{resolution}", market_area.upper(), delivery_date, fetch)

    if df is None or df.empty:
        return f"# No {market_area.upper()} total load data for {delivery_date}"

    df = _format_index(df.copy())
    header = f"# {market_area.upper()} Total Load on {delivery_date} ({resolution})\n"
    header += "# Source: SMARD (Bundesnetzagentur)\n"
    header += "# Unit: MW\n\n"

    return header + df.to_csv()


def get_smard_prices(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    market_area: Annotated[str, "Bidding zone (e.g., 'DE-LU', 'AT', 'FR', 'CZ')"] = "DE-LU",
    resolution: Annotated[str, "Resolution: 'hour' or 'quarterhour'"] = "hour",
) -> str:
    """Fetch Day-Ahead Market prices for a specific region from SMARD."""
    def fetch():
        area_map = {
            "DE-LU": "price_de_lu", "AT": "price_at", "FR": "price_fr",
            "NL": "price_nl", "PL": "price_pl", "CZ": "price_cz",
            "DK1": "price_dk1", "DK2": "price_dk2", "CH": "price_ch"
        }
        filter_name = area_map.get(market_area.upper())
        if not filter_name:
            return pd.DataFrame()

        filter_id = FILTER_IDS.get(filter_name)

        df = _fetch_smard_series(filter_id, resolution, delivery_date, region="DE")

        if df.empty:
            return pd.DataFrame()

        df = df.rename(columns={"value": "Price EUR/MWh"})

        date_dt = datetime.strptime(delivery_date, "%Y-%m-%d")
        start = CET.localize(date_dt)
        end = CET.localize(date_dt + timedelta(days=1))
        df = df[(df.index >= start) & (df.index < end)]

        return df

    df = _load_or_fetch("smard", f"prices_{market_area.upper()}_{resolution}",
                        market_area.upper(), delivery_date, fetch)

    if df is None or df.empty:
        return f"# No SMARD price data for {market_area.upper()} on {delivery_date}"

    df = _format_index(df.copy())
    header = f"# Day-Ahead Prices for {market_area.upper()} on {delivery_date} ({resolution})\n"
    header += "# Source: SMARD (Bundesnetzagentur)\n"
    header += "# Unit: EUR/MWh\n\n"

    return header + df.to_csv()


def get_german_generation_forecast(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    market_area: Annotated[str, "Bidding zone, e.g. 'DE-LU'"] = "DE-LU",
    resolution: Annotated[str, "Resolution: 'hour' or 'quarterhour'"] = "hour",
) -> str:
    """Fetch German forecasted generation (Total, Wind, Solar) from SMARD."""
    if market_area.upper() != "DE-LU":
        logger.warning(f"SMARD generation forecast client only supports DE-LU market area. Requested: {market_area}")
        return f"# No generation forecast data available for {market_area} on {delivery_date} (SMARD supports DE-LU only)"

    def fetch():
        forecast_types = [
            ("Forecast Total", "forecast_generation_total"),
            ("Forecast Wind Onshore", "forecast_wind_onshore"),
            ("Forecast Wind Offshore", "forecast_wind_offshore"),
            ("Forecast Solar", "forecast_solar"),
            ("Forecast Combined Wind & Solar", "forecast_generation_wind_solar"),
        ]

        dfs = []
        for col_name, filter_name in forecast_types:
            filter_id = FILTER_IDS.get(filter_name)
            df = _fetch_smard_series(filter_id, resolution, delivery_date)
            if not df.empty:
                df = df.rename(columns={"value": col_name})
                dfs.append(df)

        if not dfs:
            return pd.DataFrame()

        result = dfs[0]
        for df in dfs[1:]:
            result = result.join(df, how="outer")

        result = result.sort_index()

        date_dt = datetime.strptime(delivery_date, "%Y-%m-%d")
        start = CET.localize(date_dt)
        end = CET.localize(date_dt + timedelta(days=1))
        result = result[(result.index >= start) & (result.index < end)]

        # Drop columns that failed to fetch instead of filling with misleading zeros
        result = result.dropna(axis=1, how='all').fillna(0)

        return result

    df = _load_or_fetch("smard", f"generation_forecast_{resolution}", market_area.upper(), delivery_date, fetch)

    if df is None or df.empty:
        return f"# No {market_area.upper()} generation forecast data for {delivery_date}"

    df = _format_index(df.copy())
    header = f"# {market_area.upper()} Generation Forecast on {delivery_date} ({resolution})\n"
    header += "# Source: SMARD (Bundesnetzagentur)\n"
    header += "# Unit: MW\n\n"

    return header + df.to_csv()


def get_german_load_forecast(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    market_area: Annotated[str, "Bidding zone, e.g. 'DE-LU'"] = "DE-LU",
    resolution: Annotated[str, "Resolution: 'hour' or 'quarterhour'"] = "hour",
) -> str:
    """Fetch German load forecast from SMARD."""
    if market_area.upper() != "DE-LU":
        logger.warning(f"SMARD load forecast client only supports DE-LU market area. Requested: {market_area}")
        return f"# No load forecast data available for {market_area} on {delivery_date} (SMARD supports DE-LU only)"

    def fetch():
        filter_id = FILTER_IDS.get("forecast_load")
        if filter_id is None:
            return pd.DataFrame()

        df = _fetch_smard_series(filter_id, resolution, delivery_date)
        if df.empty:
            return pd.DataFrame()

        df = df.rename(columns={"value": "Load Forecast MW"})
        df = df[["Load Forecast MW"]]

        date_dt = datetime.strptime(delivery_date, "%Y-%m-%d")
        start = CET.localize(date_dt)
        end = CET.localize(date_dt + timedelta(days=1))
        df = df[(df.index >= start) & (df.index < end)]

        return df

    df = _load_or_fetch("smard", f"forecast_load_{resolution}", market_area.upper(), delivery_date, fetch)

    if df is None or df.empty:
        return f"# No {market_area.upper()} load forecast data for {delivery_date}"

    df = _format_index(df.copy())
    header = f"# {market_area.upper()} Load Forecast on {delivery_date} ({resolution})\n"
    header += "# Source: SMARD (Bundesnetzagentur)\n"
    header += "# Unit: MW\n\n"

    return header + df.to_csv()


if __name__ == "__main__":
    import sys
    date = sys.argv[1] if len(sys.argv) > 1 else "2026-04-28"

    try:
        deleted_count = cache_layer.clear_cache(source="smard")
        print(f"Deleted {deleted_count} parquet files from the cache.")
    except Exception as e:
        logger.warning(f"Error clearing cache: {e}")
        pass

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

    try:
        deleted_count = cache_layer.clear_cache(source="smard")
        print(f"Deleted {deleted_count} parquet files from the cache.")
    except Exception as e:
        logger.warning(f"Error clearing cache: {e}")
        pass


"""
Reference output
=== get_dam_prices ===
# Day-Ahead Prices for CZ on 2026-04-28
# Source: OTE Czech Republic
# Note: 15-minute periods have been aggregated into Hourly records

Hour (CET),Price EUR/MWh,Price EUR/MWh StdDev,Price EUR/MWh Range,Volume MWh
00:00,116.03,4.09,9.54,3842.55
01:00,111.44,2.35,5.46,3661.88
02:00,107.98,0.35,0.81,3679.58
03:00,108.07,0.85,1.92,3711.42
04:00,110.61,3.48,7.81,3694.6
05:00,117.18,6.14,13.68,3736.25
06:00,127.9,3.47,7.9,4061.82
07:00,126.18,11.95,26.9,4267.65
08:00,114.61,16.93,38.5,3250.78
09:00,77.9,37.53,87.23,3337.12
10:00,29.58,23.69,52.64,3669.18
11:00,-0.04,0.46,1.05,4021.8
12:00,-3.8,2.51,5.81,4370.23
13:00,-14.2,3.9,9.33,4324.0
14:00,-11.24,3.89,9.16,4317.73
15:00,8.36,8.69,21.0,4188.88
16:00,42.17,33.61,78.19,3683.85
17:00,60.69,37.04,88.04,3304.82
18:00,96.2,22.19,47.46,2902.02
19:00,123.48,14.45,33.83,3299.62
20:00,140.27,3.98,7.99,4409.0
21:00,121.49,8.39,18.08,4100.77
22:00,115.8,6.31,14.83,3870.8
23:00,106.41,3.66,8.75,3781.22


=== get_intraday_prices ===
# Intraday Continuous Prices for CZ on 2026-04-28
# Source: OTE Czech Republic
# Note: 15-minute periods have been aggregated into Hourly records

Hour (CET),Price EUR/MWh,Price EUR/MWh StdDev,Price EUR/MWh Range,Volume MWh
00:00,101.35,2.59,5.65,578.38
01:00,99.94,0.67,1.62,435.28
02:00,96.2,0.58,1.21,394.68
03:00,96.63,0.55,1.16,358.78
04:00,100.4,0.43,1.03,356.5
05:00,103.93,1.81,4.04,327.8
06:00,108.84,0.5,1.02,689.52
07:00,107.12,2.6,5.9,778.25
08:00,91.38,11.17,26.11,1041.25
09:00,52.68,11.66,25.87,1195.3
10:00,7.94,7.31,16.83,1270.7
11:00,-2.11,0.59,1.13,1652.68
12:00,-12.24,1.43,3.33,850.3
13:00,-12.55,0.57,1.35,762.97
14:00,-7.12,2.85,6.05,747.65
15:00,1.06,2.3,4.69,921.72
16:00,19.57,9.59,21.56,692.3
17:00,36.47,9.0,20.1,667.45
18:00,89.3,8.78,18.38,772.0
19:00,114.49,1.66,4.0,1470.58
20:00,131.81,3.67,8.08,708.45
21:00,112.82,4.65,9.54,797.82
22:00,103.54,2.57,5.79,837.75
23:00,93.49,3.13,7.57,983.4


=== get_ida_prices ===
# IDA Auction Prices for CZ on 2026-04-28
# Source: OTE Czech Republic
# Note: 15-minute periods have been aggregated into Hourly records

Hour (CET),Auction,Price EUR/MWh,Price EUR/MWh StdDev,Price EUR/MWh Range,Volume MWh,Import MWh,Export MWh,Saldo MWh
00:00,IDA1,119.99,3.48,7.87,49.4,-50.97,82.72,31.75
00:00,IDA2,103.78,3.23,7.82,48.8,-246.52,207.2,-39.32
01:00,IDA1,114.27,2.6,5.9,29.5,-43.98,57.12,13.15
01:00,IDA2,100.09,2.5,5.89,46.4,-237.88,205.75,-32.12
02:00,IDA1,109.74,0.67,1.6,23.6,-29.48,27.68,-1.8
02:00,IDA2,97.69,0.56,1.35,35.1,-352.9,324.8,-28.1
03:00,IDA1,110.19,0.75,1.61,23.8,-31.4,25.42,-5.98
03:00,IDA2,97.38,0.76,1.72,26.9,-160.7,143.55,-17.15
04:00,IDA1,115.3,5.61,12.42,40.9,-50.62,79.28,28.65
04:00,IDA2,101.32,3.19,6.68,35.8,-214.9,187.98,-26.92
05:00,IDA1,119.31,3.5,7.3,31.2,-31.92,48.18,16.25
05:00,IDA2,106.5,3.29,7.42,39.1,-213.35,191.85,-21.5
06:00,IDA1,124.41,3.01,6.23,34.2,-80.08,84.62,4.55
06:00,IDA2,114.52,3.38,7.85,48.5,-134.02,97.02,-37.0
07:00,IDA1,123.23,11.84,26.62,36.0,-90.72,94.65,3.93
07:00,IDA2,113.98,10.06,23.27,37.3,-54.48,38.42,-16.05
08:00,IDA1,112.49,15.06,35.34,46.4,-31.57,45.22,13.65
08:00,IDA2,102.56,14.78,34.3,49.6,-41.68,19.25,-22.42
09:00,IDA1,75.63,33.91,76.51,27.4,-10.02,0.55,-9.48
09:00,IDA2,65.32,36.52,81.75,35.9,-29.82,23.42,-6.4
10:00,IDA1,29.56,20.65,44.1,27.8,-1.32,4.15,2.82
10:00,IDA2,13.32,21.2,44.94,38.1,-17.92,0.0,-17.92
11:00,IDA1,1.21,2.34,4.76,35.9,-0.55,15.95,15.4
11:00,IDA2,-2.31,1.35,2.93,37.3,-173.68,167.1,-6.58
12:00,IDA1,-3.88,5.19,10.83,29.4,-0.88,9.25,8.38
12:00,IDA2,-10.06,1.67,3.91,37.4,-93.62,70.0,-23.62
12:00,IDA3,-12.08,5.94,13.62,10.2,-57.28,59.88,2.6
13:00,IDA1,-15.04,4.57,9.52,19.8,-0.6,0.9,0.3
13:00,IDA2,-12.93,2.4,4.99,19.5,-88.3,89.25,0.95
13:00,IDA3,-6.57,1.76,3.9,5.4,-8.17,12.05,3.88
14:00,IDA1,-12.71,3.51,8.08,21.1,-0.57,4.08,3.5
14:00,IDA2,-11.24,1.66,3.5,28.0,-54.58,74.3,19.73
14:00,IDA3,-7.27,1.97,4.56,8.9,-3.9,2.2,-1.7
15:00,IDA1,7.8,9.76,23.0,27.3,-1.95,0.75,-1.2
15:00,IDA2,-6.1,4.44,9.98,23.8,-36.4,26.6,-9.8
15:00,IDA3,5.04,1.88,3.95,7.6,-23.1,30.22,7.12
16:00,IDA1,38.41,23.39,51.11,44.7,-13.48,0.62,-12.85
16:00,IDA2,6.46,11.96,26.01,48.4,-85.95,52.2,-33.75
16:00,IDA3,23.54,22.22,41.78,5.2,-38.05,40.83,2.78
17:00,IDA1,63.69,36.44,83.22,45.5,-2.05,19.5,17.45
17:00,IDA2,19.36,23.71,54.73,55.6,-64.1,30.62,-33.48
17:00,IDA3,55.34,25.24,55.42,19.1,-48.62,59.52,10.9
18:00,IDA1,95.31,22.77,47.46,27.6,-0.22,1.78,1.55
18:00,IDA2,109.8,25.59,54.39,48.4,-152.0,196.82,44.82
18:00,IDA3,108.96,33.8,68.15,29.5,-100.92,127.02,26.1
19:00,IDA1,122.73,15.21,35.83,27.6,-0.75,0.75,0.0
19:00,IDA2,133.94,13.65,28.14,41.6,-287.98,315.45,27.48
19:00,IDA3,126.04,23.44,46.07,6.0,-23.75,22.18,-1.58
20:00,IDA1,141.88,4.65,11.01,22.6,-0.88,0.82,-0.05
20:00,IDA2,160.33,18.2,44.19,33.5,-302.12,322.42,20.3
20:00,IDA3,140.0,10.23,22.83,72.2,0.0,64.6,64.6
21:00,IDA1,124.62,5.51,11.41,29.4,-0.45,12.18,11.72
21:00,IDA2,130.34,14.37,32.05,32.6,-129.65,136.7,7.05
21:00,IDA3,119.0,15.26,34.22,78.2,0.0,73.25,73.25
22:00,IDA1,114.38,8.11,19.8,24.8,-11.92,0.28,-11.65
22:00,IDA2,110.9,7.82,16.59,26.9,-149.35,141.02,-8.32
22:00,IDA3,104.42,12.36,28.15,11.6,-47.85,54.65,6.8
23:00,IDA1,104.54,3.88,9.17,20.2,-10.58,0.35,-10.22
23:00,IDA2,102.76,5.92,12.18,29.6,-139.85,128.82,-11.02
23:00,IDA3,89.77,11.2,27.1,10.4,-54.12,62.7,8.57


=== get_imbalance_settlement ===
# Imbalance Settlement for CZ on 2026-04-28 (v0)
# Source: OTE Czech Republic
# Note: 15-minute periods have been aggregated into Hourly records
# Note: Financial values converted from CZK to EUR at official rate of 24.37 CZK/EUR

Hour (CET),System Imbalance MWh,Absolute Imbalance Sum MWh,Positive Imbalance MWh,Negative Imbalance MWh,Rounded Imbalance MWh,Regulating Energy Cost EUR,Imbalance Cost EUR,Imbalance Price EUR/MWh,Imbalance Price EUR/MWh StdDev,Imbalance Price EUR/MWh Range,Counter Imbalance Price EUR/MWh,Counter Imbalance Price EUR/MWh StdDev,Counter Imbalance Price EUR/MWh Range,Weighted Avg RE Price EUR/MWh,Weighted Avg RE Price EUR/MWh StdDev,Weighted Avg RE Price EUR/MWh Range,Opposite Direction RE Price EUR/MWh,Opposite Direction RE Price EUR/MWh StdDev,Opposite Direction RE Price EUR/MWh Range,Weighted Avg Intraday Price EUR/MWh,Weighted Avg Intraday Price EUR/MWh StdDev,Weighted Avg Intraday Price EUR/MWh Range,Base Curve Price EUR/MWh,Base Curve Price EUR/MWh StdDev,Base Curve Price EUR/MWh Range
00:00,-12.48,307.18,147.32,-159.86,0.29,1389.41,-2431.57,55.45,1560.61,2728.17,55.45,1560.61,2728.17,91.81,232.4,539.56,50.03,1411.7,2567.14,101.35,275.53,559.99,92.9,230.4,487.26
01:00,-32.5,289.2,128.31,-160.89,0.27,3320.85,-3605.28,110.2,16.41,39.37,110.2,16.41,39.37,114.76,822.06,1790.78,98.38,199.88,357.26,110.2,16.41,39.37,97.31,240.76,534.66
02:00,-59.94,319.62,129.89,-189.73,0.03,5538.02,-6379.51,106.45,14.06,29.61,106.45,14.06,29.61,91.69,182.65,374.55,94.48,265.26,555.39,106.45,14.06,29.61,95.06,196.3,398.01
03:00,-39.38,298.53,129.57,-168.95,0.21,3034.9,-4209.64,106.89,13.56,28.32,106.89,13.56,28.32,77.52,397.86,954.92,96.66,201.84,427.21,106.89,13.56,28.32,79.74,394.48,941.73
04:00,-30.65,244.12,106.74,-137.37,0.05,2689.71,-3391.22,110.66,10.6,25.15,110.66,10.6,25.15,88.34,112.3,236.49,97.66,186.08,395.52,110.66,10.6,25.15,89.93,112.21,222.63
05:00,-55.79,267.68,105.92,-161.76,0.29,4508.96,-6360.78,114.19,43.95,98.35,114.19,43.95,98.35,78.71,322.8,720.62,80.79,345.76,780.57,114.19,43.95,98.35,81.11,338.66,728.51
06:00,-3.36,325.55,161.09,-164.46,-0.01,626.94,-932.73,89.39,1452.28,2913.33,89.39,1452.28,2913.33,121.36,1838.53,3791.82,63.34,1093.19,2572.98,113.96,254.59,517.54,82.55,236.68,493.05
07:00,12.77,462.79,237.75,-225.04,0.32,-758.27,-11.21,30.0,1462.42,2924.85,30.0,1462.42,2924.85,143.7,6089.83,13971.32,24.4,1189.26,2378.51,101.99,296.59,643.82,57.88,981.51,2109.2
08:00,7.6,535.6,271.64,-263.96,0.04,600.29,-639.26,65.66,1260.35,2744.9,65.66,1260.35,2744.9,73.52,986.62,2062.23,50.68,883.26,1921.82,91.38,489.92,1136.24,68.46,299.13,660.63
09:00,109.71,609.21,359.46,-249.75,0.17,-2880.8,-204.44,-1.9,92.85,185.7,-1.9,92.85,185.7,25.9,321.77,664.25,-1.9,92.85,185.7,42.42,284.18,630.54,20.75,354.81,668.58
10:00,265.42,643.32,454.37,-188.95,0.23,567.1,-4252.14,-15.93,109.42,231.95,-15.93,109.42,231.95,-2.01,127.56,304.22,-13.72,184.89,432.08,-2.33,178.22,410.21,-11.55,133.64,325.58
11:00,147.22,631.38,389.3,-242.08,0.4,-3955.24,-3171.25,-19.48,221.52,470.06,-19.48,221.52,470.06,26.34,223.95,545.8,-13.04,386.25,783.25,-12.37,14.34,27.38,21.28,214.49,517.81
12:00,136.95,593.41,365.17,-228.24,0.51,-4783.88,-3040.01,-22.5,34.72,81.04,-22.5,34.72,81.04,32.3,308.2,734.61,0.0,0.0,0.0,-22.5,34.72,81.04,29.86,150.54,358.97
13:00,61.11,587.41,324.26,-263.15,0.59,-1861.37,-1578.0,-6.32,817.07,1640.95,-6.32,817.07,1640.95,-44.84,2973.84,6538.14,10.19,540.65,1122.49,-17.68,263.06,532.87,22.15,405.97,976.45
14:00,134.36,499.6,316.98,-182.62,0.62,-2357.44,-2424.65,-17.37,69.5,147.31,-17.37,69.5,147.31,21.38,348.93,813.19,0.0,0.0,0.0,-17.37,69.5,147.31,18.21,363.85,884.72
15:00,79.47,591.35,335.41,-255.94,0.66,318.61,-2063.77,-23.72,534.22,1192.25,-23.72,534.22,1192.25,-2.32,642.52,1569.59,-20.19,544.25,1239.7,-9.21,56.04,114.31,-15.67,817.25,1976.49
16:00,141.59,548.64,345.1,-203.54,0.67,648.81,-2412.09,-15.98,316.31,673.59,-15.98,316.31,673.59,-4.33,409.45,893.08,-15.15,329.26,673.59,9.31,233.65,525.47,-9.4,411.58,923.63
17:00,113.41,438.34,275.85,-162.49,0.6,-4914.88,-256.11,-1.17,56.9,113.81,-1.17,56.9,113.81,9.29,2083.24,4546.2,-1.17,56.9,113.81,26.21,219.22,489.87,41.61,525.07,1176.6
18:00,-84.71,416.69,166.01,-250.69,0.36,11160.14,-12466.85,102.86,1749.46,4002.9,102.86,1749.46,4002.9,123.37,566.17,1347.6,98.95,1661.09,3756.64,94.43,437.15,947.99,119.97,924.49,2139.6
19:00,-75.74,392.44,158.32,-234.13,0.22,7468.78,-9482.17,124.75,40.38,97.43,124.75,40.38,97.43,99.05,252.24,605.33,107.86,165.33,339.23,124.75,40.38,97.43,105.29,268.3,622.55
20:00,-17.5,320.75,151.63,-169.11,0.14,1674.73,-2491.21,142.07,89.39,196.93,142.07,89.39,196.93,95.77,348.07,844.25,102.14,98.15,225.67,142.07,89.39,196.93,70.94,1148.74,2357.56
21:00,4.51,275.86,140.17,-135.69,0.26,-342.37,-200.99,32.2,1569.33,3138.66,32.2,1569.33,3138.66,81.93,2192.4,4994.95,28.08,1368.5,2736.99,107.69,348.91,732.49,92.05,496.86,1188.24
22:00,-18.79,238.47,109.84,-128.63,0.06,2477.64,-2327.11,124.9,303.91,623.56,124.9,303.91,623.56,159.45,2125.08,4788.44,112.74,626.28,1281.62,113.8,62.69,141.15,111.7,670.62,1254.27
23:00,-51.51,214.03,81.24,-132.8,0.1,3451.32,-5546.56,78.73,1280.03,2622.68,78.73,1280.03,2622.68,90.37,1125.17,2707.84,69.26,1136.5,2426.28,98.62,313.55,684.4,74.53,558.21,1331.85

Deleted 4 parquet files from the cache.

(tradingagents) D:\TradingAgents-private\tradingagents\dataflows>C:\ProgramData\miniconda3\envs\tradingagents\python.exe d:/TradingAgents-private/tradingagents/dataflows/smard_client.py
Deleted 10 parquet files from the cache.

=== get_german_generation ===
Failed to fetch SMARD filter 1224: 404 Client Error: Not Found for url: https://www.smard.de/app/chart_data/1224/DE/1224_DE_hour_1777240800000.json
# DE-LU Generation by Type on 2026-04-28 (hour)
# Source: SMARD (Bundesnetzagentur)
# Unit: MW

Hour,Total,Wind Onshore,Wind Offshore,Solar,Lignite,Hard Coal,Gas,Pumped Storage,Hydro,Biomass,Other
00:00,43650.37,15770.97,2344.41,0.0,7635.19,4003.27,5963.71,517.53,1356.7,4186.96,1871.63
01:00,43537.74,16012.09,2126.1,0.0,7640.42,3968.5,5804.67,641.11,1337.11,4146.37,1861.37
02:00,42759.51,15577.76,1917.42,0.0,7764.59,3871.05,5777.56,572.26,1326.09,4128.83,1823.95
03:00,42612.42,15323.79,1678.29,0.0,7935.84,3871.57,5883.08,664.6,1309.66,4120.14,1825.45
04:00,43172.35,15597.73,1706.6,0.0,8083.3,3870.3,6162.75,461.03,1299.04,4145.66,1845.94
05:00,45452.55,16207.26,2293.24,16.07,8222.99,3861.93,6305.59,1142.01,1303.84,4237.15,1862.47
06:00,49074.98,16551.72,2859.35,1680.36,8040.83,3894.56,6367.37,2048.64,1352.81,4414.77,1864.57
07:00,52845.35,13845.56,2594.85,8345.49,7554.47,3884.55,5889.42,2967.22,1379.46,4499.45,1884.88
08:00,55431.05,9049.73,2086.46,19783.22,6783.66,3245.9,4656.55,2060.2,1352.03,4483.53,1929.77
09:00,59425.2,6663.03,1934.99,33204.97,4409.91,2038.4,3014.08,451.26,1378.19,4407.9,1922.47
10:00,65926.22,6401.55,1906.49,43190.32,3386.94,1394.46,2143.15,70.63,1346.23,4288.72,1797.73
11:00,70896.26,7577.58,1126.6,48275.64,3215.2,1197.4,2025.69,145.9,1363.68,4170.1,1798.47
12:00,71435.96,8390.82,663.72,48890.47,3206.46,1157.34,2008.95,69.41,1182.6,4058.62,1807.57
13:00,71272.94,8836.52,429.27,48709.0,3192.67,1079.71,2004.19,32.35,1173.32,4030.73,1785.18
14:00,69327.94,8924.18,520.52,46482.75,3306.6,1068.81,2005.04,54.54,1150.51,4041.69,1773.3
15:00,68209.74,11607.01,775.22,42237.23,3404.79,1116.27,2042.27,37.62,1140.32,4076.71,1772.3
16:00,64516.19,14819.56,1010.76,34612.5,3455.91,1173.43,2141.94,90.6,1318.27,4117.6,1775.62
17:00,61771.25,19071.93,2485.44,24973.09,3569.73,1535.38,2665.94,66.23,1315.15,4274.28,1814.08
18:00,57867.54,21541.21,3320.67,12741.32,5657.98,2587.89,3805.5,491.51,1354.39,4480.78,1886.29
19:00,55152.13,21240.43,3729.69,4007.52,6675.7,3294.97,4913.76,3467.98,1342.72,4582.34,1897.02
20:00,53280.06,21235.8,3730.0,342.14,6350.25,3363.72,5138.99,5231.78,1368.47,4608.94,1909.97
21:00,54335.35,23660.34,3820.41,1.79,6777.43,3617.8,5281.08,3349.22,1370.13,4551.88,1905.27
22:00,53018.61,23835.27,3593.57,0.43,6800.55,3761.99,5139.5,2213.77,1333.32,4434.07,1906.14
23:00,50092.68,23698.75,3036.29,0.23,6796.61,3795.96,4758.17,489.04,1301.56,4321.56,1894.51


=== get_german_residual_load ===
# DE-LU Residual Load on 2026-04-28 (hour)
# Source: SMARD (Bundesnetzagentur)
# Unit: MW (Load - Wind - Solar)

Hour,Residual Load MW
00:00,26523.46
01:00,24721.39
02:00,24986.16
03:00,25553.62
04:00,26718.0
05:00,29422.69
06:00,33633.23
07:00,33653.46
08:00,29443.52
09:00,17926.88
10:00,8414.22
11:00,1261.08
12:00,-1127.38
13:00,-2764.79
14:00,-2227.21
15:00,-1807.35
16:00,1863.9
17:00,7013.27
18:00,18097.43
19:00,28475.15
20:00,30380.28
21:00,27591.28
22:00,24240.93
23:00,21787.64


=== get_german_total_load ===
# DE-LU Total Load on 2026-04-28 (hour)
# Source: SMARD (Bundesnetzagentur)
# Unit: MW

Hour,Total Load MW
00:00,44638.85
01:00,42859.58
02:00,42481.34
03:00,42555.71
04:00,44022.33
05:00,47939.26
06:00,54724.66
07:00,58439.36
08:00,60362.93
09:00,59729.87
10:00,59912.58
11:00,58240.9
12:00,56817.62
13:00,55210.0
14:00,53700.24
15:00,52812.11
16:00,52306.72
17:00,53543.73
18:00,55700.63
19:00,57452.8
20:00,55688.22
21:00,55073.82
22:00,51670.2
23:00,48522.91


=== get_smard_prices ===
# Day-Ahead Prices for DE-LU on 2026-04-28 (hour)
# Source: SMARD (Bundesnetzagentur)
# Unit: EUR/MWh

Hour,Price EUR/MWh
00:00,112.66
01:00,106.9
02:00,102.98
03:00,102.83
04:00,105.28
05:00,111.84
06:00,122.1
07:00,121.43
08:00,112.32
09:00,79.78
10:00,21.82
11:00,-1.09
12:00,-14.04
13:00,-29.0
14:00,-29.01
15:00,-17.33
16:00,-4.66
17:00,33.32
18:00,90.1
19:00,117.4
20:00,120.97
21:00,115.83
22:00,111.3
23:00,101.77

# Day-Ahead Prices for CZ on 2026-04-28 (hour)
# Source: SMARD (Bundesnetzagentur)
# Unit: EUR/MWh

Hour,Price EUR/MWh
00:00,116.03
01:00,111.45
02:00,107.98
03:00,108.07
04:00,110.61
05:00,117.18
06:00,127.9
07:00,126.19
08:00,114.61
09:00,77.9
10:00,29.58
11:00,-0.04
12:00,-3.8
13:00,-14.2
14:00,-11.24
15:00,8.36
16:00,42.17
17:00,60.69
18:00,96.2
19:00,123.48
20:00,140.27
21:00,121.49
22:00,115.8
23:00,106.41


=== get_german_generation_forecast ===
# DE-LU Generation Forecast on 2026-04-28 (hour)
# Source: SMARD (Bundesnetzagentur)
# Unit: MW

Hour,Forecast Total,Forecast Wind Onshore,Forecast Wind Offshore,Forecast Solar,Forecast Combined Wind & Solar
00:00,41354.96,13995.89,1667.17,0.0,15663.07
01:00,40074.06,14328.72,1743.35,0.0,16072.07
02:00,39332.94,14484.91,1704.37,0.0,16189.28
03:00,39473.01,14504.25,1625.5,0.0,16129.75
04:00,39866.06,14597.78,1630.35,0.0,16228.14
05:00,41434.48,14823.32,1782.01,31.04,16636.37
06:00,45610.18,15177.46,1970.95,1552.47,18700.88
07:00,51736.26,14315.76,2063.44,7510.28,23889.48
08:00,55684.21,10899.03,1983.53,17728.81,30611.37
09:00,59431.01,8388.34,1973.77,29235.99,39598.1
10:00,66842.2,8375.32,1897.61,38994.84,49267.77
11:00,73233.79,8813.78,716.84,45088.87,54619.49
12:00,74672.58,9551.2,647.22,47927.78,58126.2
13:00,74324.05,10334.25,598.29,48476.94,59409.48
14:00,71400.29,11264.08,603.59,46383.79,58251.46
15:00,68814.74,12570.78,655.09,41738.7,54964.57
16:00,65048.94,14538.18,838.22,34743.51,50119.91
17:00,61786.49,16883.61,2205.85,24829.72,43919.17
18:00,57309.71,18221.82,2854.2,13031.17,34107.19
19:00,52636.6,18894.72,3532.24,4085.04,26512.01
20:00,51504.47,20185.61,3804.43,409.72,24399.75
21:00,51694.12,21915.63,3706.9,0.0,25622.53
22:00,50222.63,22033.6,3377.99,0.0,25411.59
23:00,47984.28,21416.9,2949.27,0.0,24366.17


=== get_german_load_forecast ===
# DE-LU Load Forecast on 2026-04-28 (hour)
# Source: SMARD (Bundesnetzagentur)
# Unit: MW

Hour,Load Forecast MW
00:00,46733.09
01:00,45201.84
02:00,44720.54
03:00,44963.49
04:00,45946.88
05:00,49067.28
06:00,54223.5
07:00,58587.63
08:00,61394.69
09:00,62743.04
10:00,62997.79
11:00,62753.25
12:00,61964.48
13:00,60249.77
14:00,58658.69
15:00,57435.41
16:00,57311.66
17:00,57862.04
18:00,58997.89
19:00,59513.95
20:00,58236.21
21:00,55762.69
22:00,52609.37
23:00,49367.71
"""
