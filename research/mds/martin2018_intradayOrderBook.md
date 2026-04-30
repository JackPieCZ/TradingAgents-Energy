| German |          |     | Intraday |     |        | Electricity |     |     | Market |       | Analysis |      |     | and |     |
| ------ | -------- | --- | -------- | --- | ------ | ----------- | --- | --- | ------ | ----- | -------- | ---- | --- | --- | --- |
|        | Modeling |     |          |     | based  |             | on  | the | Limit  | Order |          | Book |     |     |     |
|        |          |     | Henry    |     | Martin |             |     |     |        | Scott | Otterson |      |     |     |     |
Institute of Cartography and Geoinformation Fraunhofer Institute for Energy Economics
ETH Zurich, Stefano-Franscini-Platz 5 and Energy System Technology
|               |       | 8093       | Zurich,  |                  | Switzerland |              |              |     |     | 34119                        | Kassel, | Germany |     |     |     |
| ------------- | ----- | ---------- | -------- | ---------------- | ----------- | ------------ | ------------ | --- | --- | ---------------------------- | ------- | ------- | --- | --- | --- |
|               |       |            | e-mail:  | martinhe@ethz.ch |             |              |              |     |     | e-mail: scotto@sharpleaf.org |         |         |     |     |     |
| Abstract—This |       | paper      | presents | a market         | model       |              | for the EPEX |     |     |                              |         |         |     |     |     |
| SPOT German   |       | continuous | intraday |                  | market      | for electric | power        |     |     |                              |         |         |     |     |     |
| trading       | based | on the     | limit    | order            | book (LOB). |              | We use the   |     |     |                              |         |         |     |     |     |
| EPEX SPOT     |       | M7 order   | book     | data,            | which       | contains     | all orders   |     |     |                              |         |         |     |     |     |
submittedtotheGermancontinuousintradaymarket,tosimulate
| the historic   | course | of the     | market. | Thereby,   |            | we reconstruct | the          |     |     |     |     |     |     |     |     |
| -------------- | ------ | ---------- | ------- | ---------- | ---------- | -------------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| complete       | state  | of the     | LOB at  | every      | point      | in (trading)   | time.        |     |     |     |     |     |     |     |     |
| We validate    | our    | simulation | by      | comparing  | the        | transactions   | that         |     |     |     |     |     |     |     |     |
| our simulation |        | generated  | with    | the actual | historical |                | transactions |     |     |     |     |     |     |     |     |
availablefromadifferentdataset.TheLOBbasedmarketmodel
| can be | used to | include | price | volatility | risk | and illiquidity | risk |     |     |     |     |     |     |     |     |
| ------ | ------- | ------- | ----- | ---------- | ---- | --------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
whensimulatingtradingattheEPEXSPOTcontinuousintraday
| market.         | Furthermore, |           | we present   | all      | preprocessing |        | steps and |         |               |        |             |            |                 |     |          |
| --------------- | ------------ | --------- | ------------ | -------- | ------------- | ------ | --------- | ------- | ------------- | ------ | ----------- | ---------- | --------------- | --- | -------- |
| decision        | rules        | necessary | to correctly |          | identify      | orders | from the  |         |               |        |             |            |                 |     |          |
|                 |              |           |              |          |               |        |           | Fig.    | 1: Comparison | of     | German      | day-ahead, | volume-weighted |     |          |
| often ambiguous |              | EPEX      | SPOT         | M7 order | book          | data.  |           |         |               |        |             |            |                 |     |          |
|                 |              |           |              |          |               |        |           | average | intraday      | price, | and minimum |            | and maximum     |     | intraday |
|                 |              | I.        | INTRODUCTION |          |               |        |           |         |               |        |             |            |                 |     |          |
prices.
A. TheImportanceoftheGermanContinuousIntradayMarket
| From      | 2010   | to 2016, | the power | generation |      | from | intermittent |        |          |        |             |           |     |              |     |
| --------- | ------ | -------- | --------- | ---------- | ---- | ---- | ------------ | ------ | -------- | ------ | ----------- | --------- | --- | ------------ | --- |
|           |        |          |           |            |      |      |              | of the | flexible | energy | application | interacts |     | with a model | of  |
| renewable | energy | sources  | in        | Germany    | rose | by   | about 100    | %      |          |        |             |           |     |              |     |
from 82 TWh to 161 TWh [BNetzA Bundesnetzagentur, 2017, the intraday market. The reliability of the simulation result
|         |        |            |     |        |        |     |            | is then | directly | dependent | of  | the quality | of  | both models. | In  |
| ------- | ------ | ---------- | --- | ------ | ------ | --- | ---------- | ------- | -------- | --------- | --- | ----------- | --- | ------------ | --- |
| p. 68]. | In the | same time, | the | volume | traded | at  | the German |         |          |           |     |             |     |              |     |
continuousintradaymarketrosebyabout400%from10TWh energy system research, the tested flexible energy applications
to 41 TWh [BNetzA Bundesnetzagentur, 2017, p. 189]. The are often modeled highly detailed and in a very sophisticated
|        |            |          |     |        |       |       |            | way, | while | the used market | model | is often | oversimplified |     | and |
| ------ | ---------- | -------- | --- | ------ | ----- | ----- | ---------- | ---- | ----- | --------------- | ----- | -------- | -------------- | --- | --- |
| German | continuous | intraday |     | market | is of | great | importance |      |       |                 |       |          |                |     |     |
for the trading of renewable energy generation in Germany can thus be a bottleneck for the overall performance of the
simulation.
| because | it offers | the possibility |     | to trade | power | shortly | before |     |     |     |     |     |     |     |     |
| ------- | --------- | --------------- | --- | -------- | ----- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
the start of power delivery. Market participants can take Powermarketmodelsoftenassumethatthereisasingleprice
advantage of precise short-term forecasts to either trade with a for each power delivery time (the time when power delivery
lower risk of forecast errors or to correct trading errors made starts). This is a good fit for the German day-ahead market,
at an earlier point in time (e.g. at the day-ahead market). a uniform priced auction, where every (successful) market
|             |     |       |           |     |           |     |              | participant |     | receives the | same price. | However, |     | in the | German |
| ----------- | --- | ----- | --------- | --- | --------- | --- | ------------ | ----------- | --- | ------------ | ----------- | -------- | --- | ------ | ------ |
| This allows | to  | avoid | the usage | of  | expensive |     | and security |             |     |              |             |          |     |        |        |
relevant balancing power. At the same time, the German continuous intraday market each delivery time generally has a
continuous intraday market becomes interesting for flexible large number of volatile prices, the result of a price building
energy applications like demand-side-management [Siano and mechanism using a limit order book (LOB), and following the
Sarno, 2016], cogeneration [Mitra et al., 2013], or virtual pay-as-bid principle
power plants [Wille-Haussmann et al., 2010], that can generate Some intraday market models have assumed a single price,
profit by providing their flexibility at the market [Goutte and for example, the volume-weighted average price per delivery
Vassilopoulos, 2017] [Resch et al., 2017]. time, as it can be directly computed from historical data, a
|        |            |        |              |        |     |      |              | practical | choice    | at the  | time because | the | data | needed | to know |
| ------ | ---------- | ------ | ------------ | ------ | --- | ---- | ------------ | --------- | --------- | ------- | ------------ | --- | ---- | ------ | ------- |
| B. The | Importance | of     | Market       | Models |     |      |              |           |           |         |              |     |      |        |         |
|        |            |        |              |        |     |      |              | the       | LOB state | was not | available.   |     |      |        |         |
| Before | flexible   | energy | applications |        | are | used | in practice, |           |           |         |              |     |      |        |         |
Unfortunately,simulationsbasedonasinglepricecanleadto
their profitability is tested in simulations. Hereby a model an underestimation of the true trading risk. This can be seen in
978-1-5386-1488-4/18/$31.00(cid:13)c2018IEEE Figure 1,wherebetweenhours16and18,thevolume-weighted

