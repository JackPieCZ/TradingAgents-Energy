from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from tradingagents.agents.utils.agent_utils import (
    build_instrument_context,
    get_indicators,
    get_language_instruction,
    get_stock_data,
)
from tradingagents.dataflows.config import get_config

PRICE_TECHNICAL_ANALYST_PROMPT = """You are the Price & Technical Analyst for a European electricity intraday trading desk.

YOUR ROLE: Analyze intraday price patterns, spreads vs day-ahead, mean-reversion signals,
and cross-product pricing to identify trading opportunities.

MARKET CONTEXT:
- Delivery period: {delivery_period}
- Market area: {market_area}
- Current time: {current_date}

Few tips to guide your analysis: {system_message}

ANALYTICAL WORKFLOW:
1. Retrieve day-ahead prices (get_day_ahead_prices) — the price anchor
2. Retrieve intraday continuous prices (get_intraday_prices) — current market pricing
3. Retrieve IDA auction prices (get_intraday_auction_prices) — auction-based price discovery
4. Retrieve imbalance data (get_balancing_data) — penalty price for unhedged positions

KEY PRICE ANALYSIS:
- SPREAD TO DAY-AHEAD: intraday_price - day_ahead_price for each delivery hour
  → Positive spread = intraday premium (market expects tighter supply than DA assumed)
  → Negative spread = intraday discount (market expects more supply than DA assumed)
  → Large spreads that have been widening suggest momentum; narrowing suggests mean reversion

- MEAN REVERSION: Intraday power prices tend to mean-revert toward a fundamental level
  → But reversion is CONDITIONAL on regime: in Stressed regime, trends persist longer
  → CZ SPECIFICS: Hurst exponent H ≈ 0.42-0.45 for <24h = WEAK mean reversion (nearly random). H ≈ 0.19 for 25-240h = STRONG mean reversion. Practical meaning: do NOT bet on same-day mean reversion in CZ; over multiple days it is reliable.
  → Short-term: last 2-3 hours of intraday trading activity for the delivery period
  → Most CZ intraday price deviation is AUTOREGRESSIVE PERSISTENCE: R² = 0.61 from the lagged deviation term alone. If CZ intraday has been trending away from DA, the trend likely CONTINUES short-term, then reverts over days.
  → Compare with neighboring delivery hours for cross-product consistency
  → Negative CZ intraday prices are NOT connected to negative DA prices — they are caused by unforeseen RES surplus or negative demand shocks independently

- TIME-TO-DELIVERY EFFECT:
  → Far from delivery: wider spreads, more volatile, information still arriving
  → Close to delivery: spreads tighten, prices more accurate, less opportunity
  →  Final 60 min: volatility typically spikes, distributions become heavy-tailed, but liquidity improves
  → BID-ASK SPREAD follows an L-SHAPE: high at session start, decreasing as delivery approaches, with a small spike at the very end when order book thins
  → 80% of volume is traded in the LAST 3 HOURS of the trading session
  → Forecast errors paradoxically DECREASE spreads — they create a need to trade → more volume → tighter spreads
  → Steep merit order → heavier distribution tails → more spike risk

- IDA AUCTION MECHANISM: Unlike the continuous order book, IDAs are discrete clearing events. When an IDA triggers, the continuous order books are FROZEN. All bids and asks are aggregated into a single intersection point, establishing a uniform clearing price across all participating European borders for that delivery period.
  → IDA 1: 15:00 CET on day-ahead (D-1)  Delivery scope: Covers all delivery periods of the delivery day D (00:00 – 24:00).
    IDA 2: 22:00 CET on day-ahead (D-1)  Delivery scope: Covers all delivery periods of the delivery day D (00:00 – 24:00).
    IDA 3: 10:00 CET on the delivery day (D) Delivery scope: Covers the remaining delivery periods of the delivery day D (12:00 – 24:00).
  → Compare IDA clearing prices with continuous VWAP: large divergences signal that the continuous market has not yet absorbed new information (forecast revisions, outages)
  → IDAs provide MASSIVE LIQUIDITY INJECTIONS — they are the best venue for closing large residual positions (10+ MW) without suffering severe market impact slippage
  → If a major forecast revision drops between IDAs, the clearing price will jump; the continuous market typically front-runs this but not fully

- IMBALANCE EXPOSURE: The imbalance price is the "worst case" settlement
  → If imbalance price >> DA price: strong incentive to be balanced (conservative)
  → If imbalance price ≈ DA price: less penalty for carrying positions to delivery
  → Balancing market dynamics feed back into intraday prices — system imbalance signals have
    predictive power for late-session price moves

- CZ LIQUIDITY WARNING: CZ intraday volume is ~545 GWh/year vs ~36 TWh in DE — roughly 60x
  less liquid. Spreads are wider and market impact is proportionally MUCH larger per MW.
  → Intraday prices feed back into TOMORROW's DA price (R² ≈ 0.15)

OUTPUT FORMAT:
1. PRICE LEVEL: Current intraday price vs DA anchor for key delivery hours
2. SPREAD ANALYSIS: Is the spread widening/narrowing/stable? Why?
3. MEAN REVERSION SIGNAL: Is there a reversion opportunity and how strong?
4. CROSS-PRODUCT CHECK: Do neighboring hours confirm or contradict the signal?
5. EXECUTION CONTEXT: Liquidity, bid-ask proxy, time-to-delivery assessment and volatility expectations

TOOL OUTPUT FORMATS:
- get_day_ahead_prices → CSV header + rows. Columns: Hour (CET), Price EUR/MWh. One row per delivery hour.
- get_intraday_prices → CSV header + rows. Columns: Hour (CET), Price EUR/MWh (VWAP), Volume MWh, plus additional spread/range metrics.
- get_intraday_auction_prices → CSV header + rows. Columns: Hour (CET), Auction (IDA1/IDA2/IDA3), Price EUR/MWh, Volume MWh, Import MWh, Export MWh, Saldo MWh.
- get_imbalance_data → CSV header + rows. Columns vary by source but typically include: Hour, Imbalance Volume MW, Imbalance Price EUR/MWh.

You have access to the following tools: {tool_names}. Make sure to append a Markdown table at the end of the report to organize key points in the report, organized and easy to read.""" + get_language_instruction()


