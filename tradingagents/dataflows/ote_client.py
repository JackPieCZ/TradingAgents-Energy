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
    from . import cache_layer
except ImportError:
    import cache_layer

logger = logging.getLogger(__name__)

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

    # 1. Extract standard hour labels depending on the data format (15min vs 60min)
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

    # 2. MATCH ENTSO-E FORMAT BEFORE AGGREGATION
    # Standardize column names to include units naturally so aggregation inherits them
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

    # 3. Drop useless raw columns BEFORE they trigger pointless aggregations
    cols_to_drop = ['Date', 'PeriodResolution', 'PeriodInterval', 'PeriodIndex', 'HourlyPrice', 'Version']
    df = df.drop(columns=[c for c in cols_to_drop if c in df.columns])

    # 4. Cast to numeric safely
    non_metric_cols = ['Auction', 'Hour']
    for col in df.columns:
        if col not in non_metric_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # 5. Separate columns by their mathematical aggregation logic
    sum_cols = [c for c in df.columns if any(k in c for k in [
                                             'Volume', 'Import', 'Export', 'Saldo', 'Sum', 'Imbalance', 'Cost']) and 'Price' not in c and 'Rate' not in c]
    mean_cols = [c for c in df.columns if any(
        k in c for k in ['Price', 'Rate', 'Index']) and c not in non_metric_cols]
    first_cols = [c for c in df.columns if c in non_metric_cols and c not in ['Hour', 'Auction']]

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
        elif c == 'Emerg':
            agg_dict[c] = ['max']
        else:
            agg_dict[c] = ['first']

    if agg_dict:
        # Aggregate and flatten the resulting MultiIndex columns
        df = df.groupby(group_cols).agg(agg_dict)

        new_cols = []
        for col, agg_func in df.columns:
            if agg_func in ['mean', 'sum', 'first', 'max']:
                new_cols.append(col)  # Preserve the primary anchor name
            elif agg_func == 'std':
                new_cols.append(f"{col} StdDev")
            elif agg_func == 'Range':
                new_cols.append(f"{col} Range")
            else:
                new_cols.append(f"{col} {agg_func}")

        df.columns = new_cols
        df = df.reset_index()

    df = df.round(2)

    # 6. Clean up flat variance columns dynamically (i.e. zero standard deviation logic)
    variance_cols = [c for c in df.columns if 'StdDev' in c or 'Range' in c]
    for c in variance_cols:
        if df[c].fillna(0).eq(0).all():
            df = df.drop(columns=[c])

    # 7. Set Hour as the actual index to mimic ENTSO-E CSV format perfectly
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
    market_area: Annotated[str, "Bidding zone, e.g. 'CZ'"] = "CZ",
) -> str:
    """Fetch Czech day-ahead hourly prices and volumes in EUR."""
    if market_area.upper() != "CZ":
        logger.warning(f"OTE client only supports CZ market area. Requested: {market_area}")
        return f"# No day-ahead prices available for {market_area} on {delivery_date} (OTE only supports CZ)"

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

    df = cache_layer._load_or_fetch("ote", "dam_prices", market_area.upper(), delivery_date, fetch)

    if df is None or df.empty:
        logger.warning(f"No day-ahead prices found for {market_area} on {delivery_date}")
        return f"# No day-ahead prices available for {market_area} on {delivery_date}"

    return _format_ote_table(df, f"Day-Ahead Prices for {market_area.upper()} on {delivery_date}")

# ─────────────────────────────────────────────
# INTRADAY CONTINUOUS MARKET
# ─────────────────────────────────────────────


