"""Open-Meteo weather data client for energy trading.

Open-Meteo provides free weather data including:
- Historical weather observations
- Weather forecasts (up to 16 days)
- Historical forecasts (what the forecast was at a past date — critical for backtesting)

The "Historical Forecast" API is especially important: it lets you reconstruct
what the weather forecast looked like at a specific past date, which is needed
to simulate forecast-update trading strategies (Kup22) without look-ahead bias.

APIs used:
- Historical: https://archive-api.open-meteo.com/v1/archive
- Forecast: https://api.open-meteo.com/v1/forecast
- Historical Forecast: https://historical-forecast-api.open-meteo.com/v1/forecast

No API key required. Free tier allows 10,000 requests/day.
"""

import logging
from datetime import datetime, date, timedelta
import os
from typing import Annotated, Optional, List
import pandas as pd
import numpy as np

import openmeteo_requests
import requests_cache
from retry_requests import retry

try:
    from .config import get_config
    from .energy_utils import CET, get_cache_path
    from . import cache_layer
except ImportError:
    from config import get_config
    from energy_utils import CET, get_cache_path
    import cache_layer

logger = logging.getLogger(__name__)

# Representative coordinates for aggregated wind/solar forecasting
# Capacity-weighted representative coordinates for aggregated forecasting
WEATHER_LOCATIONS = {
    "DE-LU": {
        "wind": [
            # Offshore (Crucial for baseline baseload wind)
            {"name": "Offshore North Sea", "lat": 54.5, "lon": 6.5},  # Major wind park cluster (Borkum Riffgrund)
            {"name": "Offshore Baltic Sea", "lat": 54.8, "lon": 13.5},  # EnBW Baltic wind parks
            # Onshore (Captures West-to-East front movements)
            {"name": "Onshore North-West (Lower Saxony)", "lat": 53.0, "lon": 8.0},
            {"name": "Onshore North-East (Brandenburg)", "lat": 53.0, "lon": 13.5},
            {"name": "Onshore Central (Hesse)", "lat": 51.0, "lon": 9.0},
            {"name": "Onshore South (Bavaria)", "lat": 49.0, "lon": 11.5},
        ],
        "solar": [
            # Heavily weighted toward the South where irradiance and installed capacity are highest
            {"name": "South-East (Bavaria)", "lat": 48.5, "lon": 11.5},
            {"name": "South-West (Baden-Württemberg)", "lat": 48.5, "lon": 9.0},
            {"name": "West (North Rhine-Westphalia)", "lat": 51.5, "lon": 7.5},  # High rooftop PV density
            {"name": "East (Saxony)", "lat": 51.0, "lon": 13.0},
            {"name": "North (Lower Saxony)", "lat": 52.5, "lon": 10.0},
        ],
    },
    "CZ": {
        "wind": [
            {"name": "Northwest (Ore Mountains)", "lat": 50.6, "lon": 13.2},  # Highest concentration of CZ wind
            {"name": "Moravian Highlands", "lat": 49.5, "lon": 15.5},        # Secondary wind area
        ],
        "solar": [
            {"name": "South Moravia (Brno)", "lat": 48.9, "lon": 16.6},      # Highest irradiance and capacity
            {"name": "South Bohemia", "lat": 49.0, "lon": 14.5},
            {"name": "Central Bohemia", "lat": 50.1, "lon": 14.4},
            # Catches fronts entering from Germany + Legacy Mega-parks (e.g., Ralsko/Veprek)
            {"name": "North-West Bohemia (Usti)", "lat": 50.5, "lon": 13.8},
            # Catches fronts entering/stalling from Poland/Slovakia + Heavy industrial load
            {"name": "Moravian-Silesian (Ostrava)", "lat": 49.8, "lon": 18.2},
        ],
    },
}

# WMO Weather interpretation codes
WMO_WEATHER_CODES = {
    0: "Sunny/Clear",
    1: "Mainly Sunny/Clear",
    2: "Partly Cloudy",
    3: "Cloudy",
    45: "Foggy",
    48: "Rime Fog",
    51: "Light Drizzle",
    53: "Drizzle",
    55: "Heavy Drizzle",
    56: "Light Freezing Drizzle",
    57: "Freezing Drizzle",
    61: "Light Rain",
    63: "Rain",
    65: "Heavy Rain",
    66: "Light Freezing Rain",
    67: "Freezing Rain",
    71: "Light Snow",
    73: "Snow",
    75: "Heavy Snow",
    77: "Snow Grains",
    80: "Light Showers",
    81: "Showers",
    82: "Heavy Showers",
    85: "Light Snow Showers",
    86: "Snow Showers",
    95: "Thunderstorm",
    96: "Light Thunderstorms With Hail",
    99: "Thunderstorm With Hail"
}

WIND_PARAMS_ARCHIVE = ["wind_speed_10m", "wind_speed_100m",
                       "wind_direction_10m", "wind_direction_100m", "wind_gusts_10m"]
WIND_PARAMS_FORECAST = ["wind_speed_10m", "wind_speed_80m", "wind_speed_120m",
                        "wind_direction_10m", "wind_direction_80m", "wind_direction_120m", "wind_gusts_10m"]

SOLAR_PARAMS = ["shortwave_radiation", "direct_radiation", "diffuse_radiation",
                "sunshine_duration", "cloud_cover", "global_tilted_irradiance",
                "cloud_cover_low", "cloud_cover_mid", "cloud_cover_high"]

WEATHER_PARAMS_ARCHIVE = ["temperature_2m", "apparent_temperature",
                          "precipitation", "pressure_msl", "snowfall", "weather_code", "snow_depth"]