average price of the intraday market corresponds closely to et al., 2013] [Ros¸u, 2009]. An order can be defined as a
the day-ahead price but the minimum and maximum prices commitment to buy or sell a fixed quantity of the traded good
for these delivery times indicate a very volatile trading period. for a defined price or ”better” (lower for buy, higher for sell).
Apart from the trading risk, such a single price model does Once an order for a delivery time is submitted, it enters the
assumethatthepriceisconstant.Inrealityhowever,theGerman delivery time’s LOB and is checked for opposing orders that
intradaymarketshowsoftensignsofilliquidity[Hagemannand fulfillitspricerestrictions.Otherwise,theorderiscalledalimit
Weber,2013]andpricescanforexamplebestronglydependent order, and stays active in the LOB until it is fully matched
on the trading-volume. by one or more opposing orders entering the LOB; until it is
canceled by the owner; or until the market closes.
C. Added Value of our Paper
If an order that enters the LOB is at least partially matched
We use the EPEX SPOT M7 order book data, a new data with an existing opposite order, it is called a market order.
set that contains all orders submitted to the intraday market, to In this case, the order gets ”matched” with the best opposite
simulate the LOB from the moment the intraday market opens order (highest priced buy order, lowest priced sell order) that
until market close. This simulation has two great benefits, first existsintheLOBandimmediatelygeneratesatransaction.The
of all it gives access to the complete market state (bid-ask- price of the transaction is defined by the price of the already
spread, LOB-depth, etc.) [Gould et al., 2013] [Neuhoff et al., existing limit order, the volume of the transaction corresponds
2016] at any point in time, data that can be used to analyze to the minimal volume of both orders. After the transaction,
how trading behavior depends on the current market situation the volumes of both orders are updated by subtracting the
[?]. Secondly, the simulation can be used as a market model transactionvolume.Noweitherthemarketorder,thelimitorder
which allows a more correct simulation of trading risk and or both orders are completely consumed. A consumed order
illiquidity. To enable others to reproduce this approach we is deleted from the LOB. If the limit order is not consumed,
describe all preprocessing steps necessary to correctly interpret it stays with its remaining volume in the LOB, if the market
the M7 EPEX SPOT order book data set. order is not consumed, it continuous to match the next limit
We start in Section II with a review of the price building order with the next best price. If existing orders can no longer
mechanism of the EPEX SPOT continuous intraday market, fulfill the price restriction of the incoming order, it stays with
in Section III we describe the EPEX SPOT M7 order book its remaining volume and its maximum price in the LOB like
data. Section IV covers the necessary preprocessing steps, a limit order.
the simulation and the validation of the market simulation For every transaction, the owner of a limit order gets the
framework. Finally, in Section V, we discuss the results and price she submitted. The example in Figure 2 illustrates the
potential applications. so-calledpay-as-bidprincipleofaLOBmarketforonedelivery
time. We can observe three transactions with three different
II. CONTINUOUSGERMANINTRADAYMARKET
prices for the same delivery time, which where potentially
A. Power Trading in Germany traded at (almost) the same time. This is in a strong contrast
On the German market wholesale level, utilities can trade to the uniform pricing rules of the day-ahead auction and can
power in several ways. They can trade directly with each other result in very volatile prices [Goutte and Vassilopoulos, 2017].
(over the counter trading) or they can trade at one of the
C. Price Dependence on Delivery and Trading Time
two power exchanges: the European Energy Exchange (EEX),
which organizes the derivatives market, where power can be The limit order book rules imply that for the German
traded up to six years in advance until several days before continuous intraday market, price is not only defined by
delivery, or the European Power Exchange (EPEX SPOT), the delivery time but also by when the power is traded for
which organizes the spot market. a specific delivery time. For example on the EPEX SPOT
Power can be traded on the spot market in several ways. On continuous intraday market for 15-minute contracts, there are
the day before delivery, power can be traded at the day-ahead 96 independent LOBs open at the same time, one for every
auction and the intraday auction. After these auctions, the delivery period. The LOBs are closed sequentially 30 minutes
continuous intraday market starts for all delivery times of the before the delivery period. Depending on the delivery time,
next day at 3pm for 1-hour contracts; at 3:30pm for 30-minute each LOB stays open for 7.5 hours to 31.5 hours. During
products; and at 4pm for 15-minute products. In Germany, this trading period, the price for the same delivery period can
power at the EPEX SPOT continuous intraday market can be vary greatly. This is also illustrated in Figure 2, which could
traded until 30-minutes before start of delivery, and since June represent a sequence of offers for the same delivery time.
2017, up to 5-minutes before the start of delivery for trades
D. Order Types, Order Restriction and Market Actions
within the same control zone.
Market participants that want to trade power in the con-
B. Price Building at the Continuous Intraday Market
tinuous intraday market, can choose between different order
Prices in the continuous intraday market are found using a types. Here is a list of order types that are available during the
set of LOBs (one for each delivery time). This is a widespread continuous intraday trading [EPEXSPOT, 2014] [EPEXSPOT,
mechanism for price formation in continuous markets [Gould 2017]

|     |     |     |     |     |     |     |     | Activation/Deactivation: |     |     |     | Market | participants | have | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | ------ | ------------ | ---- | --- |
•
|     |     |     |     |     |     |     |     | possibility |         | to temporarily |     | deactivate | and | later to reactivate |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | -------------- | --- | ---------- | --- | ------------------- | --- |
|     |     |     |     |     |     |     |     | their       | orders. |                |     |            |     |                     |     |
Modify:Priceandvolumeofactiveorderscanbeadjusted.
•
• Cancel:Marketparticipantscancanceltheiractiveorders.
III. EPEXSPOTLOBDATA
| (a) Example   | of a        | 5 MWh            | market | (b)TheLOBafterthetransaction |         |             |                  |              |           |      |      |                |             |     |         |
| ------------- | ----------- | ---------------- | ------ | ---------------------------- | ------- | ----------- | ---------------- | ------------ | --------- | ---- | ---- | -------------- | ----------- | --- | ------- |
| order to      | sell, that  | matches          | the    | from                         | 2a.     | The matched | volume           |              |           |      |      |                |             |     |         |
|               |             |                  |        |                              |         |             |                  | A. Available | datasets  |      |      |                |             |     |         |
| best limit    | order       | to buy           | power  | was                          | deleted | from        | the LOB. The     |              |           |      |      |                |             |     |         |
| at 30 EUR/MWh |             | (red rectangle). |        | remaining                    |         | volume      | is still active. |              |           |      |      |                |             |     |         |
|               |             |                  |        |                              |         |             |                  | There        | are three | data | sets | with different | resolutions |     | for the |
| The result    | is a        | transaction      |        | of                           |         |             |                  |              |           |      |      |                |             |     |         |
|               |             |                  |        |                              |         |             |                  | analysis     | of the    | EPEX | SPOT | intraday       | market:     |     |         |
| 5MWh for      | 30 EUR/MWh. |                  |        |                              |         |             |                  |              |           |      |      |                |             |     |         |
1) Aggregatedmarketdata:
IsfreelyavailableviatheEPEX
|     |     |     |     |     |     |     |     | SPOT homepage1. |       | This | data     | set provides | a                       | single price | for |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ----- | ---- | -------- | ------------ | ----------------------- | ------------ | --- |
|     |     |     |     |     |     |     |     | each delivery   | time, | for  | example, | the          | volume-weighted-average |              |     |
price.
|     |     |     |     |     |     |     |     | 2) Transaction |      | data:       | Can   | be purchased | from         | EPEX   | SPOT, |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---- | ----------- | ----- | ------------ | ------------ | ------ | ----- |
|     |     |     |     |     |     |     |     | describes      | the  | prices and  | times | at           | which LOB    | orders | were  |
|     |     |     |     |     |     |     |     | satisfied      | by a | transaction | but   | it does      | not describe | when   | the   |
(c) Example of a 30 MWh mar- (d)TheLOBafterthetransaction orders entered the LOB or give information about orders that
| ket order  | to buy,       | that | fully con- | from      | 2c.     | The matched | volume         |         |         |               |       |     |         |               |     |
| ---------- | ------------- | ---- | ---------- | --------- | ------- | ----------- | -------------- | ------- | ------- | ------------- | ----- | --- | ------- | ------------- | --- |
|            |               |      |            |           |         |             |                | did not | lead to | transactions. |       |     |         |               |     |
| sumes the  | best opposite |      | order      | at was    | deleted | from        | the LOB. The   |         |         |               |       |     |         |               |     |
|            |               |      |            |           |         |             |                | 3) The  | M7      | order book    | data: | A   | dataset | that contains | all |
| 42 EUR/MWh | and           | then | matches    | partially |         | consumed    | order is still |         |         |               |       |     |         |               |     |
the next best opposite order at active with the remaining vol- orders that have been submitted to the intraday market,
48 EUR/MWh (red rectangles). ume. including orders that never resulted in a transaction or orders
| The result  | is a       | transaction | of  | 5   |     |     |     |                |           |        |      |               |          |              |         |
| ----------- | ---------- | ----------- | --- | --- | --- | --- | --- | -------------- | --------- | ------ | ---- | ------------- | -------- | ------------ | ------- |
|             |            |             |     |     |     |     |     | that were      | canceled. | This   | data | theoretically | allows   | the complete |         |
| MWh for     | 42 EUR/MWh |             | and | a   |     |     |     |                |           |        |      |               |          |              |         |
|             |            |             |     |     |     |     |     | reconstruction |           | of the | LOB  | state at      | any time | of the       | trading |
| transaction | for        | 25 MWh      | for | 48  |     |     |     |                |           |        |      |               |          |              |         |
period.
EUR/MWh.
|                 |     |           |     |           |     |        |            | Table I    | shows | the order | information |                | available | in the     | EPEX   |
| --------------- | --- | --------- | --- | --------- | --- | ------ | ---------- | ---------- | ----- | --------- | ----------- | -------------- | --------- | ---------- | ------ |
| Fig. 2: Example |     | of orders |     | submitted | in  | an LOB | market and |            |       |           |             |                |           |            |        |
|                 |     |           |     |           |     |        |            | SPOT order | book  | data      | set. It     | is categorized |           | by whether | or not |
their effect on the LOB. In this example, two orders were it is available at the moment of order submission (ex-ante) or
| submitted | after | another | and | resulted | in three | transactions | with |     |     |     |     |     |     |     |     |
| --------- | ----- | ------- | --- | -------- | -------- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
after (ex-post).
| three different |       | prices | (30, 42,  | 48  | EUR/MWh) |                |       |            |          |             |     |           |             |          |      |
| --------------- | ----- | ------ | --------- | --- | -------- | -------------- | ----- | ---------- | -------- | ----------- | --- | --------- | ----------- | -------- | ---- |
|                 |       |        |           |     |          |                |       | TABLE      | I: Order | information |     | available | in          | the EPEX | SPOT |
|                 |       |        |           |     |          |                |       | order book | data     | separated   | in  | ex-ante   | and ex-post | data.    |      |
| A limit         | order | is     | the offer | to  | buy or   | sell a defined | power |            |          |             |     |           |             |          |      |
•
volume for a specific price or better, as discussed in Ex-ante Ex-post
|         |        |     |            |        |     |            |          |     |     | Instrumenttype     |     | Isexecuted      |     |     |     |
| ------- | ------ | --- | ---------- | ------ | --- | ---------- | -------- | --- | --- | ------------------ | --- | --------------- | --- | --- | --- |
| Section | II-B.  |     |            |        |     |            |          |     |     |                    |     |                 |     |     |     |
|         |        |     |            |        |     |            |          |     |     | Deliveryinstrument |     | Endvaliditydate |     |     |     |
| Iceberg | orders |     | are ”large | volume |     | orders[for | the same |     |     |                    |     |                 |     |     |     |
| •       |        |     |            |        |     |            |          |     |     | Deliverydate       |     | Cancelingdate   |     |     |     |
delivery time], divided into several smaller orders which Startvaliditydate Executionprice
|     |         |        |       |      |               |     |            |     |     | Status |     | Executedvolume |     |     |     |
| --- | ------- | ------ | ----- | ---- | ------------- | --- | ---------- | --- | --- | ------ | --- | -------------- | --- | --- | --- |
| are | entered | in the | order | book | sequentially” |     | (EPEXSPOT, |     |     |        |     |                |     |     |     |
Side
| 2014). | This | allows | market | participants |     | who | need to trade |     |     |     |     |     |     |     |     |
| ------ | ---- | ------ | ------ | ------------ | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Price
| large | amounts | to  | conceal | their | total | trading | volume and |     |     | Volume |     |     |     |     |     |
| ----- | ------- | --- | ------- | ----- | ----- | ------- | ---------- | --- | --- | ------ | --- | --- | --- | --- | --- |
InitialID
| thus | limit | the market | impact |     | of their | actions | [Gould et al., |     |     |     |     |     |     |     |     |
| ---- | ----- | ---------- | ------ | --- | -------- | ------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ParentID
| 2013].                 | At            | the EPEX      | SPOT     |              | intraday    | market     | an iceberg    |                               |         |          |          |         |                         |              |     |
| ---------------------- | ------------- | ------------- | -------- | ------------ | ----------- | ---------- | ------------- | ----------------------------- | ------- | -------- | -------- | ------- | ----------------------- | ------------ | --- |
| order                  | consists      | of            | several, | equally      | sized       | limit      | orders, each  |                               |         |          |          |         |                         |              |     |
| with                   | a minimal     |               | size of  | 25 MW.       |             |            |               |                               |         |          |          |         |                         |              |     |
|                        |               |               |          |              |             |            |               | B. Difficulties               |         | with the | EPEX     | SPOT    | LOB Data                |              |     |
| Additional             | to            | the different |          | order        | types,      | market     | participants  |                               |         |          |          |         |                         |              |     |
|                        |               |               |          |              |             |            |               | An LOB                        | user    | must     | overcome | various | data                    | problems.    |     |
| can restrict           | the           | execution     | of       | their        | orders.     | Here is    | a list of the |                               |         |          |          |         |                         |              |     |
|                        |               |               |          |              |             |            |               | 1) ErroneousOrderInformation: |         |          |          |         | ThefieldsExecutionPrice |              |     |
| possible               | restrictions, |               | market   | participants |             | can choose | from:         |                               |         |          |          |         |                         |              |     |
|                        |               |               |          |              |             |            |               | and Execution                 |         | Volume   | contain  | errors  | and cannot              | be used2.    |     |
| • Immediate-or-cancel: |               |               |          | The order    | is          | either     | immediately   |                               |         |          |          |         |                         |              |     |
|                        |               |               |          |              |             |            |               | 2) Overlapping                |         | Content: |          | The M7  | order                   | book dataset | is  |
| executed               | or            | automatically |          | canceled.    |             |            |               |                               |         |          |          |         |                         |              |     |
|                        |               |               |          |              |             |            |               | delivered                     | by EPEX | SPOT     | as       | one or  | more Excel              | spreadsheets |     |
| Fill-or-kill:          |               | The           | order    | is either    | immediately |            | and entirely  |                               |         |          |          |         |                         |              |     |
•
|             |     |          |       |               |     |            |        | per month. | Adjacent  |     | months      | sometimes | overlap | for      | several |
| ----------- | --- | -------- | ----- | ------------- | --- | ---------- | ------ | ---------- | --------- | --- | ----------- | --------- | ------- | -------- | ------- |
| executed    | or  | canceled | in    | its entirety. |     |            |        |            |           |     |             |           |         |          |         |
|             |     |          |       |               |     |            |        | days. This | redundant |     | information |           | must be | detected | and be  |
| All-or-none |     | The      | order | is executed   |     | completely | or not | at         |           |     |             |           |         |          |         |
•
deleted.
all.
| After | an order | is submitted, |     | market | participants |     | have several |     |     |     |     |     |     |     |     |
| ----- | -------- | ------------- | --- | ------ | ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
1http://www.epexspot.com/en/market-data/intradaycontinuous/
actions available. 2ThiswascommunicatedbyEPEXSPOTpriortopurchase.

