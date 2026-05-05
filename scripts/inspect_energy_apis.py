#!/usr/bin/env python
"""Script to inspect outputs from all energy data API clients.

Usage:
    python scripts/inspect_energy_apis.py [--date YYYY-MM-DD] [--market-area DE-LU|CZ]

Reads ENTSOE_API_KEY from .env file or environment.
"""

from tradingagents.dataflows.mock_energy import (
    generate_day_ahead_prices,
    generate_intraday_prices,
    generate_wind_solar_forecast,
    generate_load_forecast,
    generate_residual_load,
    generate_weather_forecast,
)
from tradingagents.dataflows.weather_client import (
    get_wind_forecast,
    get_solar_forecast,
    get_weather_forecast,
    get_historical_forecast,
)
from tradingagents.dataflows.smard_client import (
    get_german_generation,
    get_german_residual_load,
    get_german_total_load,
    get_smard_prices,
    get_german_generation_forecast,
    get_german_load_forecast

)
from tradingagents.dataflows.ote_client import (
    get_dam_prices,
    get_intraday_prices,
    get_ida_prices,
    get_imbalance_settlement,
)
from tradingagents.dataflows.entsoe_client import (
    query_day_ahead_prices,
    query_intraday_prices,
    query_solar_forecast,
    query_actual_generation,
    query_generation_forecast_updates,
    query_load_forecast,
    query_actual_load,
    query_crossborder_flows,
    query_outages,
    query_imbalance_prices,
    query_residual_load,
)
import argparse
import os
import sys
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

