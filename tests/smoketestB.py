from tradingagents.agents.schemas import (
    PowerTradingAction, MarketRegime,
    PowerTraderProposal, PowerPortfolioDecision,
    render_power_trader_proposal, render_power_pm_decision
)
from tradingagents.agents.utils.rating import parse_rating

# Test power rating parsing
assert parse_rating("**Action**: NoTrade") == "NoTrade"
assert parse_rating("**Action**: Buy") == "Buy"
assert parse_rating("**Action**: Reduce") == "Reduce"
assert parse_rating("**Rating**: Sell") == "Sell"  # backward compat

# Test schema instantiation
proposal = PowerTraderProposal(
    action=PowerTradingAction.BUY,
    reasoning="Strong downward wind revision",
    volume_mw=10.0,
    limit_price_eur=45.50,
    execution_strategy="passive_limit",
    urgency="medium"
)
print(proposal)
rendered = render_power_trader_proposal(proposal)
print(rendered)
assert "10.0 MW" in rendered
assert "45.5" in rendered
print("SCHEMA TEST PASSED")