3) Simulation of Austrian Orders: Germany and Austria 3) Market Actions: Market actions (Section II-D) also
are in the same market area but the EPEX SPOT LOB data appearasrowsintheEPEXSPOTdata.Herewedescribehow
includes only orders for power generated within, or to be market actions are identified.
delivered to, Germany. We attempt to complete the order • Order Modifications: Once an order is submitted, the
flow using EPEX SPOT intraday transaction data, which ownermaymodifyitspriceorvolume.IntheEPEXSPOT
includes transactions delivered to or from Austria. If power data,modificationactionshavethesameIDasanexisting
wasdeliveredto(respectivelyfrom)theAustriandeliveryzone, order and a non-empty Canceling time field containing
a buy (respectively sell) order with the same volume, price themodificationtimestamp.Itisfollowedbyaneworder
and delivery time as the transaction is created. with the same ID and a modified price or volume. So that
the simulation can identify modifications, a modification
IV. SIMULATIONOFTHECONTINUOUSGERMANINTRADAY flag is introduced in a preprocessing step. This is done by
MARKET iterating the LOB data and whenever a row with an ID
thatalreadyappearedhasanonemptyfieldCancelingtime
The sequence of simulated LOB states, along with the and is not the last row with this ID, this row is marked
transaction volumes and pricing they emit, is generated by as a modification.
processing the EPEX SPOT order book data for one delivery • Activation and Deactivation of Orders: Market par-
time,order-by-order.Unfortunately,noteveryrowintheEPEX ticipants may deactivate an order temporarily and later
SPOT order book data corresponds to an individual submitted reactivate it. A deactivation appears in the order flow as
order. an item with the ID of an existing order and the field
Status set to N. The Canceling time field is filled with the
reactivation time of the order.
A. Identify Orders in the EPEX SPOT LOB data
• Cancellations:Marketparticipantsmaycanceltheiractive
Here, we describe how we extract the meaning of the EPEX limit orders. A cancellation can be identified by the non-
SPOT data rows, and which LOB actions are taken in response empty Canceling time after modification and deactivation
to them. actions have already been excluded.
1) Orders: Most of the rows in the EPEX SPOT data
B. Implementation and Simulation
correspond to orders. Orders are identified by excluding all
The Lob is simulated by processing the EPEX SPOT data
other cases:
row by row and consists of two tasks: The interpretation of the
• Limit Orders and Market Orders: If a new order matches currentrowoftheEPEXSPOTdataandthereproductionofthe
an opposing order, the order is identified as market order.
market mechanisms. The order flow is processed sequentially
If not, it is classified as a limit order (see Section II-B).
andonlyvalidorderswithrespecttothespecialcasesdiscussed
• Iceberg Orders: In the moment of their submission, only in section IV-A, are presented to an order book object, which
the first suborder of an iceberg order appears as a row in
reproduces the LOB mechanism. The simulation process is
theEPEXSPOTdata.Oncethevisibleorderisconsumed,
shown in Figure 3.
it is immediately followed by an order with the same
ID and with volume zero, and this is followed by a new C. Validation
order with the same ID and the new volume. Since all The information provided in the EPEX SPOT order book
suborders spawned by an iceberg order have the same data is not sufficiently detailed to identify all order types,
ID, they cannot be distinguished from reborn orders (see market actions and order restrictions with certainty. This leads
IV-A2) which are ignored during the simulation. To be to an error in the reconstruction of the historic LOB state.
able to correctly identify all parts of an iceberg orders, This true LOB state is not observable, but we can compare
we assign them with unique IDs in a preprocessing step. the transactions the LOB simulation generates with the actual
This is done by iterating the LOB data and whenever an historical transactions (Section III-A2). The EPEX SPOT
order with volume zero appears, all following orders with transaction data contains all individual intraday transactions
the same ID are equipped with a new ID. withtheirvolumeandpriceinformation.Weconsiderthetrans-
• Restricted Orders: Unfortunately, it was not possible for action data to be ground-truth information and the generated
us to identify the different restrictions given the limited transactions should match them as closely as possible. The
information in the order flow. match is assessed over April 2015 to December 2016, using
three derived transaction statistics:
2) Rebirth of Partially Matched Orders: Limit orders are
often only partially matched. In this case, the order reappears • Number of transactions
inthedataasaneworderwiththesameID,priceandwiththe • Volume weighted average price
residual volume. So that the number of submitted orders can • Traded volume
be properly counted, the reborn order must be distinguished We calculate the three transaction statistics as totals for each
fromoriginalneworders.Wedothisbykeepingtrackofactive deliverytimeandeachday(e.g.thetotaltradedvolumeonday
order IDs during the simulation. 1fordeliveryperiod1)andthencompareittothegroundtruth.

