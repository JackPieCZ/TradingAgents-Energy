# tests/agents/utils/test_system_data_tools.py
from unittest.mock import patch
from tradingagents.agents.utils.system_data_tools import (
    get_residual_load, get_actual_generation, get_load_forecast,
    get_cross_border_flows, get_outages
)

@patch('tradingagents.agents.utils.system_data_tools.route_to_vendor')
def test_system_data_routing(mock_route):
    mock_route.return_value = "mock_data"
    
    get_residual_load.invoke({"delivery_date": "2026-05-01", "market_area": "DE-LU"})
    mock_route.assert_called_with("get_residual_load", delivery_date="2026-05-01", market_area="DE-LU")
    
    get_actual_generation.invoke({"delivery_date": "2026-05-01", "market_area": "DE-LU"})
    mock_route.assert_called_with("get_actual_generation", delivery_date="2026-05-01", market_area="DE-LU")
    
    get_load_forecast.invoke({"delivery_date": "2026-05-01", "market_area": "DE-LU"})
    mock_route.assert_called_with("get_load_forecast", delivery_date="2026-05-01", market_area="DE-LU")

    get_cross_border_flows.invoke({"delivery_date": "2026-05-01", "market_area": "DE-LU"})
    mock_route.assert_called_with("get_cross_border_flows", delivery_date="2026-05-01", market_area="DE-LU")

    get_outages.invoke({"delivery_date": "2026-05-01", "market_area": "DE-LU"})
    mock_route.assert_called_with("get_outages", delivery_date="2026-05-01", market_area="DE-LU")
