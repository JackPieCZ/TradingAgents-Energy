"""Trader: turns the Research Manager's investment plan into a concrete transaction proposal."""

from __future__ import annotations

import functools

from langchain_core.messages import AIMessage

from tradingagents.agents.schemas import TraderProposal, render_trader_proposal
from tradingagents.agents.utils.agent_utils import build_instrument_context
from tradingagents.agents.utils.structured import (
    bind_structured,
    invoke_structured_or_freetext,
)


def create_trader_exchange(llm):
    structured_llm = bind_structured(llm, TraderProposal, "Trader")

    def trader_node(state, name):
        company_name = state["company_of_interest"]
        instrument_context = build_instrument_context(company_name)
        investment_plan = state["investment_plan"]

        messages = [
            {
                "role": "system",
                "content": (
                    "zYou are a trading agent analyzing market data to make investment decisions. "
                    "Based on your analysis, provide a specific recommendation to buy, sell, or hold. "
                    "Anchor your reasoning in the analysts' reports and the research plan."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Based on a comprehensive analysis by a team of analysts, here is an investment "
                    f"plan tailored for {company_name}. {instrument_context} This plan incorporates "
                    f"insights from current technical market trends, macroeconomic indicators, and "
                    f"social media sentiment. Use this plan as a foundation for evaluating your next "
                    f"trading decision.\n\nProposed Investment Plan: {investment_plan}\n\n"
                    f"Leverage these insights to make an informed and strategic decision."
                ),
            },
        ]

        trader_plan = invoke_structured_or_freetext(
            structured_llm,
            llm,
            messages,
            render_trader_proposal,
            "Trader",
        )

        return {
            "messages": [AIMessage(content=trader_plan)],
            "trader_investment_plan": trader_plan,
            "sender": name,
        }

    return functools.partial(trader_node, name="Trader")


def create_trader(llm):
    structured_llm = bind_structured(llm, TraderProposal, "Trader")

    def trader_node(state, name):
        company_name = state["company_of_interest"]
        instrument_context = build_instrument_context(company_name)
        investment_plan = state["investment_plan"]
        delivery_period = state.get("delivery_period", state.get("company_of_interest", ""))
        market_area = state.get("market_area", "CZ")

        messages = [
            {
                "role": "system",
                "content": (
                    f"""You are the Trader on a European electricity intraday trading desk.
                    Based on the Research Manager's plan, propose a specific trade for delivery period {delivery_period}
                    in {market_area}.
                    Your proposal MUST specify:
                    1. ACTION: Buy / Sell / Hold / Reduce / NoTrade
                    2. VOLUME: Position size in MW (typical range: 1-30 MW)
                    3. LIMIT PRICE: Maximum price to pay (Buy) or minimum price to accept (Sell) in EUR/MWh
                    4. EXECUTION STRATEGY:
                    - "passive_limit": Place limit orders at favorable prices. Best when time to delivery > 4h.
                    - "aggressive_market": Take available prices immediately. Use when signal is strong and urgent.
                    - "iceberg": Hide large orders by splitting into small visible portions. Use when > 10 MW.
                    - "twap": Spread execution evenly over the remaining trading window.
                    - "ida_submission": Submit limit orders into the next upcoming IDA auction.
                      IDAs freeze the continuous order book and clear at a uniform price across
                      borders, providing massive liquidity. BEST for large positions (>10 MW)
                      where continuous market impact would erode the edge. Check IDA timing
                      relative to delivery — if the next IDA is before your delivery period,
                      use it. If not, fall back to continuous execution.
                    5. URGENCY: low/medium/high based on time to delivery and signal decay rate
                    EXECUTION COST AWARENESS:
                    - Typical bid-ask spread: 0.5-3 EUR/MWh depending on liquidity and time to delivery
                    - Market impact: ~0.5 EUR/MWh per 5 MW in liquid hours, up to 3 EUR/MWh in thin hours
                    - Gate closure: 5-60 minutes before delivery (varies by product and exchange)
                    - Imbalance penalty: can be 50-500% of DA price in extreme cases
                    - IDA auctions: zero market impact slippage (uniform price clearing), but you accept price uncertainty until the auction clears
                    IMPORTANT: NoTrade is a valid and valuable decision. If the expected edge after costs is < 1 EUR/MWh,
                    or if the regime is unclear, choosing NoTrade protects capital for better opportunities."""
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Based on a comprehensive analysis by a team of analysts, here is an investment "
                    f"plan tailored for delivery period {delivery_period} in {market_area}. Use this plan as a foundation for evaluating your next trading decision.\n\nProposed Investment Plan: {investment_plan}\n\n"
                    f"Leverage these insights to make an informed and strategic decision."
                ),
            },
        ]

        trader_plan = invoke_structured_or_freetext(
            structured_llm,
            llm,
            messages,
            render_trader_proposal,
            "Trader",
        )

        return {
            "messages": [AIMessage(content=trader_plan)],
            "trader_investment_plan": trader_plan,
            "sender": name,
        }

    return functools.partial(trader_node, name="Trader")