|     |     |     |     |     |     |     | TABLE          | II: Simulated |           | transactions | compared |             | to the   | official |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------------- | --------- | ------------ | -------- | ----------- | -------- | -------- |
|     |     |     |     |     |     |     | transactions   | data          | set. Mean | and          | median   | of the      | absolute | errors   |
|     |     |     |     |     |     |     | calculated     | for every     | delivery  | time         | on       | every       | day from | April    |
|     |     |     |     |     |     |     | 2015 to        | December      | 2016.     |              |          |             |          |          |
|     |     |     |     |     |     |     | Nameoferror    |               |           | Volume       |          | No.oftrades | Price    |          |
|     |     |     |     |     |     |     | Meanerrorin%   |               |           | 11.58%       |          | 8.86%       | 13.52%   |          |
|     |     |     |     |     |     |     | Medianerrorin% |               |           | 6.6%         |          | 6.17%       | 1.38%    |          |
Number of transactions
|     |     |     |     |     |     |     | 104 |     | average per delivery time from Apr 15 to Dec 16 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- |
9
Intraday transaction data (baseline)
|     |     |     |     |     |     |     | 8   |     |     |     |     | Order book simulation |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- |
7
sedart fo rebmuN
6
5
4
3
2
|     |     |     |     |     |     |     | 0   | 10 20 | 30  | 40 50 | 60  | 70  | 80 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- | --- | ----- | --- |
Delivery time (as 15 minute increments)
(a)
Volume weighted average transaction price
average per delivery time from Apr 15 to Dec 16
50
Intraday transaction data (baseline)
|     |     |     |     |     |     |     | 45  |     |     |     |     | Order book simulation |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- |
hWM/RUE ni ecirP 40
35
30
25
20
15
|     |     |     |     |     |     |     | 0   | 10  | 20 30 | 40  | 50 60 | 70  | 80 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- | ----- | --- |
Delivery time (as 15 minute increments)
(b)
Total transaction volume per delivery time
|     |     |     |     |     |     |     | 105 |     |     | from Apr 15 to Dec 16 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- |
7
Intraday transaction data (baseline)
|     |     |     |     |     |     |     | ruoh retrauq/hWM ni emuloV 6 |     |     |     |     | Order book simulation |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --------------------- | --- | --- |
5
4
3
2
| Fig. | 3: Work flow | of the historic |     | order | flow simulation. |     |     |     |     |     |     |     |     |     |
| ---- | ------------ | --------------- | --- | ----- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
0
|     |     |     |     |     |     |     | 0   | 10 20 | 30  | 40 50 | 60  | 70  | 80 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- | --- | ----- | --- |
Delivery time (as 15 minute increments)
Figure 4 shows the results for all three transaction statistics. (c)
| The comparisons | of Figure      | 4 show     | that        | the    | simulation | follows      |            |            |       |                  |          |           |             |        |
| --------------- | -------------- | ---------- | ----------- | ------ | ---------- | ------------ | ---------- | ---------- | ----- | ---------------- | -------- | --------- | ----------- | ------ |
|                 |                |            |             |        |            |              | Fig. 4:    | Comparison | of    | the transactions |          | generated |             | by the |
| the true        | behavior very  | closely.   | The average |        | price      | per delivery |            |            |       |                  |          |           |             |        |
|                 |                |            |             |        |            |              | simulation | of the     | order | flow and         | the EPEX | SPOT      | transaction |        |
| time is         | matched almost | perfectly, | the         | number | of         | transactions |            |            |       |                  |          |           |             |        |
data.
| is slightly    | overestimated | and     | the traded |     | volume | is slightly |     |     |     |     |     |     |     |     |
| -------------- | ------------- | ------- | ---------- | --- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| underestimated | at peak       | trading | times.     |     |        |             |     |     |     |     |     |     |     |     |
Table II shows the numerical results of the comparison. The a trader suspects the existence of so-called iceberg orders, he
average of the absolute errors of the total transactions volume may repeatedly submit fill-or-kill orders to find them. Without
| per delivery | time was | 11.58 % | and the | average | of  | the absolute |     |     |     |     |     |     |     |     |
| ------------ | -------- | ------- | ------- | ------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
correctlyidentifyingtherestriction,theordercanmatchexisting
errors of the total number of trades was 8.86 %. For all three orders even if it is only filled partially. The missing restriction
| error categories | the median      | is    | much | lower than | the    | mean. This  |             |       |         |                    |     |     |            |     |
| ---------------- | --------------- | ----- | ---- | ---------- | ------ | ----------- | ----------- | ----- | ------- | ------------------ | --- | --- | ---------- | --- |
|                  |                 |       |      |            |        |             | information | could | explain | the overestimation |     | of  | the number | of  |
| is evidence      | of few delivery | times |      | which      | have a | large error | trades.     |       |         |                    |     |     |            |     |
| while most       | of the delivery | times | have | a small    | error. |             |             |       |         |                    |     |     |            |     |
|                  |                 |       |      |            |        |             |             |       | V.      | CONCLUSION         |     |     |            |     |
Apossiblesourceoferrorareorderrestrictionsthatcouldnot
be identified (Section IV-A1). An example of a restricted order Inthiswork,weusedtheEPEXSPOTM7orderflowdatato
is a fill-or-kill order, which allows traders to test the market simulatethelimitorderbookofthecontinuousGermanintraday
for hidden liquidity (iceberg-orders) [Cesari et al., 2012]. If market.Thisrepresentationgivesaccesstothecompletemarket

