"""OTE Czech Republic electricity market SOAP client.

OTE (Operátor trhu s elektřinou) operates the Czech electricity market.
This client fetches day-ahead prices, intraday continuous VWAP prices,
IDA auction results, and imbalance settlement data.

SOAP endpoint: http://www.ote-cr.cz/services/PublicDataService
WSDL: http://www.ote-cr.cz/services/PublicDataService/wsdl
No authentication required.

Reference: uzivatelskymanual_webove_sluzby_ote_g.pdf in project knowledge.
"""

import logging
import requests
from xml.etree import ElementTree as ET
from datetime import datetime, timedelta
from typing import Annotated, Optional, List, Dict
import pandas as pd

try:
    from .config import get_config
    from .energy_utils import format_price_table, get_cache_path
    from . import cache_layer
except ImportError:
    from config import get_config
    from energy_utils import format_price_table, get_cache_path
    import cache_layer

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(asctime)s - %(name)s - %(message)s',
    datefmt='%H:%M:%S'
)

OTE_NAMESPACE = "http://www.ote-cr.cz/schema/service/public"
OTE_SOAP_URL = "http://www.ote-cr.cz/services/PublicDataService"

_session = None


def _get_session() -> requests.Session:
    global _session
    if _session is None:
        _session = requests.Session()
        _session.headers.update({"Content-Type": "text/xml; charset=utf-8"})
    return _session


def _soap_request(method_name: str, params: Dict[str, str]) -> ET.Element:
    """Send a SOAP request to the OTE API and return the parsed XML response."""
    soap_envelope = f"""<?xml version="1.0" encoding="utf-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:pub="{OTE_NAMESPACE}">
  <soapenv:Header/>
  <soapenv:Body>
    <pub:{method_name}>
"""
    for key, value in params.items():
        soap_envelope += f"      <pub:{key}>{value}</pub:{key}>\n"
    soap_envelope += f"""    </pub:{method_name}>
  </soapenv:Body>
</soapenv:Envelope>"""

    try:
        response = _get_session().post(OTE_SOAP_URL, data=soap_envelope.encode('utf-8'), timeout=30)
        response.raise_for_status()
        root = ET.fromstring(response.content)

        body = root.find(".//{http://schemas.xmlsoap.org/soap/envelope/}Body")
        if body is None:
            body = root.find(".//soap:Body", {"soap": "http://schemas.xmlsoap.org/soap/envelope/"})

        if body is not None:
            for child in body:
                return child

        return root
    except requests.RequestException as e:
        logger.error(f"SOAP request failed for {method_name}: {e}")
        raise


def _parse_items(root: ET.Element) -> List[Dict[str, str]]:
    """Parse <Item>, <DamIndex>, or <IDAIndex> elements from an OTE SOAP response."""
    items = []
    # OTE uses different wrapper tags depending on the endpoint
    valid_tags = ("Item", "DamIndex", "IDAIndex")

    for elem in root.iter():
        if any(elem.tag.endswith(tag) for tag in valid_tags):
            item_data = {}
            for child in elem:
                tag = child.tag
                if "}" in tag:
                    tag = tag.split("}")[1]
                item_data[tag] = child.text if child.text else ""
            if item_data:
                items.append(item_data)
    return items