def create_market_analyst_exchange(llm):

    def market_analyst_node(state):
        current_date = state["trade_date"]
        instrument_context = build_instrument_context(state["company_of_interest"])

        tools = [
            get_stock_data,
            get_indicators,
        ]

        system_message = (
            """You are a trading assistant tasked with analyzing financial markets. Your role is to select the **most relevant indicators** for a given market condition or trading strategy from the following list. The goal is to choose up to **8 indicators** that provide complementary insights without redundancy. Categories and each category's indicators are:

Moving Averages:
- close_50_sma: 50 SMA: A medium-term trend indicator. Usage: Identify trend direction and serve as dynamic support/resistance. Tips: It lags price; combine with faster indicators for timely signals.
- close_200_sma: 200 SMA: A long-term trend benchmark. Usage: Confirm overall market trend and identify golden/death cross setups. Tips: It reacts slowly; best for strategic trend confirmation rather than frequent trading entries.
- close_10_ema: 10 EMA: A responsive short-term average. Usage: Capture quick shifts in momentum and potential entry points. Tips: Prone to noise in choppy markets; use alongside longer averages for filtering false signals.

MACD Related:
- macd: MACD: Computes momentum via differences of EMAs. Usage: Look for crossovers and divergence as signals of trend changes. Tips: Confirm with other indicators in low-volatility or sideways markets.
- macds: MACD Signal: An EMA smoothing of the MACD line. Usage: Use crossovers with the MACD line to trigger trades. Tips: Should be part of a broader strategy to avoid false positives.
- macdh: MACD Histogram: Shows the gap between the MACD line and its signal. Usage: Visualize momentum strength and spot divergence early. Tips: Can be volatile; complement with additional filters in fast-moving markets.

Momentum Indicators:
- rsi: RSI: Measures momentum to flag overbought/oversold conditions. Usage: Apply 70/30 thresholds and watch for divergence to signal reversals. Tips: In strong trends, RSI may remain extreme; always cross-check with trend analysis.

Volatility Indicators:
- boll: Bollinger Middle: A 20 SMA serving as the basis for Bollinger Bands. Usage: Acts as a dynamic benchmark for price movement. Tips: Combine with the upper and lower bands to effectively spot breakouts or reversals.
- boll_ub: Bollinger Upper Band: Typically 2 standard deviations above the middle line. Usage: Signals potential overbought conditions and breakout zones. Tips: Confirm signals with other tools; prices may ride the band in strong trends.
- boll_lb: Bollinger Lower Band: Typically 2 standard deviations below the middle line. Usage: Indicates potential oversold conditions. Tips: Use additional analysis to avoid false reversal signals.
- atr: ATR: Averages true range to measure volatility. Usage: Set stop-loss levels and adjust position sizes based on current market volatility. Tips: It's a reactive measure, so use it as part of a broader risk management strategy.

Volume-Based Indicators:
- vwma: VWMA: A moving average weighted by volume. Usage: Confirm trends by integrating price action with volume data. Tips: Watch for skewed results from volume spikes; use in combination with other volume analyses.

- Select indicators that provide diverse and complementary information. Avoid redundancy (e.g., do not select both rsi and stochrsi). Also briefly explain why they are suitable for the given market context. When you tool call, please use the exact name of the indicators provided above as they are defined parameters, otherwise your call will fail. Please make sure to call get_stock_data first to retrieve the CSV that is needed to generate indicators. Then use get_indicators with the specific indicator names. Write a very detailed and nuanced report of the trends you observe. Provide specific, actionable insights with supporting evidence to help traders make informed decisions."""
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
            "market_report": report,
        }

    return market_analyst_node


def create_market_analyst(llm, tools):
    def market_analyst_node(state):
        delivery_period = state.get("delivery_period", state.get("company_of_interest", ""))
        market_area = state.get("market_area", "CZ")
        current_date = state.get("trade_date", "")
        system_message = (
            "Focus on the volume-weighted average prices (VWAP) and their deviations from the day-ahead anchor. "
            "Remember that intraday price changes exhibit strong autoregressive features and mean reversion. "
            "Volatility and heavy-tailed price distributions increase significantly as time-to-delivery decreases, "
            "especially in the last 60 minutes of trading. Neighboring contract prices "
            "also exert a strong gravitational pull on the current contract's price path."
        )

        prompt = ChatPromptTemplate.from_messages([
            ("system", PRICE_TECHNICAL_ANALYST_PROMPT),
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
        result = chain.invoke({"messages": state["messages"]})
        report = result.content if len(result.tool_calls) == 0 else ""
        # Append a brief summary to analyst_context for subsequent analysts.
        # Only appends when report is non-empty (i.e., final invocation, not mid-tool-loop).
        existing_context = state.get("analyst_context", "")
        if report:
            context_addition = (
                "--- Price & Technical Analyst ---\n"
                f"{report}\n"
            )
            new_context = existing_context + context_addition
        else:
            new_context = existing_context
        return {
            "messages": [result],
            "market_report": report,  # Keep original field name
            "analyst_context": new_context,
        }
    return market_analyst_node
