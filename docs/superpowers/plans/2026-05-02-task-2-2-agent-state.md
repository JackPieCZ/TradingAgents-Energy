# Phase 2.2 AgentState Update Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update `AgentState` schema to support power-market trading while maintaining backward compatibility with the equity trading path.

**Architecture:** Modifies the existing `AgentState` TypedDict to include new fields like `delivery_period`, `market_area`, and power-specific positions, and updates the docstrings of existing analyst reports to match the new power-focused agent roles.

**Tech Stack:** Python, LangGraph (`MessagesState`), Typing (`Annotated`)

---

### Task 1: Update AgentState definition

**Files:**
- Modify: `tradingagents/agents/utils/agent_states.py`

- [ ] **Step 1: Replace AgentState definition with new schema**

Update the `AgentState` class starting around line 46. Add new fields and update annotations for existing fields to reflect the new agent structure.

Modify `tradingagents/agents/utils/agent_states.py` to replace `class AgentState(MessagesState):` block with:

```python
class AgentState(MessagesState):
    # Core identifiers
    delivery_period: Annotated[str, "Delivery period start (ISO datetime), e.g. 2024-06-15T14:00"]
    market_area: Annotated[str, "Bidding zone (e.g. DE-LU, CZ)"]
    trade_date: Annotated[str, "Current trading timestamp"]

    # Backward compat — keep for stock path
    company_of_interest: Annotated[str, "Ticker or delivery_period identifier"]

    sender: Annotated[str, "Agent that sent this message"]

    # Analyst reports — power market names
    # Keep old field names as aliases for graph wiring compatibility
    market_report: Annotated[str, "Report from Price & Technical Analyst"]
    sentiment_report: Annotated[str, "Report from System State Analyst"]
    news_report: Annotated[str, "Report from Energy News & Regulatory Analyst"]
    fundamentals_report: Annotated[str, "Report from Weather & Forecast Analyst"]

    # Debate states (unchanged structure, updated descriptions)
    investment_debate_state: Annotated[InvestDebateState, "Bull/bear debate state"]
    investment_plan: Annotated[str, "Research Manager's plan"]
    trader_investment_plan: Annotated[str, "Trader's plan"]
    risk_debate_state: Annotated[RiskDebateState, "Risk debate state"]
    final_trade_decision: Annotated[str, "Final decision"]
    past_context: Annotated[str, "Memory log context"]

    # NEW: Power-specific context
    day_ahead_position: Annotated[str, "Current day-ahead position for this delivery period"]
    residual_position: Annotated[str, "Current residual (unhedged) position"]
    regime_indicator: Annotated[str, "Current market regime classification"]
```

- [ ] **Step 2: Commit the changes**

```bash
git add tradingagents/agents/utils/agent_states.py
git commit -m "feat: update AgentState for Phase 2 power market support"
```