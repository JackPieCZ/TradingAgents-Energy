"""ENTSO-E Transparency Platform data client.

Uses the entsoe-py library (already installed).
API docs: https://transparency.entsoe.eu/content/static_content/Static%20content/web%20api/Guide.html
entsoe-py docs: https://github.com/EnergieID/entsoe-py

Data available:
- Day-ahead prices (hourly, all EU bidding zones)
- Generation forecasts (wind onshore/offshore, solar, by TSO area)
- Actual generation (by type: wind, solar, gas, coal, nuclear, hydro, etc.)
- Load forecasts and actuals
- Cross-border physical flows
- Generation unit outages (REMIT UMMs)
- Imbalance prices
"""

import os
import logging
from datetime import datetime, timedelta
from typing import Annotated, Optional
import pandas as pd

from dotenv import load_dotenv
import requests_cache
from retry_requests import retry
from entsoe.entsoe import EntsoePandasClient
from entsoe.exceptions import NoMatchingDataError, InvalidBusinessParameterError

try:
    from .ote_client import get_official_exchange_rate
    from .config import get_config
    from .energy_utils import (
        get_entsoe_area_code,
        delivery_date_to_entsoe_period,
        handle_dst_transition,
        format_price_table,
        get_cache_path,
        CET,
    )
    from . import cache_layer
except ImportError:
    from ote_client import get_official_exchange_rate
    from config import get_config
    from energy_utils import (
        get_entsoe_area_code,
        delivery_date_to_entsoe_period,
        handle_dst_transition,
        format_price_table,
        get_cache_path,
        CET,
    )
    import cache_layer

load_dotenv()

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(asctime)s - %(name)s - %(message)s',
    datefmt='%H:%M:%S'
)


class Pandas2EntsoeWrapper:
    """
    Wraps EntsoePandasClient to bypass the pandas 2.0+ timezone inference bug.
    Forces start/end parameters to UTC before querying, preventing the 'Inferred 
    time zone not equal to passed time zone' error, and restores the original 
    timezone (CET/Europe/Berlin) on the returned data.
    """

    def __init__(self, client):
        self._client = client

    def __getattr__(self, name):
        attr = getattr(self._client, name)
        if not callable(attr) or not name.startswith('query_'):
            return attr

        def wrapper(*args, **kwargs):
            new_args = list(args)
            orig_tz = None

            # Intercept kwargs
            if 'start' in kwargs and hasattr(kwargs['start'], 'tz'):
                orig_tz = kwargs['start'].tz
                kwargs['start'] = kwargs['start'].tz_convert('UTC')
            if 'end' in kwargs and hasattr(kwargs['end'], 'tz'):
                orig_tz = orig_tz or kwargs['end'].tz
                kwargs['end'] = kwargs['end'].tz_convert('UTC')

            # Intercept positional args
            for i, val in enumerate(new_args):
                if hasattr(val, 'tz') and isinstance(val, pd.Timestamp):
                    orig_tz = orig_tz or val.tz
                    new_args[i] = val.tz_convert('UTC')

            # Make the API call using UTC bounds
            result = attr(*new_args, **kwargs)

            # Re-localize index to original timezone
            if result is not None and hasattr(result, 'index') and isinstance(result.index, pd.DatetimeIndex):
                if result.index.tz is not None and orig_tz is not None:
                    result = result.tz_convert(orig_tz)

            return result
        return wrapper


_client = None


def _get_client() -> EntsoePandasClient:
    """Create and return an ENTSO-E client with the configured API key and retry logic."""
    global _client
    if _client is not None:
        return _client

    api_key = os.environ.get("ENTSOE_API_KEY")
    if not api_key:
        config = get_config()
        api_key = config.get("entsoe_api_key")

    if not api_key:
        raise ValueError(
            "ENTSOE_API_KEY not found in environment or config. "
            "Set ENTSOE_API_KEY env var or 'entsoe_api_key' in config."
        )

    # Inject a retry session to perfectly handle ENTSO-E 503 Rate Limits
    cache_session = requests_cache.CachedSession('.entsoe_cache', expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.5)

    base_client = EntsoePandasClient(api_key=api_key, session=retry_session)
    # Wrap the client to fix pandas 2.0+ timezone crash
    _client = Pandas2EntsoeWrapper(base_client)
    return _client


def _load_or_fetch(source: str, query_type: str, market_area: str, date_str: str, fetch_fn):
    """Generic cache wrapper: check cache first, call fetch_fn on miss, save result."""
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


def _format_index(df: pd.DataFrame, resample_hourly: bool = True) -> pd.DataFrame:
    """Format DatetimeIndex, resample to save LLM tokens, and calculate variance metrics."""
    if df is not None and not df.empty and isinstance(df.index, pd.DatetimeIndex):
        if resample_hourly:
            agg_dict = {}
            for col in df.columns:
                # Selectively apply variance only to volatile financial/system metrics
                if any(k in col for k in ['Price', 'Imbalance']):
                    agg_dict[col] = ['mean', 'std', ('Range', lambda x: x.max() - x.min())]
                else:
                    # For Load, Generation, and Flows, the mean anchor is sufficient
                    agg_dict[col] = ['mean']

            resampled = df.resample('1h').agg(agg_dict)

            # Flatten the MultiIndex columns
            new_cols = []
            for col, agg_func in resampled.columns:
                if agg_func == 'mean':
                    new_cols.append(col)
                elif agg_func == 'std':
                    new_cols.append(f"{col} StdDev")
                elif agg_func == 'Range':
                    new_cols.append(f"{col} Range")

            resampled.columns = new_cols
            df = resampled

        df = df.round(3)  # Round to 3 decimals for cleaner display
        df.index = df.index.strftime('%H:%M')
        df.index.name = "Hour"
    return df


# ─────────────────────────────────────────────
# PRICE DATA
# ─────────────────────────────────────────────


def query_day_ahead_prices(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    market_area: Annotated[str, "Bidding zone, e.g. 'DE-LU' or 'CZ'"],
) -> str:
    """Fetch day-ahead auction prices for a given date and bidding zone."""
    def fetch():
        client = _get_client()
        area_code = get_entsoe_area_code(market_area)
        start, end = delivery_date_to_entsoe_period(delivery_date)
        try:
            series = client.query_day_ahead_prices(area_code, start=start, end=end)
            if isinstance(series, pd.Series):
                df = series.to_frame(name="Price EUR/MWh")
            else:
                df = pd.DataFrame(series)
                df.columns = ["Price EUR/MWh"]

            df.index.name = "Delivery Hour (CET)"
            return handle_dst_transition(df)
        except NoMatchingDataError:
            logger.warning(f"No day-ahead prices for {market_area} on {delivery_date}")
            return pd.DataFrame(columns=["Price EUR/MWh"])

    df = _load_or_fetch("entsoe", "day_ahead_prices", market_area, delivery_date, fetch)
    if df is None or df.empty:
        logger.warning(f"No day-ahead prices available for {market_area} on {delivery_date}")
        return f"# No day-ahead prices available for {market_area} on {delivery_date}"

    df = _format_index(df.copy())
    header = f"# Day-Ahead Prices for {market_area} on {delivery_date}\n# Source: ENTSO-E Transparency Platform\n# Unit: EUR/MWh\n\n"
    return header + df.to_csv()


