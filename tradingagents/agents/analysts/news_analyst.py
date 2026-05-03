from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from tradingagents.agents.utils.agent_utils import (
    build_instrument_context,
    get_global_news,
    get_language_instruction,
    get_news,
)
from tradingagents.dataflows.config import get_config

NEWS_REGULATORY_ANALYST_PROMPT = """You are the Energy News & Regulatory Analyst for a European electricity intraday trading desk.

YOUR ROLE: Monitor REMIT urgent market messages (UMMs), outage notifications, and regulatory
developments that could affect electricity prices for the target delivery period.

MARKET CONTEXT:
- Delivery period: {delivery_period}
- Market area: {market_area}
- Current time: {current_date}

ANALYTICAL WORKFLOW:
1. Retrieve outage notifications (get_outage_notifications) — planned and unplanned
2. Retrieve actual load data (get_actual_load) — compare with forecast for demand surprises

KEY ANALYSIS:
- OUTAGE IMPACT: For each significant outage, assess:
  → Total MW unavailable during the delivery period
  → Plant type (nuclear/coal/gas) — nuclear and baseload outages are most impactful
  → Planned vs unplanned — unplanned outages are more price-moving (market surprise)
  → Duration — short outages (hours) vs long (days/weeks) have different implications

- REGULATORY AWARENESS (REMIT compliance):
  → Under REMIT, inside information specifically relates to the capacity and use of facilities (e.g., maintenance work and outages).
  → Timely public disclosure of this inside information is mandatory to prevent market manipulation
  → Inside information: outage knowledge before public disclosure is REMIT-prohibited
  → All outage data in our tools is from public ENTSO-E transparency filings
  → Flag any information that seems not yet publicly available

- DEMAND SURPRISES: If actual load deviates significantly from forecast:
  → Higher load = more generation needed = upward price pressure
  → Lower load = surplus capacity = downward price pressure

OUTPUT FORMAT:
1. OUTAGE SUMMARY: Key outages active during delivery period (plant, MW, type)
2. NET SUPPLY IMPACT: Total MW unavailable and whether this is unusual
3. DEMAND ASSESSMENT: Any significant load forecast deviations
4. REMIT FLAGS: Any information that requires special handling

You have access to the following tools: {tool_names}."""


def create_news_analyst_exchange(llm):
    def news_analyst_node(state):
        current_date = state["trade_date"]
        instrument_context = build_instrument_context(state["company_of_interest"])

        tools = [
            get_news,
            get_global_news,
        ]

        system_message = (
            "You are a news researcher tasked with analyzing recent news and trends over the past week. Please write a comprehensive report of the current state of the world that is relevant for trading and macroeconomics. Use the available tools: get_news(query, start_date, end_date) for company-specific or targeted news searches, and get_global_news(curr_date, look_back_days, limit) for broader macroeconomic news. Provide specific, actionable insights with supporting evidence to help traders make informed decisions."
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
        result = chain.invoke(state["messages"])

        report = ""

        if len(result.tool_calls) == 0:
            report = result.content

        return {
            "messages": [result],
            "news_report": report,
        }

    return news_analyst_node


def create_news_analyst(llm, tools):
    def news_analyst_node(state):
        delivery_period = state.get("delivery_period", state.get("company_of_interest", ""))
        market_area = state.get("market_area", "CZ")
        current_date = state.get("trade_date", "")
        system_message = (
            "Focus on REMIT Urgent Market Messages (UMMs) regarding the capacity and use of facilities, "
            "specifically planned maintenance and unplanned outages. Under REMIT, timely public disclosure "
            "of such inside information is mandatory. Trading based on non-public capacity information constitutes "
            "illegal insider trading. Your role is to assess how these public outage disclosures impact market "
            "fundamentals and supply constraints."
        )

        prompt = ChatPromptTemplate.from_messages([
            ("system", NEWS_REGULATORY_ANALYST_PROMPT),
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
            "news_report": report,  # Keep original field name
        }
    return news_analyst_node
