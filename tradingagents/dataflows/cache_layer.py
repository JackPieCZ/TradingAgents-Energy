"""Local caching layer for energy data API responses."""

import os
import logging
from typing import Optional, Callable
import pandas as pd

from .config import get_config
from .energy_utils import get_cache_path as build_cache_path

logger = logging.getLogger(__name__)

def get_cache_dir() -> str:
    """Get the cache directory from config, creating it if needed."""
    config = get_config()
    cache_dir = config.get("data_cache_dir", os.path.expanduser("~/.tradingagents/cache"))
    os.makedirs(cache_dir, exist_ok=True)
    return cache_dir

def cache_key_path(source: str, query_type: str, market_area: str, date_str: str) -> str:
    """Build the full file path for a cache entry."""
    cache_dir = get_cache_dir()
    return build_cache_path(source, query_type, market_area, date_str, cache_dir)

def load_cached(source: str, query_type: str, market_area: str, date_str: str) -> Optional[pd.DataFrame]:
    """Load a cached DataFrame if it exists, otherwise return None."""
    path = cache_key_path(source, query_type, market_area, date_str)
    if os.path.exists(path):
        try:
            return pd.read_parquet(path)
        except Exception as e:
            logger.warning(f"Failed to read cache at {path}: {e}")
            return None
    return None

def save_to_cache(df: pd.DataFrame, source: str, query_type: str, market_area: str, date_str: str) -> None:
    """Save a DataFrame to the cache."""
    path = cache_key_path(source, query_type, market_area, date_str)
    try:
        df.to_parquet(path)
    except Exception as e:
        logger.warning(f"Failed to write cache at {path}: {e}")

def cached_fetch(source: str, query_type: str, market_area: str, date_str: str,
                 fetch_fn: Callable[[], pd.DataFrame]) -> pd.DataFrame:
    """Generic cache-or-fetch wrapper."""
    df = load_cached(source, query_type, market_area, date_str)
    if df is not None:
        return df
    
    df = fetch_fn()
    save_to_cache(df, source, query_type, market_area, date_str)
    return df

def clear_cache(source: Optional[str] = None, market_area: Optional[str] = None) -> int:
    """Clear cached data. Returns number of files deleted."""
    cache_dir = get_cache_dir()
    count = 0
    for root, dirs, files in os.walk(cache_dir):
        for file in files:
            if not file.endswith('.parquet'):
                continue
            
            # path is roughly cache_dir/source/market_area/query_type/date.parquet
            rel_path = os.path.relpath(os.path.join(root, file), cache_dir)
            parts = rel_path.split(os.sep)
            if len(parts) >= 4:
                file_source, file_market, _, _ = parts[0], parts[1], parts[2], parts[3]
                if source and file_source != source:
                    continue
                if market_area and file_market != market_area:
                    continue
                
                os.remove(os.path.join(root, file))
                count += 1
    return count