def query_intraday_prices(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    market_area: Annotated[str, "Bidding zone, e.g. 'DE-LU' or 'CZ'"],
    auction_sequence: Annotated[Optional[int], "Intraday auction number: 1, 2, or 3. None for all."] = None,
) -> str:
    """Fetch intraday auction prices (XBID/CIDAR) for a given date and zone."""
    def fetch():
        client = _get_client()
        area_code = get_entsoe_area_code(market_area)
        start, end = delivery_date_to_entsoe_period(delivery_date)

        if auction_sequence is not None:
            try:
                series = client.query_intraday_prices(area_code, start=start, end=end, sequence=auction_sequence)
                df = series.to_frame(
                    name=f"IDA{auction_sequence} Price EUR/MWh") if isinstance(series, pd.Series) else pd.DataFrame(series)
                df.index.name = "Delivery Hour (CET)"
                return handle_dst_transition(df)
            except NoMatchingDataError:
                logger.warning(
                    f"No intraday prices for sequence {auction_sequence} in {market_area} on {delivery_date}")
                return pd.DataFrame()

        all_auctions = {}
        for seq in [1, 2, 3]:
            try:
                series = client.query_intraday_prices(area_code, start=start, end=end, sequence=seq)
                if not series.empty:
                    all_auctions[f"IDA{seq}"] = series
            except (NoMatchingDataError, InvalidBusinessParameterError):
                logger.warning(f"No intraday prices for sequence {seq} in {market_area} on {delivery_date}")
                continue

        if not all_auctions:
            logger.warning(f"No intraday prices available for {market_area} on {delivery_date}")
            return pd.DataFrame()

        df = pd.DataFrame(all_auctions)
        df.index.name = "Delivery Hour (CET)"
        return handle_dst_transition(df)

    df = _load_or_fetch("entsoe", "intraday_prices", market_area, delivery_date, fetch)
    if df is None or df.empty:
        logger.warning(f"No intraday prices available for {market_area} on {delivery_date}")
        return f"# No intraday prices available for {market_area} on {delivery_date}"

    df = _format_index(df.copy())
    header = f"# Intraday Auction Prices for {market_area} on {delivery_date}\n# Source: ENTSO-E (XBID)\n# Unit: EUR/MWh\n\n"
    return header + df.to_csv()


# ─────────────────────────────────────────────
# GENERATION FORECASTS (wind, solar)
# ─────────────────────────────────────────────

def query_wind_solar_forecast(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    market_area: Annotated[str, "Bidding zone, e.g. 'DE-LU' or 'CZ'"],
) -> str:
    """Fetch day-ahead wind and solar generation forecasts."""
    def fetch():
        client = _get_client()
        area_code = get_entsoe_area_code(market_area)
        start, end = delivery_date_to_entsoe_period(delivery_date)
        try:
            df = client.query_wind_and_solar_forecast(area_code, start=start, end=end)
            if df.empty:
                logger.warning(f"No wind/solar forecast data for {market_area} on {delivery_date}")
                return pd.DataFrame()

            if isinstance(df, pd.Series):
                df = df.to_frame(name=df.name or "Total Renewable")

            df = df.copy()
            wind_on = df["Wind Onshore"].fillna(0) if "Wind Onshore" in df.columns else pd.Series(0, index=df.index)
            wind_off = df["Wind Offshore"].fillna(0) if "Wind Offshore" in df.columns else pd.Series(0, index=df.index)
            solar = df["Solar"].fillna(0) if "Solar" in df.columns else pd.Series(0, index=df.index)

            df["Wind Total MW"] = wind_on + wind_off
            df["Solar MW"] = solar
            df["Total Renewable MW"] = df["Wind Total MW"] + df["Solar MW"]

            # Keep only the aggregated columns to save LLM tokens as requested by Phase 1
            df = df[["Wind Total MW", "Solar MW", "Total Renewable MW"]]
            df.index.name = "Hour (CET)"
            return handle_dst_transition(df)
        except NoMatchingDataError:
            logger.warning(f"No wind/solar forecast found for {market_area} on {delivery_date}")
            return pd.DataFrame()

    df = _load_or_fetch("entsoe", "wind_solar_forecast", market_area, delivery_date, fetch)
    if df is None or df.empty:
        logger.warning(f"No wind/solar forecast available for {market_area} on {delivery_date}")
        return f"# No wind/solar forecast available for {market_area} on {delivery_date}"

    df = _format_index(df.copy())
    header = f"# Wind & Solar Day-Ahead Forecast for {market_area} on {delivery_date}\n# Source: ENTSO-E (TSO forecasts)\n# Unit: MW\n\n"
    return header + df.to_csv()


def query_actual_generation(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    market_area: Annotated[str, "Bidding zone, e.g. 'DE-LU' or 'CZ'"],
) -> str:
    """Fetch actual generation by production type for a given date."""
    def fetch():
        client = _get_client()
        area_code = get_entsoe_area_code(market_area)
        start, end = delivery_date_to_entsoe_period(delivery_date)
        try:
            df = client.query_generation(area_code, start=start, end=end, psr_type=None)
            if df.empty:
                logger.warning(f"No actual generation data for {market_area} on {delivery_date}")
                return pd.DataFrame()

            if isinstance(df.columns, pd.MultiIndex):
                df.columns = [
                    f"{col[0]} (Consumption)" if col[1] == "Actual Consumption" else f"{col[0]}"
                    for col in df.columns
                ]

            df = df.fillna(0)
            df.index.name = "Hour (CET)"
            return handle_dst_transition(df)
        except NoMatchingDataError:
            logger.warning(f"No actual generation found for {market_area} on {delivery_date}")
            return pd.DataFrame()

    df = _load_or_fetch("entsoe", "actual_generation", market_area, delivery_date, fetch)
    if df is None or df.empty:
        logger.warning(f"No generation data available for {market_area} on {delivery_date}")
        return f"# No generation data available for {market_area} on {delivery_date}"

    df = _format_index(df.copy())
    header = f"# Actual Generation by Type for {market_area} on {delivery_date}\n# Source: ENTSO-E\n# Unit: MW\n\n"
    return header + df.to_csv()


