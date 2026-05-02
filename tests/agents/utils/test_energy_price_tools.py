# tests/agents/utils/test_energy_price_tools.py
from unittest.mock import patch
from tradingagents.agents.utils.energy_price_tools import (
    get_day_ahead_prices, get_intraday_prices,
    get_intraday_auction_prices, get_imbalance_data
)
@patch('tradingagents.agents.utils.energy_price_tools.route_to_vendor')
def test_get_day_ahead_prices(mock_route):
    mock_route.return_value = "mock_data"
    result = get_day_ahead_prices.invoke({"delivery_date": "2026-05-01", "market_area": "DE-LU"})
    assert result == "mock_data"
    mock_route.assert_called_once_with("get_day_ahead_prices", delivery_date="2026-05-01", market_area="DE-LU")
@patch('tradingagents.agents.utils.energy_price_tools.route_to_vendor')
def test_get_intraday_prices(mock_route):
    mock_route.return_value = "mock_data"
    result = get_intraday_prices.invoke({"delivery_date": "2026-05-01", "market_area": "DE-LU"})
    assert result == "mock_data"
    mock_route.assert_called_once_with("get_intraday_prices", delivery_date="2026-05-01", market_area="DE-LU")
@patch('tradingagents.agents.utils.energy_price_tools.route_to_vendor')
def test_get_intraday_auction_prices(mock_route):
    mock_route.return_value = "mock_data"
    result = get_intraday_auction_prices.invoke({"delivery_date": "2026-05-01", "market_area": "DE-LU"})
    assert result == "mock_data"
    mock_route.assert_called_once_with("get_intraday_auction_prices", delivery_date="2026-05-01", market_area="DE-LU")
@patch('tradingagents.agents.utils.energy_price_tools.route_to_vendor')
def test_get_imbalance_data(mock_route):
    mock_route.return_value = "mock_data"
    result = get_imbalance_data.invoke({"delivery_date": "2026-05-01", "market_area": "DE-LU"})
    assert result == "mock_data"
    mock_route.assert_called_once_with("get_balancing_data", delivery_date="2026-05-01", market_area="DE-LU")
