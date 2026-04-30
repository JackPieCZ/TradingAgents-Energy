"""Shared utilities for energy market data modules."""

import pytz
from datetime import datetime, timedelta
from typing import Optional, Tuple
import pandas as pd
import os

# Constants
CET = pytz.timezone("Europe/Berlin")  # CET/CEST automatic
UTC = pytz.UTC

# Bidding zone codes used by ENTSO-E
BIDDING_ZONES = {
    "DE-LU": "10Y1001A1001A82H",  # Germany-Luxembourg
    "CZ": "10YCZ-CEPS-----N",     # Czech Republic
    "AT": "10YAT-APG------L",     # Austria
    "PL": "10YPL-AREA-----S",     # Poland
    "SK": "10YSK-SEPS-----K",     # Slovakia
    "FR": "10YFR-RTE------C",     # France
    "NL": "10YNL----------L",     # Netherlands
    "DK1": "10YDK-1--------W",    # Denmark West
    "DK2": "10YDK-2--------M",    # Denmark East
    "CH": "10YCH-SWISSGRIDZ",    # Switzerland
}

def get_entsoe_area_code(market_area: str) -> str:
    """Convert a human-readable market area code to the ENTSO-E EIC code."""
    if market_area not in BIDDING_ZONES:
        raise ValueError(f"Market area '{market_area}' not found in known ENTSO-E bidding zones.")
    return BIDDING_ZONES[market_area]

def parse_delivery_period(delivery_period: str) -> Tuple[datetime, datetime]:
    """Parse a delivery period string into (start, end) datetimes in CET."""
    parts = delivery_period.split('/')
    start_str = parts[0]
    
    # Parse start time
    try:
        start_dt = datetime.fromisoformat(start_str)
    except ValueError:
        # Try appending :00 if seconds are missing, etc, but fromisoformat usually handles "2024-06-15T14:00"
        start_dt = datetime.strptime(start_str, "%Y-%m-%dT%H:%M")
        
    if start_dt.tzinfo is None:
        start_dt = CET.localize(start_dt)
        
    # Default duration 60 minutes
    duration_mins = 60
    if len(parts) > 1:
        duration_str = parts[1]
        if duration_str.startswith('PT') and duration_str.endswith('M'):
            duration_mins = int(duration_str[2:-1])
            
    end_dt = start_dt + timedelta(minutes=duration_mins)
    return start_dt, end_dt

def delivery_date_to_entsoe_period(date_str: str) -> Tuple[pd.Timestamp, pd.Timestamp]:
    """Convert a date string to the (start, end) pd.Timestamp range needed by entsoe-py."""
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    start = pd.Timestamp(dt, tz='Europe/Berlin')
    end = start + pd.Timedelta(days=1)
    return start, end

def handle_dst_transition(df: pd.DataFrame, method: str = "ffill") -> pd.DataFrame:
    """Handle daylight saving time transitions in a DataFrame with CET-indexed data."""
    if df.empty or not isinstance(df.index, pd.DatetimeIndex):
        return df
        
    # Note: df.index might already be localized and have handling depending on how data is fetched.
    # True handling of DST requires finding duplicate indices (autumn) or missing indices (spring).
    # Since we're keeping it simple for the AI's sake:
    if df.index.has_duplicates:
        df = df.groupby(level=0).mean()
        
    # Check for gaps. We can resample to the expected frequency (e.g. 1H or 15T)
    freq = pd.infer_freq(df.index)
    if freq:
        # Reindexing to full range can fill gaps
        full_idx = pd.date_range(start=df.index.min(), end=df.index.max(), freq=freq, tz='Europe/Berlin')
        df = df.reindex(full_idx)
        if method == "ffill":
            df = df.ffill()
        else:
            df = df.bfill()
            
    return df

def format_price_table(df: pd.DataFrame, title: str, market_area: str) -> str:
    """Format a price DataFrame as a readable string for LLM consumption."""
    header = f"# {title} for {market_area}\n"
    if hasattr(df.index, 'name') and df.index.name is None:
        df.index.name = 'Hour (CET)'
    return header + "\n" + df.to_csv()

def get_cache_path(source: str, query_type: str, market_area: str, 
                   date_str: str, cache_dir: str) -> str:
    """Build a cache file path for storing/loading cached API responses."""
    path = os.path.join(cache_dir, source, market_area, query_type)
    os.makedirs(path, exist_ok=True)
    return os.path.join(path, f"{date_str}.parquet")