def query_generation_forecast_updates(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    market_area: Annotated[str, "Bidding zone, e.g. 'DE-LU' or 'CZ'"],
) -> str:
    """Fetch updated (intraday) wind and solar forecasts and compute deltas."""
    def fetch():
        client = _get_client()
        area_code = get_entsoe_area_code(market_area)
        start, end = delivery_date_to_entsoe_period(delivery_date)

        try:
            da_raw = client.query_wind_and_solar_forecast(area_code, start=start, end=end)
            da_forecast = da_raw.to_frame(name="Total Generation") if isinstance(da_raw, pd.Series) else da_raw
        except NoMatchingDataError:
            logger.warning(f"No day-ahead generation forecast found for {market_area} on {delivery_date}")
            da_forecast = pd.DataFrame()

        try:
            id_raw = client.query_generation_forecast(area_code, start=start, end=end)
            id_forecast = id_raw.to_frame(name="Total Generation") if isinstance(id_raw, pd.Series) else id_raw
        except (NoMatchingDataError, InvalidBusinessParameterError):
            logger.warning(f"No intraday generation forecast found for {market_area} on {delivery_date}")
            id_forecast = pd.DataFrame()

        if da_forecast.empty and id_forecast.empty:
            logger.warning(f"No generation forecast data (day-ahead or intraday) for {market_area} on {delivery_date}")
            return pd.DataFrame()

        result = pd.DataFrame(index=da_forecast.index if not da_forecast.empty else id_forecast.index)
        result.index.name = "Hour (CET)"

        # Safely map Day-Ahead columns
        result["DA Wind Onshore"] = da_forecast.get("Wind Onshore", pd.Series(
            dtype=float)) if not da_forecast.empty else pd.Series(dtype=float)
        result["DA Wind Offshore"] = da_forecast.get("Wind Offshore", pd.Series(
            dtype=float)) if not da_forecast.empty else pd.Series(dtype=float)
        result["DA Solar"] = da_forecast.get("Solar", pd.Series(
            dtype=float)) if not da_forecast.empty else pd.Series(dtype=float)

        # Safely map Intraday columns
        if not id_forecast.empty:
            result["ID Wind Onshore"] = id_forecast.get("Wind Onshore", result["DA Wind Onshore"])
            result["ID Wind Offshore"] = id_forecast.get("Wind Offshore", result["DA Wind Offshore"])
            result["ID Solar"] = id_forecast.get("Solar", result["DA Solar"])
        else:
            result["ID Wind Onshore"] = result["DA Wind Onshore"]
            result["ID Wind Offshore"] = result["DA Wind Offshore"]
            result["ID Solar"] = result["DA Solar"]

        # CRITICAL FIX: If Intraday has NaNs for specific hours, fallback to Day-Ahead for those exact hours
        result["ID Wind Onshore"] = result["ID Wind Onshore"].fillna(result["DA Wind Onshore"])
        result["ID Wind Offshore"] = result["ID Wind Offshore"].fillna(result["DA Wind Offshore"])
        result["ID Solar"] = result["ID Solar"].fillna(result["DA Solar"])

        # Now it is safe to fill any remaining absolute gaps with 0
        result = result.fillna(0)

        result["Wind Delta"] = (result["ID Wind Onshore"] + result["ID Wind Offshore"]) - \
                               (result["DA Wind Onshore"] + result["DA Wind Offshore"])
        result["Solar Delta"] = result["ID Solar"] - result["DA Solar"]

        # Token saving logic: Check if all deltas are exactly zero (indicative of missing ID data falling back to DA)
        is_fallback = (result["Wind Delta"] == 0).all() and (result["Solar Delta"] == 0).all()

        if is_fallback:
            # Drop the redundant Intraday and Delta columns to save LLM tokens
            cols_to_drop = ["ID Wind Onshore", "ID Wind Offshore", "ID Solar", "Wind Delta", "Solar Delta"]
            result = result.drop(columns=[c for c in cols_to_drop if c in result.columns])

        return handle_dst_transition(result)

    df = _load_or_fetch("entsoe", "generation_forecast_updates", market_area, delivery_date, fetch)
    if df is None or df.empty:
        logger.warning(f"No forecast updates available for {market_area} on {delivery_date}")
        return f"# No forecast updates available for {market_area} on {delivery_date}"

    # Determine if it was a fallback based on the cached/returned df columns
    is_fallback_df = "Wind Delta" not in df.columns

    df = _format_index(df.copy())
    header = f"# Forecast Updates for {market_area} on {delivery_date}\n# Source: ENTSO-E\n"

    if is_fallback_df:
        header += "# WARNING: Intraday forecast updates unavailable. Displaying Day-Ahead baseline only.\n# Unit: MW\n\n"
    else:
        header += "# Unit: MW (delta = intraday_forecast - day_ahead_forecast)\n\n"

    return header + df.to_csv()

# ─────────────────────────────────────────────
# LOAD DATA
# ─────────────────────────────────────────────


def query_load_forecast(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    market_area: Annotated[str, "Bidding zone, e.g. 'DE-LU' or 'CZ'"],
) -> str:
    """Fetch day-ahead load (demand) forecast."""
    def fetch():
        client = _get_client()
        area_code = get_entsoe_area_code(market_area)
        start, end = delivery_date_to_entsoe_period(delivery_date)
        try:
            series = client.query_load_forecast(area_code, start=start, end=end)
            if isinstance(series, pd.Series):
                df = series.to_frame(name="Load Forecast MW")
            elif isinstance(series, pd.DataFrame):
                df = series.rename(columns={series.columns[0]: "Load Forecast MW"})
            else:
                df = pd.DataFrame({"Load Forecast MW": [series]}, index=[start])

            df.index.name = "Hour (CET)"
            return handle_dst_transition(df)
        except NoMatchingDataError:
            logger.warning(f"No load forecast found for {market_area} on {delivery_date}")
            return pd.DataFrame(columns=["Load Forecast MW"])

    df = _load_or_fetch("entsoe", "load_forecast", market_area, delivery_date, fetch)
    if df is None or df.empty:
        logger.warning(f"No load forecast available for {market_area} on {delivery_date}")
        return f"# No load forecast available for {market_area} on {delivery_date}"

    df = _format_index(df.copy())
    header = f"# Load Forecast for {market_area} on {delivery_date}\n# Source: ENTSO-E\n# Unit: MW\n\n"
    return header + df.to_csv()


def query_actual_load(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    market_area: Annotated[str, "Bidding zone, e.g. 'DE-LU' or 'CZ'"],
) -> str:
    """Fetch actual total load."""
    def fetch():
        client = _get_client()
        area_code = get_entsoe_area_code(market_area)
        start, end = delivery_date_to_entsoe_period(delivery_date)
        try:
            series = client.query_load(area_code, start=start, end=end)
            if isinstance(series, pd.Series):
                df = series.to_frame(name="Actual Load MW")
            elif isinstance(series, pd.DataFrame):
                df = series.rename(columns={series.columns[0]: "Actual Load MW"})
            else:
                df = pd.DataFrame({"Actual Load MW": [series]}, index=[start])

            df.index.name = "Hour (CET)"
            return handle_dst_transition(df)
        except NoMatchingDataError:
            logger.warning(f"No actual load data found for {market_area} on {delivery_date}")
            return pd.DataFrame(columns=["Actual Load MW"])

    df = _load_or_fetch("entsoe", "actual_load", market_area, delivery_date, fetch)
    if df is None or df.empty:
        logger.warning(f"No actual load data available for {market_area} on {delivery_date}")
        return f"# No actual load data available for {market_area} on {delivery_date}"

    df = _format_index(df.copy())
    header = f"# Actual Load for {market_area} on {delivery_date}\n# Source: ENTSO-E\n# Unit: MW\n\n"
    return header + df.to_csv()


