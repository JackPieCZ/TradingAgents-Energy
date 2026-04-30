| Simulation-based |             |       | Forecasting |         | for Intraday |           | Power | Markets: |     |
| ---------------- | ----------- | ----- | ----------- | ------- | ------------ | --------- | ----- | -------- | --- |
| Modelling        | Fundamental |       |             | Drivers | for          | Location, |       | Shape    | and |
|                  |             | Scale | of the      | Price   | Distribution |           |       |          |     |
|                  |             | Simon | Hirsch1,2   |         | Florian      | Ziel1     |       |          |     |
2202 voN 32  ]TS.nif-q[  1v20031.1122:viXra
|     | 1House | of Energy | Markets    | and Finance, | University   | of Duisburg-Essen |     |     |     |
| --- | ------ | --------- | ---------- | ------------ | ------------ | ----------------- | --- | --- | --- |
|     |        |           | 2Statkraft |              | Trading GmbH |                   |     |     |     |
|     |        |           |            | November     | 24, 2022     |                   |     |     |     |
Working Paper
Abstract: During the last years, European intraday power markets have gained importance
for balancing forecast errors due to the rising volumes of intermittent renewable generation.
However, compared to day-ahead markets, the drivers for the intraday price process are still
sparsely researched. In this paper, we propose a modelling strategy for the location, shape
and scale parameters of the return distribution in intraday markets, based on fundamental
variables. We consider wind and solar forecasts and their intraday updates, outages, price
information and a novel measure for the shape of the merit-order, derived from spot auction
curves as explanatory variables. We validate our modelling by simulating price paths and
compare the probabilistic forecasting performance of our model to benchmark models in a
forecasting study for the German market. The approach yields significant improvements in the
forecasting performance, especially in the tails of the distribution. At the same time, we are
abletoderivethecontributionofthedrivingvariables. Wefindthat, apartfromthefirstlagof
the price changes, none of our fundamental variables have explanatory power for the expected
value of the intraday returns. This implies weak-form market efficiency as renewable forecast
changesandoutageinformationseemstobepricedinbythemarket. Wefindthatthevolatility
is driven by the merit-order regime, the time to delivery and the closure of cross-border order
books. The tail of the distribution is mainly influenced by past price differences and trading
activity. OurapproachisdirectlytransferabletoothercontinuousintradaymarketsinEurope.
Keywords: electricity price forecasting, volatility forecasting, intraday energy market, auction curves,
gamlss
1. Introduction
Intraday power markets gained significant importance throughout the past few years, most visible in
sharply increased trading volumes. In the European power market structure, they provide traders, asset
1

ownersandmarketersofintermittentRenewableEnergySources(RES)theopportunitytobalanceforecast
errors arising after the day-ahead auction until five minutes before the beginning of the delivery period
(Koch and Hirth, 2019). Increasingly, this balancing action is taken over by algorithmic trading strategies,
for which reliable short-term price and volatility forecasts are necessary. At the same time, our results
shed light on the influence of idiosyncratic features of intraday markets such as Single IntraDay Coupling
(SIDC) on the price process and are thus valuable for policy makers concerned with short-term markets.
The recent and still sparse literature on probabilistic forecasting in intraday markets (Janke and Steinke,
2019, Narajewski and Ziel, 2020b, Uniejewski et al., 2019) and the markets’ driving fundamentals has, so
far, focussed on modelling the impact of renewable forecast (Balardy, 2022, Gürtler and Paulsen, 2018,
Kath, 2019, Pape et al., 2016, Ziel, 2017) and forecast errors (Kulakov and Ziel, 2020, Kuppelwieser and
Wozabal, 2021, Ziel, 2017). A different strand of literature emerged around modelling of the merit-order
effect for price changes and price elasticity (Balardy, 2022, Kiesel and Paraschiv, 2017, Kremer et al.,
2020, 2021, Kulakov and Ziel, 2019). To the best knowledge of the authors, only Narajewski and Ziel
(2020a) and Baule and Naumann (2021) focus on modelling the volatility in intraday markets. This paper
aims to generalize the above research by investigating the fundamental drivers of the location, scale and
shape parameters of the intraday price return distribution. We use the Generalized Additive Models for
Location, Shape and Scale (GAMLSS) framework to model the distribution moments in a parametric and
explainable fashion. Our contribution is thus two-fold: We are able to significantly improve forecasting
performance compared to benchmarks and qualitatively analyse the impact of fundamental drivers for
the distribution moments. While this paper focuses on the German intraday market, our methodology is
transferable to any continuous intraday market such as France, Great Britain, Spain or Turkey.
This paper builds on the work of Narajewski and Ziel (2020a) to develop a simulation-based probabilistic
forecasting model for the path of the five-minute-volume-weighted price P between 185 and 30 minutes
before delivery. Instead of directly modelling the price P as it is common in day-ahead forecasting and
is done in other forecasting studies on the intraday market (Janke and Steinke, 2019, Uniejewski et al.,
2019), the first differences ∆P will be modelled. The path of P is thus the cumulative sum of the initial
price P and all price differences in the forecasting period. Following the suggestions of Narajewski and
0
Ziel (2020a), we assume the first differences ∆P follow a mixture distribution of the Dirac distribution δ
0
with an atom at 0 and a continuous distribution F. In Narajewski and Ziel (2020a), the latter is assumed
to be t-distributed without any detailed justification, except the observation that ∆P tends to be heavy
tailed. This manuscript extends the approach in four dimensions:
1. We study in more detail the distribution assumption for F. We investigate more distributions,
including those with potential skewness. The distribution for F is selected from the skew-t and
the Johnson’s S . These distributions have been used successfully to model asset returns or and
U
have been applied to forecasting in energy markets (Bunn et al., 2018, Gianfreda and Bunn, 2018,
Serinaldi, 2011).
2. One natural starting point to improve the models is adding intra-daily updated forecasts for wind
and solar generation to reflect the information set available to market participants better. High
forecast updates indicate that market participants with RES assets need to solve larger positions
in the intraday market. Capturing this effect aims at improving the modelling of the location and
volatility of ∆P. The findings will be discussed in the light of the market efficiency hypothesis
indicated by Kuppelwieser and Wozabal (2021), Narajewski and Ziel (2020b). Additionally, the
variance of individual forecast updates is used to model the volatility of ∆P. This is motivated
by the assumption that uncertainty regarding the weather situations is transmitted to the price
formation.
2

3. A measure for the intraday price elasticity is derived from the day-ahead auction curves, which are
used as proxy for the intraday merit-order and included in the modelling of the volatility (Kulakov
and Ziel, 2019, 2020). This is motivated by Kremer et al. (2020, 2021), who show that the price
impact of forecast errors depends on whether the market is in a flat or steep merit-order ’regime’
and the work of Balardy (2022), who shows that the intraday bid-ask spread can be explained by
the price elasticity derived from the day-ahead auction curves. Additionally, the predictive power of
the day-ahead level of outages and the change in planned and unplanned outages between day-ahead
and intraday is tested.
4. As in Narajewski and Ziel (2020a), we utilize the GAMLSS framework for parameter estimation.
However, we allow for a more flexible parameter training approach utilizing an automatic variable
selection for all distribution moments by utilising the adaptive Least Absolute Shrinkage and Selec-
tion Operator (LASSO) estimation technique for the GAMLSS model as well. This procedure was
similarly used in Ziel (2021) in the context of the M5 forecasting competition.
The extended models are tested in a forecasting study and compared to the benchmark models. We
evaluate the probabilistic forecasting performance by utilizing established probabilistic scoring rules and
calibration measures. Statistical significance is evaluated by the widely used Diebold-Mariano (DM)-test
(Diebold and Mariano, 2002, Narajewski and Ziel, 2020a, Nowotarski and Weron, 2018, Ziel and Berk,
2019). In our forecasting study, the GAMLSS-based model assuming Johnson’s S significantly outper-
U
forms all proposed benchmark models as well as the GAMLSS-based model assuming the popular skew-t
distribution. The GAMLSS-based model assuming the skew-t distribution exhibits stark sensitivity to-
wards outliers. Qualitatively, our results indicate that price changes ∆P in the intraday market are
influenced by the first lag, while other explanatory variables have little predictive power for the expected
value of ∆P. This result supports the notion of weak-form efficient markets already indicated by Kup-
pelwieser and Wozabal (2021), Narajewski and Ziel (2020b). We find evidence for a merit-order effect
in the volatility and kurtosis of the distribution ∆P. A steeper merit-order implies higher volatility and
heavier tails. Additionally, the volatility rises with decreasing time to delivery and with the gate closure
of XBID/SIDC, while kurtosis is more driven by trading-related variables such as lagged absolute price
differences. We find that none of the included explanatory variables has predictive power for the skewness
of the distribution.
The presented models and methodology are also of interest to practitioners in intraday markets. Path-
based forecasts allow to price short-term asset optionality using Asian option valuation. Additionally,
the explicit modelling of the volatility provides a starting point to introduce time-varying volatility to
mathematical finance models for market making and position solving (Aïd et al., 2016, Glas et al., 2020,
Kath and Ziel, 2020, von Luckner et al., 2017).
The remainder of this paper is structured as follows: Section 2 gives a short introduction to the structure
of the German short-term power markets. Section 3 presents the data preparation of the intraday trade
data, theforecastandoutagedatasetsandthetransformationoftheday-aheadauctioncurvesandrelated
assumptions. Also, some exploratory data analysis is carried out in this Section. Section 4 introduces the
used models. The forecasting study design and scoring rules are discussed in Section 5. Finally, Sections
6 and 7 present the results and conclude this paper.
3

Figure 1.: Daily procedure in the German short-term power markets (based on EPEX SPOT SE, 2018,
|     | Narajewski  |                  | and | Ziel,          | 2020a, Nordpool | SE,   | 2018).          |          |        |        |                |
| --- | ----------- | ---------------- | --- | -------------- | --------------- | ----- | --------------- | -------- | ------ | ------ | -------------- |
|     | Day-ahead   |                  |     | HourlyIntraday |                 | SIDC  |                 |          | SIDC   |        |                |
|     | SpotAuction |                  |     | opens          |                 | opens |                 |          | closes |        | Deliveryb(d,s) |
|     |             | FirstSpotAuction |     |                |                 |       | StartSimulation |          |        | Market |                |
|     |             | ResultsPd,s      |     |                |                 |       |                 | withPd,s |        | closes |                |
|     |             |                  |     | DA             |                 |       |                 | ID,0     |        |        |                |
Controlzones
close
|              |     | d−1,  | d−1,  | d−1,   |       | d−1,   |     | d,    | d,   | d,   | d, d, s |
| ------------ | --- | ----- | ----- | ------ | ----- | ------ | --- | ----- | ---- | ---- | ------- |
|              |     | 12.00 | 12.45 | 15.00  |       | 18.00  |     | s−185 | s−60 | s−30 | s−5     |
|              |     |       |       |        |       |        |     | min   | min  | min  | min     |
| 2. Structure |     | of    | the   | German | Power | Market |     |       |      |      |         |
This section briefly introduces the relevant structure of the German power market. As we work with data
from the day-ahead auction and the intraday market, the description focuses on these markets. Generally,
denote the delivery day as d and the delivery hour as s for s = 0,...,S and S = 23. Times are usually
expressed in local time unless otherwise noted.1 Electric power markets generally follow the structure of
a forward market, where different delivery periods in the future can be traded almost up to the start of
actual physical delivery. Figure 1 shows the time line of the German short-term markets, for more details
see Viehmann (2017). Let us generally note here that we place indices referring to the delivery periods
d,s as superscript, while placing indices relating to the time where the price is determined as subscript.
| The | same holds | for | other | variables | as e.g. | production | forecasts. |     |     |     |     |
| --- | ---------- | --- | ----- | --------- | ------- | ---------- | ---------- | --- | --- | --- | --- |
The spot market is organized as a pay-as-cleared auction. The order book closes on at 12:00 and
d−1
first auction results are published around 12:42 on d−1. Official results shall be published at latest at
14:00 on d−1. From the bids submitted by the market participants, EPEX Spot calculates aggregated
supply and demand curves for each delivery period. The intersection between supply and demand curves
is the market clearing price Pd,s. Additionally to normal bids, market participants can submit special bids
DA
such as block bids spanning more than one delivery period and linked bids, where execution is linked to
neighbouring bids. The day-ahead spot price also serves as reference price for cascading financial futures.
EPEX SPOT SE (2020c) publishes aggregate curves together with the official market results. The lower
price level is set to -500 EUR/MWh, the upper level is set to 3000 EUR/MWh.
The intraday market is structured as continuous pay-as-bid auction similar to financial markets. However,
contrary to equity or currency markets, the individual trading sessions of the intraday electricity markets
are not part of a larger process, as the intraday trading session ends with the physical delivery of power.
Hence, trading sessions for the same delivery period on different delivery days might be driven by funda-
mentally different circumstances and need to be viewed separately. Trading starts at 15:00, 15:30, 16:00
on d−1 for hourly, half-hourly and quarter-hourly products with delivery on day d. At 18:00 on d−1,
cross-border trading within the SIDC system, formerly known as Cross Border Intraday (XBID), starts
in Germany, Denmark, Netherlands, Norway and Poland.2 At 22:00 on d−1, the remaining countries of
the core market area follow. Here, the intraday order books of all participating countries are shared and
1) Central European Time (CET) respectively Central European Summer Time (CEST) for Germany.
2) For the sake of consistency, both the XBID and SIDC are referred to as SIDC throughout this paper.
4

orders can be matched internationally as long as sufficient transmission capacity is available. For each
product, the cross-border shared order books close one hour before delivery. SIDC went live on June 18,
2018 (Nordpool SE, 2018). 30 minutes before delivery, the Germany-wide order book closes and trading
resumes in local (control zone) products up to five minutes before delivery. Note that all open delivery
periods are traded in parallel. The market price limits are at ±9999 EUR/MWh. The smallest possible
price tick changed multiple times throughout the last few years and is currently set to 0.01 EUR/MWh.
The smallest possible volume tick is 0.1 MW (EPEX SPOT SE, 2018, 2020b, Viehmann, 2017).
3. Data and Exploratory Analysis
3.1. Intraday Trade Data
On the intraday market, trading happens continuously. Hence, the transactions are irregularly spaced and
need to be aggregated. The following paragraphs and Figure 2 give a brief overview of the aggregation. A
detailed description can be found in Appendix A. Trade data is obtained from EPEX SPOT SE (2020a).
The data consists of all hourly trades on the continuous intraday market between January 1st, 2016 and
July 31st, 2020.
For each delivery period d,s we aggregate all trades on an equidistant 5-minute grid by taking the volume-
weighted average price within each bucket, denoted by Pd,s , where t denotes the 5-minute interval (see
ID,t
panel 2in Figure 2). We then takefirst differences∆Pd,s = Pd,s −Pd,s (see panel3). Lastly, wedefine
ID,t ID,t ID,t−1
a boolean variable αd,s, which takes the value 1 if there has been at least one trade within the 5-minute
t
interval (see panel 4). As the trading sessions in the intraday market are of varying length for the different
delivery periods and our simulation concerns the last 185 minutes of trading for each product, we define
t relative to the start of the physical delivery. t = 1 denotes the first 5-minute interval in the simulation
window, thus 185 to 180 minutes before the start of physical delivery and t = 31 = T denotes the last
5-minute interval in the simulation window, 35 to 30 minutes before the start of physical delivery. Similar
aggregation methods have been used by Narajewski and Ziel (2020a,b) and Serafin et al. (2022).
Figure3showstherelationshipbetweentheshareofno-tradeevents,i.e. 5-minuteintervalswhereαd,s = 0,
t
relative to the time to delivery on the initial training set. With decreasing time to delivery, the probability
of no-trade events decreases in a non-linear fashion. For periods close to 30 minutes to delivery, the share
of no-trade events in the initial training data set is close to 0, while further away from delivery, there are
more periods without trades. For products with delivery in the peak hours, there are less no-trade events
at the beginning of the ID period already. Additionally, Table 1 presents summary statistics for α and
3 t
∆Pd,s for all 5-minute intervals with at least one trade, grouped by year. The share of 5-minute intervals
ID,t
where α = 1, i.e. at least one trade happens happens, increases throughout the years. It is almost 1
t
from 2018 onwards, implying that there are barely any periods without trades. Accordingly, the number
of observations for α and ∆Pd,s | α = 1 converge. We can thus identify two levels of time-varying
t ID,t t
behaviour of αd,s, first across the multiple years of the data set, but also second within each trading
t
session. While we explicitly model the latter, the first will be coped with due to the set-up of a rolling
window forecasting study.
5

40.0
37.5
35.0
32.5
30.0
27.5
25.0
360 330 300 270 240 210 180 150 120 90 60 30
]hWM/RUE[
ecirP
dedarT
20 40 60 80
Traded Volume [MW]
ID3-Timeframe
40.0
37.5
35.0
32.5
30.0
27.5
25.0
360 330 300 270 240 210 180 150 120 90 60 30
]hWM/RUE[
P
5-minute VWAP
ID3-Timeframe
3
2
1
0
1
2
3
360 330 300 270 240 210 180 150 120 90 60 30
]hWM/RUE[
P
First Difference of the the 5-minute VWAP
ID3-Timeframe
1
0
360 330 300 270 240 210 180 150 120 90 60 30
Time
t
t
ID3-Timeframe
Figure 2.: Overview of the data preparation. The first figure shows the raw trade data. The color refers
to the traded volume. Below, the 5-minute Volume-Weighted Average Price (VWAP) P and
their first differences ∆Pd,s are shown. Lastly, αd,s is shown. The plots show the data for d =
ID,t t
January 1st, 2016 for delivery period s = 12 in the last 6 hours to delivery.
6

0.7
S
h
a 0.6
re 0.7
o f
n
0.5
0.6
o
-tra 0.4
0.5
d e 0.3
e v e 0.2 0.4
n
ts
0.1
0.3
0.0 0.2
T
im180 0.1
e 160
to
d 140 0.0
e 120
liv
e 100
ry
[M
in u t
8
e s
0
] 60 40 0 2 4 6 8 1 P 0 rodu 1 c 2 t [s 1 ] 4 16 18 20 22
Figure 3.: Share of no-trade events over time to delivery and delivery hour for the initial one-year training
set from January 1st to December 31st, 2016. Colour corresponds to the z-axis. Low values
correspond to few no-trade events, high values correspond to many no-trade events.
The mean and median values of ∆Pd,s are close to 0 across all years in the dataset. However the standard
ID,t
deviation is rather high and the extreme minima and maxima already hint at a leptokurtic distribution of
∆Pd,s . Theminimaandmaximaincrease throughoutthedataset, whilethe5%respectively95%and the
ID,t
10%respectively90%quantilesareroughlyconstant. Especiallyfor2020,theminimaandmaximaofmore
than 2000 respectively less than -2000 EUR/MWh are noteworthy. Driven by these larger outliers in 2020,
the standard deviation of ∆Pd,s rises fourfold between 2019 and 2020, while staying roughly constant
ID,t
before. The more robust dispersion measures median absolute deviation (MAD) and the interquartile
range (IQR) support this notion.
Figure 5 plots histograms for ∆Pd,s in the initial training set in the hours s ∈ {4,12,20} exemplary.
ID,t
These delivery hours represent the typical night, noon and afternoon peak load hours. The first plot
focuses on the general shape of the distribution as well as the relation between intervals with and without
trades. The center bar shows the relative weight of 5-minute intervals without trades (i.e. αd,s = 0) and
t
5-minute intervals with at least one trade (i.e. αd,s = 1), but small or no price changes. As visible already
t
in Figure 3, the share of 5-minute intervals with αd,s = 0 decreases strongly for delivery hours after 8.
t
In the second Figure, the tails of the distribution are shown together with fitted normal, student-t, and
Johnson’s S distributions. Additionally, Figure 6 (a) plots the pearson autocorrelation coefficients r for
U
∆Pd,s foreachtradingsessionforthefirstlag. Colourintensitycorrespondstothecoefficientsize. Forthe
ID,t
first lag, slight positive autocorrelation is present for the morning hours, while some negative correlation
is visible for noon and evening hours. Figure 6 (b) shows the according p-values for the test statistic
√ √
r· n−2/ 1−r2 where n is the number of 5-minute intervals in the trading session. We find that for
around one-fifth of all trading sessions, the lag 1 autocorrelation coefficient is significant at the 10%-level
and for only 15% of all trading sesions, the lag 1 autocorrelation is significant at the 5%-level. For lags 2
and 3, we find even less significant autocorrelation (see Figures 19 and 20 in Appendix C).
7

Table 1.: Summary statistics for αd,s and ∆Pd,s for 185 to 30 minutes before delivery. denotes the
Q
|     | t   | ID,t |     |     | τ   |
| --- | --- | ---- | --- | --- | --- |
empirical τ ·100%-quantile. Note that all ∆Pd,s | αd,s = 0 are 0 by definition.
ID,t t
|          |           | 2016 2017     | 2018 2019     | 2020   |     |
| -------- | --------- | ------------- | ------------- | ------ | --- |
| α t      | Count (n) | 257424 252960 | 268584 267096 | 158472 |     |
|          | Mean (µ)  | 0.82 0.87     | 0.95 0.98     | 0.98   |     |
|          | Std. (σ)  | 0.39 0.34     | 0.23 0.14     | 0.15   |     |
| ∆P |α =1 | Count (n) | 209995 219258 | 253931 261721 | 154597 |     |
t t
|     | Mean (µ) | 0.02 0.02      | -0.00 -0.00     | -0.01    |     |
| --- | -------- | -------------- | --------------- | -------- | --- |
|     | Std. (σ) | 1.57 2.06      | 1.94 2.15       | 8.13     |     |
|     | MAD      | 0.94 1.11      | 1.03 0.91       | 1.10     |     |
|     | IQR      | 1.17 1.33      | 1.23 1.01       | 1.07     |     |
|     | Skewness | 1.07 1.94      | 8.02 12.25      | 0.65     |     |
|     | Kurtosis | 131.50 322.14  | 902.99 2544.57  | 64968.44 |     |
|     | Min      | -76.38 -127.70 | -108.22 -214.16 | -2161.80 |     |
|     | Q        | -1.40 -1.61    | -1.52 -1.29     | -1.45    |     |
0.10
|     | Q   | -0.57 -0.65 | -0.62 -0.51 | -0.54 |     |
| --- | --- | ----------- | ----------- | ----- | --- |
0.25
|     | Q   | 0.00 0.00 | 0.00 -0.01 | 0.00 |     |
| --- | --- | --------- | ---------- | ---- | --- |
0.50
|     | Q   | 0.60 0.68 | 0.61 0.50 | 0.53 |     |
| --- | --- | --------- | --------- | ---- | --- |
0.75
|     | Q 0.90 | 1.43 1.64    | 1.49 1.26     | 1.40    |     |
| --- | ------ | ------------ | ------------- | ------- | --- |
|     | Max    | 82.16 119.88 | 183.94 226.26 | 2164.23 |     |
5.0
S ta
4.5
n 5
d 4.0
a rd
3.5
 d
e
| v 3.0 |     |     |     |     | 4   |
| ----- | --- | --- | --- | --- | --- |
ia
tio 2.5
n
|   2.0 |     |     |     |     | 3   |
| ----- | --- | --- | --- | --- | --- |
(
P 1.5
)
1.0
2
0.5
T im
| 40  |     |     |     |     | 1   |
| --- | --- | --- | --- | --- | --- |
e  to 60
 D 80
e
liv 100
e 120
ry
 [M 1 4 0
22
| in 1 6 0 |     |                 | 16 18 20 |     |     |
| -------- | --- | --------------- | -------- | --- | --- |
| u        |     | 1 0 1 2 1 4     |          |     |     |
| t e 1 80 | 4 6 | 8 rodu c t [s ] |          |     |     |
| s ]      | 0 2 | P               |          |     |     |
Figure 4.: Volatility development over time to delivery and delivery hour for the initial training one-year
set from January 1st to December 31st, 2016. Colour corresponds to the z-axis. Note the
inverted y-axis (Time to delivery) compared to Figure 3 to ease visualisation.
8

Therelationshipbetweentherealizedvarianceandthetimetodeliveryintheinitialtrainingdataisshown
in Figure 4. The volatility increases slightly until 60 minutes before the start of the delivery and rises
sharply between 60 and 30 minutes before the start the delivery. Here, we note three levels of time-varying
behaviour: first, across the full data set, volatility is increasing. Second, within each day, the volatility
moves with the peak/off-peak hours. Third, within each trading session, volatility increases towards the
| end of | the trading | session. |     |     |     |     |     |
| ------ | ----------- | -------- | --- | --- | --- | --- | --- |
To analyse the stationarity properties of the differenced and un-differenced price series, we apply the
augmented Dickey-Fuller test to each simulation window individually and report aggregate results in
Table 2. For the majority of the trading windows, we find stationarity of the price differences and unit-
root behaviour in the prices. We note though, that due to the heteroskedasticity present in the individual
tradingwindows,theunderlyingassumptionsoftheADF-testmightbeviolated. Togetherwiththeresults
of Löhndorf and Wozabal (2022), who aggregate trades in the intraday market on a 1-hour grid and report
similar results for the ADF-test at the 10%-level, we conclude that the price changes in the intraday
| market | are stationary. |     |     |     |     |     |     |
| ------ | --------------- | --- | --- | --- | --- | --- | --- |
Table 2.: Aggregate results of the augmented Dickey-Fuller unit-root tests. Tests are applied to each
simulation window individually. The table reports the share of simulation windows where the
|     | test result | implies | stationarity, | i.e. rejection | of the | H of a unit root. |     |
| --- | ----------- | ------- | ------------- | -------------- | ------ | ----------------- | --- |
0
|     |     |          | Year         | 2016       | 2017  | 2018 2019   | 2020  |
| --- | --- | -------- | ------------ | ---------- | ----- | ----------- | ----- |
|     |     | Variable | Significance |            |       |             |       |
|     |     | ∆Pd,s    | α =          | 0.01 0.675 | 0.658 | 0.633 0.596 | 0.555 |
ID,t
|     |     |      | α = | 0.05 0.750 | 0.744 | 0.717 0.684 | 0.641 |
| --- | --- | ---- | --- | ---------- | ----- | ----------- | ----- |
|     |     | Pd,s | α = | 0.01 0.059 | 0.055 | 0.055 0.059 | 0.088 |
ID,t
|                 |     |           | α =         | 0.05 0.128 | 0.125 | 0.122 0.117 | 0.157 |
| --------------- | --- | --------- | ----------- | ---------- | ----- | ----------- | ----- |
| 3.2. Renewables |     | Forecasts | and Outages |            |       |             |       |
Intra-daily updated renewable production forecasts used in this paper are provided by Statkraft Markets
and generated by energy & meteo systems GmbH (2020). Day-ahead demand / system load forecasts are
obtained from ENTSO-E (2021). The forecasts have a 15-minute delivery period resolution and denote
the expected produced power by all assets of the respective technology in Germany in MW. Forecasts are
sampled to hourly frequency using a simple arithmetic average. A new update is available every hour.
The first forecast version is issued several days before the delivery day, the latest version usually after
the end of the delivery period due to ex-post updates. Let Wˆ d,s,Sˆd,s denote forecasts for wind and solar
|     |     |     |     |     |     | v v |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
production for delivery period d,s available at time v. Forecasts for demand are not updated as regularly,
hence intraday-updates are not considered in this paper. We denote demand forecasts as Dˆd,s. Note
DA
that the issuance time of a new forecast does not necessarily correspond to the timing of trades on the
v
continuous market or the 5-minute intervals used to aggregate these trades. For any forecasting study, it
is important to keep in mind the information set at the point of forecasting. The start of the simulation is
setto185minutesbeforethestartofthedeliveryperiod. Hence, forecastversionsandupdatescanonlybe
considered if they are available earlier than 185 minutes before the start of the delivery period.3 For each
3) Forexample,foraproductwithdeliveryonSeptember1st,12:00to13:00,allforecastversionsavailableuntilSeptember
1st, 8:55 can be used. For the product with delivery 13:00 to 14:00, all versions up to 9:55 can be used.
9

