# Energy Tool Files Implementation Plan
>
> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.
**Goal:** Redesign Phase 1 data methods into LangChain-compatible tools that power-market-focused agents can call.
**Papers to re-read before starting**: Kup22, Kie17, Kre21b, Hir22, Kat20 in D:\TradingAgents-private\research\mds
**Architecture:** We will create four new tool modules replacing the old equity-focused tools. Each file exposes functions decorated with `@tool` that proxy requests to `route_to_vendor` from `tradingagents.dataflows.interface`. Tests will use `unittest.mock.patch` to verify routing behavior.
**Tech Stack:** Python 3, LangChain (`@tool`), `pytest`, `unittest.mock`
---

### Task 1: Create Energy Price Tools

**Files:**

- Create: `tradingagents/agents/utils/energy_price_tools.py`
- Create: `tests/agents/utils/test_energy_price_tools.py`
- [ ] **Step 1: Write the failing test**

```python
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
- [ ] Step 2: Run test to verify it fails
Run: /mnt/c/ProgramData/miniconda3/envs/tradingagents/python.exe -m pytest tests/agents/utils/test_energy_price_tools.py -v
Expected: FAIL with "No module named 'tradingagents.agents.utils.energy_price_tools'"
- [ ] Step 3: Write minimal implementation
# tradingagents/agents/utils/energy_price_tools.py
"""Energy price data tools for analyst agents."""
from langchain_core.tools import tool
from tradingagents.dataflows.interface import route_to_vendor
@tool
def get_day_ahead_prices(delivery_date: str, market_area: str = "DE-LU") -> str:
    """Fetch day-ahead auction clearing prices for a delivery date and bidding zone.
    Returns hourly prices in EUR/MWh. Use this to establish the price baseline
    that intraday trading operates around."""
    return route_to_vendor("get_day_ahead_prices", delivery_date=delivery_date, market_area=market_area)
@tool
def get_intraday_prices(delivery_date: str, market_area: str = "DE-LU") -> str:
    """Fetch intraday continuous market prices (VWAP, volume, spread metrics)
    for a delivery date. Shows how prices have moved relative to day-ahead."""
    return route_to_vendor("get_intraday_prices", delivery_date=delivery_date, market_area=market_area)
@tool
def get_intraday_auction_prices(delivery_date: str, market_area: str = "DE-LU") -> str:
    """Fetch IDA (Intraday Auction) clearing prices — IDA1, IDA2, IDA3.
    These sequential auctions provide price discovery between DA and delivery."""
    return route_to_vendor("get_intraday_auction_prices", delivery_date=delivery_date, market_area=market_area)
@tool
def get_imbalance_data(delivery_date: str, market_area: str = "DE-LU") -> str:
    """Fetch imbalance settlement prices and volumes. Imbalance price is
    the penalty for positions not closed before gate closure."""
    return route_to_vendor("get_balancing_data", delivery_date=delivery_date, market_area=market_area)
- [ ] Step 4: Run test to verify it passes
Run: /mnt/c/ProgramData/miniconda3/envs/tradingagents/python.exe -m pytest tests/agents/utils/test_energy_price_tools.py -v
Expected: PASS
- [ ] Step 5: Commit
git add tests/agents/utils/test_energy_price_tools.py tradingagents/agents/utils/energy_price_tools.py
git commit -m "feat: add energy price tools for analyst agents"
---
Task 2: Create System Data Tools
Files:
- Create: tradingagents/agents/utils/system_data_tools.py
- Create: tests/agents/utils/test_system_data_tools.py
- [ ] Step 1: Write the failing test
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
- [ ] Step 2: Run test to verify it fails
Run: /mnt/c/ProgramData/miniconda3/envs/tradingagents/python.exe -m pytest tests/agents/utils/test_system_data_tools.py -v
Expected: FAIL with "No module named 'tradingagents.agents.utils.system_data_tools'"
- [ ] Step 3: Write minimal implementation
# tradingagents/agents/utils/system_data_tools.py
"""Grid system state tools for the System State Analyst."""
from langchain_core.tools import tool
from tradingagents.dataflows.interface import route_to_vendor
@tool
def get_residual_load(delivery_date: str, market_area: str = "DE-LU") -> str:
    """Fetch residual load forecast (total load minus wind minus solar).
    High residual load = tight conventional capacity = steep merit order = price sensitive to shocks.
    Low residual load = abundant renewables = potential negative prices."""
    return route_to_vendor("get_residual_load", delivery_date=delivery_date, market_area=market_area)
@tool
def get_actual_generation(delivery_date: str, market_area: str = "DE-LU") -> str:
    """Fetch actual generation breakdown by fuel type (wind, solar, gas, coal, etc.).
    Use to assess merit order position and available conventional capacity."""
    return route_to_vendor("get_actual_generation", delivery_date=delivery_date, market_area=market_area)
@tool
def get_load_forecast(delivery_date: str, market_area: str = "DE-LU") -> str:
    """Fetch the day-ahead total load (demand) forecast in MW."""
    return route_to_vendor("get_load_forecast", delivery_date=delivery_date, market_area=market_area)
@tool
def get_cross_border_flows(delivery_date: str, market_area: str = "DE-LU") -> str:
    """Fetch cross-border physical power flows with neighboring bidding zones.
    Positive = import into zone, Negative = export. Includes NTC capacity where available."""
    return route_to_vendor("get_cross_border_flows", delivery_date=delivery_date, market_area=market_area)
@tool
def get_outages(delivery_date: str, market_area: str = "DE-LU") -> str:
    """Fetch planned and unplanned generation unit outages (REMIT UMMs).
    Large outages tighten supply and can push prices up significantly."""
    return route_to_vendor("get_outages", delivery_date=delivery_date, market_area=market_area)
- [ ] Step 4: Run test to verify it passes
Run: /mnt/c/ProgramData/miniconda3/envs/tradingagents/python.exe -m pytest tests/agents/utils/test_system_data_tools.py -v
Expected: PASS
- [ ] Step 5: Commit
git add tests/agents/utils/test_system_data_tools.py tradingagents/agents/utils/system_data_tools.py
git commit -m "feat: add system data tools for System State Analyst"
---
Task 3: Create Weather & Forecast Tools
Files:
- Create: tradingagents/agents/utils/weather_tools.py
- Create: tests/agents/utils/test_weather_tools.py
- [ ] Step 1: Write the failing test
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
- [ ] Step 2: Run test to verify it fails
Run: /mnt/c/ProgramData/miniconda3/envs/tradingagents/python.exe -m pytest tests/agents/utils/test_weather_tools.py -v
Expected: FAIL with "No module named 'tradingagents.agents.utils.weather_tools'"
- [ ] Step 3: Write minimal implementation
# tradingagents/agents/utils/weather_tools.py
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
- [ ] Step 4: Run test to verify it passes
Run: /mnt/c/ProgramData/miniconda3/envs/tradingagents/python.exe -m pytest tests/agents/utils/test_weather_tools.py -v
Expected: PASS
- [ ] Step 5: Commit
git add tests/agents/utils/test_weather_tools.py tradingagents/agents/utils/weather_tools.py
git commit -m "feat: add weather and forecast tools for Weather Analyst"
---
Task 4: Create Energy News Tools
Files:
- Create: tradingagents/agents/utils/energy_news_tools.py
- Create: tests/agents/utils/test_energy_news_tools.py
- [ ] Step 1: Write the failing test
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
- [ ] Step 2: Run test to verify it fails
Run: /mnt/c/ProgramData/miniconda3/envs/tradingagents/python.exe -m pytest tests/agents/utils/test_energy_news_tools.py -v
Expected: FAIL with "No module named 'tradingagents.agents.utils.energy_news_tools'"
- [ ] Step 3: Write minimal implementation
# tradingagents/agents/utils/energy_news_tools.py
"""Energy news and regulatory tools for the News & Regulatory Analyst."""
from langchain_core.tools import tool
from tradingagents.dataflows.interface import route_to_vendor
@tool
def get_outage_notifications(delivery_date: str, market_area: str = "DE-LU") -> str:
    """Fetch REMIT urgent market messages (UMMs) about generation unit outages.
    Includes planned maintenance and unplanned outages with MW unavailable."""
    return route_to_vendor("get_outage_notifications", delivery_date=delivery_date, market_area=market_area)
@tool
def get_actual_load(delivery_date: str, market_area: str = "DE-LU") -> str:
    """Fetch actual realized total load (demand) for context on demand patterns."""
    return route_to_vendor("get_actual_load", delivery_date=delivery_date, market_area=market_area)
- [ ] Step 4: Run test to verify it passes
Run: /mnt/c/ProgramData/miniconda3/envs/tradingagents/python.exe -m pytest tests/agents/utils/test_energy_news_tools.py -v
Expected: PASS
- [ ] Step 5: Commit
git add tests/agents/utils/test_energy_news_tools.py tradingagents/agents/utils/energy_news_tools.py
git commit -m "feat: add energy news tools and REMIT endpoints"
