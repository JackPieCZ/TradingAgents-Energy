# CLAUDE.md — TradingAgents-private (Energy/Power Markets Fork)

## Project Overview

This is a fork of [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) being adapted from **stock trading** to **European electricity/energy intraday markets**. The original framework is a multi-agent LLM system inspired by real-world trading firms, using LangGraph to orchestrate specialized agents (analysts, researchers, traders, risk managers) that debate and collaborate to produce trading decisions.

**Paper**: Xiao et al., "TradingAgents: Multi-Agents LLM Financial Trading Framework" (arXiv:2412.20138v7)

**Original target**: US equities (AAPL, NVDA, GOOGL, etc.) with daily Buy/Hold/Sell decisions.
**Fork target**: European power intraday markets (EPEX/OTE) with delivery-period-level trading signals for electricity products.

**Target markets**: German EPEX Spot (primary), Czech OTE (secondary)
**Target products**: Hourly and quarter-hourly intraday continuous + intraday auctions
**Trading horizon**: Intraday, from day-ahead gate closure to delivery

---

## Current Status

Phase 0 (research & context gathering) is **complete**. All 27 papers are in project knowledge. All data access is resolved.
Phase 1 (data layer) is **complete** — all 8 data modules implemented and tested with live APIs (ENTSO-E, OTE SOAP, SMARD, Open-Meteo).
Phase 2 (agent roles & state) is **complete** — AgentState updated, 4 energy tool files created, tool nodes wired, propagation updated, propagate() signature changed to `(delivery_period, trade_timestamp, market_area)`.
Phase 3 (agent prompts) is **complete** — all 13 agent prompts rewritten with power-market domain expertise (analysts, researchers, risk analysts, trader, PM, research manager). CLI display names updated.
Implementation continues at **Phase 4: Update Schemas and Decision Outputs**.

**Known bugs to fix at start of Phase 4-5** (discovered during Phase 2-3 code review):
1. **CRITICAL**: `propagation.py` line 83-85 — `RiskDebateState` initialized with wrong field names (`agg_history`, `con_history` instead of `aggressive_history`, `conservative_history`, etc.). Will crash at runtime.
2. **MODERATE**: All 4 analyst `create_*` functions — prompt template includes literal `"..."` strings, and `instrument_context` is computed but never injected into the template (LLM never sees the CZ vs DE-LU specific context).
3. **MODERATE**: `schemas.py` still uses equity schemas — prompts ask for power-specific outputs (volume_mw, execution_strategy, etc.) but schemas can't capture them. Fix in Phase 4.
4. **MODERATE**: `_fetch_returns()` and `reflection.py` still use yfinance/SPY — equity-specific. Fix in Phase 5.
5. `rating.py` / `signal_processing.py` only recognize equity 5-tier ratings, not power actions (Reduce, NoTrade). Fix in Phase 4.

**Phase 1 known data bugs** (still unfixed):
1. ENTSO-E CZ imbalance prices are in CZK not EUR — needs conversion (~÷25)
2. SMARD filter_id 410 used for both generation_total and total_load — must compute total from parts
3. SMARD load forecast filter (123) returns wrong data (~10x too low) — needs correct filter ID
4. `_load_or_fetch` duplicated in all 4 clients — consolidate to `cache_layer.cached_fetch()`

**Phase 1 key insight for prompt design**: CZ wind data from ENTSO-E is often zero (Czech installed wind ~350 MW = negligible). Weather & Forecast Analyst should focus on solar for CZ and wind+solar for DE-LU. Open-Meteo Historical Forecast API provides forecast revision deltas — the primary alpha signal per Kup22.

See `STRATEGY.md` for the full 13-phase implementation plan with detailed instructions for each phase.
See `phase1_review_and_phase2_3_plan.md` for detailed Phase 2-3 implementation instructions.
See `phase4_5_implementation_plan.md` for detailed Phase 4-5 implementation instructions with bug fixes.

---

## Repository Structure

