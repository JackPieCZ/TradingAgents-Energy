# Power trading transition playbook

##### [**Undermind**](https://undermind.ai)

---


## Table of Contents

- [Power trading transition playbook](#power-trading-transition-playbook)
- [Bottom line](#bottom-line)
- [Where power differs from exchange algo trading](#where-power-differs-from-exchange-algo-trading)
- [Best approaches for the transition](#best-approaches-for-the-transition)
  - [Rebuild the signal stack around forecast updates](#rebuild-the-signal-stack-around-forecast-updates)
  - [Model regimes, not one average market](#model-regimes-not-one-average-market)
  - [Treat execution as a first class source of edge](#treat-execution-as-a-first-class-source-of-edge)
  - [Optimize for joint price and imbalance risk](#optimize-for-joint-price-and-imbalance-risk)
  - [Put physical constraints inside the optimizer](#put-physical-constraints-inside-the-optimizer)
  - [Trade the market sequence, not one venue](#trade-the-market-sequence-not-one-venue)
  - [Build compliance around asset information as well as trade data](#build-compliance-around-asset-information-as-well-as-trade-data)
- [Best verified intraday strategies](#best-verified-intraday-strategies)
  - [Strategies for a trader without physical assets](#strategies-for-a-trader-without-physical-assets)
  - [Strategies for asset backed trading](#strategies-for-asset-backed-trading)
- [Best tips and tricks from the papers](#best-tips-and-tricks-from-the-papers)
- [What usually fails](#what-usually-fails)
- [Practical build order for a new desk](#practical-build-order-for-a-new-desk)
- [Recommended default operating stance](#recommended-default-operating-stance)
- [References](#references)

## Power trading transition playbook

The move from exchange based algo trading into power is not mainly a move into a new asset class. It is a move into a sequential physical market where prices are shaped by forecast revisions, system constraints, and imbalance incentives as much as by order flow. The best papers in the project point to the same conclusion. The winning transition is not to port equity style microstructure models as they are, but to rebuild the stack around forecast driven position management, regime aware execution, and hard physical constraints \[Kie17, Kre21b, Kat20, Kup22, Aid15\].

The literature is strongest on Germany and EPEX, with the clearest transfer path into the broader European intraday market through XBID, single intraday coupling, and flow based cross border effects \[Kat19, Le19, Kri20\]. Czech specific academic evidence is much thinner, so the safest playbook is to treat German and wider European results as the core template, then map them onto local market rules, credit setup, and balancing specifics \[Ber17, Pah15\].

## Bottom line

- The main edge in power intraday is forecast edge, not pure speed. The strongest recurring signals come from wind, solar, load, outage, and residual system updates, especially when the merit order is steep \[Kup22, Kie17, Kre21b\].
- Execution matters far more than in liquid exchange markets because books are thin, spreads are wide, and impact can overwhelm nominal alpha. Order slicing and passive execution are usually better than immediate aggressive trading \[Kat20, Nar21\].
- The right objective is usually not to maximize raw spread capture. It is to maximize expected value net of impact, transaction costs, imbalance exposure, and physical constraints \[Nar21, Aid15, Gla20\].
- Point forecasts are not enough. Distribution and path forecasts are often more useful because power trading is a timing problem under fat tails and asymmetric loss \[Hir22, Ser22, Bun18\].
- Balancing markets should be treated mainly as a residual risk to minimize, not as a primary alpha venue, unless there is a very specific structural advantage \[Nar22\].
- Asset backed trading works best as rolling reoptimization of a physical position, not as a financial overlay pasted onto a plant or battery \[Aid15, Ber20\].

## Where power differs from exchange algo trading

| Dimension | Exchange based algo trading | Power and energy trading implication | Best adaptation |
|:---|:---|:---|:---|
| Price formation | Order flow and news dominate at short horizons | Forecast revisions, residual load, outages, renewable errors, and imbalance incentives drive repricing | Build a fundamentals plus microstructure stack \[Kie17, Kup22\] |
| Liquidity | Usually deeper and more stable | Thin books, lumpy volume, regime shifts near delivery, high spread costs | Slice orders, prefer passive logic, model impact explicitly \[Kat20, Kup21\] |
| Time structure | One instrument with rolling liquidity | Many linked delivery products with day ahead, intraday auction, continuous, and balancing stages | Trade the sequence and cross product dependencies \[Nar21, Hir23\] |
| Risk | Mark to market and execution risk | Joint price, volume, imbalance, and physical feasibility risk | Use probabilistic optimization and scenario limits \[Bun18, Nar22\] |
| Constraints | Mostly financial and regulatory | Ramping, start times, storage limits, cross border capacity, gate closures | Put physical constraints inside the optimizer \[Aid15, Ber20, Kri20\] |
| Compliance | Market abuse and execution rules from finance | REMIT style inside information and manipulation rules sit on top of energy market specifics | Build market surveillance around asset and outage information as well as trades \[Hie20\] |

## Best approaches for the transition

### Rebuild the signal stack around forecast updates

The strongest verified lesson is that intraday power trading is driven by forecast change, not just forecast level. The classic example is an updated renewable forecast that creates a shortage or surplus relative to the day ahead position. In \[Kup22\], a purely speculative strategy with no physical asset makes money by trading these forecast revisions. In \[Kie17\] and \[Kre21b\], intraday prices respond asymmetrically to wind and solar forecast errors, with larger effects when the system is in a steep merit order regime.

The practical implication is simple. A power desk should treat these data feeds as core market data rather than side information:

- Wind and solar nowcasts and forecast deltas
- Load updates and residual load estimates
- Unit outages and availability changes
- Auction curves and merit order slope proxies
- Cross border capacity and coupling status
- Balancing state proxies and recent neighboring product prices

A desk coming from finance often overweights order book features and underweights system state. The literature suggests the reverse mistake is more costly in power \[Kie17, Kre21b, Kup22\].

### Model regimes, not one average market

Power does not have one stationary intraday regime. The same forecast shock has very different price impact when conventional capacity is ample versus when the merit order is steep. \[Kie17\] shows threshold behavior tied to a demand quote regime. \[Kre21b\] sharpens this by linking the regime directly to merit order slope.

That leads to a better modeling blueprint:

- Use regime switching or threshold models for price response
- Condition signal strength on merit order steepness
- Include neighboring contracts because adjacent quarter hours and hours transmit information strongly \[Kre21b, Hir23\]
- Include explicit time to delivery effects because volatility and liquidity change sharply as delivery approaches \[Kat20, Hir22\]
- Treat spike behavior as a regime problem, not a small perturbation around normal returns \[Jon05\]

This is one of the biggest conceptual breaks from exchange based stat arb. In power, it is safer to model state dependent behavior first and only then fit local alpha.

### Treat execution as a first class source of edge

Execution in power intraday is not a back office detail. It is often the difference between a valid signal and a losing trade. \[Kat20\] finds that large orders should generally be sliced rather than executed instantly, and that execution quality depends heavily on order book depth, time to delivery, and market regime. That paper estimates meaningful savings from optimized trajectories relative to naive TWAP for a typical hourly trader.

\[Kup22\] reaches a similar conclusion from another angle. Their forecast based speculative strategy works much better with patient limit order logic than with aggressive market taking. The reason is that bid ask spreads in power are huge relative to liquid financial markets. \[Nar21\] shows the same issue in auctions. For large volumes, minimizing impact is more important than maximizing apparent arbitrage.

Practical execution rules that are well supported by the papers:

- Slice almost any non trivial position into child orders \[Kat20\]
- Prefer passive and adaptive quote management over immediate crossing unless the signal is decaying fast \[Kup22\]
- Increase urgency as delivery approaches, but avoid known costly transition windows around local gate and coupling changes \[Kat20, Hir22\]
- Track execution quality against power relevant benchmarks, not equity ones. ID3, ID1, auction clears, and realized spread are more useful than generic implementation shortfall alone \[Kat20, Nar21\]
- Separate signal generation from impact aware execution. A good forecast can still lose money if routed naively \[Nar21, Ser22\]

### Optimize for joint price and imbalance risk

Many finance traders arrive with a point forecast mentality. The power literature repeatedly shows that this is too narrow. \[Hir22\] finds that fundamental variables often help more with volatility and tail shape than with the next expected return. \[Bun18\] shows that density forecasts beat mean forecasts because they reduce sign flips and large losses in imbalance related trading. \[Ser22\] shows that path forecasts outperform point style approaches for timing execution across the final trading window.

The best desk level adaptation is to split forecasting into three layers:

| Forecast layer | What it predicts | Why it matters |
|:---|:---|:---|
| Direction and relative value | Expected price move or spread between linked products | Opens or closes positions \[Kie17, Kat18\] |
| Distribution | Volatility, tail risk, skew, imbalance exposure | Sizes positions and sets risk limits \[Hir22, Bun18, Nar22\] |
| Path | Sequence of likely prices until delivery | Times execution and optionality capture \[Ser22\] |

This is more useful than a single all purpose alpha model. In power, good traders often win by sizing and timing better, not just by guessing direction better.

### Put physical constraints inside the optimizer

The cleanest way to fail in asset based power trading is to run financial models outside the physical stack. \[Aid15\] shows that optimal trading depends jointly on market impact, imbalance penalties, and production costs. When there are forecast jumps, the optimal policy front loads or delays trading depending on whether price jumps are expected. When production has delay, the whole strategy changes again because flexibility disappears before delivery.

\[Ber20\] shows the same point for storage. An adaptive policy for continuous intraday trading outperforms a rolling intrinsic style benchmark on historical data. \[Gla20\] also models optimal trading with renewable and conventional generation while directly incorporating spread and immediate price impact.

This leads to a robust asset backed design principle:

- Optimize trades and dispatch together
- Carry ramp limits, round trip efficiency, start costs, and delay constraints directly in the state space
- Reoptimize whenever forecasts or plant state changes
- Value flexibility by what it can still do before gate closure, not by an unconstrained mark to market shadow price

### Trade the market sequence, not one venue

European power is a sequence of linked venues. Day ahead positions feed intraday auctions. Intraday auctions feed continuous markets. Residual errors settle in balancing. \[Nar21\] shows that coordinated bidding across day ahead and quarter hourly intraday auctions is materially better than treating them as isolated pools. \[Le19\] and \[Ock20\] show that European intraday design is still heterogeneous across continuous and auction mechanisms. \[Kri20\] highlights that cross border constraints can change price formation in ways that look like market anomalies to a finance trader but are actually network effects.

The practical lesson is to build one optimizer across venues, products, and delivery buckets. The primitive unit is not the trade. It is the residual position by delivery period.

### Build compliance around asset information as well as trade data

A finance background helps with surveillance instincts, but REMIT is not just MAR transplanted into energy. \[Hie20\] emphasizes that energy trading sits inside a fragmented framework with its own reporting, inside information, and manipulation concerns. In practice, outage knowledge, plant availability changes, and operational constraints can be market sensitive information. That means the control framework has to watch the link between operational events and trading, not just classic spoofing style behavior.

## Best verified intraday strategies

### Strategies for a trader without physical assets

| Strategy | Core idea | Why it works | Main limits |
|:---|:---|:---|:---|
| Forecast update directional trading | Trade renewable and load forecast revisions against day ahead anchored positions | Public forecast updates move prices, especially in stressed regimes \[Kup22, Kie17\] | Edge decays as forecasts become commoditized |
| Regime aware mean reversion | Combine short term mean reversion with merit order state and neighboring products \[Kre21b\] | Intraday returns are locally mean reverting but state dependent | Weak if used without fundamentals and delivery state |
| Path forecast execution | Use a distribution of future prices to decide when to place limit orders during the final hours \[Ser22\] | Timing matters as much as direction in thin markets | Requires heavier infrastructure and calibration |
| Cross venue spread trading | Shift execution between auction and continuous venues based on relative value net of impact \[Kat18, Nar21\] | Simple spread logic can monetize forecast differences | Gross spread can vanish after impact and costs |

The best supported speculative intraday strategy in the project is the forecast update strategy from \[Kup22\]. It is important to read that result correctly. The paper does not say that simple public weather variables are a durable free lunch. It says that timely and better renewable forecasts can be monetized if execution is patient and the market remains thin enough for information to diffuse gradually. That is a signal engineering and execution problem, not a pure HFT problem.

A second strong strategy class is regime aware intraday modeling. \[Kre21b\] shows that neighboring contracts and autoregressive price terms carry a lot of information, while \[Kie17\] shows that renewable forecast errors matter much more in stressed system states. The practical strategy is not pure mean reversion. It is conditional mean reversion filtered by residual system state.

\[Ser22\] adds an important refinement. Trading profits do not line up perfectly with classic forecast error metrics. A desk should therefore evaluate intraday models by realized trading value and execution outcomes, not only by RMSE or MAE. This is a major transfer lesson for a finance trader who is used to model contests dominated by statistical fit.

### Strategies for asset backed trading

| Strategy | Best use case | Verified recommendation |
|:---|:---|:---|
| Residual position optimization | Wind, solar, load serving, virtual power plant | Trade the residual error relative to day ahead and update continuously as forecasts change \[Aid15, Gla20\] |
| Adaptive storage trading | Battery and storage assets | Use adaptive intraday policies rather than simple rolling intrinsic logic \[Ber20\] |
| Auction plus continuous co optimization | Larger flexible books | Solve the allocation across venues jointly with impact and transaction costs \[Nar21\] |
| Imbalance avoidance routing | Any balance responsible portfolio | Use continuous intraday to minimize residual imbalance rather than trying to monetize balancing volatility \[Nar22\] |

For an asset backed trader, the most robust strategy is repeated residual optimization. Forecast what the asset will produce or consume, compare that with the current hedge stack, and trade only the residual in the best venue subject to physical constraints and impact. That sounds basic, but it is the center of gravity of the literature \[Aid15, Gla20, Ber20\].

## Best tips and tricks from the papers

- Treat every delivery bucket as its own small market, but never model it alone. Cross product effects are too strong to ignore \[Kre21b, Hir23\].
- Use the latest known traded price and neighboring contract prices as core features. These often matter more than a long list of slower fundamentals for immediate direction \[Kre21b, Ser22\].
- Use fundamentals more aggressively for volatility and tail modeling than for one step expected return \[Hir22\].
- Track a proxy for merit order steepness. The same weather update is far more valuable in a tight system \[Kie17, Kre21b\].
- Build separate logic for hourly and quarter hourly products. Quarter hours are structurally different and often harder to trade well \[Kat18, Kup22\].
- Avoid the temptation to route large volume only into the least obvious venue. \[Nar21\] shows that quarter hourly auction liquidity can be too weak to carry large size efficiently.
- Evaluate strategies on net trading value after spread, impact, and imbalance. Several papers show that better statistical forecasts do not automatically create better trading profits \[Kat18, Ser22, Bun18\].
- Make the optimizer say no trade often. In power, selective trading is a feature, not a bug \[Bun18\].
- Model negative prices and spike regimes explicitly. These are structural features of the market, not dirty data \[Sch11, Jon05\].
- Use balancing forecasts mainly to size residual risk and routing decisions, not to justify routine speculative exposure \[Nar22, Bro22\].

## What usually fails

| Common mistake | Why it fails | Better practice |
|:---|:---|:---|
| Porting equity microstructure models with little system data | Misses the real state variables in power | Fuse market, weather, outage, and system data \[Kie17, Kup22\] |
| Chasing gross arbitrage spreads | Impact and spread erase the edge | Optimize net of impact first \[Nar21, Kat20\] |
| Using only point forecasts | Ignores tail risk and timing value | Use density and path forecasts \[Bun18, Ser22\] |
| Treating balancing as a routine alpha source | Prices are extreme and hard to predict reliably | Minimize residual imbalance \[Nar22\] |
| Running trading logic outside the physical optimizer | Produces infeasible or low value schedules | Co optimize dispatch and trading \[Aid15, Ber20\] |
| Assuming negative prices and spikes are anomalies | Breaks model calibration and risk limits | Use transformations and regime models suited to power \[Sch11, Jon05\] |

## Practical build order for a new desk

1.  Start with a residual position engine by delivery period. Everything should reduce to forecast position minus hedged position.
2.  Add a regime layer using residual load, auction curves, and time to delivery.
3.  Add a cross product feature block so each product sees its neighbors.
4.  Build an impact aware execution layer with passive order placement and child order logic.
5.  Add probabilistic forecasting for volatility, tails, and imbalance exposure.
6.  Put plant and storage constraints directly into the optimizer.
7.  Evaluate everything on realized net value, not just forecast error.
8.  Add compliance controls that link operational events, outage information, and trading decisions under REMIT.

## Recommended default operating stance

For someone moving from exchange based algo trading into European power, the most defensible starting stance is this:

- Trade forecast revisions, not raw price noise
- Size for illiquidity first and alpha second
- Stay mostly inside intraday and use balancing as a penalty to avoid
- Prefer simple regime aware models that are operationally reliable over complex black boxes that ignore physical state
- If assets are involved, optimize dispatch and trade as one problem

That is the core transfer lesson across the strongest papers in the project \[Kat20, Kup22, Nar21, Kie17, Kre21b, Hir22, Aid15, Nar22\].

---

## References

\[Kie17\] R. Kiesel and F. Paraschiv, “Econometric Analysis of 15-Minute Intraday Electricity Prices,” May 01, 2017. doi: [10.1016/J.ENECO.2017.03.002](https://doi.org/10.1016/J.ENECO.2017.03.002).

\[Kre21b\] M. Kremer, R. Kiesel, and F. Paraschiv, “An econometric model for intraday electricity trading,” *Philosophical Transactions of the Royal Society A*, vol. 379, Jun. 2021, doi: [10.1098/rsta.2019.0624](https://doi.org/10.1098/rsta.2019.0624).

\[Kat20\] C. Kath and F. Ziel, “Optimal Order Execution in Intraday Markets: Minimizing Costs in Trade Trajectories,” Sep. 16, 2020.

\[Kup22\] T. Kuppelwieser and D. Wozabal, “Intraday power trading: toward an arms race in weather forecasting?” *OR Spectrum*, vol. 45, pp. 57–83, Nov. 2022, doi: [10.1007/s00291-022-00698-5](https://doi.org/10.1007/s00291-022-00698-5).

\[Aid15\] R. Aïd, P. Gruet, and H. Pham, “An optimal trading problem in intraday electricity markets,” Jan. 19, 2015. doi: [10.1007/s11579-015-0150-8](https://doi.org/10.1007/s11579-015-0150-8).

\[Kat19\] C. Kath, “Modeling Intraday Markets under the New Advances of the Cross-Border Intraday Project (XBID): Evidence from the German Intraday Market,” Nov. 14, 2019. doi: [10.3390/en12224339](https://doi.org/10.3390/en12224339).

\[Le19\] H. L. Le, V. Ilea, and C. Bovo, “Integrated European intra-day electricity market: Rules, modeling and analysis,” Mar. 15, 2019. doi: [10.1016/J.APENERGY.2018.12.073](https://doi.org/10.1016/J.APENERGY.2018.12.073).

\[Kri20\] T. Kristiansen, “The flow based market coupling arrangement in Europe: Implications for traders,” 2020. doi: [10.1016/j.esr.2019.100444](https://doi.org/10.1016/j.esr.2019.100444).

\[Ber17\] S. Béreš, “Impact of Czech intraday market on the electricity prices,” Sep. 18, 2017.

\[Pah15\] I. Paholok, “Credit Value Adjustment and Economic Motivation to Trade on PXE,” 2015. doi: [10.18267/J.PEP.517](https://doi.org/10.18267/J.PEP.517).

\[Nar21\] M. Narajewski and F. Ziel, “Optimal bidding in hourly and quarter-hourly electricity price auctions: Trading large volumes of power with market impact and transaction costs,” Apr. 29, 2021. doi: [10.1016/j.eneco.2022.105974](https://doi.org/10.1016/j.eneco.2022.105974).

\[Gla20\] S. Glas *et al.*, “Intraday renewable electricity trading: advanced modeling and numerical optimal control,” Feb. 04, 2020. doi: [10.1186/s13362-020-0071-x](https://doi.org/10.1186/s13362-020-0071-x).

\[Hir22\] S. Hirsch and F. Ziel, “Simulation-based Forecasting for Intraday Power Markets: Modelling Fundamental Drivers for Location, Shape and Scale of the Price Distribution,” *The Energy Journal*, vol. 45, pp. 107–144, Nov. 2022, doi: [10.5547/01956574.45.3.shir](https://doi.org/10.5547/01956574.45.3.shir).

\[Ser22\] T. Serafin, G. Marcjasz, and R. Weron, “Trading on short-term path forecasts of intraday electricity prices,” Jun. 01, 2022. doi: [10.1016/j.eneco.2022.106125](https://doi.org/10.1016/j.eneco.2022.106125).

\[Bun18\] D. W. Bunn, A. Gianfreda, and S. Kermer, “A Trading-Based Evaluation of Density Forecasts in a Real-Time Electricity Market,” Oct. 05, 2018. doi: [10.3390/EN11102658](https://doi.org/10.3390/EN11102658).

\[Nar22\] M. Narajewski, “Probabilistic Forecasting of German Electricity Imbalance Prices,” May 23, 2022. doi: [10.3390/en15144976](https://doi.org/10.3390/en15144976).

\[Ber20\] G. Bertrand and A. Papavasiliou, “Adaptive Trading in Continuous Intraday Electricity Markets for a Storage Unit,” May 01, 2020. doi: [10.1109/TPWRS.2019.2957246](https://doi.org/10.1109/TPWRS.2019.2957246).

\[Kup21\] T. Kuppelwieser and D. Wozabal, “Liquidity costs on intraday power markets: Continuous trading versus auctions,” Jul. 01, 2021. doi: [10.1016/J.ENPOL.2021.112299](https://doi.org/10.1016/J.ENPOL.2021.112299).

\[Hir23\] S. Hirsch and F. Ziel, “Multivariate simulation‐based forecasting for intraday power markets: Modeling cross‐product price effects,” *Applied Stochastic Models in Business and Industry*, Jun. 2023, doi: [10.1002/asmb.2837](https://doi.org/10.1002/asmb.2837).

\[Hie20\] L. Hiemstra, “REMIT: ten years and counting,” Sep. 21, 2020. doi: [10.1080/17521440.2020.1805870](https://doi.org/10.1080/17521440.2020.1805870).

\[Jon05\] C. de Jong, “The Nature of Power Spikes: A Regime-Switch Approach,” Oct. 14, 2005. doi: [10.2202/1558-3708.1361](https://doi.org/10.2202/1558-3708.1361).

\[Kat18\] C. Kath and F. Ziel, “The value of forecasts: Quantifying the economic gains of accurate quarter-hourly electricity price forecasts,” Oct. 01, 2018. doi: [10.1016/j.eneco.2018.10.005](https://doi.org/10.1016/j.eneco.2018.10.005).

\[Ock20\] F. Ocker and V. Jaenisch, “The way towards European electricity intraday auctions – Status quo and future developments,” Oct. 01, 2020. doi: [10.1016/j.enpol.2020.111731](https://doi.org/10.1016/j.enpol.2020.111731).

\[Sch11\] S. Schneider, “Power Spot Price Models with negative Prices,” Dec. 01, 2011. doi: [10.21314/JEM.2011.079](https://doi.org/10.21314/JEM.2011.079).

\[Bro22\] J. Browell and C. Gilbert, “Predicting Electricity Imbalance Prices and Volumes: Capabilities and Opportunities,” May 16, 2022. doi: [10.3390/en15103645](https://doi.org/10.3390/en15103645).