def _aggregate_to_hourly(df: pd.DataFrame) -> pd.DataFrame:
    """Safely converts OTE 15-min or hourly raw data into standardized hourly records to save LLM tokens."""
    if df.empty:
        return df

    # 1. Cast all known metric columns to numeric
    non_metric_cols = ['Date', 'PeriodResolution', 'PeriodInterval', 'Auction', 'Hour', 'PeriodIndex', 'Version']
    for col in df.columns:
        if col not in non_metric_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # 2. Extract standard hour labels depending on the data format (15min vs 60min)
    if 'PeriodIndex' in df.columns:
        res = df.get('PeriodResolution', pd.Series(['PT15M']*len(df))).iloc[0]
        if res == 'PT15M':
            # 15 min: Periods 1-4 = Hour 00:00
            df['Hour'] = ((pd.to_numeric(df['PeriodIndex']) - 1) // 4).apply(lambda x: f"{int(x):02d}:00")
        else:
            # 60 min
            df['Hour'] = (pd.to_numeric(df['PeriodIndex']) - 1).apply(lambda x: f"{int(x):02d}:00")
    elif 'Hour' in df.columns:
        # Legacy OTE hour indices go from 1 to 24 (or 25)
        df['Hour'] = (pd.to_numeric(df['Hour']) - 1).apply(lambda x: f"{int(x):02d}:00")

    if 'Hour' not in df.columns:
        return df

    # 3. Separate columns by their mathematical aggregation logic
    sum_cols = [c for c in df.columns if any(k in c for k in [
                                             'Volume', 'Import', 'Export', 'Saldo', 'Sum', 'Imbalance', 'Cost']) and 'Price' not in c and 'Rate' not in c]
    mean_cols = [c for c in df.columns if any(
        k in c for k in ['Price', 'EurRate', 'Index']) and c not in non_metric_cols]
    first_cols = [c for c in df.columns if c in non_metric_cols and c not in [
        'Hour', 'PeriodIndex', 'PeriodInterval', 'Auction']]

    # Group by Hour (and Auction if it exists) so multiple auctions don't get squashed
    group_cols = ['Hour']
    if 'Auction' in df.columns:
        group_cols.append('Auction')

    agg_dict = {}
    for c in df.columns:
        if c in group_cols:
            continue
        if c in sum_cols:
            agg_dict[c] = ['sum']
        elif c in mean_cols:
            # Capture the Anchor (mean), Stability (std), and Extremes (range)
            agg_dict[c] = [
                'mean', 
                'std', 
                ('Range', lambda x: x.max() - x.min())
            ]
        elif c in first_cols:
            agg_dict[c] = ['first']
        elif c == 'Emerg':
            agg_dict[c] = ['max']

    if agg_dict:
        # Aggregate and flatten the resulting MultiIndex columns
        df = df.groupby(group_cols).agg(agg_dict)
        
        new_cols = []
        for col, agg_func in df.columns:
            if agg_func in ['mean', 'sum', 'first', 'max']:
                new_cols.append(col)  # Preserve the primary anchor name
            elif agg_func == 'std':
                new_cols.append(f"{col}_StdDev")
            elif agg_func == 'Range':
                new_cols.append(f"{col}_Range")
            else:
                new_cols.append(f"{col}_{agg_func}")
        
        df.columns = new_cols
        df = df.reset_index()

    df = df.round(2)

    # 4. MATCH ENTSO-E FORMAT
    # Standardize column names to include units naturally
    rename_map = {
        'Price': 'Price EUR/MWh',
        'Volume': 'Volume MWh',
        'VolumeTotal': 'Volume MWh',
        'PriceCZ': 'Price EUR/MWh',
        'VolumeCZ': 'Volume MWh',
        'ImportCZ': 'Import MWh',
        'ExportCZ': 'Export MWh',
        'SaldoCZ': 'Saldo MWh',
        'SystemImbalance': 'System Imbalance MWh',
        'Sum': 'Absolute Imbalance Sum MWh',
        'PositiveImbalance': 'Positive Imbalance MWh',
        'NegativeImbalance': 'Negative Imbalance MWh',
        'RoundedImbalance': 'Rounded Imbalance MWh',
        'ReCost': 'Regulating Energy Cost EUR',
        'ImbalanceCost': 'Imbalance Cost EUR',
        'SettlImbalancePrice': 'Imbalance Price EUR/MWh',
        'SettlCounterImbalancePrice': 'Counter Imbalance Price EUR/MWh',
        'PriceWARE': 'Weighted Avg RE Price EUR/MWh',
        'PriceRE': 'Opposite Direction RE Price EUR/MWh',
        'PriceWAIM': 'Weighted Avg Intraday Price EUR/MWh',
        'PriceCurve': 'Base Curve Price EUR/MWh'
    }
    df = df.rename(columns=rename_map)

    # Safely keep only useful columns using positive matching (prevents KeyError)
    cols_to_drop = ['Date', 'PeriodResolution', 'PeriodInterval', 'PeriodIndex', 'HourlyPrice', 'Version']
    keep_cols = [c for c in df.columns if c not in cols_to_drop]
    df = df[keep_cols]

    # Set Hour as the actual index to mimic ENTSO-E CSV format perfectly
    if 'Hour' in df.columns:
        df = df.set_index('Hour')
        df.index.name = 'Hour (CET)'

    return df


def _format_ote_table(df: pd.DataFrame, title: str) -> str:
    """Format aggregated OTE data as a readable string table."""
    if df is None or df.empty:
        logger.warning(f"No data to format for {title}")
        return f"# {title}\n# No data available\n"

    header = f"# {title}\n"
    header += "# Source: OTE Czech Republic\n"
    header += "# Note: 15-minute periods have been aggregated into Hourly records\n\n"

    # Enable index=True to print the "Hour (CET)" index column
    return header + df.to_csv(index=True)


def get_official_exchange_rate(delivery_date: str) -> float:
    """Fetch the official EUR/CZK exchange rate from OTE DAM Index.
    Queries a 7-day window to ensure we find the most recent published rate.
    """
    try:
        # Query the past 7 days up to the delivery date
        dt = datetime.strptime(delivery_date, "%Y-%m-%d")
        start_date = (dt - timedelta(days=7)).strftime("%Y-%m-%d")

        params = {"StartDate": start_date, "EndDate": delivery_date}
        root = _soap_request("GetDamIndexE", params)
        items = _parse_items(root)

        # Extract all valid rates and return the last one (the most recent)
        valid_rates = [float(item["EurRate"]) for item in items if "EurRate" in item and item["EurRate"]]
        if valid_rates:
            return valid_rates[-1]

    except Exception as e:
        logger.warning(f"Failed to fetch exact EurRate from OTE, falling back to static rate: {e}")

    return 25  # Fallback static rate if API call fails or no valid rates found

# ─────────────────────────────────────────────
# DAY-AHEAD MARKET
# ─────────────────────────────────────────────


def get_dam_prices(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
) -> str:
    """Fetch Czech day-ahead hourly prices and volumes in EUR."""
    def fetch():
        # Handle API cutover dates dynamically per the OTE manual
        if delivery_date >= "2025-10-01":
            params = {
                "StartDate": delivery_date,
                "EndDate": delivery_date,
                "PeriodResolution": "PT15M"
                # Note: The modern GetDamPricePeriodE endpoint natively returns EUR
                # and does not accept the InEur parameter.
            }
            method = "GetDamPricePeriodE"
        else:
            params = {
                "StartDate": delivery_date,
                "EndDate": delivery_date,
                "InEur": "true",  # Hardcoded to EUR to maintain consistency
            }
            method = "GetDamPriceE"

        try:
            root = _soap_request(method, params)
            items = _parse_items(root)
            df = pd.DataFrame(items)
            return _aggregate_to_hourly(df)
        except Exception as e:
            logger.warning(f"Failed to get DAM prices for {delivery_date}: {e}")
            return pd.DataFrame()

    df = _load_or_fetch("ote", "dam_prices", "CZ", delivery_date, fetch)

    if df is None or df.empty:
        logger.warning(f"No day-ahead prices found for CZ on {delivery_date}")
        return f"# No day-ahead prices available for CZ on {delivery_date}"

    return _format_ote_table(df, f"Day-Ahead Prices for CZ on {delivery_date}")

# ─────────────────────────────────────────────
# INTRADAY CONTINUOUS MARKET
# ─────────────────────────────────────────────


def get_intraday_prices(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
) -> str:
    """Fetch Czech intraday continuous market prices."""
    def fetch():
        params = {
            "StartDate": delivery_date,
            "EndDate": delivery_date,
        }
        # The legacy ImPriceE API was deprecated in July 2024
        if delivery_date >= "2024-07-01":
            method = "GetImPricePeriodE"
        else:
            method = "GetImPriceE"

        try:
            root = _soap_request(method, params)
            items = _parse_items(root)
            df = pd.DataFrame(items)
            return _aggregate_to_hourly(df)
        except Exception as e:
            logger.warning(f"Failed to get intraday prices for {delivery_date}: {e}")
            return pd.DataFrame()

    df = _load_or_fetch("ote", "intraday_prices", "CZ", delivery_date, fetch)

    if df is None or df.empty:
        logger.warning(f"No intraday prices found for CZ on {delivery_date}")
        return f"# No intraday prices available for CZ on {delivery_date}"

    return _format_ote_table(df, f"Intraday Continuous Prices for CZ on {delivery_date}")


def get_intraday_prices_period(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
) -> str:
    """Fallback reference for tools calling the specific period fetcher."""
    # Since get_intraday_prices automatically aggregates periods to hours now,
    # we just map this request back to the primary function.
    return get_intraday_prices(delivery_date)


# ─────────────────────────────────────────────
# INTRADAY AUCTIONS (IDA)
# ─────────────────────────────────────────────

def get_ida_prices(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    auction: Annotated[Optional[str], "Auction type: 'IDA1', 'IDA2', or 'IDA3'. None for all."] = None,
) -> str:
    """Fetch IDA (Intraday Auction) results for Czech market."""
    def fetch():
        # OTE requires the Auction param. If None, we must query all 3 explicitly.
        auctions_to_fetch = [auction] if auction else ["IDA1", "IDA2", "IDA3"]
        method = "GetIDAAllPeriodE" if delivery_date >= "2024-06-14" else "GetIDAAllE"

        all_dfs = []
        for auc in auctions_to_fetch:
            params = {
                "StartDate": delivery_date,
                "EndDate": delivery_date,
                "InEur": "true",
                "Auction": auc
            }
            try:
                root = _soap_request(method, params)
                items = _parse_items(root)
                df = pd.DataFrame(items)
                if not df.empty:
                    all_dfs.append(df)
            except Exception as e:
                logger.warning(f"Failed to get {auc} prices for {delivery_date}: {e}")

        if not all_dfs:
            return pd.DataFrame()

        combined_df = pd.concat(all_dfs, ignore_index=True)
        return _aggregate_to_hourly(combined_df)

    query_type = f"ida_prices_{auction}" if auction else "ida_prices_all"
    df = _load_or_fetch("ote", query_type, "CZ", delivery_date, fetch)

    if df is None or df.empty:
        logger.warning(f"No IDA prices found for CZ on {delivery_date}")
        return f"# No IDA prices available for CZ on {delivery_date}"

    title = f"IDA Auction Prices for CZ on {delivery_date}" + (f" ({auction})" if auction else "")
    return _format_ote_table(df, title)

# ─────────────────────────────────────────────
# IMBALANCE SETTLEMENT
# ─────────────────────────────────────────────


def get_imbalance_settlement(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    version: Annotated[int, "Settlement version: 0=daily, 1=monthly, 2=final"] = 0,
) -> str:
    """Fetch Czech imbalance settlement data."""
    exchange_rate = get_official_exchange_rate(delivery_date)

    def fetch():
        params = {
            "StartDate": delivery_date,
            "EndDate": delivery_date,
            "Version": str(version),
        }
        if delivery_date >= "2024-07-01":
            method = "GetImbalanceSettlementPeriodE"
        else:
            method = "GetImbalanceSettlementE"

        try:
            root = _soap_request(method, params)
            items = _parse_items(root)
            df = pd.DataFrame(items)
            df = _aggregate_to_hourly(df)

            # --- CONVERT CZK TO EUR ---
            # These must exactly match the mapped English names from _aggregate_to_hourly
            czk_columns = [
                'Regulating Energy Cost EUR', 'Imbalance Cost EUR',
                'Imbalance Price EUR/MWh', 'Counter Imbalance Price EUR/MWh',
                'Weighted Avg RE Price EUR/MWh', 'Opposite Direction RE Price EUR/MWh',
                'Weighted Avg Intraday Price EUR/MWh', 'Base Curve Price EUR/MWh'
            ]
            for col in czk_columns:
                if col in df.columns:
                    df[col] = (df[col] / exchange_rate).round(2)

            return df
        except Exception as e:
            logger.warning(f"Failed to get imbalance settlement for {delivery_date}: {e}")
            return pd.DataFrame()

    df = _load_or_fetch("ote", f"imbalance_v{version}", "CZ", delivery_date, fetch)

    if df is None or df.empty:
        logger.warning(f"No imbalance settlement available for CZ on {delivery_date}")
        return f"# No imbalance settlement available for CZ on {delivery_date}"

    header = f"# Imbalance Settlement for CZ on {delivery_date} (v{version})\n"
    header += "# Source: OTE Czech Republic\n"
    header += "# Note: 15-minute periods have been aggregated into Hourly records\n"
    header += f"# Note: Financial values converted from CZK to EUR at official rate of {exchange_rate} CZK/EUR\n\n"

    # Enable index=True to print the "Hour (CET)" index column
    return header + df.to_csv(index=True)


def _load_or_fetch(source: str, query_type: str, market_area: str, date_str: str, fetch_fn):
    """Cache wrapper for OTE data."""
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


if __name__ == "__main__":
    import sys
    date = sys.argv[1] if len(sys.argv) > 1 else "2026-04-30"
    deleted_count = cache_layer.clear_cache(source="ote")
    print(f"Deleted {deleted_count} parquet files from the cache.")

    print("\n=== get_dam_prices ===")
    print(get_dam_prices(date))

    print("\n=== get_intraday_prices ===")
    print(get_intraday_prices(date))

    print("\n=== get_ida_prices ===")
    print(get_ida_prices(date))

    print("\n=== get_imbalance_settlement ===")
    print(get_imbalance_settlement(date, version=0))

"""
Reference output
=== get_dam_prices ===
# Day-Ahead Prices for CZ on 2026-04-30
# Source: OTE Czech Republic
# Note: 15-minute periods have been aggregated into Hourly records

Hour (CET),Price EUR/MWh,Price_StdDev,Price_Range,HourlyPrice_StdDev,HourlyPrice_Range,Volume MWh
00:00,107.71,3.13,6.91,0.0,0.0,3100.48
01:00,105.52,1.31,2.93,0.0,0.0,3065.05
02:00,103.63,1.82,3.84,0.0,0.0,3103.98
03:00,105.39,1.07,2.48,0.0,0.0,3149.32
04:00,110.02,5.21,11.53,0.0,0.0,3219.58
05:00,120.44,7.5,17.25,0.0,0.0,3282.98
06:00,132.12,11.56,25.45,0.0,0.0,3653.2
07:00,122.05,21.34,50.44,0.0,0.0,3708.35
08:00,101.18,36.49,82.75,0.0,0.0,3015.0
09:00,47.51,51.56,114.26,0.0,0.0,2971.52
10:00,0.24,1.26,3.02,0.0,0.0,2907.9
11:00,-2.5,3.21,7.07,0.0,0.0,2949.7
12:00,-13.47,6.15,14.76,0.0,0.0,3122.42
13:00,-27.55,4.27,9.61,0.0,0.0,3198.5
14:00,-21.05,4.83,11.7,0.0,0.0,3192.75
15:00,-8.07,5.6,13.14,0.0,0.0,2970.08
16:00,1.83,5.63,13.49,0.0,0.0,2741.8
17:00,39.89,45.2,94.86,0.0,0.0,2656.98
18:00,103.43,40.84,95.49,0.0,0.0,2516.2
19:00,145.36,30.81,70.61,0.0,0.0,2709.48
20:00,170.52,12.31,28.29,0.0,0.0,3679.65
21:00,131.6,28.18,64.5,0.0,0.0,3305.52
22:00,120.92,11.45,25.95,0.0,0.0,2815.15
23:00,111.6,6.29,13.9,0.0,0.0,2688.95


=== get_intraday_prices ===
# Intraday Continuous Prices for CZ on 2026-04-30
# Source: OTE Czech Republic
# Note: 15-minute periods have been aggregated into Hourly records

Hour (CET),Price EUR/MWh,Price_StdDev,Price_Range,Volume MWh
00:00,106.68,0.15,0.35,500.12
01:00,106.67,0.4,0.91,320.85
02:00,104.88,0.28,0.6,341.5
03:00,106.22,1.14,2.53,336.22
04:00,113.46,1.32,2.69,297.32
05:00,119.36,3.41,8.33,476.67
06:00,136.39,5.69,12.35,915.28
07:00,130.14,7.71,17.46,1371.52
08:00,106.98,13.62,31.4,803.42
09:00,55.44,27.79,63.36,991.0
10:00,15.37,4.12,9.08,719.9
11:00,1.7,0.79,1.64,917.8
12:00,-4.51,0.19,0.46,1179.18
13:00,3.47,2.13,4.47,1180.05
14:00,-13.74,1.22,2.98,1647.52
15:00,-0.21,1.18,2.74,1125.8
16:00,5.04,2.96,6.12,866.48
17:00,25.09,13.57,30.01,850.72
18:00,95.13,13.01,29.45,841.0
19:00,134.38,6.52,14.5,2292.67
20:00,160.32,2.02,4.33,1771.12
21:00,134.96,6.43,15.09,1393.92
22:00,117.68,1.83,4.4,1588.38
23:00,107.22,1.71,4.16,1769.58


=== get_ida_prices ===
# IDA Auction Prices for CZ on 2026-04-30
# Source: OTE Czech Republic
# Note: 15-minute periods have been aggregated into Hourly records

Hour (CET),Auction,Price EUR/MWh,PriceCZ_StdDev,PriceCZ_Range,Volume MWh,Import MWh,Export MWh,Saldo MWh
00:00,IDA1,103.7,2.9,6.28,40.4,-22.9,0.68,-22.22
00:00,IDA2,105.3,2.69,5.87,106.5,-53.88,107.28,53.4
01:00,IDA1,101.73,0.62,1.27,34.0,-18.0,0.75,-17.25
01:00,IDA2,103.62,4.23,9.86,109.0,-55.2,131.52,76.32
02:00,IDA1,99.88,1.3,3.0,37.5,-8.85,9.88,1.03
02:00,IDA2,101.8,1.3,2.77,115.3,-16.12,82.62,66.5
03:00,IDA1,103.56,5.02,8.8,44.0,-20.85,34.17,13.32
03:00,IDA2,100.82,1.01,2.19,108.2,-13.75,70.75,57.0
04:00,IDA1,109.1,1.57,3.57,53.3,-74.22,106.15,31.92
04:00,IDA2,103.5,3.26,7.68,58.7,-124.82,72.97,-51.85
05:00,IDA1,121.76,8.45,18.58,42.2,-31.65,64.25,32.6
05:00,IDA2,113.3,7.71,17.91,48.1,-162.82,118.6,-44.22
06:00,IDA1,132.84,9.54,20.81,27.4,-27.75,31.38,3.62
06:00,IDA2,125.44,6.72,14.06,412.2,-46.12,422.12,376.0
07:00,IDA1,118.29,18.76,43.78,37.3,-29.62,8.12,-21.5
07:00,IDA2,115.0,17.66,42.55,406.2,0.0,390.35,390.35
08:00,IDA1,92.64,26.66,63.03,50.7,-224.3,216.62,-7.68
08:00,IDA2,91.68,28.48,65.65,39.0,-71.92,85.25,13.32
09:00,IDA1,44.74,41.12,91.45,45.0,-72.6,72.45,-0.15
09:00,IDA2,38.88,39.85,89.47,31.4,-51.15,43.05,-8.1
10:00,IDA1,11.0,7.34,15.0,753.2,-668.18,0.0,-668.18
10:00,IDA2,12.0,1.52,3.68,279.4,-245.2,0.0,-245.2
11:00,IDA1,9.0,2.36,5.44,683.0,-598.67,0.0,-598.67
11:00,IDA2,-0.73,2.97,6.79,419.0,-495.88,83.02,-412.85
12:00,IDA1,1.0,5.37,12.46,505.8,-409.02,0.0,-409.02
12:00,IDA2,2.4,6.83,16.23,457.6,-446.62,0.0,-446.62
12:00,IDA3,-4.67,3.07,7.45,45.7,-116.52,72.7,-43.82
13:00,IDA1,-11.0,1.58,3.47,406.0,-315.58,0.0,-315.58
13:00,IDA2,0.0,0.85,2.07,261.4,-236.38,0.0,-236.38
13:00,IDA3,-12.02,3.64,8.32,221.7,-277.45,57.42,-220.02
14:00,IDA1,-7.0,2.64,6.24,430.2,-331.4,0.0,-331.4
14:00,IDA2,-0.3,6.71,14.51,546.3,-523.78,0.0,-523.78
14:00,IDA3,-14.3,3.33,8.06,75.1,-146.15,73.78,-72.38
15:00,IDA1,3.0,5.55,12.78,634.9,-535.8,0.0,-535.8
15:00,IDA2,1.71,1.45,2.58,355.3,-344.58,6.72,-337.85
15:00,IDA3,-5.0,5.26,12.36,20.2,-46.2,28.6,-17.6
16:00,IDA1,19.0,18.98,41.87,298.7,-233.38,0.0,-233.38
16:00,IDA2,12.21,12.32,27.99,39.3,-15.95,10.65,-5.3
16:00,IDA3,5.61,7.76,17.07,21.8,-78.68,59.03,-19.65
17:00,IDA1,56.69,23.2,54.44,62.7,-30.38,83.12,52.75
17:00,IDA2,22.9,21.7,49.45,47.0,-144.62,116.05,-28.58
17:00,IDA3,14.52,29.55,64.92,99.8,-137.6,39.6,-98.0
18:00,IDA1,103.25,32.43,75.11,33.0,-12.82,7.2,-5.62
18:00,IDA2,86.1,34.71,81.82,36.4,-290.5,296.65,6.15
18:00,IDA3,88.6,32.36,76.14,8.9,-37.15,34.12,-3.02
19:00,IDA1,149.01,29.18,65.42,43.9,-32.52,34.9,2.38
19:00,IDA2,127.0,28.06,64.02,430.6,-33.9,435.8,401.9
19:00,IDA3,135.93,27.94,64.03,115.0,-56.48,161.1,104.62
20:00,IDA1,174.34,9.56,20.24,33.8,-0.8,1.35,0.55
20:00,IDA2,157.42,5.74,12.67,387.6,-267.4,619.55,352.15
20:00,IDA3,165.6,9.91,22.62,63.9,-91.38,148.75,57.38
21:00,IDA1,135.27,22.32,50.38,30.0,-27.52,24.9,-2.62
21:00,IDA2,131.38,24.69,57.0,529.4,-10.18,525.5,515.33
21:00,IDA3,135.53,23.05,53.44,15.1,-61.7,50.9,-10.8
22:00,IDA1,121.92,10.48,23.34,29.9,-41.82,48.22,6.4
22:00,IDA2,113.55,8.63,19.65,20.1,-77.6,75.2,-2.4
22:00,IDA3,118.43,6.89,15.78,11.0,-52.78,43.8,-8.98
23:00,IDA1,111.63,4.55,11.0,48.7,-49.12,55.92,6.8
23:00,IDA2,106.36,4.72,11.05,19.7,-68.25,56.25,-12.0
23:00,IDA3,111.98,3.84,8.56,10.1,-10.7,3.97,-6.72


=== get_imbalance_settlement ===
# Imbalance Settlement for CZ on 2026-04-30 (v0)
# Source: OTE Czech Republic
# Note: 15-minute periods have been aggregated into Hourly records
# Note: Financial values converted from CZK to EUR at official rate of 24.36 CZK/EUR

Hour (CET),System Imbalance MWh,Absolute Imbalance Sum MWh,Positive Imbalance MWh,Negative Imbalance MWh,Rounded Imbalance MWh,Regulating Energy Cost EUR,Imbalance Cost EUR,Imbalance Price EUR/MWh,SettlImbalancePrice_StdDev,SettlImbalancePrice_Range,Counter Imbalance Price EUR/MWh,SettlCounterImbalancePrice_StdDev,SettlCounterImbalancePrice_Range,Weighted Avg RE Price EUR/MWh,PriceWARE_StdDev,PriceWARE_Range,Opposite Direction RE Price EUR/MWh,PriceRE_StdDev,PriceRE_Range,Weighted Avg Intraday Price EUR/MWh,PriceWAIM_StdDev,PriceWAIM_Range,Base Curve Price EUR/MWh,PriceCurve_StdDev,PriceCurve_Range
00:00,-109.54,264.52,77.48,-187.04,-0.14,12126.78,-14279.81,132.86,196.43,446.12,132.86,196.43,446.12,117.98,588.49,1316.41,130.85,149.67,359.55,116.94,3.65,8.69,123.87,530.23,1184.0
01:00,-54.8,275.22,110.21,-165.01,-0.07,3343.25,-6414.25,116.93,9.67,22.22,116.93,9.67,22.22,46.45,585.31,1402.03,77.98,524.82,1218.98,116.93,9.67,22.22,61.85,288.6,681.9
02:00,-53.23,235.08,90.96,-144.12,-0.13,4071.52,-6120.61,115.14,6.86,14.67,115.14,6.86,14.67,72.12,668.95,1578.27,86.44,843.38,1876.46,115.14,6.86,14.67,74.41,694.4,1642.2
03:00,-44.97,232.36,93.73,-138.63,-0.07,4728.68,-5219.55,116.49,27.83,61.66,116.49,27.83,61.66,103.65,213.14,447.07,108.62,74.41,165.41,116.49,27.83,61.66,106.5,215.07,450.82
04:00,-46.97,278.85,115.95,-162.9,0.01,5555.56,-6022.21,126.94,147.59,322.59,126.94,147.59,322.59,114.68,371.7,738.44,118.01,331.52,776.35,123.71,32.14,65.5,117.14,406.51,815.35
05:00,-151.87,364.41,106.26,-258.15,-0.08,19007.73,-20492.35,134.27,147.45,330.18,134.27,147.45,330.18,124.42,215.02,506.31,124.45,179.54,416.55,129.62,83.16,202.92,133.02,207.67,452.32
06:00,-172.6,415.77,121.61,-294.16,0.01,25755.55,-27890.31,156.53,342.8,735.58,156.53,342.8,735.58,146.6,224.82,491.62,146.79,238.01,516.68,146.65,138.54,300.74,156.53,342.8,735.58
07:00,-121.0,345.01,112.02,-232.99,0.15,18053.87,-19448.49,167.88,601.03,1334.09,167.88,601.03,1334.09,160.66,996.55,2350.24,156.49,808.32,1913.48,140.4,187.77,425.36,163.32,748.1,1778.29
08:00,-89.11,400.4,155.6,-244.79,0.05,12039.27,-13502.21,103.23,1744.96,3967.71,103.23,1744.96,3967.71,104.58,1061.82,2565.5,99.79,1671.3,3705.64,112.11,561.94,1264.84,105.15,1262.48,3020.7
09:00,41.83,383.39,212.61,-170.78,-0.21,395.28,-1581.13,21.25,1035.18,2070.36,21.25,1035.18,2070.36,25.02,574.88,1229.22,21.25,1035.18,2070.36,50.31,789.32,1581.93,29.72,720.4,1514.85
10:00,44.17,484.18,264.16,-220.02,-0.09,-366.18,-276.71,-11.34,389.27,845.69,-11.34,389.27,845.69,7.72,1026.62,2326.82,-10.79,394.57,839.45,5.11,100.54,221.26,-2.88,687.8,1669.74
11:00,13.41,426.88,220.15,-206.74,-0.52,-287.57,-243.22,17.47,798.77,1637.4,17.47,798.77,1637.4,76.86,2648.52,5385.85,18.97,754.02,1572.2,1.69,307.4,539.98,22.46,608.53,1275.35
12:00,-4.07,371.27,183.56,-187.71,-0.1,356.8,-221.89,27.81,865.65,2025.64,27.81,865.65,2025.64,122.92,3229.67,6589.69,31.1,733.36,1661.11,0.62,250.15,506.02,38.27,551.44,1274.79
13:00,-70.39,509.81,219.72,-290.09,-0.22,3794.08,-5771.2,38.5,969.61,2054.96,38.5,969.61,2054.96,40.37,688.37,1465.29,40.25,897.25,1846.98,8.6,281.69,608.66,54.36,559.56,1133.06
14:00,7.08,447.17,227.14,-220.03,-0.39,-640.09,-283.36,2.12,755.47,1339.77,2.12,755.47,1339.77,67.1,2155.64,5157.56,14.37,404.39,717.4,-13.74,309.86,572.67,36.3,711.38,1667.53
15:00,-4.21,441.53,218.7,-222.83,-0.23,876.75,-677.6,34.31,791.82,1885.05,34.31,791.82,1885.05,42.87,1184.7,2873.28,36.31,663.5,1609.22,4.92,260.07,548.79,42.51,445.75,1086.22
16:00,15.91,456.96,236.45,-220.51,-0.02,-2401.51,-291.97,-4.93,385.72,932.5,-4.93,385.72,932.5,13.15,2763.17,5957.11,30.3,1894.13,4179.44,-0.1,202.7,461.72,53.97,1724.96,3703.67
17:00,60.4,544.0,302.2,-241.8,0.05,-1985.94,-1189.43,-12.32,357.47,707.66,-12.32,357.47,707.66,30.3,202.3,488.4,-12.32,357.47,707.66,14.83,330.49,731.06,31.62,296.66,623.21
18:00,-83.41,604.03,260.34,-343.69,-0.36,7018.9,-9796.52,110.54,350.03,760.96,110.54,350.03,760.96,84.17,257.17,488.74,97.28,497.9,1063.8,105.4,316.84,717.5,89.2,300.93,604.66
19:00,-70.05,582.58,256.3,-326.28,-0.5,8959.99,-10269.78,144.65,158.81,353.19,144.65,158.81,353.19,138.21,581.62,1309.41,120.83,375.72,858.44,144.65,158.81,353.19,122.84,478.7,1108.16
20:00,-111.86,538.92,213.53,-325.39,-0.39,13034.41,-19078.68,170.59,49.3,105.59,170.59,49.3,105.59,114.74,189.11,379.26,121.43,330.3,705.71,170.59,49.3,105.59,121.36,189.29,359.74
21:00,-149.47,485.53,168.05,-317.49,-0.24,15999.67,-21930.7,145.22,156.71,367.58,145.22,156.71,367.58,106.21,173.1,388.57,115.23,119.23,274.54,145.22,156.71,367.58,113.62,227.24,512.52
22:00,-13.85,282.15,134.12,-148.03,-0.14,1613.2,-2308.18,96.1,1561.26,3173.55,96.1,1561.26,3173.55,103.17,572.96,1326.41,81.68,1334.55,2799.45,122.82,262.57,570.03,98.73,345.91,645.87
23:00,-38.46,294.09,127.79,-166.3,-0.14,3441.72,-4518.71,117.48,41.74,101.34,117.48,41.74,101.34,89.68,166.04,353.75,86.03,128.17,263.57,117.48,41.74,101.34,88.2,144.18,331.62
"""
