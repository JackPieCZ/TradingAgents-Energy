#!/usr/bin/env python
"""Script to inspect outputs from all energy data API clients.

Usage:
    python scripts/inspect_energy_apis.py [--date YYYY-MM-DD] [--market-area DE-LU|CZ]

Reads ENTSOE_API_KEY from .env file or environment.
"""

import argparse
import os
import sys
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

# LIMIT = 500
LIMIT = 10000000

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tradingagents.dataflows.entsoe_client import (
    query_day_ahead_prices,
    query_intraday_prices,
    query_wind_solar_forecast,
    query_actual_generation,
    query_generation_forecast_updates,
    query_load_forecast,
    query_actual_load,
    query_crossborder_flows,
    query_outages,
    query_imbalance_prices,
    query_residual_load,
)

from tradingagents.dataflows.ote_client import (
    get_dam_prices,
    get_intraday_prices,
    get_intraday_prices_period,
    get_ida_prices,
    get_imbalance_settlement,
)

from tradingagents.dataflows.smard_client import (
    get_german_generation,
    get_german_residual_load,
    get_german_total_load,
)

from tradingagents.dataflows.weather_client import (
    get_wind_forecast,
    get_solar_forecast,
    get_weather_forecast,
    get_historical_forecast,
)

from tradingagents.dataflows.mock_energy import (
    generate_day_ahead_prices,
    generate_intraday_prices,
    generate_wind_solar_forecast,
    generate_load_forecast,
    generate_residual_load,
    generate_weather_forecast,
)


def print_section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print('='*60)


def test_entsoe(date: str, market_area: str):
    print_section(f"ENTSO-E ({market_area})")
    
    print("\n--- query_day_ahead_prices ---")
    print(query_day_ahead_prices(date, market_area)[:LIMIT])
    
    print("\n--- query_intraday_prices ---")
    print(query_intraday_prices(date, market_area)[:LIMIT])
    
    print("\n--- query_wind_solar_forecast ---")
    print(query_wind_solar_forecast(date, market_area)[:LIMIT])
    
    print("\n--- query_actual_generation ---")
    print(query_actual_generation(date, market_area)[:LIMIT])
    
    print("\n--- query_generation_forecast_updates ---")
    print(query_generation_forecast_updates(date, market_area)[:LIMIT])
    
    print("\n--- query_load_forecast ---")
    print(query_load_forecast(date, market_area)[:LIMIT])
    
    print("\n--- query_actual_load ---")
    print(query_actual_load(date, market_area)[:LIMIT])
    
    print("\n--- query_crossborder_flows ---")
    print(query_crossborder_flows(date, market_area)[:LIMIT])
    
    print("\n--- query_outages ---")
    print(query_outages(date, market_area)[:LIMIT])
    
    print("\n--- query_imbalance_prices ---")
    print(query_imbalance_prices(date, market_area)[:LIMIT])
    
    print("\n--- query_residual_load ---")
    print(query_residual_load(date, market_area)[:LIMIT])


def test_ote(date: str):
    print_section("OTE Czech Republic")
    
    print("\n--- get_dam_prices ---")
    print(get_dam_prices(date, in_eur=True)[:LIMIT])
    
    print("\n--- get_intraday_prices (hourly) ---")
    print(get_intraday_prices(date)[:LIMIT])
    
    print("\n--- get_intraday_prices_period (15-min) ---")
    print(get_intraday_prices_period(date)[:LIMIT])
    
    print("\n--- get_ida_prices ---")
    print(get_ida_prices(date)[:LIMIT])
    
    print("\n--- get_imbalance_settlement ---")
    print(get_imbalance_settlement(date, version=0)[:LIMIT])


def test_smard(date: str):
    print_section("SMARD Germany")
    
    print("\n--- get_german_generation ---")
    print(get_german_generation(date, resolution="hour")[:LIMIT])
    
    print("\n--- get_german_residual_load ---")
    print(get_german_residual_load(date, resolution="hour")[:LIMIT])
    
    print("\n--- get_german_total_load ---")
    print(get_german_total_load(date, resolution="hour")[:LIMIT])


