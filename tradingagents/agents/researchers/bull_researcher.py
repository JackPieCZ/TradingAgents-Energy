

def create_bull_researcher_exchange(llm):
    def bull_node(state) -> dict:
        investment_debate_state = state["investment_debate_state"]
        history = investment_debate_state.get("history", "")
        bull_history = investment_debate_state.get("bull_history", "")

        current_response = investment_debate_state.get("current_response", "")
        market_research_report = state["market_report"]
        sentiment_report = state["sentiment_report"]
        news_report = state["news_report"]
        fundamentals_report = state["fundamentals_report"]

        prompt = f"""You are a Bull Analyst advocating for investing in the stock. Your task is to build a strong, evidence-based case emphasizing growth potential, competitive advantages, and positive market indicators. Leverage the provided research and data to address concerns and counter bearish arguments effectively.

Key points to focus on:
- Growth Potential: Highlight the company's market opportunities, revenue projections, and scalability.
- Competitive Advantages: Emphasize factors like unique products, strong branding, or dominant market positioning.
- Positive Indicators: Use financial health, industry trends, and recent positive news as evidence.
- Bear Counterpoints: Critically analyze the bear argument with specific data and sound reasoning, addressing concerns thoroughly and showing why the bull perspective holds stronger merit.
- Engagement: Present your argument in a conversational style, engaging directly with the bear analyst's points and debating effectively rather than just listing data.

Resources available:
Market research report: {market_research_report}
Social media sentiment report: {sentiment_report}
Latest world affairs news: {news_report}
Company fundamentals report: {fundamentals_report}
Conversation history of the debate: {history}
Last bear argument: {current_response}
Use this information to deliver a compelling bull argument, refute the bear's concerns, and engage in a dynamic debate that demonstrates the strengths of the bull position.
"""

        response = llm.invoke(prompt)

        argument = f"Bull Analyst: {response.content}"

        new_investment_debate_state = {
            "history": history + "\n" + argument,
            "bull_history": bull_history + "\n" + argument,
            "bear_history": investment_debate_state.get("bear_history", ""),
            "current_response": argument,
            "count": investment_debate_state["count"] + 1,
        }

        return {"investment_debate_state": new_investment_debate_state}

    return bull_node


def create_bull_researcher(llm):
    def bull_node(state) -> dict:
        investment_debate_state = state["investment_debate_state"]
        history = investment_debate_state.get("history", "")
        bull_history = investment_debate_state.get("bull_history", "")
        delivery_period = state.get("delivery_period", state.get("company_of_interest", ""))
        market_area = state.get("market_area", "CZ")

        current_response = investment_debate_state.get("current_response", "")
        market_research_report = state["market_report"]
        sentiment_report = state["sentiment_report"]
        news_report = state["news_report"]
        fundamentals_report = state["fundamentals_report"]

        prompt = f"""You are the Bullish Researcher (arguing FOR a LONG/BUY position) on a European
electricity intraday trading desk.
You are analyzing the {market_area} market for delivery period {delivery_period}.
Given the analyst reports, argue for going LONG (buying power for this delivery period) if any of
these conditions hold:
1. FORECAST REVISION SIGNAL: Wind/solar forecast revised downward → less renewable supply → prices should rise above day-ahead level. Look for asymmetric upside risk and high confidence in the forecast delta.
2. SYSTEM STRESS: High residual load, tight conventional capacity, or significant outages → upward price pressure and risk of spikes. 
3. MEAN REVERSION & ARBITRAGE: Intraday prices have overcorrected downward relative to fundamentals → buying opportunity.
4. CROSS-BORDER SUPPORT & XBID: Neighboring zones have higher prices; interconnector flows in the XBID phase suggest potential price convergence upward before local-only trading begins.
5. IDA AUCTION OPPORTUNITY: If the next IDA auction is approaching and the continuous market hasn't fully priced in the forecast revision yet, submitting into the IDA provides a chance to establish a position at the clearing price without suffering market impact from continuous order book execution.
6. FAVORABLE EXECUTION: The order book depth is sufficient to absorb the required MW volume without excessive market impact (slippage). Argue that the expected edge outweighs the bid-ask spread and transaction costs.
Counter the Bear's arguments with evidence from the analyst reports. Be specific about MW magnitudes,
EUR/MWh price levels, expected market impact, and reference the regime classification.
You must evaluate the following analyst reports:
Price & Technical Report: {market_research_report}
System State Report: {sentiment_report}
Energy News & Regulatory Report: {news_report}
Weather & Forecast Report {fundamentals_report}
Conversation history of the debate: {history}
Last bear argument: {current_response}
Use this information to deliver a compelling bull argument, refute the bear's concerns, and engage in a dynamic debate that demonstrates the strengths of the bull position.
"""

        response = llm.invoke(prompt)

        argument = f"Bull Analyst: {response.content}"

        new_investment_debate_state = {
            "history": history + "\n" + argument,
            "bull_history": bull_history + "\n" + argument,
            "bear_history": investment_debate_state.get("bear_history", ""),
            "current_response": argument,
            "count": investment_debate_state["count"] + 1,
        }

        return {"investment_debate_state": new_investment_debate_state}

    return bull_node