```
TradingAgents/
├── main.py                          # Entry point — backtest loop
├── cli/                             # CLI interface (main.py, utils.py, models.py)
│   └── main.py                      # ✅ Display names updated for energy analysts
├── tradingagents/
│   ├── __init__.py
│   ├── default_config.py            # All configuration defaults (LLM, vendors, paths)
│   ├── agents/
│   │   ├── analysts/
│   │   │   ├── fundamentals_analyst.py   # ✅ Weather & Forecast Analyst (create_fundamentals_analyst)
│   │   │   ├── market_analyst.py         # ✅ Price & Technical Analyst (create_market_analyst)
│   │   │   ├── news_analyst.py           # ✅ Energy News & Regulatory Analyst (create_news_analyst)
│   │   │   └── social_media_analyst.py   # ✅ System State Analyst (create_social_media_analyst)
│   │   ├── researchers/
│   │   │   ├── bull_researcher.py        # ✅ Power market bull arguments (create_bull_researcher)
│   │   │   └── bear_researcher.py        # ✅ Power market bear arguments (create_bear_researcher)
│   │   ├── managers/
│   │   │   ├── research_manager.py       # ✅ Power market synthesis (create_research_manager)
│   │   │   └── portfolio_manager.py      # ✅ Power market PM with regime/MW/imbalance (create_portfolio_manager)
│   │   ├── risk_mgmt/
│   │   │   ├── aggressive_debator.py     # ✅ Power risk context (create_aggressive_debator)
│   │   │   ├── conservative_debator.py   # ✅ Power risk context (create_conservative_debator)
│   │   │   └── neutral_debator.py        # ✅ Power risk context (create_neutral_debator)
│   │   ├── trader/
│   │   │   └── trader.py                 # ✅ Power execution strategy (create_trader)
│   │   ├── schemas.py                    # → Phase 4: Add PowerTradingAction, MarketRegime, PowerTraderProposal, PowerPortfolioDecision
│   │   └── utils/
│   │       ├── agent_states.py           # ✅ Power fields added (delivery_period, market_area, regime_indicator, etc.)
│   │       ├── agent_utils.py            # Unchanged — still has old tool imports for exchange path
│   │       ├── core_stock_tools.py       # Legacy — kept for stock path backward compatibility
│   │       ├── energy_price_tools.py     # ✅ NEW — 4 tools (DA prices, intraday, IDA, imbalance)
│   │       ├── system_data_tools.py      # ✅ NEW — 5 tools (residual load, generation, load, flows, outages)
│   │       ├── weather_tools.py          # ✅ NEW — 6 tools (wind, solar, generation forecast, updates, weather, historical)
│   │       ├── energy_news_tools.py      # ✅ NEW — 2 tools (outage notifications, actual load)
│   │       ├── fundamental_data_tools.py # Legacy — kept for stock path
│   │       ├── news_data_tools.py        # Legacy — kept for stock path
│   │       ├── technical_indicators_tools.py  # Legacy — kept for stock path
│   │       ├── memory.py                 # Append-only markdown decision log (reuse as-is, update in Phase 5)
│   │       ├── rating.py                 # → Phase 4: Add power action vocabulary (Reduce, NoTrade)
│   │       └── structured.py             # Provider-agnostic structured output binding (reuse as-is)
│   ├── dataflows/
│   │   ├── interface.py                  # ✅ Vendor routing — energy categories, 20+ methods
│   │   ├── config.py                     # Runtime config access (reuse)
│   │   ├── entsoe_client.py              # ✅ ENTSO-E — 10 methods
│   │   ├── ote_client.py                 # ✅ OTE Czech SOAP — 5 methods
│   │   ├── smard_client.py               # ✅ SMARD German — 6 methods
│   │   ├── weather_client.py             # ✅ Open-Meteo — 4 methods
│   │   ├── energy_utils.py               # ✅ Shared utilities
│   │   ├── cache_layer.py                # ✅ Parquet-based local cache
│   │   ├── mock_energy.py                # ✅ Synthetic data generators
│   │   ├── y_finance.py                  # Legacy — still used by stock path
│   │   └── ...                           # Other legacy modules
│   ├── graph/
│   │   ├── trading_graph.py              # ✅ Tool nodes updated, propagate() signature changed. → Phase 5: clean up _run_graph, replace _fetch_returns
│   │   ├── setup.py                      # ✅ Energy tools wired to energy analyst factories
│   │   ├── propagation.py                # ✅ Power initial state. ⚠️ BUG: RiskDebateState field names wrong
│   │   ├── conditional_logic.py          # Unchanged — routing works for energy path
│   │   ├── reflection.py                 # → Phase 5: Replace "Alpha vs SPY" with power P&L reflection
│   │   ├── signal_processing.py          # → Phase 4: Must handle power actions after rating.py update
│   │   └── checkpointer.py              # SQLite checkpointing (reuse as-is)
│   ├── backtesting/                      # → Phase 7: entire module
│   ├── analytics/                        # → Phase 8: regime.py
│   └── llm_clients/                      # Multi-provider LLM client factory (reuse as-is)
├── phase4_5_implementation_plan.md       # ✅ Detailed Phase 4-5 instructions with bug fixes
├── tests/                                # Test suite
└── pyproject.toml                        # Package definition
```

---

## Architecture & Data Flow

The system runs as a **LangGraph StateGraph** with this pipeline (showing new power-market names):