LIMIT = 1000
# LIMIT = 10000000

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


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
    print(query_solar_forecast(date, market_area)[:LIMIT])

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
    print(get_dam_prices(date)[:LIMIT])

    print("\n--- get_intraday_prices (hourly) ---")
    print(get_intraday_prices(date)[:LIMIT])

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

    print("\n--- get_smard_prices ---")
    print(get_smard_prices(date)[:LIMIT])

    print("\n--- get_german_generation_forecast ---")
    print(get_german_generation_forecast(date, resolution="hour")[:LIMIT])

    print("\n--- get_german_load_forecast ---")
    print(get_german_load_forecast(date, resolution="hour")[:LIMIT])

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
    parser.add_argument("--date", default="2026-05-04", help="Date in YYYY-MM-DD format")
    parser.add_argument("--market-area", default="CZ", choices=["DE-LU", "CZ"], help="Market area")
    parser.add_argument("--client", default="all", choices=["entsoe", "ote", "smard", "openmeteo", "mock", "all"],
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

"""
Reference output with [:LIMIT=1000]:
Testing APIs for date: 2026-05-04, market area: CZ

============================================================
  Open-Meteo (CZ)
============================================================

--- get_wind_forecast ---
# Wind Forecast for CZ on 2026-05-04
# Source: Open-Meteo averaged over few locations
# Unit: m/s and Degrees

Hour,Wind 10m m/s,Wind 80m m/s,Wind 120m m/s,Wind Dir 10m,Wind Dir 80m,Wind Dir 120m,Wind Gusts 10m m/s
00:00,13.298435,24.855122,29.432194,188.83763,205.07323,206.66196,24.48
01:00,14.918152,28.354795,35.380394,61.589325,237.74426,240.14893,27.900002
02:00,12.966029,25.310585,32.207554,222.04153,236.37741,239.21017,29.88
03:00,11.597791,23.751799,30.098965,221.14413,233.64307,236.22353,25.199999
04:00,13.773796,23.459785,29.711702,99.20239,81.41943,77.75876,25.199999
05:00,11.16525,25.619852,32.24169,70.841064,62.053986,60.849182,29.34
06:00,8.682703,16.937016,22.852802,218.578,232.74965,236.65247,22.32
07:00,5.473692,9.568858,13.976047,170.00842,225.1927,234.60083,23.579998
08:00,7.4446206,11.694985,12.889137,191.59929,203.20816,210.19783,14.939999
09:00,7.4966574,9.745832,10.55061,195.612,197.61574,202.5,19.619999
10:00,6.5846,7.79068,8.111986,195.51619,197.67215

--- get_solar_forecast ---
# Solar Forecast for CZ on 2026-05-04
# Source: Open-Meteo averaged over few locations
# Unit: W/m² for radiation, minutes for sunshine, % for clouds

Hour,Radiation (Flat) W/m2,Radiation (Tilted) W/m2,Direct W/m2,Diffuse W/m2,Sunshine min,Cloud Cover %,Cloud Cover Low %,Cloud Cover Mid %,Cloud Cover High %
00:00,0.0,0.0,0.0,0.0,0.0,61.8,0.0,20.0,55.8
01:00,0.0,0.0,0.0,0.0,0.0,65.4,0.0,20.0,65.4
02:00,0.0,0.0,0.0,0.0,0.0,65.2,0.0,28.4,62.4
03:00,0.0,0.0,0.0,0.0,0.0,81.2,0.0,30.0,81.2
04:00,0.0,0.0,0.0,0.0,0.0,89.6,0.0,36.4,69.4
05:00,0.0,0.0,0.0,0.0,0.0,75.2,0.0,22.4,75.2
06:00,5.0,4.456389,0.2,4.8,0.0,85.6,0.0,18.4,74.8
07:00,71.4,49.903175,18.6,52.8,25.77268,85.8,0.0,23.2,69.4
08:00,196.8,164.54317,88.4,108.4,60.0,74.8,0.0,40.4,74.8
09:00,342.6,329.20874,189.6,153.0,54.220856,85.8,0.0,30.0,74.8
10:00,488.6,510.00214,318.0,170.6,58.195473,86.0,0.0,28.8,78.4
11:00,620.6,680.9889,434.2,186.4,60.0,90.8,0.0,52.4,64.4
12:00,684.4,763.7833,466.0,218.4,60.0,62.2,0.0,38.8,45.0
1

--- get_weather_forecast ---
# Weather Forecast for CZ on 2026-05-04
# Source: Open-Meteo averaged over multiple locations
# Unit: °C, mm, hPa, cm, WMO Code

Hour,Temperature °C,Feels Like °C,Precipitation mm,Pressure hPa,Snowfall cm,Precip Prob %,Snow Depth meters,Freezing Level meters,Visibility meters,CAPE J/kg,Weather Code,Is Day (1=Yes),Weather Condition
00:00,15.326858,12.526854,0.0,1013.41425,0.0,0.0,0.0,3231.4285,39445.715,0.0,3.0,0.0,Cloudy
01:00,14.291143,11.433424,0.0,1013.6429,0.0,0.0,0.0,3232.8572,37528.57,0.0,3.0,0.0,Cloudy
02:00,13.619714,10.967024,0.0,1013.5286,0.0,0.0,0.0,3194.2856,37271.43,0.0,3.0,0.0,Cloudy
03:00,12.8054285,10.308873,0.0,1013.7714,0.0,0.42857143,0.0,3175.7144,36000.0,0.0,3.0,0.0,Cloudy
04:00,12.355429,9.765154,0.042857144,1013.89996,0.0,1.1428572,0.0,3151.4285,33974.285,0.0,3.0,0.0,Cloudy
05:00,11.969714,9.505148,0.014285714,1014.10004,0.0,2.857143,0.0,3180.0,33585.715,0.0,3.0,0.0,Cloudy
06:00,11.234,9.129695,0.0,1014.34283,0.0,4.0,0.0,3160.0,33128.57,0.0,3.0,1.0,Cloudy


--- get_historical_forecast ---
(Forecast issued: 2026-05-03)
# Historical Weather Forecast for CZ on 2026-05-04
# Forecast issued: 2026-05-03
# Source: Open-Meteo Historical Forecast API averaged over multiple locations

Hour,Wind 10m m/s,Wind 80m m/s,Wind Dir 80m,Wind Gusts 10m m/s,Radiation (Flat) W/m2,Radiation (Tilted) W/m2,Direct W/m2,Diffuse W/m2,Sunshine min,Cloud Cover %,Cloud Cover Low %,Cloud Cover Mid %,Cloud Cover High %,Temperature °C,Snowfall cm,Snow Depth meters,CAPE J/kg,Freezing Level meters,Visibility meters,Weather Code,Is Day (1=Yes),Weather Condition
00:00,9.839541,20.383024,162.54962,19.697142,0.0,0.0,0.0,0.0,0.0,72.14286,0.0,28.571428,67.85714,15.326858,0.0,0.0,0.0,3231.4285,39445.715,3.0,0.0,Cloudy
01:00,10.375979,19.628723,138.80316,18.925714,0.0,0.0,0.0,0.0,0.0,75.28571,0.0,28.571428,75.28571,14.291143,0.0,0.0,0.0,3232.8572,37528.57,3.0,0.0,Cloudy
02:00,8.87175,16.518847,124.84985,18.822857,0.0,0.0,0.0,0.0,0.0,75.14286,0.0,34.57143,73.14286,13.619714,0.0,0.0,0.0,3194.2856,37271.43,3.0,0.0,Cloudy
03:00,7.689624,15.69
Deleted 3 parquet files from the cache.

============================================================
  OTE Czech Republic
============================================================

--- get_dam_prices ---
# Day-Ahead Prices for CZ on 2026-05-04
# Source: OTE Czech Republic
# Note: 15-minute periods have been aggregated into Hourly records

Hour (CET),Price EUR/MWh,Price EUR/MWh StdDev,Price EUR/MWh Range,Volume MWh
00:00,117.13,7.89,17.2,3464.25
01:00,108.15,2.46,5.8,3573.9
02:00,110.8,2.07,5.02,3735.35
03:00,106.56,0.89,2.08,3794.68
04:00,110.54,2.63,5.99,3840.52
05:00,126.17,15.85,35.87,3805.6
06:00,146.34,5.11,11.45,3740.9
07:00,149.35,8.58,20.12,3792.98
08:00,133.02,22.14,52.2,3554.82
09:00,87.35,35.06,83.41,3656.2
10:00,50.46,11.47,26.41,3916.52
11:00,43.25,2.36,5.22,4352.65
12:00,20.47,1.82,3.95,4635.25
13:00,20.85,1.13,2.71,4554.62
14:00,25.95,4.37,10.09,4470.85
15:00,55.0,29.57,68.45,4224.92
16:00,104.93,24.65,58.55,3883.6
17:00,132.21,28.19,65.78,3688.08
18:00,173.4,36.41,81.19,3855.3
19:00,233.0,80.26,182.18,4200.23
20:00,250.15,22.26,47.36,4854.5
21:00,185.42,53.82,120.19,4253.9
22:00,152.96,20.69,45.82,3761.88
23:00,135.84,11.89,27.65,3782.88


--- get_intraday_prices (hourly) ---
# Intraday Continuous Prices for CZ on 2026-05-04
# Source: OTE Czech Republic
# Note: 15-minute periods have been aggregated into Hourly records

Hour (CET),Price EUR/MWh,Price EUR/MWh StdDev,Price EUR/MWh Range,Volume MWh
00:00,102.16,2.28,4.83,643.67
01:00,99.1,0.47,1.09,650.58
02:00,99.0,0.31,0.68,618.65
03:00,98.69,0.54,1.13,507.55
04:00,101.38,0.95,2.02,490.58
05:00,117.31,5.09,11.9,620.08
06:00,131.5,1.35,3.25,800.45
07:00,138.45,2.44,5.85,932.4
08:00,132.76,5.52,13.17,606.6
09:00,87.98,9.04,19.76,222.78
10:00,66.87,2.5,5.95,336.12
11:00,73.4,4.16,8.81,265.7
12:00,59.79,4.06,9.46,408.85
13:00,70.48,2.37,5.73,495.65
14:00,75.47,3.38,6.5,549.85
15:00,86.18,7.53,18.43,593.28
16:00,123.6,7.46,15.32,773.98
17:00,131.06,10.27,23.89,1055.75
18:00,157.22,7.65,16.94,1255.05
19:00,229.81,18.31,42.42,1517.65
20:00,268.77,7.44,17.11,1434.1
21:00,187.91,17.5,39.67,1714.48
22:00,150.82,5.04,11.59,1438.82
23:00,143.43,4.14,9.75,858.08


--- get_ida_prices ---
# IDA Auction Prices for CZ on 2026-05-04
# Source: OTE Czech Republic
# Note: 15-minute periods have been aggregated into Hourly records

Hour (CET),Auction,Price EUR/MWh,Price EUR/MWh StdDev,Price EUR/MWh Range,Volume MWh,Import MWh,Export MWh,Saldo MWh
00:00,IDA1,115.91,7.18,16.32,22.0,-1.3,9.43,8.12
00:00,IDA2,105.0,6.35,14.57,46.5,-54.15,92.65,38.5
01:00,IDA1,107.07,1.67,3.92,25.7,-19.25,3.75,-15.5
01:00,IDA2,98.31,2.48,5.88,19.0,-24.22,33.95,9.72
02:00,IDA1,109.04,0.7,1.51,33.2,-42.08,35.28,-6.8
02:00,IDA2,100.53,0.84,1.99,27.3,-108.7,127.12,18.42
03:00,IDA1,107.46,0.33,0.75,23.3,-14.5,31.42,16.92
03:00,IDA2,101.94,1.34,3.05,22.3,-100.92,92.08,-8.85
04:00,IDA1,109.34,2.25,5.37,19.1,-20.23,17.4,-2.82
04:00,IDA2,103.52,5.21,11.07,25.2,-61.85,75.43,13.58
05:00,IDA1,123.17,11.91,25.4,29.1,-22.05,14.75,-7.3
05:00,IDA2,119.09,10.33,25.15,31.0,-38.8,53.08,14.28
06:00,IDA1,142.5,3.97,8.97,33.1,-101.6,81.8,-19.8
06:00,IDA2,133.13,5.28,12.18,329.0,0.0,318.3,318.3
07:00,IDA1,

--- get_imbalance_settlement ---
No imbalance settlement available for CZ on 2026-05-04
# No imbalance settlement available for CZ on 2026-05-04
Deleted 6 parquet files from the cache.

============================================================
  SMARD Germany
============================================================

--- get_german_generation ---
Failed to fetch SMARD filter 1224: 404 Client Error: Not Found for url: https://www.smard.de/app/chart_data/1224/DE/1224_DE_hour_1777845600000.json
# DE-LU Generation by Type on 2026-05-04 (hour)
# Source: SMARD (Bundesnetzagentur)
# Unit: MW

Hour,Total,Wind Onshore,Wind Offshore,Solar,Lignite,Hard Coal,Gas,Pumped Storage,Hydro,Biomass,Other
00:00,39182.0,13957.08,3989.17,0.0,6708.71,2621.82,4339.82,388.11,1324.34,4055.1,1797.85
01:00,38433.88,14349.8,3374.85,0.0,6698.21,2750.34,4095.67,117.13,1305.94,3990.98,1750.96
02:00,37224.9,13294.89,3048.46,0.0,7017.97,2832.72,4039.62,48.65,1281.77,3975.03,1685.79
03:00,35719.35,11434.35,2719.02,0.0,7253.71,3167.16,4202.96,15.1,1267.19,3980.17,1679.69
04:00,34513.78,10038.63,2328.47,0.0,7509.36,3227.18,4422.64,14.66,1294.48,4016.77,1661.59
05:00,33527.53,8212.95,2130.2,26.24,7515.52,3356.92,4802.38,374.44,1323.4,4105.1,1680.38
06:00,36446.19,6692.61,1550.82,1670.34,7290.69,3581.97,5236.51,3048.36,1355.26,4298.73,1720.9
07:00,42628.56,5520.11,1424.36,7404.84,7238.0,3598.15,5395.71,4401.74,1535.89,4390.75,1719.01
08:00,47785.77,4394.33,1534.22,16495.4,6654.87,3600.7,5458.61,2077.96,

--- get_german_residual_load ---
# DE-LU Residual Load on 2026-05-04 (hour)
# Source: SMARD (Bundesnetzagentur)
# Unit: MW (Load - Wind - Solar)

Hour,Residual Load MW
00:00,22796.8
01:00,22310.55
02:00,23427.42
03:00,25286.81
04:00,28999.32
05:00,35765.75
06:00,43014.39
07:00,43292.59
08:00,37071.56
09:00,28352.19
10:00,19719.84
11:00,14155.37
12:00,13719.13
13:00,16027.68
14:00,18598.55
15:00,22085.44
16:00,29107.78
17:00,38215.55
18:00,47097.81
19:00,51257.91
20:00,51911.99
21:00,51107.32
22:00,47184.83
23:00,


--- get_german_total_load ---
# DE-LU Total Load on 2026-05-04 (hour)
# Source: SMARD (Bundesnetzagentur)
# Unit: MW

Hour,Total Load MW
00:00,40743.05
01:00,40035.2
02:00,39770.78
03:00,39440.18
04:00,41366.42
05:00,46135.14
06:00,52928.16
07:00,57641.89
08:00,59495.5
09:00,59858.54
10:00,58752.31
11:00,58087.77
12:00,58255.18
13:00,57130.3
14:00,55886.36
15:00,54990.51
16:00,55235.65
17:00,56631.21
18:00,58423.14
19:00,58252.83
20:00,56226.97
21:00,54729.61
22:00,51271.68
23:00,


--- get_smard_prices ---
# Day-Ahead Prices for CZ on 2026-05-04 (hour)
# Source: SMARD (Bundesnetzagentur)
# Unit: EUR/MWh

Hour,Price EUR/MWh
00:00,117.13
01:00,108.15
02:00,110.8
03:00,106.56
04:00,110.54
05:00,126.17
06:00,146.34
07:00,149.35
08:00,133.02
09:00,87.35
10:00,50.47
11:00,43.25
12:00,20.47
13:00,20.85
14:00,25.95
15:00,55.01
16:00,104.93
17:00,132.21
18:00,173.4
19:00,233.0
20:00,250.15
21:00,185.42
22:00,152.96
23:00,135.84


--- get_german_generation_forecast ---
# DE-LU Generation Forecast on 2026-05-04 (hour)
# Source: SMARD (Bundesnetzagentur)
# Unit: MW

Hour,Forecast Total,Forecast Wind Onshore,Forecast Wind Offshore,Forecast Solar,Forecast Combined Wind & Solar
00:00,36161.19,13131.22,1531.24,0.0,14662.47
01:00,34906.77,12197.79,1503.21,0.0,13701.0
02:00,33861.36,11213.2,1519.85,0.0,12733.05
03:00,33097.79,10127.0,1549.3,0.0,11676.3
04:00,32779.17,8993.27,1561.78,0.0,10555.06
05:00,34517.55,7909.85,1506.27,45.19,9461.3
06:00,38699.42,6790.16,1418.45,1712.31,9920.92
07:00,43883.22,5356.0,1310.73,7275.09,13941.82
08:00,48120.46,3858.46,1211.07,15995.39,21064.92
09:00,53263.83,3176.12,1115.97,25473.08,29765.17
10:00,56891.06,3038.73,1029.4,33067.18,37135.3
11:00,61358.24,3093.52,912.44,37779.27,41785.23
12:00,62872.62,3256.92,776.56,39551.8,43585.28
13:00,61586.14,3363.33,697.28,38257.27,42317.88
14:00,57885.3,3482.48,662.76,34339.39,38484.63
15:00,53259.48,3483.2,667.46,28722.21,32872.87
16:00,48865.87,3394.86,674.54,21788.

--- get_german_load_forecast ---
# DE-LU Load Forecast on 2026-05-04 (hour)
# Source: SMARD (Bundesnetzagentur)
# Unit: MW

Hour,Load Forecast MW
00:00,41293.49
01:00,40100.28
02:00,39554.36
03:00,39646.11
04:00,41113.51
05:00,45920.36
06:00,53787.14
07:00,59719.34
08:00,62922.07
09:00,64097.63
10:00,64416.64
11:00,64567.67
12:00,63568.72
13:00,62120.65
14:00,60920.49
15:00,59711.01
16:00,59578.95
17:00,60182.55
18:00,60842.8
19:00,60792.57
20:00,58986.49
21:00,56484.62
22:00,53024.92
23:00,49404.97

Deleted 10 parquet files from the cache.

============================================================
  ENTSO-E (CZ)
============================================================

--- query_day_ahead_prices ---
# Day-Ahead Prices for CZ on 2026-05-04
# Source: ENTSO-E Transparency Platform
# Unit: EUR/MWh

Hour,Price EUR/MWh,Price EUR/MWh StdDev,Price EUR/MWh Range
00:00,117.132,7.891,17.2
01:00,108.152,2.46,5.8
02:00,110.798,2.072,5.02
03:00,106.558,0.894,2.08
04:00,110.542,2.632,5.99
05:00,126.172,15.853,35.87
06:00,146.335,5.112,11.45
07:00,149.348,8.578,20.12
08:00,133.025,22.139,52.2
09:00,87.352,35.06,83.41
10:00,50.465,11.472,26.41
11:00,43.248,2.36,5.22
12:00,20.472,1.821,3.95
13:00,20.85,1.127,2.71
14:00,25.95,4.372,10.09
15:00,55.005,29.568,68.45
16:00,104.928,24.648,58.55
17:00,132.207,28.191,65.78
18:00,173.4,36.407,81.19
19:00,233.0,80.264,182.18
20:00,250.15,22.261,47.36
21:00,185.418,53.824,120.19
22:00,152.96,20.692,45.82
23:00,135.84,11.889,27.65
00:00,142.69,,0.0


--- query_intraday_prices ---
No intraday prices for sequence 1 in CZ on 2026-05-04
No intraday prices for sequence 2 in CZ on 2026-05-04
No intraday prices for sequence 3 in CZ on 2026-05-04
No intraday prices available for CZ on 2026-05-04
No intraday prices available for CZ on 2026-05-04
# No intraday prices available for CZ on 2026-05-04

--- query_wind_solar_forecast ---
# Solar Day-Ahead Forecast for CZ on 2026-05-04
# Source: ENTSO-E (TSO forecasts)
# Unit: MW

Hour,Solar MW
00:00,0.0
01:00,0.0
02:00,0.0
03:00,0.0
04:00,0.0
05:00,32.0
06:00,219.75
07:00,669.25
08:00,1331.75
09:00,1973.75
10:00,2430.75
11:00,2722.75
12:00,2828.0
13:00,2765.0
14:00,2513.0
15:00,2132.0
16:00,1664.0
17:00,1077.75
18:00,510.75
19:00,164.0
20:00,27.25
21:00,0.0
22:00,0.0
23:00,0.0


--- query_actual_generation ---
# Actual Generation by Type for CZ on 2026-05-04
# Source: ENTSO-E
# Unit: MW

Hour,Biomass,Fossil Brown coal/Lignite,Fossil Coal-derived gas,Fossil Gas,Fossil Hard coal,Fossil Oil,Hydro Pumped Storage,Hydro Pumped Storage (Consumption),Hydro Run-of-river and poundage,Hydro Water Reservoir,Nuclear,Other,Other renewable,Solar,Waste,Wind Onshore
00:00,296.552,2138.668,0.0,65.05,55.658,3.39,29.822,0.0,78.565,66.12,3485.288,76.442,262.597,0.0,34.728,147.988
01:00,295.5,2171.26,0.0,63.345,54.688,3.39,0.0,0.0,83.265,50.242,3488.79,76.705,262.905,0.0,34.81,150.878
02:00,296.548,2207.842,0.0,62.768,55.978,3.39,0.0,0.0,84.828,12.95,3493.528,76.905,263.1,0.0,34.85,152.452
03:00,296.175,2208.17,0.0,62.4,55.188,3.39,0.0,0.0,81.87,13.045,3495.245,76.968,263.252,0.0,34.845,147.305
04:00,296.935,2243.555,0.0,68.062,54.32,3.398,0.0,0.0,82.115,13.03,3496.768,76.118,264.248,14.552,34.882,131.228
05:00,299.298,2299.412,0.0,85.08,53.642,3.412,147.24,0.0,78.682,73.238,3496.538,74.65,267.31,61.642,34.

--- query_generation_forecast_updates ---
# Forecast Updates for CZ on 2026-05-04
# Source: ENTSO-E
# WARNING: Intraday forecast updates unavailable. Displaying Day-Ahead baseline only.
# Unit: MW

Hour,DA Solar
00:00,0.0
01:00,0.0
02:00,0.0
03:00,0.0
04:00,0.0
05:00,32.0
06:00,219.75
07:00,669.25
08:00,1331.75
09:00,1973.75
10:00,2430.75
11:00,2722.75
12:00,2828.0
13:00,2765.0
14:00,2513.0
15:00,2132.0
16:00,1664.0
17:00,1077.75
18:00,510.75
19:00,164.0
20:00,27.25
21:00,0.0
22:00,0.0
23:00,0.0


--- query_load_forecast ---
# Load Forecast for CZ on 2026-05-04
# Source: ENTSO-E
# Unit: MW

Hour,Load Forecast MW
00:00,5440.75
01:00,5457.0
02:00,5309.75
03:00,5247.25
04:00,5371.25
05:00,5785.75
06:00,6825.0
07:00,7441.0
08:00,7922.25
09:00,8202.25
10:00,8215.5
11:00,8321.5
12:00,8369.75
13:00,8255.25
14:00,7936.0
15:00,7691.75
16:00,7473.75
17:00,7233.5
18:00,7089.25
19:00,7130.25
20:00,7064.25
21:00,6734.5
22:00,6365.0
23:00,5965.25


--- query_actual_load ---
# Actual Load for CZ on 2026-05-04
# Source: ENTSO-E
# Unit: MW

Hour,Actual Load MW
00:00,5174.888
01:00,5146.152
02:00,4995.138
03:00,4938.892
04:00,5103.45
05:00,5529.865
06:00,6507.138
07:00,7176.295
08:00,7724.652
09:00,8139.698
10:00,8131.055
11:00,8223.258
12:00,8276.508
13:00,8159.99
14:00,7829.57
15:00,7629.33
16:00,7387.008
17:00,7155.008
18:00,7006.808
19:00,7004.032
20:00,6977.565
21:00,6569.448
22:00,6216.827


--- query_crossborder_flows ---
# Cross-Border Flows for CZ on 2026-05-04
# Source: ENTSO-E
# Positive = import into CZ, Negative = export
# Unit: MW

Hour,DE-LU Flow,AT Flow,PL Flow,SK Flow,Net Import MW
00:00,851.45,1136.2,0.0,1517.7,3505.35
01:00,1066.825,1246.7,0.0,1239.275,3552.8
02:00,1136.5,1334.3,0.0,1047.325,3518.125
03:00,1265.025,1394.5,0.0,1016.5,3676.025
04:00,1161.975,1332.8,0.0,959.45,3454.225
05:00,914.925,1245.8,0.0,1272.175,3432.9
06:00,612.9,955.4,0.0,1024.375,2592.675
07:00,706.9,864.9,0.0,84.175,1655.975
08:00,1837.55,1090.8,0.0,0.0,2928.35
09:00,2153.475,1138.9,0.0,0.0,3292.375
10:00,2129.5,920.4,0.0,0.0,3049.9
11:00,1802.55,669.4,0.0,0.0,2471.95
12:00,1642.05,305.9,0.0,0.0,1947.95
13:00,1644.0,254.2,0.0,0.0,1898.2
14:00,1762.15,363.9,0.0,0.0,2126.05
15:00,1929.55,750.2,0.0,0.0,2679.75
16:00,1554.275,731.8,0.0,0.0,2286.075
17:00,873.5,624.4,0.0,532.75,2030.65
18:00,303.625,366.6,0.0,1228.225,1898.45
19:00,65.0,215.7,0.0,1318.775,1599.475
20:00,56.65,40.2,65.025,1468.275,1630

--- query_outages ---
# Generation Outages (REMIT UMMs) for CZ on 2026-05-04

## System State Summary
* Total Unavailable Capacity: 5579 MW
  - Planned Maintenance (Priced into DA): 4734 MW
  - Unplanned Outages (Intraday Shocks): 845 MW

## Offline Capacity by Plant Type
* Fossil Brown coal/Lignite: 2819 MW
* Fossil Gas: 1580 MW
* Hydro Pumped Storage: 650 MW
* Nuclear: 530 MW

## Detailed REMIT Messages (Sorted by Newest Publication First)
  published_time                plant_type  plant_name         outage_type  nominal_capacity  available_capacity            start              end  unavailable_MW
2026-05-04 21:03                Fossil Gas EPVR_______ Planned maintenance             186.0                   0 2026-05-04 00:00 2026-05-04 14:00           186.0
2026-05-04 21:03                Fossil Gas EPVR_______ Planned maintenance             186.0                  15 2026-05-04 21:00 2026-05-04 22:00           171.0
2026-05-04 21:03                Fossil Gas EPVR_______ Planned maintenance             

--- query_imbalance_prices ---
# Imbalance Prices and Volumes for CZ on 2026-05-04
# Source: ENTSO-E
# Unit: EUR/MWh (Prices), MW (Volumes)
# Note: Financial values converted from CZK to EUR at official rate of 24.395 CZK/EUR

Hour,Imbalance Volume MW,Imbalance Volume MW StdDev,Imbalance Volume MW Range,Imbalance Price EUR/MWh,Imbalance Price EUR/MWh StdDev,Imbalance Price EUR/MWh Range
00:00,5.047,16.853,40.45,64.334,74.618,137.268
01:00,-20.32,18.52,37.04,89.638,59.768,120.848
02:00,14.838,4.825,9.65,25.816,51.631,103.262
03:00,3.99,8.74,17.48,80.902,55.442,117.968
04:00,-35.488,7.025,14.05,121.164,3.239,7.482
05:00,57.968,57.935,115.87,30.266,60.531,121.062
06:00,76.185,37.27,74.54,52.206,61.137,116.892
07:00,-67.867,38.085,76.17,154.472,14.965,34.196
08:00,-48.605,48.41,96.82,79.482,91.945,165.758
09:00,13.628,2.005,4.01,0.0,0.0,0.0
10:00,-1.242,2.235,4.47,86.963,100.616,181.686
11:00,15.792,9.655,19.31,-1.176,2.352,4.703
12:00,-32.922,21.295,42.59,135.942,5.87,12.129
13:00,26.65,61.84,123.68,55.56

--- query_residual_load ---
# Residual Load Actual for CZ on 2026-05-04
# Source: ENTSO-E
# Unit: MW

Hour,Actual Load MW,Solar MW
00:00,5174.888,0.0
01:00,5146.152,0.0
02:00,4995.138,0.0
03:00,4938.892,0.0
04:00,5103.45,0.0
05:00,5529.865,32.0
06:00,6507.138,219.75
07:00,7176.295,669.25
08:00,7724.652,1331.75
09:00,8139.698,1973.75
10:00,8131.055,2430.75
11:00,8223.258,2722.75
12:00,8276.508,2828.0
13:00,8159.99,2765.0
14:00,7829.57,2513.0
15:00,7629.33,2132.0
16:00,7387.008,1664.0
17:00,7155.008,1077.75
18:00,7006.808,510.75
19:00,7004.032,164.0
20:00,6977.565,27.25
21:00,6569.448,0.0
22:00,6216.827,0.0
"""