Multivariate Simulation-based Forecasting for Intraday Power Markets:
|     |     |     | Modelling |           | Cross-Product |     | Price | Effects       |
| --- | --- | --- | --------- | --------- | ------------- | --- | ----- | ------------- |
|     |     |     | Simon     | Hirsch1,2 |               |     |       | Florian Ziel1 |
3202 nuJ 32  ]TS.nif-q[  1v91431.6032:viXra simon.hirsch@stud.uni-due.de florian.ziel@uni-due.de
simon.hirsch@statkraft.com
1House
|     |     |     | of Energy | Markets | and        | Finance,      | University | of Duisburg-Essen |
| --- | --- | --- | --------- | ------- | ---------- | ------------- | ---------- | ----------------- |
|     |     |     |           |         | 2Statkraft | Trading       | GmbH       |                   |
|     |     |     |           |         |            | June 26, 2023 |            |                   |
Abstract
Intraday electricity markets play an increasingly important role in balancing the intermittent generation of
renewable energy resources, which creates a need for accurate probabilistic price forecasts. However, research
to date has focused on univariate approaches, while in many European intraday electricity markets all delivery
periods are traded in parallel. Thus, the dependency structure between different traded products and the
correspondingcross-producteffectscannotbeignored. Weaimtofillthisgapintheliteraturebyusingcopulas
tomodelthehigh-dimensionalintradaypricereturnvector. Wemodelthemarginaldistributionasazero-inflated
Johnson’s S U distribution with location, scale and shape parameters that depend on market and fundamental
data. The dependence structure is modelled using latent beta regression to account for the particular market
structure of the intraday electricity market, such as overlapping but independent trading sessions for different
deliverydays. Weallowthedependenceparametertobetime-varying. Wevalidateourapproachinasimulation
studyfortheGermanintradayelectricitymarketandfindthatmodellingthedependencestructureimprovesthe
forecasting performance. Additionally, we shed light on the impact of the single intraday coupling (SIDC) on
the trading activity and price distribution and interpret our results in light of the market efficiency hypothesis.
| The | approach | is directly | applicable | to  | other European | electricity | markets. |     |
| --- | -------- | ----------- | ---------- | --- | -------------- | ----------- | -------- | --- |
Keywords: Intraday Electricity Markets, Electricity Price Forecasting, Volatility Forecasting, Copula, Probabilistic
| Forecasting, | Monte-Carlo |     | Methods, | SIDC |     |     |     |     |
| ------------ | ----------- | --- | -------- | ---- | --- | --- | --- | --- |
Acknowledgements: Simon Hirsch is employed at Statkraft Trading GmbH and gratefully acknowledges support
through Statkraft (https://www.statkraft.com/). This work contains the author’s opinion and does not neces-
| sarily reflect | Statkraft’s |     | position. | The authors | declare | no conflict | of interest. |     |
| -------------- | ----------- | --- | --------- | ----------- | ------- | ----------- | ------------ | --- |
1 Introduction
Intraday electricity markets are used to balance the short-term intermittency of renewable energy assets. The
increasing penetration of wind and solar yields the need for accurate probabilistic price forecasts. This need is
1

12-02 00:00
12-02 01:00
12-02 02:00
12-02 03:00
12-02 04:00
12-02 05:00
12-02 06:00
12-02 07:00
12-02 08:00
12-02 09:00
12-02 10:00
12-02 11:00
12-02 12:00
12-02 13:00
12-02 14:00
12-02 15:00
12-02 16:00
12-02 17:00
12-02 18:00
12-02 19:00
12-02 20:00
12-02 21:00
12-02 22:00
12-02 23:00
12-01 16 12-01 20 12-02 00 12-02 04 12-02 08 12-02 12 12-02 16 12-02 20 12-03 00
Trading Time
ruoH
yrevileD
Intraday Trades on the Germany Market by Delivery Hour
500
Trade Volume [MW]
10 40 70 90
20 50 80 100
30 60
450
400
350
300
250
200
]hWM/RUE[
ecirP
Figure 1: All trades for delivery on 2022-12-02 on the German continuous intraday market by delivery period and
trading time. Trading for all delivery periods opens on 2022-12-01 at 15:00 hours. Each dot represents one trade.
The size of the dots corresponds to the size of individual trades in MW. The color reflects the transacted price in
EUR/MWh. The correlated behaviour of neighbouring trading periods is clearly visible.
underscored by the heightened volatility in light of the European energy crisis in 2022/23. To date, the literature
on (probabilistic) electricity price forecasting on intraday markets remains scarce [33, 20, 48, 32] and is exclusively
focusedonunivariateapproaches. However,inmostEuropeancountries,theintradaymarketisacontinuousforward
market, wherealldeliveryperiodsforadeliverydaydaretradedinparallel, thusunivariateapproachesneglectthe
complex dependency structurein these markets. Asproducts closewith thephysical delivery ofelectricity, it isnot
possible to “glue” subsequent trading sessions together, as it is commonly done with equity markets. Additionally,
while the spot market is driven by the absolute level of fundamentals such as wind and solar production, the
intraday prices are influenced more by the changes in forecasts [50]. Our work focuses on these challenges in
modelling the dependency structure and fills the according gap in the literature. Based on the work of [33, 20] on
the marginal distribution of the price process, we employ copulas to model the time-dependent correlation. We
model the dependency parameter as latent variable using beta regression. We validate our results in a forecasting
study for the German intraday electricity market. Our results indicate that modelling the dependence structure
between the different trading session improves the forecasting performance. Additionally, we provide evidence on
market efficiency in the German short-term market. Our fundamental and parametric approach allows us to shed
further light on the impact of the cross-border shared order books of the single intraday coupling (SIDC) and the
driving factors of the distribution parameters.
Let us give an illustrative example for the trading schedule of the German intraday electricity market. Trading for
physical delivery on d starts on the previous day d 1, 15:00 hours and lasts till few minutes before the start of
−
physical delivery of electricity. For example, trading for the delivery on d, 18:00-19:00 started on d 1 at 15:00
−
hoursandclosesatd,17:55hours. Duringthebeginningofthistradingwindow,traderswillbeabletotradepower
2

in many neighbouring delivery hours, from delivery at d 16:00-17:00 (which closes at d 1 15:55), to all delivery
−
periods for the next delivery day d+1 (which start trading at d, 15:00 hours). Figure 1 shows all trades in the two
trading sessions for delivery on 2022-12-01 and 2022-12-02 for all hourly products on the German intraday market.
Theliteratureonintradayelectricitypriceforecastingcanbedividedintothreemaingroups: (1)paperwhichtreat
theintradaymarketinasimilarfashionastheday-aheadmarketandpredict(index)pricesalongthedeliverytime
line [48, 9, 23] and (2) paper which predict prices along the trading time for single delivery periods [42, 20, 32, 33,
21, 30]. The correlation between different trading windows has, to the best knowledge of the authors, not been
investigated so far, while the correlation between day-ahead and intraday (index) prices has been the subject of
studies such as [3, 9]. Lastly, (3), empirical, in-sample studies on price formation in intraday electricity markets
have been conducted by [24, 25, 22].
In light of the aforementioned challenges and the gap identified in the literature, our contributions are:
• We develop a global model for the marginal distribution of intraday electricity prices in the German market
and extend previous work from [33, 20] by taking the whole trading window into account.
• As novelty, we analyse the correlation and dependence structure in the German intraday electricity market
and develop a multivariate, probabilistic forecasting model for the German intraday electricity markets to
take cross-product effects into account.
• We validate our approach in an extensive simulation study for the German intraday electricity market.
• Using a parametric approach, our methods and models shed light on the driving variables such as trading
activity and renewable forecasts in the intraday market, but also on the impact of the market structure and
SIDC.
Ourmainstrategyisthecanonicalinference-for-margins[37]approachcommonlyusedforcopulamodellingandcan
be summarized as follows: We use the probabilistic models developed by [33, 20] as a starting point to gaussianize
the intraday market observations. We use the pseudo-Gaussian observations to fit the dependency structure. For
forecasting, we simulate (multivariate) Gaussian random variates and use the inverse probability integral trans-
formation to receive samples in the desired marginal distribution. Within the energy markets literature, similar
approaches have been used for simulating wind and load forecast deviations [47, 7, 8], day-ahead electricity prices
[see e.g. 28, 39, 5] and the design of hedging strategies [40]. Our results show that modelling the dependence
structure leads to significantly improved forecasting performance compared to univariate approaches. However,
we find that time-dependent modelling of the dependence structure is of little added value compared to constant
dependence. Additionally,weprovidenewinsightontheeffectsoftheopeningandclosingofthecross-borderorder
books during SIDC. We interpret our results in light of the market efficiency hypothesis and discuss reflections
on modelling already highly volatile prices during a period of increased uncertainty. Figure 2 gives an illustrative
example of our 24-dimensional forecast
Our results offer multiple avenues for further research. First, we restrict ourselves to Gaussian dependence struc-
tures. Future work might improve our methods by using copulas that reflect possible tail dependence effects or use
Vine-copulas to better approximate the dependence structure. Secondly, we note that the zero-inflated Johnson’s
S distribution offers a good, but not yet perfect fit for the marginal distribution in the intraday market and
U
hence further research in the marginal distribution of intraday electricity prices is required. Third, in light of the
continued development of SIDC and the planned introduction of intraday auctions within the SIDC system and
the possible integration of interconnector cables in the SIDC system [14], our results on the impact of SIDC on the
trading activity provide a fruitful starting point for further research [for an early work on the topic see 22].
What is more, our results are also relevant for researchers and practitioners working on stochastic optimization
3

120
100
80
60
40
20
0
20
40
0 2 4 6 8 10 12 14 16 18 20 22
Delivery hour h
]hWM/RUE[
ecirP
Spot Prices Simulations for the Intraday Market
Delivery hour h
0 4 8 12 16 20
1 5 9 13 17 21
2 6 10 14 18 22
3 7 11 15 19 23
0 4 8 12 16 20 24 28 32 36 40 44 48 52 56 60 64 68 72 76 80 84 88 92 96100104108112116120124128
Trading Time t
Figure 2: One exemplary simulation for all delivery hours of 2022-01-02. All simulations start at the day-ahead
spot price and develop correlated along the trading time t.
of bidding strategies for the intraday markets. For storage assets such as batteries and pumped-hydro, modelling
the dependency structure is important as charging (pumping) positions some periods depends on the ability to
discharge (generate) later during the day and therefore depends on the dependency structure. Recent works as
[6, 35, 17] use sampled paths for the intraday market, but model the dependency structure only implicitly, if at all,
and thus might produce too optimistic results.
The remainder of this paper is structured as follows: the following Section 2 gives a detailed introduction to the
German short-term electricity market. Section 3 introduces our data set, preparation and summary statistics. We
present our modelling approach in Section 4. Section 5 describes the forecasting study design and scoring rules.
Finally, Section 6 and 7 present and discuss our results and conclude this paper.
2 Market Description
Electricity markets are structured as forward markets. The German short-term electricity market consists of three
major parts: (1) the daily spot auction, (2) the continuous intraday market and (3) the balancing market. The
following discussion focuses on the spot and intraday markets. The spot market is the main electricity market in
Germany. It is organized as a daily auction at noon on which electricity for all 24 delivery hours on the following
day is traded. The following intraday market is used to balance deviations in forecasts after the day-ahead market.
It is organized as continuous trading similar to equity markets. The continuous trading starts at d 1, 15:00 hours
−
andclosesshortlybeforedelivery. Afterthedeliveryperiodends,remainingimbalancesbetweenthetradedposition
and the actual production are settled in the balancing market with the TSO. However, strict market regulation in
Germany prohibit explicit active position taking in the balancing market. Figure 3 depicts the daily procedure for
a single delivery hour.
Letusintroducesomenomenclaturetoeasethefollowingdiscussionofthemarketstructureofthespotandintraday
market. We refer to the delivery time as the time of actual production power, while the trading time refers to the
time at which a trade for a certain delivery period is conducted. As a general rule, we try to denote delivery time
in superscript, while we denote trading time in subscript. We refer to a trading session on the intraday market as
4

|     | Day-ahead |     |     | Intraday | 1stWave | 2ndWave |     |     |     |
| --- | --------- | --- | --- | -------- | ------- | ------- | --- | --- | --- |
SIDC
|     | SpotAuction |     | Marketopens |     | SIDCopens | SIDCopens |     | closes | Delivery |
| --- | ----------- | --- | ----------- | --- | --------- | --------- | --- | ------ | -------- |
Market
closes
Controlzones
close
|     |     | d−1,  |     | d−1,  | d−1,  | d−1,  |     | d, d,     | d, d,h |
| --- | --- | ----- | --- | ----- | ----- | ----- | --- | --------- | ------ |
|     |     | 12.00 |     | 15.00 | 18.00 | 22.00 |     | h−60 h−30 | h−5    |
|     |     |       |     |       |       |       |     | min min   | min    |
Figure 3: Daily procedure in the German short-term power markets [based on 15]. Note that the figure abstracts
| from half-hourly |     | and quarter-hourly |     |     | delivery periods. |     |     |     |     |
| ---------------- | --- | ------------------ | --- | --- | ----------------- | --- | --- | --- | --- |
the time window between market opening on d 1, 15:00 hours to gate closure. Note that for different delivery
−
| periods, | trading | sessions | are | of different | length. |     |     |     |     |
| -------- | ------- | -------- | --- | ------------ | ------- | --- | --- | --- | --- |
The spot market in Germany is organized by EPEX Spot and Nordpool AS with shared order books. On the spot
market, electricity for all 24 hours for the following day is traded. The market is organized as a pay-as-cleared
auction and its order book closes at d 1, 12:00 hours. Results are published at d 1, 12:42 hours. The minimum
|     |     |     |     |     | −   |     |     | −   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
price is currently set to -500 EUR/MWh and the maximum price is set to 3000 EUR/MWh.
| d   | 1 , 1 2 : 00 | d 1 , 1 5 :0 0 |     |     |     |     | d , 1 2 : 0 0 | d, 15 :0 0 |     |
| --- | ------------ | -------------- | --- | --- | --- | --- | ------------- | ---------- | --- |
Sp ot−a u c ti o n for Sta rt−o f i n tr a day d,00:00 Spot a u c t i o nfor Start of in t raday d+1,00:00
deliveryond tradingford Beginofdayd deliveryond+1 tradingford+1 Beginofdayd+1
|     | Deliveryond | 1forspotauctionatd |     | 2   |     |                              |     |     |     |
| --- | ----------- | ------------------ | --- | --- | --- | ---------------------------- | --- | --- | --- |
|     |             | −                  |     | −   |     |                              |     |     |     |
|     |             |                    |     |     |     | Deliveryondforspotauctionatd |     | 1   |     |
−
Spot
Intraday
|     | Tradingsessionfordeliveryond |     | 1,h=22 |     |     |     |     |     |     |
| --- | ---------------------------- | --- | ------ | --- | --- | --- | --- | --- | --- |
−
|     | Tradingsessionfordeliveryond |     | 1,h=23 |     |     |     |     |     |     |
| --- | ---------------------------- | --- | ------ | --- | --- | --- | --- | --- | --- |
−
Tradingsessionfordeliveryond,h=0
Tradingsessionfordeliveryond,h=1
Tradingsessionfordeliveryond,h=15
Tradingsessionfordeliveryond,h=23
Tradingsessionfordeliveryond+1,h=0
Tradingsessionfordeliveryond+1,h=1
Tradingsessionfordeliveryond+1,h=2
Tradingsessionfordeliveryond+1,h=3
Figure4: Scheduleoftheday-aheadspotandthecontinuousintradaymarketincomparison. Whitecirclesindicate
the order book closing of the day-ahead auctions. White boxes indicate trading sessions for different delivery
periods. Filled boxes indicate delivery periods. Own figure based on the schedules given in [15]. Note that we have
| omitted | trading | windows | during | days | to save space. |     |     |     |     |
| ------- | ------- | ------- | ------ | ---- | -------------- | --- | --- | --- | --- |
The intraday market is structured as continuous forward market. For all hourly delivery periods with delivery on
d, trading starts at d 1, 15:00 hours and ends 5 minutes before the actual start of delivery. Within the Single
−
Intraday Coupling (SIDC), the order books of all major continuous intraday markets across Europe are coupled, as
long as there is sufficient cross-border transmission capacity. The coupling proceeds in two waves: first, at d 1,
−
5

40
30
20
10
0
10
20
12-31 16 12-31 18 12-31 20 12-31 22 01-01 00 01-01 02 01-01 04 01-01 06 01-01 08 01-01 10 01-01 12
Trading time t
]hWM/RUE[
ecirP
noitcasnarT
Raw transaction data for delivery period 2020-01-01 12:00
0 2 4 6 8 10
Transaction Volume [MW]
40
30
20
10
0
10
20
12-31 16 12-31 18 12-31 20 12-31 22 01-01 00 01-01 02 01-01 04 01-01 06 01-01 08 01-01 10 01-01 12
Trading time t
]hWM/RUE[
ecirP
noitcasnarT
Aggregated transaction data for delivery period 2020-01-01 12:00
Aggregated Price Ptd,h Price changes Ptd,h No-Trade Dummy td,h
Figure 5: Data aggregation process. The top panel shows the raw transaction data. The lower panel shows the
volume weighted 15-minute price path Pd,h (red line) and the price differences ∆Pd,h (blue line). The background
t t
shading indicates the Boolean variable αd,h, where red denotes no trades. The trading periods until the first trade
t
are filled with Pd,h . Own figure.
Spot
18:00hours,theorderbooksofGermany,Denmark,Sweden,PolandandNorwayandNetherlands1 arecoupled. At
d 1, 22:00, France, Netherlands, Belgium, Austria, the Czech Republic, Hungary, Romania follow [34]. All shared
−
orderbooksclose60minutesbeforethestartofphysicaldeliveryandtradingresumeswithGermanywidedelivery.
30 minutes before the start of physical delivery, the Germany wide delivery and trading resumes on a TSO/grid
zone-level. Finally, 5 minutes before delivery, the grid-zone trading closes as well. Note that all hourly (and also
half-hourly and quarter-hourly) delivery periods for a delivery day d are traded in parallel, as it shown in Figure 4.
A more detailed overview on intraday electricity markets can be found in [43] and [49].
3 Data
The following chapter gives a brief introduction of the data used in this paper and the required pre-processing.
We use intraday transaction data from EPEX, the anonymous day-ahead spot auction bid curves from EPEX, and
wind, solar and demand forecasts from SMARD respectively ENTSO-E. We also provide summary statistics. As
a rule of thumb, superscript indices denote delivery periods while subscript indices denote trading time. We hope
this makes the forward market structure of the short-term electricity markets more clear.
Intraday transactions are individual trades conducted on the continuous intraday market. We use only trades
conducted with either the buy- or sell leg in one of the 4 German grid zones. As trading happens continuously in
theintradaymarket,transactionsareirregularspacedintimeandneedtobeaggregated. Inlinewith[20,33,32,42],
weaggregatealltradesfordeliveryperiodd,hona15-minuteequidistantgridalongthetradingtime(denotedwith
1NorwayandNetherlandsarecoupledthroughtheNorNedhigh-voltagesubmarinecable. WithinthecentralEuropeanCoreregion,
theNetherlandsiscoupledtothegeographicneighboursat22:00hours.
6

Pd,h
t), where t=0 denotes the first 15 minutes after trading start. Let t denote the volume-weighted average price
of all trades with delivery period d,h belonging to bucket t and αd,h denote a Boolean indicator whether there was
t
ThespotpriceforeachdeliveryperiodisdenoteasPd,h
| atleastonetrade. |     |     |     |     |     |     |     |     |     | .   | Wedropalltradesinthelocaltrading |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- |
Spot
phase in the last 30 minutes to the start of physical delivery. The full aggregation process can be seen in Figure
5. Summary statistics for the price differences are given in Table 1. We especially note an increasing volatility in
year 2022 driven by the Russian invasion in Ukraine and the energy crisis in Europe. Additionally, we note that
tradingactivityingeneralincreasesastheshareofno-tradeeventdecreases. Figure6givesthepairwisecorrelation
between price changes for all 24 24 intraday delivery periods during the training set. We already note a cluster
×
| of high correlation |        | for  | the night | hours  | and  | for the | afternoon | peak           | hours.         |                |                          |                     |                          |
| ------------------- | ------ | ---- | --------- | ------ | ---- | ------- | --------- | -------------- | -------------- | -------------- | ------------------------ | ------------------- | ------------------------ |
|                     |        |      |           |        |      |         | 0         | 0.43 0.33 0.26 | 0.22 0.17 0.12 | 0.09 0.08 0.06 | 0.05 0.04 0.04 0.04 0.02 | 0.03 0.02 0.03 0.03 | 0.02 0.03 0.04 0.02 0.02 |
|                     |        |      |           |        |      |         | 1 0.43    | 0.46 0.36      | 0.27 0.21 0.15 | 0.1 0.09 0.06  | 0.05 0.05 0.04 0.04 0.03 | 0.04 0.03 0.02 0.03 | 0.03 0.03 0.03 0.02 0.03 |
|                     |        |      |           |        |      |         | 2 0.33    | 0.46 0.48      | 0.37 0.26 0.17 | 0.12 0.09 0.07 | 0.06 0.04 0.04 0.04 0.04 | 0.03 0.03 0.02 0.03 | 0.03 0.04 0.04 0.02 0.02 |
|                     |        |      |           |        |      |         | 3 0.26    | 0.36 0.48      | 0.45 0.31 0.2  | 0.14 0.1 0.07  | 0.05 0.06 0.05 0.04 0.04 | 0.04 0.04 0.03 0.03 | 0.03 0.03 0.02 0.02 0.02 |
|                     |        |      |           |        |      |         | 4 0.22    | 0.27 0.37 0.45 | 0.38 0.23      | 0.16 0.12 0.08 | 0.06 0.07 0.04 0.04 0.04 | 0.04 0.03 0.03 0.03 | 0.03 0.02 0.02 0.01 0.03 |
|                     |        | 2020 | 2021      |        | 2022 |         |           |                |                |                |                          |                     |                          |
|                     |        |      |           |        |      |         | 5 0.17    | 0.21 0.26 0.31 | 0.38 0.31      | 0.2 0.15 0.1   | 0.08 0.07 0.05 0.05 0.05 | 0.04 0.03 0.03 0.03 | 0.03 0.03 0.04 0.04 0.02 |
|                     |        |      |           |        |      |         | 6 0.12    | 0.15 0.17 0.2  | 0.23 0.31      | 0.34 0.23 0.15 | 0.13 0.09 0.08 0.05 0.05 | 0.05 0.04 0.05 0.05 | 0.05 0.05 0.03 0.04 0.02 |
| Count               | 445184 |      | 480948    | 505673 |      |         |           |                |                |                |                          |                     |                          |
|                     |        |      |           |        |      |         | 7 0.09    | 0.1 0.12 0.14  | 0.16 0.2 0.34  | 0.35 0.23      | 0.16 0.13 0.1 0.08 0.06  | 0.07 0.06 0.05 0.06 | 0.04 0.06 0.04 0.03 0.01 |
| Mean                |        | 0.03 | 0.16      |        | 0.13 |         |           |                |                |                |                          |                     |                          |
|                     |        |      |           |        |      |         | 8 0.08    | 0.09 0.09 0.1  | 0.12 0.15 0.23 | 0.35 0.33      | 0.22 0.18 0.14 0.11 0.09 | 0.09 0.06 0.07 0.06 | 0.05 0.05 0.04 0.04 0.02 |
Std 4.33 6.46 13.12 9 0.06 0.06 0.07 0.07 0.08 0.1 0.15 0.23 0.33 0.33 0.25 0.19 0.14 0.13 0.12 0.09 0.09 0.07 0.07 0.05 0.04 0.04 0.03
MAD 0.62 1.03 2.51 01 0.05 0.05 0.06 0.05 0.06 0.08 0.13 0.16 0.22 0.33 0.36 0.26 0.2 0.16 0.15 0.12 0.1 0.08 0.06 0.06 0.05 0.04 0.03
ruoH yrevileD 11
IQR 1.24 2.06 5.02 0.04 0.05 0.04 0.06 0.07 0.07 0.09 0.13 0.18 0.25 0.36 0.35 0.26 0.22 0.18 0.14 0.11 0.09 0.07 0.06 0.05 0.05 0.03
21
|      |         |       |         |          |       |     | 0.04    | 0.04 0.04 0.05 | 0.04 0.05 0.08 | 0.1 0.14 0.19  | 0.26 0.35 0.36 0.28      | 0.22 0.17 0.12 0.09 | 0.06 0.05 0.05 0.05 0.03 |
| ---- | ------- | ----- | ------- | -------- | ----- | --- | ------- | -------------- | -------------- | -------------- | ------------------------ | ------------------- | ------------------------ |
| Min  | -999.35 |       | -523.97 | -1600.27 |       |     | 31      |                |                |                |                          |                     |                          |
|      |         |       |         |          |       |     | 0.04    | 0.04 0.04 0.04 | 0.04 0.05 0.05 | 0.08 0.11 0.14 | 0.2 0.26 0.36 0.37       | 0.28 0.21 0.14 0.1  | 0.08 0.07 0.06 0.05 0.04 |
| Q5%  |         | -3.06 | -5.61   | -11.70   |       |     | 41      |                |                |                |                          |                     |                          |
|      |         |       |         |          |       |     | 0.02    | 0.03 0.04 0.04 | 0.04 0.05 0.05 | 0.06 0.09 0.13 | 0.16 0.22 0.28 0.37      | 0.35 0.25 0.15 0.11 | 0.09 0.07 0.05 0.06 0.04 |
| Q10% |         | -1.75 | -3.06   |          | -6.89 |     | 51      |                |                |                |                          |                     |                          |
|      |         |       |         |          |       |     | 0.03    | 0.04 0.03 0.04 | 0.04 0.04 0.05 | 0.07 0.09 0.12 | 0.15 0.18 0.22 0.28 0.35 | 0.32 0.19 0.13      | 0.11 0.09 0.06 0.07 0.05 |
|      |         |       |         |          |       |     | 61 0.02 | 0.03 0.03 0.04 | 0.03 0.03 0.04 | 0.06 0.06 0.09 | 0.12 0.14 0.17 0.21 0.25 | 0.32 0.25 0.17      | 0.13 0.1 0.08 0.07 0.06  |
| Q25% |         | -0.62 | -1.00   |          | -2.50 |     |         |                |                |                |                          |                     |                          |
|      |         |       |         |          |       |     | 71 0.03 | 0.02 0.02 0.03 | 0.03 0.03 0.05 | 0.05 0.07 0.09 | 0.1 0.11 0.12 0.14 0.15  | 0.19 0.25 0.27      | 0.18 0.14 0.11 0.09 0.06 |
| Q50% |         | 0     |         | 0        | 0     |     |         |                |                |                |                          |                     |                          |
|      |         |       |         |          |       |     | 81 0.03 | 0.03 0.03 0.03 | 0.03 0.03 0.05 | 0.06 0.06 0.07 | 0.08 0.09 0.09 0.1 0.11  | 0.13 0.17 0.27      | 0.29 0.2 0.16 0.12 0.09  |
Q75% 0.63 1.06 2.52 91 0.02 0.03 0.03 0.03 0.03 0.03 0.05 0.04 0.05 0.07 0.06 0.07 0.06 0.08 0.09 0.11 0.13 0.18 0.29 0.27 0.19 0.16 0.1
Q90% 1.75 3.25 6.87 02 0.03 0.03 0.04 0.03 0.02 0.03 0.05 0.06 0.05 0.05 0.06 0.06 0.05 0.07 0.07 0.09 0.1 0.14 0.2 0.27 0.27 0.2 0.13
Q95% 3.06 6.12 11.71 12 0.04 0.03 0.04 0.02 0.02 0.04 0.03 0.04 0.04 0.04 0.05 0.05 0.05 0.06 0.05 0.06 0.08 0.11 0.16 0.19 0.27 0.28 0.18
|     |         |     |        |         |     |     | 22 0.02 | 0.02 0.02 0.02 | 0.01 0.04 0.04 | 0.03 0.04 0.04 | 0.04 0.05 0.05 0.05 0.06 | 0.07 0.07 0.09 0.12 | 0.16 0.2 0.28 0.23 |
| --- | ------- | --- | ------ | ------- | --- | --- | ------- | -------------- | -------------- | -------------- | ------------------------ | ------------------- | ------------------ |
| Max | 1007.97 |     | 735.88 | 2356.06 |     |     |         |                |                |                |                          |                     |                    |
|     |         |     |        |         |     |     | 32 0.02 | 0.03 0.02 0.02 | 0.03 0.02 0.02 | 0.01 0.02 0.03 | 0.03 0.03 0.03 0.04 0.04 | 0.05 0.06 0.06 0.09 | 0.1 0.13 0.18 0.23 |
|     |         |     |        |         |     |     | 0       | 1 2 3          | 4 5 6          | 7 8 9          | 10 11 12 13 14           | 15 16 17 18         | 19 20 21 22 23     |
Delivery Hour
| Table 1: | Summary |     | Statistics |     | for | all |     |     |     |     |     |     |     |
| -------- | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∆Pd,h αd,h
|                 | =1.       | MAD |     | denotes     | the | me-    |        |            |     |              |                        |             |                |
| --------------- | --------- | --- | --- | ----------- | --- | ------ | ------ | ---------- | --- | ------------ | ---------------------- | ----------- | -------------- |
| t               | t         |     |     |             |     |        | 0.5    | 0.4        | 0.3 | 0.2 0.1      | 0.0 0.1                | 0.2 0.3     | 0.4 0.5        |
| dian absolute | | deviation |     | and | IQR denotes |     | the    |        |            |     |              | Dependece              |             |                |
| interquartile   | range.    |     |     |             |     |        |        |            |     |              |                        |             |                |
|                 |           |     |     |             |     | Figure | 6:     | Dependence |     | matrix       | for the 24-dimensional |             | intraday price |
|                 |           |     |     |             |     | change | vector | ∆Pd,h.     |     | We calculate | pairwise               | correlation | to account     |
t
|     |     |     |     |     |     | for | the different | trading |     | window | lengths. |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------- | --- | ------ | -------- | --- | --- |
We use wind on- and offshore, solar and demand forecasts from ENTSO-E. The data is aggregated to hourly
resolution using a simple arithmetic average. Forecasts are generated by the transmission system operator for each
deliveryperiodd,handavailableattheday-aheadstage,i.e. latestatd 1,12:00o’clock. Wedenotetheforecastsas
−
WindOnd,h,WindOffd,h,Solard,h andLoadd,h. Foralldata,weadjustth edaylightsavingtimesby(back-)fillingthe
missinghourinspringandaveragingthedoublehourinautumnasitisstandardintheelectricitypriceforecasting
literature.
7

35
30
25
20
15
10
5
0
]WG[
raloS
Training Data Validation Data Test Data
7
6
5
4
3
2
1
0
]WG[
erohsffO
40
35
30
25
20
15
10
5
0
]WG[
erohsnO
75
70
65
60
55
50
45
40
35
30
2020-01-01 2020-04-01 2020-07-01 2020-10-01 2021-01-01 2021-04-01 2021-07-01 2021-10-01 2022-01-01 2022-04-01 2022-07-01 2022-10-01 2023-01-01
Date
]WG[
daoL
Figure 7: Solar, wind on- and offshore and load day-ahead forecasts from ENTSO-E/SMARD. The initial training
data set consists of the first 1.5 years. The subsequent half year is used as validation data set for tuning hyperpa-
rameters and model selection. We evaluate our results on the final year of data.
8

Auction Supply/Demand Curves Transformed Auction Supply/Demand Curves Calculation of Merit Order Regime Slope
| 1000 |     |     | 1000 | 300 |     |
| ---- | --- | --- | ---- | --- | --- |
Sell / Supply Bids Transformed Supply Bids Transformed Supply Bids
|     |     | Buy / Demand Bids | Inelastic Demand  |     | Inelastic Demand |
| --- | --- | ----------------- | ----------------- | --- | ---------------- |
|     |     | Equilibrium Price | Equilibrium Price | 250 | Slope            |
| 800 |     |                   | 800               |     | Shifted Demands  |
Equilibrium Price
200
| 600 |     |     | 600 |     |     |
| --- | --- | --- | --- | --- | --- |
150
| ]hWM/RUE[ ecirP |     |     | ]hWM/RUE[ ecirP | ]hWM/RUE[ ecirP |     |
| --------------- | --- | --- | --------------- | --------------- | --- |
| 400             |     |     | 400             | 100             |     |
50
| 200 |     |     | 200 |     |     |
| --- | --- | --- | --- | --- | --- |
0
| 0   |     |     | 0   |     |     |
| --- | --- | --- | --- | --- | --- |
50
200 20 22 24 26 28 30 32 34 36 38 200 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 100 30 32 34 36 38 40 42 44 46
Cumulative Bid Volume [GW] Cumulative Bid Volume [GW] Cumulative Bid Volume [GW]
Figure 8: Calculation of the merit-order regime coefficient MOd,h. The first panel shows the anonymous supply
and demand bids for delivery day 2020-01-01 13:00. The second panel shows the transformed auctions curves. The
thirdpanelshowsthecalculationoftheslopecoefficient(green)aroundtheequilibriumprice. Notethatwezoomed
| x and y-axes | for the third | panel. |     |     |     |
| ------------ | ------------- | ------ | --- | --- | --- |
Additionally,weemployametricforthemerit-orderregime. Intheclassicalmodel,themerit-orderisdefinedasthe
supply side of the electricity market, sorted by the marginal production costs. The intersection of the supply and
demand curve gives the market price. Depending on the slope of the merit-order, changes in the supply or demand
have different impacts on the market price. [25] and [20] have shown that the different merit-order regimes explain
the size and volatility of price changes in the intraday markets. However, modelling the merit-order in short-term
power markets is not straight forward and several approaches have proposed. We follow the approach of [20] by
using anonymous bid and offer curves from the day-ahead market to model the intraday merit order. The curves
are published by EPEX Spot around 14:30 and are therefore available at the time of forecasting.
Theoverviewofthestrategyforthecalculationofthemerit-orderregimecoefficientMOd,h isgiveninFigure8. We
take the anonymous supply and demand curves from the auction and transform these into an elastic supply curve
and an inelastic demand curve using the same transformation as in [20, 26]. This transformation is based on the
idea that buying 50 MW up to a price of 100 EUR/MWh is the same as buying 50 MW at any price and placing a
sell order at 100.01 EUR/MWh. Intuitively, we can therefore create a price independent buy curve and move the
price-dependent bids to the sell side. The resulting demand and supply curves are depicted in the middle panel
of Figure 8. Note that the equilibrium price at the intersection between supply and demand curve is unchanged.
Lastly, we calculate the slope around the equilibrium price as finite difference quotient. For the exact calculation,
| we refer the | reader to | [20]. |     |     |     |
| ------------ | --------- | ----- | --- | --- | --- |
4 Models
Our approach follows the widely used inference for margins approach for copula models. We first use a univariate
model to estimate the time-varying conditional marginal distribution, apply the probability integral transform and
estimatethecopuladistributionrespectivelythetime-varyingdependenceparameterinthesecondstep. Thefollow-
ing two subsections 4.1 and 4.2 describe our modelling in more detail. Section 4.3 describes the general simulation
set-up. Subsection 4.4 describes the different (nested) models for our forecasting study and our benchmark models.
9

Letusremarkthatstrictly,Sklar’stheorem[44]isonlyvalidforcontinuous marginaldistributions,as (X)
X [0,1]
F ∼U
is not true for discrete distributions . This leads to the issue that the copula distribution is not necessarily
F
identifiable with discrete or mixed discrete-continuous marginals. A practical approach to alleviate this issue is to
fill the gaps induced through the discreteness of the marginal distribution by some uniform ’jitters’, which results
in the so-called checkerboard copula, a strategy we employ in this paper as well [18, 16].
4.1 Marginal Model for Electricity Prices
Wemodelthedistributionofthepricechanges∆Pd,h asamixturedistribution d,h toaccountforthezero-inflation
t Dt
in price changes.
∆Pd,h d,h (1)
t ∼Dt
where d,h is a mixture distribution from a continuous distribution and the Dirac distribution with an atom at 0,
Dt
denoted as δ .
0
=(1 αd,h)δ +αd,h d,h (2)
D − t 0 t ·Ft
where αd,h =1 indicates a trade event and is modelled as an binomial variable αd,h d,h(πd,h).
t t ∼Bt t
A similar approach is taken by [33, 20], who estimate the mixture distribution in a two-stage procedure. Owing
to stylized facts on intraday electricity prices, [33, 20] assume to follow the (skewed) Student-t or Johnson’s S
U
F
distribution. With regards to [20] remarks on the issues with estimation stability using the skew t-distribution, we
generally use Johnson’s S distribution in this work. We use a two-step estimation procedure for the estimation.
U
First, we estimate the conditional mixing probability πd,h using regularized logistic regression. Subsequently, we
t
estimate the conditional distribution parameters on all non-zero price changes ∆Pd,h αd,h = 1 using maximum
t | t
likelihood. The remainder of this section describes our feature engineering, the exact specifications for our models
for the conditional mixing probabilities and the conditional distribution parameters as well as our hyperparameter
tuning scheme.2
Our predictive variables can be grouped into five groups:
1. Fundamental forecasts. We use the day-ahead forecasts for the solar, wind on- and offshore production, the
day-aheadloadforecastandameasurefortheslopeofthemerit-ordertoaccountfordifferentmarketregimes.
2. Time derived dummies. We use dummies for the hour-of-the-day, denoted as HOUR(d,h,t) and day-of-the-
week, denoted as DOW(d,h,t).
3. Market structure dummies. We use dummies to distinguish the periods at which the SIDC pan-European
order books open and close. The 1st wave opens at 18:00 hours, the 2nd wave opens at 22:00 hours and the
order books close 1 hour before the physical delivery. We use an additional dummy to mark the phase where
the pan-European order books are open.
4. Trading time splines. We use ReLU splines to model non-linear effects of the trading time t and the time to
delivery T t.
−
2We have also experimented with estimating the zero-inflation in a single estimation step. However, there are two kinds of zero-
inflationpresentintheintradaytradedata: Wehaveperiodswithouttradesandperiodswheretradinghappens,butthetradingdoes
notleadtoachangeintheprice. Ajointestimationdoesnotdifferentiatebetweenbotheffectsandprovidedinferiorresultsininitial
testing. Additionally, theestimation ofdiscrete-continuous mixturedistributions isnot straight-forward usingmaximum-likelihood as
theprobabilitymassandlikelihoodfunctionsliveondifferentscales.
10

Empiricial mixing probability t Fitted ReLU(t) Splines and SIDC-dummies for the conditional mixing probability t
| 1.0 |     |     |     |     |     |                 |     | 1.0 |     |     |     |                 |     |
| --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --------------- | --- |
|     |     |     |     |     |     | Delivery Hour h |     |     |     |     |     | Delivery Hour h |     |
| 0.9 |     |     |     |     | 0   | 9 18            |     | 0.9 |     |     | 0 5 | 10 14 18        | 22  |
|     |     |     |     |     | 1   | 10 19           |     |     |     |     | 1 6 | 11 15 19        | 23  |
stneve edart-on fo ytilibaborp dettiF 0.8 2 11 20 stneve edart-on fo ytilibaborp dettiF 0.8 2 7 12 16 20 1st SIDC Wave Opens
|     |     |     |     |     | 3   | 12 21                    |     |     |     |     | 3 8 | 13 17 21 | 2nd SIDC Wave Opens |
| --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | -------- | ------------------- |
| 0.7 |     |     |     |     | 4   | 13 22                    |     | 0.7 |     |     | 4 9 |          |                     |
|     |     |     |     |     | 5   | 1 4 2 3                  |     |     |     |     |     |          |                     |
| 0.6 |     |     |     |     | 6   | 1 5 1 st SIDC Wave Opens |     | 0.6 |     |     |     |          |                     |
| 0.5 |     |     |     |     | 7   | 1 6 2nd SIDC Wave Opens  |     | 0.5 |     |     |     |          |                     |
|     |     |     |     |     | 8   | 1 7                      |     |     |     |     |     |          |                     |
| 0.4 |     |     |     |     |     |                          |     | 0.4 |     |     |     |          |                     |
| 0.3 |     |     |     |     |     |                          |     | 0.3 |     |     |     |          |                     |
| 0.2 |     |     |     |     |     |                          |     | 0.2 |     |     |     |          |                     |
| 0.1 |     |     |     |     |     |                          |     | 0.1 |     |     |     |          |                     |
| 0.0 |     |     |     |     |     |                          |     | 0.0 |     |     |     |          |                     |
1.0 3.5 6.0 8.5 11.0 13.5 16.0 18.5 21.0 23.5 26.0 28.5 31.0 1.0 3.5 6.0 8.5 11.0 13.5 16.0 18.5 21.0 23.5 26.0 28.5 31.0
|     |     |     | Trading Time (Hours) |     |     |     |     |     |     |     | Trading Time (Hours) |     |     |
| --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- |
Figure 9: Empirical mixing probabilities α and the fitted conditional mixing probabilities using a ReLU spline for
t
the trading time t. Note that in the logistic regression model specified in Equation 4, all variables apart from the
ReLU spline and the SIDC dummies are constant across t, but vary only along d and s.
5. Trading variables. We use first three lagged prices, absolute lagged prices and the first three lagged values of
α t to account for the auto-regressive nature in the distribution parameters. We also use a spline for the level
|     | of the | spot price, | denoted | as  | ReLU(Pd,h | ).  |     |     |     |     |     |     |     |
| --- | ------ | ----------- | ------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Spot
ReLU splines are piecewise linear approximations on the domain of an explanatory variable. For an arbitrary
explanatory variable x we define a set of thresholds τ and we define the ReLU splines as
x
∈T
(cid:88)
|     |     |     |     |     | ReLU(x, | x )= |     | β τ,x min(x,τ) |     |     |     |     | (3) |
| --- | --- | --- | --- | --- | ------- | ---- | --- | -------------- | --- | --- | --- | --- | --- |
|     |     |     |     |     |         | T    |     | ·              |     |     |     |     |     |
τ∈Tx
thereby the clipped values on the domain can contribute with individual slope coefficients. This allows an efficient
approximationofnon-linearfunctionalrelationshipswhilepreservinglinearityinthecoefficients[31]. ReLUsplines
are especially useful for variables with known and bounded domain such as the trading time t in our application,
but can in theory be used for any continuous variable. Even though the thresholds x can be chosen arbitrarily, we
T
| generally |     | use an equidistant |     | grid. |     |     |     |     |     |     |     |     |     |
| --------- | --- | ------------------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
πd,h
The logistic regression model used to estimate the conditional mixing probabilities is defined as
t
|     | (cid:32) | πd,h (cid:33) |     |     |     |     |     |     |     |     |     |     |     |
| --- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
log t =β +β WindOnd,h+β WindOffd,h+β Solard,h+β Loadd,h+β MOd,h
|     |     | πd,h | 0         | 1   |     | 2   |     | 3                    |     | 4   |     | 5           |     |
| --- | --- | ---- | --------- | --- | --- | --- | --- | -------------------- | --- | --- | --- | ----------- | --- |
|     | 1   |      | (cid:124) | ·   |     | ·   |     | (cid:123) (cid:122)· |     | ·   |     | · (cid:125) |     |
− t
FundamentalForecasts.
+β SIDC (d,h,t)+β SIDC (d,h,t)+β SIDC (d,h,t)+β SIDC (d,h,t)+β SIDC (d,h,t)
|     |           | 6 · O |     | 7 · | 1   | 8 · | 2                  |     | 9 · | C   |     | 10 · L |           |
| --- | --------- | ----- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | ------ | --------- |
|     | (cid:124) |       |     |     |     |     | (cid:123)(cid:122) |     |     |     |     |        | (cid:125) |
DummiesforSIDC.SeeTable2fortheexactdefinitions
|     |     |     |     |     | 6                       |                    |           |           | H                                         |     |                    |                 |           |
| --- | --- | --- | --- | --- | ----------------------- | ------------------ | --------- | --------- | ----------------------------------------- | --- | ------------------ | --------------- | --------- |
|     |     |     |     |     | (cid:88)                | DOWk(d)+           |           | (cid:88)  | (cid:88)                                  |     |                    |                 |           |
|     |     |     |     |     | +                       | β                  |           |           | β                                         |     | ReLU(t,            | ) Hour (d,h,s), | (4)       |
|     |     |     |     |     |                         | 10+k ·             |           |           | 17+(τ,h)                                  | ·   |                    | T t ⊗ h         |           |
|     |     |     |     |     | k=1                     |                    |           | τ∈Tt      | h                                         |     |                    |                 |           |
|     |     |     |     |     | (cid:124)               | (cid:123)(cid:122) | (cid:125) | (cid:124) |                                           |     | (cid:123)(cid:122) |                 | (cid:125) |
|     |     |     |     |     | Day-of-the-weekdummies. |                    |           |           | ReLUsplinesfortradingtimeperdeliveryhour. |     |                    |                 |           |
where β denotes the intercept, β to β are the coefficients for the fundamental wind, solar and load forecasts, β
|     | 0   |     |     | 1   | 4   |     |     |     |     |     |     |     | 5   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
to β 9 are the coefficients for the single intraday coupling dummies SIDC {O,1,2,C,L} (d,h,t). The dummies denote
whether the cross-border order books are open, the start of the 1st and 2nd wave, the closing of the cross-border
order books 1 hour before the gate closure and the last periods of (local) trading. Table 2 gives the specification
11

|     | Variable |     | Trading | Time | t   | Interpretation |     |     |     |     |     |     |     |
| --- | -------- | --- | ------- | ---- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
SIDC (d,h,t) t 12 & T t 2 All periods in which the cross-border order books are open.
O
|     |     |     | ≥   |     | − ≥ |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
SIDC 1 (d,h,t) t=12 First wave of cross-border order book coupling at d 1 18:00 hours.
−
SIDC (d,h,t) t=28 Second wave of cross-border order book coupling at d 1 22:00 hours.
|     | 2   |     |     |     |     |     |     |     |     |     |     | −   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
SIDC (d,h,t) T t=2 Closing of the cross-border order books one hour before delivery.
C
−
SIDC (d,h,t) T t 2 All periods after the closing of cross-border order books.
|     | L   |     |     | − ≤ |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Table 2: Specification of the Boolean variables related to the single intraday coupling SIDC. The opening of the
cross-border order books happens at 18:00 and 22:00 hours for all delivery periods of the following day. However,
the closure of cross-border order books is relative to the delivery time. Hence we need to count backwards in the
| trading | time, | taking | T   | t for | variables | related | to  | the closure |     | of SIDC. |     |     |     |
| ------- | ----- | ------ | --- | ----- | --------- | ------- | --- | ----------- | --- | -------- | --- | --- | --- |
−
of the SIDC related dummies. We include day-of-the-week dummies for the delivery day d with the coefficients β
10
to β . The last term denotes a ReLU spline for the trading time t on an equidistant grid , with denoting the
|     | 15  |     |     |     |     |     |     |     |     |     |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
T ⊗
Kronecker product. We conduct a grid search on the validation data set to select the step size of the grid and
T t
theregularizationparameterbasedonthevalidationaccuracy. Thestepsizeisconstantacrossallh. Anexemplary
fit for the ReLU spline along the trading time t can be seen in Figure 9. The estimation is regularized using the
L norm, which we choose from an exponential grid on 0.001 to 1000. We also evaluate the Bayesian Information
2
Criterion (BIC) for each combination of step size and L regularization and find that the results align.
2
The following paragraph describes the probabilistic model for the marginal distribution with time-varying loca-
F
tion, scaleandshapeparameters. Ourgeneralframeworkfollowsthegeneralizedadditivemodelsforlocation, scale
and shape introduced by [41]. Let Y =(Y 1 ,Y 2 ,...,Y n ) be a vector of n independent observations Y i and Y i have the
| probability |     | (density) |     | function |     |     |         |           |              |     |       |     |     |
| ----------- | --- | --------- | --- | -------- | --- | --- | ------- | --------- | ------------ | --- | ----- | --- | --- |
|             |     |           |     |          |     |     | f(y i µ | i ,σ i ,ν | i ,τ i )=f(y | i   | θ i ) |     |     |
|             |     |           |     |          |     |     | |       |           |              |     | |     |     |     |
θk
where each distribution parameter can be a smooth function of explanatory variables. Denote =(µ i ,σ i ,ν i ,τ i )=
i
(θ1,θ2,θ3,θk) as the n k parameter vector with k location, scale and shape parameters. We have
×
|     |     |     |     |     |     | Y   | (µ  | ,σ ,ν | ,τ ) | Y      | (θ ). |     | (5) |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---- | ------ | ----- | --- | --- |
|     |     |     |     |     |     | i   | ∼F  | i i   | i i  | ⇔ i ∼F | i     |     |     |
θk
Let g k () be a known monotonic link function for each distribution parameter relating to explanatory variables
·
| through | an  | additive | model |     |     |     |     |        |     |     |     |     |     |
| ------- | --- | -------- | ----- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
|         |     |          |       |     |     |     | g   | (θk)=η | =X  | β   |     |     | (6) |
|         |     |          |       |     |     |     | k   |        | k   | k k |     |     |     |
X
where k is a n J k known design matrix of J k exogenous regressors. Additionally, the model can consists of
×
non-linear effects as in classical generalized additive models. Note that each distribution parameter can have an
| individual |     | design | matrix | X . |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
k
∆Pd,h.
As noted, we assume Johnson’s S distribution for the marginal distribution of The probability density
|          |     |           |     |                | U   |            |     |          |     |     |     | t   |     |
| -------- | --- | --------- | --- | -------------- | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- |
| function | of  | Johnson’s |     | S distribution |     | is defined | as  | follows: |     |     |     |     |     |
U
|     |     |     |     |     |     | 1   |     | τ   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
µ)/σ))2)
|     |     |     | f(y;µ,σ,ν,τ)= |     |      | (cid:112) |       |         |     | exp( 0.5(ν+τarcsinh((y |     |     | (7) |
| --- | --- | --- | ------------- | --- | ---- | --------- | ----- | ------- | --- | ---------------------- | --- | --- | --- |
|     |     |     |               |     | σ√2π |           | 1+((y | µ)/σ))2 |     | −                      |     | −   |     |
−
where µ ,0 < σ ,0 < ν , τ represent the location, scale, tail and skewness
|     | −∞  | ≤   | ≤ ∞ |     | ≤ ∞ |     | ≤ ∞ | −∞  | ≤   | ≤ ∞ |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
parametersandtheirrespectivedomains. Toensurealldistributionparametersarewithintheirdomain,weemploy
the link functions
|     |     |     |     |     |     | g   | (x)=x, |     |     |     |     |     | (8) |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
µ
12

g (x)=ϵ+log(1+exp(γ x)), (9)
σ
·
g (x)=ϵ+log(1+exp(γ x)), (10)
ν
·
g (x)=x, (11)
τ
where the link functions for µ and τ are the identity and the link functions for σ and ν are known as Softplus link
function with constants ϵ=1−3 and γ =0.1 to improve numerical stability [45]. Formally, we define the model as
follows:
3
(cid:88)
g (µ)= β ∆Pd,h (12)
µ i · t−i
i=1
g (σ)=β +β WindOnd,h+β WindOffd,h+β Solard,h+β Loadd,h+β MOd,h
σ 0 1 2 3 4 5
(cid:124) · · (cid:123)(cid:122)· · · (cid:125)
FundamentalForecasts.
+β SIDC (d,h,t)+β SIDC (d,h,t)+β SIDC (d,h,t)+β SIDC (d,h,t)+β SIDC (d,h,t)
6 O 7 1 8 2 9 C 10 L
· · · · ·
(cid:124) (cid:123)(cid:122) (cid:125)
DummiesforSIDC.
6 23
(cid:88) (cid:88)
+ β DOWk(d)+ β Hour (d,h,s)
10+k 16+h h
·
k=1 h=0
(cid:124) (cid:123)(cid:122) (cid:125) (cid:124) (cid:123)(cid:122) (cid:125)
Day-of-the-weekdummies. Dummiesperdeliveryhour.
(cid:88) (cid:88)
+ β ReLU(t, 10)+ β ReLU(T t, 10 )
39+(τ,t) · Tt 52+(τ,T−t) · − TT−t
τ∈T10 τ∈T10
t T−t
(cid:124) (cid:123)(cid:122) (cid:125) (cid:124) (cid:123)(cid:122) (cid:125)
TradingtimetReLUspline. TimetodeliveryT−tReLUspline.
3 3
(cid:88) (cid:88) (cid:88)
+ β ∆Pd,h + β αd,h+ β ReLU(P , 50 )
65+i ·| t−i | 68+i · t−i 71+(τ,Spot) · Spot TSpot
i=1 i=1 τ∈T50
(cid:124) (cid:123)(cid:122) (cid:125) (cid:124) (cid:123)(cid:122) (cid:125) Spot
(cid:124) (cid:123)(cid:122) (cid:125)
Laggedabsolute∆P t d − ,h i . Laggedαd t ,h. SpotpriceReLUspline.
(13)
g (ν)=β WindOnd,h+β WindOffd,h+β Solard,h+β Loadd,h+β MOd,h
ν 0 1 2 3 4
(cid:124) · · (cid:123)(cid:122)· · · (cid:125)
FundamentalForecasts.
+β SIDC (d,h,t)+β SIDC (d,h,t)+β SIDC (d,h,t)+β SIDC (d,h,t)+β SIDC (d,h,t)
5 O 6 1 7 2 8 C 9 L
· · · · ·
(cid:124) (cid:123)(cid:122) (cid:125)
DummiesforSIDC.
6 3 3 23
(cid:88) (cid:88) (cid:88) (cid:88)
+ β DOWk(d)+ β ∆Pd,h + β αd,h+ β Hour (d,h,s)
10+k · 15+i ·| t−i | 18+i · t−i 21+h h
k=1 i=1 i=1 h=0
(cid:124) (cid:123)(cid:122) (cid:125) (cid:124) (cid:123)(cid:122) (cid:125) (cid:124) (cid:123)(cid:122) (cid:125) (cid:124) (cid:123)(cid:122) (cid:125)
Day-of-the-weekdummies. Laggedabsolute∆Pd,h. Laggedαd,h. Dummiesperdeliveryhour.
t−i t
(14)
23 6
(cid:88) (cid:88)
g (τ)= β Hour (d,h,s) + β DOWk(d)
τ h h 23+k
· (15)
h=0 k=1
(cid:124) (cid:123)(cid:122) (cid:125) (cid:124) (cid:123)(cid:122) (cid:125)
Dummiesperdeliveryhour. Day-of-the-weekdummies.
We model the conditional location, scale and shape parameters based on fundamental variables. We guide our
selection from the literature [20, 33, 21, 32] and regularize the estimation to avoid overfitting.
13

| •   |     |     |     |     |     |     |     |     | ∆Pd,h. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
The location parameter µ is modelled through three autoregressive lags of t
• The scale parameter σ is modelled through the the fundamental wind, solar and demand forecasts and the
coefficientforthemerit-orderregime. Additionally,weincludeday-of-theweekandhourlydummiestoaccount
for different baseline volatility. We include a ReLU spline for the trading time and the time to delivery to
capture the effects of increasing volatility towards gate closure and a ReLU spline for the spot price level to
| account | for the impact | of  | different | price regimes. |     |     |     |     |     |
| ------- | -------------- | --- | --------- | -------------- | --- | --- | --- | --- | --- |
• The tail parameter ν is explained using a similar, but slightly reduced set of features as the scale parameter
σ.
• Theskewnessparameterτ isexplainedonlyusingday-of-the-weekandhourlydummies. Thischaracterization
| is backed | by the recent | findings | of  | [20]. |     |     |     |     |     |
| --------- | ------------- | -------- | --- | ----- | --- | --- | --- | --- | --- |
As the modelling of the distributions higher moments is dependent on the quality of the lower moments’ models
[on this issue, see. e.g. 51], we refrain from making the models for ν and τ as complex as the model for the scale
parameter σ and decrease complexity accordingly. For the expected value of intraday price changes, many studies
have shown indications of weak-form market efficiency [20, 32, 33, 48, 21, 27], hence we keep the model simple as
| possible without | comprising | the | quality | of the estimation |     | for σ,ν | and | τ.  |     |
| ---------------- | ---------- | --- | ------- | ----------------- | --- | ------- | --- | --- | --- |
Ourestimationsareimplementedusingthescikit-learn[38]andthetensorflow-probabilitypackages[13,1]in
python. Weautomaticallytunethehyperparametersofourmodelusingthewell-knownoptunalibrary, aBayesian
framework specifically tailored towards the optimization of hyperparameters of machine learning models [2]. The
sampling space for the hyperparameter tuning framework can be found in Table 3. We initialize the coefficients for
the estimation of the conditional location parameter µ as 0, while the remaining coefficient vectors are initialized
uniformly sampled. We tune the L -regularization for all distribution parameters, the learning rate and introduce
1
a dropout layer during the training process to reduce the risk of overfitting [4, 46, 51]. During model fitting, we
reserve 25% of our training data as validation set to employ early stopping if the training-validation loss does not
improve after 25 epochs [51, 29]. We run 250 iterations of the optuna algorithm and observe the best trial at
| iteration | 48. Diagnostic | plots can | be found | in the | Appendix | (see  | Figure | 15). |     |
| --------- | -------------- | --------- | -------- | ------ | -------- | ----- | ------ | ---- | --- |
|           |                | Parameter |          |        | Search   | space |        |      |     |
(1−6,103)
|     |     | L   | 1 regularization |     | µ Exponential |     | grid | on           |     |
| --- | --- | --- | ---------------- | --- | ------------- | --- | ---- | ------------ | --- |
|     |     | L   | regularization   |     | σ Exponential |     | grid | on (1−6,103) |     |
1
|     |     | L   | regularization |     | ν Exponential |     | grid | on (1−6,103) |     |
| --- | --- | --- | -------------- | --- | ------------- | --- | ---- | ------------ | --- |
1
(1−6,103)
|     |     | L        | 1 regularization |      | τ Exponential |      | grid | on           |     |
| --- | --- | -------- | ---------------- | ---- | ------------- | ---- | ---- | ------------ | --- |
|     |     | Learning |                  | Rate | Exponential   |      | grid | on (1−5,1−2) |     |
|     |     | Dropout  |                  | Rate | Uniform       | grid | on   | (0, 1)       |     |
Table 3: Search spaces for our automated hyperparameter optimization tuning using the optuna framework.
4.2 Dependence
=(∆Pd,1,∆Pd,2,...,∆Pd,23),wherethedifferent
| RememberthatwesimulatetheT |     |     | H pricedifferencevector∆Pd |     |     |     |     |     |     |
| -------------------------- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- |
|                            |     |     | ×                          |     |     |     | t   | t   | t t |
delivery periods can be correlated. Our strategy follows the general setup of [7, 8]. We estimate the dependence as
| the covariance | after we gaussianize |     | our | data in the | spirit | of Sklar’s | theorem. |     |     |
| -------------- | -------------------- | --- | --- | ----------- | ------ | ---------- | -------- | --- | --- |
In our copula-based modelling approach, we employ three different structures for the dependence with increasing
14

ThesimplestmodelassumesthatalldeliveryperiodsareindependentandisdenotedasMix.Ind.
| complexity. |     |     |     |     |     |     |     |     | The |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
next complex model assumes a constant cross-product dependence across the trading window and is denoted as
Mix.CD. Lastly, we estimate a time-varying dependence parameter across the trading time t. The resulting most
| complex | model | is denoted | as  | Mix.TD. |     |     |     |     |     |
| ------- | ----- | ---------- | --- | ------- | --- | --- | --- | --- | --- |
WedenotethedependenceparameterbetweentwodeliveryhoursA,B asρA,B. Fortheconstantdependencemodel,
| we estimate | the | pairwise | dependence |     | parameter | as: |     |     |     |
| ----------- | --- | -------- | ---------- | --- | --------- | --- | --- | --- | --- |
ρA,B =cov(∆Pd,A,∆Pd,B).
|     |     |     |     |     |     |     | t t |     | (16) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
Thepair-wiseestimationisnecessaryasnotalldeliveryperiodshavethesametradinglength. Forourtime-varying
dependence model Mix.TD, we fit ρ as a latent variable using the beta-regression.
10
|     |     |     |     | ρA,B |     | (cid:88) |                         |     |      |
| --- | --- | --- | --- | ---- | --- | -------- | ----------------------- | --- | ---- |
|     |     |     |     |      | =β  | 0 + β i  | ReLU(t,(0,12,...,128)). |     | (17) |
|     |     |     |     |      | t   |          | ·                       |     |      |
i=1
To estimate the beta-regression, we use the correlation coefficient on the pseudo-Gaussian observations, which we
map to the (0, 1) space required by the beta-regression model. We use the BIC to decide on the width of the grid
of the spline on t and transform the estimated values back to the covariance using the inverse mapping and the
| empirical      | standard | deviation |          | of the pseudo-Gaussian |     |     | observations. |     |     |
| -------------- | -------- | --------- | -------- | ---------------------- | --- | --- | ------------- | --- | --- |
| 4.3 Simulation |          |           | Approach |                        |     |     |               |     |     |
d,h,[m]
We simulate m=1,...,M paths for the T H-dimensional intraday price path vector. Denote with ∆P the
t
×
simulated price change at trading time t for delivery period d,h. The price path can be seen as the cumulative
sum of all price changes and the initial price P d,h,[m] . In line with previous works [see e.g. 35, 27] we initialise the
0
|          |          |          |       | d,h,[m] | =Pd,h |             |          |     |     |
| -------- | -------- | -------- | ----- | ------- | ----- | ----------- | -------- | --- | --- |
| intraday | price as | the spot | price | P       |       | . Formally, | we have: |     |     |
|          |          |          |       | 0       |       | Spot        |          |     |     |
t
(cid:88)
|     |     |     |     |     | P d,h,[m] | =Pd,h | + ∆P | d,h,[m] | (18) |
| --- | --- | --- | --- | --- | --------- | ----- | ---- | ------- | ---- |
|     |     |     |     |     | t         |       | Spot | k       |      |
k=1
where it is important to note that the end of trading, T, depends on h. Therefore, the vector is not square but has
| the asymmetric |     | trapezoid | shape  | already | visible | in Figure | 1 and Figure | 4.  |     |
| -------------- | --- | --------- | ------ | ------- | ------- | --------- | ------------ | --- | --- |
| 4.4 Benchmark  |     |           | Models |         |         |           |              |     |     |
naive
We employ three benchmark models from the literature. First, we employ the well performing model intro-
ducedby[33,20]. Themodelre-usespastpricetrajectoriesbysampling. Weemploythemodelintwoversions,first
assuming independence between different delivery hours (i.e sampling each delivery hour h=0,...,H individually)
andsecondbysamplingthefullT H pathvector. Thethirdbenchmarkmodelisaarithmeticrandomwalkmodel
×
introducedby[27]drawingfromtheempiricalpricedifferencedistribution. Thefollowingparagraphsintroducethe
| benchmark     | models | formally.     |     |       |            |     |     |     |     |
| ------------- | ------ | ------------- | --- | ----- | ---------- | --- | --- | --- | --- |
| The Naive.Ind |        | and Naive.Dep |     | model | is defined | as  |     |     |     |
=∆Pd′,h,
|     |     |     |     |     |     | ∆Pd,h,[m] |     |     | (19) |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | ---- |
where d′ is a random day sampled from the training data set d′ ( 0,...,d 1 ). Note that for the Naive.Ind
|     |     |     |     |     |     |     | ∼   | U { − } |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
we sample d′ independent for each delivery hour h = 0,...,H and for the Naive.Dep, we use the same d′ for all
15

h. [20, 33] have shown that this type of benchmark models provides very good point and probabilistic forecasting
| performance | in  | ensemble | forecasting |     | settings. |     |     |     |     |     |     |
| ----------- | --- | -------- | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- |
TheRW.Emphasbeenusedby[27]togeneratepathsfortheintradaymarketinanapplicationstudyforgrid-scale
storageoptimization. Thepriceprocessisdefinedasrandomwalk,wheretheinnovationsaredrawnfromadiscrete
| distribution | of  | the centered |     | empirical | price | changes. | It is | defined | as: |     |     |
| ------------ | --- | ------------ | --- | --------- | ----- | -------- | ----- | ------- | --- | --- | --- |
d−1
1 (cid:88)
|     |     |     |     |     | d,h,[m] | =∆Pd′,h |     |     | (Pd,h | Pd,h), |      |
| --- | --- | --- | --- | --- | ------- | ------- | --- | --- | ----- | ------ | ---- |
|     |     |     |     |     | ∆P t    | t       |     |     | t−1−  | t      | (20) |
− d 1
− d=0
|     | d′  |     |     |     |     |     |     |     | d′  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
where again is a random day sampled from the training data set ( 0,...,d 1 ) and the second term
|     |     |     |     |     |     |     |     |     |     | ∼ U { − } |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- |
centers all residuals to mean zero, ensuring the price process to be a martingale.
For all three benchmark models, the size of the training data d = 0,...,d 1 is a tuning parameter, which we
−
| optimize   | through | a grid | search. |     |            |     |         |     |     |     |     |
| ---------- | ------- | ------ | ------- | --- | ---------- | --- | ------- | --- | --- | --- | --- |
| 5 Forecast |         | Study  |         | and | Evaluation |     | Metrics |     |     |     |     |
We employ the well-known rolling window forecasting study design. Our data comprises of the three years between
2020-01-01and2023-01-01. Wesplitourdatasetinatraining, validationandtestdataset. Ourinitialtrainingset
is 2020-01-01 to 2021-07-01, the validation set contains 2021-07-01 to 2022-01-01 and our test set contains the final
year 2022-01-01 to 2023-01-01. The split is also depicted in Figure 7. We use the initial training set to develop and
estimate our models and the validation data set to calibrate hyperparameters. We use the test set to run a rolling
window forecasting study with monthly re-training of all models using the most recent two years of data. This is
duetothehighcomputationalburdenoftrainingandtuningtheprobabilisticmodelsintensorflow-probability.
Weevaluateoursimulationsfromapointandprobabilisticforecastingperspectiveusingstrictlyproperscoringrules
[19]. Weevaluatethemeanandmediansimulationpathsusingthewellknownrootmeansquarederror(RMSE)and
medianabsoluteerror(MAE).Themarginalfitisevaluatedusingthecontinuousrankedprobabilityscore(CRPS),
whichweapproximateonadensegridofquantilesusingthepinballscore(PB).Weevaluatethescenariopathsusing
theenergyscore(ES).Theenergyscoreisthemultivariategeneralizationofthecontinuousrankedprobabilityscore,
taking into account the correlation structure. We establish significance using the Diebold-Mariano test [12, 11] for
comparing predictive accuracy. The following few paragraphs introduce our metrics formally.
| The root | mean | squared | error | is defined | as: |     |     |     |     |     |     |
| -------- | ---- | ------- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- |
(cid:118)
|     |     |     |     |         |     |                      | (cid:32) |          |           | (cid:33)2 |      |
| --- | --- | --- | --- | ------- | --- | -------------------- | -------- | -------- | --------- | --------- | ---- |
|     |     |     |     |         |     | (cid:117)            | T        | M        |           |           |      |
|     |     |     |     |         |     | (cid:117) 1 (cid:88) | 1        | (cid:88) |           |           |      |
|     |     |     |     | RMSEd,h |     | = (cid:116)          |          |          | P d,h,[m] | Pd,h .    | (21) |
|     |     |     |     |         |     |                      |          |          | t         | t         |      |
|     |     |     |     |         |     | T                    | M        |          | −         |           |      |
|     |     |     |     |         |     | t=1                  |          | m=1      |           |           |      |
The RMSE is a strictly proper scoring rule for the expected value. We also report the RMSE averaged additionally
| across the | delivery | hours | h   | and delivery |     | days d. |     |     |     |     |     |
| ---------- | -------- | ----- | --- | ------------ | --- | ------- | --- | --- | --- | --- | --- |
d,h,[m]
DenotethemediantrajectoryoverallM simulatedtrajectoriesasmed(P t ). Themeanabsoluteerrorisdefined
as:
T
|     |     |     |     |     | MAEd,h | 1 (cid:88) |       | d,h,[m] | Pd,h |     |      |
| --- | --- | --- | --- | --- | ------ | ---------- | ----- | ------- | ---- | --- | ---- |
|     |     |     |     |     |        | =          | med(P |         | )    | .   | (22) |
|     |     |     |     |     |        | T          | |     | t       | −    | t | |      |
t=1
16

We evaluate the probabilistic forecasting performance using the continuous ranked probability score (CRPS) and
the energy score (ES). Both are strictly proper scoring rules for the marginal distribution respectively the multidi-
mensional predictive distribution [19, 52] and routinely used in probabilistic energy forecasting [20, 33, 5, 36].
The CRPS is approximated using the pinball score on a dense grid of quantiles of our scenarios. Let Qd,h(P d,h,[m] )
|     |     |     |     |     |     |     |     |     |     |     | τ,t | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
denote the τ-quantile of our simulation paths P d,h,[m] . The τ-PB can be defined as:
t
|     |     |     |     |            | (cid:16) |         |         | (cid:17) |             |            |     |      |
| --- | --- | --- | ---- | ---------- | -------- | ------- | ------- | -------- | ----------- | ---------- | --- | ---- |
|     |     |     | (1  | τ)         | Qd,h(P   | d,h,[m] | )       | Pd,h for | Pd,h Qd,h(P | d,h,[m] ). |     |      |
|     |     | PBd | , h  |            |          | τ,t t   |         | t        | t τ,t       | t          |     |      |
|     |     |     | =    | − (cid:16) | ·        |         | −       | (cid:17) | ≤           |            |     | (23) |
|     |     |     | τ, t | Pd,        | h        | d,h(    | d,h,[m] |          |             |            |     |      |
|     |     |     | τ   |            |          | Q P     | )       | else.    |             |            |     |      |
|     |     |     |      | ·          | t −      | τ,t t   |         |          |             |            |     |      |
The CRPS is the average across all quantile levels = 0.01,..,0.99 of length 99:
|     |     |     |     |     |     |     | T { |     | }   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
T
|     |     |     |     |     |         |     | 1 1 | (cid:88)(cid:88) |     |     |     |      |
| --- | --- | --- | --- | --- | ------- | --- | --- | ---------------- | --- | --- | --- | ---- |
|     |     |     |     |     | CRPSd,h |     | =   | PBd,h            |     |     |     | (24) |
τ,t
T 99
t=0τ∈T
| For the energy | score, | we  | implement | the      | K-band | estimator |     | as given | in [52]:   |     |          |     |
| -------------- | ------ | --- | --------- | -------- | ------ | --------- | --- | -------- | ---------- | --- | -------- | --- |
|                |        |     | M         | (cid:13) |        | (cid:13)  |     | M        | K (cid:13) |     | (cid:13) |     |
ESd,h 1 (cid:88) d,h,[m] Pd,h 1 (cid:88) (cid:88) d,h,[m] d,h,[k+1]
|     |     | =   |     | (cid:13)P |     | (cid:13) |     |     | (cid:13)P | P   | (cid:13) | (25) |
| --- | --- | --- | --- | --------- | --- | -------- | --- | --- | --------- | --- | -------- | ---- |
K M (cid:13) t − t (cid:13) 2− M (K 1) (cid:13) t − t (cid:13)
2
|     |     |     | m=1 |     |     |           | ·   | − m=1k=m |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | -------- | --- | --- | --- | --- |
|     |     |     |     |     |     | d,h,[M+k] |     | d,h,[k]  |     |     |     |     |
for an integer 1 K M and where we set P =P . denotes the L or Euclidean norm. We use
|     | ≤   | ≤   |     |     |     | t   |     | t ∥·∥2 |     | 2   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
K =10 as trade-off between computational complexity and estimation accuracy. We evaluate the energy score for
the full scenario trajectory and for the last three hours of before the start of physical delivery for each model. The
later evaluation acknowledges the importance of the last hours of trading and appeals to practitioners in the field.
We use the Diebold-Mariano (DM) test to compare the predictive accuracy of the forecasts [36, 12, 11]. Intuitively,
the DM-test evaluates the null hypothesis (H ) that the difference in means between the loss series of two models
0
is statistically significantly different from zero. Formally, for two models A and B, let L and L the loss series.
|                       |     |     |            |     |     |     |     |     |     | A   | B   |     |
| --------------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| The loss differential |     | ∆   | is defined | as  |     |     |     |     |     |     |     |     |
A,B
|     |     |     |     |     |     | ∆i  | = L | L         |     |     |     | (26) |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | ---- |
|     |     |     |     |     |     | A,B | A   | ∥i−∥ A ∥i |     |     |     |      |
∥
(cid:2) (cid:3)
for the i-norm. For each model pair, we test two one-sided tests for the null hypothesis (1) E ∆i > 0 and
A,B
| E(cid:2) ∆i | (cid:3) |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(2) < 0, i.e. (1) the forecasts of model B outperform the forecasts of model A and (2) the forecasts of
A,B
model A outperform the forecasts of model B. These tests are complimentary. Note that the Diebold-Mariano test
assumes the loss differential series to be stationary. We test this assumption using the augmented Dickey-Fuller
test [10].
| 6 Results |     | and | Discussion |     |     |     |     |     |     |     |     |     |
| --------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Our parametric approach to modelling the distribution parameters allows us to derive some fundamental insight
in the driving factors of the intraday price process. The following section presents first presents some in-sample
results from our modelling and subsequently presents the results from our forecasting study.
17

6.1 Fundamental Analysis
Our parametric modelling set-up allows us to analyse the influence of the driving factors for the location, shape
and scale parameters of the price distribution. Our focus here is on the impact of the SIDC on the trading activity
and the impact of fundamental variables on the volatility.
The evolution of the trading activity respectively the share of no-trade events can be seen in Figure 9. We note
that in the first hours of trading and that trading activity rises non-linearly towards gate closure. The opening of
SIDC induces to spikes in trading activity when the cross-border order books are coupled. At this point, orders in
markets with previously different price levels are instantly matched, leading high trading activity for short periods
oftime. AftertheSIDCcoupling,tradingactivityincreasestowardsthegateclosure. Thelasttradingperiodshave
(almost) no no-trade events.
We show the contribution of individual groups of regressors on the scale parameter in Figure 10. Recall that we
model the volatility by four main groups of regressors: fundamental forecasts, time-derived variables, SIDC-related
variables, and variables related to the trading activity. Generally, we note a pattern of higher volatility in the
beginning of the trading session, followed by decrease and an increase closer to delivery. We note that SIDC has
a distinct impact on the scale parameter: The opening of the cross-border order books at 18:00 and 22:00 for the
leads to clearly visible spikes in the volatility. Subsequently, the phase during which the order-books are coupled
is characterized by lower volatility. The closing of the cross-border order books shortly before delivery leads to a
spike in volatility. The dampening effect of the open SIDC order books on volatility is likely due to the increased
liquidity available to market participants, while the volatility spikes during the opening at 18:00 and 22:00 hours
can be explained by matching the order books at different price levels. Overall, the effects contradict the results of
[22], who finds no effects of SIDC, but align with [33, 20] on the effect of the SIDC closing period. Comparing the
different delivery hours h = 0,6,12 and 18, we note the different impact of the time to delivery and trading time
splines. The time-to-delivery spline kicks in early, but keeps rather constant shortly before the delivery. On the
other side, the trading time t spline rises with trading time.
The influence of fundamental variables like wind, solar and demand forecasts is small. One reason for this might
be, that these forecasts are generated at the day-ahead stage and are not updated throughout the trading window,
aspreviousworks[25,50,20]haveshownthattheintradaymarketismoreimpactedbyforecastchangescompared,
while the level of forecasts is less important. Additionally, the conclusion that fundamental variables seem not to
improve forecasts supports the notion of market efficiency as already indicated by [32, 33, 20].
6.2 Forecasting Performance
This section presents the results of the out-of-sample forecasting study. Aggregate error metrics are given in Table
4. Figure 11 presents the error metrics by the delivery hour h. Figure 13 gives the results of our pairwise Diebold-
Mariano tests.
Remember that we have both, the naive model and the mixture model in in at least two versions: one version
assuming independence between different delivery hours and at least one version that considers the correlation
structure. Additionally, the RW.Emp considers the correlation structure implicitly. The results for the energy
score show that considering the correlation structure leads to (significantly, see Figure 13) better forecasts than
assumingindependenceiftheremainingmodelstructureisunchanged. ThisholdsformovingfromtheNaive.Indto
the Naive.Dep and for moving from the Mix.Ind to Mix.CD. Interestingly, modelling the dependence structure
in a potentially time-varying fashion does not improve the forecasting performance. For the energy score, the
difference in ordering for the models between the full path and the last three hours of trading. Note however, that
the scale of both is not directly comparable. This is an important result for modelling the intraday market in
18

Decomposition of the driving variables for g( t) for 2020-01-02, h = 0 Decomposition of the driving variables for g( t) for 2020-01-02, h = 6
| 25  |     |     |     | 25  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Delivery Hour Wind Onshore Merit-Order Regime Delivery Hour Wind Onshore Merit-Order Regime
Day of the week Wind Offshore Lagged t Day of the week Wind Offshore Lagged t
20 Spline for Trading t Solar Lagged P 20 Spline for Trading t Solar Lagged P
Spline for Time-to-delivery Load Spline for Spot Price Spline for Time-to-delivery Load Spline for Spot Price
| SIDC                 |                |       |       |                      | SIDC  |                |     |
| -------------------- | -------------- | ----- | ----- | -------------------- | ----- | -------------- | --- |
| 15                   |                |       |       | 15                   |       |                |     |
| )t(g ot noitubirtnoC |                |       |       | )t(g ot noitubirtnoC |       |                |     |
| 10                   |                |       |       | 10                   |       |                |     |
| 5                    |                |       |       | 5                    |       |                |     |
| 0                    |                |       |       | 0                    |       |                |     |
| 5                    |                |       |       | 5                    |       |                |     |
| 10                   |                |       |       | 10                   |       |                |     |
| 15                   |                |       |       | 15                   |       |                |     |
| 5 10                 | 15             | 20 25 | 30 35 |                      | 10 20 | 30 40          | 50  |
|                      | Trading time t |       |       |                      |       | Trading time t |     |
Decomposition of the driving variables for g( t) for 2020-01-02, h = 12 Decomposition of the driving variables for g( t) for 2020-01-02, h = 18
| 25  |     |     |     | 25  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Delivery Hour Wind Onshore Merit-Order Regime Delivery Hour Wind Onshore Merit-Order Regime
Day of the week Wind Offshore Lagged t Day of the week Wind Offshore Lagged t
| Spline for Trading t |       |          |     |     | Spline for Trading t |       |          |
| -------------------- | ----- | -------- | --- | --- | -------------------- | ----- | -------- |
| 20                   | Solar | Lagged P |     | 20  |                      | Solar | Lagged P |
Spline for Time-to-delivery Load Spline for Spot Price Spline for Time-to-delivery Load Spline for Spot Price
| SIDC                    |                |       |       |                         | SIDC  |                |        |
| ----------------------- | -------------- | ----- | ----- | ----------------------- | ----- | -------------- | ------ |
| 15                      |                |       |       | 15                      |       |                |        |
| )t(g ot noitubirtnoC 10 |                |       |       | )t(g ot noitubirtnoC 10 |       |                |        |
| 5                       |                |       |       | 5                       |       |                |        |
| 0                       |                |       |       | 0                       |       |                |        |
| 5                       |                |       |       | 5                       |       |                |        |
| 10                      |                |       |       | 10                      |       |                |        |
| 15                      |                |       |       | 15                      |       |                |        |
| 10 20                   | 30 40          | 50 60 | 70 80 |                         | 20 40 | 60             | 80 100 |
|                         | Trading time t |       |       |                         |       | Trading time t |        |
Figure 10: Decomposition of the driving variables for the scale parameter g (σd,h). We show 2020-01-02 for hours
σ t
0, 6, 12 and 18. Variables are grouped by color. The impact of fundamental forecasts is constant throughout the
trading window as these are only available at the day-ahead stage. The link-function g () ensures that the final
σ
| σd,h         |           |     |     |     |     | ·   |     |
| ------------ | --------- | --- | --- | --- | --- | --- | --- |
| estimated is | positive. |     |     |     |     |     |     |
t
19

|     |     |     |     |     | MAE | RMSE | CRPS | ES  | ES  |     |
| --- | --- | --- | --- | --- | --- | ---- | ---- | --- | --- | --- |
3H
|     |     |     | Naive.Ind |     | 16.340 | 26.649 | 7.470 812.705  |     | 191.423 |     |
| --- | --- | --- | --------- | --- | ------ | ------ | -------------- | --- | ------- | --- |
|     |     |     | Naive.Dep |     | 16.330 | 26.626 | 6.782 801.908  |     | 185.909 |     |
|     |     |     | RW.Emp    |     | 15.942 | 26.407 | 6.352 846.752  |     | 214.710 |     |
|     |     |     | Mix.Ind   |     | 16.035 | 26.543 | 6.355 1028.382 |     | 258.125 |     |
|     |     |     | Mix.CD    |     | 16.032 | 26.558 | 7.462 992.077  |     | 243.131 |     |
|     |     |     | Mix.TD    |     | 16.024 | 26.511 | 7.321 1023.270 |     | 256.778 |     |
Table 4: Error statistics. All error metrics are averaged over t, h and d. The lowest value is highlighted.
Background color corresponds to forecasting accuracy. ES 3H denotes the energy score for the last 3 hours of
trading.
MAE by delivery hour h RMSE by delivery hour h ES by delivery hour h
|        |           |     |     |     |      | 28        |     |     | 275           |     |
| ------ | --------- | --- | --- | --- | ---- | --------- | --- | --- | ------------- | --- |
| 20     | Naive.Ind |     |     |     |      | Naive.Ind |     |     | Naive.Ind     |     |
|        | Naive.Dep |     |     |     |      | Naive.Dep |     |     | 250 Naive.Dep |     |
| 19     | RW.Emp    |     |     |     |      | 26 RW.Emp |     |     | RW.Emp        |     |
|        | Mix.Ind   |     |     |     |      | Mix.Ind   |     |     | 225 Mix.Ind   |     |
| 18     | Mix.CD    |     |     |     |      | Mix.CD    |     |     | Mix.CD        |     |
|        | Mix.TD    |     |     |     |      | 24 Mix.TD |     |     | 200 Mix.TD    |     |
| EAM 17 |           |     |     |     | ESMR |           |     |     | SE            |     |
175
| 16  |     |     |     |     |     | 22  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
150
15
|     |     |     |     |     |     | 20  |     |     | 125 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
14
100
| 13  |     |     |     |     |     | 18  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0 1 2 3 4 5 6 7 8 9 01 11 21 31 41 51 61 71 81 91 02 12 22 32 0 1 2 3 4 5 6 7 8 9 01 11 21 31 41 51 61 71 81 91 02 12 22 32 0 1 2 3 4 5 6 7 8 9 01 11 21 31 41 51 61 71 81 91 02 12 22 32
|     |     | Delivery hour h |     |     |     |     | Delivery hour h |     |     | Delivery hour h |
| --- | --- | --------------- | --- | --- | --- | --- | --------------- | --- | --- | --------------- |
Figure11: Errorstatisticsbydeliveryhourh. NotethatthescaleoftheMAEandRMSEisnotdirectlycomparable
to the ES.
applications such as battery/storage optimisation, where the neglecting the correlation structure can therefore lead
| to too | optimistic | results | [35, | 27]. |     |     |     |     |     |     |
| ------ | ---------- | ------- | ---- | ---- | --- | --- | --- | --- | --- | --- |
On an aggregate level, we see that the RW.Emp yields the best point forecasting performance (MAE and RMSE)
and the Naive.Dep yields the best probabilistic forecasting performance. The Diebold-Mariano test confirms
the statistical significance of superior probabilistic forecasting forecasts for the Naive.Dep. We note that the
forecastingperformanceofthemixturemodelsisnotasgoodastherathersimplebenchmarkmodels. Additionally,
we note that the Mix.Ind exhibits a lower CRPS than the Mix.CD and Mix.TD, which suggests some some
cross-propagationoferrors. Ontheotherhand,theMix.Indyieldsworsescoresfortheenergyscorethanitssister
| models | including | a dependence |     | structure. |     |     |     |     |     |     |
| ------ | --------- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- |
The hourly shape of forecasts errors throughout the day is depicted in Figure 11. It follows the typical shape of
prices in electricity prices, we see low forecast errors in the morning and higher errors through the day. Let us note
that the benchmark models exhibit a slightly higher MAE during the afternoon peak, but show lower RMSE and
ES during the same periods. Figure 12 presents the PB across the quantile range and the delivery hour. We can
see that the highest errors occur during the afternoon peak hours and in the higher distribution quantiles. Note
thatthepinballlossonlymeasuresthemarginalfittothedistribution. Inananalysisofthein-sample,transformed
observations we also note that throughout the rolling window study, the calibration decreases and we experience
| an  | underdispersed | forecast |     | (see Figure | 14  | in the Appendix). |     |     |     |     |
| --- | -------------- | -------- | --- | ----------- | --- | ----------------- | --- | --- | --- | --- |
Our results also emphasize the importance of robust approaches to modelling and forecasting in periods of high
20

22
20
18
16
14
12
10
8
6
4 2
0
ruoH
yrevileD
Naive.Ind Naive.Dep
22
20
18
16
14
12
10
8
6
4
2
0
ruoH
yrevileD
RW.Emp Mix.Ind
22
20
18 16
14
12
10
8
6
4
2
0
10 20 30 40 50 60 70 80 90
Quantile Level
ruoH
yrevileD
14
12
10
8
6
Mix.CD Mix.TD
4
2
10 20 30 40 50 60 70 80 90
Quantile Level
erocS
llabniP
Figure 12: Pinball Score by quantile level τ and delivery hour h.
dnI.eviaN peD.eviaN pmE.WR dnI.xiM DC.xiM DT.xiM
Diebold-Mariano Test Matrix
0.10
Naive.Ind 0.02 0.86 1 1 1
0.08
Naive.Dep 0.98 0.91 1 1 1
RW.Emp 0.14 0.09 1 1 1 0.06
Mix.Ind 0 0 0 0 0
0.04
Mix.CD 0 0 0 1 1
0.02
Mix.TD 0 0 0 1 0
0.00
eulaV-p
Figure 13: Diebold-Mariano Test Matrix. A p-value <0.05 implies that the model on the column has significantly
better forecasts than the model on the row.
21

volatility and black swan events such as the Russian invasion of Ukraine and the subsequent energy crisis in
Europe 2022/23. The Naive.Dep and Naive.Ind model already have shown very good probabilistic forecasting
performance in the respective studies of [20, 33] and are robust to extreme events, as out-of-support situations
with extreme prices cannot happen for these models. Additionally, our results can be viewed in the light of
the market efficiency hypothesis. Our result indicate that including more data, especially data that does not
change throughout the trading period (such as day-ahead forecasts) does not improve the modelling or the price.
The superior performance of the benchmark models, especially of the RW.Emp, which ensures the Martingale
assumption, underscores this notion. Similar results with respect to market efficiency have been found by [32].
7 Conclusion
This paper presents a a forecasting study for multivariate, simulation-based forecasting for intraday electricity
markets. We provide insight in the dependence structure of short-term electricity markets and extend previous
works of [33, 20] to include cross-product price effects.
Wedevelopaprobabilisticmodelforthemarginaldistributionoftheintradaypricepath,accountingfortheimpact
of fundamental driving variables on the location, scale and shape parameters. As novelty, we employ copulas
to model the (time-dependent) dependency between different delivery periods and the according parallel trading
sessions and allow the dependency parameter to be time-dependent. We validate our results in a forecasting study
for the German intraday electricity market. Our results indicate that modelling the dependence structure between
the different trading session improves the forecasting performance. Additionally, we provide evidence on market
efficiency in the German short-term market. Our fundamental and parametric approach allows us to shed further
light on the impact of the cross-border shared order books of the single intraday coupling (SIDC) and the driving
factors of the distribution parameters. Our case study employs data from the German intraday electricity market,
but our method is directly transferable to other European electricity markets.
While we are able to show that modelling the dependence structure improves the forecasting performance, our
methods can surely be improved and our results offer a multitude of further research areas: First, a further
investigation of the dependency structure seems worthwhile. However, the improved modelling of the correlation
structure is dependent on having a suitable probabilistic marginal model at hand. We note that the proposed
mixture of Johnson’s S distribution still does not provide a perfect fit and struggles to cope with periods of
U
extreme volatility. Hence, the modelling of the price distribution is an important field for further research. Third,
weprovidenewevidenceontheimpactofthesingleintradaycoupling(SIDC)onthepricedistributionandtrading
activity. As the SIDC system is dynamically changing and little researched, this might be an interesting direction
for further research into the micro-structure of intraday electricity markets. The literature on intraday markets is
still scarce compared to the fast growth of renewable energy sources and intraday electricity markets.
References
[1] M. Abadi, P. Barham, J. Chen, Z. Chen, A. Davis, J. Dean, M. Devin, S. Ghemawat, G. Irving, M. Isard,
etal. Tensorflow: asystemforlarge-scalemachinelearning. InProceedings of the 12th USENIX Symposium on
Operating Systems Design and Implementation (OSDI ’16), volume 16, pages 265–283. Savannah, GA, USA,
2016.
[2] T.Akiba,S.Sano,T.Yanase,T.Ohta,andM.Koyama. Optuna: Anext-generationhyperparameteroptimiza-
tion framework. In Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery
and Data Mining, 2019.
22

[3] J. R. Andrade, J. Filipe, M. Reis, and R. J. Bessa. Probabilistic price forecasting for day-ahead and intraday
| markets: | Beyond the statistical | model. | Sustainability, | 9(11):1990, | 2017. |
| -------- | ---------------------- | ------ | --------------- | ----------- | ----- |
[4] Y. Bengio. Practical recommendations for gradient-based training of deep architectures. Neural Networks:
| Tricks of | the Trade: Second | Edition, pages | 437–478, | 2012. |     |
| --------- | ----------------- | -------------- | -------- | ----- | --- |
[5] J. Berrisch, S. Pappert, F. Ziel, and A. Arsova. Modeling volatility and dependence of european carbon and
| energy prices. | Finance Research | Letters, | 52:103503, | 2023. |     |
| -------------- | ---------------- | -------- | ---------- | ----- | --- |
[6] I.Boukas,D.Ernst,T.Th´eate,A.Bolland,A.Huynen,M.Buchwald,C.Wynants,andB.Corn´elusse. Adeep
reinforcement learning framework for continuous intraday market bidding. Machine Learning, 110:2335–2387,
2021.
[7] R.CarmonaandX.Yang. Glassomodelforelectricloadandwindpowerandmontecarloscenariogeneration.
| arXiv preprint | arXiv:2111.14628, | 2021. |     |     |     |
| -------------- | ----------------- | ----- | --- | --- | --- |
[8] R. Carmona and X. Yang. Joint stochastic model for electric load, solar and wind power at asset level and
| monte carlo | scenario generation. | arXiv | preprint | arXiv:2209.13497, | 2022. |
| ----------- | -------------------- | ----- | -------- | ----------------- | ----- |
[9] E. Cramer, D. Witthaut, A. Mitsos, and M. Dahmen. Multivariate probabilistic forecasting of intraday elec-
tricity prices using normalizing flows. arXiv preprint arXiv:2205.13826, 2022.
[10] D. A. Dickey and W. A. Fuller. Distribution of the estimators for autoregressive time series with a unit root.
| Journal | of the American | statistical association, |     | 74(366a):427–431, | 1979. |
| ------- | --------------- | ------------------------ | --- | ----------------- | ----- |
[11] F.X.Diebold. Comparingpredictiveaccuracy,twentyyearslater: Apersonalperspectiveontheuseandabuse
of diebold–mariano tests. Journal of Business & Economic Statistics, 33(1):1–1, 2015.
[12] F. X. Diebold and R. S. Mariano. Comparing predictive accuracy. Journal of Business & economic statistics,
| 20(1):134–144, | 2002. |     |     |     |     |
| -------------- | ----- | --- | --- | --- | --- |
[13] J. V. Dillon, I. Langmore, D. Tran, E. Brevdo, S. Vasudevan, D. Moore, B. Patton, A. Alemi, M. Hoffman,
and R. A. Saurous. Tensorflow distributions. arXiv preprint arXiv:1711.10604, 2017.
[14] ENTSO-E. Single Intraday Coupling (SIDC). https://www.entsoe.eu/network_codes/cacm/
| implementation/sidc/#future-development, |     |     |     | 2023. Accessed: | 2023-06-02. |
| ---------------------------------------- | --- | --- | --- | --------------- | ----------- |
[15] EPEX Spot. Trading on EPEX Spot. Technical report, EPEX Spot SE, 2021.
[16] O. P. Faugeras. Inference for copula modeling of discrete data: a cautionary tale and some facts. Dependence
Modeling,
|     | 5(1):121–132, | 2017. |     |     |     |
| --- | ------------- | ----- | --- | --- | --- |
[17] E. Finhold, C. G¨artner, R. Grindel, T. Heller, N. Leith¨auser, E. R¨oger, and F. Schirra. Optimizing the
marketing of flexibility for avirtual battery in day-ahead and balancingmarkets: A rolling horizon case study.
| arXiv preprint | arXiv:2303.10025, | 2023. |     |            |           |
| -------------- | ----------------- | ----- | --- | ---------- | --------- |
|                |                   |       |     | Dependence | Modeling, |
[18] G. Geenens. Copula modeling for discrete random vectors. 8(1):417–440, 2020.
[19] T. Gneiting and A. E. Raftery. Strictly proper scoring rules, prediction, and estimation. Journal of the
| American | statistical Association, |                   |     |       |     |
| -------- | ------------------------ | ----------------- | --- | ----- | --- |
|          |                          | 102(477):359–378, |     | 2007. |     |
[20] S.HirschandF.Ziel. Simulation-basedforecastingforintradaypowermarkets: Modellingfundamentaldrivers
|     |     |     |     | The Energy | Journal. Accepted., |
| --- | --- | --- | --- | ---------- | ------------------- |
for location, shape and scale of the price distribution. 2023+.
23

Energies,
[21] T.JankeandF.Steinke. Forecastingthepricedistributionofcontinuousintradayelectricitytrading.
| 12(22):4262, | 2019. |     |     |     |     |     |     |     |
| ------------ | ----- | --- | --- | --- | --- | --- | --- | --- |
[22] C. Kath. Modeling intraday markets under the new advances of the cross-border intraday project (xbid):
| Evidence | from the | german | intraday |     | market. | Energies, | 12(22):4339, | 2019. |
| -------- | -------- | ------ | -------- | --- | ------- | --------- | ------------ | ----- |
[23] C. Kath and F. Ziel. Conformal prediction interval estimation and applications to day-ahead and intraday
| power markets. |     | International |     | Journal | of Forecasting, |     | 37(2):777–799, | 2021. |
| -------------- | --- | ------------- | --- | ------- | --------------- | --- | -------------- | ----- |
[24] R. Kiesel and F. Paraschiv. Econometric analysis of 15-minute intraday electricity prices. Energy Economics,
| 64:77–90, | 2017. |     |     |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
[25] M. Kremer, R. Kiesel, and F. Paraschiv. An econometric model for intraday electricity trading. Philosophical
| Transactions | of  | the Royal | Society | A,  | 379(2202):20190624, |     | 2021. |     |
| ------------ | --- | --------- | ------- | --- | ------------------- | --- | ----- | --- |
[26] S. Kulakov and F. Ziel. The impact of renewable energy forecasts on intraday electricity prices. Economics of
| Energy | & Environmental |     | Policy, | 10(1), | 2021. |     |     |     |
| ------ | --------------- | --- | ------- | ------ | ----- | --- | --- | --- |
[27] N. L¨ohndorf and D. Wozabal. The value of coordination in multimarket bidding of grid energy storage.
| Operations | Research, |     | 71(1):1–22, | 2023. |     |     |     |     |
| ---------- | --------- | --- | ----------- | ----- | --- | --- | --- | --- |
[28] H. Manner, F. A. Fard, A. Pourkhanali, and L. Tafakori. Forecasting the joint distribution of australian
electricity prices using dynamic vine copulae. Energy Economics, 78:143–164, 2019.
[29] G. Marcjasz, M. Narajewski, R. Weron, and F. Ziel. Distributional neural networks for electricity price
| forecasting. | arXiv | preprint | arXiv:2207.02832, |     |     | 2022. |     |     |
| ------------ | ----- | -------- | ----------------- | --- | --- | ----- | --- | --- |
[30] G. Marcjasz, B. Uniejewski, andR. Weron. Beatingthe na¨ıve—combininglasso with na¨ıve intraday electricity
| price forecasts. |     | Energies, | 13(7):1667, |     | 2020. |     |     |     |
| ---------------- | --- | --------- | ----------- | --- | ----- | --- | --- | --- |
[31] V. Nair and G. E. Hinton. Rectified linear units improve restricted boltzmann machines. In Proceedings of the
27th international conference on machine learning (ICML-10), pages 807–814, 2010.
[32] M. Narajewski and F. Ziel. Econometric modelling and forecasting of intraday electricity prices. Journal of
| Commodity | Markets, |     | 19:100107, | 2020. |     |     |     |     |
| --------- | -------- | --- | ---------- | ----- | --- | --- | --- | --- |
[33] M.NarajewskiandF.Ziel. Ensembleforecastingforintradayelectricityprices: Simulatingtrajectories. Applied
| Energy, | 279:115801, | 2020. |     |     |     |     |     |     |
| ------- | ----------- | ----- | --- | --- | --- | --- | --- | --- |
[34] NEMO Commitee. Single Intraday Coupling (XBID) Information Package. https://www.nemo-committee.
eu/assets/files/SIDC_Information%20Package_April%202021-99076f6ed5001c4d47442ae5cccebf30.
pdf.
[35] N. Nolzen, A. Ganter, N. Baumg¨artner, L. Leenders, and A. Bardow. Where to market flexibility? optimal
participation of industrial energy systems in balancing-power, day-ahead, and continuous intraday electricity
| markets. | arXiv | preprint | arXiv:2212.12507, |     |     | 2022. |     |     |
| -------- | ----- | -------- | ----------------- | --- | --- | ----- | --- | --- |
[36] J. Nowotarski and R. Weron. Recent advances in electricity price forecasting: A review of probabilistic fore-
| casting. | Renewable | and | Sustainable |     | Energy | Reviews, | 81:1548–1568, | 2018. |
| -------- | --------- | --- | ----------- | --- | ------ | -------- | ------------- | ----- |
[37] A. J. Patton. A review of copula models for economic time series. Journal of Multivariate Analysis, 110:4–18,
2012.
24

[38] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer,
R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher, M. Perrot, and E. Duchesnay.
Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12:2825–2830, 2011.
[39] A. Pircalabu and F. E. Benth. A regime-switching copula approach to modeling day-ahead prices in coupled
| electricity | markets. | Energy | Economics, | 68:283–302, |     | 2017. |     |
| ----------- | -------- | ------ | ---------- | ----------- | --- | ----- | --- |
[40] A. Pircalabu and J. Jung. A mixed c-vine copula model for hedging price and volumetric risk in wind power
| trading. | Quantitative | Finance, | 17(10):1583–1600, |     |     | 2017. |     |
| -------- | ------------ | -------- | ----------------- | --- | --- | ----- | --- |
[41] R. A. Rigby and D. M. Stasinopoulos. Generalized additive models for location, scale and shape. Journal of
the Royal Statistical Society: Series C (Applied Statistics), 54(3):507–554, 2005.
[42] T. Serafin, G. Marcjasz, and R. Weron. Trading on short-term path forecasts of intraday electricity prices.
| Energy Economics, |     | 112:106125, | 2022. |     |     |     |     |
| ----------------- | --- | ----------- | ----- | --- | --- | --- | --- |
[43] P. Shinde and M. Amelin. A literature review of intraday electricity markets and prices. 2019 IEEE Milan
| PowerTech, | pages | 1–6, 2019. |     |     |     |     |     |
| ---------- | ----- | ---------- | --- | --- | --- | --- | --- |
[44] A. Sklar. Random variables, joint distribution functions, and copulas. Kybernetika, 9(6):449–460, 1973.
[45] B. Sonnenschein and F. Ziel. Probabilistic intraday wastewater treatment plant inflow forecast utilizing rain
| forecast | data and | sewer | network sensor | data. | Authorea | Preprints, | 2022. |
| -------- | -------- | ----- | -------------- | ----- | -------- | ---------- | ----- |
[46] N.Srivastava,G.Hinton,A.Krizhevsky,I.Sutskever,andR.Salakhutdinov. Dropout: asimplewaytoprevent
neural networks from overfitting. The Journal of Machine Learning Research, 15(1):1929–1958, 2014.
[47] J. Tastu, P. Pinson, and H. Madsen. Space-time trajectories of wind power generation: Parametrized preci-
sion matrices under a gaussian copula approach. In Modeling and stochastic learning for forecasting in high
| dimensions, | pages | 267–296. | Springer, | 2015. |     |     |     |
| ----------- | ----- | -------- | --------- | ----- | --- | --- | --- |
[48] B.Uniejewski,G.Marcjasz,andR.Weron. Understandingintradayelectricitymarkets: Variableselectionand
very short-term price forecasting using lasso. International Journal of Forecasting, 35(4):1533–1547, 2019.
[49] J. Viehmann. State of the german short-term power market. Zeitschrift fu¨r Energiewirtschaft, 41(2):87–103,
2017.
[50] F. Ziel. Modeling the impact of wind and solar power forecasting errors on intraday electricity prices. In 2017
14th International Conference on the European Energy Market (EEM), pages 1–5. IEEE, 2017.
Interna-
[51] F. Ziel. M5 competition uncertainty: Overdispersion, distributional forecasting, gamlss, and beyond.
| tional Journal | of  | Forecasting, | 38(4):1546–1554, |     |     | 2022. |     |
| -------------- | --- | ------------ | ---------------- | --- | --- | ----- | --- |
arXiv
[52] F. Ziel and K. Berk. Multivariate forecasting evaluation: On sensitive and strictly proper scoring rules.
| preprint | arXiv:1910.07325, |     | 2019. |     |     |     |     |
| -------- | ----------------- | --- | ----- | --- | --- | --- | --- |
25

1.2
1.0
0.8
0.6
0.4
0.2
0.0
ytisneD
Training Pseudo-Uniform for 2022-01 Training Pseudo-Uniform for 2022-02 Training Pseudo-Uniform for 2022-03
1.2
1.0
0.8
0.6
0.4
0.2
0.0
ytisneD
Training Pseudo-Uniform for 2022-04 Training Pseudo-Uniform for 2022-05 Training Pseudo-Uniform for 2022-06
1.2
1.0
0.8
0.6
0.4
0.2
0.0
ytisneD
Training Pseudo-Uniform for 2022-07 Training Pseudo-Uniform for 2022-08 Training Pseudo-Uniform for 2022-09
1.2
1.0
0.8
0.6
0.4
0.2
0.0
0.0 0.2 0.4 0.6 0.8 1.0
Pseudo-Uniform Bins
ytisneD
Training Pseudo-Uniform for 2022-10 Training Pseudo-Uniform for 2022-11 Training Pseudo-Uniform for 2022-12
0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0
Pseudo-Uniform Bins Pseudo-Uniform Bins
Figure 14: Diagnostic plots for the in-sample pseudo-uniform observations after each refit during the forecasting
study.
26

1.0
0.8
0.6
0.4
0.2
0.0
4 6 8
negative log-likelihood
etar_tuopord_smarap
105 102 101 104 106 104 102 100 102 105 102 101 104 106 104 102 100 102 105 104 103 102
params_l1_loc params_l1_scale params_l1_skew params_l1_tail params_learning_rate
104
102
100
102
104
106
0.00 0.25 0.50 0.75 1.00
params_dropout_rate
col_1l_smarap
4 6 8 106 104 102 100 102 105 102 101 104 106 104 102 100 102 105 104 103 102
negative log-likelihood params_l1_scale params_l1_skew params_l1_tail params_learning_rate
102
100
102
104
106
0.00 0.25 0.50 0.75 1.00
params_dropout_rate
elacs_1l_smarap
105 102 101 104 4 6 8 105 102 101 104 106 104 102 100 102 105 104 103 102
params_l1_loc negative log-likelihood params_l1_skew params_l1_tail params_learning_rate
104
102
100
102
104
106
0.00 0.25 0.50 0.75 1.00
params_dropout_rate
weks_1l_smarap
105 102 101 104 106 104 102 100 102 4 6 8 106 104 102 100 102 105 104 103 102
params_l1_loc params_l1_scale negative log-likelihood params_l1_tail params_learning_rate
102
100
102
104
106
0.00 0.25 0.50 0.75 1.00
params_dropout_rate
liat_1l_smarap
105 102 101 104 106 104 102 100 102 105 102 101 104 4 6 8 105 104 103 102
params_l1_loc params_l1_scale params_l1_skew negative log-likelihood params_learning_rate
102
103
104
105
0.00 0.25 0.50 0.75 1.00
params_dropout_rate
etar_gninrael_smarap
105 102 101 104 106 104 102 100 102 105 102 101 104 106 104 102 100 102 4 6 8
params_l1_loc params_l1_scale params_l1_skew params_l1_tail negative log-likelihood
Figure 15: Diagnostic plots for our hyperparameter tuning using the optuna framework. We show the bivariate
distribution of the explored hyperparameters and the scatter plot of each hyperparameter towards the negative
log-likelihood on the diagonal. Color represents increasing the trial number from dark to yellow. The red dot
represents the best trial.
27