```
START
  → Weather & Forecast Analyst (tools: get_wind_forecast, get_solar_forecast, get_forecast_updates)
  → System State Analyst (tools: get_residual_load, get_merit_order_proxy, get_cross_border_flows, get_outages)
  → Price & Technical Analyst (tools: get_intraday_prices, get_price_spreads, get_power_indicators)
  → Energy News & Regulatory Analyst (tools: get_energy_news, get_remit_messages, get_outage_notifications)
  → Bull Researcher ↔ Bear Researcher (debate, N rounds)
  → Research Manager (synthesizes debate → ResearchPlan)
  → Trader (converts plan → PowerTraderProposal: Buy/Sell/Hold/Reduce/NoTrade)
  → Aggressive ↔ Conservative ↔ Neutral Risk Analysts (debate, N rounds)
  → Portfolio Manager (final PowerPortfolioDecision with volume, price target, regime assessment)
END
```

**Key design patterns (unchanged from original):**
- Each analyst node creates a LangChain prompt with tool bindings, invokes the LLM, returns a report string to state
- Analysts use `quick_thinking_llm`; Research Manager and Portfolio Manager use `deep_thinking_llm`
- Tool calls loop: analyst → tools → analyst until no more tool calls, then messages are cleared
- The `dataflows/interface.py` layer abstracts data vendors; tools call `route_to_vendor(method_name, *args)`
- State is a `TypedDict` (`AgentState`) accumulating reports, debate history, and final decision
- After each run, decisions are stored in a markdown memory log with LLM reflection

**Key design changes for power markets (implemented):**
- `propagate(delivery_period, trade_timestamp, market_area)` replaces `propagate(company_name, trade_date)` ✅
- State includes power-specific fields: `delivery_period`, `market_area`, `regime_indicator`, `day_ahead_position` ✅
- Tool nodes bind energy tools (ENTSO-E, OTE, SMARD, Open-Meteo) to energy analyst factories ✅
- Analyst reports write to original field names (`market_report`, `sentiment_report`, `fundamentals_report`, `news_report`) for backward compat ✅
- Weather & Forecast Analyst is the most important role (forecast deltas = primary alpha source) ✅
- Reflection still compares against SPY — needs Phase 5 update to compare against DA price benchmark
- Schemas still use equity ratings — needs Phase 4 update for PowerTradingAction/MarketRegime

---

## Data Access (Resolved)

**Strategy: Option A+C — zero-cost MVP**

| Source | Provides | Access |
|--------|----------|--------|
| **ENTSO-E** (`entsoe-py`) | DA prices, generation forecasts (wind/solar), load, cross-border flows, outages, imbalance prices — all EU zones | REST API, key obtained, library installed |
| **OTE SOAP** | Czech DA prices, intraday continuous VWAP/volumes per 15-min period, IDA auction results, imbalance settlement | SOAP at `http://www.ote-cr.cz/services/PublicDataService`, no auth needed |
| **SMARD** | German generation by type, total load, residual load (hourly + QH) | REST API, no auth |
| **Open-Meteo** | Wind speed (multiple heights), solar radiation, temperature — historical + forecast + "historical forecast" for backtesting | REST API, no auth, `openmeteo-requests` installed |

**OTE SOAP services for electricity** (from `uzivatelskymanual_webove_sluzby_ote_g.pdf`):
- `GetDamPriceE` — Day-ahead hourly prices + volumes
- `GetImPriceE` — Intraday continuous daily VWAP + min/max + volumes
- `GetImPricePeriodE` — Intraday continuous per 15-min period (price + volume per `PeriodIndex`)
- `GetIDAPriceE` — IDA auction hourly results
- `GetIDAPricePeriodE` — IDA auction per period (includes `Auction` field: IDA1/IDA2/IDA3)
- `GetImbalanceSettlementE` — Hourly imbalance results (Version: 0=daily, 1=monthly, 2=final)
- All take `StartDate`/`EndDate` (YYYY-MM-DD), optionally `StartHour`/`EndHour` or `StartPeriod`/`EndPeriod`

**OTE JSON endpoint** (undocumented): `https://www.ote-cr.cz/pw-data/chart-data/01?language=en`

---

## Configuration

All config in `default_config.py` as a flat dict. Key settings:
- `llm_provider`: "openai" | "anthropic" | "google" | "xai"
- `deep_think_llm` / `quick_think_llm`: Model names
- `market_area`: "DE-LU" | "CZ"
- `delivery_resolution`: "60min" | "15min"
- `data_vendors`: Market-area-aware vendor routing for price, system, weather, fundamentals, news data
- `entsoe_api_key`: Set via env var `ENTSOE_API_KEY`
- `max_debate_rounds` / `max_risk_discuss_rounds`: Debate iteration caps
- `output_language`: For multilingual reports

---

## Environment Setup

**Conda environment**: `tradingagents`

