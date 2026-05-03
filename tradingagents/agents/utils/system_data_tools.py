"""Grid system state tools for the System State Analyst."""
from langchain_core.tools import tool
from tradingagents.dataflows.interface import route_to_vendor

@tool
def get_residual_load(delivery_date: str, market_area: str = "CZ") -> str:
    """Fetch residual load forecast (total load minus wind minus solar).
    High residual load = tight conventional capacity = steep merit order = price sensitive to shocks.
    Low residual load = abundant renewables = potential negative prices."""
    return route_to_vendor("get_residual_load", delivery_date=delivery_date, market_area=market_area)

@tool
def get_actual_generation(delivery_date: str, market_area: str = "CZ") -> str:
    """Fetch actual generation breakdown by fuel type (wind, solar, gas, coal, etc.).
    Use to assess merit order position and available conventional capacity."""
    return route_to_vendor("get_actual_generation", delivery_date=delivery_date, market_area=market_area)

@tool
def get_load_forecast(delivery_date: str, market_area: str = "CZ") -> str:
    """Fetch the day-ahead total load (demand) forecast in MW."""
    return route_to_vendor("get_load_forecast", delivery_date=delivery_date, market_area=market_area)

@tool
def get_cross_border_flows(delivery_date: str, market_area: str = "CZ") -> str:
    """Fetch cross-border physical power flows with neighboring bidding zones.
    Positive = import into zone, Negative = export. Includes NTC capacity where available."""
    return route_to_vendor("get_cross_border_flows", delivery_date=delivery_date, market_area=market_area)

@tool
def get_outages(delivery_date: str, market_area: str = "CZ") -> str:
    """Fetch planned and unplanned generation unit outages (REMIT UMMs).
    Large outages tighten supply and can push prices up significantly."""
    return route_to_vendor("get_outages", delivery_date=delivery_date, market_area=market_area)