WEATHER_PARAMS_FORECAST = ["temperature_2m", "apparent_temperature", "precipitation", "pressure_msl", "snowfall",
                           "weather_code", "precipitation_probability", "snow_depth", "freezing_level_height", "is_day", "cape", "visibility"]

HISTORICAL_FORECAST_PARAMS = WIND_PARAMS_FORECAST + SOLAR_PARAMS + \
    [p for p in WEATHER_PARAMS_FORECAST if p != "precipitation_probability"]


def get_weather_description(code: float) -> str:
    """Safely translate a WMO code into a human-readable string."""
    if pd.isna(code):
        logger.warning("Received NaN weather code, returning 'Unknown'")
        return "Unknown"
    return WMO_WEATHER_CODES.get(int(code), "Unknown")


_client = None


def _get_session():
    global _client
    if _client is None:
        cache_session = requests_cache.CachedSession('.openmeteo_cache', expire_after=3600)
        retry_session = retry(cache_session, retries=3, backoff_factor=0.2)
        _client = openmeteo_requests.Client(session=retry_session)
    return _client


# --- DYNAMIC EXTRACTION HELPERS ---

def _circular_mean(degrees: pd.Series) -> float:
    """Calculate the circular mean of an array of angles in degrees."""
    valid_deg = degrees.dropna()
    if valid_deg.empty:
        return np.nan
    rads = np.deg2rad(valid_deg)
    mean_sin = np.mean(np.sin(rads))
    mean_cos = np.mean(np.cos(rads))
    mean_rad = np.arctan2(mean_sin, mean_cos)
    mean_deg = np.rad2deg(mean_rad)
    return (mean_deg + 360) % 360


def _extract_hourly_data(hourly, params_list: List[str]) -> dict:
    """Dynamically extract Open-Meteo variables by their exact requested order."""
    extracted = {}
    for idx, param in enumerate(params_list):
        v = hourly.Variables(idx)
        extracted[param] = v.ValuesAsNumpy() if v else np.array([])
    return extracted


def _get_val(extracted: dict, param: str, index: int, default=np.nan):
    """Safely get a value from the extracted arrays."""
    arr = extracted.get(param, [])
    return arr[index] if index < len(arr) else default


def get_wind_forecast(
    delivery_date: Annotated[str, "Delivery date YYYY-MM-DD"],
    market_area: Annotated[str, "Bidding zone, e.g. 'DE-LU' or 'CZ'"],
) -> str:
    """Fetch wind speed data at hub heights relevant for wind turbines."""
    def fetch():
        locations = WEATHER_LOCATIONS.get(market_area, {}).get("wind", [])
        if not locations:
            logger.warning(f"No wind locations configured for market area {market_area}")
            return pd.DataFrame()

        delivery_dt = datetime.strptime(delivery_date, "%Y-%m-%d")
        is_past = delivery_dt.date() < datetime.now().date()
        params_list = WIND_PARAMS_ARCHIVE if is_past else WIND_PARAMS_FORECAST

        all_data = []
        for loc in locations:
            try:
                url = "https://archive-api.open-meteo.com/v1/archive" if is_past else "https://api.open-meteo.com/v1/forecast"
                params = {
                    "latitude": loc["lat"], "longitude": loc["lon"],
                    "hourly": ",".join(params_list),
                    "start_date": delivery_date, "end_date": delivery_date,
                    "timezone": "Europe/Berlin",
                }
                responses = _get_session().weather_api(url, params)
                if not responses or not responses[0].Hourly():
                    logger.warning(f"Failed to fetch wind data for {loc['name']}")
                    continue

                extracted = _extract_hourly_data(responses[0].Hourly(), params_list)
                base_len = len(extracted.get("wind_speed_10m", []))

                # Safely iterate based on the base variable length
                for i in range(base_len):
                    all_data.append({
                        "Location": loc["name"],
                        "Hour": i,
                        "Wind 10m m/s": _get_val(extracted, "wind_speed_10m", i),
                        "Wind 80m m/s": _get_val(extracted, "wind_speed_100m" if is_past else "wind_speed_80m", i),
                        "Wind 120m m/s": np.nan if is_past else _get_val(extracted, "wind_speed_120m", i),
                        "Wind Dir 10m": _get_val(extracted, "wind_direction_10m", i),
                        "Wind Dir 80m": _get_val(extracted, "wind_direction_100m" if is_past else "wind_direction_80m", i),
                        "Wind Dir 120m": np.nan if is_past else _get_val(extracted, "wind_direction_120m", i),
                        "Wind Gusts 10m m/s": _get_val(extracted, "wind_gusts_10m", i),
                    })
            except Exception as e:
                logger.warning(f"Failed to fetch wind data for {loc['name']}: {e}")

        if not all_data:
            logger.warning(f"No valid wind data fetched for any location in {market_area} on {delivery_date}")
            return pd.DataFrame()

        df = pd.DataFrame(all_data)

        # Aggregate safely across all regions using circular mean for directions
        avg_df = df.groupby("Hour").agg({
            "Wind 10m m/s": "mean",
            "Wind 80m m/s": "mean",
            "Wind 120m m/s": "mean",
            "Wind Dir 10m": _circular_mean,
            "Wind Dir 80m": _circular_mean,
            "Wind Dir 120m": _circular_mean,
            "Wind Gusts 10m m/s": "mean",
        }).reset_index()

        avg_df["Hour"] = avg_df["Hour"].apply(lambda h: f"{int(h):02d}:00")

        return avg_df

    df = cache_layer._load_or_fetch("openmeteo", "wind_forecast", market_area, delivery_date, fetch)

    if df is None or df.empty:
        logger.warning(f"No wind forecast data available for {market_area} on {delivery_date}")
        return f"# No wind forecast available for {market_area} on {delivery_date}"

    header = f"# Wind Forecast for {market_area} on {delivery_date}\n"
    header += "# Source: Open-Meteo averaged over few locations\n"
    header += "# Unit: m/s and Degrees\n\n"

    return header + df.to_csv(index=False)