**Installed energy-specific packages**:
- `entsoe-py` — ENTSO-E API client (returns pandas DataFrames)
- `openmeteo-requests` — Open-Meteo client
- `requests-cache` — HTTP caching
- `retry-requests` — Retry logic

**Still needed** (install when implementing):
- Additional packages as phases require them

**Not needed**: `zeep` — OTE client uses raw SOAP XML via `requests` instead (lighter dependency).

**epftoolbox**: Cloned to `epftoolbox-master/` but NOT pip-installable (requires Python ≤3.13, env has 3.13.13). Use as reference code only — import individual modules by path if needed.

---

## How to Run (Original — Still Working)

```bash
# Activate conda env
conda activate tradingagents
# Set LLM API key
export OPENAI_API_KEY=...  # or ANTHROPIC_API_KEY
# Run original stock trading backtest
python main.py
```

The backtest loop iterates over trading days, calling `ta.propagate(ticker, date)` which returns `(final_state, signal)`.

See `complete_report.md` for example output of the original system (SPY analysis showing: 4 analyst reports → bull/bear debate → research manager synthesis → trader proposal → risk debate → portfolio manager decision).

---

## Implementation Workflow

Three coding tools available, each with different strengths. See STRATEGY.md Appendix D for the full allocation plan.

**Quick summary**:
- **Claude Code (Pro, limited)** → Architecture decisions, prompt engineering, domain-heavy logic, code review. Use for: data layer design, all agent prompts, execution model review, regime classifier design. ~5-6 sessions total.
- **Opencode (open models + Gemini)** → Bulk code generation. Use for: data client implementations, tool files, indicator calculations, backtest scaffolding. ~15 sessions.
- **VS Code + GitHub Copilot Pro** → Always-on completions. Use for: utilities, tests, mechanical refactoring, config updates, graph wiring, repetitive patterns. Continuous.

**Key principle**: Use Claude Code for decisions, Opencode for generation, Copilot for completion. Claude Code sessions should produce clear artifacts (skeletons, prompts, design notes) that other tools execute against.

**Implementation order** (from STRATEGY.md Appendix B):
1. ~~Phase 1 (data layer) — without data, nothing works~~ ✅
2. ~~Phases 2-3 (agent roles + prompts) — core architecture + domain expertise~~ ✅
3. **Phase 4 (schemas) — structured outputs** ← NEXT (see `phase4_5_implementation_plan.md`)
4. **Phase 5 (graph wiring cleanup + bug fixes)** ← NEXT (includes critical bug fixes from Phases 2-3)
5. Phase 7 (backtesting + metrics) — need to measure results
6. Phase 6 (power indicators) — enrich agent inputs
7. Phase 8 (regime detection) — conditional performance
8. Phases 9-13 (iteration, assets, testing, docs) — refinement

---

## Key Domain Concepts for AI Agents

| Stock Trading Concept | Power Trading Equivalent |
|----------------------|-------------------------|
| Ticker symbol (AAPL) | Delivery period + market area (2024-06-15T14:00 DE-LU) |
| Stock price (OHLCV) | Intraday continuous trade prices for a delivery period |
| Company fundamentals | Grid system state (residual load, generation mix, outages) |
| Earnings reports | Renewable forecast updates and forecast revisions |
| Social media sentiment | Weather forecasts and forecast deltas (this IS the sentiment) |
| P/E ratio, market cap | Merit order slope, residual load ratio, available flexibility |
| Insider transactions | REMIT urgent market messages, outage notifications |
| Daily Buy/Hold/Sell | Per-delivery-period position signal (may trade same product multiple times) |
| Alpha vs S&P 500 | Net trading value vs day-ahead settlement |
| Transaction cost | Spread + market impact + imbalance settlement cost |

---

## References

- Paper: arXiv:2412.20138v7 (TradingAgents)
- Upstream repo: https://github.com/TauricResearch/TradingAgents
- Fork: https://github.com/JackPieCZ/TradingAgents-private.git
- Implementation plan: `STRATEGY.md` (13 phases + 4 appendices)
- Phase 2-3 instructions: `phase1_review_and_phase2_3_plan.md`
- Phase 4-5 instructions: `phase4_5_implementation_plan.md` (includes bug fix list)
- Power trading playbook: `Power_trading_transition_playbook.md`
- Source analysis: `Sources_Power_trading_transition_from_algo_finance.md`
- Key papers: Kup22, Kie17, Kre21b, Kat20, Nar21, Aid15, Hir22, Ser22, Bun18, Féron20, Martin18, Balardy22
- OTE SOAP docs: `uzivatelskymanual_webove_sluzby_ote_g.pdf`
- ENTSO-E API docs: https://transparencyplatform.zendesk.com/hc/en-us/articles/15692855254548-Sitemap-for-Restful-API-Integration
- Example output: `complete_report.md` (original SPY analysis — reference for expected report structure)
