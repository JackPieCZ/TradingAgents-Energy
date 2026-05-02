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