def get_intraday_prices(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    market_area: Annotated[str, "Bidding zone, e.g. 'CZ'"] = "CZ",
) -> str:
    """Fetch Czech intraday continuous market prices."""
    if market_area.upper() != "CZ":
        logger.warning(f"OTE client only supports CZ market area. Requested: {market_area}")
        return f"# No intraday prices available for {market_area} on {delivery_date} (OTE only supports CZ)"

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

    df = cache_layer._load_or_fetch("ote", "intraday_prices", market_area.upper(), delivery_date, fetch)

    if df is None or df.empty:
        logger.warning(f"No intraday prices found for {market_area} on {delivery_date}")
        return f"# No intraday prices available for {market_area} on {delivery_date}"

    return _format_ote_table(df, f"Intraday Continuous Prices for {market_area.upper()} on {delivery_date}")


def get_intraday_prices_period(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    market_area: Annotated[str, "Bidding zone, e.g. 'CZ'"] = "CZ",
) -> str:
    """Fallback reference for tools calling the specific period fetcher."""
    # Since get_intraday_prices automatically aggregates periods to hours now,
    # we just map this request back to the primary function.
    return get_intraday_prices(delivery_date, market_area)


# ─────────────────────────────────────────────
# INTRADAY AUCTIONS (IDA)
# ─────────────────────────────────────────────

def get_ida_prices(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    auction: Annotated[Optional[str], "Auction type: 'IDA1', 'IDA2', or 'IDA3'. None for all."] = None,
    market_area: Annotated[str, "Bidding zone, e.g. 'CZ'"] = "CZ",
) -> str:
    """Fetch IDA (Intraday Auction) results for Czech market."""
    if market_area.upper() != "CZ":
        logger.warning(f"OTE client only supports CZ market area. Requested: {market_area}")
        return f"# No IDA prices available for {market_area} on {delivery_date} (OTE only supports CZ)"

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
    df = cache_layer._load_or_fetch("ote", query_type, market_area.upper(), delivery_date, fetch)

    if df is None or df.empty:
        logger.warning(f"No IDA prices found for {market_area} on {delivery_date}")
        return f"# No IDA prices available for {market_area} on {delivery_date}"

    title = f"IDA Auction Prices for {market_area.upper()} on {delivery_date}" + (f" ({auction})" if auction else "")
    return _format_ote_table(df, title)

# ─────────────────────────────────────────────
# IMBALANCE SETTLEMENT
# ─────────────────────────────────────────────


def get_imbalance_settlement(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    version: Annotated[int, "Settlement version: 0=daily, 1=monthly, 2=final"] = 0,
    market_area: Annotated[str, "Bidding zone, e.g. 'CZ'"] = "CZ",
) -> str:
    """Fetch Czech imbalance settlement data."""
    if market_area.upper() != "CZ":
        logger.warning(f"OTE client only supports CZ market area. Requested: {market_area}")
        return f"# No imbalance settlement available for {market_area} on {delivery_date} (OTE only supports CZ)"

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

    df = cache_layer._load_or_fetch("ote", f"imbalance_v{version}", market_area.upper(), delivery_date, fetch)

    if df is None or df.empty:
        logger.warning(f"No imbalance settlement available for {market_area} on {delivery_date}")
        return f"# No imbalance settlement available for {market_area} on {delivery_date}"

    header = f"# Imbalance Settlement for {market_area.upper()} on {delivery_date} (v{version})\n"
    header += "# Source: OTE Czech Republic\n"
    header += "# Note: 15-minute periods have been aggregated into Hourly records\n"
    header += f"# Note: Financial values converted from CZK to EUR at official rate of {exchange_rate} CZK/EUR\n\n"

    # Enable index=True to print the "Hour (CET)" index column
    return header + df.to_csv(index=True)


if __name__ == "__main__":
    import sys
    date = sys.argv[1] if len(sys.argv) > 1 else "2026-04-28"
    deleted_count = cache_layer.clear_cache(source="ote")
    print(f"Deleted {deleted_count} parquet files from the cache.")
    logging.basicConfig(
        level=logging.INFO,
        format='[%(levelname)s] %(asctime)s - %(name)s - %(message)s',
        datefmt='%H:%M:%S'
    )

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
"""