def get_solar_forecast(
    delivery_date: Annotated[str, "Delivery date YYYY-MM-DD"],
    market_area: Annotated[str, "Bidding zone, e.g. 'DE-LU' or 'CZ'"],
) -> str:
    """Fetch solar irradiance data for PV output estimation."""
    def fetch():
        locations = WEATHER_LOCATIONS.get(market_area, {}).get("solar", [])
        if not locations:
            logger.warning(f"No solar locations configured for market area {market_area}")
            return pd.DataFrame()

        delivery_dt = datetime.strptime(delivery_date, "%Y-%m-%d")
        is_past = delivery_dt.date() < datetime.now().date()

        all_data = []
        for loc in locations:
            try:
                url = "https://archive-api.open-meteo.com/v1/archive" if is_past else "https://api.open-meteo.com/v1/forecast"
                params = {
                    "latitude": loc["lat"], "longitude": loc["lon"],
                    "hourly": ",".join(SOLAR_PARAMS),
                    "start_date": delivery_date, "end_date": delivery_date,
                    "timezone": "Europe/Berlin",
                    "tilt": 35, "azimuth": 0
                }
                responses = _get_session().weather_api(url, params)
                if not responses or not responses[0].Hourly():
                    continue

                extracted = _extract_hourly_data(responses[0].Hourly(), SOLAR_PARAMS)
                base_len = len(extracted.get("shortwave_radiation", []))

                for i in range(base_len):
                    sunshine = _get_val(extracted, "sunshine_duration", i)
                    all_data.append({
                        "Location": loc["name"],
                        "Hour": i,
                        "Radiation (Flat) W/m2": _get_val(extracted, "shortwave_radiation", i),
                        "Radiation (Tilted) W/m2": _get_val(extracted, "global_tilted_irradiance", i),
                        "Direct W/m2": _get_val(extracted, "direct_radiation", i),
                        "Diffuse W/m2": _get_val(extracted, "diffuse_radiation", i),
                        "Sunshine min": (sunshine / 60) if not np.isnan(sunshine) else 0,
                        "Cloud Cover %": _get_val(extracted, "cloud_cover", i),
                        "Cloud Cover Low %": _get_val(extracted, "cloud_cover_low", i),
                        "Cloud Cover Mid %": _get_val(extracted, "cloud_cover_mid", i),
                        "Cloud Cover High %": _get_val(extracted, "cloud_cover_high", i),
                    })
            except Exception as e:
                logger.warning(f"Failed to fetch solar data for {loc['name']}: {e}")
                continue

        if not all_data:
            logger.warning(f"No valid solar data fetched for any location in {market_area} on {delivery_date}")
            return pd.DataFrame()

        df = pd.DataFrame(all_data)

        avg_df = df.groupby("Hour").agg({
            "Radiation (Flat) W/m2": "mean",
            "Radiation (Tilted) W/m2": "mean",
            "Direct W/m2": "mean",
            "Diffuse W/m2": "mean",
            "Sunshine min": "mean",
            "Cloud Cover %": "mean",
            "Cloud Cover Low %": "mean",
            "Cloud Cover Mid %": "mean",
            "Cloud Cover High %": "mean",
        }).reset_index()
        avg_df["Hour"] = avg_df["Hour"].apply(lambda h: f"{h:02d}:00")

        return avg_df

    df = cache_layer._load_or_fetch("openmeteo", "solar_forecast", market_area, delivery_date, fetch)

    if df is None or df.empty:
        logger.warning(f"No solar forecast data available for {market_area} on {delivery_date}")
        return f"# No solar forecast available for {market_area} on {delivery_date}"

    header = f"# Solar Forecast for {market_area} on {delivery_date}\n"
    header += "# Source: Open-Meteo averaged over few locations\n"
    header += "# Unit: W/m² for radiation, minutes for sunshine, % for clouds\n\n"

    return header + df.to_csv(index=False)


