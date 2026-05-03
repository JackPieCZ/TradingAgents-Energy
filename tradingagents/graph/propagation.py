# TradingAgents/graph/propagation.py

from typing import Dict, Any, List, Optional
from tradingagents.agents.utils.agent_states import (
    AgentState,
    InvestDebateState,
    RiskDebateState,
)


class Propagator:
    """Handles state initialization and propagation through the graph."""

    def __init__(self, max_recur_limit=100):
        """Initialize with configuration parameters."""
        self.max_recur_limit = max_recur_limit

    # def create_initial_state(
    #     self, company_name: str, trade_date: str, past_context: str = ""
    # ) -> Dict[str, Any]:
    #     """Create the initial state for the agent graph."""
    #     return {
    #         "messages": [("human", company_name)],
    #         "company_of_interest": company_name,
    #         "trade_date": str(trade_date),
    #         "past_context": past_context,
    #         "investment_debate_state": InvestDebateState(
    #             {
    #                 "bull_history": "",
    #                 "bear_history": "",
    #                 "history": "",
    #                 "current_response": "",
    #                 "judge_decision": "",
    #                 "count": 0,
    #             }
    #         ),
    #         "risk_debate_state": RiskDebateState(
    #             {
    #                 "aggressive_history": "",
    #                 "conservative_history": "",
    #                 "neutral_history": "",
    #                 "history": "",
    #                 "latest_speaker": "",
    #                 "current_aggressive_response": "",
    #                 "current_conservative_response": "",
    #                 "current_neutral_response": "",
    #                 "judge_decision": "",
    #                 "count": 0,
    #             }
    #         ),
    #         "market_report": "",
    #         "fundamentals_report": "",
    #         "sentiment_report": "",
    #         "news_report": "",
    #     }
    def create_initial_state(self, delivery_period, trade_timestamp, past_context: str = "", market_area="CZ") -> Dict[str, Any]:
        return {
            "messages": [("human", f"Analyze the electricity market for delivery period "
                          f"{delivery_period} in {market_area} as of {trade_timestamp}.")],
            # Backward compat
            "company_of_interest": f"{delivery_period}_{market_area}",
            # Power fields
            "delivery_period": delivery_period,
            "market_area": market_area,
            "trade_date": trade_timestamp,
            "sender": "",
            # Reports initialized empty
            "market_report": "",
            "sentiment_report": "",
            "news_report": "",
            "fundamentals_report": "",
            # Power context
            "day_ahead_position": "No current position",
            "residual_position": "No residual position",
            "regime_indicator": "Unknown — to be classified by System State Analyst",
            # Debate states
            "investment_debate_state": InvestDebateState(
                history="", bull_history="", bear_history="",
                current_response="", judge_decision="", count=0
            ),
            "investment_plan": "",
            "trader_investment_plan": "",
            "risk_debate_state": RiskDebateState(
                aggressive_history="", conservative_history="", neutral_history="",
                history="", latest_speaker="",
                current_aggressive_response="", current_conservative_response="",
                current_neutral_response="", judge_decision="", count=0
            ),
            "final_trade_decision": "",
            "past_context": past_context,
        }

    def get_graph_args(self, callbacks: Optional[List] = None) -> Dict[str, Any]:
        """Get arguments for the graph invocation.

        Args:
            callbacks: Optional list of callback handlers for tool execution tracking.
                       Note: LLM callbacks are handled separately via LLM constructor.
        """
        config = {"recursion_limit": self.max_recur_limit}
        if callbacks:
            config["callbacks"] = callbacks
        return {
            "stream_mode": "values",
            "config": config,
        }
