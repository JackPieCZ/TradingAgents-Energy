# tests/agents/utils/test_energy_news_tools.py
from unittest.mock import patch
from tradingagents.agents.utils.energy_news_tools import (
    get_outage_notifications, get_actual_load
)

@patch('tradingagents.agents.utils.energy_news_tools.route_to_vendor')
def test_energy_news_routing(mock_route):
    mock_route.return_value = "mock_data"
    
    get_outage_notifications.invoke({"delivery_date": "2026-05-01", "market_area": "DE-LU"})
    mock_route.assert_called_with("get_outage_notifications", delivery_date="2026-05-01", market_area="DE-LU")
    
    get_actual_load.invoke({"delivery_date": "2026-05-01", "market_area": "DE-LU"})
    mock_route.assert_called_with("get_actual_load", delivery_date="2026-05-01", market_area="DE-LU")
