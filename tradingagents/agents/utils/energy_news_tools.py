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