# ─────────────────────────────────────────────
# CROSS-BORDER FLOWS
# ─────────────────────────────────────────────

_NEIGHBOR_MAP = {
    "DE-LU": ["AT", "FR", "NL", "PL", "CZ", "DK1", "DK2", "CH"],
    "CZ": ["DE-LU", "AT", "PL", "SK"],
    "AT": ["DE-LU", "CZ", "IT", "SI", "CH"],
    "PL": ["DE-LU", "CZ", "SE", "LT"],
}


def query_crossborder_flows(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    market_area: Annotated[str, "Bidding zone, e.g. 'DE-LU' or 'CZ'"],
) -> str:
    """Fetch cross-border physical flows for a bidding zone."""
    def fetch():
        client = _get_client()
        area_code = get_entsoe_area_code(market_area)
        start, end = delivery_date_to_entsoe_period(delivery_date)

        neighbors = _NEIGHBOR_MAP.get(market_area, [])
        result_data = {}

        for neighbor in neighbors:
            try:
                neighbor_code = get_entsoe_area_code(neighbor)

                # Fetch actual physical flows
                flows = client.query_crossborder_flows(area_code, neighbor_code, start=start, end=end)

                # Fetch maximum allowed capacity (NTC)
                has_ntc = False
                try:
                    ntc = client.query_net_transfer_capacity_dayahead(area_code, neighbor_code, start=start, end=end)
                    has_ntc = True
                except NoMatchingDataError:
                    # In Flow-Based Market Coupling regions (like CZ/DE), bilateral NTC is not published.
                    logger.debug(f"No bilateral NTC data for {market_area}-{neighbor}. Skipping congestion calc.")

                if not flows.empty:
                    border_df = pd.DataFrame({f"{neighbor} Flow": flows})

                    if has_ntc:
                        border_df[f"{neighbor} Capacity"] = ntc
                        capacity_safe = border_df[f"{neighbor} Capacity"].replace(0, pd.NA)
                        border_df[f"{neighbor} Congestion %"] = (
                            border_df[f"{neighbor} Flow"].abs() / capacity_safe) * 100
                    else:
                        logger.debug(f"No NTC data for {market_area}-{neighbor}. Congestion % will not be calculated.")

                    # Fill NaNs back to 0, but only for existing columns
                    border_df = border_df.fillna(0).round(1)
                    result_data[neighbor] = border_df
                else:
                    logger.warning(f"No flow data between {market_area} and {neighbor} on {delivery_date}")

            except (NoMatchingDataError, InvalidBusinessParameterError):
                logger.warning(f"No cross-border flow data between {market_area} and {neighbor} on {delivery_date}")
                continue

        if not result_data:
            logger.warning(f"No cross-border flow data for {market_area} on {delivery_date}")
            return pd.DataFrame()

        # Combine all the individual border DataFrames
        result_df = pd.concat(result_data.values(), axis=1)

        # Ffill propagates lower-resolution data to match higher-resolution data
        result_df = result_df.ffill().fillna(0)

        # Calculate the total Net Import based only on the Flow columns
        flow_cols = [col for col in result_df.columns if "Flow" in col]
        result_df["Net Import MW"] = result_df[flow_cols].sum(axis=1)
        result_df.index.name = "Hour (CET)"

        return handle_dst_transition(result_df)

    df = _load_or_fetch("entsoe", "crossborder_flows", market_area, delivery_date, fetch)
    if df is None or df.empty:
        logger.warning(f"No cross-border flow data available for {market_area} on {delivery_date}")
        return f"# No cross-border flow data for {market_area} on {delivery_date}"

    df = _format_index(df.copy())
    header = f"# Cross-Border Flows for {market_area} on {delivery_date}\n# Source: ENTSO-E\n# Positive = import into {market_area}, Negative = export\n# Unit: MW\n\n"
    return header + df.to_csv()


# ─────────────────────────────────────────────
# OUTAGES (REMIT UMMs)
# ─────────────────────────────────────────────

def query_outages(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    market_area: Annotated[str, "Bidding zone, e.g. 'DE-LU' or 'CZ'"],
) -> str:
    """Fetch generation unit unavailabilities (planned and unplanned outages)."""
    def fetch():
        client = _get_client()
        area_code = get_entsoe_area_code(market_area)
        start, end = delivery_date_to_entsoe_period(delivery_date)
        try:
            df = client.query_unavailability_of_generation_units(area_code, start=start, end=end)
            if df.empty:
                logger.warning(f"No outage data for {market_area} on {delivery_date}")
                return pd.DataFrame()
            return df
        except NoMatchingDataError:
            logger.warning(f"No outage data found for {market_area} on {delivery_date}")
            return pd.DataFrame()

    df = _load_or_fetch("entsoe", "outages", market_area, delivery_date, fetch)
    if df is None or df.empty:
        logger.warning(f"No outage data available for {market_area} on {delivery_date}")
        return f"# No outage data for {market_area} on {delivery_date}"

    cols_to_keep = ['plant_type', 'production_resource_name', 'nominal_capacity', 'available_capacity', 'start', 'end']
    avail_cols = [c for c in cols_to_keep if c in df.columns]
    df_clean = df[avail_cols].copy()

    if 'production_resource_name' in df_clean.columns and 'start' in df_clean.columns and 'end' in df_clean.columns:
        df_clean = df_clean.drop_duplicates(subset=['production_resource_name', 'start', 'end'])

    # Safely convert returned localized timestamps to CET string formats
    if 'start' in df_clean.columns:
        df_clean['start'] = pd.to_datetime(df_clean['start'], utc=True).dt.tz_convert(
            'Europe/Berlin').dt.strftime('%Y-%m-%d %H:%M')
    if 'end' in df_clean.columns:
        df_clean['end'] = pd.to_datetime(df_clean['end'], utc=True).dt.tz_convert(
            'Europe/Berlin').dt.strftime('%Y-%m-%d %H:%M')

    summary = f"# Generation Outages for {market_area} on {delivery_date}\n# Source: ENTSO-E (REMIT UMMs)\n# Unit: MW unavailable\n\n"

    # Calculate the unavailable MW if capacity data is present
    if "available_capacity" in df_clean.columns and "nominal_capacity" in df_clean.columns:
        df_clean["unavailable_MW"] = df_clean["nominal_capacity"].fillna(0) - df_clean["available_capacity"].fillna(0)
        total_unavail = df_clean["unavailable_MW"].sum()
        summary += f"Total unavailable capacity: {total_unavail:.0f} MW\n\n"

    # Sort by the start time to get the most recent outages (newest first)
    if "start" in df_clean.columns:
        df_clean = df_clean.sort_values(by="start", ascending=False)

    # df_clean = df_clean.head(30)

    summary += df_clean.to_string(index=False)
    return summary