| 1.4       |             |        |        | =1  | 1.4       |     |             |        | =1  | 1.4       |             |        |        | =1  |
| --------- | ----------- | ------ | ------ | --- | --------- | --- | ----------- | ------ | --- | --------- | ----------- | ------ | ------ | --- |
|           |             |        |        | =0  |           |     |             |        | =0  |           |             |        |        | =0  |
| 1.2       |             |        |        |     | 1.2       |     |             |        |     | 1.2       |             |        |        |     |
| 1.0       |             |        |        |     | 1.0       |     |             |        |     | 1.0       |             |        |        |     |
| ycneuqerF |             |        |        |     | ycneuqerF |     |             |        |     | ycneuqerF |             |        |        |     |
| 0.8       |             |        |        |     | 0.8       |     |             |        |     | 0.8       |             |        |        |     |
| 0.6       |             |        |        |     | 0.6       |     |             |        |     | 0.6       |             |        |        |     |
| 0.4       |             |        |        |     | 0.4       |     |             |        |     | 0.4       |             |        |        |     |
| 0.2       |             |        |        |     | 0.2       |     |             |        |     | 0.2       |             |        |        |     |
| 0.0       |             |        |        |     | 0.0       |     |             |        |     | 0.0       |             |        |        |     |
|           | 4           | 2 0    | 2      | 4   |           | 4   | 2 0         | 2      | 4   |           | 4           | 2 0    | 2      | 4   |
|           |             | Pt d,s |        |     |           |     | Pt d,s      |        |     |           |             | Pt d,s |        |     |
| 0.025     |             |        |        |     | 0.025     |     |             |        |     | 0.025     |             |        |        |     |
|           | Johnsons SU |        | Normal |     |           |     | Johnsons SU | Normal |     |           | Johnsons SU |        | Normal |     |
0.020 Student-t d , s 0.020 Student-t d , s 0.020 Student-t d , s
| ycneuqerF |     |     | PI D , | t   | ycneuqerF |     |     | PI D , | t   | ycneuqerF |     |     | PI D , | t   |
| --------- | --- | --- | ------ | --- | --------- | --- | --- | ------ | --- | --------- | --- | --- | ------ | --- |
| 0.015     |     |     |        |     | 0.015     |     |     |        |     | 0.015     |     |     |        |     |
| 0.010     |     |     |        |     | 0.010     |     |     |        |     | 0.010     |     |     |        |     |
| 0.005     |     |     |        |     | 0.005     |     |     |        |     | 0.005     |     |     |        |     |
| 0.000     |     |     |        |     | 0.000     |     |     |        |     | 0.000     |     |     |        |     |
10.0 7.5 5.0 2.5 0.0 2.5 5.0 7.5 10.0 10.0 7.5 5.0 2.5 0.0 2.5 5.0 7.5 10.0 10.0 7.5 5.0 2.5 0.0 2.5 5.0 7.5 10.0
|     |          | PI d , s |     |     |     |     | PI d , s   |     |     |     |          | PI d , s |     |     |
| --- | -------- | -------- | --- | --- | --- | --- | ---------- | --- | --- | --- | -------- | -------- | --- | --- |
|     |          | D ,      | t   |     |     |     | D ,        | t   |     |     |          | D ,      | t   |     |
|     | (a) Hour | s=4.     |     |     |     | (b) | Hour s=12. |     |     |     | (c) Hour | s=20.    |     |     |
Figure 5.: Histograms of ∆Pd,s for in the initial one-year training set.
s = 4,12,20
ID,t
delivery period, two forecast versions deserve special attention: First, the latest forecast available before
12:00 on d−1, the deadline for submission of bids to the spot auction, is referred to as the day-ahead
forecast Wˆ d,s and Sˆd,s. Secondly, the newest forecast available before the start of the simulation, i.e. at
|     | DA  | DA  |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
which holds, is denoted as the intraday forecast Wˆ d,s and Sˆd,s.
|     | v ≥ b(d,s)−185 |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |                |     |     |     |     |     |     |     | ID  | ID  |     |     |     |     |
An initial analysis showed that individual forecast updates immediately before the start of the simulation
carries little predictive power for the whole simulation period of three hours. Therefore, the forecast
updates are aggregated. We consider two aggregated measures for forecast changes: first, the aggregated
change between the production forecasts at the day-ahead stage and the production forecasts at the start
of the simulation. Second, we employ the volatility of all forecast changes between the day-ahead stage
and the production forecasts at the start of the simulation. Let us generally define the change between
two forecast versions as ∆Wˆ d,s Wˆ d,s−Wˆ d,s with being the newer forecast.
|     |     |     | v ,v |     | =     |     |     | v   |     |           |      |     |     |     |
| --- | --- | --- | ---- | --- | ----- | --- | --- | --- | --- | --------- | ---- | --- | --- | --- |
|     |     |     | 1 2  |     | v1,v2 | v2  | v1  | 2   |     |           |      |     |     |     |
|     |     |     |      |     |       |     |     | ∆Wˆ | d,s | Wˆ d,s−Wˆ | d,s. |     |     |     |
• The day-ahead to simulation forecast update is defined as: = The symmetry
|     |     |     |     |     |     |     |     |     | DA,ID | ID  | DA  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
of the impact of forecast errors on ∆Pd,s is a disputed topic in the literature (Kremer et al., 2020,
ID,t
2021, Ziel, 2017) and has, so far, not been explored for the volatility of ∆Pd,s . To address this issue
ID,t
and test for possible asymmetric effects, ∆Wˆ d,s and ∆Sˆd,s are split in positive and negative
|     |     |     |     |     |     |     | DA,ID |     | DA,ID |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- |
updates: ∆Wˆ d,s,+ = max(∆Wˆ d,s , 0) and ∆Wˆ d,s,− = | min(∆Wˆ d,s , 0) |.
|     |     | DA,ID |     |     | DA,ID |     | DA,ID |     |     | DA,ID |     |     |     |     |
| --- | --- | ----- | --- | --- | ----- | --- | ----- | --- | --- | ----- | --- | --- | --- | --- |
• The standard deviation of the forecast updates should reflect the uncertainty about the weather
situation. Highly volatile forecast updates are mirrored to starkly changing positions in renewable
energy asset portfolios and should thus exercise an influence on the volatility of the price process
10

0
1
2 3
4
5
6
7
8 9 10
11 12
13
14
15
16
17
18
19
20 21
22
23
2016-03-01 2016-09-01 2017-03-01 2017-09-01 2018-03-01 2018-09-01 2019-03-01 2019-09-01 2020-03-01
Date d
s
ruoH
Autocorrelation for Lag 1 of PI d D , , s t for each trading session by delivery day and hour
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
1 gaL
rof
FCA
(a) Lag 1 autocorrelation of ∆Pd,s .
ID,t
0
1
2
3
4
5
6
7 8
9
10 11
12
13
14
15
16
17
18
19
20 21
22
23
2016-03-01 2016-09-01 2017-03-01 2017-09-01 2018-03-01 2018-09-01 2019-03-01 2019-09-01 2020-03-01
Date d
s ruoH
Autocorrelation p-value for Lag 1 of PI d D , , s t for each trading session by delivery day and hour
0.10
0.08
0.06
0.04
0.02
0.00
eulav-p
(b) p-values for lag 1 autocorrelation of ∆Pd,s .
ID,t
Figure 6.: Autocorrelation of ∆Pd,s per trading window for lags 1 and according p-values. The first heat
ID,t
maps show the size of the correlation coefficient by delivery day d and hour s, second shows
according p-values. Lags 2 and 3 can be found in Appendix C.
11

due to quickly changing demand and supply. Let
Vd,s = [d−1, 12:00 ≥ v ≥ b(d,s)−185]
be the set of all forecast versions received between the day-ahead auction and the start of the
simulation. The difference between two consecutive forecast versions v,v−1 is denoted as ∆Wˆ d,s .
v−1,v
Then σd,s (∆Wˆ ) = σ (∆Wˆ d,s ) denotes the standard deviation of all differences between two
DA,ID v−1,v
v∈Vd,s
consecutive forecasts received between the day-ahead auction and the start of the simulation. It is
worth noting that due to the schedule of the day-ahead and intraday markets, V is larger for later
delivery hours, thus more forecast versions are considered for σd,s (∆Wˆ ) for later delivery hours.
DA,0
Analogously, ∆Wˆ d,s ,∆Sˆd,s,+ ,∆Sˆd,s,− and σd,s (∆Sˆ) are defined for the solar production forecasts.
DA,ID DA,ID DA,ID DA,ID
Panels (a) - (c) in Figure 7 show the day-ahead versions of wind, solar and demand forecasts. For wind
and solar, the change between day-ahead and intraday versions and the standard deviation are plotted as
well.
Under the Regulation on wholesale Energy Market Integrity and Transparency (REMIT), market partic-
ipants are required to report non-availabilities of their assets and make this information available to all
othermarketparticipantsinordertoavoidinsidertrading. Inpractice,thisobligationisfulfilledbymarket
participants by submitting non-availability messages to an inside information platform (European Com-
mission, 2011, Agency for the Cooperation of Energy Regulators (ACER), 2020, Lazarczyk and Le Coq,
2018). WeretrieveunavailabilitymessagesfromtheEuropeanEnergyExchange(EEX)AG(2020)market
transparency platform for all non-availabilities regarding the delivery periods between January 1st, 2016
and July 31st, 2020. A non-availability message is defined by the date of publication, beginning and end
of the non-availability, the type of non-availability, i.e. whether it has been planned or unplanned, the
fuel type of the unavailable asset as well as the unavailable capacity in MW. The outage messages are
aggregated to the total non-available generation capacity for the delivery period d,s known at the time of
the spot auction. Additionally, the outages are aggregated to the total non-available generation capacity
known at the start of the simulation for a delivery period d,s. Sub-hourly outages are taken into account
with the respective share of the full hour. The differences between the level of outages day-ahead and at
the start of the simulation is calculated similar as the difference in the forecasts: ∆Od,s = Od,s−Od,s.
DA,ID ID DA
Afterwards, the difference ∆Od,s is split into planned and unplanned outages denoted as ∆Od,s,planned
DA,0 DA,ID
and ∆Od,s,unplanned. Figure 7 (d) plots the aggregated outage data; Table 3 gives summary statistics.
DA,ID
12

Table 3.: Summary Statistics for wind, solar and demand forecasts, and the reported outages. Day-ahead
to intraday forecast changes and the standard deviation of versioned updates. Indices d,s and t
|     | omitted | for | better | readability. |     | Values | in MW. |        |        |     |     |         |           |
| --- | ------- | --- | ------ | ------------ | --- | ------ | ------ | ------ | ------ | --- | --- | ------- | --------- |
|     |         |     | Wind   |              |     |        | Solar  |        | Demand |     |     | Outages |           |
|     |         | Wˆ  |        | ∆Wˆ σ(∆Wˆ)   |     | Sˆ     | ∆Sˆ    | σ(∆Sˆ) |        | Dˆ  |     | O ∆O    | ∆O        |
|     |         |     |        |              |     |        |        |        |        |     |     | planned | unplanned |
Count (n) 38856 38856 38856 38856 38856 38856 38856 38856 38856 38856
Mean (µ) 12372.39 -59.60 182.78 4634.27 8.35 56.22 59422.74 15506.99 573.24 410.07
Std. (σ) 9410.80 1291.23 110.11 6994.23 521.30 84.29 10286.86 5498.09 711.15 486.55
Min 172.75 -9515.50 6.00 0.00 -4604.50 0.00 33927.90 5157.40 -3451.60 -1690.00
Max 47708.00 11383.25 1940.55 32474.50 5914.50 842.83 83494.50 33384.40 5569.00 3847.00
50
|     | WDA WDA,t |     | (DDA,t) |     |     |     |     | SDA | SDA,t | (SDA,t) |     |     |     |
| --- | --------- | --- | ------- | --- | --- | --- | --- | --- | ----- | ------- | --- | --- | --- |
30
40
25
30
20
| hWG |     |     |     |     |     |     |     | hWG |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 20  |     |     |     |     |     |     | 15  |     |     |     |     |     |
|     | 10  |     |     |     |     |     |     | 10  |     |     |     |     |     |
5
0
0
|     | 10   |      |      |      |      |        |     | 5    |     |      |      |        |      |
| --- | ---- | ---- | ---- | ---- | ---- | ------ | --- | ---- | --- | ---- | ---- | ------ | ---- |
|     | 2016 | 2017 | 2018 |      | 2019 | 2020   |     | 2016 |     | 2017 | 2018 | 2019   | 2020 |
|     |      |      |      | Date |      |        |     |      |     |      |      | Date   |      |
|     |      |      |      |      |      | Wˆd,s, |     |      |     |      |      | Sˆd,s, |      |
(a) Day-ahead wind production forecasts (b) Day-ahead solar production forecasts difference
|     |     |     |     |     |     |     | DA  |     |     |     |     |     | DA  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
difference to intraday ∆Wˆd,s and standard to intraday ∆Sˆd,s and standard deviation of
|     |     |     |     | DA,ID |     |     |     |     |     |     | DA,ID |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
deviation of forecast updates σd,s (∆Wˆ). forecast updates σd,s (∆Sˆ).
|     |     |     |     |     | DA,ID |     |     |     |     |     |     | DA,ID |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | ----- | --- |
35
|     | Demand DDA |     |     |     |     |     |     | ODA | Oplanned | Ounplanned |     |     |     |
| --- | ---------- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | --- | --- |
30
70
25
|     | 60  |     |     |     |     |     |     | 20  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
hWG
| hWG |     |     |     |     |     |     |     | 15  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 50  |     |     |     |     |     |     | 10  |     |     |     |     |     |
5
40
0
5
|     | 2016          | 2017 | 2018   |           | 2019  | 2020 |     | 2016          |         | 2017       | 2018      | 2019          | 2020          |
| --- | ------------- | ---- | ------ | --------- | ----- | ---- | --- | ------------- | ------- | ---------- | --------- | ------------- | ------------- |
|     |               |      |        | Date      |       |      |     |               |         |            |           | Date          |               |
|     |               |      |        |           |       |      |     | (d) Day-ahead |         | aggregated | outage    | notifications | Od,s and      |
|     | (c) Day-ahead |      | demand | forecasts | Dˆd,s |      |     |               |         |            |           |               |               |
|     |               |      |        |           | DA    |      |     |               |         |            |           |               | DA            |
|     |               |      |        |           |       |      |     | the           | planned | and        | unplanned | changes       | ∆Od,s,planned |
DA,ID
|     |     |     |     | .   |     |     |     |     |     | and | ∆Od,s,unplanned. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- |
DA,ID
Figure 7.: Day-ahead RES production forecasts, forecast updates and their standard deviation and the
|      | aggregated   |     | outage | notifications. |            |     |     |     |     |     |     |     |     |
| ---- | ------------ | --- | ------ | -------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3.3. | Spot Auction |     | Curves | and            | Elasticity |     |     |     |     |     |     |     |     |
The impact of forecast errors on ∆Pd,s depends on the steepness of the merit-order (Kremer et al., 2020,
ID,t
2021, Kulakov and Ziel, 2020). Following this thought, the volatility of the intraday price should also be
influencedbytheslopeofthemerit-order. Ifthemarketisinasteepmerit-orderregime,evensmallvolume
changes might have a high price impact. Thus, the expected price impact of changes in (RES) supply is
13

stronger. Under uncertainty of future RES forecast updates, the expected volatility should increase with
the steepness of the merit-order. If the market price corresponds to a rather flat region of the merit-order,
the price impact of changes in RES supply should be smaller and hence the volatility of ∆Pd,s should be
ID,t
lower. This thought will be the main intuition for the addition of a merit-order slope to the model for the
volatility of the distribution of ∆Pd,s .
ID,t
There are different methods to model the merit-order used in practice and academia. Fundamental meth-
ods as developed by Beran et al. (2019), Gürtler and Paulsen (2018), Pape et al. (2016) are complex,
data-intensive and rely heavily on assumptions. For this reason, Kremer et al. (2020, 2021) develop an
econometric model based on He et al. (2013) by fitting the relationship between demand forecasts and
day-ahead prices to an exponential function. This yields an analytically traceable function, whose slope
can easily be calculated as the first derivative. This paper develops a further method to derive the slope
of the merit-order by using the day-ahead auction curves as a proxy for the supply stack. This approach is
based on Balardy (2022) and Kulakov and Ziel (2020) and has three advantages compared to the approach
of He et al. (2013): First, the auction curves combine all market and availability information available on
d−1 and do not depend on a longer time frame for the estimation of the function coefficients. Second,
by using the auction curves, there is no need to assume an explicit functional form for the merit-order.
Lastly, the auction curves also represent negative prices, while the exponential function is only defined on
the positive real line.
However, it is also important to discuss the drawbacks attached to modelling the intraday merit-order
based on day-ahead information in general and attached to the auction curves especially. First, the
available generation capacity can (and due to RES will) change between d−1 and d, leading to shifts in
themerit-order. Second, powerplantsmightnotbeasflexibleintradayasinaday-aheadplanninghorizon
due toramping behaviour, start-up costsor constraints due to gridservice delivery. On the contrary, some
power plants might be optimised predominantly intraday and not on the day-ahead auction if they are at-
the-money(onthisissueseee.g.Papeetal.,2016). Especiallyfortheauctioncurves, twofurtherproblems
arise: First, the demand and supply curve are both elastic curves, contrary to the common assumption of
largely inflexible demand in energy markets. This problem is addressed by applying the transformation
introduced by Kulakov and Ziel (2019, 2020) in the following paragraph. Thereby, all elasticity from the
demand curve is shifted to the supply curve, which yields a perfectly inelastic demand and elastic supply
curve. Second, theday-aheadauctioncurvesasprovidedbyEPEXSpotonlycontainstandardbids. Thus,
linked, block and other complex bids are excluded from the curves, which removes information about the
available generation capacity. This problem cannot be addressed simply and needs to be kept in mind for
the further interpretation of the results.
The intuition behind the transformation of the auction curves is outlined in detail in Kulakov and Ziel
(2019)andCoulonetal.(2014),sohereonlyabriefintroductionisgiven. Figure8ashowsthatthedemand
curveattheday-aheadauctioniselastic, whichisatoddswiththecommonassumptionoffewpriceelastic
consumersofelectricity,especiallyatshortnotice(Coulonetal.,2014,KnautandPaulus,2016). However,
producers and consumers have the chance to sell/purchase their energy not only on the spot auction, but
also in the OTC and derivative markets. In addition, there might be market participants that own both
assets on the supply and demand side. Thus, arbitrage opportunities between the two markets arise that
canbeusedbythetrader. Coulonetal.(2014)andKulakovandZiel(2019)considerthiseffectbyflipping
the elasticity from the demand curve to the supply curve, hence obtaining a perfectly inelastic (vertical)
demand curve and an elastic supply curve to incorporate those effects. The core idea here is that, at the
day-ahead auction, placing a buy order for a volume x for a price y is the same placing a buy order for
the volume x at the maximum price and placing a sell order with volume x for the price y + the smallest
14