def test_openmeteo(date: str, market_area: str):
    print_section(f"Open-Meteo ({market_area})")
    
    print("\n--- get_wind_forecast ---")
    print(get_wind_forecast(date, market_area)[:LIMIT])
    
    print("\n--- get_solar_forecast ---")
    print(get_solar_forecast(date, market_area)[:LIMIT])
    
    print("\n--- get_weather_forecast ---")
    print(get_weather_forecast(date, market_area)[:LIMIT])
    
    print("\n--- get_historical_forecast ---")
    issue_date = (datetime.strptime(date, "%Y-%m-%d") - timedelta(days=1)).strftime("%Y-%m-%d")
    print(f"(Forecast issued: {issue_date})")
    print(get_historical_forecast(date, issue_date, market_area)[:LIMIT])


def test_mock(date: str, market_area: str):
    print_section(f"MOCK Data ({market_area})")
    
    print("\n--- generate_day_ahead_prices ---")
    print(generate_day_ahead_prices(date, market_area, seed=42)[:LIMIT])
    
    print("\n--- generate_intraday_prices ---")
    print(generate_intraday_prices(date, market_area, seed=42)[:LIMIT])
    
    print("\n--- generate_wind_solar_forecast ---")
    print(generate_wind_solar_forecast(date, market_area, seed=42)[:LIMIT])
    
    print("\n--- generate_load_forecast ---")
    print(generate_load_forecast(date, market_area, seed=42)[:LIMIT])
    
    print("\n--- generate_residual_load ---")
    print(generate_residual_load(date, market_area, seed=42)[:LIMIT])
    
    print("\n--- generate_weather_forecast ---")
    print(generate_weather_forecast(date, market_area, seed=42)[:LIMIT])


def main():
    parser = argparse.ArgumentParser(description="Inspect energy API outputs")
    parser.add_argument("--date", default="2026-04-29", help="Date in YYYY-MM-DD format (default: 2 days ago)")
    parser.add_argument("--market-area", default="CZ", choices=["DE-LU", "CZ"], help="Market area")
    parser.add_argument("--client", default="smard", choices=["entsoe", "ote", "smard", "openmeteo", "mock", "all"], 
                        help="Only test specific client")
    args = parser.parse_args()
    
    if args.date:
        date = args.date
    else:
        date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    
    market_area = args.market_area
    
    print(f"Testing APIs for date: {date}, market area: {market_area}")
    print(f"ENTSOE_API_KEY set: {'ENTSOE_API_KEY' in os.environ}")
    
    # if args.client in (None, "all", "mock"):
    #     test_mock(date, market_area)
    from tradingagents.dataflows.cache_layer import clear_cache
    if args.client in (None, "all", "openmeteo"):
        deleted_count = clear_cache(source="openmeteo")
        print(f"Deleted {deleted_count} parquet files from the cache.")
        sqlite_cache = ".openmeteo_cache.sqlite"
        if os.path.exists(sqlite_cache):
            os.remove(sqlite_cache)
            print("Deleted Open-Meteo SQLite cache.")
        test_openmeteo(date, market_area)
    
    if args.client in (None, "all", "ote"):
        deleted_count = clear_cache(source="ote")
        print(f"Deleted {deleted_count} parquet files from the cache.")
        test_ote(date)
    
    if args.client in (None, "all", "smard"):
        deleted_count = clear_cache(source="smard")
        print(f"Deleted {deleted_count} parquet files from the cache.")
        test_smard(date)
    
    if args.client in (None, "all", "entsoe"):
        if "ENTSOE_API_KEY" not in os.environ:
            print("\n!!! ENTSOE_API_KEY not set - skipping ENTSO-E tests !!!")
            print("Create a .env file with: ENTSOE_API_KEY=your-key")
        else:
            deleted_count = clear_cache(source="entsoe")
            print(f"Deleted {deleted_count} parquet files from the cache.")
            test_entsoe(date, market_area)


if __name__ == "__main__":
    main()