from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from tradingagents.agents.utils.agent_utils import build_instrument_context, get_language_instruction, get_news
from tradingagents.dataflows.config import get_config

SYSTEM_STATE_ANALYST_PROMPT = """You are the System State Analyst for a European electricity intraday trading desk.

YOUR ROLE: Analyze grid fundamentals — residual load, merit order steepness, cross-border flows,
and outages — to classify the current market regime and identify structural price drivers.

MARKET CONTEXT:
- Delivery period: {delivery_period}
- Market area: {market_area}
- Current time: {current_date}

ANALYTICAL WORKFLOW:
1. Retrieve residual load forecast (get_residual_load) — this is load minus wind minus solar
2. Retrieve actual generation breakdown (get_actual_generation) — assess merit order position
3. Retrieve cross-border flows (get_cross_border_flows) — assess FBMC congestion and import/export situation
4. Retrieve outages (get_outages) — unavailable capacity

REGIME CLASSIFICATION:
You MUST classify the current regime as one of:
- NORMAL: Residual load within typical range, adequate conventional margins. Demand-quote near 1.0.
- STRESSED: High residual load, tight conventional capacity, steep merit order curve
  → Small forecast errors cause disproportionately large price moves
  → Key indicator: residual load > 70 percent of available conventional capacity or demand-quote > 1.2
- OVERSUPPLIED: Wind + Solar > Load, potential for negative prices
  → Conventional plants may be curtailed; prices can go deeply negative
  → Key indicator: residual load < 20 percent of typical, or total renewables > total demand
- VOLATILE: Large recent forecast revisions, active cross-border congestion, or price swings, regime uncertain
  → Multiple possible outcomes; wider spreads and more cautious positioning needed

MERIT ORDER & CONGESTION REASONING:
- FLAT MERIT ORDER (Low residual load): Marginal generator is cheap (gas/coal minimum). Price insensitive to small shocks, but large swings possible at transition points.
- STEEP MERIT ORDER (High residual load): Marginal generator is expensive (peak gas, oil). Price very sensitive to ANY supply/demand change — outages matter most here.
- CROSS-BORDER DECOUPLING: If cross-border flows are at maximum capacity, Flow Based Market Coupling (FBMC) constraints are active. The local market is decoupled, meaning it must absorb its own supply/demand shocks without neighbor assistance.

IMBALANCE & SYSTEM TENSION:
- IMBALANCE VOLUME interpretation: Positive imbalance volume generally means the system is LONG
  (oversupplied — more generation than scheduled consumption). Negative means SHORT (undersupplied).
  NOTE: Different TSOs may use different sign conventions; always cross-reference with the
  residual load direction. A 400 MW positive imbalance volume is significant — roughly the output
  of a mid-sized gas plant. Over 1000 MW indicates serious system stress.
- When imbalance prices are delayed or unavailable (common for DE-LU), use residual load deviation
  and cross-border flow saturation as proxies for system tension.
- If the system is consistently short (negative imbalance), expect upward pressure on both
  intraday and imbalance settlement prices.

OUTPUT FORMAT:
1. REGIME CLASSIFICATION: Normal/Stressed/Oversupplied/Volatile with supporting evidence
2. KEY RISK FACTORS: List the top 3 system risks (outages, congestion, ramp constraints)
3. DIRECTIONAL BIAS: Does system state favor higher or lower prices vs day-ahead?
4. MERIT ORDER ASSESSMENT: Is the merit order curve steep or flat at current operating point?

You have access to the following tools: {tool_names}."""


def create_social_media_analyst_exchange(llm):
    def social_media_analyst_node_exchange(state):
        current_date = state["trade_date"]
        instrument_context = build_instrument_context(state["company_of_interest"])

        tools = [
            get_news,
        ]

        system_message = (
            "You are a social media and company specific news researcher/analyst tasked with analyzing social media posts, recent company news, and public sentiment for a specific company over the past week. You will be given a company's name your objective is to write a comprehensive long report detailing your analysis, insights, and implications for traders and investors on this company's current state after looking at social media and what people are saying about that company, analyzing sentiment data of what people feel each day about the company, and looking at recent company news. Use the get_news(query, start_date, end_date) tool to search for company-specific news and social media discussions. Try to look at all sources possible from social media to sentiment to news. Provide specific, actionable insights with supporting evidence to help traders make informed decisions."
            + """ Make sure to append a Markdown table at the end of the report to organize key points in the report, organized and easy to read."""
            + get_language_instruction()
        )

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a helpful AI assistant, collaborating with other assistants."
                    " Use the provided tools to progress towards answering the question."
                    " If you are unable to fully answer, that's OK; another assistant with different tools"
                    " will help where you left off. Execute what you can to make progress."
                    " If you or any other assistant has the FINAL TRANSACTION PROPOSAL: **BUY/HOLD/SELL** or deliverable,"
                    " prefix your response with FINAL TRANSACTION PROPOSAL: **BUY/HOLD/SELL** so the team knows to stop."
                    " You have access to the following tools: {tool_names}.\n{system_message}"
                    "For your reference, the current date is {current_date}. {instrument_context}",
                ),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )

        prompt = prompt.partial(system_message=system_message)
        prompt = prompt.partial(tool_names=", ".join([tool.name for tool in tools]))
        prompt = prompt.partial(current_date=current_date)
        prompt = prompt.partial(instrument_context=instrument_context)

        chain = prompt | llm.bind_tools(tools)

        result = chain.invoke({"messages": state["messages"]})

        report = ""

        if len(result.tool_calls) == 0:
            report = result.content

        return {
            "messages": [result],
            "sentiment_report": report,
        }

    return social_media_analyst_node_exchange


def create_social_media_analyst(llm, tools):
    def social_media_analyst_node(state):
        delivery_period = state.get("delivery_period", state.get("company_of_interest", ""))
        market_area = state.get("market_area", "CZ")
        current_date = state.get("trade_date", "")
        system_message = (
            f"You are evaluating the system state for the {market_area} electricity market, delivery on {delivery_period}. "
            f"Key framework elements to consider:\n"
            f"- Demand-Quote Regime: Compare expected demand to available day-ahead capacity. High quotes (>1.0 to 1.2) signal reliance on the intraday market to cover deficits.\n"
            f"- Merit Order Slope: Assess whether we are in a 'flat' (low demand/high renewables) or 'steep' (high demand/low renewables) portion of the merit order curve. Steep regimes amplify the price impact of any forecast errors.\n"
            f"- FBMC Cross-Border Congestion: Monitor import/export flows against NTC or RAM limits. Congestion on borders (e.g. DE-NL or DE-FR) decouples regional prices and traps local supply/demand shocks."
        )

        prompt = ChatPromptTemplate.from_messages([
            ("system", SYSTEM_STATE_ANALYST_PROMPT),
            MessagesPlaceholder(variable_name="messages"),
        ])
        prompt = prompt.partial(
            tool_names=", ".join([tool.name for tool in tools]),
            current_date=current_date,
            delivery_period=delivery_period,
            market_area=market_area,
        )
        chain = prompt | llm.bind_tools(tools)
        result = chain.invoke({"messages": state["messages"]})
        report = result.content if len(result.tool_calls) == 0 else ""
        return {
            "messages": [result],
            "sentiment_report": report,
        }
    return social_media_analyst_node
