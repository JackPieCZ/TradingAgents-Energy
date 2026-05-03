from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from tradingagents.agents.utils.agent_utils import (
    build_instrument_context,
    get_balance_sheet,
    get_cashflow,
    get_fundamentals,
    get_income_statement,
    get_insider_transactions,
    get_language_instruction,
)
from tradingagents.dataflows.config import get_config


def create_fundamentals_analyst_exchange(llm):
    def fundamentals_analyst_node_exchange(state):
        current_date = state["trade_date"]
        instrument_context = build_instrument_context(state["company_of_interest"])

        tools = [
            get_fundamentals,
            get_balance_sheet,
            get_cashflow,
            get_income_statement,
        ]

        system_message = (
            "You are a researcher tasked with analyzing fundamental information over the past week about a company. Please write a comprehensive report of the company's fundamental information such as financial documents, company profile, basic company financials, and company financial history to gain a full view of the company's fundamental information to inform traders. Make sure to include as much detail as possible. Provide specific, actionable insights with supporting evidence to help traders make informed decisions."
            + " Make sure to append a Markdown table at the end of the report to organize key points in the report, organized and easy to read."
            + " Use the available tools: `get_fundamentals` for comprehensive company analysis, `get_balance_sheet`, `get_cashflow`, and `get_income_statement` for specific financial statements."
            + get_language_instruction(),
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

        result = chain.invoke(state["messages"])

        report = ""

        if len(result.tool_calls) == 0:
            report = result.content

        return {
            "messages": [result],
            "fundamentals_report": report,
        }

    return fundamentals_analyst_node_exchange


def create_fundamentals_analyst(llm, tools):
    def fundamentals_analyst_node(state):
        delivery_period = state.get("delivery_period", state.get("company_of_interest", ""))
        market_area = state.get("market_area", "CZ")
        current_date = state.get("trade_date", "")
        system_message = (
            f"Focus on wind and solar forecast revisions since the day-ahead auction. "
            f"For CZ: solar is the dominant variable force (~2.5 GW installed), wind is negligible (~350 MW). "
            f"For DE-LU: both wind (~65 GW onshore + 8 GW offshore) and solar (~80 GW) matter significantly."
        )

        WEATHER_FORECAST_ANALYST_PROMPT = """You are the Weather & Forecast Analyst for a European electricity intraday trading desk.

YOUR ROLE: Analyze renewable generation forecasts and weather data to identify forecast revisions
that create trading opportunities. Forecast deltas — the difference between the current forecast
and what the day-ahead market priced in — are the PRIMARY source of alpha in intraday power trading.

MARKET CONTEXT:
- Delivery period: {delivery_period}
- Market area: {market_area}
- Current time: {current_date}

Few tips to guide your analysis: {system_message}

ANALYTICAL WORKFLOW:
1. Retrieve the TSO's official generation forecast (get_generation_forecast) to see what the
   day-ahead market was priced on
2. Retrieve current weather forecasts (get_wind_forecast, get_solar_forecast)
3. Retrieve forecast updates (get_forecast_updates) to see intraday forecast revisions
4. If available, retrieve the historical forecast (get_historical_forecast) to compare
   yesterday's forecast vs today's for the delivery date
5. Retrieve general weather conditions (get_weather_forecast) for demand-side effects

CRITICAL ANALYSIS FRAMEWORK:
- A POSITIVE wind/solar forecast error (MORE renewable than DA forecast expected):
  → DOWNWARD price pressure (surplus generation pushes prices down)
  → If large enough, could trigger negative prices during peak solar/wind hours
- A NEGATIVE wind/solar forecast error (LESS renewable than DA forecast expected):
  → UPWARD price pressure (shortage requires more expensive conventional generation)
  → In stressed regimes, even small forecast errors cause large price spikes

QUANTITATIVE BENCHMARKS (from literature):
- German wind forecast error std dev: ~2-4 GW for day-ahead forecasts
- Forecast error halves roughly every 6 hours closer to delivery
- A 5 GW wind forecast error in Germany can move prices by 10-30 EUR/MWh
- Czech solar installed capacity is ~2.5 GW; a clear→cloudy revision moves ~1-2 GW
- Temperature: each 1°C below normal adds ~500 MW load (winter), ~200 MW (summer cooling)

OUTPUT FORMAT: Your report must include:
1. FORECAST DELTA SUMMARY: Current forecast vs DA forecast for wind and solar (MW difference)
2. DIRECTIONAL SIGNAL: Price pressure direction (UP/DOWN/NEUTRAL) with magnitude estimate
3. CONFIDENCE LEVEL: High/Medium/Low based on forecast horizon and consistency
4. KEY UNCERTAINTIES: What could invalidate this signal (e.g., forecast model disagreement)

You have access to the following tools: {tool_names}."""

        prompt = ChatPromptTemplate.from_messages([
            ("system", WEATHER_FORECAST_ANALYST_PROMPT),
            MessagesPlaceholder(variable_name="messages"),
        ])
        prompt = prompt.partial(
            system_message=system_message,
            tool_names=", ".join([tool.name for tool in tools]),
            current_date=current_date,
            delivery_period=delivery_period,
            market_area=market_area,
        )
        chain = prompt | llm.bind_tools(tools)
        result = chain.invoke(state["messages"])
        report = result.content if len(result.tool_calls) == 0 else ""
        return {
            "messages": [result],
            "fundamentals_report": report,  # Keep original field name
        }
    return fundamentals_analyst_node