def get_weather_forecast(
    delivery_date: Annotated[str, "Delivery date YYYY-MM-DD"],
    market_area: Annotated[str, "Bidding zone, e.g. 'DE-LU' or 'CZ'"],
) -> str:
    """Fetch general weather data (temperature, precipitation, snow, cloud cover)."""
    def fetch():
        wind_locs = WEATHER_LOCATIONS.get(market_area, {}).get("wind", [])
        solar_locs = WEATHER_LOCATIONS.get(market_area, {}).get("solar", [])
        locations = wind_locs + solar_locs
        locations = {loc["name"]: loc for loc in locations}.values()

        if not locations:
            logger.warning(f"No weather locations configured for market area {market_area}")
            return pd.DataFrame()

        delivery_dt = datetime.strptime(delivery_date, "%Y-%m-%d")
        is_past = delivery_dt.date() < datetime.now().date()
        params_list = WEATHER_PARAMS_ARCHIVE if is_past else WEATHER_PARAMS_FORECAST

        all_data = []
        for loc in locations:
            try:
                url = "https://archive-api.open-meteo.com/v1/archive" if is_past else "https://api.open-meteo.com/v1/forecast"
                params = {
                    "latitude": loc["lat"], "longitude": loc["lon"],
                    "hourly": ",".join(params_list),
                    "start_date": delivery_date, "end_date": delivery_date,
                    "timezone": "Europe/Berlin",
                }
                responses = _get_session().weather_api(url, params)
                if not responses or not responses[0].Hourly():
                    continue

                extracted = _extract_hourly_data(responses[0].Hourly(), params_list)
                base_len = len(extracted.get("temperature_2m", []))

                for i in range(base_len):
                    all_data.append({
                        "Location": loc["name"],
                        "Hour": i,
                        "Temperature °C": _get_val(extracted, "temperature_2m", i),
                        "Feels Like °C": _get_val(extracted, "apparent_temperature", i),
                        "Precipitation mm": _get_val(extracted, "precipitation", i),
                        "Pressure hPa": _get_val(extracted, "pressure_msl", i),
                        "Snowfall cm": _get_val(extracted, "snowfall", i),
                        "Weather Code": _get_val(extracted, "weather_code", i),
                        "Snow Depth meters": _get_val(extracted, "snow_depth", i),
                        "Precip Prob %": np.nan if is_past else _get_val(extracted, "precipitation_probability", i),
                        "Freezing Level meters": np.nan if is_past else _get_val(extracted, "freezing_level_height", i),
                        "Is Day (1=Yes)": np.nan if is_past else _get_val(extracted, "is_day", i),
                        "CAPE J/kg": np.nan if is_past else _get_val(extracted, "cape", i),
                        "Visibility meters": np.nan if is_past else _get_val(extracted, "visibility", i),
                    })

            except Exception as e:
                logger.warning(f"Failed to fetch weather data for {loc['name']}: {e}")
                continue

        if not all_data:
            logger.warning(f"No valid weather data fetched for any location in {market_area} on {delivery_date}")
            return pd.DataFrame()

        df = pd.DataFrame(all_data)

        # Aggregate safely across all regions
        avg_df = df.groupby("Hour").agg({
            "Temperature °C": "mean",
            "Feels Like °C": "mean",
            "Precipitation mm": "mean",
            "Pressure hPa": "mean",
            "Snowfall cm": "mean",
            "Precip Prob %": "mean",
            "Snow Depth meters": "mean",
            "Freezing Level meters": "mean",
            "Visibility meters": "mean",
            "CAPE J/kg": "max",
            "Weather Code": lambda x: pd.Series.mode(x).max() if not pd.Series.mode(x).empty else np.nan,
            "Is Day (1=Yes)": lambda x: pd.Series.mode(x).max() if not pd.Series.mode(x).empty else np.nan,
        }).reset_index()

        avg_df["Hour"] = avg_df["Hour"].apply(lambda h: f"{int(h):02d}:00")

        # Translate the numeric code into text!
        avg_df["Weather Condition"] = avg_df["Weather Code"].apply(get_weather_description)

        return avg_df

    df = cache_layer._load_or_fetch("openmeteo", "weather_forecast", market_area, delivery_date, fetch)

    if df is None or df.empty:
        logger.warning(f"No weather forecast data available for {market_area} on {delivery_date}")
        return f"# No weather data available for {market_area} on {delivery_date}"

    header = f"# Weather Forecast for {market_area} on {delivery_date}\n"
    header += "# Source: Open-Meteo averaged over multiple locations\n"
    header += "# Unit: °C, mm, hPa, cm, WMO Code\n\n"

    return header + df.to_csv(index=False)


