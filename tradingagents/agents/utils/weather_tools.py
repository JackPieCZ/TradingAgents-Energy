"""Weather and renewable forecast tools for the Weather & Forecast Analyst."""
from langchain_core.tools import tool
from tradingagents.dataflows.interface import route_to_vendor

@tool
def get_wind_forecast(delivery_date: str, market_area: str = "DE-LU") -> str:
    """Fetch wind speed forecasts at turbine hub heights (80m, 120m) averaged
    across capacity-weighted representative locations. Includes wind direction
    and gust data. Key input for wind power production estimation."""
    return route_to_vendor("get_wind_forecast", delivery_date=delivery_date, market_area=market_area)

@tool
def get_solar_forecast(delivery_date: str, market_area: str = "DE-LU") -> str:
    """Fetch solar irradiance forecasts (GHI, DNI, DHI, tilted) and cloud cover
    averaged across representative PV locations. Key input for solar production estimation."""
    return route_to_vendor("get_solar_forecast", delivery_date=delivery_date, market_area=market_area)

@tool
def get_generation_forecast(delivery_date: str, market_area: str = "DE-LU") -> str:
    """Fetch the TSO's official day-ahead wind and solar generation forecast in MW.
    Compare this with weather data to assess forecast accuracy."""
    return route_to_vendor("get_generation_forecast", delivery_date=delivery_date, market_area=market_area)

@tool
def get_forecast_updates(delivery_date: str, market_area: str = "DE-LU") -> str:
    """Fetch intraday updates to the renewable generation forecast and compute
    deltas vs day-ahead forecast. CRITICAL SIGNAL: positive wind delta = more wind
    than expected = downward price pressure. This is the primary alpha source."""
    return route_to_vendor("get_forecast_updates", delivery_date=delivery_date, market_area=market_area)

@tool
def get_weather_forecast(delivery_date: str, market_area: str = "DE-LU") -> str:
    """Fetch general weather data: temperature, precipitation, cloud cover, pressure.
    Temperature affects demand (heating/cooling). Precipitation affects hydro and PV."""
    return route_to_vendor("get_weather_forecast", delivery_date=delivery_date, market_area=market_area)

@tool
def get_historical_forecast(delivery_date: str, market_area: str = "DE-LU") -> str:
    """Fetch what yesterday's weather forecast predicted for today. Compare with
    today's forecast to identify forecast revisions — the trading signal per Kup22.
    A large revision means the market has not yet fully priced in the new information."""
    from datetime import datetime, timedelta
    issue_date = (datetime.strptime(delivery_date, "%Y-%m-%d") - timedelta(days=1)).strftime("%Y-%m-%d")
    return route_to_vendor("get_historical_forecast",
                          delivery_date=delivery_date,
                          forecast_issue_date=issue_date,
                          market_area=market_area)