# ─────────────────────────────────────────────
# IMBALANCE / BALANCING
# ─────────────────────────────────────────────

def query_imbalance_prices(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    market_area: Annotated[str, "Bidding zone, e.g. 'DE-LU' or 'CZ'"],
) -> str:
    """Fetch imbalance (balancing energy) prices and volumes."""
    def fetch():
        client = _get_client()
        area_code = get_entsoe_area_code(market_area)
        start, end = delivery_date_to_entsoe_period(delivery_date)

        # 1. Fetch Imbalance Prices
        try:
            price_df = client.query_imbalance_prices(area_code, start=start, end=end)
        except NoMatchingDataError:
            logger.warning(f"No imbalance price data found for {market_area} on {delivery_date}")
            price_df = pd.DataFrame()

        # 2. Fetch Imbalance Volumes (Physical system state indicator)
        try:
            vol_df = client.query_imbalance_volumes(area_code, start=start, end=end)

            # CRITICAL FIX: Convert Series to DataFrame safely before checking columns
            if isinstance(vol_df, pd.Series):
                vol_df = vol_df.to_frame(name="Imbalance Volume MW")

            # Flatten multi-index if ENTSO-E returns one for volumes
            if not vol_df.empty and isinstance(vol_df.columns, pd.MultiIndex):
                vol_df.columns = [f"{col[0]} {col[1]}" for col in vol_df.columns]
        except (NoMatchingDataError, InvalidBusinessParameterError):
            logger.warning(f"No imbalance volume data found for {market_area} on {delivery_date}")
            vol_df = pd.DataFrame()

        if price_df.empty and vol_df.empty:
            logger.warning(f"No imbalance price or volume data for {market_area} on {delivery_date}")
            return pd.DataFrame()

        # 3. Combine Prices and Volumes safely on the DatetimeIndex
        df = pd.concat([price_df, vol_df], axis=1)

        # 4. Clean up single-imbalance pricing markets (like CZ)
        # Round first to kill microscopic floating-point noise before comparing
        df = df.round(3)
        if "Long" in df.columns and "Short" in df.columns:
            if df["Long"].equals(df["Short"]):
                df["Imbalance Price EUR/MWh"] = df["Long"]
                df = df.drop(columns=["Long", "Short"])

        df.index.name = "Hour (CET)"
        return handle_dst_transition(df)

    # Note: Changed cache key to 'imbalance_data' since it now holds both price and volume
    df = _load_or_fetch("entsoe", "imbalance_data", market_area, delivery_date, fetch)
    if df is None or df.empty:
        logger.warning(f"No imbalance data available for {market_area} on {delivery_date}")
        return f"# No imbalance data for {market_area} on {delivery_date}"

    # Currency conversion for CZ
    exchange_rate = None
    if market_area.upper() == "CZ" and not df.empty:
        exchange_rate = get_official_exchange_rate(delivery_date)
        for col in df.columns:
            if "Price" in col or "Cost" in col or "EUR" in col:
                df[col] = (df[col] / exchange_rate).round(3)

    df = _format_index(df.copy())
    
    header = f"# Imbalance Prices and Volumes for {market_area} on {delivery_date}\n# Source: ENTSO-E\n# Unit: EUR/MWh (Prices), MW (Volumes)\n"
    if exchange_rate is not None:
        header += f"# Note: Financial values converted from CZK to EUR at official rate of {exchange_rate} CZK/EUR\n"
    header += "\n"
    
    return header + df.to_csv()


# ─────────────────────────────────────────────
# RESIDUAL LOAD
# ─────────────────────────────────────────────

def query_residual_load(
    delivery_date: Annotated[str, "Delivery date in YYYY-MM-DD format"],
    market_area: Annotated[str, "Bidding zone, e.g. 'DE-LU' or 'CZ'"],
) -> str:
    """Fetch residual load (load - wind - solar) forecast."""
    def fetch():
        client = _get_client()
        area_code = get_entsoe_area_code(market_area)
        start, end = delivery_date_to_entsoe_period(delivery_date)

        try:
            load = client.query_load_forecast(area_code, start=start, end=end)
            if isinstance(load, pd.DataFrame):
                load = load.iloc[:, 0]
        except (NoMatchingDataError, Exception) as e:
            logger.warning(f"Residual Load - Failed to fetch load: {e}")
            load = pd.Series(dtype=float)

        try:
            wind_solar = client.query_wind_and_solar_forecast(area_code, start=start, end=end)
        except (NoMatchingDataError, Exception) as e:
            logger.warning(f"Residual Load - Failed to fetch wind/solar: {e}")
            wind_solar = pd.DataFrame()

        if load.empty:
            logger.warning(f"No load forecast data for {market_area} on {delivery_date}, cannot compute residual load")
            return pd.DataFrame()

        result = pd.DataFrame(index=load.index)
        result["Load Forecast MW"] = load

        if not wind_solar.empty:
            wind_total = pd.Series(0, index=wind_solar.index)
            if "Wind Onshore" in wind_solar.columns:
                wind_total += wind_solar["Wind Onshore"].fillna(0)
            if "Wind Offshore" in wind_solar.columns:
                wind_total += wind_solar["Wind Offshore"].fillna(0)

            solar = wind_solar["Solar"].fillna(
                0) if "Solar" in wind_solar.columns else pd.Series(0, index=wind_solar.index)

            wind_total = wind_total.reindex(load.index, method='ffill')
            solar = solar.reindex(load.index, method='ffill')

            result["Wind MW"] = wind_total
            result["Solar MW"] = solar
            result["Residual Load MW"] = result["Load Forecast MW"] - wind_total - solar
        else:
            result["Residual Load MW"] = result["Load Forecast MW"]

        result.index.name = "Hour (CET)"
        return handle_dst_transition(result)

    df = _load_or_fetch("entsoe", "residual_load", market_area, delivery_date, fetch)
    if df is None or df.empty:
        logger.warning(f"No residual load data available for {market_area} on {delivery_date}")
        return f"# No residual load data for {market_area} on {delivery_date}"

    df = _format_index(df.copy())
    header = f"# Residual Load Forecast for {market_area} on {delivery_date}\n# Source: ENTSO-E (calculated: Load - Wind - Solar)\n# Unit: MW\n\n"
    return header + df.to_csv()