def get_historical_forecast(
    delivery_date: Annotated[str, "Delivery date YYYY-MM-DD"],
    forecast_issue_date: Annotated[str, "Date the forecast was issued YYYY-MM-DD"],
    market_area: Annotated[str, "Bidding zone, e.g. 'DE-LU' or 'CZ'"],
) -> str:
    """Fetch what the weather forecast WAS on a specific past date."""
    def fetch():
        wind_locs = WEATHER_LOCATIONS.get(market_area, {}).get("wind", [])
        solar_locs = WEATHER_LOCATIONS.get(market_area, {}).get("solar", [])
        locations = wind_locs + solar_locs
        locations = {loc["name"]: loc for loc in locations}.values()

        if not locations:
            logger.warning(f"No locations configured for market area {market_area} to fetch historical forecast")
            return pd.DataFrame()

        delivery_dt = datetime.strptime(delivery_date, "%Y-%m-%d")
        issue_dt = datetime.strptime(forecast_issue_date, "%Y-%m-%d")
        horizon_days = max(1, (delivery_dt - issue_dt).days)

        all_data = []
        for loc in locations:
            try:
                url = "https://historical-forecast-api.open-meteo.com/v1/forecast"
                params = {
                    "latitude": loc["lat"], "longitude": loc["lon"],
                    "hourly": ",".join(HISTORICAL_FORECAST_PARAMS),
                    "start_date": delivery_date, "end_date": delivery_date,
                    "forecast_horizon_days": horizon_days,
                    "timezone": "Europe/Berlin",
                    "tilt": 35, "azimuth": 0
                }
                responses = _get_session().weather_api(url, params)
                if not responses or not responses[0].Hourly():
                    continue

                extracted = _extract_hourly_data(responses[0].Hourly(), HISTORICAL_FORECAST_PARAMS)
                base_len = len(extracted.get("wind_speed_10m", []))

                for i in range(base_len):
                    sunshine = _get_val(extracted, "sunshine_duration", i)
                    all_data.append({
                        "Location": loc["name"],
                        "Hour": i,
                        "Wind 10m m/s": _get_val(extracted, "wind_speed_10m", i),
                        "Wind 80m m/s": _get_val(extracted, "wind_speed_80m", i),
                        "Wind Dir 80m": _get_val(extracted, "wind_direction_80m", i),
                        "Wind Gusts 10m m/s": _get_val(extracted, "wind_gusts_10m", i),
                        "Radiation (Flat) W/m2": _get_val(extracted, "shortwave_radiation", i),
                        "Radiation (Tilted) W/m2": _get_val(extracted, "global_tilted_irradiance", i),
                        "Direct W/m2": _get_val(extracted, "direct_radiation", i),
                        "Diffuse W/m2": _get_val(extracted, "diffuse_radiation", i),
                        "Sunshine min": (sunshine / 60) if not np.isnan(sunshine) else 0,
                        "Cloud Cover %": _get_val(extracted, "cloud_cover", i),
                        "Cloud Cover Low %": _get_val(extracted, "cloud_cover_low", i),
                        "Cloud Cover Mid %": _get_val(extracted, "cloud_cover_mid", i),
                        "Cloud Cover High %": _get_val(extracted, "cloud_cover_high", i),
                        "Temperature °C": _get_val(extracted, "temperature_2m", i),
                        "Snowfall cm": _get_val(extracted, "snowfall", i),
                        "Snow Depth meters": _get_val(extracted, "snow_depth", i),
                        "Weather Code": _get_val(extracted, "weather_code", i),
                        "Is Day (1=Yes)": _get_val(extracted, "is_day", i),
                        "CAPE J/kg": _get_val(extracted, "cape", i),
                        "Freezing Level meters": _get_val(extracted, "freezing_level_height", i),
                        "Visibility meters": _get_val(extracted, "visibility", i),
                    })
            except Exception as e:
                logger.warning(f"Failed to fetch historical forecast for {loc['name']}: {e}")
                continue

        if not all_data:
            logger.warning(
                f"No valid historical forecast data fetched for any location in {market_area} on {delivery_date} (issued {forecast_issue_date})")
            return pd.DataFrame()

        df = pd.DataFrame(all_data)

        # Aggregate safely across all regions using circular mean for direction
        avg_df = df.groupby("Hour").agg({
            "Wind 10m m/s": "mean",
            "Wind 80m m/s": "mean",
            "Wind Dir 80m": _circular_mean,
            "Wind Gusts 10m m/s": "mean",
            "Radiation (Flat) W/m2": "mean",
            "Radiation (Tilted) W/m2": "mean",
            "Direct W/m2": "mean",
            "Diffuse W/m2": "mean",
            "Sunshine min": "mean",
            "Cloud Cover %": "mean",
            "Cloud Cover Low %": "mean",
            "Cloud Cover Mid %": "mean",
            "Cloud Cover High %": "mean",
            "Temperature °C": "mean",
            "Snowfall cm": "mean",
            "Snow Depth meters": "mean",
            "CAPE J/kg": "max",
            "Freezing Level meters": "mean",
            "Visibility meters": "mean",
            "Weather Code": lambda x: pd.Series.mode(x).max() if not pd.Series.mode(x).empty else np.nan,
            "Is Day (1=Yes)": lambda x: pd.Series.mode(x).max() if not pd.Series.mode(x).empty else np.nan,
        }).reset_index()

        avg_df["Hour"] = avg_df["Hour"].apply(lambda h: f"{int(h):02d}:00")

        # Translate the numeric code into text!
        avg_df["Weather Condition"] = avg_df["Weather Code"].apply(get_weather_description)

        return avg_df

    query_key = f"{delivery_date}_{forecast_issue_date}"
    df = cache_layer._load_or_fetch("openmeteo", f"historical_forecast_{query_key}", market_area, delivery_date, fetch)

    if df is None or df.empty:
        logger.warning(
            f"No historical forecast data available for {market_area} on {delivery_date} (issued {forecast_issue_date})")
        return f"# No historical forecast available for {market_area} on {delivery_date} (issued {forecast_issue_date})"

    header = f"# Historical Weather Forecast for {market_area} on {delivery_date}\n"
    header += f"# Forecast issued: {forecast_issue_date}\n"
    header += "# Source: Open-Meteo Historical Forecast API averaged over multiple locations\n\n"

    return header + df.to_csv(index=False)


if __name__ == "__main__":
    import sys
    from datetime import timedelta
    from cache_layer import clear_cache
    deleted_count = clear_cache(source="openmeteo")
    print(f"Deleted {deleted_count} parquet files from the cache.")
    sqlite_cache = ".openmeteo_cache.sqlite"
    if os.path.exists(sqlite_cache):
        os.remove(sqlite_cache)
        print("Deleted Open-Meteo SQLite cache.")

    date = sys.argv[1] if len(sys.argv) > 1 else "2026-05-01"
    market_area = sys.argv[2] if len(sys.argv) > 2 else "CZ"

    print("\n=== get_wind_forecast ===")
    print(get_wind_forecast(date, market_area))

    print("\n=== get_solar_forecast ===")
    print(get_solar_forecast(date, market_area))

    print("\n=== get_weather_forecast ===")
    print(get_weather_forecast(date, market_area))

    print("\n=== get_historical_forecast ===")
    issue_date = (datetime.strptime(date, "%Y-%m-%d") - timedelta(days=1)).strftime("%Y-%m-%d")
    print(f"(Forecast issued: {issue_date})")
    print(get_historical_forecast(date, issue_date, market_area))

