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

    date = sys.argv[1] if len(sys.argv) > 1 else "2026-04-28"
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

    deleted_count = clear_cache(source="openmeteo")
    print(f"Deleted {deleted_count} parquet files from the cache.")

"""
Reference output:
=== get_wind_forecast ===
# Wind Forecast for CZ on 2026-04-28
# Source: Open-Meteo averaged over few locations
# Unit: m/s and Degrees

Hour,Wind 10m m/s,Wind 80m m/s,Wind 120m m/s,Wind Dir 10m,Wind Dir 80m,Wind Dir 120m,Wind Gusts 10m m/s
00:00,7.475976,20.346153,,80.519714,72.32172,,12.599999
01:00,7.4327326,20.98173,,94.20111,88.69873,,13.68
02:00,6.964756,18.674423,,105.65933,95.02109,,12.599999
03:00,6.4158287,16.985306,,115.31082,104.57782,,11.16
04:00,5.5959573,16.281506,,116.690765,102.99225,,10.98
05:00,4.729927,14.096548,,134.95538,108.93744,,9.18
06:00,4.555111,12.776284,,143.02213,112.66171,,7.74
07:00,4.2856627,12.03504,,138.90771,111.42938,,7.56
08:00,3.944734,8.784254,,118.635895,99.867584,,10.619999
09:00,5.2736006,8.118663,,82.7731,85.06204,,15.119999
10:00,6.6837535,9.021767,,75.87518,77.986115,,19.079998
11:00,7.0197563,9.389641,,82.21365,83.1095,,20.699999
12:00,6.6863604,8.840338,,84.73602,85.063446,,21.059998
13:00,6.667797,8.936132,,78.88449,79.911194,,21.599998
14:00,6.4676166,8.583071,,62.118652,63.833008,,22.5
15:00,7.6081533,9.874218,,348.8099,359.824,,23.039999
16:00,15.444936,21.132053,,12.173553,14.651764,,34.199997
17:00,17.890244,25.783886,,24.781311,26.742554,,41.939995
18:00,14.72084,21.674377,,28.480774,30.157043,,37.8
19:00,13.918633,23.167643,,35.886017,38.84143,,33.3
20:00,12.717754,24.63292,,38.69919,41.64322,,28.259998
21:00,11.445945,24.918352,,49.5343,51.779907,,23.399998
22:00,11.227539,25.078026,,56.72699,60.40515,,21.78
23:00,9.715631,23.395401,,66.459595,71.15576,,20.880001


=== get_solar_forecast ===
# Solar Forecast for CZ on 2026-04-28
# Source: Open-Meteo averaged over few locations
# Unit: W/m² for radiation, minutes for sunshine, % for clouds

Hour,Radiation (Flat) W/m2,Radiation (Tilted) W/m2,Direct W/m2,Diffuse W/m2,Sunshine min,Cloud Cover %,Cloud Cover Low %,Cloud Cover Mid %,Cloud Cover High %
00:00,0.0,0.0,0.0,0.0,0.0,40.8,0.0,9.6,36.4
01:00,0.0,0.0,0.0,0.0,0.0,73.6,0.0,20.6,69.2
02:00,0.0,0.0,0.0,0.0,0.0,61.8,0.0,18.6,54.4
03:00,0.0,0.0,0.0,0.0,0.0,62.4,0.0,7.4,60.4
04:00,0.0,0.0,0.0,0.0,0.0,82.6,0.0,9.8,80.0
05:00,0.0,0.0,0.0,0.0,0.0,100.0,0.0,12.6,100.0
06:00,1.8,1.2987251,0.0,1.8,0.0,99.8,0.0,13.4,99.8
07:00,60.0,41.67979,15.4,44.6,35.63071,100.0,0.0,19.0,100.0
08:00,192.0,161.18571,92.6,99.4,57.58959,97.2,0.0,19.8,96.6
09:00,364.0,359.1822,239.8,124.2,60.0,72.6,0.0,14.6,66.2
10:00,534.6,582.3539,411.2,123.4,60.0,55.0,0.0,22.6,36.8
11:00,667.8,764.76416,533.4,134.4,60.0,59.2,0.0,15.0,48.4
12:00,763.6,898.64514,624.0,139.6,60.0,62.8,0.0,25.2,48.2
13:00,804.4,952.86456,647.2,157.2,60.0,64.4,0.0,24.2,48.6
14:00,797.0,941.0714,634.4,162.6,60.0,89.2,0.0,37.8,70.0
15:00,721.2,830.3169,534.2,187.0,60.0,76.2,0.0,29.0,59.8
16:00,639.4,721.2463,485.8,153.6,60.0,87.0,0.2,18.8,83.4
17:00,492.8,524.2755,347.4,145.4,60.0,83.2,0.0,15.6,77.6
18:00,348.6,337.54297,240.4,108.2,60.0,42.0,0.0,2.4,41.4
19:00,192.8,146.55028,123.0,69.8,60.0,20.8,0.0,5.4,16.4
20:00,54.4,26.088114,26.8,27.6,58.848885,32.0,0.0,7.8,26.2
21:00,0.6,0.37106434,0.0,0.6,0.0,28.0,0.0,5.0,25.8
22:00,0.0,0.0,0.0,0.0,0.0,29.2,0.0,2.6,29.0
23:00,0.0,0.0,0.0,0.0,0.0,21.8,0.0,0.0,21.8


=== get_weather_forecast ===
# Weather Forecast for CZ on 2026-04-28
# Source: Open-Meteo averaged over multiple locations
# Unit: °C, mm, hPa, cm, WMO Code

Hour,Temperature °C,Feels Like °C,Precipitation mm,Pressure hPa,Snowfall cm,Precip Prob %,Snow Depth meters,Freezing Level meters,Visibility meters,CAPE J/kg,Weather Code,Is Day (1=Yes),Weather Condition
00:00,7.698857,4.309916,0.0,1021.25714,0.0,,0.0,,,,0.0,,Sunny/Clear
01:00,6.7702856,3.5056674,0.0,1021.5143,0.0,,0.0,,,,3.0,,Cloudy
02:00,5.6845713,2.6971135,0.0,1021.62854,0.0,,0.0,,,,3.0,,Cloudy
03:00,4.5845714,1.6373354,0.0,1021.58575,0.0,,0.0,,,,3.0,,Cloudy
04:00,4.241714,1.3043989,0.0,1021.5571,0.0,,0.0,,,,3.0,,Cloudy
05:00,3.7274284,0.7808469,0.0,1021.58575,0.0,,0.0,,,,3.0,,Cloudy
06:00,3.4988573,0.50005895,0.0,1021.6429,0.0,,0.0,,,,3.0,,Cloudy
07:00,5.256,2.107778,0.0,1021.9286,0.0,,0.0,,,,3.0,,Cloudy
08:00,7.248857,4.4179206,0.0,1022.3571,0.0,,0.0,,,,3.0,,Cloudy
09:00,9.927428,6.8400154,0.0,1022.41425,0.0,,0.0,,,,3.0,,Cloudy
10:00,12.098857,8.652492,0.0,1022.2143,0.0,,0.0,,,,3.0,,Cloudy
11:00,13.734571,10.796479,0.0,1022.12854,0.0,,0.0,,,,3.0,,Cloudy
12:00,14.906,12.522659,0.0,1021.81433,0.0,,0.0,,,,3.0,,Cloudy
13:00,15.663142,13.544063,0.0,1021.3,0.0,,0.0,,,,2.0,,Partly Cloudy
14:00,15.813143,13.561243,0.0,1021.1429,0.0,,0.0,,,,3.0,,Cloudy
15:00,16.156,13.266053,0.0,1020.81433,0.0,,0.0,,,,3.0,,Cloudy
16:00,15.727429,11.704126,0.0,1020.67145,0.0,,0.0,,,,3.0,,Cloudy
17:00,15.056,10.590757,0.0,1020.4571,0.0,,0.0,,,,3.0,,Cloudy
18:00,14.520286,10.154028,0.0,1020.2857,0.0,,0.0,,,,0.0,,Sunny/Clear
19:00,13.148857,8.733199,0.0,1020.7286,0.0,,0.0,,,,0.0,,Sunny/Clear
20:00,11.577429,7.2063937,0.0,1021.34283,0.0,,0.0,,,,0.0,,Sunny/Clear
21:00,9.977429,5.641704,0.0,1022.2714,0.0,,0.0,,,,0.0,,Sunny/Clear
22:00,8.813143,4.17525,0.0,1023.0286,0.0,,0.0,,,,0.0,,Sunny/Clear
23:00,7.748857,3.254647,0.0,1023.5714,0.0,,0.0,,,,0.0,,Sunny/Clear


=== get_historical_forecast ===
(Forecast issued: 2026-04-27)
# Historical Weather Forecast for CZ on 2026-04-28
# Forecast issued: 2026-04-27
# Source: Open-Meteo Historical Forecast API averaged over multiple locations

Hour,Wind 10m m/s,Wind 80m m/s,Wind Dir 80m,Wind Gusts 10m m/s,Radiation (Flat) W/m2,Radiation (Tilted) W/m2,Direct W/m2,Diffuse W/m2,Sunshine min,Cloud Cover %,Cloud Cover Low %,Cloud Cover Mid %,Cloud Cover High %,Temperature °C,Snowfall cm,Snow Depth meters,CAPE J/kg,Freezing Level meters,Visibility meters,Weather Code,Is Day (1=Yes),Weather Condition
00:00,3.9436078,9.384479,57.29956,9.102857,0.0,0.0,0.0,0.0,0.0,76.85714,0.0,65.14286,57.285713,8.041142,0.0,0.0,0.0,2050.0,41071.43,3.0,0.0,Cloudy
01:00,4.236441,8.686125,58.83426,8.177142,0.0,0.0,0.0,0.0,0.0,84.28571,0.0,65.14286,67.0,7.398286,0.0,0.0,0.0,1997.1428,41328.57,3.0,0.0,Cloudy
02:00,4.34288,7.416153,68.78735,8.588572,0.0,0.0,0.0,0.0,0.0,64.57143,0.85714287,43.142857,40.0,6.262572,0.0,0.0,0.0,1951.4286,40471.43,3.0,0.0,Cloudy
03:00,4.6172996,8.162727,47.52661,9.051429,0.0,0.0,0.0,0.0,0.0,77.0,1.2857143,33.142857,61.42857,5.476857,0.0,0.0,0.0,1915.7142,39925.715,3.0,0.0,Cloudy
04:00,4.554168,7.8802023,65.33307,9.308571,0.0,0.0,0.0,0.0,0.0,89.85714,0.0,55.857143,89.57143,4.9554286,0.0,0.0,0.0,1937.1428,39580.0,3.0,0.0,Cloudy
05:00,3.7476676,6.7071657,63.046356,8.639999,0.0,0.0,0.0,0.0,0.0,94.28571,0.0,61.142857,94.28571,4.076857,0.0,0.0,0.0,2040.0,38980.0,3.0,0.0,Cloudy
06:00,3.7430663,6.681762,55.990936,8.022857,1.4285715,1.0601838,0.0,1.4285715,0.0,97.14286,0.0,70.14286,97.14286,3.884,0.0,0.0,0.0,2012.8572,38628.57,3.0,1.0,Cloudy
07:00,3.4359362,7.153809,49.51657,7.662857,53.142857,42.69576,7.285714,45.857143,6.603526,92.57143,0.0,72.14286,81.0,4.9482856,0.0,0.0,0.0,1982.8572,38997.145,3.0,1.0,Cloudy
08:00,3.717157,6.264454,60.514343,8.897142,166.14285,144.27242,52.714287,113.42857,45.557037,99.42857,0.0,74.71429,98.0,7.2911425,0.0,0.0,0.0,1994.2858,39751.43,3.0,1.0,Cloudy
09:00,5.581482,6.9465766,51.33307,12.291429,314.7143,304.05646,146.85715,167.85715,58.84329,96.0,0.0,72.57143,84.0,9.491143,0.0,0.0,0.0,1957.1428,41591.43,3.0,1.0,Cloudy
10:00,6.703014,8.310309,48.153717,15.531428,464.57144,484.30978,255.28572,209.28572,60.0,100.0,0.0,85.14286,100.0,11.384001,0.0,0.0,0.0,1862.8572,42382.855,3.0,1.0,Cloudy
11:00,8.161706,10.286391,72.339966,19.08,575.8571,620.8764,317.7143,258.14285,60.0,85.14286,0.0,70.42857,63.857143,13.384001,0.0,0.0,20.0,1852.8572,43371.43,3.0,1.0,Cloudy
12:00,9.53417,11.968923,67.782745,19.697142,712.2857,809.95636,485.57144,226.71428,60.0,84.85714,3.142857,71.71429,44.285713,14.569715,0.0,0.0,20.0,1855.7142,43980.0,3.0,1.0,Cloudy
13:00,11.503855,14.336622,55.333374,20.10857,749.5714,855.7028,498.0,251.57143,60.0,94.71429,15.571428,81.85714,60.57143,15.391144,0.0,0.0,30.0,1857.1428,44842.855,3.0,1.0,Cloudy
14:00,11.417031,14.36894,48.352478,22.679998,698.0,771.3585,386.0,312.0,60.0,88.57143,11.0,71.85714,66.28571,15.748285,0.0,0.0,20.0,1892.8572,46228.57,3.0,1.0,Cloudy
15:00,12.428068,16.450241,51.549957,24.068571,669.0,740.88007,397.7143,271.2857,60.0,84.57143,5.714286,66.42857,71.42857,15.841143,0.0,0.0,20.0,1897.1428,46082.855,3.0,1.0,Cloudy
16:00,14.189132,19.111408,43.54251,26.177141,574.0,619.00964,327.0,247.0,60.0,93.28571,6.285714,74.71429,83.42857,15.655428,0.0,0.0,20.0,1975.7142,46028.57,3.0,1.0,Cloudy
17:00,14.616331,20.490965,37.106598,27.102856,439.42856,451.2311,225.71428,213.71428,60.0,78.85714,1.0,29.0,56.142857,15.376857,0.0,0.0,20.0,1942.8572,46611.43,3.0,1.0,Cloudy
18:00,14.36633,21.318127,49.3396,29.314285,347.85715,337.56,229.71428,118.14286,60.0,68.42857,0.0,17.857143,53.285713,14.748286,0.0,0.0,10.0,1944.2858,46365.715,2.0,1.0,Partly Cloudy
19:00,14.464964,23.41328,59.281647,30.342855,192.28572,149.58842,116.14286,76.14286,60.0,46.285713,0.0,18.857143,30.428572,13.5482855,0.0,0.0,0.0,1934.2858,46120.0,0.0,1.0,Sunny/Clear
20:00,10.973097,21.95804,42.4765,27.617142,53.142857,30.587269,20.571428,32.57143,49.988087,32.857143,0.0,0.0,32.714287,11.969714,0.0,0.0,0.0,1975.7142,44840.0,3.0,1.0,Cloudy
21:00,11.927125,24.747923,51.952484,22.937143,0.5714286,0.3975689,0.0,0.5714286,0.0,14.285714,0.0,0.0,14.285714,10.134001,0.0,0.0,0.0,1894.2858,44008.57,0.0,0.0,Sunny/Clear
22:00,11.267927,23.366777,59.80191,23.194286,0.0,0.0,0.0,0.0,0.0,34.714287,0.0,0.0,34.714287,8.898286,0.0,0.0,0.0,1882.8572,43854.285,0.0,0.0,Sunny/Clear
23:00,9.353724,19.924677,63.94806,22.679998,0.0,0.0,0.0,0.0,0.0,42.0,0.0,4.428571,42.0,7.6268573,0.0,0.0,0.0,1890.0,43071.43,0.0,0.0,Sunny/Clear
"""