| 100 |     |     |     | DEMWd,Ss(q) | 100 | SUPd,s(q)       |     |     |     | 100 | SUPd,s(q)     |     |     |
| --- | --- | --- | --- | ----------- | --- | --------------- | --- | --- | --- | --- | ------------- | --- | --- |
|     |     |     |     | SUPWd,Ss(q) |     | DEMidn,eslastic |     |     |     |     | DEMidm,splied |     |     |
2000MWh
DEMidm,splied+2000MWh
| 80  |     |     |     |     |     | 80  |     |     |     | 80  | DEMidm,splied |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- |
DEMidn,eslastic
Slope
| 60       |     |     |     |     |          | 60  |     |     |     | 60       |     |     |     |
| -------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | -------- | --- | --- | --- |
| ][ ecirP |     |     |     |     | ][ ecirP |     |     |     |     | ][ ecirP |     |     |     |
| 40       |     |     |     |     |          | 40  |     |     |     | 40       |     |     |     |
| 20       |     |     |     |     |          | 20  |     |     |     | 20       |     |     |     |
| 0        |     |     |     |     |          | 0   |     |     |     |          | 0   |     |     |
| 20       |     |     |     |     |          | 20  |     |     |     | 20       |     |     |     |
22500 25000 27500 30000 32500 35000 37500 40000 42500 30000 35000 40000 45000 50000 55000 30000 35000 40000 45000 50000 55000
|     |     | Volume [MWh] |     |     |     |     | Volume [MWh] |     |     |     |     | Volume [MWh] |     |
| --- | --- | ------------ | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | ------------ | --- |
(a) Original curves. (b) Transformed curves. (c) Slope coefficient.
Figure 8.: Transformed auction curves for June 1, delivery hour s = 9 and the calculation of the merit-
order slope coefficient. Note how the intersection of SUPd,s(DEMd,s again yields Pd,s for
)
|     |        |     |          |         |     |           |        |        |          |       | inelastic |     | Spot |
| --- | ------ | --- | -------- | ------- | --- | --------- | ------ | ------ | -------- | ----- | --------- | --- | ---- |
|     | Panels | (a) | and (b). | Figures |     | truncated | on the | y-axis | to [-20, | 100]. |           |     |      |
tick. Kulakov and Ziel (2019) elaborate in detail on the econometric framework, which is adopted in this
| paper | and the | implications |     | for the | different |     | market participants. |     |     |     |     |     |     |
| ----- | ------- | ------------ | --- | ------- | --------- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
Figure 8 shows the supply and demand curves from the spot auction for the delivery day June 1st, 2017
for hour 9. The intersection of supply and demand yields the spot price Pd,s . The notation follows
s =
Spot
largely Kulakov and Ziel (2019, 2020). Define the supply and demand curves as a mapping of volumes
to prices by SUP : (0,∞) → [P ,P ] and DEM : (0,∞) → [P ,P ]. Due to strict
|     |     | WS  |     |     |     | min | max | WS  |     |     |     | min max |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
monotonicity the inverse SUP −1 and DEM −1 always exist. Hence, SUPd,s (q) = P is the supply
|     |     |     |     | WS  |     |     | WS  |     |     |     |     | WS  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
or sell curve and DEMd,s (q) = P is the demand curve at the spot auction for delivery day d and hour
WS
s relating the volume q ought to be sold/bought to the according price P. The inelastic demand in the
−1
wholesale market can be calculated by DEMd,s = DEMd,s (P ) where P = −500 EUR/MWh
|     |     |     |     |     |     |     | inelastic | WS  |     | min |     | min |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
is the minimum price at the day-ahead auction (EPEX SPOT SE, 2018, see Chapter 2 of this paper). The
| transformed |     | inverse supply |     | curve                        | can       | be written         | as:       |                                     |           |                    |     |           |     |
| ----------- | --- | -------------- | --- | ---------------------------- | --------- | ------------------ | --------- | ----------------------------------- | --------- | ------------------ | --- | --------- | --- |
|             |     | SUPd,s−1       |     |                              | SUPd,s    |                    | −1        | DEMd,s                              |           | −DEMd,s            |     | −1        |     |
|             |     |                | (z) | =                            |           |                    | (z)       | +                                   |           |                    |     | (z)       | (1) |
|             |     |                |     |                              |           | WS                 |           |                                     | inelastic |                    |     | WS        |     |
|             |     |                |     |                              | (cid:124) | (cid:123)(cid:122) | (cid:125) | (cid:124)                           |           | (cid:123)(cid:122) |     | (cid:125) |     |
|             |     |                |     | invertedwholesalesupplycurve |           |                    |           | flippedinvertedwholesaledemandcurve |           |                    |     |           |     |
As the curves are monotonic, SUPd,s−1 also defines SUPd,s(q). As it is clearly visible in Figure 8, the
(z)
original equilibrium is reached at the point Pd,s SUPd,s(DEMd,s ). For the transformed curves it
=
|     |     |     |     |     |     |     | DA  |     | inelastic |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
now holds that for the resulting clearing price, shifting DEMd,s by some quantity equals shifting
x
inelastic
SUPd,s−1
|     | (z) | by −x, | as the | demand | is  | perfectly | inelastic. |     |     |     |     |     |     |
| --- | --- | ------ | ------ | ------ | --- | --------- | ---------- | --- | --- | --- | --- | --- | --- |
Under the assumptions that the merit-order does not change significantly between day-ahead and intra-
day and that the transformed supply curve is a reasonable proxy for the merit-order, the the implied
intraday demand and the slope coefficient for the merit-order can be derived. The first assumption is
implicitly already made by Kremer et al. (2020, 2021). The second assumption is discussed above. The
last known 5-minute-interval-VWAP before the start of the simulation is Pd,s . Under the Market Effi-
ID,0
ciency Hypothesis (MEH), this price should reflect all changes to demand and supply. As all flexibility
is already included in the supply curve, the implied intraday inelastic demand at can be calculated
|     |     |     |     |     |     |     |     |     |     |     |     | t = 0 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
15

as DEMd,s = SUPd,s−1 (Pd,s ). As already mentioned in Chapter 2, the lower and upper price lim-
implied ID,0
its at the day-ahead auction are [−500,3000] EUR/MWh, while in the intraday market these are set to
[−9999,9999] EUR/MWh. Hence, it might be possible that Pd,s is outside the domain of SUPd,s−1 (z).
ID,0
This case, however, does not occur in the dataset used in this paper. In the spirit of Balardy (2022) and
Kulakov and Ziel (2019), the measure for the elasticity MOd,s is calculated as a finite central difference
q
quotient of the transformed supply curve around DEMd,s :
implied
SUPd,s(DEMd,s +q)−SUPd,s(DEMd,s −q)
MOd,s = implied implied , (2)
q 2·q
where q = {500,1000,2000} MWh. It is defined in EUR/MWh2 and is the steepness of the auction curves
around the price level at t = 0. Intuitively, it can be interpreted as the expected price change for a 1 MWh
change in supply. In this paper, three values for q are tested as there is some arbitrariness in choosing this
value. In the literature, Kulakov and Ziel (2019) choose q = 100 MWh, Balardy (2022) chooses q = 500
MWh. In this paper, slightly higher q are selected to accommodate the fact that the standard deviation
of ∆Wˆ d,s and ∆Sˆd,s is roughly between 500 MW and 1300 MW (see Table 3). Values of q < 500
DA,ID DA,ID
MWh thus might not catch the full range of volume changes occurring during the intraday trading. These
volume changes in turn lead to movements along the merit-order. Figure 8 (c) shows the intuition of the
slope coefficient for q = 2000. Figure 9 shows boxplots of the slope coefficients for q = 2000 MWh by the
price level. Clearly, the slope increases with increasing price level, which is in line with the classic merit
order model. However, we see the slope rising as well for small and negative prices. This observation is at
odds with the common assumption of zero-marginal cost renewable production, which would imply a flat
lower end of the merit order. However, many renewable assets are part of subsidy schemes, making their
effective marginal costs negative. These assets are sold to the market even for negative prices, as long as
the subsidy paid per produced MWh offsets negative selling prices.
]041-
,051-(
]031-
,041-(
]021-
,031-(
]011-
,021-(
]001-
,011-(
]09-
,001-(
]08-
,09-(
]07-
,08-(
]06-
,07-(
]05-
,06-(
]04-
,05-(
]03-
,04-(
]02-
,03-(
]01-
,02-(
]0
,01-(
]01
,0(
]02
,01(
]03
,02(
]04
,03(
]05
,04(
]06
,05(
]07
,06(
]08
,07(
]09
,08(
]001
,09(
]011
,001(
]021
,011(
]031
,021(
]041
,031(
]051
,041(
]061
,051(
]071
,061(
]081
,071(
]091
,081(
]002
,091(
]012
,002(
]022
,012(
]032
,022(
]042
,032(
0.06
0.05
0.04
0.03
0.02
0.01
0.00
Grouped P 0 d,s
0002OM
tneiciffeoC
epolS
7173
1495
563
103
39
22
14
4
0
snoitavresbO
fo
rebmuN
Figure 9.: Boxplots for the merit-order slope MO grouped by the price level. Colouring indicates the
2000
Number of observations, note the log-scale of the colorbar. Upper and lower end of the box
correspond to Q and Q respectively.
0.25 0.75
16

| 4. Electricity |     | Price | Models |     |     |     |     |     |     |     |     |     |
| -------------- | --- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Recall from the introduction that the price differences ∆Pd,s follow certain distribution that we denote
ID,t
| Gd,s which | is  | a mixture | distribution |     |       |        |             |     |           |     |     |     |
| ---------- | --- | --------- | ------------ | --- | ----- | ------ | ----------- | --- | --------- | --- | --- | --- |
|            |     |           |              |     | ∆Pd,s | ∼ Gd,s | = (1−αd,s)δ |     | +αd,sFd,s |     |     |     |
|            |     |           |              |     | ID,t  |        |             | t   | 0 t       |     |     |     |
with the Dirac distribution , the continuous distribution Fd,s and the Bernoulli variable αd,s with
δ
|             |       |     |           | 0        |     |     |     |     |     |     | t   |     |
| ----------- | ----- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| probability | πd,s. | The | two-stage | approach |     | is: |     |     |     |     |     |     |
t
|     |     |     |     | πd,s |     |     | αd,s |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | ---- | --- | --- | --- | --- | --- |
1. Model the probability for a trade-event = 1 by a logistic regression model.
|     |     |     |     | t   |     |     |     | t   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2. Model the distribution Fd,s by skewed Student’s t-distribution respectively the Johnson’s S and
|     |     |     |     | t   |     |     |     |     |     |     |     | U   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
estimate θd,s using the GAMLSS-framework (Stasinopoulos and Rigby, 2005, 2007, Stasinopoulos
| et  | al., 2017, | 2018). |     |     |     |     |     |     |     |     |     |     |
| --- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
This introduces a dependence structure between the parameters of and F, as the probability πd,s is
δ
0
explained by past realisations of ∆Pd,s and αd,s. In the following three sections, the logistic model, the
|               |       |            |          |            | ID,t  |     | t          |     |     |     |     |     |
| ------------- | ----- | ---------- | -------- | ---------- | ----- | --- | ---------- | --- | --- | --- | --- | --- |
| GAMLSS        | model | and        | the used | benchmarks |       | are | presented. |     |     |     |     |     |
| 4.1. Logistic |       | regression |          | model      | for α |     |            |     |     |     |     |     |
The binary variable αd,s will be modelled by a regularized logistic regression model (Meier et al., 2008,
t
Tibshirani, 1996) in the implementation of Friedman et al. (2010) using coordinate descent. Generally, for
| a logistic | model |     |     |     |     |          |     |          |     |     |     |     |
| ---------- | ----- | --- | --- | --- | --- | -------- | --- | -------- | --- | --- | --- | --- |
|            |       |     |     |     |     | (cid:18) |     | (cid:19) |     |     |     |     |
π
|     |     |     |     |     |     | log |     | =   | XTβ |     |     | (3) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1−π
for the Bernoulli variable with probability π, the LASSO estimator βˆLASSO is given by
|     |     |     |     | α       |     | P(α   | =        | 1) =     |          |          |     |     |
| --- | --- | --- | --- | ------- | --- | ----- | -------- | -------- | -------- | -------- | --- | --- |
|     |     |     |     | βˆLASSO |     |       | (cid:16) | (cid:16) | (cid:17) | (cid:17) |     |     |
|     |     |     |     |         |     | = arg | min      | −l β,X˜  | +λ||β||  | ,        |     | (4) |
1
where is a tunable shrinkage parameter. The corresponding log-likelihood is given by
| λ   |     |     |     |     |     |     |     |     |     |     | l   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
N
|     |     |     |     | (cid:16) | (cid:17) | 1 (cid:88) |          |     | (cid:16) | (cid:16) | (cid:17)(cid:17) |     |
| --- | --- | --- | --- | -------- | -------- | ---------- | -------- | --- | -------- | -------- | ---------------- | --- |
|     |     |     |     | l β,X˜   | =        | α          | X˜Tβ−log |     | 1+exp    | X˜Tβ     | ,                | (5) |
|     |     |     |     |          |          |            | i i      |     |          | i        |                  |     |
N
i=1
where X˜ is a standardisation of X. The parameter is optimised from an exponential grid of 100 values
λ
by choosing the minimum Bayesian Information Criterion (BIC), i.e. λopt = arg min BIC(λ) using the
| glmnet | package | by Friedman |     | et al. | (2010). |     |     |     |     |     |     |     |
| ------ | ------- | ----------- | --- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
Here, the logit function for αd,s is explained by four components: the impact of past price differences, the
t
time to maturity and weekday effects, fundamental variables such as RES forecasts, outages and the slope
of the merit-order, and a regression on averaged past αd,s. Intuitively, the probability of trades should rise
t
with higher ∆Pd,s , closer to delivery, with increasing wind and solar forecasts and with increased recent
ID,t
trading activity measured by past αd,s, but decrease on the weekends and the transition day Monday.
t
17

|     |     | (cid:32) |        | (cid:33) |     |           |         |        |          |                    |        |     |           |           |     |
| --- | --- | -------- | ------ | -------- | --- | --------- | ------- | ------ | -------- | ------------------ | ------ | --- | --------- | --------- | --- |
|     |     |          | d,s    |          |     | 3         |         |        | 6        |                    |        |     | 12        |           |     |
|     |     |          | π      |          |     | (cid:88)  |         |        | (cid:88) |                    |        |     | (cid:88)  |           |     |
|     |     | log      | t      |          | = β | +         | β ∆Pd,s |        | + β      | |∆Pd,s             |        | |+β | |∆Pd,s    | |         |     |
|     |     |          | 1−πd,s |          | 0   |           | j       | ID,t−j |          | 3+j                | ID,t−j |     | 10 ID,t−j |           |     |
|     |     |          |        | t        |     | j=1       |         |        | j=1      |                    |        |     | j=7       |           |     |
|     |     |          |        |          |     | (cid:124) |         |        |          | (cid:123)(cid:122) |        |     |           | (cid:125) |     |
Pricedifferences
31
(cid:88)
|     |     | +β  | MON(d)+β |     |     | SAT(d)+β |     | SUN(d)+ |     |     | β    | TTD(t) |     |     |     |
| --- | --- | --- | -------- | --- | --- | -------- | --- | ------- | --- | --- | ---- | ------ | --- | --- | --- |
|     |     |     | 11       |     |     | 12       |     | 13      |     |     | 13+j |        |     |     |     |
j=1
|     |     |     | (cid:124) |     |     |     |     | (cid:123)(cid:122) |     |     |     |     | (cid:125) |     |     |
| --- | --- | --- | --------- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --------- | --- | --- |
Timedummies
|     |     | +β  | Dˆd,s     | +β  | Wˆ  | d,s +β             | Sˆd,s | +Od,s |           |     |     |     |     |     | (6) |
| --- | --- | --- | --------- | --- | --- | ------------------ | ----- | ----- | --------- | --- | --- | --- | --- | --- | --- |
|     |     |     | 47        | DA  | 48  | DA                 | 49 DA |       | DA        |     |     |     |     |     |     |
|     |     |     | (cid:124) |     |     | (cid:123)(cid:122) |       |       | (cid:125) |     |     |     |     |     |     |
Day-aheadfundamentalvariables
|     |     | +β  | ∆Wˆ       | d,s,+ | +∆Wˆ | d,s,− | +β                 | ∆Sˆd,s,+ |       | +β  | ∆Sˆd,s,− |           |     |     |     |
| --- | --- | --- | --------- | ----- | ---- | ----- | ------------------ | -------- | ----- | --- | -------- | --------- | --- | --- | --- |
|     |     |     | 51        |       |      |       |                    | 53       |       | 54  |          |           |     |     |     |
|     |     |     |           | DA,ID |      | DA,ID |                    |          | DA,ID |     | DA,ID    |           |     |     |     |
|     |     |     | (cid:124) |       |      |       | (cid:123)(cid:122) |          |       |     |          | (cid:125) |     |     |     |
Day-ahedtointradayforecastupdates
|     |     |     | σd,s |       | (∆Wˆ |     | σd,s  | (∆Sˆ)+ |     | ∆Od,s,planned+β |       |     | ∆Od,s,unplanned |     |     |
| --- | --- | --- | ---- | ----- | ---- | --- | ----- | ------ | --- | --------------- | ----- | --- | --------------- | --- | --- |
|     |     | +β  | 55   |       | )+β  | 56  |       |        | β   | 57              |       |     | 58              |     |     |
|     |     |     |      | DA,ID |      |     | DA,ID |        |     |                 | DA,ID |     | DA,ID           |     |     |
(cid:124) (cid:123)(cid:122) (cid:125) (cid:124) (cid:123)(cid:122) (cid:125)
Standarddeviationofforecastupdates Intradaychangesinplannedandunplannedoutages
|     |     |     |           |      |                    |        |           | 3        |       |     | 12       |      |       |     |     |
| --- | --- | --- | --------- | ---- | ------------------ | ------ | --------- | -------- | ----- | --- | -------- | ---- | ----- | --- | --- |
|     |     |     |           | Pd,s | −Pd,s              |        |           | (cid:88) | MOd,s |     | (cid:88) |      | α¯d,s |     |     |
|     |     | +   | β         | |    |                    |        | | +       |          | β     |     | +        | β    | ,     |     |     |
|     |     |     | 59        | DA   |                    | ID,t−1 |           |          | 59+j  | j   |          | 62+j | t−j   |     |     |
|     |     |     | (cid:124) |      | (cid:123)(cid:122) |        | (cid:125) | j=1      |       |     | j=1      |      |       |     |     |
Day-aheadtot−1pricespread
|     |     |     |     |     |     |     |     | (cid:124)             | (cid:123)(cid:122) | (cid:125) | (cid:124)         | (cid:123)(cid:122) | (cid:125) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | ------------------ | --------- | ----------------- | ------------------ | --------- | --- | --- |
|     |     |     |     |     |     |     |     | Slopeofthemerit-order |                    |           | Regressiononα¯d,s |                    |           |     |     |
t
| whereα¯d,s |     |        | (cid:80)j | αd,s, |                      |     |     |     | observedvaluesofαd,s. |     |     |     |                          |     |     |
| ---------- | --- | ------ | --------- | ----- | -------------------- | --- | --- | --- | --------------------- | --- | --- | --- | ------------------------ | --- | --- |
|            |     | = 1/j· |           |       | theaverageofthelastj |     |     |     |                       |     |     |     | Thisapproachtotransform- |     |     |
|            | t−j |        | i=1       | t−i   |                      |     |     |     |                       |     |     |     | t                        |     |     |
ing lagged values is similar to HAR-type models found in the field of financial econometrics. A thorough
description of the model is omitted here and can be found in Narajewski and Ziel (2020a). SAT(d),
SUN(d), and MON(d) are dummies for the weekday of d. TTD(t) is a set of dummies for t. Accordingly,
the model has more than 70 coefficients of which some tend to be highly correlated. To avoid problems
with over fitting and multicollinearity, the model is estimated using the LASSO of Tibshirani (1996).
Note however, that for the one year training set used in this paper, we have 365·T = 365·31 = 11315
observations and are still in a setting where n (cid:29) p. The number of observations is sufficiently larger than
| the  | number | of parameters, |           |     | hence | identification |     | is  | not an | issue | here. |     |     |     |     |
| ---- | ------ | -------------- | --------- | --- | ----- | -------------- | --- | --- | ------ | ----- | ----- | --- | --- | --- | --- |
| 4.2. | GAMLSS |                | Framework |     |       |                |     |     |        |       |       |     |     |     |     |
This chapter briefly introduces the GAMLSS-framework used to model
|     |     |     |     |     |     |     | ∆Pd,s | |    | αd,s = | 1 ∼ F. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---- | ------ | ------ | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |       | ID,t | t      |        |     |     |     |     |     |
The GAMLSS is an extension of the Generalized Additive Models (GAM) introduced by Hastie and
Tibshirani (1987, 1990). It allows to model not only the expected value of the a variable but
|     |     |     |     |     |     |     |     |     |     |     |     |     |     | Y ∼ | F   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
also the higher moments under a wide range of continuous and discrete distributions F. For an in-depth
treatment we refer the reader to Stasinopoulos and Rigby (2005, 2007), Stasinopoulos et al. (2018) and
themanualoftheR-packagegamlss(Stasinopoulosetal.,2017). Thenotationinthefollowingparagraphs
| follows | the | notation | of  | aforementioned |     |     | sources. |     |     |     |     |     |     |     |     |
| ------- | --- | -------- | --- | -------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
We first introduce the framework in an abstract notation. Following the mathematical formulation we
will relate the abstract notation to the notation of the price differences. Let be Y = (Y ,Y ,...,Y ) be
|     |     |     |     |     |     |     |     |     |     |     |     |     |     | 1 2 | n   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
18

a vector of independent observations . The GAMLSS-framework assumes that have the
|             |     | i = 1,...,n |          |     |     |     |       | Y       |       |     |     |     | Y   |     |
| ----------- | --- | ----------- | -------- | --- | --- | --- | ----- | ------- | ----- | --- | --- | --- | --- | --- |
|             |     |             |          |     |     |     |       | i       |       |     |     |     | i   |     |
| probability |     | density     | function |     |     |     |       |         |       |     |     |     |     |     |
|             |     |             |          |     |     |     | f(y | | µ ,σ ,ν | ,τ ), |     |     |     |     |     |
|             |     |             |          |     |     |     | i     | i i     | i i   |     |     |     |     |     |
where each of the distribution parameters can be a smooth function of the explanatory variables. We
| denote | as  |       |      |         |        |       |      | the vector | of  |           | distribution | parameters |     | which |
| ------ | --- | ----- | ---- | ------- | ------ | ----- | ---- | ---------- | --- | --------- | ------------ | ---------- | --- | ----- |
|        | θ   | = (θ  | θ ,θ | ,θ      | ) = (µ | ,σ ,ν | ,τ ) |            | k   | = 1,...,4 |              |            |     |       |
|        |     | i i,1 | i,2  | i,3 i,4 |        | i i   | i i  |            |     |           |              |            |     |       |
are usually known as the location, scale and shape parameters . For the distributions used in this
θ i,k
paper, ν denotes the skewness and τ denotes the kurtosis. θ is a matrix whose individual components
|     | i   |     |     |     |     | i   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
have the indices i and k. The vectors θ and θ are defined along the 2 axis of θ. Formally, we have
|     |     |     |     |     |     | i     | k     |        |         |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | ----- | ------ | ------- | --- | --- | --- | --- | --- |
|     |     |     |     |     | Y   | ∼ F(µ | ,σ ,ν | ,τ ) ⇔ | Y ∼ F(θ | ).  |     |     |     |     |
|     |     |     |     |     |     | i     | i i   | i i    | i       | i   |     |     |     |     |
For each k, let be a known and monotonic link function that relates the distribution parameters
|        |           | g (·) |               |     |     |        |       |          |     |     |     |     |     | θ   |
| ------ | --------- | ----- | ------------- | --- | --- | ------ | ----- | -------- | --- | --- | --- | --- | --- | --- |
|        |           | k     |               |     |     |        |       |          |     |     |     |     |     | k   |
| to the | predictor |       | . We consider |     | the | GAMLSS | model | equation |     |     |     |     |     |     |
|        |           | η k   |               |     |     |        |       |          |     |     |     |     |     |     |
|        |           |       |               |     |     | g      | (θ )  | = η =    | X β |     |     |     |     | (7) |
|        |           |       |               |     |     |        | k k   | k        | k k |     |     |     |     |     |
where X is a n×J fixed design matrix and β(cid:48) = (β ,β ,...,β ) is a parameter vector of length J .
|     | k   |     | k   |     |     |     | k   | 1,k | 2,k | J ,k |     |     |     | k   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
k
The link functions g ensure that the estimated distribution parameters fulfil the necessary assumptions
k
concerning their support. To improve the robustness of the estimation, the following link functions are
used:
|     |     |     |     |     | g   | (z) = | z   |     |     |     |     |     |     | (8) |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
ident
(9)
|     |     |     |     |     | g   | (z) = | log(z) |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
log
|     |     |     |     | g   |     | (z) = | log(z)1(z | ≤   | 1)+(z−1)1(z |     | > 1) |     |     | (10) |
| --- | --- | --- | --- | --- | --- | ----- | --------- | --- | ----------- | --- | ---- | --- | --- | ---- |
logident
|     |     |     |     | g   |     | (z) = | log(z−2) |     |     |     |     |     |     | (11) |
| --- | --- | --- | --- | --- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | ---- |
logshift2
We use g for the location parameters µ in both distribution assumptions, and additionally for the
ident
skewness parameter of the skewed t-distribution which also has support (−∞,∞). is introduced
|     |     |     | ν   |     |     |     |     |     |     |     |     | g   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
logident
to avoid the exponential inverse for large estimates, thus improving the robustness of the estimation
(Narajewski and Ziel, 2020a, Ziel, 2021). We utilize it for all scale parameters σ. In addition, g
logshift2
is simply the natural logarithm shifted to 2 to preserve the condition ν > 2 for the scale of the skewed
| t-distribution. |     | For | the remaining |     | parameters |     | we consider |     | .   |     |     |     |     |     |
| --------------- | --- | --- | ------------- | --- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
g
log
Ziel and Muniain (2021) extend the GAMLSS framework to allow for regularized LASSO estimation. As
with the logistic model, we employ the BIC to select the optimal shrinkage parameter λ. The adaptive
| LASSO | estimator | β∗  | is  | used. | It is defined |     | as  |     |     |     |     |     |     |     |
| ----- | --------- | --- | --- | ----- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
k
|     |     |     |     |     |          |     |          | J   |       | J        |         |     |     |      |
| --- | --- | --- | --- | --- | -------- | --- | -------- | --- | ----- | -------- | ------- | --- | --- | ---- |
|     |     |     |     |     |          |     | (cid:88) |     |       | (cid:88) |         |     |     |      |
|     |     |     |     | β∗  | = argmin |     | | y−     | x β | |2 +λ | wˆ       | |β |    |     |     | (12) |
|     |     |     |     | k   |          | β   |          | j   | j,k n |          | j,k j,k |     |     |      |
|     |     |     |     |     |          |     | j=1      |     |       | j=1      |         |     |     |      |
with the weights vector βˆ |γ. βˆ denotes a root-n consistent estimator such as ordinary least
|     |     |     | wˆ  | =   | 1/ | |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
k
| squares | (Zou, | 2006). |     |     |     |     |     |     |     |     |     |     |     |     |
| ------- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
LetusnowrelatetheabstractnotationY to∆Pd,s . ThedistributionF(θd,s)isfittedtoall∆Pd,s αd,s 1.
|     |     |     |     |     |     | i   |      |     |     |     |     |     |      | | = |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | ---- | --- |
|     |     |     |     |     |     |     | ID,t |     |     |     | t   |     | ID,t | t   |
The abstract index i = 1,...,N is replaced by the combination of the superscript index d = 1,...,D and
the subscript index t = 1,...,T. We fit 24 models each day, one for each delivery period s. The delivery
periods are treated as independent. Thereby, we yield an estimated vector of four distribution parameters
θˆd,s (µd,s,σd,s,τd,sνd,s)andaccordinglyparameterestimatesβd,s thatconditionθˆd,s
| =   |           |                     |           |     |     |     |     |     |     |     |     | onourexplanatory |     |     |
| --- | --------- | ------------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- |
| t   | (cid:98)t | (cid:98)t (cid:98)t | (cid:98)t |     |     |     |     |     | k   |     |     | t                |     |     |
19

variables. Analogously, we can also define the the vector θd,s (θd,s,...,θd,s) along the time-axis t. We
=
|     |     |     |     |     |     |     |     |     | k   | 1,k | T,k |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
explain all moments of the distribution by the same set of explanatory variables. Narajewski and Ziel
(2020a) choose F as Student’s t-distribution. Here, we extend their choice to the skewed Student’s t-
distribution and Johnson’s distribution. Both distributions have four parameters. A short description
S
U
| of the distributions |              | used | can       | be  | found  | in the | Appendix |              | B.  |     |     |     |     |
| -------------------- | ------------ | ---- | --------- | --- | ------ | ------ | -------- | ------------ | --- | --- | --- | --- | --- |
| For each             | distribution |      | parameter |     | k, the | model  | for      | θˆd,s reads: |     |     |     |     |     |
t,k
| g   | (θd,s) | = β              |                    |           |                    |       |                          |                    |           |                |           |     |     |
| --- | ------ | ---------------- | ------------------ | --------- | ------------------ | ----- | ------------------------ | ------------------ | --------- | -------------- | --------- | --- | --- |
| k   | t,k    | k1(k≥2),0        |                    |           |                    |       |                          |                    |           |                |           |     |     |
|     |        | 3                |                    |           | 6                  |       |                          |                    |           | 12             |           |     |     |
|     |        | (cid:88)         | ∆Pd,s              |           | (cid:88)           |       | ∆Pd,s                    |                    |           | (cid:88) ∆Pd,s |           |     |     |
|     |        | + β              |                    |           | +                  | β     | |                        |                    | | +β      | |              | |         |     |     |
|     |        | k,j              | ID,t−j             |           |                    | k,3+j |                          | ID,t−j             | 10        | ID,t−j         |           |     |     |
|     |        | j=1              |                    |           | j=1                |       |                          |                    |           | j=7            |           |     |     |
|     |        | (cid:124)        | (cid:123)(cid:122) | (cid:125) | (cid:124)          |       |                          | (cid:123)(cid:122) |           |                | (cid:125) |     |     |
|     |        | Pricedifferences |                    |           |                    |       | Absolutepricedifferences |                    |           |                |           |     |     |
|     |        | +β MON(d)+β      |                    |           | SAT(d)+β           |       |                          | SUN(d)             |           |                |           |     |     |
|     |        | k,11             |                    |           | k,12               |       | k,13                     |                    |           |                |           |     |     |
|     |        | (cid:124)        |                    |           | (cid:123)(cid:122) |       |                          |                    | (cid:125) |                |           |     |     |
Timedummies
|     |     | Lˆd,s     |     |      | Wˆ d,s             |      | Sˆd,s |      | Od,s      |     |     |     |     |
| --- | --- | --------- | --- | ---- | ------------------ | ---- | ----- | ---- | --------- | --- | --- | --- | --- |
|     |     | +β        | +β  |      |                    | +β   |       | +β   |           |     |     |     |     |
|     |     | k,14      | DA  | k,15 | DA                 | k,17 | DA    | k,18 | DA        |     |     |     |     |
|     |     | (cid:124) |     |      | (cid:123)(cid:122) |      |       |      | (cid:125) |     |     |     |     |
Day-aheadfundamentalvariables
|     |     | ∆Wˆ       | d,s,+ |     | ∆Wˆ  | d,s,− |                    | ∆Sˆd,s,+ |       | ∆Sˆd,s,− |           |     |      |
| --- | --- | --------- | ----- | --- | ---- | ----- | ------------------ | -------- | ----- | -------- | --------- | --- | ---- |
|     |     | +β        |       | +β  |      |       | +β                 |          |       | +β       |           |     | (13) |
|     |     | k,19      | DA,ID |     | k,20 | DA,ID |                    | k,21     | DA,ID | k,22     | DA,ID     |     |      |
|     |     | (cid:124) |       |     |      |       | (cid:123)(cid:122) |          |       |          | (cid:125) |     |      |
Day-ahedtointradayforecastupdates
+β σd,s (∆Wˆ )+β σd,s (∆Sˆ)+ β ∆Od,s,planned+β ∆Od,s,unplanned
|     |     | k,23 |       |     | k,24 |       |     |     | k,25 |       | k,26 |       |     |
| --- | --- | ---- | ----- | --- | ---- | ----- | --- | --- | ---- | ----- | ---- | ----- | --- |
|     |     |      | DA,ID |     |      | DA,ID |     |     |      | DA,ID |      | DA,ID |     |
(cid:124) (cid:123)(cid:122) (cid:125) (cid:124) (cid:123)(cid:122) (cid:125)
Standarddeviationofforecastupdates Intradaychangesinplannedandunplannedoutages
|     |     | αd,s      |                    |      | αd,s      |                           | Pd,s | −Pd,s              |           |     |     |     |     |
| --- | --- | --------- | ------------------ | ---- | --------- | ------------------------- | ---- | ------------------ | --------- | --- | --- | --- | --- |
|     |     | +β        | +β                 |      | +         | β                         | |    |                    |           | |   |     |     |     |
|     |     | k,27      | t−1                | k,28 | t−2       | k,29                      |      | DA                 | ID,t−1    |     |     |     |     |
|     |     | (cid:124) | (cid:123)(cid:122) |      | (cid:125) |                           |      |                    |           |     |     |     |     |
|     |     |           |                    |      |           | (cid:124)                 |      | (cid:123)(cid:122) | (cid:125) |     |     |     |     |
|     |     |           | Laggedαd,s         |      |           | Day-aheadtot−1pricespread |      |                    |           |     |     |     |     |
t
3
(cid:88)
|     |     | + β |        | MOd,s | +β        | f        | (t)+β |                    | SIDC(d,t) |           |     |     |     |
| --- | --- | --- | ------ | ----- | --------- | -------- | ----- | ------------------ | --------- | --------- | --- | --- | --- |
|     |     |     | k,29+j | j     |           | k,32 TTD |       | k,33               |           |           |     |     |     |
|     |     | j=1 |        |       | (cid:124) |          |       | (cid:123)(cid:122) |           | (cid:125) |     |     |     |
TimetodeliveryandSIDCclosing
|     |     | (cid:124) | (cid:123)(cid:122) |     | (cid:125) |     |     |     |     |     |     |     |     |
| --- | --- | --------- | ------------------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Slopeofthemerit-order
fork 1,2,3,4. Theinterceptisonlyincludedfork 2asthepricedifferencesareassumedtobecentred
| =   |     |     |     |     |     |     |     | ≥   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
around 0, as indicated by the summary statistics in Table 1. The volatility is expected to rise with higher
absolutepastpricedifferences,onweekends,andwithhigherRESgeneration. Thestrongchangesbetween
day-ahead and intraday RES and demand forecasts should also imply higher volatility. We expect the
volatility to decrease with more recent trading activity measured by lagged αd,s. SIDC(d,t) is a dummy
t
variable taking the value 1 for d ≥ June 18, 2018 and 26 ≤ t ≤ 31, indicating that the cross-country
order books are closed. f (t) models the non-linear impact of the time to delivery and takes the form
|     |     | √   | TTD |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
−t+1. It is a deterministic transformation of the variable and can thus be calculated
| f (t) | = 1/ | T   |     |     |     |     |     |     |     |     | t   |     |     |
| ----- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TTD
ex-ante. As argued already in Section 3.3, we expect a steeper merit-order regime to lead to higher price
volatility. Similar expectations hold for the kurtosis, i.e. we expect a steep merit-order regime to lead to
| heavier        | tails | of the distribution. |     |     |     |     |     |     |     |     |     |     |     |
| -------------- | ----- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4.3. Benchmark |       | Models               |     |     |     |     |     |     |     |     |     |     |     |
Lastly, some simple benchmark models are introduced. Even though the main focus of this paper is on
modellingthevolatilityanditsinfluencingfactor,simplebenchmarkscanserveasavaluablebenchmarkto
20

identifypotentialareasformodelimprovement. Asourstudysharestheconceptualset-upwithNarajewski
andZiel(2020a),itisnaturaltoemploysimilarbenchmarkmodels. Additionally,wecompareourapproach
toclassicaltimeseriesmethodssuchasAutoRegressiveIntegratedMovingAverage(ARIMA)models. The
| following |     | section | introduces |     | these | models | in more | detail. |     |     |     |
| --------- | --- | ------- | ---------- | --- | ----- | ------ | ------- | ------- | --- | --- | --- |
Narajewski and Ziel (2020a) introduce six simple benchmark models to evaluate the value-added by more
complex models, briefly described in the following. For the exact specification we refer the reader to their
work.
|     | • The | Naive | benchmark |     | randomly |     | draws past | trajectories. |     |     |     |
| --- | ----- | ----- | --------- | --- | -------- | --- | ---------- | ------------- | --- | --- | --- |
• For and MV.t, a multivariate normal respectively t-distribution is fitted to the vector of
MV.N
|     | price | differences. |     | Forecasts |     | are | randomly drawn | from | the distribution. |     |     |
| --- | ----- | ------------ | --- | --------- | --- | --- | -------------- | ---- | ----------------- | --- | --- |
• The RW.N, RW.t and RW.t.mix.D are random-walk type of models, where the distribution
parametersareestimatedfromthein-sampledata. TheRW.t.mix.Dalsoincludesasimplemixture
|     | term | for | αd,s | by estimating |     | πd,s | as the empirical | mean | of αd,s. |     |     |
| --- | ---- | --- | ---- | ------------- | --- | ---- | ---------------- | ---- | -------- | --- | --- |
|     |      |     | t    |               |     | t    |                  |      | t        |     |     |
The closeness of intraday electricity markets to traditional equity markets invites the use of classical time
series models as benchmark. However, some attention to the unique time-structure of the intraday market
is necessary: As already noted in Section 2, for all delivery periods s on day d, trading starts at 15:00
on d−1. The same delivery hour on two following delivery days can have overlapping intraday trading
sessions. Thus, we cannot simply combine all trading sessions of a product, as it is done in equity markets.
We therefore can only estimate our time series models on the price differences between the start of the
trading period and the start of the simulation window. The GAMLSS-based approach does not suffer
from this limitation as we learn the coefficients from past data of the simulation windows directly. The
following paragraphs introduce the time series benchmark models formally.
| The | classic | ARIMA(p,k,q) |     |          | model | is defined | as follows: |      |          |               |      |
| --- | ------- | ------------ | --- | -------- | ----- | ---------- | ----------- | ---- | -------- | ------------- | ---- |
|     |         |              |     | (cid:32) |       |            | (cid:33)    |      | (cid:32) | (cid:33)      |      |
|     |         |              |     |          |       | p          |             |      |          | q             |      |
|     |         |              |     |          |       | (cid:88)   |             |      |          | (cid:88)      |      |
|     |         |              |     |          | 1−    | ϕ Li       | (1−L)∆Pd,s  | =    | δ+ 1+    | θ Li (cid:15) | (14) |
|     |         |              |     |          |       | i          |             | ID,t |          | i t           |      |
|     |         |              |     |          |       | i=1        |             |      |          | i=1           |      |
(cid:80)
is an ARIMA(p,k,q) process with drift δ/(1− ϕ ). L denotes the lag operator. A full treatment of
i
ARIMAmodelscanbefoundine.g. ShumwayandStoffer(2017). WeestimatetheARIMA(p,k,q)models
using the function in the package (Hyndman et al., 2020). The function uses a
|     |     | auto.arima() |     |     |     |     | forecast |     |     |     |     |
| --- | --- | ------------ | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
stepwise approach to fit the lag order for p and q based on the BIC and performs the KPSS unit-root
tests to evaluate the integration order k. For each delivery period d,s, we fit the model on all 5-minute
intervals between the start of trading on d−1, 15:00 and the start of the simulation period. The models
| are  | denoted     | as     | Auto.ARIMA. |                |     |            |           |     |     |     |     |
| ---- | ----------- | ------ | ----------- | -------------- | --- | ---------- | --------- | --- | --- | --- | --- |
| 5.   | Forecasting |        | Study       |                | and | Evaluation |           |     |     |     |     |
| 5.1. | Study       | Design |             | and Simulation |     |            | Algorithm |     |     |     |     |
We employ the well-known rolling window forecasting study design, which is common in energy price
forecasting (see e.g. Gianfreda and Bunn, 2018, Janke and Steinke, 2019, Narajewski and Ziel, 2020a,
Nowotarski and Weron, 2018, Uniejewski et al., 2019, Ziel et al., 2015). This setting reduces the impact of
structuralbreakswithinthedataandensuresarobustsettingforthecomparisonofpredictiveperformance
21

using the DM-test (Diebold, 2015, Diebold and Mariano, 2002). The scheme is visualized in Figure 10.
We train one model for each delivery hour on 365 days of in-sample data and issue forecasts for the next
delivery. Subsequently, the training data set is shifted forward by one day, the models are re-trained for
each delivery hour and forecasts are issued for the next day and henceforth. Keeping the length of the
training set constant we thus move through the test set. Our full data set ranges from January 2016 to
August 2020, holding in total N = 1618 days. The training set length is fixed to D = 365 days. The test
| set holds | L = 1256 | days.    |               |                          |     |          |            |     |     |     |
| --------- | -------- | -------- | ------------- | ------------------------ | --- | -------- | ---------- | --- | --- | --- |
|           |          | Training | set of length | D with days d=1,...,365. |     | Forecast | for d=366. |     |     |     |
n=1
n=2
n=3
n=4
| ... |     |     |     | ... |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
n=N −1
n=N
Training set of length D with days d=N,...,N +D−1. Forecast for d=N +D.
Figure 10.: Structure of the rolling window forecasting study. Blue denotes in-sample data, red denotes
|     | the | out-of-sample | forecast. |     |     |     |     |     |     |     |
| --- | --- | ------------- | --------- | --- | --- | --- | --- | --- | --- | --- |
Forecasts are issued for all delivery hours s = 0,...,23. For each delivery hour, the forecast consists of
j = 1,...,M paths with M = 1000 paths of t = 1,...,31 steps. Generally, let variables with superscript [j]
d,s,[j]
denotesimulatedvaluesonpathj andhenceP denotesthesimulationforsteptfordeliveryperiodd,s
ID,t
in the path j. The vector notation d,s,[j] d,s,[j] d,s,[j] is frequently used in the chapter on error
|     |     |     | P   | = (P | ,...,P | )   |     |     |     |     |
| --- | --- | --- | --- | ---- | ------ | --- | --- | --- | --- | --- |
|     |     |     | ID  | ID,1 | ID,31  |     |     |     |     |     |
metrics. For the simulation of the paths, an algorithm similar to the recursive Euler-Maruyama-Scheme is
used (Asmussen and Glynn, 2007, Narajewski and Ziel, 2020a). Each simulation starts 185 minutes and
ends 30 minutes before the start of physical delivery. For each simulation step and path j, the boolean
t
variable d,s,[j] is simulated times from the Bernoulli distribution d,s,[j] and the price difference
|     | α   |     | M   |     |     |     | B(π       | )   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- |
|     | t   |     |     |     |     |     | (cid:98)t |     |     |     |
d ,s,[j]
∆P d ,s ,[j] is sampled M times from the distribution F(θ(cid:98) ) = F(µ d ,s,[j] ,σ d,s,[j] ,ν d,s,[j] and τ d,s,[j] ). The
| I D   | ,t              |            |     |     | t   | (cid:98) t | (cid:98)t | (cid:98)t | (cid:98)t |     |
| ----- | --------------- | ---------- | --- | --- | --- | ---------- | --------- | --------- | --------- | --- |
| price | d,s,[j] is then | calculated | as: |     |     |            |           |           |           |     |
P
ID,t
|     |     |     | P d,s,[j] | = P d,s,[j] +∆P | d,s,[j] | ·α d,s,[j] | .   |     |     | (15) |
| --- | --- | --- | --------- | --------------- | ------- | ---------- | --- | --- | --- | ---- |
|     |     |     | ID,t      | ID,t−1          | ID,t    | t          |     |     |     |      |
The algorithm is visualized in Figure 11. The estimates for π d,s,[j] ,µ d,s,[j] ,σ d,s,[j] ,ν d,s,[j] and τ d,s,[j] for the
|     |     |     |     |     | (cid:98)t | (cid:98)t | (cid:98)t | (cid:98)t | (cid:98)t |     |
| --- | --- | --- | --- | --- | --------- | --------- | --------- | --------- | --------- | --- |
first step t = 1 are all equal, but begin to differ from t ≥ 2 onwards as the paths develop individually.
Therefore, the prediction matrix needs to be updated dynamically for each path and each step.
22

|     |                    |            |             |     | Simulatej=1,...,M. |                  |                     |     | CalculateP | d ,s ,[j]foreachpath. |     |
| --- | ------------------ | ---------- | ----------- | --- | ------------------ | ---------------- | ------------------- | --- | ---------- | --------------------- | --- |
|     | Predictbasedont−1. |            |             |     |                    |                  |                     |     |            | I D ,t                |     |
|     | Pr                 | e d ic t π | d , s , [j] |     |                    | α d, s , [ j ] ∼ | B (π d, s , [ j ] ) |     |            |                       |     |
t=1 (cid:98) 1 1 (cid:98) 1 P d ,s ,[j] = P d ,s +∆P d ,s ,[j]·α d,s,[j]
d ,s , [ j ] d , s ,[ j] d , s , [ j ] I D ,1 I D ,0 I D ,1 1
|     |     | a n d θ(cid:98) |     |     | ∆   | P I D , 1 | ∼ F (θ(cid:98) 1 ) |     |     |     |     |
| --- | --- | --------------- | --- | --- | --- | --------- | ------------------ | --- | --- | --- | --- |
1
|     | Pr  | e d ic t π | d , s , [j] |     | α   | d, s , [ j ] ∼ | B (π d, s , [ j ] ) |     |     |     |     |
| --- | --- | ---------- | ----------- | --- | --- | -------------- | ------------------- | --- | --- | --- | --- |
t=2 (cid:98) 2 2 (cid:98) 2 P d ,s ,[j] = P d ,s ,[j]+∆P d ,s ,[j]·α d,s,[j]
a n d d ,s , [ j ] d , s ,[ j] d , s , [ j ] I D ,2 I D ,1 I D ,2 2
|     |     | θ(cid:98) 2 |     |     | ∆   | P I D , 2 | ∼ F (θ(cid:98) 2 ) |     |     |     |     |
| --- | --- | ----------- | --- | --- | --- | --------- | ------------------ | --- | --- | --- | --- |
Predictπd,s,[j]
| t=3 |     | (cid:98)3             |             |     |     |              |              |     |     |     |     |
| --- | --- | --------------------- | ----------- | --- | --- | ------------ | ------------ | --- | --- | --- | --- |
|     |     | andθ(cid:98) d ,s,[j] |             |     |     |              |              |     |     |     |     |
|     |     | 3                     |             |     |     |              | ...          |     |     | ... |     |
|     |     |                       |             |     |     | d, s , [ j ] | d, s , [ j ] |     |     |     |     |
|     | Pr  | e d ic t π            | d , s , [j] |     | α   | ∼            | B (π )       |     |     |     |     |
t=T (cid:98) T T (cid:98) T P d ,s ,[j] = P d ,s ,[j ] +∆P d ,s ,[j]·α d,s,[j]
a n d d ,s , [ j ] ∆ P d , s ,[ j] ∼ F (θ(cid:98) d , s , [ j ] ) I D ,T I D ,T − 1 I D ,T T
|     |     | θ(cid:98) T |     |     |     | I D , T | T   |     |     |     |     |
| --- | --- | ----------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
Figure 11.: Simulation Algorithm. After t = 3, the steps until t = T are omitted. For each path j, an
individual regression matrix is created with the information of the path’s past development.
d,s,[j].
Together, the results of the right, green column yield the path vector P
ID
| 5.2. Forecast | Evaluation |     |     |     |     |     |     |     |     |     |     |
| ------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The mean and median trajectory are evaluated using the Root Mean Squared Error (RMSE) and Mean
Absolute Error (MAE) respectively. For the probabilistic evaluation of the generated scenarios the Energy
Score (ES), Continuously Ranked Probability Score (CRPS) and the empirical coverage ratio are used.
Additionally, the Winkler-Score (WS) is used to evaluate the coverage of an 100%-Prediction
|     |     |     |     |     |     |     |     |     | (1 − | α) · |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --- |
Interval (PI). The ES, CRPS and the WS are strictly proper scoring rules (Gneiting and Raftery, 2007,
Nowotarski and Weron, 2018, Ziel and Berk, 2019). To draw conclusions about the statistical significance
of the difference in forecasting performance for each model, the DM-test is used. All measures are widely
| employed  | in academia | and | practice. |             |     |     |     |     |     |     |     |
| --------- | ----------- | --- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| Formally, | the RMSE    | and | MAE       | are defined | as: |     |     |     |     |     |     |
(cid:118)
|     |     |     |      | (cid:117)   |                   |          |       |            | 2        |     |      |
| --- | --- | --- | ---- | ----------- | ----------------- | -------- | ------ | ---------- | --------- | --- | ---- |
|     |     |     |      | (cid:117)   | N                 | S T      |        | M          |           |     |      |
|     |     |     |      | (cid:117) 1 | (cid:88) (cid:88) | (cid:88) | d ,s   | 1 (cid:88) | d ,s ,[j] |     |      |
|     |     |     | RMSE | =           |                   |          | P −   | P          |  ,       |     | (16) |
|     |     |     |      | (cid:116)   |                   |          | I D ,t |            | I D ,t    |     |      |
|     |     |     |      | N ST        |                   |          |        | M          |           |     |      |
|     |     |     |      |             | d=1s=1            | t=1      |        | j=1        |           |     |      |
and:
|     |     |     |     | 1   | (cid:88)(cid:88)(cid:88)(cid:12) N | S T |                     |         | (cid:12)    |     |      |
| --- | --- | --- | --- | --- | ---------------------------------- | --- | ------------------- | ------- | ----------- | --- | ---- |
|     |     |     | MAE |     |                                    |     | (cid:12)Pd,s −med(P | d,s,[j] |             |     | (17) |
|     |     |     |     | =   |                                    |     |                     |         | ) (cid:12), |     |      |
|     |     |     |     | NST |                                    |     | (cid:12) ID,t       | ID,t    | (cid:12)    |     |      |
d=1s=1 t=1
Foran(1−α)·100%-PIwiththelowerandupperboundsL ,U andpredictionintervalwidthδ = Uˆ −Lˆ ,
|               |          |     |       |                 |     |     | t t |     |     | t   | t t |
| ------------- | -------- | --- | ----- | --------------- | --- | --- | --- | --- | --- | --- | --- |
| the empirical | Coverage |     | Ratio | (CR) is defined | as: |     |     |     |     |     |     |
(cid:40)
|     |     |     |     | 1   | N S               | T 1      | for Pd,s | ∈ [Lˆd,s,Uˆd,s] |     |     |      |
| --- | --- | --- | --- | --- | ----------------- | -------- | -------- | --------------- | --- | --- | ---- |
|     |     |     |     |     | (cid:88) (cid:88) | (cid:88) |          | t               | t   |     |      |
|     |     |     | CR  | =   |                   |          | ID,t     |                 |     |     | (18) |
|     |     |     |     | NST |                   |          | else.    |                 |     |     |      |
0
|     |     |     |     |     | d=1s=1 | t=1 |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
23

| The WSd,s | is defined |     | as: |     |     |     |     |     |     |     |     |     |     |
| --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t
|     |     |     |     |    |     |     |     | Pd,s | [Lˆd,s,Uˆd,s] |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------- | --- | --- | --- | --- |
|     |     |     |     |     | δ , |     |     | for  | ∈             |     |     |     |     |
|     |     |     |     |    | t   |     |     |      | ID,t t        | t   |     |     |     |

|     |     |     | WSd,s | =   | δ + | 2(Lˆd,s−Pd,s | ),   | for Pd,s | < Lˆd,s |     |     |     | (19) |
| --- | --- | --- | ----- | --- | --- | ------------ | ---- | -------- | ------- | --- | --- | --- | ---- |
|     |     |     |       | t   | t   | t            | ID,t |          | ID,t t  |     |     |     |      |
α
|                |     |     |     |  δ |     | 2(Pd,s | −Uˆd,s),                 | for Pd,s | Uˆd,s  |     |     |     |      |
| -------------- | --- | --- | --- | ---- | --- | ------ | ------------------------ | -------- | ------ | --- | --- | --- | ---- |
|                |     |     |     |      | t + |        |                          |          | >      |     |     |     |      |
|                |     |     |     |      |     | α ID,t | t                        |          | ID,t t |     |     |     |      |
| and aggregated |     | as: |     |      |     |        |                          |          |        |     |     |     |      |
|                |     |     |     |      |     |        | N                        | S T      |        |     |     |     |      |
|                |     |     |     |      |     | 1      | (cid:88)(cid:88)(cid:88) |          |        |     |     |     |      |
|                |     |     |     |      | WS  | =      |                          | WSd,s.   |        |     |     |     | (20) |
t
NST
|     |     |     |     |     |     |     | d=1s=1 | t=1 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
For both, CR and WS, the upper and lower bounds of the (1−α)·100% PI are defined by the respective
quantiles Lˆd,s = Q α/2 (P d,s,[j] ) and Uˆd,s = Q 1−α/2 (P d,s,[j] ), where Qτ (P d,s,[j] ) denotes the
|     | t   | j=1,...,M |     | ID,t |     | t   | j=1,...,M | ID,t |     | j=1,...,M |     | ID,t |     |
| --- | --- | --------- | --- | ---- | --- | --- | --------- | ---- | --- | --------- | --- | ---- | --- |
τ-th quantile of simulated d,s,[j] prices. Comparing both, WS and CR, one can see how the WS
|     |     | M   |     | P   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ID,t
penalizes for an observation outside the interval and rewards the forecaster at the same time for a more
narrow PI. Contrary to the CR, the WS is a strictly proper evaluation measure (Nowotarski and Weron,
2018).
The CRPS (see e.g. Gneiting and Raftery, 2007, Nowotarski and Weron, 2018) is approximated by the
| Pinball-Score | (PB) |     |     |     |     |         |     |          |     |     |     |     |      |
| ------------- | ---- | --- | --- | --- | --- | ------- | --- | -------- | --- | --- | --- | --- | ---- |
|               |      |     |     |     |     |         | 1   | (cid:88) |     |     |     |     |      |
|               |      |     |     |     |     | CRPSd,s | =   | PBd,s    |     |     |     |     | (21) |
|               |      |     |     |     |     | t       |     | t,τ      |     |     |     |     |      |
R
τ∈T
PBd,s
for a dense equidistant grid of probabilities T = {0.01,...0.99} of size R = 99. denotes the pinball
t,τ
| loss for | probability | τ.  | The formula |     | is given  | by:     |         |     |      |           |      |         |      |
| -------- | ----------- | --- | ----------- | --- | --------- | ------- | ------- | --- | ---- | --------- | ---- | ------- | ---- |
|          |             |     | (cid:40)    |     |           | d,s,[j] | )−Pd,s) | for | Pd,s |           |      | d,s,[j] |      |
|          |             |     | (1−τ)·(Qτ   |     |           | (P      |         |     | ≤    | Qτ        | (P   | )       |      |
|          | PBd,s       | =   |             |     | j=1,...,M | ID,t    |         | t,j | ID,t | j=1,...,M | ID,t |         | (22) |
t,τ
|             |      |     | τ ·(Pd,s   | −Qτ  |              | (P   | d,s,[j] ))               | else.    |     |     |     |     |      |
| ----------- | ---- | --- | ---------- | ---- | ------------ | ---- | ------------------------ | -------- | --- | --- | --- | --- | ---- |
|             |      |     |            | ID,t | j=1,...,M    | ID,t |                          |          |     |     |     |     |      |
| The overall | CRPS | is  | calculated | by   | the average: |      |                          |          |     |     |     |     |      |
|             |      |     |            |      |              | 1    | N                        | S T      |     |     |     |     |      |
|             |      |     |            |      |              |      | (cid:88)(cid:88)(cid:88) | CRPSd,s. |     |     |     |     |      |
|             |      |     |            |      | CRPS         | =    |                          |          |     |     |     |     | (23) |
|             |      |     |            |      |              | NST  |                          |          | t   |     |     |     |      |
|             |      |     |            |      |              |      | d=1s=1                   | t=1      |     |     |     |     |      |
The pinball loss is also used to evaluate the performance of different models in specific quantile levels. For
| this reason, | the | PB is | aggregated | as  | follows: |     |                          |        |     |     |     |     |      |
| ------------ | --- | ----- | ---------- | --- | -------- | --- | ------------------------ | ------ | --- | --- | --- | --- | ---- |
|              |     |       |            |     |          |     | N                        | S T    |     |     |     |     |      |
|              |     |       |            |     |          | 1   | (cid:88)(cid:88)(cid:88) |        |     |     |     |     |      |
|              |     |       |            |     | PB       | =   |                          | PBd,s. |     |     |     |     | (24) |
|              |     |       |            |     | τ        |     |                          |        | t,τ |     |     |     |      |
NST
|     |     |     |     |     |     |     | d=1s=1 | t=1 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
To measure the quality of the generated paths, Narajewski and Ziel (2020a) propose the ES. It is a
generalisation of the CRPS for two dimensions. Thereby, not only the approximation of the marginal
distribution is evaluated, but the generated multivariate distribution (Gneiting and Raftery, 2007, Ziel
| and Berk, | 2019): |     |                    |          |     |                   |     |            |                            |     |     |                   |     |
| --------- | ------ | --- | ------------------ | -------- | --- | ----------------- | --- | ---------- | -------------------------- | --- | --- | ----------------- | --- |
|           |        |     | M                  |          |     |                   |     |            | M M                        |     |     |                   |     |
|           |        |     | 1 (cid:88)(cid:12) | (cid:12) |     | (cid:12) (cid:12) |     | 1 (cid:88) | (cid:88) (cid:12) (cid:12) |     |     | (cid:12) (cid:12) |     |
ESd,s = (cid:12) (cid:12)Pd,s−P d,s,[j] (cid:12) (cid:12) − (cid:12) (cid:12)P d,s,[j] −P d,s,[i] (cid:12) (cid:12) . (25)
|     |     |     | (cid:12)(cid:12) | ID  | ID  | (cid:12)(cid:12) |        |          | (cid:12)(cid:12) | ID  | ID  | (cid:12)(cid:12) |     |
| --- | --- | --- | ---------------- | --- | --- | ---------------- | ------ | -------- | ---------------- | --- | --- | ---------------- | --- |
|     |     |     | M                |     |     | 2                | ·M ·(M | −1)      |                  |     |     | 2                |     |
|     |     |     | j=1              |     |     |                  |        | j=1i=j+1 |                  |     |     |                  |     |
24

| The average | yields | the overall | energy | score | for each | model: |     |     |     |     |
| ----------- | ------ | ----------- | ------ | ----- | -------- | ------ | --- | --- | --- | --- |
|             |        |             |        |       |          | N S    |     |     |     |     |
1 (cid:88)(cid:88)
|     |     |     |     |     | ES  | ESd,s. |     |     |     | (26) |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | ---- |
=
NS
d=1s=1
The aforementioned measures provide insight in the accuracy of different forecasting models. To evaluate
the statistical significance of the difference in forecast accuracy of two models A and B, the DM-test
(Diebold, 2015, Diebold and Mariano, 2002) is routinely employed in the field of energy price forecasting
(Janke and Steinke, 2019, Nowotarski and Weron, 2018, Ziel and Weron, 2018). It originally stems from
the field of point forecasting, however Diebold (2015) notes that the test is agnostic to the scoring rule
used to evaluate forecasts. Hence, using strictly proper probabilistic scoring rules, such as the CRPS and
ES loss, the DM test can be applied to probabilistic forecasts as well (see e.g. Diebold, 2015, Nowotarski
and Weron, 2018). Following Narajewski and Ziel (2020a) and Ziel and Weron (2018), the DM-test is
employed in a multivariate fashion. Hence, let Ld (Ld,1,...,Ld,S) and Ld (Ld,1,...,Ld,S) denote the
|     |     |     |     |     | =   |     |     | =   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | A   | A   | A   | A B | B   |     |
out-of-sample loss vectors for model A and B for day d and delivery period s of length N. For models
A,B, the N ×S vector of losses are reduced to an N ×1 vector by taking the 1-norm. The difference
| between | both is the | loss differential |     | used | in the DM-test.                        |                                     |                   |     |     |      |
| ------- | ----------- | ----------------- | --- | ---- | -------------------------------------- | ----------------------------------- | ----------------- | --- | --- | ---- |
|         |             |                   |     |      | (cid:12)(cid:12)                       | (cid:12)(cid:12) (cid:12)(cid:12)   | (cid:12)(cid:12)  |     |     |      |
|         |             |                   |     | ∆Ld  | (cid:12)(cid:12)Ld(cid:12)(cid:12)     | −(cid:12)(cid:12)Ld(cid:12)(cid:12) |                   |     |     | (27) |
|         |             |                   |     |      | =                                      |                                     | .                 |     |     |      |
|         |             |                   |     |      | A,B (cid:12)(cid:12) A(cid:12)(cid:12) | (cid:12)(cid:12)                    | B(cid:12)(cid:12) |     |     |      |
|         |             |                   |     |      |                                        | 1                                   | 1                 |     |     |      |
For example, for the ES and the model, the loss vector Ld (ESd,1 ,...,ESd,S ).
|     |     |     | Naive |     |     |     | =     |       |       |     |
| --- | --- | --- | ----- | --- | --- | --- | ----- | ----- | ----- | --- |
|     |     |     |       |     |     |     | Naive | Naive | Naive |     |
We test the loss differential series for stationarity using the augmented Dickey-Fuller (ADF) test (Dickey
and Fuller, 1979, 1981) and reject the of unit root at the 5% significance level for all loss differential
|     |     |     |     | H   | 0   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
series. Harveyetal.(1997)proposetheusageofthet-distributionwithν = N−1degreesoffreedomrather
than the normal distribution, as well as the introduction of a bias correction. Formally, the corrected test
(cid:113)
statistic is defined as tHLN,h=1 = N+3 ·t ∼ t(0,1,N −1) under the H , where N is the length of
|     |     | DM  |     |     | DM  |     |     | 0   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
N
the loss differential series ∆Ld and denotes the forecast horizon. The standard deviation is computed
h
A,B
usinganautocorrelation-consistentestimator. Foreachmodelpair, twoone-sidedDM-testsarecomputed.
The first test has the H that the forecasts of model A are significantly better than the forecasts of model
0
B. For the second test, the is that the forecasts of model are significantly better than the forecasts
|     |     |     | H   |     |     |     | B   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
of model A. These tests are complimentary. We use the implementation in the R-package
forecast
| (Hyndman | and Khandakar, |     | 2008, | Hyndman | et al., 2020). |     |     |     |     |     |
| -------- | -------------- | --- | ----- | ------- | -------------- | --- | --- | --- | --- | --- |
6. Results
The following chapter presents the results of the forecasting study. It is split into two parts: First, we
show the error metrics for the out-of-sample analysis. Additionally, we show the in-sample coefficients for
| the model | using Johnson’s |     | S distribution. |     |     |     |     |     |     |     |
| --------- | --------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
U
6.1. Out-of-sample Analysis: Forecasting Performance on Test Data
First,theaggregateerrorstatisticswillbepresented,followedbythescoringrulesconsideringthemarginal
fit relative to the time to delivery and the quantile range T. Statistical significance is evaluated using the
| Diebold-Mariano | test. |     |     |     |     |     |     |     |     |     |
| --------------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
25

The performs best in terms of RMSE and MAE, while performs best across the prob-
| Naive |     |     |     |     |     | Mix.JSU |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
abilistic evaluation using the CRPS and ES scoring rules. Its superior performance in terms of ES is
statistically significant according to the DM-test. The GAMLSS-based model assuming the skew-t dis-
tribution however shows a very poor performance for hour 6, which yields an overall poor performance.
For this delivery period, we can trace the high error back to outliers and extreme ∆Pd,s larger than 2000
ID,t
EUR/MWh on March 11th, 2020. This indicates that Johnson’s S is more robust towards outliers. An
U
investigationofthelosstimeseriesforMix.JSUandMix.SSTshowsthedeterioratingforecastingperfor-
manceoftheMix.SSTafterMarch11th,2020clearly(seeFigure21inAppendixC).TheAuto.ARIMA
performs surprisingly bad in terms of the RMSE and MAE and somewhat better in terms of the CRPS
and ES. With respect to the other benchmark models, we see an overall mixed performance. We note a
worse performance for the benchmark models for the probabilistic measures CRPS and ES compared to
| the | and Mix.JSU. |     |     |     |     |     |     |     |     |     |
| --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Naive
Table 4.: Aggregate error statistics for the MAE, RMSE, CRPS, ES and the CR and WS for the 50%,
90% and 99% prediction interval. Colour indicates performance. The best value for each scoring
rule is highlighted.
|     |     | Aggregate | Statistics |     | Coverage | Ratio |      |     | Winkler Score |      |
| --- | --- | --------- | ---------- | --- | -------- | ----- | ---- | --- | ------------- | ---- |
|     | MAE | RMSE      | CRPS       | ES  | CR       | CR    | CR   | WS  | WS            | WS   |
|     |     |           |            |     | 0.5      | 0.9   | 0.99 | 0.5 | 0.9           | 0.99 |
Naive 3.178 6.564 1.222 17.271 0.491 0.892 0.984 8.676 12.922 36.218
| Auto.ARIMA | 3.295 | 7.240 | 1.313 | 18.623 | 0.407 | 0.713 | 0.845 | 9.544 |       |        |
| ---------- | ----- | ----- | ----- | ------ | ----- | ----- | ----- | ----- | ----- | ------ |
|            |       |       |       |        |       |       |       |       | 9.269 | 13.656 |
MV.N 3.193 6.570 1.275 18.009 0.680 0.927 0.972 9.364 16.392 25.500
MV.t 3.191 6.570 1.240 17.495 0.622 0.930 0.986 8.805 15.972 33.279
RW.N 3.209 6.577 1.472 20.030 0.824 0.970 0.989 12.098 25.726 39.947
RW.t 3.195 6.686 1.323 18.393 0.748 0.968 0.996 9.888 23.068 63.616
RW.t.Mix.D 3.192 6.616 1.304 18.171 0.726 0.964 0.996 9.624 21.941 61.102
| Mix.JSU | 3.182 | 6.571 |       |        | 0.628 | 0.947 | 0.991 |       | 16.763 | 31.549 |
| ------- | ----- | ----- | ----- | ------ | ----- | ----- | ----- | ----- | ------ | ------ |
|         |       |       | 1.218 | 17.127 |       |       |       | 8.519 |        |        |
Mix.SST 4.509 109.661 1.748 28.247 0.604 0.936 0.989 12.427 17.356 33.674
Figure 12 shows the ES relative to the delivery hours s. Relative to the Naive, the GAMLSS-based
models show an improved forecasting performance in the peak hours (Plot 12 b). The error of the
RW.N
| and     | models | explodes | for hour | 6.  |     |     |     |     |     |     |
| ------- | ------ | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| Mix.SST |        |          |          | s = |     |     |     |     |     |     |
The PB over is shown in Figure 13. Again, subfigure (a) represents absolute values
T = 0.01,...,0.99
and (b) depicts all models relative to the Naive. All models show similar performance in the central
quantiles, as already indicated by the very close values for the MAE. Relative to the Naive, most other
benchmark models show worse performance in the tails of the distribution. The shows an
Mix.JSU
improved modelling of the tails compared to the Naive. The again shows a weak performance
Mix.SST
given by its sensitivity to outliers. The development of the CRPS throughout the simulation window is
shown in Figure 14. Again, (a) shows absolute values while (b) shows the error relative to Naive. The
CRPS is rising through the simulation window, especially for the last 60 to 30 minutes of trading. The
relative error of most models towards the Naive decreases throughout the simulation window, however, it
increases for the Auto.ARIMA. This might indicate that learning the model parameters of past trading
sessions can be beneficial compared to learning the parameters only from the trading session of interest,
before the start of the simulation, as market behaviour changes throughout the session.
26

| 24  |     |     | 1.30 |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- |
Model
|     |     |     |      |     | Naive      | MV.t | RW.t.Mix.D |
| --- | --- | --- | ---- | --- | ---------- | ---- | ---------- |
| 22  |     |     | 1.25 |     | Auto.ARIMA | RW.N | Mix.JSU    |
|     |     |     |      |     | MV.N       | RW.t | Mix.SST    |
1.20
eviaN ot oitar SE
20
1.15
SE 18
1.10
16
1.05
Model
|     | Naive | MV.t RW.t.Mix.D |     |     |     |     |     |
| --- | ----- | --------------- | --- | --- | --- | --- | --- |
14
|     | Auto.ARIMA | RW.N Mix.JSU | 1.00 |     |        |     |     |
| --- | ---------- | ------------ | ---- | --- | ------ | --- | --- |
|     | MV.N       | RW.t Mix.SST |      |     |        |     |     |
| 12  |            |              | 0.95 |     |        |     |     |
| 0   | 4 8        | 12 16 20     | 0    | 4 8 | 12     | 16  | 20  |
|     |            | Hour s       |      |     | Hour s |     |     |
(a) ES over hours s=0,...,23. (b) Relative to Naive over hours s=0,...,23.
Figure 12.: Plot (a) shows the ES and (b) its ratio to Naive over the delivery hours s.
Model
|     |     |     | 2.0 | Naive      | MV.t | RW.t.Mix.D |     |
| --- | --- | --- | --- | ---------- | ---- | ---------- | --- |
| 2.0 |     |     |     | Auto.ARIMA | RW.N | Mix.JSU    |     |
eviaN ot evitaler oitaR BP 1.8
|     |     |     |     | MV.N | RW.t | Mix.SST |     |
| --- | --- | --- | --- | ---- | ---- | ------- | --- |
1.6
1.5
| BP  |     |     | 1.4 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
1.0
1.2
Model
|     | Naive | MV.t RW.t.Mix.D | 1.0 |     |     |     |     |
| --- | ----- | --------------- | --- | --- | --- | --- | --- |
0.5
|     | Auto.ARIMA | RW.N Mix.JSU |     |     |     |     |     |
| --- | ---------- | ------------ | --- | --- | --- | --- | --- |
0.8
|     | MV.N | RW.t Mix.SST |     |     |     |     |     |
| --- | ---- | ------------ | --- | --- | --- | --- | --- |
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
|     | (a) | PB . |     | (b) Relative | to Naive. |     |     |
| --- | --- | ---- | --- | ------------ | --------- | --- | --- |
τ
Figure 13.: Plot (a) shows the PB and (b) its ratio to Naive over the quantile range T.
The results are largely confirmed as statistically significant by the Diebold-Mariano-Test. Figure 15 shows
the p-values for the pairwise DM-tests for the ES and CRPS. The lower the p-value, the more significant
is the difference in the forecasting performance, which implies that the model on the column (or x-axis)
outputs superior forecasts than the model on the row (or y-axis). Generally, the p-values for the CRPS
and ES are rather close. This makes sense, as a good coupling to the path’s distribution should be closely
related to a good fit on the marginal distribution. The other way, however, is not necessarily true. Inside
the group of the benchmark models, the Naive model is confirmed as the superior model as it yields
significantly better forecasting performance than all other benchmark models. The Auto.ARIMA is
significantly better as the only. The yields significantly better forecasting performance
RW.N Mix.JSU
than all other models in terms of the ES. The yields significantly worse forecasting accuracy in
Mix.SST
terms of both CRPS and ES than all other models, which is expected given the results shown in Figures
12 to 14.
27

| 3.0 |       |     |       |            |     | 1.4 |            |       |      |            |     |
| --- | ----- | --- | ----- | ---------- | --- | --- | ---------- | ----- | ---- | ---------- | --- |
|     |       |     | Model |            |     |     |            | Model |      |            |     |
|     | Naive |     | MV.t  | RW.t.Mix.D |     |     | Naive      |       | MV.t | RW.t.Mix.D |     |
| 2.5 |       |     |       |            |     |     | Auto.ARIMA |       | RW.N | Mix.JSU    |     |
Auto.ARIMA RW.N Mix.JSU eviaN ot evitaler oitaR sSPRC 1.3 MV.N RW.t Mix.SST
|     | MV.N |     | RW.t | Mix.SST |     |     |     |     |     |     |     |
| --- | ---- | --- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- |
2.0
1.2
sSPRC
1.5
1.1
1.0
1.0
0.5
| 0.0 |     |     |     |     |     | 0.9 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
185175165155145135125115105 95 85 75 65 55 45 35 185175165155145135125115105 95 85 75 65 55 45 35
|     |     |     | Time to Delivery [Minutes] |     |     |     |     |     | Time to Delivery [Minutes] |           |     |
| --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | -------------------------- | --------- | --- |
|     |     | (a) | CRPS over                  | t.  |     |     |     | (b) | Relative                   | to Naive. |     |
t
Figure 14.: Plot (a) shows the CRPS and (b) its ratio to Naive over the time to delivery.
|     | Naive | 1   | 1 1 1 | 1 0.1 | 1 1      |     | Naive | 1   | 1 1 | 1 1 | 0 1 1      |
| --- | ----- | --- | ----- | ----- | -------- | --- | ----- | --- | --- | --- | ---------- |
|     | MV.N  |     |       |       |          |     | MV.N  |     |     |     |            |
|     |       | 0   | 0 1 1 | 1 0   | 1 1      |     |       | 0   | 0 1 | 1 1 | 0 1 1      |
|     | MV.t  | 0 1 | 1 1   | 1 0   | 1 1 0.10 |     | MV.t  | 0 1 | 1   | 1 1 | 0 1 1 0.10 |
0.08 0.08
|     | RW.N | 0 0 | 0 0 | 0 0 | 0.98 0 |     | RW.N | 0 0 | 0   | 0 0 | 0 1 0 |
| --- | ---- | --- | --- | --- | ------ | --- | ---- | --- | --- | --- | ----- |
eulaV-p eulaV-p
0.06 0.06
|     | RW.t | 0 0 | 0 1 | 0 0 | 1 0.08 |     | RW.t | 0 0 | 0 1 | 0   | 0 1 0.99 |
| --- | ---- | --- | --- | --- | ------ | --- | ---- | --- | --- | --- | -------- |
0.04 0.04
| RW.t.Mix.D |     | 0 0 | 0 1 1 | 0   | 1 0.87 | RW.t.Mix.D |     | 0 0 | 0 1 | 1   | 0 1 1 |
| ---------- | --- | --- | ----- | --- | ------ | ---------- | --- | --- | --- | --- | ----- |
0.02 0.02
|     | Mix.JSU | 0.9 1 | 1 1 1 | 1   | 1 1 |     | Mix.JSU | 1 1 | 1 1 | 1 1 | 1 1 |
| --- | ------- | ----- | ----- | --- | --- | --- | ------- | --- | --- | --- | --- |
0.00 0.00
| Mix.SST |     | 0 0 | 0 0.02 0 | 0 0 | 0   |     | Mix.SST | 0 0 | 0 0 | 0 0 | 0 0 |
| ------- | --- | --- | -------- | --- | --- | --- | ------- | --- | --- | --- | --- |
Auto.ARIMA 0 0 0 1 0.92 0.13 0 1 Auto.ARIMA 0 0 0 1 0.01 0 0 1
eviaN N.VM t.VM N.WR t.WR D.xiM.t.WR USJ.xiM TSS.xiM AMIRA.otuA eviaN N.VM t.VM N.WR t.WR D.xiM.t.WR USJ.xiM TSS.xiM AMIRA.otuA
|     | (a) Continuous |     | Ranked | Probability | Score. |     |     | (b) | Energy | Score. |     |
| --- | -------------- | --- | ------ | ----------- | ------ | --- | --- | --- | ------ | ------ | --- |
Figure 15.: Pairwise p-values for the DM-test for the CRPS and ES loss. The closer the p-value to 0, the
more significant is the difference between the model on the column (better) and the model on
|     | the | row | (worse). |     |     |     |     |     |     |     |     |
| --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
28

6.2. In-sample Analysis: Estimated Coefficients and their Development
Given the strong probabilistic forecasting performance of the Mix.JSU we turn to an in-sample analysis
of the estimated coefficients. Compared to black-box deep learning algorithms, the parametric GAMLSS
framework used in this paper allows for explainable machine learning by quantitatively and qualitatively
analysing the estimated coefficients. Hence, we can gain further insight in the driving variables for all
distribution parameters. Tables 5 to 8 present the estimated scaled coefficients for d = January 22nd,
2017, the first out-of-sample day. Scaled coefficient correspond to mean-variance scaled inputs. Hence,
the coefficients are hence unit-free and can be compared in the magnitude. The background colouring
indicates the share of non-zero estimates for the whole out-of-sample data set. Green indicates that few
estimates are set to zero by the sparsity property of the LASSO, the darker the red, the more estimates
are set to zero.
For µ, only the first lag of ∆Pd,s shows more than a couple non-zero values for the first day of the test set.
ID,t
This variable yields non-zero estimates as well across the test set for the late morning to afternoon peak
hours. This result is similar to the findings of Narajewski and Ziel (2020b), who find the most recent price
tobeamongthemostimportantfeaturesforforecastingtheID aswellaswiththeresultsofKremeretal.
3
(2020, 2021), who find that lagged prices are an important predictor. The fact that other fundamental
and trading related information, especially intraday forecast changes, do not yield additional predictive
power suggests that this information is contained in the price already. These results support the notion
of weak-form market efficiency already indicated by Narajewski and Ziel (2020b) and Kuppelwieser and
Wozabal (2021).
For the volatility σ, we present coefficients in similar fashion in Table 6. For the first day of the test
set, we yield non-zero estimates for the coefficients for the merit-order slope, for the intercept and for
the transformed time to delivery. For a few hours, the coefficient for lagged values of αd,s has a negative
t
non-zero estimate as well. The large and positive coefficients for the merit-order slope confirm our initial
assumption that the shape of the merit-order is a driving factor for the volatility in intraday markets.
Intuitively, this is derived from the observation that on a steep merit-order, a slight change in supply or
demandhasahigherimpactonthepricethaninaflatregime. Movingthiseffectfromathresholdvariable
for the size of ∆Pd,s to the volatility parameter of the distribution of ∆Pd,s thus generalizes the results
ID,t ID,t
of Kremer et al. (2020, 2021). Contrary to Baule and Naumann (2021), we find little predictive power for
the spread between spot and intraday price as well as for the fundamental forecasts and their intraday
changes for the volatility. Remember that the coefficients in Table 6 correspond to January 22nd, 2017,
wellbeforetheintroductionofSIDC.Thus, theSIDCvariableiszeroforthistrainingperiod. Weshowthe
evolution of the estimated coefficient across the rolling training set in Figure 16. After the launch of SIDC
on June 13, 2018, the dummy is first included in the rolling training set. A sizeable positive estimate is
visible, i.e. the volatility rises after gate closure of the cross-border shared order books 60 minutes before
delivery. The effect is the strongest in 2019 and 2020 for the morning and afternoon peak hours and less
clear for the solar peak hours around noon. Our findings are consistent with Narajewski and Ziel (2020a)
and contradict Kath (2019), who finds no evidence of rising volatility due to SIDC.
29

Table 5.: Estimated scaled coefficients for µ (expected value) on the first day of the test set.
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
αt−1 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
αt−2 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
|∆Pt−1| 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
|∆Pt−2| 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
|∆Pt−3| 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
|∆Pt−4| 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
|∆Pt−5| 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
|∆Pt−6| 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
(cid:80) ∆P i i = = t− 1 7 2 1 |∆Pt−i| - 0 0 . . 0 0 0 8 0 8 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 - 0 0 . . 0 0 0 8 0 4 0 0 . . 0 0 0 0 0 0 - 0 0 . . 0 0 0 7 0 1 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 8 0 0 0 0 . . 0 0 0 8 0 8 0 0 . . 0 1 0 1 0 5 0 0 . . 0 1 0 1 0 4 0 0 . . 0 0 0 4 0 7 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 7 0 1 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 4 0 5 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0
∆Pt−2 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
∆Pt−3 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.034 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
MO1000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
MO2000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
MO4000 0.000 0.000 0.000 0.000 0.000 0.036 0.000 0.000 0.000 0.028 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
LDA 0.001 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
ODA 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
∆O 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
∆Oplanned 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
∆Ounplanned 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
|PSpot−Pt−1| 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
SIDC 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
SDA 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
∆S− 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
∆S+ 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
σS 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
TTD 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.054 0.000
MON(d) 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
SAT(d) 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
SUN(d) 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
WDA 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
∆W− 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
∆W+ 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
σW 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.005 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
Table 6.: Estimated scaled coefficients for σ (scale / volatility) on the first day of the test set.
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Intercept -0.277 -0.302 -0.464 -0.700 -0.551 -0.206 -0.178 -0.490 -0.426 -0.060 -0.044 -0.551 -0.876 -0.700 -0.813 -0.918 -1.045 -0.724 -0.799 -0.730 -0.742 -0.727 -0.654 -0.347
αt−1 0.000 0.000 0.000 0.000 0.000 -0.052 0.000 0.000 -0.015 -0.167 -0.216 -0.094 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
αt−2 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
|∆Pt−1| 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.295 0.174 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
|∆Pt−2| 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
|∆Pt−3| 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
|∆Pt−4| 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
|∆Pt−5| 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
| (cid:80) ∆ ∆ P i i = = P t− 1 7 t− 2 1 6 |∆ | Pt−i| 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0
∆Pt−2 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
∆Pt−3 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
MO1000 0.000 0.177 0.000 0.267 0.047 0.000 0.000 0.101 0.319 0.198 0.038 0.131 0.000 0.000 0.000 0.000 0.049 0.138 0.228 0.000 0.000 0.000 0.000 0.150
MO2000 0.285 0.000 0.399 0.024 0.358 0.451 0.060 0.378 0.244 0.000 0.146 0.000 0.228 0.000 0.000 0.000 0.015 0.000 0.000 0.567 0.249 0.000 0.000 0.000
MO4000 0.239 0.471 0.459 0.680 0.352 0.000 0.222 0.000 0.000 0.252 0.213 0.170 0.264 0.405 0.420 0.572 0.705 0.831 0.454 0.000 0.336 0.355 0.315 0.183
L O ∆ D D O A A 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0
∆ ∆ | S P I O O D S p u p l C n o a t p n l − n an ed P ne t d −1| 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0
S ∆ D S A − 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0
∆S+ 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
σS 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
TTD 0.226 0.122 0.172 0.273 0.265 0.370 0.410 0.425 0.339 0.309 0.188 0.294 0.295 0.201 0.266 0.296 0.398 0.301 0.385 0.334 0.367 0.339 0.447 0.332
MON(d) 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
SAT(d) 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
SUN(d) 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
W ∆W DA − 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0
∆W+ 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
σW 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
30

Table 7.: Estimated scaled coefficients for ν (skewness) on the first day of the test set.
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Intercept 0.003 -0.034 -0.011 -0.033 -0.008 0.026 -0.025 0.005 -0.010 0.006 0.001 0.035 0.015 -0.017 -0.044 0.042 0.006 0.017 0.032 0.025 0.022 -0.000 0.065 0.002
αt−1 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
αt−2 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
|∆Pt−1| 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
|∆Pt−2| 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
|∆Pt−3| 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
|∆Pt−4| 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
|∆Pt−5| 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
| (cid:80) ∆ ∆ P i i = = P t− 1 7 t− 2 1 6 |∆ | Pt−i| 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0
∆Pt−2 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
∆Pt−3 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
MO1000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
MO2000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
MO4000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
L O ∆ D D O A A 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0
∆ ∆ | S P I O O D S p u p l C n o a t p n l − n an ed P ne t d −1| 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0
S ∆ D S A − 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0
∆S+ 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
σS 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
TTD 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
MON(d) 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
SAT(d) 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
SUN(d) 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
W ∆W DA − 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0
∆W+ 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
σW 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
Table 8.: Estimated scaled coefficients for τ (kurtosis) on the first day of the test set.
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Intercept -0.100 -0.147 -0.098 0.029 -0.154 -0.256 -0.425 0.014 0.004 0.079 0.103 0.051 0.218 0.232 0.328 0.573 0.409 -0.014 0.072 0.111 0.101 0.044 0.013 0.009
αt−1 -0.186 -0.064 -0.086 -0.095 -0.074 -0.086 -0.120 -0.080 -0.063 0.000 0.000 0.000 0.000 -0.058 -0.054 -0.075 -0.141 -0.083 -0.092 -0.092 -0.098 -0.122 -0.119 -0.128
αt−2 0.000 -0.032 -0.039 0.000 -0.047 -0.037 -0.040 -0.040 0.000 -0.050 0.000 -0.046 0.000 0.000 0.000 -0.043 0.000 0.000 -0.029 -0.023 -0.036 -0.003 0.000 0.000
|∆Pt−1| 0.227 0.000 0.000 0.037 0.000 0.208 0.215 0.049 0.057 0.052 0.034 0.097 0.000 0.019 0.000 0.052 0.215 0.027 0.184 0.000 0.076 0.217 0.107 0.127
|∆Pt−2| 0.000 0.099 0.131 0.000 0.103 0.077 0.088 0.128 0.000 0.000 0.000 0.120 0.000 0.000 0.000 0.048 0.000 0.000 0.051 0.033 0.122 0.058 0.000 0.104
|∆Pt−3| 0.020 0.073 0.060 0.000 0.000 0.041 0.018 0.007 0.000 0.029 0.004 0.025 0.000 0.000 0.000 0.053 0.000 0.000 0.000 0.036 0.052 0.038 0.029 0.045
|∆Pt−4| 0.058 0.051 0.013 0.000 0.088 0.108 0.000 0.009 0.019 0.014 0.022 0.000 0.000 0.000 0.000 0.035 0.000 0.049 0.027 0.048 0.022 0.010 0.059 0.063
|∆Pt−5| 0.000 0.033 0.013 0.000 0.000 0.057 0.022 0.000 0.000 0.000 0.000 0.052 0.000 0.000 0.000 0.012 0.000 0.013 0.000 0.030 0.050 0.039 0.000 0.073
| (cid:80) ∆ ∆ P i i = = P t− 1 7 t− 2 1 6 |∆ | Pt−i| 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 1 0 0 0 0 0 7 0 0 0 0 . . . 0 0 0 0 7 0 0 8 0 0 0 0 . . . 0 0 0 4 3 0 3 7 0 - 0 0 0 . . . 0 0 0 1 5 4 0 2 0 0 0 0 . . . 0 0 0 1 0 0 0 0 0 0 0 0 . . . 0 0 0 0 4 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 1 0 0 1 0 0 6 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 - 0 0 0 . . . 0 0 0 2 0 3 4 0 2 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 1 0 0 3 0 0 5 0 0 0 0 . . . 0 1 0 0 0 0 0 6 0 0 0 0 . . . 0 0 0 2 0 0 9 0 0 - 0 0 0 . . . 0 0 0 1 4 7 4 0 6 0 0 0 . . . 0 0 0 1 6 0 9 9 0 0 0 0 . . . 0 0 0 0 6 0 0 9 0 0 0 0 . . . 0 0 0 6 0 0 3 0 0
∆Pt−2 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.004 0.000 -0.020 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
∆Pt−3 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
MO1000 -0.047 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.018 0.000 0.000 0.000 0.000 0.000 0.002 0.011 0.005 0.000 -0.009 0.000 0.000 -0.027
MO2000 -0.017 0.000 0.000 0.000 0.000 -0.057 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 -0.034 -0.017 0.016 -0.062 0.000 -0.058 -0.041 -0.030 0.000 0.000
MO4000 0.000 -0.040 -0.050 -0.065 -0.069 -0.020 0.000 -0.042 0.000 0.000 -0.103 -0.106 -0.063 -0.068 -0.013 -0.138 -0.096 -0.053 -0.092 0.000 -0.036 -0.037 -0.021 0.000
L O ∆ D D O A A 0 0 0 . . . 0 0 0 0 0 0 6 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 1 0 0 0 0 0 0 0 0 . . . 0 0 0 4 0 0 3 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 - 0 0 0 . . . 0 0 0 0 0 3 0 0 1 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 - 0 0 0 . . . 0 0 0 0 0 2 0 0 7 - 0 0 0 . . . 0 0 0 0 0 0 0 0 3 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0 0 0 0 . . . 0 0 0 0 0 0 0 0 0
∆ ∆ | S P I O O D S p u p l C n o a t p n l − n an ed P ne t d −1| 0 0 0 0 . . . . 0 0 0 0 0 0 4 0 0 0 7 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 . . . . 0 0 0 0 0 0 7 0 0 0 1 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 6 0 0 0 8 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 1 0 0 0 2 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 . . . . 0 0 0 0 0 0 0 0 0 0 0 0
S ∆ D S A − 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 - 0 0 . . 0 0 0 7 0 2 - 0 0 . . 0 0 0 7 0 7 - 0 0 . . 0 0 0 8 0 5 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0
∆S+ 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
σS 0.000 0.000 0.000 0.000 0.052 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.019 0.000 0.000 0.000 0.000 0.000 -0.005 0.000 0.000 0.000
TTD 0.095 0.120 0.153 0.141 0.180 0.000 0.061 0.067 0.050 0.000 0.043 0.000 0.000 0.132 0.078 0.000 0.000 0.073 0.049 0.115 0.042 0.017 0.000 0.000
MON(d) 0.000 0.000 0.000 0.000 0.000 0.050 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 -0.029 0.000 0.000 0.000 0.000 -0.023 0.000 0.000 0.000 0.000
SAT(d) -0.018 0.000 0.000 0.000 0.000 0.000 0.000 -0.021 0.000 0.000 0.000 0.025 0.000 0.041 0.000 0.041 0.000 0.023 0.030 0.005 0.010 0.000 0.000 0.000
SUN(d) 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.047 0.000 0.012 0.046 0.028 0.000 0.011 0.000 0.000 0.006 0.000
W ∆W DA − 0 0 . . 0 0 3 0 5 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 4 0 8 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 1 0 5 0 0 0 . . 0 0 4 0 8 0 0 0 . . 0 0 6 0 3 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 4 0 9 0 0 0 . . 0 0 0 0 0 0 0 0 . . 1 0 0 0 1 0 0 0 . . 0 0 9 0 1 0 0 0 . . 0 0 5 0 3 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 5 0 0 0 0 0 . . 0 0 0 0 7 0 0 0 . . 0 0 0 0 0 0 0 0 . . 0 0 5 0 9 0 0 0 . . 0 0 0 0 0 0
∆W+ 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.020 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
σW 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
For the skewness parameter ν none of the variables apart from the intercept yield non-zero coefficient
estimates. The intercept is slightly negative in the night hours and positive in the morning and afternoon
hours. Weconcludethattheintradaypricereturnsdonotexhibitanystrongskewnesswithintheindividual
trading sessions.
Lastly,weturntoTable8givingtheestimatedcoefficientsforthekurtosisparameterτ. Wefindanegative
impact of lagged αd,s and a positive impact of lagged ∆Pd,s . Thus, we expect the distribution of ∆Pd,s
t ID,t ID,t
to be lighter-tailed if there has been no trade in the preceding 15 minutes of trading. On the other hand,
large absolute price changes in the previous 15 minutes of trading increase τ and thus the heaviness of the
tails. The impact of lagged αd,s and ∆Pd,s is more pronounced during the night hours. During the day
t ID,t
31

hours, there are some none-zero estimates for wind and solar forecasts. This is consistent with Kremer
et al. (2020)’s finding that the behaviour of night contracts is more driven by trading-related variables
than fundamentals. For τ, we find a negative impact of the merit-order slope parameter. This implies
that a steep-merit leads to heavier tails for the distribution of ∆Pd,s . Thus, if the merit-order is steep,
ID,t
not only the volatility level is elevated, but also the likelihood of spikes is higher. Lastly, we find that with
decreasing time to delivery the heaviness of the distribution’s tails decreases.
0
1
2
3
4
5
6 7
8
9
10 11
12
13
14 15
16
17
18 19
20 21 22 23
2017-0
2
2 017-0
2
3 017-0
2
4 017-0
2
5 017-0
2
6 017-0
2
7 017-0
2
8 017-0
2
9 017-1
2
0 017-1
2
1 017-1
2
2 018-0
2
1 018-0
2
2 018-0
2
3 018-0
2
4 018-0
2
5 018-0
2
6 018-0
2
7 018-0
2
8 018-0
2
9 018-1
2
0 018-1
2
1 018-1
2
2 019-0
2
1 019-0
2
2 019-0
2
3 019-0
2
4 019-0
2
5 019-0
2
6 019-0
2
7 019-0
2
8 019-0
2
9 019-1
2
0 019-1
2
1 019-1
2
2 020-0
2
1 020-0
2
2 020-0
2
3 020-0
2
4 020-0
2
5 020-0
2
6 020-07
Date
ruoH
SIDC for distribution parameter
1.5
1.0
0.5
0.0
XBID/SIDC go-live on June 13, 2018
Figure 16.: Estimated coefficients for the SIDC dummy across the test set.
7. Discussion and Conclusion
This paper develops a simulation-based forecasting model for the intraday price process in the last three
hours of each product’s trading window. We expand the key work of Narajewski and Ziel (2020a) in four
dimensionsby(i)investigatingdistributionswithpotentialskewnessandmodellingallmomentsexplicitly,
(ii) adding intra-daily forecast updates and (iii) a novel measure for the merit-order slope, derived from
day-ahead auction curves, and (iv) employing a regularized estimation using the GAMLSS-LASSO for all
distribution moments.
Our results are two-fold: First, we show that the proposed method is able to generate high quality
ensembles for the intraday markets, whose predictive performance is significantly better than benchmark
models such as random walk or ARIMA-type processes on a wide range of probabilistic scoring rules.
The improvement in accuracy is especially distinct in the tails of the predictive distribution. Thus,
our results can be applied directly to trading problems as proposed by Serafin et al. (2022) or plugged
into any optimization method relying on accurate sampling methods. Second, the GAMLSS framework’s
explicittraceabilityandtheregularizedestimationallowstodrawconclusionsontheimpactofexplanatory
variables. Qualitatively, our results for the expected value of the intraday return distribution imply weak-
form efficient markets, as the inclusion of additional variables does not improve the prediction of the
expected value significantly. Additionally, we find evidence for a merit-order effect in the volatility and
kurtosis of the return distribution. A steep merit-order regime leads to higher volatility and heavier tails.
Whatismore, wefindthatthevolatilityriseswithdecreasingtimetodeliveryandriseswiththeclosureof
the pan-European order book sharing (SIDC). On the other hand, the kurtosis is driven by trading-related
variables such as trade events and lagged prices. We find however, that the skewness is close to zero for
all hours, and that none of the analysed variables show predictive power.
32

This paper’s result opens several new research strings: the models used can be improved by the inclusion
of cross-product effects and neighbouring products as additional input variables. However, due to the
structure of intraday markets with parallel and overlapping trading sessions, this task is non-trivial. A
second interesting research avenue is the relationship between trading volume, liquidity and volatility
in intraday markets. Further research is also needed to better understand the impact of fundamental
variables for modelling the volatility, kurtosis and skewness of the distribution of intraday price returns.
The influence of the merit-order shape as explanatory variable for the volatility warrants further research
| into its modelling | for short-term | markets. |     |     |     |     |     |     |
| ------------------ | -------------- | -------- | --- | --- | --- | --- | --- | --- |
Acknowledgements
This paper is based on research conducted during a joint project of Simon Hirsch and Statkraft Trading
GmbH. Simon Hirsch is grateful to Statkraft, especially Patrick Otto, Dr. Konstantin Wiegandt and Dr.
Daniel Gruhlke for the support received while writing his thesis. The authors are grateful to energy &
meteo systems GmbH for providing the forecasts used in the paper. The views and opinions expressed
in this paper are the author’s own and do not reflect the views of Statkraft Trading GmbH or energy &
meteo systems GmbH. The authors are grateful to helpful discussions at the 30. GEE Doctoral Workshop,
Essen, 2022.
Data Statement
Due to the commercial nature of production forecasts the dataset remains confidential and cannot be
shared.
| Declaration | of Interest |     |     |     |     |     |     |     |
| ----------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
Simon Hirsch is employed by Statkraft Trading GmbH. The authors declare no conflict of interest.
References
René Aïd, Pierre Gruet, and Huyên Pham. An optimal trading problem in intraday electricity markets.
|             |               | Economics, | 10(1):49–85, | 2016. |     |     |     |     |
| ----------- | ------------- | ---------- | ------------ | ----- | --- | --- | --- | --- |
| Mathematics | and Financial |            |              |       |     |     |     |     |
SørenAsmussenandPeterWGlynn. Stochastic Simulation: Algorithms and Analysis,volume57. Springer
| Science | & Business Media, | 2007. |     |     |     |     |     |     |
| ------- | ----------------- | ----- | --- | --- | --- | --- | --- | --- |
Clara Balardy. An empirical analysis of the bid-ask spread in the continuous intraday trading of the
| german | power market. |     | Journal, 43(3), | 2022. |     |     |     |     |
| ------ | ------------- | --- | --------------- | ----- | --- | --- | --- | --- |
The Energy
Rainer Baule and Michael Naumann. Volatility and Dispersion of Hourly Electricity Contracts on the
GermanContinuousIntradayMarket. Energies,14(22),2021. doi: https://doi.org/10.3390/en14227531.
Philip Beran, Benjamin Böcker, and Christoph Weber. Spot Market Price Effects Of Reserve Provision-
Analyses Based On A Parsimonious Fundamental Model. In Local Energy, Global Markets, 42nd IAEE
|               |             |             | 2019. | International | Association | for Energy | Economics, | 2019. |
| ------------- | ----------- | ----------- | ----- | ------------- | ----------- | ---------- | ---------- | ----- |
| International | Conference, | May 29-June | 1,    |               |             |            |            |       |
33

DerekW.Bunn,AngelicaGianfreda,andStefanKermer. ATrading-basedEvaluationofDensityForecasts
in a Real-time Electricity Market. Energies (Special Issue on Forecasting Models of Electricity Prices),
| 11(10):2658, |     | 2018. | doi: | https://doi.org/10.3390/en11102658. |     |     |     |     |     |     |     |
| ------------ | --- | ----- | ---- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Michael Coulon, Christian Jacobsson, and Jonas Ströjby. Hourly Resolution Forward Curves for Power:
StatisticalModelingmeetsMarketFundamentals. InMarcelProkopczuk,editor,Energy Pricing Models:
| Recent | Advances, |     | Methods |     | and Tools. | Palgrave | Macmillan, |     | 2014. |     |     |
| ------ | --------- | --- | ------- | --- | ---------- | -------- | ---------- | --- | ----- | --- | --- |
David A Dickey and Wayne A Fuller. Distribution of the estimators for autoregressive time series with a
unit root. Journal of the American statistical association, 74(366a):427–431, 1979.
David A Dickey and Wayne A Fuller. Likelihood ratio statistics for autoregressive time series with a unit
| root. |               |     |     |         |        |             | Society, |     | pages | 1057–1072, | 1981. |
| ----- | ------------- | --- | --- | ------- | ------ | ----------- | -------- | --- | ----- | ---------- | ----- |
|       | Econometrica: |     |     | journal | of the | Econometric |          |     |       |            |       |
Francis X. Diebold. Comparing Predictive Accuracy, Twenty Years Later: A Personal Perspective on the
Use and Abuse of Diebold–Mariano tests. Statistics, 33(1):1–1, 2015.
|     |     |     |     |     |     | Journal |     | of Business |     | & Economic |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | ----------- | --- | ---------- | --- |
doi: https://doi.org/10.1080/07350015.2014.983236.
Francis X. Diebold and Robert S. Mariano. Comparing Predictive Accuracy.
Journal of Business &
Statistics, 20(1):134–144, 2002. doi: https://doi.org/10.1198/073500102753410444.
Economic
EEX AG. Transparency Plattform, 2020. URL https://www.eex-transparency.com/power/.
energy&meteosystemsGmbH. IntradailyUpdatedRenewablesProductionForecasts, 2020. URLhttps:
//www.energymeteo.de/.
ENTSO-E. Day-ahead demand forecasts, 2021. URL https://transparency.entsoe.eu/.
EPEX SPOT SE. Trading on EPEX SPOT. Technical report, EEX Group SE, 2018.
| EPEX | SPOT | SE. | Public | Trades, | 2020a. | URL | www.epex-spot.de. |     |     |     |     |
| ---- | ---- | --- | ------ | ------- | ------ | --- | ----------------- | --- | --- | --- | --- |
EPEX SPOT SE. Description of EPEX SPOT Markets Indices. Technical report, EEX Group SE, 2020b.
EPEX SPOT SE. Aggregated Day-ahead Auction Curves, 2020c. URL www.epex-spot.de.
European Commission. Regulation (EU) No 1227/2011 of the European Parliament and of the Council
of 25 October 2011 on wholesale energy market integrity and transparency Text with EEA relevance.
|          |     |         |        |          | Union, | L 326/1:1–16, |     |     | 2011. doi: | http://data.europa.eu/eli/reg/2011/ |     |
| -------- | --- | ------- | ------ | -------- | ------ | ------------- | --- | --- | ---------- | ----------------------------------- | --- |
| Official |     | Journal | of the | European |        |               |     |     |            |                                     |     |
1227/oj.
Carmen Fernández and Mark F.J. Steel. On Bayesian Modeling of Fat Tails and Skewness.
Journal of the
|          |     |             |     | Association, | 93(441):359–371, |     |     | 1998. |     |     |     |
| -------- | --- | ----------- | --- | ------------ | ---------------- | --- | --- | ----- | --- | --- | --- |
| American |     | Statistical |     |              |                  |     |     |       |     |     |     |
Jerome Friedman, Trevor Hastie, and Robert Tibshirani. Regularization Paths for Generalized Linear
Models via Coordinate Descent. Software, 33(1):1–22, 2010. doi: 10.18637/jss.
|     |     |     |     |     | Journal | of  | Statistical |     |     |     |     |
| --- | --- | --- | --- | --- | ------- | --- | ----------- | --- | --- | --- | --- |
v033.i01.
AngelicaGianfredaandDerekW.Bunn. Astochasticlatentmomentmodelforelectricitypriceformation.
Research, 66(5):1189–1203, 2018. doi: https://doi.org/10.1287/opre.2018.1733.
Operations
Silke Glas, Rüdiger Kiesel, Sven Kolkmann, Marcel Kremer, Nikolaus Graf von Luckner, Lars Ostmeier,
KarstenUrban, andChristophWeber. IntradayRenewableEectricityTrading: AdvancedModelingand
| Numerical |     | Optimal |     | Control. |         |                |     |     | Industry, | 10(1):3, | 2020. |
| --------- | --- | ------- | --- | -------- | ------- | -------------- | --- | --- | --------- | -------- | ----- |
|           |     |         |     |          | Journal | of Mathematics |     | in  |           |          |       |
34

ACER. Guidance on the Application of Regulation (EU) No 1227/2011 of the European Parliament and
of the Council of 25 October 2011 on wholesale energy market integrity and Transparency. 5th Edition.
| Technical | report, ACER, | 2020. |     |     |     |     |     |
| --------- | ------------- | ----- | --- | --- | --- | --- | --- |
Tilmann Gneiting and Adrian E. Raftery. Strictly proper scoring rules, prediction, and estimation. Jour-
nal of the American statistical Association, 102(477):359–378, 2007. doi: https://doi.org/10.1198/
016214506000001437.
Marc Gürtler and Thomas Paulsen. The Effect of Wind and Solar Power Forecasts on Day-ahead and
Intraday Electricity Prices in Germany. Economics, 75:150–162, 2018. doi: https://doi.org/10.
Energy
1016/j.eneco.2018.07.006.
David Harvey, Stephen Leybourne, and Paul Newbold. Testing the Equality of Prediction Mean Squared
Errors. Forecasting, 13(2):281–291, 1997. doi: https://doi.org/10.1016/
|     | International | Journal | of  |     |     |     |     |
| --- | ------------- | ------- | --- | --- | --- | --- | --- |
S0169-2070(96)00719-4.
Trevor J. Hastie and Robert J. Tibshirani. Generalized Additive Models: Some Applications.
|              |             |              |                  |       |     | Journal | of  |
| ------------ | ----------- | ------------ | ---------------- | ----- | --- | ------- | --- |
| the American | Statistical | Association, | 82(398):371–386, | 1987. |     |         |     |
Trevor J. Hastie and Robert J. Tibshirani. Generalized Additive Models. In
|         |             |              |                |                  | Monographs | on Statistics | and |
| ------- | ----------- | ------------ | -------------- | ---------------- | ---------- | ------------- | --- |
| Applied | Probability | 43. Chapmann | & Hall / CRCs, | 1 edition, 1990. |            |               |     |
Yang He, Marcus Hildmann, Florian Herzog, and Göran Andersson. Modeling the Merit Order Curve of
the European Energy Exchange Power Market in Germany. IEEE Transactions on Power Systems, 28
| (3):3155–3164, | 2013. | doi: 10.1109/TPWRS.2013.2242497. |     |     |     |     |     |
| -------------- | ----- | -------------------------------- | --- | --- | --- | --- | --- |
Rob J. Hyndman and Yeasmin Khandakar. Automatic time series forecasting: the forecast package for R.
Journal of Statistical Software, 26(3):1–22, 2008. URL https://www.jstatsoft.org/article/view/
v027i03.
Rob J. Hyndman, George Athanasopoulos, Christoph Bergmeir, Gabriel Caceres, Leanne Chhay, Mitchell
O’Hara-Wild, FotiosPetropoulos, SlavaRazbash, EaroWang, andFarahYasmeen.
forecast: Forecast-
ing functions for time series and linear models, 2020. URLhttps://pkg.robjhyndman.com/forecast/.
| R package | version | 8.13. |     |     |     |     |     |
| --------- | ------- | ----- | --- | --- | --- | --- | --- |
TimJankeandFlorianSteinke.Forecastingthepricedistributionofcontinuousintradayelectricitytrading.
| Energies, | 12(22):4262, | 2019. doi: | https://doi.org/10.3390/en12224262. |     |     |     |     |
| --------- | ------------ | ---------- | ----------------------------------- | --- | --- | --- | --- |
Norman L Johnson. Systems of frequency curves generated by methods of translation. Biometrika, 36
| (1/2):149–176, | 1949. | doi: https://doi.org/10.2307/2332539. |     |     |     |     |     |
| -------------- | ----- | ------------------------------------- | --- | --- | --- | --- | --- |
ChristopherKath. Modelingintradaymarketsunderthenewadvancesofthecross-borderintradayproject
(XBID): Evidence from the German intraday market. Energies, 12(22):4339, 2019. doi: https://doi.
org/10.3390/en12224339.
Christopher Kath and Florian Ziel. Optimal Order Execution in Intraday Markets: Minimizing Costs in
| Trade Trajectories. |     |     | arXiv:2009.07892, | 2020. |     |     |     |
| ------------------- | --- | --- | ----------------- | ----- | --- | --- | --- |
arXiv preprint
Rüdiger Kiesel and Florentina Paraschiv. Econometric analysis of 15-minute intraday electricity prices.
|     | Economics, | 64:77–90, | 2017. |     |     |     |     |
| --- | ---------- | --------- | ----- | --- | --- | --- | --- |
Energy
Andreas Knaut and Simon Paulus. When are Consumers Responding to Electricity Prices? An Hourly
Pattern of Demand Elasticity. EWI Working Paper, No 16/07, Institute of Energy Economics at the
| University | of Cologne | (EWI), | 2016. |     |     |     |     |
| ---------- | ---------- | ------ | ----- | --- | --- | --- | --- |
35

Christopher Koch and Lion Hirth. Short-term electricity trading for system balancing: An empirical
analysis of the role of intraday trading in balancing Germany’s electricity system. Renewable and
Sustainable Energy Reviews, 113:109275, 2019. doi: https://doi.org/10.1016/j.rser.2019.109275.
MarcelKremer, RüdigerKiesel, andFlorentinaParaschiv. IntradayElectricityPricingofNightContracts.
| Energies, | 13(17):4501, |     | 2020. | doi: | https://doi.org/10.3390/en13174501. |     |     |     |     |     |
| --------- | ------------ | --- | ----- | ---- | ----------------------------------- | --- | --- | --- | --- | --- |
Marcel Kremer, Rüdiger Kiesel, and Florentina Paraschiv. An econometric model for intraday electricity
| trading. |               |     |              |     |     |           |         | A, 379(2202):20190624, |     | 2021. |
| -------- | ------------- | --- | ------------ | --- | --- | --------- | ------- | ---------------------- | --- | ----- |
|          | Philosophical |     | Transactions |     | of  | the Royal | Society |                        |     |       |
Sergei Kulakov and Florian Ziel. Determining Fundamental Supply and Demand Curves in a Wholesale
| Electricity | Market. |     |       |          | arXiv:1903.11383, |     |     | 2019. |     |     |
| ----------- | ------- | --- | ----- | -------- | ----------------- | --- | --- | ----- | --- | --- |
|             |         |     | arXiv | preprint |                   |     |     |       |     |     |
SergeiKulakovandFlorianZiel. TheImpactofRenewableEnergyForecastsonIntradayElectricityPrices.
Economics of Energy & Environmental Policy, 10, 2020. doi: 10.5547/2160-5890.10.1.skul.
Thomas Kuppelwieser and David Wozabal. Intraday Power Trading: Towards an Arms Race in Weather
Forecasting? Working Paper, TUM School of Management, Technical University of Munich, 2021.
Ewa Lazarczyk and Chloe Le Coq. Information Disclosure Rules in the European Electricity Market: An
Overview. In 2018 15th International Conference on the European Energy Market (EEM), pages 1–4.
| IEEE, | 2018. | doi: 10.1109/EEM.2018.8469779. |     |     |     |     |     |     |     |     |
| ----- | ----- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Nils Löhndorf and David Wozabal. The value of coordination in multimarket bidding of grid energy
| storage. | Operations |     | Research, | 2022. |     |     |     |     |     |     |
| -------- | ---------- | --- | --------- | ----- | --- | --- | --- | --- | --- | --- |
Lukas Meier, Sara Van De Geer, and Peter Bühlmann. The group lasso for logistic regression.
Journal of
|           |             |     |          |        |     |              | Methodology), |     | 70(1):53–71, | 2008. |
| --------- | ----------- | --- | -------- | ------ | --- | ------------ | ------------- | --- | ------------ | ----- |
| the Royal | Statistical |     | Society: | Series | B   | (Statistical |               |     |              |       |
Michał Narajewski and Florian Ziel. Ensemble forecasting for intraday electricity prices: Simulating
| trajectories. |     |     | Energy, | 279:115801, |     | 2020a. |     |     |     |     |
| ------------- | --- | --- | ------- | ----------- | --- | ------ | --- | --- | --- | --- |
Applied
MichałNarajewskiandFlorianZiel. EconometricModellingandForecastingofIntradayElectricityPrices.
Journal of Commodity Markets, 19:100107, 2020b. doi: https://doi.org/10.1016/j.jcomm.2019.100107.
Nordpool SE. XBID Launch Information Package. Technical report, Nordpool SE, 2018.
Jakub Nowotarski and Rafał Weron. Recent Advances in Electricity Price Forecasting: A Review of
Probabilistic Forecasting. Reviews, 81:1548–1568, 2018. doi: https:
|     |     |     |     | Renewable |     | and Sustainable |     | Energy |     |     |
| --- | --- | --- | --- | --------- | --- | --------------- | --- | ------ | --- | --- |
//doi.org/10.1016/j.rser.2017.05.234.
Christian Pape, Simon Hagemann, and Christoph Weber. Are Fundamentals Enough? Explaining Price
VariationsintheGermanDay-AheadandIntradayPowerMarket. Economics,54:376–387,2016.
Energy
doi: https://doi.org/10.1016/j.eneco.2015.12.013.
Tomasz Serafin, Grzegorz Marcjasz, and Rafał Weron. Trading on short-term path forecasts of intraday
| electricity | prices. |     | Economics, |     |     | 112:106125, | 2022. |     |     |     |
| ----------- | ------- | --- | ---------- | --- | --- | ----------- | ----- | --- | --- | --- |
Energy
Francesco Serinaldi. Distributional modeling and short-term forecasting of electricity prices by generalized
additive models for location, scale and shape. Economics, 33(6):1216–1226, 2011.
Energy
Robert H Shumway and David S Stoffer. Time Series Analysis and Its Applications: With R Examples.
| Springer, | Cham, | Switzerland, |     | 4   | edition, | 2017. |     |     |     |     |
| --------- | ----- | ------------ | --- | --- | -------- | ----- | --- | --- | --- | --- |
36

D. Mikis Stasinopoulos and Robert A. Rigby. Generalized Additive Models for Location, Scale and Shape.
| Applied | Statistics, | 54:507–554, |     | 2005. |     |     |     |     |     |     |     |     |     |
| ------- | ----------- | ----------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
D. Mikis Stasinopoulos and Robert A. Rigby. Generalized additive models for location scale and shape
(gamlss) in r. Software, 23(7):1–46, 2007. doi: 10.18637/jss.v023.i07.
|     | Journal |     | of Statistical |     |     |     |     |     |     |     |     |     |     |
| --- | ------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
D. Mikis Stasinopoulos and Robert A. Rigby. gamlss.dist: Distributions for Generalized Additive Models
Shape, 2020. URL https://CRAN.R-project.org/package=gamlss.dist. R
| for Location | Scale   | and    |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| package      | version | 5.1-7. |     |     |     |     |     |     |     |     |     |     |     |
D. Mikis Stasinopoulos, Robert A. Rigby, Gillian Z. Heller, Vlasios Voudouris, and Fernanda De Bastiani.
|          |            |     |            |     |       |        |     | R.  | Chapman | and | Hall/CRC, | New | York, 2017. |
| -------- | ---------- | --- | ---------- | --- | ----- | ------ | --- | --- | ------- | --- | --------- | --- | ----------- |
| Flexible | Regression | and | Smoothing: |     | Using | GAMLSS |     | in  |         |     |           |     |             |
D. Mikis Stasinopoulos, Robert A. Rigby, and Fernanda De Bastiani. Gamlss: a distributional regression
| approach.         | Statistical |                                             | Modelling, |     | 18(3-4):248–273, |     | 2018. |     |     |     |     |     |     |
| ----------------- | ----------- | ------------------------------------------- | ---------- | --- | ---------------- | --- | ----- | --- | --- | --- | --- | --- | --- |
| RobertTibshirani. |             | Regressionshrinkageandselectionviathelasso. |            |     |                  |     |       |     |     |     |     |     |     |
JournaloftheRoyalStatisticalSociety:
Series B (Methodological), 58(1):267–288, 1996. doi: https://doi.org/10.1111/j.2517-6161.1996.tb02080.
x.
Bartosz Uniejewski, Grzegorz Marcjasz, and Rafał Weron. Understanding Intraday Electricity Markets:
Variable Selection and very Short-term Price Forecasting Using LASSO. International Journal of Fore-
casting, 35(4):1533–1547, 2019. doi: https://doi.org/10.1016/j.ijforecast.2019.02.001.
Johannes Viehmann. State of the German short-term power market. Zeitschrift für Energiewirtschaft, 41
| (2):87–103, | 2017. | doi: | https://doi.org/10.1007/s12398-017-0196-9. |     |     |     |     |     |     |     |     |     |     |
| ----------- | ----- | ---- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Nikolaus Graf von Luckner, Álvaro Cartea, Sebastian Jaimungal, and Rüdiger Kiesel. Optimal market
maker pricing in the german intraday power market. Working Paper, House of Energy Markets and
| Finance, | University | of  | Duisburg-Essen, |     |     | Germany, | 2017. |     |     |     |     |     |     |
| -------- | ---------- | --- | --------------- | --- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- |
Diethelm Wurtz, Yohan Chalabi, and Ladislav Luksan. Parameter Estimation of ARMA Models with
GARCH/APARCH errors an R and SPlus Software Implementation. Journal of Statistical Software, 55
| (2):28–33, | 2006. |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Florian Ziel. Modeling the impact of wind and solar power forecasting errors on intraday electricity prices.
In 2017 14th International Conference on the European Energy Market (EEM), pages 1–5. IEEE, 2017.
doi: 10.1109/EEM.2017.7981900.
Florian Ziel. M5 competition uncertainty: Overdispersion, distributional forecasting, gamlss, and beyond.
| International | Journal |     | of Forecasting, |     | 2021. |     |     |     |     |     |     |     |     |
| ------------- | ------- | --- | --------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
Florian Ziel and Kevin Berk. Multivariate Forecasting Evaluation: On Sensitive and Strictly Proper
| Scoring      | Rules.   | arXiv    | preprint | arXiv:1910.07325, |     |       | 2019.      |     |          |       |     |         |           |
| ------------ | -------- | -------- | -------- | ----------------- | --- | ----- | ---------- | --- | -------- | ----- | --- | ------- | --------- |
| Florian Ziel | and Peru | Muniain. |          |                   |     |       |            |     |          |       |     | GAMLSS, | 2021. URL |
|              |          |          |          | gamlss.lasso:     |     | Extra | Lasso-Type |     | Additive | Terms | for |         |           |
https://CRAN.R-project.org/package=gamlss.lasso. R package version 1.0-2.
Florian Ziel and Rafał Weron. Day-ahead electricity price forecasting with high-dimensional structures:
Univariate vs. multivariate modeling frameworks. Economics, 70:396–420, 2018.
Energy
Florian Ziel, Rick Steinert, and Sven Husmann. Efficient modeling and forecasting of electricity spot
prices. Energy Economics, 47:98–111, 2015. doi: https://doi.org/10.1016/j.eneco.2014.10.012.
37

Hui Zou. The adaptive lasso and its oracle properties. Association,
|                     |     |       |          |        |     | Journal | of the American | Statistical |     |
| ------------------- | --- | ----- | -------- | ------ | --- | ------- | --------------- | ----------- | --- |
| 101(476):1418–1429, |     | 2006. |          |        |     |         |                 |             |     |
| A. Aggregation      |     | of    | Intraday | Trades |     |         |                 |             |     |
The following section gives a detailed definition of the volume-weighted prices Pd,s and the price changes
ID,t
∆Pd,s . We start with the definition of a single trade and describe how we aggregate trades.
ID,t
A trade on the intraday market for the delivery period is identified by the unique time stamp i. For
d,s
each trade, we have the transacted price Pd,s in EUR/MWh and the volume Vd,s in MW. We now
|            |         |           |     |         | trade,i |     |     | trade,i |     |
| ---------- | ------- | --------- | --- | ------- | ------- | --- | --- | ------- | --- |
| define two | sets to | aggregate | the | trades: |         |     |     |         |     |
1. Let Id,s denote the set of all trade timestamps for the delivery period d,s.
| 2. Let | b(d,s) | denote | the start | of the delivery | period | d,s and    | let       |       |     |
| ------ | ------ | ------ | --------- | --------------- | ------ | ---------- | --------- | ----- | --- |
|        |        |        | Td,s      | = [b(d,s)−x−y,  |        | b(d,s)−x), | x ≥ 0 and | y > 0 |     |
x,y
denote the left closed time interval between x+y and x minutes before the delivery of product d,s.
We can then define the the 5-minute volume-weighted average price of the interval x,y for the delivery
| period | as: |     |     |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
d,s
|     |     |     |         | 1            |               | (cid:88)     |               |         |      |
| --- | --- | --- | ------- | ------------ | ------------- | ------------ | ------------- | ------- | ---- |
|     |     |     | IDd,s = |              |               | ·            | Vd,s          | Pd,s    | (28) |
|     |     | x   | y       |              |               | id,s∈Id,s∩Td | , s           |         |      |
|     |     |     |         | (cid:80)     | Vd,s          |              | x , y trade,i | trade,i |      |
|     |     |     |         | id,s∈Id,s∩Td | , s           |              |               |         |      |
|     |     |     |         |              | x , y trade,i |              |               |         |      |
|     |     |     | Pd,s    | IDd,s        |               |              |               |         | (29) |
=
|     |     |       | ID,t (T−t)·y+30 |             | y   |     |     |     |      |
| --- | --- | ----- | --------------- | ----------- | --- | --- | --- | --- | ---- |
|     |     | ∆Pd,s | =Pd,s           | −Pd,s       |     |     |     |     | (30) |
|     |     |       | ID,t            | ID,t ID,t−1 |     |     |     |     |      |
with minutes. The shift of 30 minutes between Equations 29 and 28 is due to the fact that we are
| y   | = 5 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
not taking the control zone trading between between 30 and 5 minutes before start of physical delivery
in the German market into account. If there are no trades observed in the interval of length y ending x
minutes before delivery, the value is set to the previous value. If no trade happened since the start of the
trading session, the corresponding day-ahead spot price Pd,s is used. The boolean variable αd,s denotes
t
DA
no-trade periods and is set to 1 if there is at least one trade within the 5-minute interval, and set to 0 if
there is none.
B. Distributions
Johnson’s S Distribution: Proposed by Johnson (1949), the S family of distributions is a trans-
|     | U   |     |     |     |     |     | U   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
formation of the normal distribution. It is a four parameter distribution with the parameter vector
ΘSU for the location and scale of the distribution and two shape parameters and for the
| =        | (µ,σ,ν,τ)    |     |                   |     |     |     |     | ν τ |     |
| -------- | ------------ | --- | ----------------- | --- | --- | --- | --- | --- | --- |
| kurtosis | and skewness | of  | the distribution. |     |     |     |     |     |     |
38

| 1.0 |     |     | JSU(0, 1, 0, 1) | 100 |     |     |     |     |
| --- | --- | --- | --------------- | --- | --- | --- | --- | --- |
JSU(0, 2, 0, 1)
JSU(0, 1, 1, 1)
JSU(0, 1, -1, 1)
| 0.8 |     |     |     | 101 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
JSU(0, 1, 0, 0.9)
JSU(0, 1, 0, 5)
| 0.6  |     |     |     | 102  |     |     |     |     |
| ---- | --- | --- | --- | ---- | --- | --- | --- | --- |
| )x(f |     |     |     | )x(f |     |     |     |     |
| 0.4  |     |     |     | 103  |     |     |     |     |
JSU(0, 1, 0, 1)
| 0.2 |     |     |     | 104 |     | JSU(0, 2, 0, 1) |     |     |
| --- | --- | --- | --- | --- | --- | --------------- | --- | --- |
JSU(0, 1, 1, 1)
JSU(0, 1, -1, 1)
JSU(0, 1, 0, 0.9)
| 0.0 |                   |              |               | 105             |                   | JSU(0, 1, 0, 5) |         |     |
| --- | ----------------- | ------------ | ------------- | --------------- | ----------------- | --------------- | ------- | --- |
| 5 4 | 3 2               | 1 0 1 2      | 3 4 5         | 5 4             | 3 2               | 1 0             | 1 2 3   | 4 5 |
|     |                   | x            |               |                 |                   | x               |         |     |
|     | (a) Untransformed | y-axis.      |               |                 | (b)               | Log-scale       | y-axis. |     |
|     | Figure            | 17.: The PDF | for Johnson’s | S for different | parametrisations. |                 |         |     |
U
The Probability Distribution Function (PDF) of the original S distribution can be written as follows:
U
(cid:18) (cid:19)
|     |     |                | τ       | 1 1   | 1    |     |     |      |
| --- | --- | -------------- | ------- | ----- | ---- | --- | --- | ---- |
|     |     | f(y | µ,σ,ν,τ) | =       | √ exp | − r2 | ,   |     | (31) |
|     |     |                | σ(z2+1) | 1 2π  | 2    |     |     |      |
2
where z = y−µ and r = ν + τsinh−1(z) for −∞ < y < ∞, µ = (−∞,∞), σ > 0, ν = (−∞,∞) and
σ
τ > 0. The implementation in the GAMLSS-package is parametrized such that µ is the mean and σ is the
standard deviation of the distribution (Stasinopoulos and Rigby, 2020, Stasinopoulos et al., 2017). If
τ
approaches ∞ and ν = 0 the distribution equals the normal distribution. ν > 0 indicates a positive or
right-sided skewness, ν < 0 indicates negative of left-sided skewness. The S -distribution has already
U
been successfully used to model day-ahead prices by Serinaldi (2011) and Gianfreda and Bunn (2018).
Figure 17 gives an intuition of the different parameters. The skewness of the for different values of
|     |     |     |     |     |     | S U |     | τ   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
is clearly visible.
Skew-t Distribution: The PDF for the 4-parameter skew-t distribution follows the form of Wurtz et al.
(2006)andFernándezandSteel(1998),sothatµisthemeanandσisthestandarddeviation. Thefollowing
definition follows Stasinopoulos et al. (2017) and is consistent to the implementation in GAMLSS.

|     |     |                | (cid:16) | (cid:17)−(τ+1)/2 |      |     |     |      |
| --- | --- | -------------- | -------- | ---------------- | ---- | --- | --- | ---- |
|     |     |                |  c 1+   | v2 z2            | if y | ≤ µ |     |      |
|     |     |                |  σ      | τ                |      | 0   |     |      |
|     |     | f(y | µ,σ,ν,τ) | = 0      |                  |      |     |     | (32) |
|     |     |                | (cid:16) | (cid:17)−(τ+1)/2 |      |     |     |      |
|     |     |                | c        | z 2              | if   |     |     |      |
|     |     |                |   1+   |                  | y    | ≥ µ |     |      |
|     |     |                | σ        | v 2 τ            |      | 0   |     |      |
0
for −∞ < y < ∞, where −∞ < µ < ∞, σ > 0, ν > 0 and τ > 2 and where µ = µ − σm/s and
0
σ = σ/s and z = (y−µ )/σ , c = 2ν[(1+ν2)B(1/2,τ/2)τ1/2]−1. m and s are obtained from equations
| 0   |     | 0 0 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
(14.32) and (14.33) on pp. 261f in Stasinopoulos et al. (2017). Figure 18 gives an intuition of the different
parameters.
| C. Supplementary |     | Figures |     |     |     |     |     |     |
| ---------------- | --- | ------- | --- | --- | --- | --- | --- | --- |
39

100
SST(0, 1, 1, 3)
0.8
SST(0, 2, 1, 3)
SST(0, 1, 2, 3)
| 0.7 |     |     | SST(0, 1, 0.5, 3) |     |     |     |     |
| --- | --- | --- | ----------------- | --- | --- | --- | --- |
101
SST(0, 1, 1, 2.5)
| 0.6 |     |     | SST(0, 1, 1, 5) |     |     |     |     |
| --- | --- | --- | --------------- | --- | --- | --- | --- |
0.5
102
| )x(f 0.4 |     |     | )x(f |     |     |     |     |
| -------- | --- | --- | ---- | --- | --- | --- | --- |
0.3
103
SST(0, 1, 1, 3)
0.2
SST(0, 2, 1, 3)
|     |     |     |     | 104 |     | SST(0, 1, 2, 3)   |     |
| --- | --- | --- | --- | --- | --- | ----------------- | --- |
| 0.1 |     |     |     |     |     | SST(0, 1, 0.5, 3) |     |
SST(0, 1, 1, 2.5)
| 0.0   |               |         |       |     |               | SST(0, 1, 1, 5) |     |
| ----- | ------------- | ------- | ----- | --- | ------------- | --------------- | --- |
| 5 4 3 | 2 1           | 0 1 2   | 3 4 5 | 5 4 | 3 2 1         | 0 1 2 3         | 4 5 |
|       |               | x       |       |     |               | x               |     |
| (a)   | Untransformed | y-axis. |       |     | (b) Log-scale | y-axis.         |     |
Figure 18.: The PDF for skew-t distribution for different parametrisations. Note that while for Johnson’s
, the skewness is symmetric around 0, for the skew-t the skew is symmetric around 1 for
S
U
1/ν.
|     | Autocorrelation for Lag 2 of  | PI d | D , , s t for each trading session by delivery day and hour |     |     |     |     |
| --- | ----------------------------- | ---- | ----------------------------------------------------------- | --- | --- | --- | --- |
0
1
2
| 3   |     |     |     |     |     | 1.00 |     |
| --- | --- | --- | --- | --- | --- | ---- | --- |
4
| 5   |     |     |     |     |     | 0.75 |     |
| --- | --- | --- | --- | --- | --- | ---- | --- |
6
| 7   |     |     |     |     |     | 0.50 |     |
| --- | --- | --- | --- | --- | --- | ---- | --- |
8
| 9   |     |     |     |     |     | 0.25 2 gaL rof FCA |     |
| --- | --- | --- | --- | --- | --- | ------------------ | --- |
s ruoH 10
| 11  |     |     |     |     |     | 0.00 |     |
| --- | --- | --- | --- | --- | --- | ---- | --- |
12
13
| 14  |     |     |     |     |     | 0.25 |     |
| --- | --- | --- | --- | --- | --- | ---- | --- |
15
| 16  |     |     |     |     |     | 0.50 |     |
| --- | --- | --- | --- | --- | --- | ---- | --- |
17
| 18  |     |     |     |     |     | 0.75 |     |
| --- | --- | --- | --- | --- | --- | ---- | --- |
19 20
| 21  |     |     |     |     |     | 1.00 |     |
| --- | --- | --- | --- | --- | --- | ---- | --- |
22
23
2016-03-01 2016-09-01 2017-03-01 2017-09-01 2018-03-01 2018-09-01 2019-03-01 2019-09-01 2020-03-01
Date d
∆Pd,s
|     |     | (a) | Lag 2 autocorrelation | of  | .   |     |     |
| --- | --- | --- | --------------------- | --- | --- | --- | --- |
ID,t
|     | Autocorrelation p-value for Lag 2 of  |     | PI d D , s t for each trading session by delivery day and hour |     |     |     |     |
| --- | ------------------------------------- | --- | -------------------------------------------------------------- | --- | --- | --- | --- |
| 0   |                                       |     | ,                                                              |     |     |     |     |
1
2
3
4
| 5   |     |     |     |     |     | 0.10 |     |
| --- | --- | --- | --- | --- | --- | ---- | --- |
6
7
| 8   |     |     |     |     |     | 0.08 |     |
| --- | --- | --- | --- | --- | --- | ---- | --- |
9
| s ruoH 10 |     |     |     |     |     | eulav-p |     |
| --------- | --- | --- | --- | --- | --- | ------- | --- |
| 11        |     |     |     |     |     | 0.06    |     |
12
13
| 14  |     |     |     |     |     | 0.04 |     |
| --- | --- | --- | --- | --- | --- | ---- | --- |
15
16
| 17  |     |     |     |     |     | 0.02 |     |
| --- | --- | --- | --- | --- | --- | ---- | --- |
18
19
| 20  |     |     |     |     |     | 0.00 |     |
| --- | --- | --- | --- | --- | --- | ---- | --- |
21
22 23
2016-03-01 2016-09-01 2017-03-01 2017-09-01 2018-03-01 2018-09-01 2019-03-01 2019-09-01 2020-03-01
Date d
∆Pd,s
|     |     | (b) p-values | for lag 2 autocorrelation | of  | .   |     |     |
| --- | --- | ------------ | ------------------------- | --- | --- | --- | --- |
ID,t
Figure 19.: Autocorrelation of ∆Pd,s per trading window for lag 2 and according p-values. The first heat
ID,t
maps show the size of the correlation coefficient by delivery day d and hour s, second shows
| according | p-values. |     |     |     |     |     |     |
| --------- | --------- | --- | --- | --- | --- | --- | --- |
40

0
1
2 3
4
5
6
7
8 9 10
11 12
13
14
15
16
17
18
19
20 21
22
23
2016-03-01 2016-09-01 2017-03-01 2017-09-01 2018-03-01 2018-09-01 2019-03-01 2019-09-01 2020-03-01
Date d
s
ruoH
Autocorrelation for Lag 3 of PI d D , , s t for each trading session by delivery day and hour
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
3 gaL
rof
FCA
(a) Lag 3 autocorrelation of ∆Pd,s .
ID,t
0
1
2
3
4
5
6
7 8
9
10 11
12
13
14
15
16
17
18
19
20 21
22
23
2016-03-01 2016-09-01 2017-03-01 2017-09-01 2018-03-01 2018-09-01 2019-03-01 2019-09-01 2020-03-01
Date d
s ruoH
Autocorrelation p-value for Lag 3 of PI d D , , s t for each trading session by delivery day and hour
0.10
0.08
0.06
0.04
0.02
0.00
eulav-p
(b) p-values for lag 3 autocorrelation of ∆Pd,s .
ID,t
Figure 20.: Autocorrelation of ∆Pd,s per trading window for lag 3 and according p-values. The first heat
ID,t
maps show the size of the correlation coefficient by delivery day d and hour s, second shows
according p-values.
41

Energy Score for Mix.JSU for hour s=6 - March 11, 2020 marked red
2000
1500
1000
500
0
2017-01 2017-07 2018-01 2018-07 2019-01 2019-07 2020-01 2020-07
(a) Energy score for the Mix.JSU for hour s=6.
Energy Score for Mix.SST for hour s=6 - March 11, 2020 marked red
50000
40000
30000
20000
10000
0
2017-01 2017-07 2018-01 2018-07 2019-01 2019-07 2020-01 2020-07
(b) Energy score for the Mix.SST for hour s=6.
Figure 21.: Energy scores for Mix.JSU and Mix.SST for hour s = 6. March 11th, 2020, where price
changes ∆Pd,s where larger than 2000 EUR/MWh, is marked in red. Note that the y-axis are
ID,t
different by a factor of more than 20.
42