if __name__ == "__main__":
    import sys
    import os
    from dotenv import load_dotenv

    load_dotenv()

    date = sys.argv[1] if len(sys.argv) > 1 else "2026-04-30"
    market_area = sys.argv[2] if len(sys.argv) > 2 else "CZ"

    print(f"Testing ENTSO-E for date: {date}, market: {market_area}")
    print(f"ENTSOE_API_KEY set: {'ENTSOE_API_KEY' in os.environ}")

    if "ENTSOE_API_KEY" not in os.environ:
        print("ERROR: ENTSOE_API_KEY not set. Set it in .env or environment.")
        sys.exit(1)

    try:
        deleted_count = cache_layer.clear_cache(source="entsoe")
        print(f"Deleted {deleted_count} parquet files from the ENTSO-E cache.")
    except Exception as e:
        logger.warning(f"Error clearing cache: {e}")
        pass

    print("\n=== query_day_ahead_prices ===")
    print(query_day_ahead_prices(date, market_area))

    print("\n=== query_intraday_prices ===")
    print(query_intraday_prices(date, market_area))

    print("\n=== query_wind_solar_forecast ===")
    print(query_wind_solar_forecast(date, market_area))

    print("\n=== query_actual_generation ===")
    print(query_actual_generation(date, market_area))

    print("\n=== query_generation_forecast_updates ===")
    print(query_generation_forecast_updates(date, market_area))

    print("\n=== query_load_forecast ===")
    print(query_load_forecast(date, market_area))

    print("\n=== query_actual_load ===")
    print(query_actual_load(date, market_area))

    print("\n=== query_crossborder_flows ===")
    print(query_crossborder_flows(date, market_area))

    print("\n=== query_outages ===")
    print(query_outages(date, market_area))

    print("\n=== query_imbalance_prices ===")
    print(query_imbalance_prices(date, market_area))

    print("\n=== query_residual_load ===")
    print(query_residual_load(date, market_area))