state for every moment in trading time for every delivery
time. We validated the simulation by comparing the resulting
transactions of our simulation to the official EPEX SPOT
transaction data set. Additionally, the simulation can be used
as a market model by simply adding new orders to the list of
the EPEX SPOT order book data. This market model allows
to model trading risk and allows market participants to test
weathertheyperformbetterorworsethanthevolume-weighted
average price depending on their trading strategy. The model
allows prices to be different for buy and sell actions and can
also represent illiquidity by modeling the relation between
price and volume (e.g. the price gets worse the more power
you buy at the same time). The instructions for the simulation
of the LOB, especially the interpretation of the EPEX SPOT
order book data, are presented in detail to allow repetition of
the process.
In the future, the simulation of the order book could be
used in two ways. At first, to get all information available for
traders at the moment of their order submission to simulate
and analyze their trading behavior at the intraday market. And
secondly, the LOB simulation can be used as a market model
of the intraday market to simulate intraday trading or arbitrage
of flexible energy systems in a much more realistic setting
than it is the case at the moment.
REFERENCES
[BNetzABundesnetzagentur,2017] BNetzA Bundesnetzagentur, B. (2017).
Monitoringbericht2017.
[Cesarietal.,2012] Cesari,R.,Marzo,M.,andZagaglia,P.(2012).Effective
tradeexecution.
[EPEXSPOT,2014] EPEXSPOT (2014). Epex spot trad-
ing brochure 2014. Technical report, EPEX SPOT,
https://www.epexspot.com/document/26145/EPEX
[EPEXSPOT,2017] EPEXSPOT(2017). Epexspotoperationalrules. EPEX
SPOT.
[Gouldetal.,2013] Gould,M.D.,Porter,M.A.,Williams,S.,McDonald,
M.,Fenn,D.J.,andHowison,S.D.(2013).Limitorderbooks.Quantitative
Finance,13(11):1709–1742.
[GoutteandVassilopoulos,2017] Goutte, S. and Vassilopoulos, P. (2017).
The value of flexibility in power markets. Chaire European Electricity
Markets,FondationParis-Daupine.
[HagemannandWeber,2013] Hagemann, S. and Weber, C. (2013). An
empiricalanalysisofliquidityanditsdeterminantsinthegermanintraday
marketforelectricity.
[Mitraetal.,2013] Mitra,S.,Sun,L.,andGrossmann,I.E.(2013). Optimal
schedulingofindustrialcombinedheatandpowerplantsundertime-sensitive
electricityprices. Energy,54:194–211.
[Neuhoffetal.,2016] Neuhoff,K.,Ritter,N.,Salah-Abou-El-Enien,A.,and
Vassilopoulos, P. (2016). Intraday markets for power: Discretizing the
continuoustrading? DIWdiscussionPaper.
[Reschetal.,2017] Resch, M., Bu¨hler, J., Klausen, M., and Sumper, A.
(2017). Impactofoperationstrategiesoflargescalebatterysystemson
distributiongridplanningingermany. RenewableandSustainableEnergy
Reviews,74:1042–1063.
[Ros¸u,2009] Ros¸u,I.(2009). Adynamicmodelofthelimitorderbook. The
ReviewofFinancialStudies,22(11):4601–4641.
[SianoandSarno,2016] Siano, P. and Sarno, D. (2016). Assessing the
benefitsofresidentialdemandresponseinarealtimedistributionenergy
market. AppliedEnergy,161:533–551.
[Wille-Haussmannetal.,2010] Wille-Haussmann,B.,Erge,T.,andWittwer,
C. (2010). Decentralised optimisation of cogeneration in virtual power
plants. SolarEnergy,84(4):604–611.