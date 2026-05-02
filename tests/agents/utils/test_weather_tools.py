# tests/agents/utils/test_weather_tools.py
from unittest.mock import patch
from tradingagents.agents.utils.weather_tools import (
    get_wind_forecast, get_solar_forecast, get_generation_forecast,
    get_forecast_updates, get_weather_forecast, get_historical_forecast
)

@patch('tradingagents.agents.utils.weather_tools.route_to_vendor')
def test_weather_data_routing(mock_route):
    mock_route.return_value = "mock_data"
    
    get_wind_forecast.invoke({"delivery_date": "2026-05-01", "market_area": "DE-LU"})
    mock_route.assert_called_with("get_wind_forecast", delivery_date="2026-05-01", market_area="DE-LU")
    
    get_solar_forecast.invoke({"delivery_date": "2026-05-01", "market_area": "DE-LU"})
    mock_route.assert_called_with("get_solar_forecast", delivery_date="2026-05-01", market_area="DE-LU")
    
    get_generation_forecast.invoke({"delivery_date": "2026-05-01", "market_area": "DE-LU"})
    mock_route.assert_called_with("get_generation_forecast", delivery_date="2026-05-01", market_area="DE-LU")

    get_forecast_updates.invoke({"delivery_date": "2026-05-01", "market_area": "DE-LU"})
    mock_route.assert_called_with("get_forecast_updates", delivery_date="2026-05-01", market_area="DE-LU")

    get_weather_forecast.invoke({"delivery_date": "2026-05-01", "market_area": "DE-LU"})
    mock_route.assert_called_with("get_weather_forecast", delivery_date="2026-05-01", market_area="DE-LU")

    get_historical_forecast.invoke({"delivery_date": "2026-05-01", "market_area": "DE-LU"})
    mock_route.assert_called_with("get_historical_forecast", delivery_date="2026-05-01", forecast_issue_date="2026-04-30", market_area="DE-LU")