"""
Reference output
=== query_day_ahead_prices ===
# Day-Ahead Prices for CZ on 2026-04-30
# Source: ENTSO-E Transparency Platform
# Unit: EUR/MWh

Hour,Price EUR/MWh,Price EUR/MWh StdDev,Price EUR/MWh Range
00:00,107.708,3.127,6.91
01:00,105.52,1.311,2.93
02:00,103.63,1.82,3.84
03:00,105.39,1.073,2.48
04:00,110.015,5.205,11.53
05:00,120.438,7.495,17.25
06:00,132.122,11.562,25.45
07:00,122.05,21.34,50.44
08:00,101.178,36.495,82.75
09:00,47.508,51.564,114.26
10:00,0.24,1.264,3.02
11:00,-2.498,3.212,7.07
12:00,-13.472,6.148,14.76
13:00,-27.553,4.265,9.61
14:00,-21.048,4.832,11.7
15:00,-8.075,5.601,13.14
16:00,1.832,5.629,13.49
17:00,39.89,45.195,94.86
18:00,103.428,40.841,95.49
19:00,145.36,30.808,70.61
20:00,170.52,12.305,28.29
21:00,131.602,28.178,64.5
22:00,120.915,11.447,25.95
23:00,111.598,6.292,13.9
00:00,119.49,,0.0


=== query_intraday_prices ===
[WARNING] 23:31:41 - __main__ - No intraday prices for sequence 1 in CZ on 2026-04-30
[WARNING] 23:31:41 - __main__ - No intraday prices for sequence 2 in CZ on 2026-04-30
[WARNING] 23:31:41 - __main__ - No intraday prices for sequence 3 in CZ on 2026-04-30
[WARNING] 23:31:41 - __main__ - No intraday prices available for CZ on 2026-04-30
[WARNING] 23:31:41 - __main__ - No intraday prices available for CZ on 2026-04-30
# No intraday prices available for CZ on 2026-04-30

=== query_wind_solar_forecast ===
# Wind & Solar Day-Ahead Forecast for CZ on 2026-04-30
# Source: ENTSO-E (TSO forecasts)
# Unit: MW

Hour,Wind Total MW,Solar MW,Total Renewable MW
00:00,0.0,0.0,0.0
01:00,0.0,0.0,0.0
02:00,0.0,0.0,0.0
03:00,0.0,0.0,0.0
04:00,0.0,0.0,0.0
05:00,0.0,23.75,23.75
06:00,0.0,237.0,237.0
07:00,0.0,843.5,843.5
08:00,0.0,1713.5,1713.5
09:00,0.0,2460.0,2460.0
10:00,0.0,2932.0,2932.0
11:00,0.0,3168.25,3168.25
12:00,0.0,3236.0,3236.0
13:00,0.0,3207.0,3207.0
14:00,0.0,3027.25,3027.25
15:00,0.0,2658.25,2658.25
16:00,0.0,2110.5,2110.5
17:00,0.0,1374.25,1374.25
18:00,0.0,629.25,629.25
19:00,0.0,174.25,174.25
20:00,0.0,21.25,21.25
21:00,0.0,0.0,0.0
22:00,0.0,0.0,0.0
23:00,0.0,0.0,0.0


=== query_actual_generation ===
# Actual Generation by Type for CZ on 2026-04-30
# Source: ENTSO-E
# Unit: MW

Hour,Biomass,Fossil Brown coal/Lignite,Fossil Coal-derived gas,Fossil Gas,Fossil Hard coal,Fossil Oil,Hydro Pumped Storage,Hydro Pumped Storage (Consumption),Hydro Run-of-river and poundage,Hydro Water Reservoir,Nuclear,Other,Other renewable,Solar,Waste,Wind Onshore
00:00,296.608,2169.812,0.0,145.67,80.12,3.07,0.0,0.0,83.64,17.83,3531.705,68.492,271.398,0.0,32.328,81.512
01:00,292.298,2166.36,0.0,144.785,82.238,3.07,0.0,0.0,85.9,11.308,3535.442,68.625,271.232,0.0,32.168,71.53
02:00,292.278,2162.442,0.0,143.99,81.2,3.06,0.0,0.0,85.42,11.218,3538.708,69.058,270.698,0.0,32.548,62.01
03:00,293.382,2170.705,0.0,146.19,81.25,3.06,0.0,0.0,85.062,11.075,3539.1,69.195,270.435,0.0,31.762,56.495
04:00,293.51,2198.168,0.0,157.48,82.425,3.075,0.0,0.0,86.052,10.308,3541.37,67.96,272.422,12.725,32.03,50.732
05:00,300.315,2183.27,0.0,179.18,81.598,3.09,273.597,0.0,85.56,10.29,3539.43,66.095,275.828,64.68,32.525,49.97
06:00,306.403,2081.633,0.0,232.385,84.938,3.138,947.315,0.0,78.375,134.68,3539.112,59.778,285.265,215.69,32.75,54.422
07:00,307.975,2015.648,0.0,224.172,86.658,3.132,380.692,0.0,77.378,144.945,3538.998,60.048,284.8,838.055,32.475,43.758
08:00,300.712,1788.828,0.0,185.972,85.385,3.08,25.78,0.0,77.608,51.032,3539.24,64.662,275.255,1767.857,32.293,36.707
09:00,277.485,1325.68,0.0,158.445,70.64,3.018,12.402,59.978,80.6,61.105,3537.73,65.902,266.108,2562.312,31.518,57.432
10:00,263.615,836.335,0.0,131.522,66.082,2.94,0.0,1023.06,79.96,60.76,3536.21,67.22,256.555,3010.217,30.855,65.482
11:00,259.418,777.225,0.0,125.892,65.485,2.925,0.0,1113.89,78.798,51.855,3532.25,67.345,257.393,3234.472,30.762,57.062
12:00,261.832,771.235,0.0,128.475,69.092,2.928,0.0,1107.92,77.44,47.45,3532.418,67.42,257.725,3435.152,31.578,45.805
13:00,263.192,791.168,0.0,127.968,70.202,2.932,0.0,1099.815,77.135,47.988,3529.148,67.612,258.998,3448.217,31.565,51.232
14:00,262.875,748.402,0.0,125.278,68.228,2.92,0.0,1090.372,82.552,6.032,3526.57,67.392,257.872,3060.553,31.442,50.71
15:00,264.572,751.462,0.0,127.738,69.08,2.92,0.0,1034.875,82.468,11.735,3519.568,67.358,257.478,2704.062,33.385,52.465
16:00,261.758,770.605,0.0,129.447,69.25,2.93,0.0,351.702,81.922,12.112,3520.998,67.165,259.533,2106.322,33.48,51.718
17:00,266.835,917.848,0.0,136.962,71.718,2.962,0.0,0.0,83.155,13.008,3523.895,67.088,262.628,1395.065,33.81,58.802
18:00,288.758,1421.16,0.0,179.767,76.68,3.058,187.045,0.0,83.695,20.06,3523.87,64.16,275.332,616.865,35.02,60.405
19:00,297.87,1669.808,0.0,207.615,79.555,3.11,934.85,0.0,72.792,520.6,3523.087,60.918,282.878,178.04,35.528,49.59
20:00,297.82,1740.06,0.0,225.462,87.702,3.135,971.882,0.0,71.865,650.285,3524.705,58.832,286.508,74.575,35.755,43.728
21:00,294.895,1731.498,0.0,211.072,86.265,3.112,958.475,0.0,72.81,362.61,3522.48,60.748,281.862,4.668,35.49,43.42
22:00,287.597,1689.338,0.0,159.675,81.285,3.042,944.61,0.0,80.97,33.65,3522.81,66.622,270.595,0.0,34.752,38.768
23:00,284.415,1655.172,0.0,144.608,82.0,3.04,877.352,0.0,86.582,16.022,3525.188,67.712,269.7,0.0,34.555,37.38


=== query_generation_forecast_updates ===
# Forecast Updates for CZ on 2026-04-30
# Source: ENTSO-E
# WARNING: Intraday forecast updates unavailable. Displaying Day-Ahead baseline only.
# Unit: MW

Hour,DA Wind Onshore,DA Wind Offshore,DA Solar
00:00,0.0,0.0,0.0
01:00,0.0,0.0,0.0
02:00,0.0,0.0,0.0
03:00,0.0,0.0,0.0
04:00,0.0,0.0,0.0
05:00,0.0,0.0,23.75
06:00,0.0,0.0,237.0
07:00,0.0,0.0,843.5
08:00,0.0,0.0,1713.5
09:00,0.0,0.0,2460.0
10:00,0.0,0.0,2932.0
11:00,0.0,0.0,3168.25
12:00,0.0,0.0,3236.0
13:00,0.0,0.0,3207.0
14:00,0.0,0.0,3027.25
15:00,0.0,0.0,2658.25
16:00,0.0,0.0,2110.5
17:00,0.0,0.0,1374.25
18:00,0.0,0.0,629.25
19:00,0.0,0.0,174.25
20:00,0.0,0.0,21.25
21:00,0.0,0.0,0.0
22:00,0.0,0.0,0.0
23:00,0.0,0.0,0.0


=== query_load_forecast ===
# Load Forecast for CZ on 2026-04-30
# Source: ENTSO-E
# Unit: MW

Hour,Load Forecast MW
00:00,6291.25
01:00,6307.5
02:00,6178.75
03:00,6205.0
04:00,6356.0
05:00,6836.75
06:00,7798.75
07:00,8367.25
08:00,8651.25
09:00,8889.75
10:00,8838.5
11:00,8818.0
12:00,8742.5
13:00,8616.25
14:00,8257.5
15:00,7960.5
16:00,7692.25
17:00,7495.0
18:00,7311.5
19:00,7384.5
20:00,7402.0
21:00,7099.25
22:00,6736.0
23:00,6367.75


=== query_actual_load ===
# Actual Load for CZ on 2026-04-30
# Source: ENTSO-E
# Unit: MW

Hour,Actual Load MW
00:00,6319.822
01:00,6347.102
02:00,6225.412
03:00,6196.828
04:00,6401.208
05:00,6914.58
06:00,7852.472
07:00,8370.695
08:00,8604.962
09:00,8803.82
10:00,8736.77
11:00,8648.745
12:00,8633.335
13:00,8461.795
14:00,8099.535
15:00,7854.662
16:00,7544.185
17:00,7237.915
18:00,6830.465
19:00,6845.755
20:00,6845.655
21:00,6567.705
22:00,6260.808
23:00,5934.098


=== query_crossborder_flows ===
# Cross-Border Flows for CZ on 2026-04-30
# Source: ENTSO-E
# Positive = import into CZ, Negative = export
# Unit: MW

Hour,DE-LU Flow,AT Flow,PL Flow,SK Flow,Net Import MW
00:00,0.0,398.0,0.0,2193.625,2591.625
01:00,0.0,498.8,0.0,2258.65,2757.45
02:00,0.0,619.7,0.0,2195.1,2814.8
03:00,0.0,535.6,0.0,2136.675,2672.275
04:00,0.0,403.3,0.0,2202.2,2605.5
05:00,0.0,340.7,0.0,2123.175,2463.875
06:00,0.0,554.0,0.0,1657.025,2211.025
07:00,0.0,591.0,0.0,1314.6,1905.6
08:00,0.0,821.9,0.0,851.25,1673.15
09:00,0.0,732.9,0.0,540.0,1272.9
10:00,0.0,377.2,0.0,1350.3,1727.5
11:00,0.0,128.7,0.0,1456.6,1585.3
12:00,1.5,0.0,0.0,1813.7,1815.2
13:00,0.0,0.0,0.0,1891.975,1891.975
14:00,0.0,0.0,0.0,1745.5,1745.5
15:00,0.0,95.7,0.0,1754.175,1849.875
16:00,0.0,324.2,0.0,1856.625,2180.825
17:00,0.0,501.0,0.0,1785.375,2286.375
18:00,0.0,358.8,33.775,1762.875,2155.45
19:00,0.0,499.8,349.75,1616.55,2466.1
20:00,0.0,402.8,467.125,1596.225,2466.15
21:00,0.0,586.7,8.2,1572.325,2167.225
22:00,0.0,820.4,0.0,1680.2,2500.6
23:00,0.0,1161.0,0.0,1905.5,3066.5


=== query_outages ===
# Generation Outages for CZ on 2026-04-30
# Source: ENTSO-E (REMIT UMMs)
# Unit: MW unavailable

               plant_type production_resource_name            start              end
Fossil Brown coal/Lignite              EPC1_______ 2026-04-30 23:45 2026-05-02 00:00
Fossil Brown coal/Lignite              EPC1_______ 2026-04-30 23:45 2026-05-05 00:00
Fossil Brown coal/Lignite              ELED_______ 2026-04-30 19:00 2026-05-02 00:00
Fossil Brown coal/Lignite              ELED_______ 2026-04-30 11:00 2026-04-30 19:00
Fossil Brown coal/Lignite              ELED_______ 2026-04-30 08:15 2026-04-30 11:00
Fossil Brown coal/Lignite              EPR2_______ 2026-04-30 08:00 2026-05-04 06:00
Fossil Brown coal/Lignite              ETU2_______ 2026-04-30 05:30 2026-04-30 08:15
               Fossil Gas              EPVR_______ 2026-04-30 00:00 2026-05-01 00:00
Fossil Brown coal/Lignite              ETI2_______ 2026-04-30 00:00 2026-05-01 00:00
Fossil Brown coal/Lignite              ELED_______ 2026-04-30 00:00 2026-04-30 08:15
Fossil Brown coal/Lignite              ELED_______ 2026-04-30 00:00 2026-04-30 11:00
Fossil Brown coal/Lignite              EECK_______ 2026-04-29 10:15 2026-05-03 00:00
Fossil Brown coal/Lignite              ELED_______ 2026-04-28 00:00 2026-05-02 00:00
Fossil Brown coal/Lignite              EPC1_______ 2026-04-27 00:00 2026-05-01 00:00
Fossil Brown coal/Lignite              EPC1_______ 2026-04-27 00:00 2026-06-03 00:00
Fossil Brown coal/Lignite              EPC1_______ 2026-04-27 00:00 2026-04-30 14:30
Fossil Brown coal/Lignite              ECHV_______ 2026-04-24 23:45 2026-05-23 00:00
Fossil Brown coal/Lignite              ECHV_______ 2026-04-18 00:00 2026-06-29 00:00
                  Nuclear              EDUK_______ 2026-04-17 20:00 2026-07-01 20:00
                  Nuclear              EDUK_______ 2026-04-17 18:00 2026-07-03 18:00
     Hydro Pumped Storage              EDST_______ 2026-04-13 00:00 2026-06-15 00:00
                  Nuclear              EDUK_______ 2026-04-10 18:00 2026-06-26 18:00
Fossil Brown coal/Lignite              EECK_______ 2026-04-10 11:00 2026-05-03 00:00
Fossil Brown coal/Lignite              ECHV_______ 2026-04-06 00:00 2026-06-20 00:00
Fossil Brown coal/Lignite              ETU2_______ 2026-04-04 00:00 2026-05-14 00:00
                  Nuclear              EDUK_______ 2026-04-03 18:00 2026-06-19 18:00
Fossil Brown coal/Lignite              ECHV_______ 2026-04-02 00:15 2026-05-09 00:00
     Hydro Pumped Storage              EDAL_______ 2026-01-02 00:00 2026-06-08 00:00
         Fossil Hard coal              EDET_______ 2026-01-01 00:00 2026-12-31 23:00
         Fossil Hard coal              EDET_______ 2026-01-01 00:00 2028-01-01 00:00
         Fossil Hard coal              EDET_______ 2025-05-01 00:00 2029-01-01 00:00
         Fossil Hard coal              EDET_______ 2025-03-01 00:00 2029-01-01 00:00

=== query_imbalance_prices ===
# Imbalance Prices and Volumes for CZ on 2026-04-30
# Source: ENTSO-E
# Unit: EUR/MWh (Prices), MW (Volumes)
# Note: Financial values converted from CZK to EUR at official rate of 24.36 CZK/EUR

Hour,Imbalance Volume MW,Imbalance Volume MW StdDev,Imbalance Volume MW Range,Imbalance Price EUR/MWh,Imbalance Price EUR/MWh StdDev,Imbalance Price EUR/MWh Range
00:00,-27.382,11.543,24.78,132.862,8.064,18.314
01:00,-13.7,12.067,26.31,116.932,0.397,0.912
02:00,-13.305,3.074,6.75,115.137,0.282,0.603
03:00,-11.245,4.91,9.34,116.489,1.143,2.532
04:00,-11.745,3.718,7.64,126.938,6.059,13.243
05:00,-37.968,8.254,19.37,134.273,6.053,13.554
06:00,-43.148,24.291,44.17,156.53,14.072,30.196
07:00,-30.248,11.736,25.18,167.881,24.673,54.766
08:00,-22.278,22.82,49.91,103.227,71.632,162.878
09:00,10.458,23.023,50.99,21.248,42.495,84.99
10:00,11.042,8.668,20.8,-11.341,15.98,34.716
11:00,3.352,6.484,14.68,17.472,32.79,67.217
12:00,-1.02,3.687,8.98,27.809,35.536,83.154
13:00,-17.6,25.813,53.11,38.503,39.803,84.358
14:00,1.77,3.28,6.54,2.117,31.013,54.999
15:00,-1.053,7.131,15.74,34.309,32.505,77.383
16:00,3.98,7.746,17.98,-4.927,15.834,38.28
17:00,15.1,10.971,21.71,-12.32,14.675,29.05
18:00,-20.852,14.481,33.98,110.543,14.369,31.238
19:00,-17.51,11.175,24.02,144.648,6.519,14.498
20:00,-27.965,10.489,23.59,170.587,2.024,4.335
21:00,-37.365,11.956,27.22,145.225,6.433,15.09
22:00,-3.462,6.849,16.56,96.099,64.091,130.277
23:00,-9.615,6.658,14.51,117.484,1.713,4.16


=== query_residual_load ===
# Residual Load Forecast for CZ on 2026-04-30
# Source: ENTSO-E (calculated: Load - Wind - Solar)
# Unit: MW

Hour,Load Forecast MW,Wind MW,Solar MW,Residual Load MW
00:00,6291.25,0.0,0.0,6291.25
01:00,6307.5,0.0,0.0,6307.5
02:00,6178.75,0.0,0.0,6178.75
03:00,6205.0,0.0,0.0,6205.0
04:00,6356.0,0.0,0.0,6356.0
05:00,6836.75,0.0,23.75,6813.0
06:00,7798.75,0.0,237.0,7561.75
07:00,8367.25,0.0,843.5,7523.75
08:00,8651.25,0.0,1713.5,6937.75
09:00,8889.75,0.0,2460.0,6429.75
10:00,8838.5,0.0,2932.0,5906.5
11:00,8818.0,0.0,3168.25,5649.75
12:00,8742.5,0.0,3236.0,5506.5
13:00,8616.25,0.0,3207.0,5409.25
14:00,8257.5,0.0,3027.25,5230.25
15:00,7960.5,0.0,2658.25,5302.25
16:00,7692.25,0.0,2110.5,5581.75
17:00,7495.0,0.0,1374.25,6120.75
18:00,7311.5,0.0,629.25,6682.25
19:00,7384.5,0.0,174.25,7210.25
20:00,7402.0,0.0,21.25,7380.75
21:00,7099.25,0.0,0.0,7099.25
22:00,6736.0,0.0,0.0,6736.0
23:00,6367.75,0.0,0.0,6367.75
"""