"""
Reference output:
=== get_wind_forecast ===
# Wind Forecast for CZ on 2026-05-01
# Source: Open-Meteo averaged over few locations
# Unit: m/s and Degrees

Hour,Wind 10m m/s,Wind 80m m/s,Wind 120m m/s,Wind Dir 10m,Wind Dir 80m,Wind Dir 120m,Wind Gusts 10m m/s
00:00,5.048864,13.106518,17.751484,79.72197,70.51635,68.920105,11.5199995
01:00,4.031579,11.552999,15.831097,103.7038,79.451035,79.29048,10.619999
02:00,3.8549676,10.124996,13.707363,95.94432,77.515594,75.87729,9.719999
03:00,4.4334936,11.123648,14.4249,76.71747,79.07419,78.012924,9.719999
04:00,3.902677,10.109263,13.82035,97.762085,80.30327,80.04813,9.36
05:00,4.614931,8.938228,11.800231,203.8162,63.445435,69.41766,8.999999
06:00,4.992321,7.669353,10.313526,175.51361,227.45454,57.986183,9.18
07:00,4.1934705,8.541393,11.37105,185.65495,226.63214,231.17145,9.18
08:00,3.441427,7.997975,11.295269,196.23564,213.64528,219.99939,9.18
09:00,7.0080433,8.277686,8.6855135,207.54268,209.15619,208.82625,15.839999
10:00,7.2310505,8.329422,8.692784,221.70908,221.07338,222.7926,17.64
11:00,7.601881,8.669317,9.016901,209.92278,211.12634,211.91318,18.18
12:00,9.042841,11.061826,11.061826,205.91829,207.09448,207.09448,20.880001
13:00,8.840166,10.154278,10.330865,193.14998,194.2478,194.3823,21.24
14:00,8.508041,9.980912,10.15968,179.42712,180.9786,181.05684,23.939999
15:00,10.645615,12.930993,13.176035,187.23523,188.83014,189.78195,21.96
16:00,11.187657,14.1382265,14.393513,14.160591,15.616419,16.249365,26.279999
17:00,10.941366,13.681196,14.056192,190.55501,188.21065,189.79614,25.02
18:00,11.545187,15.399469,15.8958435,203.18681,34.629192,34.76385,24.84
19:00,8.535991,12.772238,14.054724,197.31216,209.59743,210.16293,23.4
20:00,4.7541394,12.136092,14.661239,181.68318,203.98679,207.08113,16.38
21:00,5.9171143,11.113699,13.932528,175.04782,209.06848,215.17311,11.7
22:00,6.462873,13.830986,17.342058,174.3087,209.7,215.30128,13.139999
23:00,6.1866527,12.83063,16.477217,173.66754,214.16646,220.0499,13.5


=== get_solar_forecast ===
# Solar Forecast for CZ on 2026-05-01
# Source: Open-Meteo averaged over few locations
# Unit: W/m² for radiation, minutes for sunshine, % for clouds

Hour,Radiation (Flat) W/m2,Radiation (Tilted) W/m2,Direct W/m2,Diffuse W/m2,Sunshine min,Cloud Cover %,Cloud Cover Low %,Cloud Cover Mid %,Cloud Cover High %
00:00,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
01:00,0.0,0.0,0.0,0.0,0.0,0.6,0.0,0.0,0.6
02:00,0.0,0.0,0.0,0.0,0.0,12.6,1.4,9.8,2.4
03:00,0.0,0.0,0.0,0.0,0.0,18.2,3.8,16.2,0.4
04:00,0.0,0.0,0.0,0.0,0.0,19.0,8.6,18.2,0.0
05:00,0.0,0.0,0.0,0.0,0.0,25.6,11.8,24.2,0.0
06:00,2.4,2.226386,0.0,2.4,0.0,31.0,13.4,29.8,0.0
07:00,63.4,42.117886,18.4,45.0,42.950638,23.6,13.0,19.2,0.0
08:00,201.8,164.54037,106.4,95.4,60.0,33.0,16.8,29.0,0.0
09:00,350.2,338.86914,215.0,135.2,57.55896,22.8,0.0,22.8,0.0
10:00,509.8,538.96423,345.0,164.8,60.0,23.2,0.0,23.2,0.0
11:00,654.8,731.7619,485.2,169.6,60.0,26.0,0.0,26.0,0.0
12:00,747.4,860.65906,574.6,172.8,60.0,18.0,0.0,18.0,0.0
13:00,813.2,956.7244,662.2,151.0,60.0,7.6,1.4,7.6,0.0
14:00,814.0,959.39667,671.8,142.2,60.0,18.6,0.0,18.6,0.0
15:00,751.6,873.1499,613.6,138.0,60.0,3.4,2.2,1.2,0.0
16:00,661.2,746.8464,537.6,123.6,60.0,12.2,3.4,8.8,0.0
17:00,508.8,538.84436,375.4,133.4,60.0,19.8,19.8,0.0,0.0
18:00,359.8,344.08124,259.2,100.6,60.0,10.2,10.2,0.0,0.0
19:00,196.8,147.63756,125.2,71.6,60.0,6.8,0.6,6.2,0.0
20:00,56.6,30.857693,23.8,32.8,55.898632,4.4,0.0,4.4,0.0
21:00,0.8,0.7421287,0.0,0.8,0.0,0.0,0.0,0.0,0.0
22:00,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
23:00,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0


=== get_weather_forecast ===
# Weather Forecast for CZ on 2026-05-01
# Source: Open-Meteo averaged over multiple locations
# Unit: °C, mm, hPa, cm, WMO Code

Hour,Temperature °C,Feels Like °C,Precipitation mm,Pressure hPa,Snowfall cm,Precip Prob %,Snow Depth meters,Freezing Level meters,Visibility meters,CAPE J/kg,Weather Code,Is Day (1=Yes),Weather Condition
00:00,6.2697144,3.3916314,0.0,1030.6285,0.0,0.0,0.0,1835.7142,40631.43,0.0,0.0,0.0,Sunny/Clear
01:00,5.855428,3.0803397,0.0,1030.6857,0.0,0.0,0.0,1850.0,40302.855,0.0,0.0,0.0,Sunny/Clear
02:00,5.0054283,2.24141,0.0,1030.2572,0.0,0.0,0.0,1905.7142,38660.0,0.0,0.0,0.0,Sunny/Clear
03:00,4.291143,1.504908,0.0,1029.9857,0.0,0.0,0.0,1948.5714,36382.855,0.0,0.0,0.0,Sunny/Clear
04:00,4.041143,1.3965528,0.0,1030.0,0.0,0.0,0.0,2021.4286,35417.145,0.0,0.0,0.0,Sunny/Clear
05:00,3.8054287,1.1275903,0.0,1030.2429,0.0,0.0,0.0,1957.1428,34202.855,0.0,0.0,0.0,Sunny/Clear
06:00,3.7482858,1.073749,0.0,1030.6285,0.0,0.0,0.0,1977.1428,32888.57,0.0,0.0,1.0,Sunny/Clear
07:00,4.898286,2.4653625,0.0,1030.4714,0.0,0.0,0.0,2064.2856,33322.855,0.0,0.0,1.0,Sunny/Clear
08:00,7.648286,5.2089186,0.0,1029.9572,0.0,0.0,0.0,2055.7144,37045.715,0.0,0.0,1.0,Sunny/Clear
09:00,10.062572,7.4538774,0.0,1030.0714,0.0,0.0,0.0,2150.0,40857.145,0.0,0.0,1.0,Sunny/Clear
10:00,12.441142,9.924532,0.0,1029.6715,0.0,0.0,0.0,2234.2856,41660.0,0.0,0.0,1.0,Sunny/Clear
11:00,14.441142,12.551888,0.0,1028.9286,0.0,0.0,0.0,2248.5715,42451.43,10.0,0.0,1.0,Sunny/Clear
12:00,16.105429,14.602391,0.0,1028.7286,0.0,0.0,0.0,2354.2856,43574.285,20.0,0.0,1.0,Sunny/Clear
13:00,17.291143,15.896871,0.0,1028.2142,0.0,0.0,0.0,2445.7144,44811.43,20.0,0.0,1.0,Sunny/Clear
14:00,18.019714,16.566343,0.0,1027.4286,0.0,0.0,0.0,2487.1428,44931.43,20.0,0.0,1.0,Sunny/Clear
15:00,18.712572,16.774672,0.0,1026.6857,0.0,0.0,0.0,2627.1428,45254.285,20.0,0.0,1.0,Sunny/Clear
16:00,19.062572,16.708015,0.0,1026.3285,0.0,0.0,0.0,2680.0,45431.43,20.0,0.0,1.0,Sunny/Clear
17:00,19.176859,16.062475,0.0,1025.7142,0.0,0.0,0.0,2732.8572,45834.285,20.0,1.0,1.0,Mainly Sunny/Clear
18:00,18.798285,15.585823,0.0,1025.5857,0.0,0.0,0.0,2732.8572,45325.715,10.0,0.0,1.0,Sunny/Clear
19:00,18.05543,15.28608,0.0,1024.9572,0.0,0.0,0.0,2822.8572,44754.285,0.0,0.0,1.0,Sunny/Clear
20:00,15.941144,13.598195,0.0,1025.1715,0.0,0.0,0.0,2875.7144,43237.145,0.0,0.0,1.0,Sunny/Clear
21:00,13.641143,11.236684,0.0,1025.7429,0.0,0.0,0.0,2918.5715,42008.57,0.0,0.0,0.0,Sunny/Clear
22:00,11.962571,9.666709,0.0,1026.1715,0.0,0.0,0.0,2990.0,41174.285,0.0,0.0,0.0,Sunny/Clear
23:00,10.912572,8.721472,0.0,1026.4143,0.0,0.0,0.0,3017.1428,40548.57,0.0,0.0,0.0,Sunny/Clear


=== get_historical_forecast ===
(Forecast issued: 2026-04-30)
# Historical Weather Forecast for CZ on 2026-05-01
# Forecast issued: 2026-04-30
# Source: Open-Meteo Historical Forecast API averaged over multiple locations

Hour,Wind 10m m/s,Wind 80m m/s,Wind Dir 80m,Wind Gusts 10m m/s,Radiation (Flat) W/m2,Radiation (Tilted) W/m2,Direct W/m2,Diffuse W/m2,Sunshine min,Cloud Cover %,Cloud Cover Low %,Cloud Cover Mid %,Cloud Cover High %,Temperature °C,Snowfall cm,Snow Depth meters,CAPE J/kg,Freezing Level meters,Visibility meters,Weather Code,Is Day (1=Yes),Weather Condition
00:00,4.272464,9.946797,118.750206,8.382856,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,6.2697144,0.0,0.0,0.0,1835.7142,40631.43,0.0,0.0,Sunny/Clear
01:00,3.5968812,7.0294805,123.42245,7.508571,0.0,0.0,0.0,0.0,0.0,0.42857143,0.0,0.0,0.42857143,5.855428,0.0,0.0,0.0,1850.0,40302.855,0.0,0.0,Sunny/Clear
02:00,3.60895,5.2084165,161.85953,6.7885714,0.0,0.0,0.0,0.0,0.0,9.0,1.0,7.0,1.7142857,5.0054283,0.0,0.0,0.0,1905.7142,38660.0,0.0,0.0,Sunny/Clear
03:00,3.888752,5.4290953,196.2078,7.56,0.0,0.0,0.0,0.0,0.0,13.0,2.7142856,11.571428,0.2857143,4.291143,0.0,0.0,0.0,1948.5714,36382.855,0.0,0.0,Sunny/Clear
04:00,3.0880501,5.151717,210.02579,7.1485715,0.0,0.0,0.0,0.0,0.0,13.571428,6.142857,13.0,0.0,4.041143,0.0,0.0,0.0,2021.4286,35417.145,0.0,0.0,Sunny/Clear
05:00,3.670075,4.63474,148.23192,6.222857,0.0,0.0,0.0,0.0,0.0,18.285715,8.428572,17.285715,0.0,3.8054287,0.0,0.0,0.0,1957.1428,34202.855,0.0,0.0,Sunny/Clear
06:00,3.8612807,4.8987727,202.31828,7.3542857,2.2857144,2.1203675,0.0,2.2857144,0.0,22.142857,9.571428,21.285715,0.0,3.7482858,0.0,0.0,0.0,1977.1428,32888.57,0.0,1.0,Sunny/Clear
07:00,3.0691936,5.2995963,219.23738,6.6857142,65.42857,40.193943,22.571428,42.857143,47.82188,16.857143,9.285714,13.714286,0.0,4.898286,0.0,0.0,0.0,2064.2856,33322.855,0.0,1.0,Sunny/Clear
08:00,3.2049851,5.650795,194.23177,7.0971427,206.85715,165.69131,118.71429,88.14286,60.0,26.285715,14.714286,20.714285,0.0,7.648286,0.0,0.0,0.0,2055.7144,37045.715,0.0,1.0,Sunny/Clear
09:00,4.3479385,4.9339175,238.16592,10.542856,361.14285,350.2349,238.14285,123.0,58.2564,16.285715,0.0,16.285715,0.0,10.062572,0.0,0.0,0.0,2150.0,40857.145,0.0,1.0,Sunny/Clear
10:00,4.3938403,4.9541197,241.07042,11.468572,521.7143,555.9207,375.85715,145.85715,60.0,16.571428,0.0,16.571428,0.0,12.441142,0.0,0.0,0.0,2234.2856,41660.0,0.0,1.0,Sunny/Clear
11:00,5.1975403,6.0589943,235.73413,12.96,663.5714,746.5878,509.85715,153.71428,60.0,19.571428,1.0,18.571428,0.0,14.441142,0.0,0.0,10.0,2248.5715,42451.43,0.0,1.0,Sunny/Clear
12:00,6.416749,7.9450064,287.63565,15.325714,757.5714,877.8224,599.1429,158.42857,60.0,18.285715,5.428571,12.857142,0.0,16.105429,0.0,0.0,20.0,2354.2856,43574.285,0.0,1.0,Sunny/Clear
13:00,7.810562,9.342928,238.85402,17.485714,817.0,962.8211,667.8571,149.14285,60.0,10.142858,5.714286,5.428571,0.0,17.291143,0.0,0.0,20.0,2445.7144,44811.43,0.0,1.0,Sunny/Clear
14:00,8.459985,10.46412,250.48914,19.337141,815.0,959.8719,667.1429,147.85715,60.0,17.142857,3.857143,13.285714,0.0,18.019714,0.0,0.0,20.0,2487.1428,44931.43,0.0,1.0,Sunny/Clear
15:00,9.620295,12.175574,165.7864,19.74857,759.5714,884.49524,623.1429,136.42857,60.0,3.7142856,2.857143,0.85714287,0.0,18.712572,0.0,0.0,20.0,2627.1428,45254.285,0.0,1.0,Sunny/Clear
16:00,9.291947,12.130649,154.3691,21.908571,669.1429,758.88904,550.4286,118.71429,60.0,8.714286,2.4285715,6.285714,0.0,19.062572,0.0,0.0,20.0,2680.0,45431.43,0.0,1.0,Sunny/Clear
17:00,9.65286,11.945092,285.51395,21.291428,522.2857,557.4046,400.85715,121.42857,60.0,16.714285,16.714285,0.0,0.0,18.905428,0.0,0.0,20.0,2732.8572,45834.285,1.0,1.0,Mainly Sunny/Clear
18:00,10.539441,14.337584,118.23168,22.371428,369.85715,355.6817,274.14285,95.71429,60.0,7.285714,7.285714,0.0,0.0,18.712572,0.0,0.0,10.0,2732.8572,45325.715,0.0,1.0,Sunny/Clear
19:00,7.5849576,11.759959,177.65028,20.571428,204.71428,154.00925,135.42857,69.28571,60.0,4.857143,0.42857143,4.428571,0.0,17.669714,0.0,0.0,0.0,2822.8572,44754.285,0.0,1.0,Sunny/Clear
20:00,5.742124,11.218735,167.52469,14.502856,61.0,31.509,27.571428,33.42857,57.070454,3.142857,0.0,3.142857,0.0,15.726858,0.0,0.0,0.0,2875.7144,43237.145,0.0,1.0,Sunny/Clear
21:00,5.962413,10.353645,180.68678,11.571428,1.1428572,0.9302444,0.14285715,1.0,0.0,0.0,0.0,0.0,0.0,13.098287,0.0,0.0,0.0,2918.5715,42008.57,0.0,0.0,Sunny/Clear
22:00,5.3221464,9.872427,134.54028,10.954286,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,11.619715,0.0,0.0,0.0,2990.0,41174.285,0.0,0.0,Sunny/Clear
23:00,4.5431643,7.600928,236.95749,9.72,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,10.362572,0.0,0.0,0.0,3017.1428,40548.57,0.0,0.0,Sunny/Clear
"""
