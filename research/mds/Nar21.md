| Optimal     | bidding         | in hourly      | and            | quarter-hourly |       |
| ----------- | --------------- | -------------- | -------------- | -------------- | ----- |
| electricity | price auctions: |                | trading        | large volumes  | of    |
| power       | with market     | impact         | and            | transaction    | costs |
|             |                 | Micha(cid:32)l | Narajewski     |                |       |
|             | University      | of             | Duisburg-Essen |                |       |
and
|     |            | Florian | Ziel           |     |     |
| --- | ---------- | ------- | -------------- | --- | --- |
|     | University | of      | Duisburg-Essen |     |     |
2202 beF 9  ]TS.nif-q[  3v40241.4012:viXra
|     |     | February | 10, 2022 |     |     |
| --- | --- | -------- | -------- | --- | --- |
Abstract
Thispaperaddressesthequestionofhowmuchtobidtomaximizetheprofitwhen
trading in two electricity markets: the hourly Day-Ahead Auction and the quarter-
hourly Intraday Auction. For optimal coordinated bidding many price scenarios are
examined, the own non-linear market impact is estimated by considering empirical
supply and demand curves, and a number of trading strategies is used. Addition-
ally, we provide theoretical results for risk neutral agents. The application study is
conducted using the German market data, but the presented methods can be easily
utilized with other two consecutive auctions. This paper contributes to the existing
literature by evaluating the costs of electricity trading, i.e. the price impact and the
transaction costs. The empirical results for the German EPEX market show that it is
far more profitable to minimize the price impact rather than maximize the arbitrage.
Keywords: electricity trading, coordinated bidding, day-ahead market, electricity price
forecasting, intraday market, portfolio optimization, auction curves, market impact, risk
averse
1

1 Introduction and motivation
Since the deregulation of the electricity markets the energy exchanges like the European
Energy Exchange (EEX) have created many trading possibilities to account for various
marketchallenges. TheelectricitytradinginEuropeconsistsoffutures,spotandbalancing
markets. Here, we deal with the biggest and the most important one – the spot market.
A brief description of the German electricity spot market can be seen in Figure 1, for
more details on the German market see e.g. Viehmann [1]. We present the German
spot electricity market as this is the biggest one in Europe, and we will also perform our
empirical study based on the data from this market.
The diversity of the trading possibilities in the market has raised new very important
questions and challenges, e.g. when and how to trade the electricity in order to maximize
the expected gain. In a perfectly efficient market with risk neutral agents this problem
would become irrelevant asthe expectedgainshould be thesame, disregarding themarket
part and product type that one would use to trade the electricity. However, this is not the
case due to the fact that the market participants do not possess the full information, and
they are highly dependent on the quality of their forecasts. Additionally, a very important
role is being played by the own price impact of the market participants, especially for the
large ones. Furthermore, some market agents may be not perfectly risk neutral but may
be risk averse.
The following paper raises the issue considering two European auction-based spot
markets: the hourly EPEX Day-Ahead Auction (DA) and the quarter-hourly Intraday
Auction (IA), as they are currently used in Germany, Netherlands, Belgium and Austria.
The DA market is the main spot market and often serves as a reference price [1]. On
the other hand, the IA was introduced in the purpose of balancing the ramping effects
of demand and power generation [2–4]. Let us note that there are countries with other
settings as e.g. France and Great Britain who use half-hourly Intraday Auctions. After a
slight adjustment, the presented analysis can be also applied to these markets.
Day-Ahead Intraday ICmarket ICcontrol
Auction Auction closes zonesclose Delivery
Quarter-Hourly
IntradayContinuous
HourlyIntradayContinuous
d−1, d−1, d−1, d, d, d,h
12:00 15:00 16:00 h−30min h−5min
Figure 1: The daily routine of the German spot electricity market. d,h correspond to the
day and hour of the delivery, respectively.
2

In the analysis, we assume that a market participant wants to trade volume of electric-
ity in a given hour, and they split it between the two markets, ignoring all other trading
possibilities, as well as not speculating against the balancing market. Limiting ourselves
only to the two auctions is a simplification to some extent, but we discuss in the paper
that it could be also generalized for usage with other markets and with a higher number
of them. Additionally, we put emphasis on large trades and the price impact they make
to the auctions. The existing studies have mostly disregarded this problem [5–9] or used
simplified settings as e.g. linear impact assumption [10, 11]. Due to this novelty, we de-
cided to start with a smaller setting for a better understanding of the problem. Moreover,
estimation of the impact in the continuous and balancing markets is very complex [12]
and deserves a separate study. We also assume that the market player places bids that are
unlimited in prices. That is to say, they bid the minimum price on the supply side and
the maximum price on the demand side. Both unlimited bidding [13] and price-volume
bidding have previously been used in the literature [5–8, 10, 11].
Even though we assume some restrictions, we take into account other major features
in the markets. As mentioned, we do consider the non-linear market impact and the
transaction costs that the trader must account for. Moreover, we assume multiple trading
strategies like minimization of the transaction costs, risk neutral and risk averse agents.
For the latter one we utilize arbitrary, but well-known in the literature and practice risk
functions such as the mean-variance utility, the value-at-risk (VaR) and the expected
shortfall, also known as the conditional value-at-risk (CVaR).
The portfolio optimization approach to the trading of the produced electricity has
alreadybeentakenintoconsiderationintheliterature. Asignificantamountoftheexisting
papers consider the setting with futures market, spot market, and bilateral contracts [14–
17]. The authors utilize the modern portfolio theory and do not estimate the own price
impact, assuming that the market participant is a price-taker. Another stream of the
literaturenametheproblemanofferingstrategy, andtheyconcernthespotday-aheadand
intradaymarketsaswellasthebalancingone[18–23]. Thesestudiesaresimilartoourone,
buttheirmaindownsideisthefactthattheyassumethemarketplayertobeaprice-taker.
This assumption automatically makes these studies inapplicable for market players that
trade medium-sized or large volumes and impact the price with their bids significantly.
An important part of the literature compares the coordinated and sequential bidding,
especially for storages [5–7, 10, 11, 13]. The authors consider a multi-market setting,
however they also simplify the market impact issue. A detailed review of coordinated
bidding literature was prepared by Aasg˚ard et al. [24].
To the best of our knowledge, the problem of portfolio optimization in auction-based
3

spot markets with market impact and trading costs has not been addressed in the liter-
ature so far. Kath and Ziel [12] investigate the optimal order execution in the intraday
continuous market accounting for the market impact. The work that is the closest to
our setting is the paper of Ay´on et al. [25] who investigate the optimal bidding curves
in day-ahead and intraday electricity markets. The authors, however, consider a flexible
demand setting and again assume not to make any price impact in the market. A big part
of the literature concerning the optimal trading problem or the bidding behaviour in the
spot markets, focuses only on one part of the market [2, 26–28]. These papers investigate
multiple aspects of the trading in the intraday continuous market. Also the renewable
energy forecasting plays a crucial role in the decision process for optimal power trading
[29, 30].
An important factor in the strategy optimization for large volumes is the price impact
estimation. We approach the problem using the aggregated curves data. Bidding in the
auction-based markets causes shifts in the demand or supply curves. We use the fact to
calculate the non-linear price impact of the market participant’s own bids. Here we also
need a forecast for the curves. Multiple papers look into the issue [31–35]. The models
are, however, very time-consuming as they estimate the full supply and demand curves.
The resulting intersection of the curves, can be regarded as an electricity price forecast.
However, usually this is not as accurate as electricity price forecasting (EPF) models
that are designed only for the purpose providing accurate price predictions. To avoid the
aforementioned problem we actually consider a modelling approach that does not need
to have curve forecast that provide accurate price predictions, but only gives reasonable
curve forecast for the neighbourhood of the expected price. It is then compared to using
the perfect forecast of both curves and prices to see the possible gain of having better,
more sophisticated models. As mentioned, we need suitable EPF models for our trading
approach, see [32, 36, 37] for reviews. However, as the objective of this study is not to
develop a new EPF model we chose to use the two well-known models often called the
naive and the expert.
Now, let us summarize the major contributions of the manuscript:
1. It is the first work concerning the electricity trading of large volumes with market
impact in the auction-based markets.
2. The first manuscript which considers transaction costs that may vary across the
considered markets.
3. We provide an extensive analysis and discussion of the price formation and trading
problem in European price auctions.
4

4. The paper presents theoretical results on optimal bidding for risk neutral agents
under linear market impact and transactions.
5. The trading setting is thoroughly examined with all the issues considered including
risk averse agents, and the possible extensions and generalization are discussed.
6. The predictive performance of the utilized methods are compared in a forecasting
study for different market players (e.g. wind and solar power traders or retailers
that just buy electricity), multiple trading strategies, and forecasts’ qualities.
7. Weprovideinsightsonimportanceoftheoverallpriceimpactreductionandevidence
of irrelevance of the arbitrage between the DA and IA markets which indicates
market efficiency.
8. The importance of this research is emphasized by the fact of launching intraday
auctions in further European countries [38].
The remainder of this manuscript has the following structure. Section 2 describes the
price formation in European price auctions. The trading setting and objective in the day-
ahead and intraday auctions are discussed in Section 3. Trading strategies are described
in Section 4. Section 5 presents the models used for the forecasting of the electricity prices
and market impact using auction curve predictions. The application including the data
description, evaluation measures and results is presented in Section 6. Section 7 discusses
the limitations and generalizations of the study where we focus on potential relaxation
of the assumptions. Finally, Section 8 concludes the paper. In the Appendix we present
the important abbreviations, the notation used in Sections 2-5, the evaluation of the EPF
models and additional figures.
2 Price formation in European price auctions
Weconsidertwoconsecutiveauctionsfortheday-ahead(DA)powermarketandtheintra-
day opening auction (IA) in Germany. The former one offers trading of hourly products,
the latter one trading of quarter-hourly products. For a selected delivery time point for
day d and hour h we have in total five products traded in five corresponding auctions.
All auctions find the market clearing price by matching supply and demand such that
welfare (consumer and producer rent) is maximized. For the day-ahead this is based on
the EUPHEMIA algorithm which incorporates the market coupling of the region to allow
cross-border trading and increase of the overall welfare.
On all markets we have non-negative volume bids BS(p) and BD(p) for p with
∈ P P
as potential price grid on the considered auction on the supply and demand side. Here
5

D represent ask/buy/demand/purchase and S represent bid/sell/supply/sale. Further,
| BS(p) | BD(p) |     |     |     |     |     |     |
| ----- | ----- | --- | --- | --- | --- | --- | --- |
and are aggregates of all bids at price p, so if multiple market participants
bid volumes at p they are aggregated in BS(p). On both markets we have a minimal bid
price increment of 0.1 EUR/MWh. For the considered markets we have p = 500,
min,DA
−
p = 3000 and p = p = 3000. Figure 2 shows an example of the bids.
| min,IA |     | max,DA | max,IA |     |     |     |     |
| ------ | --- | ------ | ------ | --- | --- | --- | --- |
−
Using the bids BS and BD on the supply and demand side we can compute the supply
and demand curves AS and AD by aggregation. More precisely, the aggregated curves
AS and AD are then defined by a linear interpolation of all aggregated bids at all bidden
(cid:80)
prices S and D. This is for the supply curve AS(p) = BS(x) for p S
x∈PS∩(−∞,p]
|     | P P |     |     |     |     |     | ∈ P |
| --- | --- | --- | --- | --- | --- | --- | --- |
(cid:80)
and for the demand curve AD(p) = BD(x) for p D. By construction, it is
x∈PD∩[p,∞)
∈ P
clear that the curves are strictly monotonic. Moreover, their inverse (AS)−1 and (AD)−1
can be regarded as continuous supply and demand curves. The unique intersection of AS
AD
and (resp. their graphs) or their inverse yields the market clearing volume and price
| (V∗,P∗).1 |     |     | AS AD |     |     |     |     |
| --------- | --- | --- | ----- | --- | --- | --- | --- |
Finally, denote and for i 0,...,4 the curves in the corresponding
|     |     |     | i i | ∈ {    | }   |     |         |
| --- | --- | --- | --- | ------ | --- | --- | ------- |
|     |     |     |     | BS BD, | S   | D.  | AS, AD, |
markets (0 = DA, 1,...,4 = IA), analogue and and Further, let
|         |         |           |          | i                 | i Pi Pi       |                         |     |
| ------- | ------- | --------- | -------- | ----------------- | ------------- | ----------------------- | --- |
| BS, BD, | PS, PD, |           |          |                   |               | AS (AS,...,AS)(cid:48). |     |
|         |         | p min and | p max be | the corresponding | vectors, e.g. | =                       |     |
0 4
An example of the curves is presented in Figure 3. For reporting purpose the exchange
rounds to a 0.01 EUR/MWh price increment, and volumes to 0.1 MW. Further, note
that especially for the day-ahead market clearing results of the intersection (V∗,P∗) does
not always equal exactly the reported market clearing volume and price of the exchange.
1Theoretically,itmayhappenthatthegraphshavenointersection. ThishappensifeitherAS(p
max )<
| AD(p | AD(p | )<AS(p |     |     |     |     | (V∗,P∗) |
| ---- | ---- | ------ | --- | --- | --- | --- | ------- |
max ) or min min ). In those extreme event scenarios, we define the intersections
by(AS(p ),p )and(AD(p ),p ). NotethatintheconsideredGermanmarket,anyofthoseevents
|                | max max                |       | min min |     |                       |     |     |
| -------------- | ---------------------- | ----- | ------- | --- | --------------------- | --- | --- |
| never happened | since                  | 2010. |         |     |                       |     |     |
|                | Day-Ahead Auction bids |       |         |     | Intraday Auction bids |     |     |
110.05
104
demand
| 100.8 3 |     |     |     |     | supply |     |     |
| ------- | --- | --- | --- | --- | ------ | --- | --- |
)WM( emuloV
102
101
0.6
0
0.4
101
102
100.23
104
0.0
0.0500 0 500 01.2000 1500 2000 205.400 3000 3000 02.6000 1000 0 0.81000 2000 30001.0
Price (EUR/MWh)
|     |     |     | BS  | BD  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Figure 2: An example of the bids and in the German market with delivery on
01.06.2017. The delivery periods are 12:00 to 13:00 for the DA and 12:00 to 12:15 for the
IA. The demand bids are plotted as negative for better comparability and the volumes are
| given in | a symmetric | logarithmic | scale |     |     |     |     |
| -------- | ----------- | ----------- | ----- | --- | --- | --- | --- |
6

|     | Day-Ahead Auction curves |     |     |     |     |     | Intraday Auction curves |     |
| --- | ------------------------ | --- | --- | --- | --- | --- | ----------------------- | --- |
1.0
| 3000 |     |     |     |     |     | 3000 |     |     |
| ---- | --- | --- | --- | --- | --- | ---- | --- | --- |
| 2000 |     |     |     |     |     | 1500 |     |     |
0.8
0
1000
)hWM/RUE( ecirP
1500
0
0.6
| 500 |     |     |     |     |     | 3000 |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- |
|     | 30  | 35  | 40  | 45  | 50  |      | 0 2 | 4 6 |
| 80  |     |     |     |     |     | 80   |     |     |
0.4
| 60  |     |     |     |     |     | 60  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 40  |     |     |     |     |     | 40  |     |     |
0.2
| 20  |     |     |     |     |     | 20  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   |     |     |     |     |     |     | 0   |     |
0.0
03.00 32 34 360.238 40 42 04.44 46 0.0 0.60.5 1.0 1.50.8 2.0 2.5 31..00
Volume (GW)
|     |     |     |     | demand | supply |     | intersection |     |
| --- | --- | --- | --- | ------ | ------ | --- | ------------ | --- |
Figure3: Anexampleofthesupplyanddemandcurves(AS)−1 and(AD)−1 intheGerman
market with delivery on 01.06.2017. The delivery periods are 12:00 to 13:00 for the DA
and 12:00 to 12:15 for the IA. The bottom plots are the zoomed-in versions of the top ones
paper.2
| There are         | sometimes |     | small | deviations, | which  | we ignore | within this |     |
| ----------------- | --------- | --- | ----- | ----------- | ------ | --------- | ----------- | --- |
| 3 Trading/Bidding |           |     |       | in          | DA and | IA        | markets     |     |
3.1 Setting
Tosimplifythetradingproblem,weconsideramarketplayerwhichonlysubmitsunlimited
bids, often referred as volume bids. Thus, we want to trade volumes = (v ,v ,v ,v )(cid:48) in
v 1 2 3 4
MWh in the corresponding market, this could be the planned wind power to be generated
in the four quarter hours of the considered hour. The trading problem is to find bids
b = (b ,b ,...,b )(cid:48) in MW for the five markets. We use the convention that the signs of
| 0   | 1   | 4   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
b indicate the market side. Thus, b > 0 are sell bids which shift the supply curve and
i
b < 0 are bids on the demand side. Obviously, the market participant may influence only
i
their own bids b. Therefore, we introduce the notation AS, AD, BS, BD which reflect
|     |     |     |     |     |     |     | b b | b b |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
the agent’s bidding behaviour. Note that the sets of bidded prices PS and PD are not
impacted by b as we assume that even without the agent’s market impact there is at least
| one further | unlimited |     | bid on | the relevant | market |     | side. |     |
| ----------- | --------- | --- | ------ | ------------ | ------ | --- | ----- | --- |
TheintersectionsofAS(p)anddemandAD(p)definethemarketclearingvolumesand
|     |     |     | b   |     |     | b   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
2Thedeviationresultsmainlyduetothehandlingofmultipleandcomplexordersatthemoneysolving
| the market | clearing | optimization |     | problem, | for more | details | see e.g. [31]. |     |
| ---------- | -------- | ------------ | --- | -------- | -------- | ------- | -------------- | --- |
7

(V∗,P∗)
prices which also depend on the own bid b. Moreover, we want to remind that
b b
the markets have a sequential order, i.e. first the DA auction is realized, and then the IA
auctions, see Figure 1. Thus, only b impacts the DA price, whereas next to b ,...,b also
|     |     |     |     | 0   |     |     |     |     |     |     | 1   | 4   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
b may have an influence on the IA auctions. This is because other market participants
0
may react on the IA auctions due to b -influenced DA auction results. We model this
0
| impact in | Section 5.2. |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Of fundamental importance are situations without own market impact, i.e. b = 0. As
it is relevant for us in further analysis, we summarize some characteristics. Obviously it
holds for arbitrary unlimited bids b that BS(p ) = BS(p ) b+ and BD(p ) =
|     |     |     |     |     |     | 0   | min | b   | min |     | 0   | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
−
BD(p ) b− where b+ and b− are the element-wise positive and negative part of b.
b max
−
Further, it holds that BS(p) = BS(p) for p > p and BD(p) = BD(p) for p < p .
|                |            |     | 0              | b                  |                     |                     | min       |             | 0                             | b         |     | max |
| -------------- | ---------- | --- | -------------- | ------------------ | ------------------- | ------------------- | --------- | ----------- | ----------------------------- | --------- | --- | --- |
| In conclusion, | we receive |     |                |                    |                     |                     |           |             |                               |           |     |     |
|                | (AS)−1(z)  | =   | (AS)−1(z       |                    | b+) and             | (AD)−1(z)           |           | =           | (AD)−1(z                      | b−).      |     | (1) |
|                | 0          |     | b              | −                  |                     |                     | 0         |             | b                             | −         |     |     |
| 3.2 Trading    | objective  |     |                |                    |                     |                     |           |             |                               |           |     |     |
| Now, the       | trader has | the | gain of        |                    |                     |                     |           |             |                               |           |     |     |
|                |            |     | (P∗)(cid:48)(s |                    | τ(cid:48)(s         |                     | b|·|)     |             | S(cid:48)b)|·|)(cid:48)R      |           |     |     |
|                | G(b;v)     | =   |                | b)                 |                     |                     |           | ((v         |                               |           |     | (2) |
|                |            |     | b              | (cid:12)           | −                   | (cid:12)            |           | − (cid:124) | −(cid:123)(cid:122) (cid:125) |           |     |     |
|                |            |     | (cid:124)      | (cid:123)(cid:122) | (cid:125) (cid:124) | (cid:123) (cid:122) | (cid:125) |             |                               |           |     |     |
|                |            |     | tradingrevenue |                    | transactioncosts    |                     |           | imbalance   |                               |           |     |     |
|                |            |     |                |                    |                     |                     |           | (cid:124)   | (cid:123)(cid:122)            | (cid:125) |     |     |
imbalancepenalty
|     |     |     |             |         |          |       |                    | (cid:12)   |          | (cid:12)        |     |     |
| --- | --- | --- | ----------- | ------- | -------- | ----- | ------------------ | ---------- | -------- | --------------- | --- | --- |
|     |     |     | 4           |         | 4        |       | (cid:88)(cid:12) 4 |            | 4        | (cid:12)        |     |     |
|     |     |     | (cid:88) P∗ |         | (cid:88) |       |                    |            | (cid:88) |                 |     |     |
|     |     | =   |             | s b     |          | τ s b | +                  | (cid:12)v  |          | s b (cid:12)R   |     | (3) |
|     |     |     |             | b,i i i |          | i i   | i                  | (cid:12) j |          | i,j i(cid:12) j |     |     |
|     |     |     |             |         | −        | |     | |                  | (cid:12)   | −        | (cid:12)        |     |     |
|     |     |     | i=0         |         | i=0      |       | j=1                |            | i=0      |                 |     |     |
where is the element-wise multiplication (also known as Hadamard product), τ is a
(cid:12)
)(cid:48)
transaction cost vector, S = (S i,j ) = (1 4 ,I 4 is a 5x4 dimensional summation matrix and
= S(cid:48)1 /4 = (s ,...,s )(cid:48) = (1,.25,.25,.25,.25)(cid:48) a summation vector which transfers MW
| s   | 4 0 | 4   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
to MWh for the corresponding markets (it contains the length of the delivery product pe-
riod for each auction). R = (R ,...,R ) is the imbalance penalty price and z|·| a element-
|     |     |     |     | 1   | 4   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
wise absolute value, i.e. z|·| = z+ +z−. The imbalance price is a cross-control area uni-
form balancing energy price (in German named REBAP: Regelzonenu¨bergreifender Ein-
heitlicher BilanzAusgleichsnergiePreis). In practice τ = (τ ,...,τ )(cid:48) = (τ ,τ ,...,τ )(cid:48)
|     |     |     |     |     |     |     |     | 0   |     | 4 DA | IA  | IA  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
satisfies τ τ , thus trading in the hourly day-ahead market is not more expensive
DA IA
≤
than trading the same volume in the intraday opening auction. Nowadays, the EPEX
| negotiate | with all market |     | participants |     | its own | trading |     | fees. |     |     |     |     |
| --------- | --------------- | --- | ------------ | --- | ------- | ------- | --- | ----- | --- | --- | --- | --- |
Note that strict market regulations require that market participants have to avoid
system imbalance. Thus, they have to satisfy the linear imbalance constraint
|     |     |     |     |     |     | S(cid:48)b = | 0   |     |     |     |     | (4) |
| --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
v
−
8

as we are not allowed to speculate against the imbalance price. Thus, under constraint
(4) the gain equation (2) simplifies to
4 4
(cid:88) (cid:88)
G(b) = (P∗)(cid:48)(s b) τ(cid:48)(s b|·|) = P∗ s b τ s b . (5)
b b,i i i i i i
(cid:12) − (cid:12) − | |
i=0 i=0
G does not depend on v any more, but v is contained in the constraint (4).
In practice, we want to maximize G with respect to b. However, one of the key
challenges is to describe adequately the price P∗. This is a multivariate random variable
b
which depends on the own bidding impact due to the bid b. To simplify this task we
considerthe’nobidding’situationwithb = 0asbaseline. Hence, wedefine∆ = P∗ P∗
b b − 0
as the price impact due to the trading of volume b. The hope is that we can easier access
∆ and P∗ than P∗.
b 0 b
We rewrite G to
4 4
(cid:88) (cid:88)
G(b) = (P∗+∆ )(cid:48)(s b) τ(cid:48)(s b|·|) = (P∗ +∆ )s b τ s b . (6)
0 b 0,i b,i i i i i i
(cid:12) − (cid:12) − | |
i=0 i=0
Note that ∆ is a highly non-linear function in b as the supply and demand curves are
b
non-linear what can be observed in Figure 3. Note that even under ∆ = 0 the remaining
b
equation is non-linear in b, as the absolute value is a non-linear function.
Now, let us assume that the market participant wants to maximize a risk functional
(G). Typically, this could be (G) = E[G] or µ-σ-utility (G) = E[G] γVar[G], but
R R R −
expected shortfall (CVaR) or value-at-risk (VaR) measures are plausible options as well.
Thus, the maximization problem is
b = argmax (G(b)). (7)
opt
R
b∈R5 withv=S(cid:48)b
Note that choosing non-linear risk measures does not seriously increase the complexity of
thetradingproblem. Thus, eveninthisrelativelysimplesettingwearefacinganon-linear
optimization problem due to the non-linearity of G. This holds even if we choose as a
R
linear functional, e.g. = E.
R
The linear imbalance constraint (4) allows us to simplify the optimization problem (7)
significantly. As v S(cid:48)b = 0 yields immediately that b = v b for i > 0, that is to say
i i 0
− −
(cid:101)b = (2b
0
,v)(cid:48) b
0
1 = (b
0
,v
1
b
0
,...,v
4
b
0
)(cid:48), (8)
− − −
and we highlight that (cid:101)b is a linear function in b
0
under the imbalance constraint (4). We
receive the one-dimensional optimization problem
bopt = (2bo
0
pt,v)(cid:48)
−
bo
0
pt1 with bo
0
pt = argmax
R
(G(v
(cid:101)
+b
0
c(cid:101)b)) (9)
b0∈R
9

For (cid:101)b the latter term in (6) are the transaction costs (b
0
) which can be simplified to
T
4
(cid:16) (cid:17) 1 (cid:88)
(b
0
) = τ(cid:48) s (cid:101)b|·| = τ
0
b
0
+ τ
i
v
i
b
0
. (10)
T (cid:12) | | 4 | − |
i=1
In addition, we want to present a decomposition of G((cid:101)b) into four interpretable com-
ponents. Disentangling the DA and IA part by remembering the definitions of (cid:101)b and s
gives
4
(cid:16) (cid:17) 1 (cid:88)(cid:16) (cid:17)
G((cid:101)b) = P
0
∗
,0
+∆
(cid:101)b,0
b
0
+
4
P
0
∗
,i
+∆
(cid:101)b,i
(v
i −
b
0
)
−T
(b
0
)
i=1
4 (cid:32) 4 (cid:33) 4
1 (cid:88) 1 (cid:88) 1 (cid:88)
= P∗ v + P∗ P∗ b +∆ b + ∆ (v b ) (b ).
4 0,i i 0,0 − 4 0,i 0 (cid:101)b,0 0 4 (cid:101)b,i i − 0 − T 0
(cid:124) (cid:123)(cid:122) (cid:125)
i=1 i=1 i=1
Transactioncosts
(cid:124) (cid:123)(cid:122) (cid:125) (cid:124) (cid:123)(cid:122) (cid:125) (cid:124) (cid:123)(cid:122) (cid:125)
IArevenue DA-IAarbitrage DA&IAmarketimpact
(11)
The four interpretable components are: a revenue term, an arbitrage term, a market
impact term and the transactions costs . We will interpret them in more detail in the
T
next section. Here, we only want to point out that the IA revenue term does not depend
on the bid b . However, in practice it usually contributes the most to the gain G, but it
0
cannot be influenced by a trader.
4 Trading strategies
4.1 Intraday Auction only
A straightforward strategy is to bid the volume v only in the IA market.
b = (0,v) = (0,v ,...,v ) (12)
IA-only 1 4
Obviously, IA-only seems odd if τ < τ holds. Moreover, we observe that the DA
DA IA
auctions have much larger volumes than the IA auctions. However, a simple counterpart
strategy DA-only that bids only at the DA auction and zero volume at the IA auctions
is only possible if v is constant, i.e. v = ... = v . Once we start having ramps in at
1 4
least one asset, we may face ramps in the accepted bids as well. Under the imbalance
constraint (4) this imbalance is removed. In our setting this forces us to bid at the IA
auction in such situations.
4.2 Minimal transaction costs
From our point of view the intuitive DA-only counterpart to IA-only is the bidding strat-
egy that minimizes transaction costs under the τ τ assumption. Intuitively this
DA IA
≤
10

approach trades as much volume in the cheaper (from the transaction cost point of view)
DA market, and balances the remaining power in the IA auction. Now, we derive the min-
imal transaction cost strategy. The transaction costs (b ) in (10) is a convex, piecewise
0
T
linear function. Thus, there exists a minimum. The minimizer of is the s-weighted
τ
|        |                  |        |             |        |          |        |            |          |        | T          | (cid:12) |      |
| ------ | ---------------- | ------ | ----------- | ------ | -------- | ------ | ---------- | -------- | ------ | ---------- | -------- | ---- |
| median | of (0,v)(cid:48) | which  | we          | define | as the   | TC-min |            | strategy |        |            |          |      |
|        | b                |        | =(cid:101)b | =      | (b       | ,v     | b          |          | ,...,v | b          | ).       | (13) |
|        |                  | TC-min | TC-min      |        | TC-min,0 |        | 1 TC-min,0 |          |        | 4 TC-min,0 |          |      |
|        |                  |        |             |        |          |        | −          |          |        | −          |          |      |
We see that the minimal transaction costs strategy depends on the transaction costs,
so in fact onτ and τ . For example, it is easy to derive that if we have v with v i v i+1
|         |        | DA  | IA      |        |     |          |     |     |     |     |     | ≤   |
| ------- | ------ | --- | ------- | ------ | --- | -------- | --- | --- | --- | --- | --- | --- |
| and v 1 | 0 then | the | optimal | volume | b   | TC-min,0 | is  |     |     |     |     |     |
≥


|     |     |     |     |     | 0,  |     | if τ | > τ |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | ---- | --- | --- | --- | --- | --- |
|     |     |     |     |     |      |     | DA   | IA  |     |     |     |     |
 
|     |     |     | b   |          | =   | v , | if τ | τ   | < 2τ |     |     | (14) |
| --- | --- | --- | --- | -------- | --- | --- | ---- | --- | ---- | --- | --- | ---- |
|     |     |     |     | TC-min,0 |     | 1   | DA   | IA  | DA   |     |     |      |
|     |     |     |     |          |    |     |      | ≤   |      |     |     |      |

 
|     |     |     |     |     |  v | ,   | if 2τ | τ   |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | ----- | --- | --- | --- | --- | --- |
|     |     |     |     |     |      | 2   | DA    | IA  |     |     |     |     |
≤
where the limiting cases τ = τ and τ = 2τ are not unique. Then, any element in
|     |     |     |     | IA  | DA  | IA  | DA  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[0,v ] and [v ,v ] is optimal, respectively. The first case in (14) is not realistic in practice.
| 1   | 1   | 2   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
For the remaining cases Figure 4 illustrates the optimal bidding strategy for selected
volume settings v. Those remaining cases in (14) are realistic and may occur in practice.
A trader with relatively cheap IA transaction trading costs that faces case 2 should trade
accordingtotheminimumtransactioncoststrategyonlythelowestproductionamongthe
four quarter hours. This would avoid any buy transactions in the IA market.
| 4.3 | Optimal | expected |     | profit | trading |     |     |     |     |     |     |     |
| --- | ------- | -------- | --- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
In this section, we analyse the optimal strategy for a risk neutral trader which maximizes
the objective (7) with respect to the expectation of = E. In this case, for equation (11)
R
we receive
|     |     |                  |     |          |          | (cid:32) |       |     |          | (cid:33) |     |     |
| --- | --- | ---------------- | --- | -------- | -------- | -------- | ----- | --- | -------- | -------- | --- | --- |
|     |     |                  |     | 1 4      |          |          |       | 1   | 4        |          |     |     |
|     |     |                  |     | (cid:88) |          |          |       |     | (cid:88) |          |     |     |
|     |     | E[G((cid:101)b)] | =   |          | E[P ∗ ]v | +        | E[P ∗ | ]   | E[P      | ∗ ] b    |     |     |
|     |     |                  |     | 4        | 0 ,i     | i        | 0 ,0  | 4   |          | 0 ,i 0   |     |     |
−
|     |     |     |                   | i=1       |                    |                     |                        |                    | i=1 |           |     |     |
| --- | --- | --- | ----------------- | --------- | ------------------ | ------------------- | ---------------------- | ------------------ | --- | --------- | --- | --- |
|     |     |     |                   | (cid:124) | (cid:123)(cid:122) | (cid:125) (cid:124) |                        | (cid:123)(cid:122) |     | (cid:125) |     |     |
|     |     |     | ExpectedIArevenue |           |                    |                     | ExpectedDA-IAarbitrage |                    |     |           |     |     |
(15)
1 4
(cid:88)
|     |     |     | +E[∆ |              | ]b + |     | E[∆          | ](v | b ) | (b ).                                    |     |     |
| --- | --- | --- | ---- | ------------ | ---- | --- | ------------ | --- | --- | ---------------------------------------- | --- | --- |
|     |     |     |      | (cid:101)b,0 | 0    | 4   | (cid:101)b,i | i   | 0   | 0                                        |     |     |
|     |     |     |      |              |      |     |              | −   | −   | T (cid:124) (cid:123)(cid:122) (cid:125) |     |     |
i=1
Transactioncosts
|     |     |     |     | (cid:124) |     | (cid:123)(cid:122) |     |     | (cid:125) |     |     |     |
| --- | --- | --- | --- | --------- | --- | ------------------ | --- | --- | --------- | --- | --- | --- |
ExpectedDA&IAmarketimpact
This decomposition into four interpretable components corresponds to the expectations in
(11). Only the transactions costs as studied in Section 4.2 remain untouched.
T
The second term in (15) is the expected arbitrage opportunity between the day-ahead
and the intraday auctions. If the price difference for trading 1 MWh (P ∗) = E[P ∗ ]
|     |     |     |     |     |     |     |     |     |     | M   | 0   | 0 ,0 − |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
11

|     | 8 DAsell |     |     | 8 DAsell    |     |     | 8 DAsell |     |     | 0   |     |     |
| --- | -------- | --- | --- | ----------- | --- | --- | -------- | --- | --- | --- | --- | --- |
|     | DAbuy    |     |     | DAbuy       |     |     | DAbuy    |     |     |     |     |     |
|     | IAsell   |     |     | I A s e l l |     |     | IAsell   |     |     |     |     |     |
|     | IAbuy    |     |     | I A b u y   |     |     | 6 IAbuy  |     |     |     |     |     |
6
|     | 6 v |     |     | v   |     |     | v   |     |     | -2  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4
4
| emuloV |     |     | emuloV |     |     | emuloV | 2   |     |     | emuloV |        |     |
| ------ | --- | --- | ------ | --- | --- | ------ | --- | --- | --- | ------ | ------ | --- |
|        | 4   |     |        |     |     |        |     |     |     | -4     |        |     |
|        |     |     |        | 2   |     |        | 0   |     |     |        |        |     |
|        | 2   |     |        |     |     |        | -2  |     |     | -6     | DAsell |     |
|        |     |     |        | 0   |     |        |     |     |     |        | DAbuy  |     |
IAsell
|     |     |                |     |                |       |     | -4  |                |       |     | IAbuy          |       |
| --- | --- | -------------- | --- | -------------- | ----- | --- | --- | -------------- | ----- | --- | -------------- | ----- |
|     | 0   |                |     | -2             |       |     |     |                |       | -8  | v              |       |
|     | Q1  | Q2 Q3 Q4       |     | Q1             | Q2 Q3 | Q4  | Q1  | Q2             | Q3 Q4 |     | Q1 Q2          | Q3 Q4 |
|     |     | DeliveryPeriod |     | DeliveryPeriod |       |     |     | DeliveryPeriod |       |     | DeliveryPeriod |       |
(a) τ DA <τ IA <2τ DA , (b) τ DA <τ IA <2τ DA , (c) τ DA <τ IA <2τ DA , (d) τ DA <τ IA <2τ DA ,
v =(2,3,5,8)(cid:48) v =(3, 2,8,5)(cid:48) v =(3, 2,8, 5)(cid:48) v =( 3, 2, 8, 5)(cid:48)
|     |          |     |     |             | −   |     |          | −   | −   |     | − − | − − |
| --- | -------- | --- | --- | ----------- | --- | --- | -------- | --- | --- | --- | --- | --- |
|     | 8 DAsell |     |     | 8 DAsell    |     |     | 8 DAsell |     |     | 0   |     |     |
|     | DAbuy    |     |     | DAbuy       |     |     | DAbuy    |     |     |     |     |     |
|     | IAsell   |     |     | I A s e l l |     |     | IAsell   |     |     |     |     |     |
|     | IAbuy    |     |     | I A b u y   |     |     | 6 IAbuy  |     |     |     |     |     |
|     | v        |     |     | 6 v         |     |     | v        |     |     |     |     |     |
|     | 6        |     |     |             |     |     |          |     |     | -2  |     |     |
4
4
| emuloV |     |     | emuloV |     |     | emuloV | 2   |     |     | emuloV |        |     |
| ------ | --- | --- | ------ | --- | --- | ------ | --- | --- | --- | ------ | ------ | --- |
|        | 4   |     |        |     |     |        |     |     |     | -4     |        |     |
|        |     |     |        | 2   |     |        | 0   |     |     |        |        |     |
|        | 2   |     |        |     |     |        | -2  |     |     | -6     | DAsell |     |
|        |     |     |        | 0   |     |        |     |     |     |        | DAbuy  |     |
IAsell
|     |     |     |     |     |     |     | -4  |     |     |     | IAbuy |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
v
|     | 0   |                |     | -2             |       |     |     |                |       | -8  |                |       |
| --- | --- | -------------- | --- | -------------- | ----- | --- | --- | -------------- | ----- | --- | -------------- | ----- |
|     | Q1  | Q2 Q3 Q4       |     | Q1             | Q2 Q3 | Q4  | Q1  | Q2             | Q3 Q4 |     | Q1 Q2          | Q3 Q4 |
|     |     | DeliveryPeriod |     | DeliveryPeriod |       |     |     | DeliveryPeriod |       |     | DeliveryPeriod |       |
(e) 2τ DA τ IA , (f) 2τ DA τ IA , (g) 2τ DA τ IA , (h) 2τ DA τ IA ,
|     |     | ≤   |     | ≤   |     |     |     | ≤   |     |     | ≤   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
v =(2,3,5,8)(cid:48) v =(3, 2,8,5)(cid:48) v =(3, 2,8, 5)(cid:48) v =( 3, 2, 8, 5)(cid:48)
|     |     |     |     |     | −   |     |     | −   | −   |     | − − | − − |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Figure 4: Illustration of optimal transaction cost minimal strategies b for different trans-
| action | costs | τ and | τ , | and target | trade | volume | v.  |     |     |     |     |     |
| ------ | ----- | ----- | --- | ---------- | ----- | ------ | --- | --- | --- | --- | --- | --- |
|        |       | DA    | IA  |            |       |        |     |     |     |     |     |     |
1 (cid:80)4 E[P ∗ ] is large, there are large arbitrage opportunities. In efficient markets the
|     | i=1 | 0 ,i |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4
| market | efficiency | assumption |     |     |     |      |     |          |      |     |     |      |
| ------ | ---------- | ---------- | --- | --- | --- | ---- | --- | -------- | ---- | --- | --- | ---- |
|        |            |            |     |     |     |      | 1   | 4        |      |     |     |      |
|        |            |            |     | ∗)  |     | ∗    |     | (cid:88) | ∗    |     |     |      |
|        |            |            |     | (P  | = 0 | E[P  | ] = | E[P      | ]    |     |     | (16) |
|        |            |            |     | M 0 | ⇔   | b ,0 | 4   |          | b ,i |     |     |      |
i=1
holds. Thus, if (16) holds the trader cannot expect any improvement of the expected gain
E[G] from the second term. The third term in (15) represents the market impact due to
the trading. If v is close to 0 then we do not expect a big impact. However, for large
| volumes | this | should | be relevant. |     |     |     |     |     |     |     |     |     |
| ------- | ---- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The expected market impact E[∆ ] in (15) depends non-linearly on b . The non-
|     |     |     |     |     | (cid:101)b,i |     |     |     |     |     | 0   |     |
| --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
linear behaviour results from the non-linearity of the auction curves (see e.g. Figure 3).
It cannot be analysed in more detail without making further assumptions. Therefore, we
| introduce |     | the linear | expected | market | impact | assumption |              |     |     |     |     |      |
| --------- | --- | ---------- | -------- | ------ | ------ | ---------- | ------------ | --- | --- | --- | --- | ---- |
|           |     |            |          |        | E[∆    | ] =        | a (cid:101)b |     |     |     |     | (17) |
|           |     |            |          |        |        | (cid:101)b | (cid:12)     |     |     |     |     |      |
wherea = (a 0 ,...,a 4 )istheexpectedlinearimpacttoanalyzeamathematicallytractable
special case. Note that is the expected linear impact and may depend on the prices P∗,
a
0
12

b
E
|     |        |            |     |      | Linear market |            | impact (17) |     |     |     |
| --- | ------ | ---------- | --- | ---- | ------------- | ---------- | ----------- | --- | --- | --- |
|     | Market | efficiency |     | (16) |               |            |             |     |     |     |
| b   |        |            |     |      |               | b E-LinImp |             |     |     |     |
E-Meff
|     |     |              |     |     | Market      | efficiency | (16)   | No market | impact     | (18) |
| --- | --- | ------------ | --- | --- | ----------- | ---------- | ------ | --------- | ---------- | ---- |
|     |     | b            |     |     |             |            |        |           | b          |      |
|     |     | E-LinImpMeff |     |     |             |            |        |           | E-NoImp    |      |
|     |     |              |     |     |             |            |        | Market    | efficiency | (16) |
|     |     |              |     |     | b           | =          | b      | (13)      |            |      |
|     |     |              |     |     | E-NoImpMeff |            | TC-min |           |            |      |
Figure 5: Special cases of analyzed models for a risk neutral trader = E.
R
P∗.
| because | ∆ may depend |     | on  |     |     |     |     |     |     |     |
| ------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|         | (cid:101)b   |     | 0   |     |     |     |     |     |     |     |
In addition to (17), we may also consider the no expected market impact assumption
given by
|     |     |     |     |     | E[∆ ] = | 0.  |     |     |     | (18) |
| --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | ---- |
(cid:101)b
Choosing a = 0 in the linear market impact case (17) leads to the no market impact
assumption. It is clear, that the no expected market impact assumption is not realistic
when trading large volumes, but it helps us understanding the optimal trading behaviour
| of rational | agents that | trade | small | volumes. |     |     |     |     |     |     |
| ----------- | ----------- | ----- | ----- | -------- | --- | --- | --- | --- | --- | --- |
The three assumptions (16), (17) and (18) open multiple combination options that
lead all to different special cases that can be analyzed. They are visualized in Figure 5.
As discussed, the b and b have the non-linear impact part which does not allow us
|     |     | E   | E-Meff |     |     |     |     |     |     |     |
| --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
to draw further analytical conclusions and has to be solved numerically. We will analyze
| the remaining | solutions | of  | Figure | 5 in | the next | paragraphs. |     |     |     |     |
| ------------- | --------- | --- | ------ | ---- | -------- | ----------- | --- | --- | --- | --- |
Underthenomarketimpactassumption(18)theexpectedgainequation(15)simplifies
to
|     |                  |     | 4        |      | (cid:32)  |                    | 4        | (cid:33)  |         |      |
| --- | ---------------- | --- | -------- | ---- | --------- | ------------------ | -------- | --------- | ------- | ---- |
|     |                  | 1   | (cid:88) |      |           | 1                  | (cid:88) |           |         |      |
|     |                  |     |          | ∗    | ∗         |                    |          | ∗         |         |      |
|     | E[G((cid:101)b)] | =   | E[P      | ]v i | + E[P     | ]                  | E[P      | ] b 0     | (b 0 ). | (19) |
|     |                  | 4   |          | 0 ,i | 0         | ,0 − 4             |          | 0 ,i      | −T      |      |
|     |                  |     | i=1      |      |           |                    | i=1      |           |         |      |
|     |                  |     |          |      | (cid:124) | (cid:123)(cid:122) |          | (cid:125) |         |      |
=M(P∗)
0
The first term is the trading revenue of volume v in the IA markets. The second term
characterizes the arbitrage opportunity of the DA and IA markets. It is linear in b 0 .
(P∗)
The corresponding slope represents the expected price relationship between the
M 0
DA and IA markets. Thus, if (b 0 ) would be zero we would choose either b 0 or
|     |     |     |     | T   |     |     |     |     |     | → ∞ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
b depending on sign of (P∗). Anyway, if the second term in (19) is zero then
0
| → −∞ |     |     |     | M   | 0   |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
13

the optimum depends only on the transaction costs (b 0 ). This is the case if b 0 = 0 or
T
the market efficiency assumption (16) holds. Thus, we have the following theorem.
Theorem 1. If the no expected market impact assumption (18) with a = 0 and the market
efficiency assumption (16) hold then the optimal trading strategy of a risk neutral trader
(i.e. = E) b E-NoImp is the minimal transaction cost strategy b TC-min .
R
Now, let us discuss the more general minimum b which is characterized by
E-NoImp
b of (19). For the a = 0 case, (19) is concave and piecewise linear as is
| E-NoImp,0 |     |     |     |     |     |     |     |     |     |     | −T  |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
concave and piecewise linear. Thus, if a global minimum b E-NoImp,0 exists, it is at one of
(0,v)(cid:48).
the 5 corners of the graph of which are in Hence, in practice we can simply
T
evaluate the function in all elements of (0,v)(cid:48) such as max((0,v)(cid:48))+1 or min((0,v)(cid:48)) 1.
−
Iftheoptimumisattheincreasedmaximumordecreasedminimumthenthereisnoglobal
optimum, otherwise the minimum correspond to the global minimum. In this case, we can
| express | b   | as  | an augmented | weighted |     | median. |     |     |     |     |     |
| ------- | --- | --- | ------------ | -------- | --- | ------- | --- | --- | --- | --- | --- |
E-NoImp,0
Now,weassumethelinearexpectedmarketimpactassumption(17)for(15)toanalyze
the corresponding solution b . It holds for the expected market impact that
E-LinImp
|         |                 |              |     | 4            |          |                  |          | 4         |          |     |      |
| ------- | --------------- | ------------ | --- | ------------ | -------- | ---------------- | -------- | --------- | -------- | --- | ---- |
|         |                 |              | 1   | (cid:88)     |          |                  | (cid:88) |           |          |     |      |
|         |                 | E[∆ ]b       | +   | E[∆          | ](v b    | ) = a(cid:48)1b2 | +        | a (v 2+2v | b ).     |     | (20) |
|         |                 |              | 0   |              | i 0      |                  |          | i         | i 0      |     |      |
|         |                 | (cid:101)b,0 | 4   | (cid:101)b,i | −        |                  | 0        | i         |          |     |      |
|         |                 |              |     | i=1          |          |                  | i=1      |           |          |     |      |
| Then we | receive         | for (15):    |     |              |          |                  |          |           |          |     |      |
|         |                 |              |     |              | (cid:32) |                  |          |           | (cid:33) |     |      |
|         | 1               | 4            |     |              |          | 1                | 4        |           |          |     |      |
|         | (cid:88)(cid:0) |              |     | (cid:1)      |          | (cid:88)         |          |           |          |     |      |
E[G((cid:101)b)] = E[P ∗ ]+a v v + E[P ∗ ] E[P ∗ ]+2a v b +a(cid:48)1b2 (b )
|     | 4         |     | 0 ,i    | i i i       | 0 ,0        | 4                  | 0                | ,i i i | 0   | 0         | 0   |
| --- | --------- | --- | ------- | ----------- | ----------- | ------------------ | ---------------- | ------ | --- | --------- | --- |
|     |           |     |         |             |             | −                  |                  |        |     |           | −T  |
|     |           | i=1 |         |             |             | i=1                |                  |        |     |           |     |
|     | (cid:124) |     |         |             |             | (cid:123)(cid:122) |                  |        |     | (cid:125) |     |
|     |           |     | =Q(b0;P | ∗,v,a)=Q0(P | ∗,v,a)+Q1(P |                    | ∗,v,a)b0+Q2(a)b2 |        |     |           |     |
|     |           |     |         | 0           | 0           |                    | 0                | 0      |     |           |     |
(21)
where we introduce the quadratic polynomial (b ) = + b + b2 for the first three
|     |     |     |     |     |     | 0   | 0   | 1 0 | 2 0 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | Q   | Q   | Q Q |     |     |     |
terms. The coefficient a(cid:48)1 in front of the quadratic term in (21) is always non-positive.
As the transaction costs (b ) are a piecewise linear function the quadratic term a(cid:48)1b2
|     |     |     |     | 0   |     |     |     |     |     |     | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
T
will always dominate for b if a(cid:48)1 < 0. Thus, we have a unique maximum if there
0
→ ±∞
| is linear, | non-zero | market | impact. |     |     |     |     |     |     |     |     |
| ---------- | -------- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
This maximum has an explicit solution. It may be computed by evaluating all maxima
of the piecewise quadratic functions choosing the corresponding maximum. Therefore,
remember that (b ) is a piecewise linear function with at most 6 different slopes. Thus,
T 0
we have to compute at most 6 solutions of quadratic functions to receive the optimum.
We want to highlight that the maximum is not necessarily the maximum of or .
|     |     |     |     |     |     |     |     |     |     | Q   | −T  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Figure 6 illustrates two possible cases. In the first example, the optimum is exactly at an
(0,v)(cid:48),
element of the namely at 2. In the second example, the optimum is not an element
of v.
(cid:101)
14

0.0
-0.2
-0.4
-0.6
-0.8
-1.0
b0
)0b(f
Functionsf 0.0
Neg.transactioncosts
Quadraticterm −T
Q
Q−T
-0.2
-0.4
-0.6
-0.8
-1.0
-2 -1 0 1 2 3 4 5 6 7 8 9 10
b0
(a) ( , , )=( 0.2,0.15, 0.05)
0 1 2
Q Q Q − −
)0b(f
Functionsf
Neg.transactioncosts
Quadraticterm −T
Q
Q−T
-2 -1 0 1 2 3 4 5 6 7 8 9 10
(b) ( , , )=( 0.2,0.05, 0.05)
0 1 2
Q Q Q − −
Figure 6: Illustration of equation (21) for v = (2,3,5,8)(cid:48), τ = 0.04 and τ = 0.1 for
DA IA
different values of ( , , ) with dashed lines that highlight the maxima values.
0 1 2
Q Q Q
Further, we want to remark that b has to be computed in the same way as
E-LinImpMeff
b . There is no structural simplification possible. Finally, note that the linear mar-
E-LinImp
ket impact coefficients a are unknown in practice and have to be estimated. Realistically,
it should depend on the price P∗ as well. So that the market impact in spiky price regions
0
is larger than in common market situations.
4.4 Risk-Averse strategies
We also consider numerical solutions of several risk averse agents. In detail, we consider:
mean-variance utility, value-at-risk (VaR) and expected shortfall (CVaR). These risk mea-
sures are well-known both in practice and in the literature [14–19]. In the mean-variance
utility, we maximize the following risk function
(G) = E[G] γVar[G] (22)
R −
to estimate the optimal bidding vector b . Here, a very important feature is the
E-Var-U
risk aversion parameter γ. In our analysis we set arbitrarily γ = 0.25. The second risk
averse function that we use to optimize the bidding vector is the value-at-risk (VaR)
(G) = VaR α (G) = inf x R : F G (x) > α = Qα (G) (23)
R { ∈ }
which with the risk aversion parameter α can be interpreted as an α-quantile of the
predicted gain. The last utilized risk measure is the expected shortfall, also known as
conditional value-at-risk (CVaR) with the following formula
1 (cid:90) α
(G) = CVaR (G) = VaR (G)dγ. (24)
α γ
R −α
0
15

In the case of CVaR also the α parameter takes the role of risk aversion parameter. Both
| for VaR       | and CVaR | we  | assume | arbitrarily |     | that | α =   | 0.05. |        |     |        |     |
| ------------- | -------- | --- | ------ | ----------- | --- | ---- | ----- | ----- | ------ | --- | ------ | --- |
| 5 Forecasting |          |     | models |             | for | the  | price | and   | market |     | impact |     |
Duetothenon-linearityofthepurchaseandsalecurves, itisprettyhardtomodeldirectly
the impacted prices P∗. Instead, we decided to model separately the not impacted price
b
vector P∗ and the price impact ∆ due to the trading of volume b. In this section, we
|           | 0            |         |     |     | b   |     |     |     |          |     |     |          |
| --------- | ------------ | ------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | -------- |
| describe  | the utilized | models. |     |     |     |     |     |     |          |     |     |          |
| 5.1 Price | models       |         |     |     |     |     |     |     |          |     |     |          |
|           |              |         |     |     |     |     |     |     | (cid:16) |     |     | (cid:17) |
LetusremindthatP∗ = (P∗ ,P∗ ,...,P∗ )andthusP∗ = P∗,DA,P∗,IAq1,...,P∗,IAq4 .
|     |     | 0   |     | 0,0 0,1 |     | 0,4 |     |     | 0,d,h |       |       |       |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- | ----- | ----- | ----- | ----- |
|     |     |     |     |         |     |     |     |     |       | 0,d,h | 0,d,h | 0,d,h |
For the scenario optimization we need many price trajectories, and we obtain them by
forecasting the expected prices and by bootstrapping then the in-sample errors. The first
expected price model that we consider is the well-known and widely utilized [36, 39, 40]
the naive model. It predicts todays prices by prices of yesterday on Tuesday, Wednesday,
Thursday and Friday, and the last week’s prices on other weekdays. Its formula is as
follows

|     |     |         |        |  P∗   |         | ,   | DoWk       | = 1 | for k = | 1,6,7, |     |      |
| --- | --- | ------- | ------ | ------- | ------- | --- | ---------- | --- | ------- | ------ | --- | ---- |
|     |     | (cid:0) |        | (cid:1) |         |     | d,h        |     |         |        |     |      |
|     |     | P       | ∗      | =       | 0,d−7,h |     |            |     |         |        |     | (25) |
|     |     | E       | 0 ,d,h |         |         |     |            |     |         |        |     |      |
|     |     |         |        |  P∗   |         | ,   | otherwise, |     |         |        |     |      |
0,d−1,h
where d and h indicate the day and the hour of the delivery, and DoWk is the day-of-
d,h
| the-week | dummy. |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The second considered model is the autoregressive with exogenous variables estimated
using the ordinary least-squares, in the literature often called the expert model [36, 40–
| 45]. It is | given   | by  |     |        |     |     |        |     |     |         |     |     |
| ---------- | ------- | --- | --- | ------ | --- | --- | ------ | --- | --- | ------- | --- | --- |
| (cid:0) ∗  | (cid:1) | ∗   |     |        | ∗   |     |        | ∗   |     |         | ∗   |     |
| E P        | = β h,1 | P   |     | +β h,2 | P   |     | +β h,3 | P   | +   | β h,4 P |     |     |
0 ,d,h (cid:12) 0 ,d−1,h (cid:12) 0 ,d−2,h (cid:12) 0 ,d−7,h (cid:12) 0 ,d−1,24
|     | (cid:124) |     |     |                       | (cid:123)(cid:122) |     |     |     | (cid:125)                | (cid:124) (cid:123)(cid:122) | (cid:125) |     |
| --- | --------- | --- | --- | --------------------- | ------------------ | --- | --- | --- | ------------------------ | ---------------------------- | --------- | --- |
|     |           |     |     | autoregressiveeffects |                    |     |     |     | yesterday’slasthourprice |                              |           |     |
7
|     |           | P∗           |           |                    |              | P∗        |           | (cid:88) | DoWi     |     |     |     |
| --- | --------- | ------------ | --------- | ------------------ | ------------ | --------- | --------- | -------- | -------- | --- | --- | --- |
|     | +β        |              |           | +β                 |              |           | +         | β        |          |     |     |     |
|     |           | h,5 (cid:12) | 0,d−1,min |                    | h,6 (cid:12) | 0,d−1,max |           | h,6+i    | (cid:12) | d,h |     |     |
|     | (cid:124) |              |           | (cid:123)(cid:122) |              |           | (cid:125) |          |          |     |     |     |
i=1
|     |     |     | non-lineareffects |     |     |     |     | (cid:124) | (cid:123)(cid:122) | (cid:125) |     |     |
| --- | --- | --- | ----------------- | --- | --- | --- | --- | --------- | ------------------ | --------- | --- | --- |
weekdaydummies
+β h,14 Load d,h +β h,15 Solar d,h +β h,16 WindOn d,h +β h,17 WindOff d,h
|     |           | (cid:12) |     |     | (cid:12) |     |     | (cid:12)           |     |     | (cid:12) |           |
| --- | --------- | -------- | --- | --- | -------- | --- | --- | ------------------ | --- | --- | -------- | --------- |
|     | (cid:124) |          |     |     |          |     |     | (cid:123)(cid:122) |     |     |          | (cid:125) |
day-aheadforecastsofelectricitygeneration/consumption
|     | +β        | h,18      | EUA                | d−2 +β              | h,19     | Coal | d−2 +β               | h,20               | Gas d−2 | +β h,21 | Oil d−2 , |     |
| --- | --------- | --------- | ------------------ | ------------------- | -------- | ---- | -------------------- | ------------------ | ------- | ------- | --------- | --- |
|     |           | (cid:12)  |                    |                     | (cid:12) |      |                      | (cid:12)           |         |         | (cid:12)  |     |
|     | (cid:124) |           | (cid:123)(cid:122) | (cid:125) (cid:124) |          |      |                      | (cid:123)(cid:122) |         |         | (cid:125) |     |
|     |           | CO2eprice |                    |                     |          |      | mostrecentfuelprices |                    |         |         |           |     |
(26)
where is the element-wise multiplication. The model is estimated separately for each
(cid:12)
of the 5 markets, however for convenience we use the vector notation. The regressors
16

considered in the model are not different to the ones utilized in the broad EPF literature.
We use autoregressive effects of lag 1, 2 and 7, the last hour’s price of the previous day,
the element-wise minimum and maximum price of the previous day, and the weekday
dummies. Additionally, we use the day-ahead forecasts of electricity load, solar, wind
onshore, and wind offshore production. Each of the vectors contains the total forecasted
power (MW) in the given time interval (hour or quarter-hour). We also feed the model
with the EUA (European Union Allowance) price which represents emission costs and the
fuel prices: API2 coal, TTF natural gas and Brent oil. Here we use the settle price lagged
by 2 as at the time of forecasting for day d, which is around 11:30 on day d 1, the settle
−
| price for day | d 1 is | not yet available. |     |     |
| ------------- | ------ | ------------------ | --- | --- |
−
The price trajectories are obtained using the bootstrap method Efron [46] which deliv-
ers very satisfying results [37, 47]. One could use more complicated probabilistic models,
but as we already mentioned in this manuscript, it is out of scope of our research. Thus,
we receive the trajectories by adding the in-sample bootstrapped errors to the forecasted
| expected | price |                           |                          |      |
| -------- | ----- | ------------------------- | ------------------------ | ---- |
|          |       | (cid:16)(cid:92) (cid:17) |                          |      |
|          |       | ∗ , m ∗                   | m                        |      |
|          |       | P(cid:98) = E P +ε        | (cid:98) for m = 1,...,M | (27) |
|          |       | 0 , d ,h 0 ,d,h           | d,h                      |      |
εm
where are drawn with replacement in-sample residuals for day d and hour h, i.e. we
(cid:98)d,h
∗ ∗
samplefromthesetofε = P P(cid:98) forj = 1,...,D. M isthenumberofpredicted
(cid:98)j,h 0 ,j,h− 0 ,j,h
trajectories and D is the number of in-sample days. Naturally M > D is possible.
| 5.2 Market | impact | models |     |     |
| ---------- | ------ | ------ | --- | --- |
The market impact is modelled using the aggregated supply AS(p) and demand AD(p)
0 0
curves. Here we make use of the fact that bidding in the auction-based markets causes
shifts in the respective curves. The curves are naturally unavailable at the time of fore-
casting, and thus we need to model them. The modelling and forecasting of the bidding
curves has been already approached in the literature [31–35], but the models are rather
complicated and time-consuming to estimate. Moreover, the obtained forecast of clearing
P∗
price is not that accurate as the one obtained using e.g. the expert model. Hence,
0
we model the curves using a functional simple moving average of the aggregated curves.
| For the recent | K days, | this is |     |     |
| -------------- | ------- | ------- | --- | --- |
K
1 (cid:88)
|     |     | A(cid:98) S (p) = | AS (p)  | (28) |
| --- | --- | ----------------- | ------- | ---- |
|     |     | 0,d,h             | 0,d−k,h |      |
K
k=1
and
K
1 (cid:88)
|     |     | A(cid:98) D (p) = | AS (p). | (29) |
| --- | --- | ----------------- | ------- | ---- |
|     |     | 0,d,h             | 0,d−k,h |      |
K
k=1
17

|     | Day-Ahead Auction curves |     |     |     |     |     | Intraday Auction curves |     |     |     |
| --- | ------------------------ | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- |
1.0
|     | 3000 |     |     |     | 3000 |     |     |     |     |     |
| --- | ---- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
|     | 2000 |     |     |     | 1500 |     |     |     |     |     |
0.8
0
1000
)hWM/RUE( ecirP
1500
0
0.6
|     | 500      |     |       |     | 3000 |     |     |     |     |     |
| --- | -------- | --- | ----- | --- | ---- | --- | --- | --- | --- | --- |
|     | 20 25 30 | 35  | 40 45 | 50  | 55   | 0   |     | 2   | 4 6 |     |
|     | 80       |     |       |     |      | 80  |     |     |     |     |
0.4
|     | 60  |     |     |     |     | 60  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 40  |     |     |     |     | 40  |     |     |     |     |
0.2
|     | 20  |     |     |     |     | 20  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 0   |     |     |     |     | 0   |     |     |     |     |
0.0
0.0 25 30 0.235 40 450.4 50 0.0 0.06.5 1.0 1.5 02.8.0 2.5 3.0 31..50
Volume (GW)
true demand true supply avg. demand avg. supply past demand past supply
|     |     |     |     |     | (cid:16) | (cid:17)−1 |     | (cid:16) | (cid:17)−1 |     |
| --- | --- | --- | --- | --- | -------- | ---------- | --- | -------- | ---------- | --- |
Figure 7: An example of the average curves A(cid:98) S and A(cid:98) D in the German
|     |     |     |     |     |     | 0,d,h |     | 0,d,h |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- | --- |
market calculated using K = 28 days before 01.06.2017. The delivery periods are 12:00
to 13:00 for the DA and 12:00 to 12:15 for the IA. The bottom plots are the zoomed-in
| versions | of the top | ones |     |     |     |     |     |     |     |     |
| -------- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
An example of such modelling and forecasting of the aggregated curves is presented in
Figure 7. We see that the model does not forecast the true curves perfectly, and especially
the location of the intersection of the forecasted curves may be very inaccurate. Still,
remember we are only interested in the impacts which is essentially given by the shape of
| the | curves around | the intersection. |     |     |     |     |     |     |     |     |
| --- | ------------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Moreover, in general the forecasted price induced as intersection of A(cid:98) S and A(cid:98) D
|     |     |     |     |     |     |     |     |     | 0,d,h | 0,d,h |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- |
∗,m
doesnotcoincidewiththeforecastedpriceP(cid:98) oftheconsideredpriceforecastingmodel,
0,d,h
e.g. naive or expert. Therefore, we shift our curve predictions so that the resulting
∗,m
intersection coincides with P(cid:98) . More precisely, without loss of generality we will shift
0,d,h
|     |     | S   |     | ∗,m |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the supply side curve A(cid:98) . As P(cid:98) differs for all m = 1,...,M this curve shift will
|     |     | 0,d,h |     | 0,d,h |     |     |     |     |     |     |
| --- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- |
depend on m as well. Thus, we define the shift for the intersection adjustment by
|     |     |               |     |             | (cid:16) (cid:17) |             | (cid:16)      | (cid:17) |     |      |
| --- | --- | ------------- | --- | ----------- | ----------------- | ----------- | ------------- | -------- | --- | ---- |
|     |     | ξ(cid:98) ∗,m | =   | A(cid:98) D | P(cid:98) ∗,m     | A(cid:98) S | P(cid:98) ∗,m | .        |     | (30) |
|     |     | 0,d,h         |     | 0,d,h       | 0,d,h             | 0,d,h       | 0,d,h         |          |     |      |
−
∗,m
Let us note that taking ξ(cid:98) we could shift the demand curve and get the same result.
− 0,d,h
|     |     |     |     |     |     |     |     | m   | ∗,m | ∗,m |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Now, rememberthatweareinterestedintheestimatedimpact∆(cid:98) = P(cid:98) P(cid:98) .
|     |     |     |     |     |     |     |     | b,d,h | b,d,h− | 0,d,h |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------ | ----- |
|     |     | ∗,m |     |     |     |     |     |       | S      | D     |
The b-impacted price P(cid:98) results from the intersection of the shifted A(cid:98) with A(cid:98) .
|            |                   | b,d,h |     |          |          |     |     |     | b,d,h | b,d,h |
| ---------- | ----------------- | ----- | --- | -------- | -------- | --- | --- | --- | ----- | ----- |
| To compute | this intersection |       | we  | may find | the root | of  |     |     |       |       |
A(cid:98) S (p)+ξ(cid:98) ∗,m A(cid:98) D (p) = A(cid:98) S (p)+ξ(cid:98) ∗,m A(cid:98) D (p)+b (31)
|     | b,d,h | 0,d,h− |     | b,d,h | 0,d,h |     | 0,d,h− | 0,d,h |     |     |
| --- | ----- | ------ | --- | ----- | ----- | --- | ------ | ----- | --- | --- |
18

|     |     |     |     |     |     |     | b+  | b−. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
where the equality holds by (1) and the fact that b = The non-linearity of the
−
function makes it impossible to find the root of (31) in an analytical way. This leads to a
need of finding it numerically. Using an optimizer is possible, but it is not very optimal
solution, as we require the solution for all m = 1,...,M and we later on have to optimize
with respect to b. This would result in using the inner optimization each iteration of the
outer optimization with high computational costs. Therefore, we decided to consider
|     |     |     |     | C(cid:98)d,h (p) | = A(cid:98) | S (p) | A(cid:98) D | (p) |     | (32) |
| --- | --- | --- | --- | ---------------- | ----------- | ----- | ----------- | --- | --- | ---- |
|     |     |     |     |                  |             | 0,d,h | 0,d,h       |     |     |      |
−
| and | want | to compute | the intersection |     | curve | C(cid:98) −1. |     |     |     |     |
| --- | ---- | ---------- | ---------------- | --- | ----- | ------------- | --- | --- | --- | --- |
d,h
For the calculation of C(cid:98) −1 we take the full price grid and compute the volumes. For
d,h
model (21) with linear market impact assumption, the linear market impact coefficients a
have to be estimated as well. Obviously, this should be the slope of the intersection curves
| at the | expected | intersection |     | as illustrated |     | in Figure | 8.  |     |     |     |
| ------ | -------- | ------------ | --- | -------------- | --- | --------- | --- | --- | --- | --- |
In the application study, we estimate a by central difference of the inverse impact
−1
curves C(cid:98) with incremental slope of average 5% of the market clearing volume of the
d,h
| past | K days.  | Formally,            | this     | is         |                |          |               |                      |          |     |
| ---- | -------- | -------------------- | -------- | ---------- | -------------- | -------- | ------------- | -------------------- | -------- | --- |
|      |          |                      | (cid:32) |            |                | (cid:33) | (cid:32)      |                      | (cid:33) |     |
|      |          |                      |          | M          |                |          |               | M                    |          |     |
|      |          |                      |          | 1 (cid:88) |                |          |               | 1 (cid:88)           |          |     |
|      |          | a = C(cid:98)        | − 1      |            | ξ(cid:98) ∗, m | +ν       | C(cid:98) − 1 | ξ(cid:98)            | ∗, m ν   |     |
|      |          | (cid:98)d,h          | d ,h     |            | 0 , d,h        |          | d ,h          |                      | 0 , d,h− |     |
|      |          |                      |          | M          |                |          | −             | M                    |          |     |
|      |          |                      |          | m=1        |                |          |               | m=1                  |          |     |
|      |          | DA impact estimation |          |            |                |          |               | IA impact estimation |          |     |
|      | 3000 1.0 |                      |          |            |                |          | 3000          |                      |          |     |
1500
2000
0.8
0
1000
| ecirp detcapmI |     |     |     |     |     |     | 1500 |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
0.6 0
|     | 500 |      |     |     |     |     | 3000 |     |       |     |
| --- | --- | ---- | --- | --- | --- | --- | ---- | --- | ----- | --- |
|     | 15  | 10 5 | 0 5 | 10  | 15  | 20  | 6    | 4 2 | 0 2 4 | 6   |
|     | 80  |      |     |     |     |     | 80   |     |       |     |
0.4
|     | 60  |     |     |     |     |     | 60  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 40  |     |     |     |     |     | 40  |     |     |     |
0.2
|     | 20    |     |     |     |     |     | 20  |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 0     |     |     |     |     |     | 0   |     |     |     |
|     | 02.00 |     |     |     |     |     | 20  |     |     |     |
01.00.0 7.5 5.0 2.50.20.0 2.5 5.0 70..54 10.0 3 0.6 2 1 0 0.8 1 2 13.0
Volume shift (GW)
|     |     |     | intersection curve |     |     | linear impact |     | expected intersection |     |     |
| --- | --- | --- | ------------------ | --- | --- | ------------- | --- | --------------------- | --- | --- |
Figure 8: An example of the predicted intersection curves C−1 in the German market
d,h
with delivery on 01.06.2017. The delivery periods are 12:00 to 13:00 for the DA and 12:00
to 12:15 for the IA. The bottom plots are the zoomed-in versions of the top ones. In
| addition, |     | the estimated | linear | impact | a is | visualized | (red). |     |     |     |
| --------- | --- | ------------- | ------ | ------ | ---- | ---------- | ------ | --- | --- | --- |
(cid:98)
19

|     |                | (cid:18) | (cid:16)(cid:92) | (cid:17) (cid:19) |     |     |
| --- | -------------- | -------- | ---------------- | ----------------- | --- | --- |
|     | 0.05 (cid:80)K | D        | P∗               |                   |     |     |
with ν = A(cid:98) E . Obviously, the 5% is an ad hoc choice, and
|     | K k=1 | 0,d,h | 0,d,h |     |     |     |
| --- | ----- | ----- | ----- | --- | --- | --- |
might be improved. However, our empirical study yield plausible results, see Figure 8.
∗,m
Given the intersection curves, we can easily calculate the P(cid:98) for m = 1,...,M by
b,d,h
|     | −1(ξ(cid:98) ∗,m |     |     | m   |     |     |
| --- | ---------------- | --- | --- | --- | --- | --- |
evaluating C(cid:98) +b), and thus also the ∆(cid:98) . The latter one is, however, not the
|     | d,h 0,d,h |     |     | b,d,h |     |     |
| --- | --------- | --- | --- | ----- | --- | --- |
final price impact. This is due to the fact that the DA and IA markets are in a sequential
order. Therefore, the b bid in the DA market can also influence the prices in the IA
0
| market. | We refer to | it with the | following | impact adjustment |     |     |
| ------- | ----------- | ----------- | --------- | ----------------- | --- | --- |
|         | ∗,m         | m           | m         | m                 | m   | m   |
∆(cid:98) = (∆(cid:98) ,∆(cid:98) +δ∆(cid:98) ,...,∆(cid:98) +δ∆(cid:98) ) (33)
|     | b,d,h | b0,d,h | b1,d,h | b0,d,h | b4,d,h | b0,d,h |
| --- | ----- | ------ | ------ | ------ | ------ | ------ |
where δ 0 is a market efficiency factor. If the two markets were inefficient and fully
≥
independent, we would use δ close to 0. However, in our study we assume a more realistic
scenario of δ = 1. In other words, we assume that the markets are efficient and a 1 EUR
price shift in the day-ahead auction results also in a 1 EUR price shift in the intraday
auction.
In order to evaluate the quality of the relatively simple curve forecasts, we consider
also a setting where we know the true curves in advance. This is naturally unrealistic,
but can help us understand the possible gain of using better curve forecasts. For the same
reason we consider also an instance of a perfect price forecast what allows us to inspect
the highest possible and at the same time highly unreachable gain rate.
| 6 Application: |             | Forecasting |     | and trading | study |     |
| -------------- | ----------- | ----------- | --- | ----------- | ----- | --- |
| 6.1 Data       | and setting |             |     |             |       |     |
For the purpose of application, we use the German market data from January 01, 2016 to
December 31, 2020. We conduct a rolling window forecasting study, which is a standard
procedure in the EPF literature. The initial in-sample data consists of D = 730 days, i.e.
2 years and the out-of-sample of 3 years, i.e. N = 1097 days.. Every day of the out-of-
sample dates we simulate a realistic situation: we estimate the price models based on the
most recent D = 730 days, bootstrap the in-sample residuals to obtain M = 1000 price
trajectories, and forecast the aggregated curves using K = 28 last days. Based on them,
we optimize the assumed risk functions using the sequential least squares programming
(SLSQP)algorithmimplementedinscipypackageinPythontoderivethetradingstrategy
(cid:98)b d,h . For the transaction costs τ DA = 0.05 EUR/MWh and τ IA = 0.10 EUR/MWh are
assumed.
In the optimization, multiple settings and volumes v are considered. We start with
= v1 which assume constant electricity generation or consumption over all hours with
v 4
20

v 1,10,100,1000 both on the supply and demand sides. This allows us to observe
∈ { }
the impact of growing volumes. Definitely more realistic are the v assumed to be 1% or
5% of the day-ahead predicted German wind or solar generation and 1% or 5% of the
day-ahead predicted German load. These portfolios are far more possible and of high
concern for practitioners. Basic summary statistics of the utilized v are presented in
Table 1. We show only the 5% values as the 1% and constant are easy to derive. In total,
we consider 14 different portfolios v and additionally we assume 2 settings concerning
the past participation in the market. In the first setting, we have a new market player
that bids the portfolio v as new in the market. In the second one, the market player
is already in the market bidding the minimal transaction cost strategy, but they would
like to evaluate their current strategy. It means that in this setting the market player is
rebidding the portfolio v in the market.
ItisworthtomentiontheforecastingofP∗ inbothsettings. Thatistosay, inthefirst
0
one the original historical price series are used as the market player is new in the market
and did not impact the prices before with their own bids. It means that the original price
series are the P∗. In the second setting however, the market player was already bidding
0
the v in the past and impacted the prices with their strategy. Here, the original price
series are the P∗ . Thus, for every v in the second setting we subtract from the prices
bTC-min
the impact of the trader caused by trading according to the b strategy. Then, we
TC-min
conduct the forecasting using the newly acquired artificial price series P∗ which depends
0
on the past trading path.
To summarize, let us remind that we use 2 models for the price forecasting: the naive
andexpertandonemodelfortheaggregatedcurves. Additionally,weuseperfectforecasts
forpricesandthecurves. Then,wetrade14variousportfoliosin2aforementionedsettings.
The portfolios are traded using 10 strategies. Three of them require no optimization: IA-
only, TC-min, E-NoImp. The other seven: E-LinImp, E-LinImpMeff, E-Meff, E,
E-Var-U, VaR and CVaR are optimized using the SLSQP algorithm.
v mean std min 25% 50% 75% max
5% of wind 551 427 15 221 429 764 2105
5% of solar 245 372 0 0 9 394 1624
5% of load -2753 472 -3796 -3151 -2748 -2368 -1621
Table1: Basicsummarystatisticsofselectedhourlyvolumesv(cid:48) 1 /4(MWh). Thevalues
d,h 4
are derived using the data from January 01, 2016 to December 31, 2020.
21

6.2 Evaluation
As the objective of this paper is not the electricity price forecasting, we present a detailed
evaluation of the forecasting accuracy price models in Appendix B. Here, we only want to
mention that for all accuracy measures the expert model shows clearly better predictive
accuracythanthenaivemodel. Thus,weexpectthetradingstrategiesbasedontheexpert
model to perform better than those based on the naive forecasting model.
For the evaluation of the bidding strategies (cid:98)b d,h we calculate an actual gain
|     |     |                      |     | ∗+∆  | )(cid:48)(s | τ(cid:48)(s    |           | | · | |     |      |
| --- | --- | -------------------- | --- | ---- | ----------- | -------------- | --------- | ----- | --- | ---- |
|     |     | G(cid:101)((cid:98)b | )   | = (P |             | (cid:98)b )    | (cid:98)b | )     |     | (34) |
|     |     |                      | d,h | 0    | (cid:98)b   | (cid:12) d,h − | (cid:12)  | d , h |     |      |
d,h
|     |     |     |     | 4        |                |               | 4        |           |     |      |
| --- | --- | --- | --- | -------- | -------------- | ------------- | -------- | --------- | --- | ---- |
|     |     |     |     | (cid:88) | ∗              |               | (cid:88) |           |     |      |
|     |     |     |     | = (P     | +∆             | )s i(cid:98)b | τ s      | (cid:98)b |     | (35) |
|     |     |     |     |          | 0 ,i (cid:98)b | ,i i,d,h −    | i i      | | i,d,h | |     |      |
d,h
|     |     |     |     | i=0 |     |     | i=0 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and for convenience and a better comparability among various v we report the average
gain in EUR/MWh
24 N
|     |     |     |     |              | 1 (cid:88)(cid:88) | G(cid:101)((cid:98)b ) |     |     |     |      |
| --- | --- | --- | --- | ------------ | ------------------ | ---------------------- | --- | --- | --- | ---- |
|     |     |     |     | G(cid:101) = |                    | d,h                    | .   |     |     | (36) |
v(cid:48)
|     |     |     |     |     | 24N    | 1 /4  |     |     |     |     |
| --- | --- | --- | --- | --- | ------ | ----- | --- | --- | --- | --- |
|     |     |     |     |     | h=1d=1 | d,h 4 |     |     |     |     |
To draw statistically significant conclusions, we perform additionally a two sample boot-
strap test to compare the performance of (cid:98)b obtained using different models and strate-
d,h
gies. Let A and B denote two strategies (cid:98)bA and (cid:98)bB . For each model pair, we com-
|     |     |     |     |     |     | d,h d,h |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
pute the p-value of two one-sided tests. In the first one we consider the null hypothesis
(cid:16) (cid:16) (cid:17)(cid:17) (cid:16) (cid:16) (cid:17)(cid:17) (cid:16) (cid:16) (cid:17)(cid:17)
: E G(cid:101) (cid:98)bA > E G(cid:101) (cid:98)bB , and in the second the reverse : E G(cid:101) (cid:98)bA
| 0                   | d,h              |     |     | d,h |     |     |     | 0   | d,h |     |
| ------------------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| H (cid:16) (cid:16) | (cid:17)(cid:17) |     |     |     |     |     |     | H   |     | ≤   |
(cid:98)bB
| E G(cid:101) | .   |     |     |     |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
d,h
Let us note that such constructed evaluation measure of the bidding strategies may
favour the E strategy as it actually optimizes the expected gain. This, however, cannot be
avoided as the E-Var-U and CVaR are not elicitable [48] which means that they cannot
be evaluated in a one step decision approach. We could additionally evaluate the α = 5%-
quantile of the actual gain what is the optimization goal of the VaR strategy, but we do
| not do | so for the | sake | of brevity. |     |     |     |     |     |     |     |
| ------ | ---------- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
6.3 Results
Tables2and3presenttheaverageactualgainG(cid:101) ofallstrategiesbandportfoliosv inboth
considered settings. The tables are split to two parts – the supply and the demand. In the
first case, we want to maximize the price, in the second one we want to minimize it. We
observe that overall the TC-min benchmark performs pretty well and the IA-only very
bad, especially for the bigger portfolios. This is caused mainly by much lower liquidity
in the IA market and thus a much higher price impact caused by the volume. Similarly,
the E-NoImp strategy fails to deliver satisfying results for bigger volumes. However, it
22

performsbestforsmallvolumeswherethenomarketimpactassumptionismet. Replacing
the no market impact (18) with the linear market impact (17) assumption keeps the very
good performance for small volumes and improves it substantially for larger volumes. By
notmakinganyadditionalassumptiononthepriceimpact, i.e. consideringtheEstrategy,
we improve the performance for large volumes even more. However, the best strategy for
large volumes is the one assuming the market efficiency (16) – E-Meff. Moreover, it is
as good for the naive forecasts as for the expert ones. This is perfectly sensible as this
strategy focuses on minimizing the overall price impact and transaction costs and ignores
the possible gain from the market arbitrage. Figure 9 presents an evidence that it is far
more profitable to minimize the price impact rather than maximize the arbitrage. Let us
remark that a much bigger improvement of the gain may be observed in the setting of
rebidding the portfolios than in the setting of a new market player when compared to the
TC-min strategy. This shows that our study may be particularly interesting for already
existing market players. However, this also indicates that the assumption of δ = 1 in
equation (33) should be verified in future research.
The enormous difference in EPF performance between the naive and expert models
Supply/Sell(thehigherthepricethebetter) Demand/Buy(thelowerthepricethebetter)
ledoM 1 10 100 1000 1%of 5%of 1%of 5%of 1 10 100 1000 1%of 5%of
Strategy
MW MW MW MW wind wind solar solar MW MW MW MW load load
IA-only 37.20 36.87 33.68 -61.20 21.78 -214.07 26.69 -84.74 37.49 37.84 40.94 117.18 66.31 1055.64
TC-min 37.43 37.34 36.78 32.55 29.73 25.48 32.69 29.38 37.57 37.67 38.23 42.82 42.13 63.10
evian
E-NoImp 37.46 37.25 35.41 -13.95 26.21 -85.85 30.30 -24.90 37.39 37.62 39.45 79.09 53.30 558.32
E-LinImp 37.46 37.28 36.59 32.56 29.52 25.41 32.55 29.33 37.39 37.60 38.37 42.70 42.14 61.99
E-LinImpMeff 37.43 37.33 36.74 32.44 29.70 25.27 32.61 29.23 37.57 37.67 38.22 42.81 42.13 64.44
E-Meff 37.43 37.33 36.76 32.66 29.74 25.59 32.65 29.43 37.57 37.66 38.21 42.62 42.03 61.58
E 37.46 37.29 36.64 32.63 29.60 25.54 32.60 29.41 37.39 37.59 38.33 42.67 42.09 61.63
E-Var-U 37.37 37.19 36.40 32.51 29.44 25.38 32.39 29.29 37.53 37.66 38.39 99.25 56.88 414.28
VaR 37.44 37.30 36.65 32.48 29.58 25.38 32.56 29.26 37.44 37.62 38.32 42.86 42.21 62.54
CVaR 37.44 37.27 36.63 32.55 29.60 25.44 32.57 29.36 37.41 37.61 38.38 42.86 42.21 62.68
trepxe
E-NoImp 37.50 37.29 35.47 -10.24 25.88 -107.88 31.30 2.68 37.35 37.57 39.37 76.70 51.83 517.79
E-LinImp 37.50 37.32 36.67 32.60 29.64 25.48 32.65 29.38 37.34 37.53 38.27 42.71 42.11 63.76
E-LinImpMeff 37.44 37.34 36.73 32.35 29.68 25.16 32.58 29.13 37.57 37.67 38.24 42.97 42.22 69.79
E-Meff 37.43 37.34 36.77 32.67 29.74 25.57 32.65 29.42 37.57 37.67 38.21 42.60 42.02 61.41
E 37.50 37.32 36.69 32.66 29.66 25.55 32.66 29.41 37.34 37.53 38.26 42.63 42.07 61.36
E-Var-U 37.45 37.31 36.66 32.51 29.60 25.29 32.58 29.30 37.40 37.57 38.33 57.16 44.96 218.01
VaR 37.47 37.33 36.69 32.52 29.64 25.37 32.61 29.29 37.42 37.58 38.25 42.74 42.14 62.18
CVaR 37.46 37.31 36.69 32.58 29.64 25.42 32.61 29.37 37.41 37.56 38.25 42.74 42.13 61.99
Table2: AverageactualgainG(cid:101) (EUR/MWh)oftheconsideredstrategiesasanewmarket
player. Colour indicates the performance column-wise (the greener, the better). With
bold, we depicted the best values in each column
23

Supply/Sell(thehigherthepricethebetter) Demand/Buy(thelowerthepricethebetter)
ledoM 1 10 100 1000 1%of 5%of 1%of 5%of 1 10 100 1000 1%of 5%of
Strategy
MW MW MW MW wind wind solar solar MW MW MW MW load load
IA-only 37.22 37.01 34.55 -37.59 23.69 -151.61 28.13 -52.56 37.47 37.70 40.08 100.42 59.55 989.44
TC-min 37.45 37.45 37.45 37.45 30.98 30.98 33.65 33.66 37.55 37.55 37.55 37.55 38.98 38.97
evian
E-NoImp 37.48 37.37 36.13 0.12 27.50 -67.09 31.19 -17.62 37.37 37.49 38.72 68.95 49.55 647.03
E-LinImp 37.48 37.40 37.34 37.79 30.86 31.20 33.56 33.80 37.37 37.47 37.61 37.18 38.78 38.05
E-LinImpMeff 37.45 37.45 37.52 37.80 31.11 31.28 33.69 33.87 37.55 37.55 37.44 37.14 38.68 38.13
E-Meff 37.45 37.45 37.52 37.91 31.11 31.40 33.71 33.93 37.55 37.54 37.45 37.10 38.66 38.04
E 37.48 37.41 37.39 37.86 30.95 31.32 33.63 33.89 37.37 37.46 37.56 37.13 38.71 38.06
E-Var-U 37.39 37.34 37.23 37.74 30.89 31.24 33.50 33.79 37.51 37.54 37.70 87.15 51.92 381.80
VaR 37.46 37.42 37.43 37.70 30.97 31.17 33.62 33.75 37.43 37.48 37.53 37.28 38.80 38.41
CVaR 37.45 37.40 37.44 37.81 31.02 31.30 33.66 33.88 37.39 37.47 37.55 37.23 38.76 38.62
trepxe
E-NoImp 37.52 37.41 36.17 1.84 27.17 -87.07 31.95 -8.77 37.33 37.45 38.65 67.48 48.61 671.17
E-LinImp 37.52 37.44 37.42 37.84 31.00 31.31 33.66 33.87 37.33 37.40 37.50 37.13 38.71 38.10
E-LinImpMeff 37.45 37.46 37.52 37.72 31.10 31.24 33.69 33.79 37.55 37.55 37.45 37.24 38.73 38.70
E-Meff 37.45 37.46 37.52 37.91 31.11 31.38 33.71 33.92 37.55 37.55 37.46 37.10 38.66 37.99
E 37.52 37.44 37.44 37.88 31.02 31.35 33.67 33.89 37.33 37.40 37.49 37.12 38.69 37.99
E-Var-U 37.47 37.45 37.46 37.80 31.04 31.27 33.66 33.85 37.38 37.45 37.62 50.15 41.41 176.12
VaR 37.48 37.45 37.47 37.76 31.03 31.22 33.66 33.80 37.41 37.45 37.47 37.21 38.75 38.25
CVaR 37.48 37.45 37.47 37.82 31.05 31.32 33.68 33.87 37.39 37.43 37.45 37.17 38.72 38.11
Table 3: Average actual gain G(cid:101) (EUR/MWh) of the considered strategies as an existing
market player rebidding their portfolio v. Colour indicates the performance row-wise (the
greener, the better). With bold, we depicted the best values in each row
does not always mean much better results in terms of trading gain. The difference in gain
between the best naive-based and expert-based strategies is often a few cents, and under
the market efficiency assumption it disappears. If we, however, consider the difference
in total actual gain, it becomes clear that better price forecasts are advantageous. For
example, if we consider the 5% of wind portfolio in the rebidding setting and the CVaR
strategy, the difference of 0.02 EUR/MWh in average may seem not very high. Taking
into account the total gain this seeming small difference translates into over 290000 EUR
of additional revenue in favour of the expert model over the analysed 1097 days. The
additional revenue is more than 10 times greater if we compare it with the benchmark
TC-min strategy.
The potential advantage of utilizing perfect curve and price forecasts can be observed
by comparing Tables 2 and 3 with Tables 5 and 6 from Appendix C. Having an oracle
forecast of the intersection curves C−1 brings further a few cents of additional gain, but
d,h
the impact of oracle price forecast is far higher for all portfolios. In the example of 5%
of wind portfolio it is 0.02 EUR/MWh using oracle curve forecast and 0.50 EUR/MWh
using additionally oracle price forecast. Thus, it is likely much more rewarding to improve
the price models rather than the curve models, especially given the wide EPF literature.
24

45M
|     | -1.26M |     | -3.56M |     |     |     | -1.27M |     | -1.21M |
| --- | ------ | --- | ------ | --- | --- | --- | ------ | --- | ------ |
-1.15M
| 44.5M 44.3M  | 358K   | 44.3M | 497K  | 44.3M | 317K  | 44.3M | 410K   | 44.3M | 348K  |
| ------------ | ------ | ----- | ----- | ----- | ----- | ----- | ------ | ----- | ----- |
| )RUE(euneveR |        |       | -953K |       |       |       |        |       | -870K |
|              | -1.18M |       |       |       | -926K |       | -1.04M |       |       |
44M
|       |                   |     |     |     | -222K-74.5K43.42M |     | -239K-81.3K43.38M |     | -340K-78.8K43.39M |
| ----- | ----------------- | --- | --- | --- | ----------------- | --- | ----------------- | --- | ----------------- |
| 43.5M | -76K -70.9K43.36M |     |     |     |                   |     |                   |     |                   |
43M
-2.61M
42.5M
|     | TC-min |     | expertE-NoImp |     | expertE-Meff |     | expertE |     | expertCVaR |
| --- | ------ | --- | ------------- | --- | ------------ | --- | ------- | --- | ---------- |
v=1%ofsolar
525M 522M-2.73M-69.7M 522M 1.4M -1.78B 522M-2.44M-64.1M 522M-2.15M-64.9M 522M-2.21M-65.3M
-33.9M
)RUE(euneveR 500M
|     |     |     |     |     | -54.2M |     | -54.2M |     | -52.8M |
| --- | --- | --- | --- | --- | ------ | --- | ------ | --- | ------ |
-69.2M
475M
|      |             |     |     |     | -9.87M-802K454.9M |     | -10.7M-814K454.4M |     | -12.4M-817K |
| ---- | ----------- | --- | --- | --- | ----------------- | --- | ----------------- | --- | ----------- |
|      | -739K449.1M |     |     |     |                   |     |                   |     | 454M        |
| 450M | -494K       |     |     |     |                   |     |                   |     |             |
425M
| 400M |        |     | -1.75B        |     |              |     |         |     |            |
| ---- | ------ | --- | ------------- | --- | ------------ | --- | ------- | --- | ---------- |
|      | TC-min |     | expertE-NoImp |     | expertE-Meff |     | expertE |     | expertCVaR |
v=5%ofwind
480M
−
500M
−
)RUE(euneveR
-518M-3.48M -518M1.03M-187M -518M -3.2M -518M -2.7M -518M-2.67M
| 520M | -42.9M |     |      |     | -38.5M |     | -39.4M |     | -39.8M |
| ---- | ------ | --- | ---- | --- | ------ | --- | ------ | --- | ------ |
| −    |        |     | -22M |     |        |     |        |     |        |
|      |        |     |      |     | -31.7M |     | -31M   |     | -29M   |
| 540M | -42.7M |     |      |     |        |     |        |     |        |
−
|      |            |     |               |         |                    |     | -8.41M-829K-560.8M |     | -10.8M-854K-561.2M |
| ---- | ---------- | --- | ------------- | ------- | ------------------ | --- | ------------------ | --- | ------------------ |
| 560M | -734K-565M |     |               |         | -6.77M-811K-560.4M |     |                    |     |                    |
| −    | -218K      |     |               |         |                    |     |                    |     |                    |
|      |            |     | -165M         | -704.6M |                    |     |                    |     |                    |
|      | TC-min     |     | expertE-NoImp |         | expertE-Meff       |     | expertE            |     | expertCVaR         |
v=1%ofload
IArevenue DA-IAarbitrage DAmarketimpact IAmarketimpact Transactioncosts Finalgain
Figure 9: Actual gain decomposition as in (11) for selected portfolios v and selected
strategies in the setting of rebidding the portfolio. The impact bars of E-NoImp strategy
push the final gain to very low values. Therefore, they are not reported for the sake of
legibility.
Figure 10 shows the results of the significance tests for selected portfolios in the rebid-
ding setting. The results for remaining portfolios can be found in Appendix C. Strategy
E-Meff is in most cases significantly better or not significantly worse than the others.
As seen before, its performance is rather undistinguishable between both price models.
This means that in both settings the market participants could significantly improve their
revenue. Figure 11 presents the average daily weight of b for selected portfolios in the
0
rebidding setting. For better clarity, we plot the risk neutral and the risk averse strategies
separately. Analogous plots for remaining portfolios can be found in Appendix C. All
strategies that do not neglect the market impact tend to vary higher between the con-
sidered markets when trading smaller portfolios. On the contrary, they put significantly
higher weight to the more liquid DA market when trading bigger portfolios. Additionally,
the strategies assuming market efficiency behave much smoother, i.e. they do not exhibit
as high spikes as the other strategies. A structural change in the weights can be observed
in the beginning of year 2020. The algorithms started then putting a much higher weight
25

to the DA market what was caused by a significant decrease of the number of offers in the
IA market. This lead to much higher impact on the prices of self bids in the IA market.
Since the curves are forecasted using only K = 28 last days, the algorithms could adjust
their behaviour relatively fast. This shows a robustness of the proposed strategies for
| changing |              | market | conditions. |     |     |              |                |     |     |
| -------- | ------------ | ------ | ----------- | --- | --- | ------------ | -------------- | --- | --- |
|          |              |        |             |     | 10% |              |                |     | 10% |
|          | IA-only      |        |             |     |     |              | IA-only        |     |     |
|          | TC-min       |        |             |     |     |              | TC-min         |     |     |
|          | E-NoImp      |        |             |     | 9%  |              | E-NoImp        |     | 9%  |
|          | E-LinImp     |        |             |     |     |              | E-LinImp       |     |     |
|          | E-LinImpMeff |        |             |     | 8%  | E-LinImpMeff |                |     | 8%  |
| evian    |              |        |             |     |     | evian        |                |     |     |
|          | E-Meff       |        |             |     | 7%  |              | E-Meff         |     | 7%  |
|          |              | E      |             |     |     |              | E              |     |     |
|          | E-Var-U      |        |             |     | 6%  |              | E-Var-U        |     | 6%  |
|          |              | VaR    |             |     |     |              | VaR            |     |     |
|          | CVaR         |        |             |     | 5%  |              | CVaR           |     | 5%  |
|          | - N oI       | m p    |             |     |     |              | - N oI m p     |     |     |
|          | E - L in     | I m p  |             |     | 4%  |              | E - L in I m p |     | 4%  |
| trepxe   | E            |        |             |     |     | trepxe       | E              |     |     |
|          | E-LinImpMeff |        |             |     | 3%  | E-LinImpMeff |                |     | 3%  |
|          | E-Meff       |        |             |     |     |              | E-Meff         |     |     |
|          |              | E      |             |     | 2%  |              | E              |     | 2%  |
|          | E-Var-U      |        |             |     |     |              | E-Var-U        |     |     |
|          |              | VaR    |             |     | 1%  |              | VaR            |     | 1%  |
|          | CVaR         |        |             |     |     |              | CVaR           |     |     |
ly in p p ff Meff ar-U R R p p ff Meff ar-U R VaR 0% ly in p p ff Meff ar-U R R p p ff Meff ar-U R VaR 0 %
IA-o n m I m I m Me E Va V a I m I m Me E Va p-value IA-o n m I m I m Me E Va V a I m I m Me E Va p-va lu e
T C - -N o L i n m p E - E-V C N o L i n m p E - E-V C T C - -N o L i n m p E - E-V C N o L i n m p E - E-V C
|        |              | E E - n I | E - E - n I |        |     |                     | E E - n I      | E - E - n I |     |
| ------ | ------------ | --------- | ----------- | ------ | --- | ------------------- | -------------- | ----------- | --- |
|        |              | - L i     | - L i       |        |     |                     | - L i          | - L i       |     |
|        |              | E         | E           |        |     |                     | E              | E           |     |
|        |              | naive     | expert      |        |     |                     | naive          | expert      |     |
|        |              | (a) v     | =1 MW       | (sell) |     |                     | (b) v =1000    | MW (sell)   |     |
|        | IA-only      |           |             |        | 10% |                     | IA-only        |             | 10% |
|        | TC-min       |           |             |        |     |                     | TC-min         |             |     |
|        |              |           |             |        | 9%  |                     |                |             | 9%  |
|        | E-NoImp      |           |             |        |     |                     | E-NoImp        |             |     |
|        | E-LinImp     |           |             |        | 8%  |                     | E-LinImp       |             | 8%  |
|        | E-LinImpMeff |           |             |        |     | E-LinImpMeff        |                |             |     |
| evian  | E-Meff       |           |             |        | 7%  | evian               | E-Meff         |             | 7%  |
|        |              | E         |             |        |     |                     | E              |             |     |
|        | E-Var-U      |           |             |        | 6%  |                     | E-Var-U        |             | 6%  |
|        |              | VaR       |             |        | 5%  |                     | VaR            |             | 5%  |
|        | CVaR         |           |             |        |     |                     | CVaR           |             |     |
|        | E - N oI     | m p       |             |        | 4%  |                     | E - N oI m p   |             | 4%  |
|        | E - L in     | I m p     |             |        |     |                     | E - L in I m p |             |     |
| trepxe | E-LinImpMeff |           |             |        |     | trepxe E-LinImpMeff |                |             |     |
|        | E-Meff       |           |             |        | 3%  |                     | E-Meff         |             | 3%  |
|        |              | E         |             |        | 2%  |                     | E              |             | 2%  |
|        | E-Var-U      |           |             |        |     |                     | E-Var-U        |             |     |
|        |              | VaR       |             |        | 1%  |                     | VaR            |             | 1%  |
|        | CVaR         |           |             |        |     |                     | CVaR           |             |     |
ly in m p m p Me ff Meff E ar-U Va R a R m p m p Me ff Meff E ar-U Va R VaR 0% ly in m p m p Me ff Meff E ar-U Va R a R m p m p Me ff Meff E ar-U Va R VaR 0 %
IA-o n C - m o I n I p - C V o I n I p - C p-value IA-o n C - m o I n I p - C V o I n I p - C p-va lu e
T -N - L i I m E E-V - N - L i I m E E-V T -N - L i I m E E-V - N - L i I m E E-V
|        |              | E E L i n | E E L i n |      |     |              | E E L i n      | E E L i n    |     |
| ------ | ------------ | --------- | --------- | ---- | --- | ------------ | -------------- | ------------ | --- |
|        |              | E -       | E -       |      |     |              | E -            | E -          |     |
|        |              | naive     | expert    |      |     |              | naive          | expert       |     |
|        |              | (c) v     | =5% of    | wind |     |              | (d) v          | =1% of solar |     |
|        | IA-only      |           |           |      | 10% |              | IA-only        |              | 10% |
|        | TC-min       |           |           |      |     |              | TC-min         |              |     |
|        | E-NoImp      |           |           |      | 9%  |              | E-NoImp        |              | 9%  |
|        | E-LinImp     |           |           |      |     |              | E-LinImp       |              |     |
|        | E-LinImpMeff |           |           |      | 8%  | E-LinImpMeff |                |              | 8%  |
| evian  |              |           |           |      |     | evian        |                |              |     |
|        | E-Meff       |           |           |      | 7%  |              | E-Meff         |              | 7%  |
|        |              | E         |           |      |     |              | E              |              |     |
|        | E-Var-U      |           |           |      | 6%  |              | E-Var-U        |              | 6%  |
|        |              | VaR       |           |      |     |              | VaR            |              |     |
|        | CVaR         |           |           |      | 5%  |              | CVaR           |              | 5%  |
|        | - N oI       | m p       |           |      |     |              | - N oI m p     |              |     |
|        | E            |           |           |      | 4%  |              | E              |              | 4%  |
| trepxe | E - L in     | I m p     |           |      |     | trepxe       | E - L in I m p |              |     |
|        | E-LinImpMeff |           |           |      | 3%  | E-LinImpMeff |                |              | 3%  |
|        | E-Meff       |           |           |      |     |              | E-Meff         |              |     |
|        |              | E         |           |      | 2%  |              | E              |              | 2%  |
|        | E-Var-U      |           |           |      |     |              | E-Var-U        |              |     |
|        |              | VaR       |           |      | 1%  |              | VaR            |              | 1%  |
|        | CVaR         |           |           |      |     |              | CVaR           |              |     |
ly in p p ff Meff ar-U R R p p ff Meff ar-U R VaR 0% ly in p p ff Meff ar-U R R p p ff Meff ar-U R VaR 0 %
IA-o n m m m Me E Va V a m m Me E Va IA-o n m m m Me E Va V a m m Me E Va
T C - -N o I L i n I m p E - E-V C N o I L i n I m p E - E-V C p-value T C - -N o I L i n I m p E - E-V C N o I L i n I m p E - E-V C p-va lu e
|     |     | E E - n I   | E - E - n I |       |     |     | E E - n I | E - E - n I |     |
| --- | --- | ----------- | ----------- | ----- | --- | --- | --------- | ----------- | --- |
|     |     | - L i       | - L i       |       |     |     | - L i     | - L i       |     |
|     |     | E           | E           |       |     |     | E         | E           |     |
|     |     | naive       | expert      |       |     |     | naive     | expert      |     |
|     |     | (e) v =1000 | MW          | (buy) |     |     | (f) v     | =1% of load |     |
Figure 10: Results of the G(cid:101) mean inequality test for selected portfolios v in the setting of
rebidding the portfolio. The plots present p-values — the closer they are to zero ( dark
→
green), the more significant the difference is between gains of X-axis strategy (better) and
| gains | of  | the Y-axis | strategy | (worse). |     |     |     |     |     |
| ----- | --- | ---------- | -------- | -------- | --- | --- | --- | --- | --- |
26

| 7   | Discussion   | on   | limitations | and | generalizations |     |     |     |
| --- | ------------ | ---- | ----------- | --- | --------------- | --- | --- | --- |
| 7.1 | Price-volume | bids |             |     |                 |     |     |     |
In the study we considered only unlimited bids. Thus, we assumed that the market player
bids always p on the supply side and p on the demand side. However, of no less
|     | min |     |     | max |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
importancearetheprice-volumebidswherethemarketparticipantsetsapricelimitonthe
bid. These could be particularly interesting for such electricity producers or consumers
1.0
0b
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
|     | − − | −   | −   | Tim−e,v=1%ofs−olar |     | −   | −   | − − |
| --- | --- | --- | --- | ------------------ | --- | --- | --- | --- |
1.0
0b
0.5
0.0
2018 − 01 2018 − 05 2018 − 09 2019 − 01 2019 Tim−e,v=5%ofw−ind 05 2019 09 2020 − 01 2020 − 05 2020 − 09 2021 − 01
1.0
0b 0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
|     | − −     | −      | −   | Tim−e,v=1%ofl−oad |          | −   | −            | − −    |
| --- | ------- | ------ | --- | ----------------- | -------- | --- | ------------ | ------ |
|     | IA-only | TC-min | E   | E-NoImp           | E-LinImp |     | E-LinImpMeff | E-Meff |
1.0
0b
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
|     | − − | −   | −   | Tim−e,v=1%ofs−olar |     | −   | −   | − − |
| --- | --- | --- | --- | ------------------ | --- | --- | --- | --- |
1.0
0b 0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
|     | − − | −   | −   | Tim−e,v=5%ofw−ind |     | −   | −   | − − |
| --- | --- | --- | --- | ----------------- | --- | --- | --- | --- |
1.0
0b 0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
|     | − − | −       | −      | Tim−e,v=1%ofl−oad |         | −   | −   | − −  |
| --- | --- | ------- | ------ | ----------------- | ------- | --- | --- | ---- |
|     |     | IA-only | TC-min |                   | E-Var-U |     | VaR | CVaR |
E
Figure 11: The average daily weight of b 0 in relation to the whole b strategy for selected
portfolios v in the setting of rebidding the portfolio. The naive-based strategies are
| excluded | for better | clarity |     |     |     |     |     |     |
| -------- | ---------- | ------- | --- | --- | --- | --- | --- | --- |
27

that can quite flexibly manage their production or consumption, e.g. hydropower and
battery storages, or natural gas, wind and solar power plants. In order to use such price-
| volume | bids, the | setting | requires | a   | slight | modification. |     |     |     |
| ------ | --------- | ------- | -------- | --- | ------ | ------------- | --- | --- | --- |
Let (b,p ) denote the pair of vectors of bids with its corresponding price limits.
lim
Placing the limited bid in the market may induce a change in the potential price grids PS
and PD as it might happen that BS(p ) = 0 or BD(p ) = 0 for i 0,...,4 . Such
|     |     |     |     | i   | lim,i |     | i   | lim,i |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | ----- | --- |
∈ { }
bids result in changing the shape of the supply AS(p) and demand AD(p) curves, as they
|     |     |     |     |     |     |     | b   |     | b   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
would be shifted in p = p . Thus, an adjustment of intersection curve estimation would
lim
be needed. Finally, to fulfil the imbalance constraint (4) one may need to introduce also
a price-limited volume vector v. A model with multiple price-volume bids would increase
| the complexity |     | of the     | trading | problem | even | further. |     |     |     |
| -------------- | --- | ---------- | ------- | ------- | ---- | -------- | --- | --- | --- |
| 7.2 Imbalance  |     | constraint |         |         |      |          |     |     |     |
Our results rely heavily on the imbalance constraint. If = and the imbalance con-
E
R
| straint | (4) does | not hold, |     | then we receive |     |          |          |          |                  |
| ------- | -------- | --------- | --- | --------------- | --- | -------- | -------- | -------- | ---------------- |
|         |          |           |     |                 |     | (cid:16) | (cid:17) | (cid:16) | (cid:17)(cid:48) |
E[G(b;v)] = E[P ∗](cid:48)(s b) τ(cid:48) b|·| (cid:0) S(cid:48)b (cid:1)|·| E[R]. (37)
|     |     |     |     | b        |     | s        |     | v   |     |
| --- | --- | --- | --- | -------- | --- | -------- | --- | --- | --- |
|     |     |     |     | (cid:12) | −   | (cid:12) | −   | −   |     |
S(cid:48)b
If the imbalance v gets small, the imbalance penalty term gets small as well. If the
−
sign of expected imbalance price E[R] is not in favour for the trader, they should have an
intrinsic motivation to have v S(cid:48)b close to zero. However, in general forcing v S(cid:48)b = 0
− −
does not lead to the global optimumm, even if R is independent of P∗.
b
| 7.3 Stochastic |     | trading |     | volume | –   | imbalance |     | uncertainty |     |
| -------------- | --- | ------- | --- | ------ | --- | --------- | --- | ----------- | --- |
The results for transaction cost minimal trading also hold for uncertain volumes to trade.
Note that the consideration of stochastic trading volumes should be the preferred choice
if the trader faces uncertainty in production or consumption. For wind and solar power
traders this is a natural situation, due to the meteorologically driven uncertainty in the
productionattimeoftheauctions. Ifwetradestochasticvolumes, denotedbytherandom
vector V = (V ,...,V ), then even the minimal transaction cost solution depends on
|     |     | 1   | 4   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
risk .
R
| If we | choose | =   | the | transaction | cost | minimal | solution | is  |     |
| ----- | ------ | --- | --- | ----------- | ---- | ------- | -------- | --- | --- |
E
R
|     |     |     |     |     |     |     | (cid:32) | 4   | (cid:33) |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------- |
(cid:88)
bo pt(V)
= argminE[ (b 0 ;V)] = argmin τ 0 b 0 τ i s iE V i b 0 . (38)
|     | 0   |     |      | T   |     |      |     | | | | | − | |
| --- | --- | --- | ---- | --- | --- | ---- | --- | --- | ----- |
|     |     |     | b0∈R |     |     | b0∈R |     |     |       |
i=1
(0,V)(cid:48).
| This can | be regarded |     | as joint | τ s-weighted |     | median | of  |     |     |
| -------- | ----------- | --- | -------- | ------------ | --- | ------ | --- | --- | --- |
(cid:12)
28

WecanalsoshowthegeneralizedversionofTheorem1: Ifweassumenomarketimpact
(18) then we receive for (cid:101)b = (2b
0
,V)(cid:48) b
0
1
−
4
E[G((cid:101)b)] = E (cid:2) P 0 ∗ ,0 b 0 (cid:3) + 4 1 (cid:88) E (cid:2) P 0 ∗ ,i (V i − b 0 ) (cid:3) − E[ T (b 0 )] (39)
i=1
Similarly as in Section 4.3, we disentangle the DA and IA component and get
4
1 (cid:88)
E[G((cid:101)b)] = E[P
0
∗
,0
]b
0
+
4
E[P
0
∗
,i
(V
i −
b
0
)]
−
E[
T
(b
0
)] (40)
i=1
4
= 1
4
(cid:88)(cid:0) E[P
0
∗
,i
]E[V
i
]+Cov[P
0
∗
,i
,V
i
] (cid:1) +
M
(P
0
∗)b
0 −
E[
T
(b
0
)]. (41)
i=1
by using E[P
0
∗
,i
(V
i −
b
0
)] = E[P
0
∗
,i
]E[V
i
]
−
b 0E[P
0
∗
,i
] + Cov[P
0
∗
,i
,V
i
]. Again, the market
efficiency assumption (P∗) = 0 leads to Theorem 1. Also without market efficiency
0
M
assumption, the solution b has the same structure based on the transaction cost
0,E-NoImp
minimal solution as the E[P
0
∗
,i
]E[V
i
] and Cov[P
0
∗
,i
,V
i
] terms are not impacted by b
0
.
The problematic part of this result is that it only holds under the imbalance con-
straint (4). For non-deterministic random variables (no Dirac measures) V S(cid:48)b = 0 can
−
never be satisfied. To maintain the results from Theorem 1 for random volumes V for
= E we have to require that the expected imbalance constraint
R
4 (cid:34)(cid:12) 4 (cid:12) (cid:35)
(cid:88) (cid:12) (cid:88) (cid:12)
E[(V S(cid:48)b)|·|)(cid:48)R] = E (cid:12) (cid:12) V j s i,j b i (cid:12) (cid:12) R j (42)
− −
(cid:12) (cid:12)
j=1 i=0
does not depend on b . Unfortunately, assuming that (42) does not depend on b is a
0 0
non-trivial assumption. However, it holds
(cid:34)(cid:12) 4 (cid:12) (cid:35) (cid:12) 4 (cid:12) (cid:34)(cid:12) 4 (cid:12) (cid:35)
(cid:12) (cid:88) (cid:12) (cid:12) (cid:88) (cid:12) (cid:12) (cid:88) (cid:12)
E (cid:12) (cid:12) V j s i,j b i (cid:12) (cid:12) R j = E (cid:12) (cid:12) V j s i,j b i (cid:12) (cid:12)E[R j ]+Cov (cid:12) (cid:12) V j s i,j b i (cid:12) (cid:12) ,R j .
− − −
(cid:12) (cid:12) (cid:12) (cid:12) (cid:12) (cid:12)
i=0 i=0 i=0
Hence, if we bid b such that
(cid:80)4
s b = med(V ) holds for the median volumes med(V )
i=0 i,j i j j
for j = 1,...,4 it follows that
(cid:12) (cid:12)
4
(cid:12) (cid:88) (cid:12)
E (cid:12) (cid:12) V j s i,j b i (cid:12) (cid:12) = 0 (43)
−
(cid:12) (cid:12)
i=0
holds. Additionally, we require that the absolute imbalance volume V
(cid:80)4
s b has
| j − i=0 i,j i |
a correlation with R that does not depend on our bids. Note that it is not required that
j
the imbalance volume is uncorrelated with the imbalance price. Summarizing, Theorem 1
holds under the no impact and market efficiency assumptions if Cor[
|
V
j −
(cid:80)4
i=0
s
i,j
b
i |
,R
j
]
does not depend on b and v = med(V ) is chosen for trading.
0 j j
However,againthissolutionisnottheglobaloptimumtothetradingproblemE[G(b;V)]
even under no market impact assumption. The general solution requires a deeper investi-
gation of the imbalance price R.
29

| 7.4 Sequential | impact | of the | markets |     |     |     |
| -------------- | ------ | ------ | ------- | --- | --- | --- |
We have accounted for the price impact caused by the sequential order of the DA and
IA markets with the introduction of δ 0 parameter in equation (33). The idea is that
≥
market participants can react in the IA market to the conditions that appeared in the
previous one. In this paper we assumed δ = 1, but the discrepancy in the results between
the two considered settings suggests that a deeper investigation of this problem may be
needed. We would rather suspect that this parameter is not equal for every quarter-hour
(or delivery period in general). Moreover, it may also depend on the price level and
possibly other factors. It is clear that its structure is not trivial and requires a thorough
analysis. Therefore, in this study we limited ourselves to the assumption of δ = 1, and we
| leave the deeper | analysis | for the future | research. |     |     |     |
| ---------------- | -------- | -------------- | --------- | --- | --- | --- |
| 7.5 Beyond       | DA und   | IA             |           |     |     |     |
TheresultsofTheorem1withoutmarketimpactcanbegeneralizedeasilytoothersettings
with two consecutive trading options where the latter market allows trading on an all
equally sized delivery periods. In such a setting, we only have to adjust the summation
S(cid:48)1/1(cid:48)S1
matrix S, such that S = (S 1 ,S 2 ) and s = for the two markets. Our setting
results from choosing = 1 and = . Similarly, we can model the setting in France
|     | S   | 1 4 S | 2 I 4 |     |     |     |
| --- | --- | ----- | ----- | --- | --- | --- |
and Great Britain where we currently have half-hourly Intraday opening auction. Here,
we simply choose S = 1 and S = I . If we consider e.g. the future market with the
|     | 1   | 2 2 | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
day-ahead base product and the day-ahead auction, then we can model this by choosing
S = 1 and S = I . If we traded in the futures market the day-ahead base and
| 1 24 | 2   | 24  |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- |
peak product then S = (1 ,1 ) would be required with 1 = (0 ,1 ,0 ). The
|     | 1   | 24 peak |     |     | peak | 7 12 5 |
| --- | --- | ------- | --- | --- | ---- | ------ |
theory remains basically the same, e.g. for b = (b ,b )(cid:48) the imbalance constraint (4) leads
1 2
to v = S(cid:48)b = S b + S b and for invertible S it holds b = S−1(v S b ). This
|     | 1 1 | 2 2 |     | 2   | 2 2 | 1 1 |
| --- | --- | --- | --- | --- | --- | --- |
−
(b(cid:48),(S−1(v
implies b = S b ))(cid:48))(cid:48). The transaction cost minimal solution can be derived
|     | 1 2 | 1 1 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
−
in the same way by minimizing (b ). Again, this is also the optimal solution under no
|     |     | T   | 1   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
market impact and the market efficiency assumption which leads to a generalized version
of Theorem 1. Note that for more than two trading options the results are not easy to
| obtain as | the problem | has to be solved | recursively. |     |     |     |
| --------- | ----------- | ---------------- | ------------ | --- | --- | --- |
8 Conclusion
The paper raised the issue of optimal bidding of various electricity portfolios between
two auction-based markets. The analysis included the market impact estimation what is
30

necessary for large market players. We considered also the transaction costs and provided
theoreticalinsightsregardingtheminimaltransactioncostsstrategy. Thelatterisoptimal
for risk neutral traders under the relatively plausible assumptions of market efficiency and
no-market impacts if the volumes to trade are small. Additionally, we considered various
strategies with no/linear/non-linear market impact assumption as well as with the (no)
market efficiency assumption. The conducted study contained a number of portfolios that
mimic the majority of electricity market participants like wind and solar power producers
–fromsmalltolargeones. Theresultsprovedthateventhoughweusedverybasicmodels
to forecast the prices and curves, we could significantly improve the overall revenue for
the majority of considered portfolios. Also, the analysis of gain components showed that
the crucial part of gain maximization is the price impact minimization, especially for large
volumes. The possible market arbitrage and the transaction costs are of marginal size
compared to the impact.
We conducted an extensive analysis of all aspects of the raised problem. The price
formation and trading in the European electricity auction markets together with possible
extensionsandchallengeswerediscussed. Thepaperleavesmanyopenquestionsforfuture
research, andwebelieveitcanbeasolidfoundationforthat. Especiallythattheattention
of researchers and practitioners may be brought to this topic additionally by the recent
launch of intraday opening auctions in further European countries [38].
Acknowledgments
This research article was partially supported by the German Research Foundation (DFG,
Germany) and the National Science Center (NCN, Poland) through BEETHOVEN grant
no. 2016/23/G/HS4/01005 (to FZ and MN), and the National Science Center (NCN,
Poland) through MAESTRO grant No. 2018/30/A/HS4/00444 (to FZ)
References
[1] J. Viehmann. State of the German Short-Term Power Market. Zeitschrift fu¨r En-
ergiewirtschaft, 41(2):87–103, Jun 2017.
[2] R. Kiesel and F. Paraschiv. Econometric analysis of 15-minute intraday electricity
prices. Energy Economics, 64:77–90, 2017.
[3] M.Kremer,R.Kiesel,andF.Paraschiv. Intradayelectricitypricingofnightcontracts.
Energies, 13(17):4501, 2020.
[4] M.Kremer,R.Kiesel,andF.Paraschiv. Aneconometricmodelforintradayelectricity
trading. PhilosophicalTransactionsoftheRoyalSocietyA,379(2202):20190624,2021.
31

[5] S.-E. Fleten and T. K. Kristoffersen. Stochastic programming for optimizing bid-
ding strategies of a Nordic hydropower producer. European Journal of Operational
| Research, | 181(2):916–928, | 2007. |     |     |     |     |
| --------- | --------------- | ----- | --- | --- | --- | --- |
[6] N. L¨ohndorf, D. Wozabal, and S. Minner. Optimizing trading decisions for hydro
storagesystemsusingapproximatedualdynamicprogramming. Operations Research,
| 61(4):810–823, | 2013. |     |     |     |     |     |
| -------------- | ----- | --- | --- | --- | --- | --- |
[7] N. L¨ohndorf and D. Wozabal. The Value of Coordination in Multimarket Bidding of
| Grid Energy | Storage. | Submitted, | 2020. |     |     |     |
| ----------- | -------- | ---------- | ----- | --- | --- | --- |
[8] B. Finnah. Optimal bidding functions for renewable energies in sequential electricity
| markets. | OR Spectrum, | pages | 1–27, 2021. |     |     |     |
| -------- | ------------ | ----- | ----------- | --- | --- | --- |
[9] B. Finnah, J. G¨onsch, and F. Ziel. Integrated day-ahead and intraday self-schedule
bidding for energy storage systems using approximate dynamic programming. Euro-
| pean Journal | of Operational | Research, |     | 2021. |     |     |
| ------------ | -------------- | --------- | --- | ----- | --- | --- |
[10] T. K. Boomsma, N. Juul, and S.-E. Fleten. Bidding in sequential electricity markets:
The Nordic case. European Journal of Operational Research, 238(3):797–809, 2014.
[11] H.Kongelf, K. Overrein, G.Klæboe, andS.-E. Fleten. Portfoliosize’s effectson gains
fromcoordinatedbiddinginelectricitymarkets. EnergySystems,10(3):567–591,2019.
[12] C. Kath and F. Ziel. Optimal Order Execution in Intraday Markets: Minimizing
| Costs in | Trade Trajectories. | arXiv | preprint | arXiv:2009.07892, |     | 2020. |
| -------- | ------------------- | ----- | -------- | ----------------- | --- | ----- |
[13] J. H. Kim and W. B. Powell. Optimal energy commitments with storage and inter-
| mittent | supply. Operations | research, |     | 59(6):1347–1360, | 2011. |     |
| ------- | ------------------ | --------- | --- | ---------------- | ----- | --- |
[14] M. Liu and F. F. Wu. Portfolio optimization in electricity markets. Electric Power
| systems | research, 77(8):1000–1009, |     | 2007. |     |     |     |
| ------- | -------------------------- | --- | ----- | --- | --- | --- |
[15] R. C. Garcia, V. Gonz´alez, J. Contreras, and J. E. Custodio. Applying modern port-
folio theory for a dynamic energy portfolio allocation in electricity markets. Electric
| Power Systems | Research, | 150:11–23, | 2017. |     |     |     |
| ------------- | --------- | ---------- | ----- | --- | --- | --- |
[16] R. P. Odeh, D. Watts, and M. Negrete-Pincetic. Portfolio applications in electricity
markets review: Private investor and manager perspective trends. Renewable and
| Sustainable | Energy Reviews, | 81:192–204, |     | 2018. |     |     |
| ----------- | --------------- | ----------- | --- | ----- | --- | --- |
[17] E.Canelas, T.Pinto-Varela, andB.Sawik. Electricityportfoliooptimizationforlarge
consumers: Iberian electricity market case study. Energies, 13(9):2249, 2020.
[18] T. Dai and W. Qiao. Optimal bidding strategy of a strategic wind power producer
in the short-term market. IEEE Transactions on Sustainable Energy, 6(3):707–719,
2015.
[19] L.BaringoandA.J.Conejo. Offeringstrategyofwind-powerproducer: Amulti-stage
32

risk-constrained approach. IEEE Transactions on Power Systems, 31(2):1420–1429,
2015.
[20] N. Mazzi, J. Kazempour, and P. Pinson. Price-taker offering strategy in electricity
pay-as-bid markets. IEEE Transactions on Power Systems, 33(2):2175–2183, 2017.
[21] C. Kath and F. Ziel. The value of forecasts: Quantifying the economic gains of
accurate quarter-hourly electricity price forecasts. Energy Economics, 76:411–423,
2018.
[22] T. Rintam¨aki, A. S. Siddiqui, and A. Salo. Strategic offering of a flexible producer in
day-ahead and intraday power markets. European Journal of Operational Research,
284(3):1136–1153, 2020.
[23] D.WozabalandG.Rameseder. OptimalbiddingofavirtualpowerplantontheSpan-
ish day-ahead and intraday market for electricity. European Journal of Operational
Research, 280(2):639–655, 2020.
[24] E. K. Aasg˚ard, S.-E. Fleten, M. Kaut, K. Midthun, and G. A. Perez-Valdes. Hy-
dropower bidding in a multi-market setting. Energy Systems, 10(3):543–565, 2019.
[25] X. Ay´on, M. A´. Moreno, and J. Usaola. Aggregators’ optimal bidding strategy in
sequentialday-aheadandintradayelectricityspotmarkets. Energies,10(4):450,2017.
[26] M. Narajewski and F. Ziel. Estimation and Simulation of the Transaction Arrival
Process in Intraday Electricity Markets. Energies, 12(23):4518, 2019.
[27] N. Graf von Luckner and R. Kiesel. Modeling market order arrivals on the intraday
market for electricity deliveries in Germany with the Hawkes process. Available at
SSRN, 2020.
[28] S. Glas, R. Kiesel, S. Kolkmann, M. Kremer, N. G. von Luckner, L. Ostmeier, et al.
Intraday renewable electricity trading: advanced modeling and numerical optimal
control. Journal of Mathematics in Industry, 10(1):3, 2020.
[29] M. Kozlova, S.-E. Fleten, and V. Hagspiel. Optimal timing and capacity choice under
the rate-of-return renewable energy support. MethodsX, 7:100828, 2020.
[30] W. Li and F. Paraschiv. Modelling the evolution of wind and solar power infeed
forecasts. Journal of Commodity Markets, page 100189, 2021.
[31] F. Ziel and R. Steinert. Electricity price forecasting using sale and purchase curves:
The X-Model. Energy Economics, 59:435–454, 2016.
[32] F. Ziel and R. Steinert. Probabilistic mid-and long-term electricity price forecasting.
Renewable and Sustainable Energy Reviews, 94:251–266, 2018.
[33] G. Mestre, J. Portela, A. M. San Roque, and E. Alonso. Forecasting hourly supply
curvesintheItalianDay-Aheadelectricitymarketwithadouble-seasonalSARMAHX
33

model. International Journal of Electrical Power & Energy Systems, 121:106083,
2020.
[34] S. Kulakov. X-model: further development and possible modifications. Forecasting,
| 2(1):20–35, | 2020. |     |     |     |     |     |
| ----------- | ----- | --- | --- | --- | --- | --- |
[35] M. Soloviova and T. Vargiolu. Efficient representation of supply and demand curves
on day-ahead electricity markets. Journal of Energy Markets, 14, 2021.
[36] R. Weron. Electricity price forecasting: A review of the state-of-the-art with a look
into the future. International journal of forecasting, 30(4):1030–1081, 2014.
[37] J. Nowotarski and R. Weron. Recent advances in electricity price forecasting: A
review of probabilistic forecasting. Renewable and Sustainable Energy Reviews, 81:
| 1548–1568, | 2018. |     |     |     |     |     |
| ---------- | ----- | --- | --- | --- | --- | --- |
[38] EPEX SPOT and ECC successfully launch Intraday auctions in Austria, Belgium,
France and the Netherlands. https://www.epexspot.com/en/news/epex-spot-
and-ecc-successfully-launch-intraday-auctions-austria-belgium-france-
| and-netherlands. |     | Accessed: | 2021-03-18. |     |     |     |
| ---------------- | --- | --------- | ----------- | --- | --- | --- |
[39] F. J. Nogales, J. Contreras, A. J. Conejo, and R. Esp´ınola. Forecasting next-day
electricity prices by time series models. IEEE Transactions on power systems, 17(2):
| 342–348, | 2002. |     |     |     |     |     |
| -------- | ----- | --- | --- | --- | --- | --- |
[40] F. Ziel and R. Weron. Day-ahead electricity price forecasting with high-dimensional
structures: Univariate vs. multivariate modeling frameworks. Energy Economics, 70:
| 396–420, | 2018. |     |     |     |     |     |
| -------- | ----- | --- | --- | --- | --- | --- |
[41] K.Maciejowska, B.Uniejewski, andT.Serafin. PCAForecastAveraging—Predicting
Day-Ahead and Intraday Electricity Prices. Energies, 13(14):3530, 2020.
[42] B. Uniejewski, R. Weron, and F. Ziel. Variance stabilizing transformations for elec-
tricityspotpriceforecasting. IEEE Transactions on Power Systems,33(2):2219–2229,
2017.
[43] B.UniejewskiandR.Weron. Efficientforecastingofelectricityspotpriceswithexpert
| and LASSO | models. | Energies, | 11(8):2039, | 2018. |     |     |
| --------- | ------- | --------- | ----------- | ----- | --- | --- |
[44] M. Narajewski and F. Ziel. Econometric modelling and forecasting of intraday elec-
| tricity prices. | Journal | of Commodity |     | Markets, | 19:100107, | 2020. |
| --------------- | ------- | ------------ | --- | -------- | ---------- | ----- |
[45] B. Uniejewski, G. Marcjasz, and R. Weron. Understanding intraday electricity mar-
kets: Variable selection and very short-term price forecasting using LASSO. Interna-
| tional Journal | of  | Forecasting, | 35(4):1533–1547, |     | 2019. |     |
| -------------- | --- | ------------ | ---------------- | --- | ----- | --- |
[46] B. Efron. Bootstrap Methods: Another Look at the Jackknife. The Annals of Statis-
| tics, pages | 1–26, | 1979. |     |     |     |     |
| ----------- | ----- | ----- | --- | --- | --- | --- |
34

[47] B. Uniejewski, G. Marcjasz, and R. Weron. On the importance of the long-term
seasonal component in day-ahead electricity price forecasting: Part ii—probabilistic
forecasting. Energy Economics, 79:171–182, 2019.
[48] T. Gneiting. Making and evaluating point forecasts. Journal of the American Statis-
tical Association, 106(494):746–762, 2011.
[49] T. Gneiting and A. E. Raftery. Strictly proper scoring rules, prediction, and estima-
tion. Journal of the American statistical Association, 102(477):359–378, 2007.
[50] M. Narajewski and F. Ziel. Ensemble forecasting for intraday electricity prices: Sim-
ulating trajectories. Applied Energy, 279:115801, 2020.
Appendix A
A.1 Abbreviations
CVaR Conditional value-at-risk
DA Day-Ahead Auction
EEX European Energy Exchange
EPEX European Power Exchange
EPF Electricity price forecasting
E-Var-U Mean-variance utility
IA Intraday Auction
IA-only strategy to bid only in the IA market
LinImp strategy assuming the linear price impact
Meff strategy assuming the market efficiency
NoImp strategy assuming no price impact
REBAP Cross-control area uniform balancing energy price (abbreviation from German)
TC-min strategy to bid at minimum transaction cost
VaR Value-at-risk
A.2 Notation used in Sections 2-5
element-wise multiplication (Hadamard product)
(cid:12)
z|·| element-wise absolute value, i.e. z|·| =z++z−
AD/S aggregated demand/supply curve impacted by own bid b in the ith market
b,i
A(cid:98) D/S estimator for the not impacted aggregated demand/supply curve for day d and hour h
0,d,h
a expected slope of the linear impact in the ith market
i
a vector of expected slopes of the linear impact
a estimator of the slope of the linear impact on day d and hour h
(cid:98)d,h
α risk aversion parameter of VaR and CVaR
35

BD/S
|     | non-negative |     | demand/supply |     | volume |     | bids impacted |     | by own bid b |
| --- | ------------ | --- | ------------- | --- | ------ | --- | ------------- | --- | ------------ |
b,i
D/S vector of non-negative demand/supply volume bids impacted by own bid
B b
b
| b   | bid in | the ith | market |     |     |     |     |     |     |
| --- | ------ | ------- | ------ | --- | --- | --- | --- | --- | --- |
i
|     | vector | of bids |     |     |     |     |     |     |     |
| --- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
b
| b+/−       | element-wise   |             | positive/negative |          |     | part of     | b   |     |     |
| ---------- | -------------- | ----------- | ----------------- | -------- | --- | ----------- | --- | --- | --- |
| (cid:101)b | (cid:101)b=(2b | ,v)(cid:48) | b 1               | – vector | of  | bids linear | in  | b   |     |
|            |                | 0           | 0                 |          |     |             |     | 0   |     |
−
| C(cid:98)d,h | estimated | intersection |        | curve | for     | day       | d and | hour h |     |
| ------------ | --------- | ------------ | ------ | ----- | ------- | --------- | ----- | ------ | --- |
| ∆            | price     | impact       | due to | the   | trading | of volume | b     |        |     |
b
∗,m
∆(cid:98) estimated price impact of mth scenario due to the trading of volume b
b,d,h
| δ   | market | efficiency | factor |     |     |     |     |     |     |
| --- | ------ | ---------- | ------ | --- | --- | --- | --- | --- | --- |
εm
(cid:98)d,h mth drawn with replacement in-sample residual for day d and hour h
| G          | gain          | function |            |        |            |      |          |            |     |
| ---------- | ------------- | -------- | ---------- | ------ | ---------- | ---- | -------- | ---------- | --- |
| G(cid:101) | actual        | gain     | function   |        |            |      |          |            |     |
| γ          | risk aversion |          | parameter  |        | of E-Var-U |      | strategy |            |     |
| i          | i 0,...,4     |          | is a       | market | index      | with | 0=DA,    | 1,...,4=IA |     |
|            | ∈{            |          | }          |        |            |      |          |            |     |
| (P∗)       | expected      | price    | difference |        | between    | the  | DA and   | the IA     |     |
0
M
| m   | m=1,...,M |          | is a  | bootstrapping |     | index  |     |     |     |
| --- | --------- | -------- | ----- | ------------- | --- | ------ | --- | --- | --- |
| P∗  | market    | clearing | price | impacted      |     | by bid | b   |     |     |
b,i
| P∗  | vector | of market | clearing |     | prices | impacted | by  | bid |     |
| --- | ------ | --------- | -------- | --- | ------ | -------- | --- | --- | --- |
| b   |        |           |          |     |        |          |     | b   |     |
∗,m
| P(cid:98) | vector | mth | forecasted | prices | for | day | d and | hour h |     |
| --------- | ------ | --- | ---------- | ------ | --- | --- | ----- | ------ | --- |
0,d,h
| D/S | price | grid in | the considered |     | auction |     |     |     |     |
| --- | ----- | ------- | -------------- | --- | ------- | --- | --- | --- | --- |
Pi
PD/S
|     | vector  | of price   | grids |        |      |        |       |     |     |
| --- | ------- | ---------- | ----- | ------ | ---- | ------ | ----- | --- | --- |
| p   | maximum | price      | bid,  | p      | =p   |        | =3000 |     |     |
| max |         |            |       | max,DA |      | max,IA |       |     |     |
| p   | vector  | of maximum |       | price  | bids |        |       |     |     |
max
| p     | minimum | price      | bid, | p      | =    | 500, | p      | = 3000 |     |
| ----- | ------- | ---------- | ---- | ------ | ---- | ---- | ------ | ------ | --- |
| min   |         |            |      | min,DA |      |      | min,IA |        |     |
|       |         |            |      |        |      | −    |        | −      |     |
| p min | vector  | of minimum |      | price  | bids |      |        |        |     |
risk functional
R
| R j | imbalance | price   | in  | jth quarter-hour |     |     |     |     |     |
| --- | --------- | ------- | --- | ---------------- | --- | --- | --- | --- | --- |
| R   | imbalance | (REBAP) |     | price            |     |     |     |     |     |
)(cid:48)
S S =(S i,j )=(1 4 ,I 4 is a 5x4 dimensional summation matrix
s s=S(cid:48)1 /4=(1,.25,.25,.25,.25)(cid:48) is a summation vector converting MW to MWh
4
|     | simplified | transaction |     | cost | function |     |     |     |     |
| --- | ---------- | ----------- | --- | ---- | -------- | --- | --- | --- | --- |
T
| τ   | transaction |     | cost in | the ith | market |     |     |     |     |
| --- | ----------- | --- | ------- | ------- | ------ | --- | --- | --- | --- |
i
|     | vector | of transaction |     | costs |     |     |     |     |     |
| --- | ------ | -------------- | --- | ----- | --- | --- | --- | --- | --- |
τ
| V∗  | market | clearing | volume |     | impacted | by  | bid b | in the ith | market |
| --- | ------ | -------- | ------ | --- | -------- | --- | ----- | ---------- | ------ |
b,i
| V∗  | vector | of market | clearing |     | volumes | impacted |     | by bid | b   |
| --- | ------ | --------- | -------- | --- | ------- | -------- | --- | ------ | --- |
b
| v   | volume | to be      | traded | in jth | quarter-hour |        | with  | j    | 1,...,4 |
| --- | ------ | ---------- | ------ | ------ | ------------ | ------ | ----- | ---- | ------- |
| j   |        |            |        |        |              |        |       | ∈{   | }       |
| v   | vector | of volumes |        | to be  | traded       | in the | given | hour |         |
∗,m
ξ(cid:98) mth shift for the intersection adjustment for day d and hour h
0,d,h
36

| Appendix |     |     | B   |     |     |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
WepresentthevaluesofRMSE,MAEandCRPSwhicharestrictlyproperscoringrulesfor
the mean, median and marginal distribution forecasts [49]. These measures are commonly
used by the practitioners and researchers [50]. We report also the bias of the forecasted
| price | trajectories. |     | The | formulas | are | given | by  |     |     |     |     |     |
| ----- | ------------- | --- | --- | -------- | --- | ----- | --- | --- | --- | --- | --- | --- |
(cid:118)
|     |     |      |     | (cid:117)   |                                  | 24 N | 4 (cid:32)        |          |           | M         | (cid:33)2                |      |
| --- | --- | ---- | --- | ----------- | -------------------------------- | ---- | ----------------- | -------- | --------- | --------- | ------------------------ | ---- |
|     |     |      |     | (cid:117)   | 1 (cid:88)(cid:88)(cid:88)       |      |                   |          | 1         | (cid:88)  |                          |      |
|     |     |      |     |             |                                  |      |                   | P∗       |           | ∗,m       |                          |      |
|     |     | RMSE |     | = (cid:116) |                                  |      |                   |          |           | P(cid:98) | ,                        | (44) |
|     |     |      |     | 24          | 5N                               |      |                   | 0,i,d,h− | M         | 0,i,d,h   |                          |      |
|     |     |      |     |             | · h=1d=1                         |      | i=0               |          | m=1       |           |                          |      |
|     |     |      |     |             | 24                               | N    | 4                 |          |           |           |                          |      |
|     |     |      |     | 1           | (cid:88)(cid:88)(cid:88)(cid:12) |      |                   |          |           | (cid:16)  | (cid:17)(cid:12)         |      |
|     |     |      | MAE | =           |                                  |      | (cid:12) P ∗      |          | med       |           | P(cid:98) ∗ , m (cid:12) | (45) |
|     |     |      |     |             |                                  |      | (cid:12) 0 ,i,d,h |          | m=1,...,M |           | (cid:12)                 |      |
|     |     |      |     | 24          | 5N                               |      |                   | −        |           |           | 0 , i ,d,h               |      |
|     |     |      |     | ·           | h=1d=1                           | i=0  |                   |          |           |           |                          |      |
|     |     |      |     |             |                                  |      |                   |          |           | (cid:16)  | (cid:17)                 |      |
|     | ∗   | , m  |     |             |                                  |      | ∗                 |          |           |           | ∗ , m                    |      |
where P(cid:98) is the m-th simulation of P and med m=1,...,M P(cid:98) is the median
|     | 0   | , i ,d,h |     |     |     |     | 0 ,i,d,h |     |     |     | 0 , i ,d,h |     |
| --- | --- | -------- | --- | --- | --- | --- | -------- | --- | --- | --- | ---------- | --- |
∗,m
| of M | simulated |     | P(cid:98) | prices. |     |     |     |     |     |     |     |     |
| ---- | --------- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
0,i,d,h
|     | We approximate |     |     | the CRPS | using | the | pinball | loss |     |     |     |     |
| --- | -------------- | --- | --- | -------- | ----- | --- | ------- | ---- | --- | --- | --- | --- |
1
(cid:88)
|     |     |     |     |     | CRPS |       | =   | PBτ |       |     |     | (46) |
| --- | --- | --- | --- | --- | ---- | ----- | --- | --- | ----- | --- | --- | ---- |
|     |     |     |     |     |      | i,d,h | R   |     | i,d,h |     |     |      |
τ∈r
for a dense equidistant grid of probabilities r between 0 and 1 of size R, see e.g. [37]. In
this study, we consider r = 0.01,0.02,...,0.99 of size R = 99. PBτ is the pinball loss
i,d,h
|      |         |          |             |            | {              |            |              | }                |          |           |                           |      |
| ---- | ------- | -------- | ----------- | ---------- | -------------- | ---------- | ------------ | ---------------- | -------- | --------- | ------------------------- | ---- |
| with | respect | to       | probability |            | τ. Its formula |            | is given     | by               |          |           |                           |      |
|      |         | (cid:16) |             |            |                |            |              | (cid:17)(cid:16) |          |           | (cid:16) (cid:17)(cid:17) |      |
|      | PBτ     |          | 1           |            |                |            |              | ∗                |          | Qτ        | ∗ , m                     |      |
|      |         | =        | τ           |            |                | (P(cid:98) | ∗ , m )      | P                |          |           | P(cid:98)                 | (47) |
|      | i,d,h   |          | −           | P ∗        | <Qτ            |            |              | 0                | ,i,d,h − | m=1,...,M | 0 , i ,d,h                |      |
|      |         |          |             | { 0 ,i,d,h | m=1,...,M      |            | 0 , i ,d,h } |                  |          |           |                           |      |
|      |         |          | (cid:16)    | (cid:17)   |                |            |              |                  |          |           |                           |      |
where Qτ P(cid:98) ∗,m is the τ-th quantile of M simulated P(cid:98) ∗,m prices. To calculate
|     | m=1,...,M |      | 0,i,d,h |      |              |     |                          |     |      | 0,i,d,h |     |      |
| --- | --------- | ---- | ------- | ---- | ------------ | --- | ------------------------ | --- | ---- | ------- | --- | ---- |
| the | overall   | CRPS | value   | we   | use a simple |     | average                  |     |      |         |     |      |
|     |           |      |         |      |              |     | 24                       | N 4 |      |         |     |      |
|     |           |      |         |      |              | 1   | (cid:88)(cid:88)(cid:88) |     |      |         |     |      |
|     |           |      |         | CRPS | =            |     |                          |     | CRPS | i,d,h . |     | (48) |
24 5N
|     |     |     |     |     |     | ·   | h=1d=1 | i=0 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
Table 4 shows the error measures of the two considered price models based on the
whole out-of-sample data. Let us recall that the out-of-sample consists of 3 years of data
(years 2018 to 2020). We observe a huge difference in the performance of the two models.
The expert model reports lower errors, but is slightly more biased. Its performance is
naturally not a surprise and is inline with the EPF literature [36, 40, 42–45]. Let us note
that the forecasts could be easily improved using a higher number of regressors or more
sophisticated estimation methods both for the point and probabilistic models.
|     |     |     |       |          |          | MAE   | RMSE   | CRPS       |      | bias         |     |     |
| --- | --- | --- | ----- | -------- | -------- | ----- | ------ | ---------- | ---- | ------------ | --- | --- |
|     |     |     |       | naive    |          | 10.73 | 16.64  |            | 4.17 | 0.08         |     |     |
|     |     |     |       | expert   |          | 6.00  | 8.68   |            | 2.22 | 0.22         |     |     |
|     |     |     | Table | 4: Error | measures |       | of the | considered |      | price models |     |     |
37

Appendix C
Supply/Sell(thehigherthepricethebetter) Demand/Buy(thelowerthepricethebetter)
ledoM 1 10 100 1000 1%of 5%of 1%of 5%of 1 10 100 1000 1%of 5%of
Strategy
MW MW MW MW wind wind solar solar MW MW MW MW load load
IA-only 37.20 36.87 33.68 -61.20 21.78 -214.07 26.69 -84.74 37.49 37.84 40.94 117.18 66.31 1055.64
TC-min 37.43 37.34 36.78 32.55 29.73 25.48 32.69 29.38 37.57 37.67 38.23 42.82 42.13 63.10
evian
E-NoImp 37.46 37.25 35.41 -13.95 26.21 -85.85 30.30 -24.90 37.39 37.62 39.45 79.09 53.30 558.32
E-LinImp 37.46 37.28 36.59 32.29 29.51 24.46 32.52 29.12 37.39 37.60 38.37 42.98 42.29 66.25
E-LinImpMeff 37.43 37.33 36.73 32.24 29.68 24.94 32.58 29.02 37.57 37.67 38.24 43.00 42.22 68.91
E-Meff 37.42 37.31 36.78 32.68 29.76 25.63 32.67 29.43 37.56 37.64 38.20 42.59 42.01 61.20
E 37.46 37.31 36.69 32.65 29.66 25.58 32.63 29.41 37.39 37.58 38.26 42.62 42.04 61.25
E-Var-U 37.37 37.20 36.49 32.46 29.48 25.45 32.41 29.24 37.53 37.66 38.55 101.01 58.61 362.07
VaR 37.44 37.29 36.65 32.45 29.62 25.42 32.54 29.21 37.44 37.61 38.32 42.89 42.20 62.85
CVaR 37.43 37.27 36.65 32.55 29.64 25.52 32.57 29.32 37.41 37.61 38.34 42.89 42.19 63.86
trepxe
E-NoImp 37.50 37.29 35.47 -10.24 25.88 -107.88 31.30 2.68 37.35 37.57 39.37 76.70 51.83 517.79
E-LinImp 37.50 37.32 36.67 32.37 29.62 25.12 32.64 29.25 37.35 37.53 38.27 42.91 42.22 68.17
E-LinImpMeff 37.43 37.34 36.73 32.27 29.71 25.09 32.57 29.03 37.57 37.67 38.24 43.03 42.23 71.24
E-Meff 37.43 37.33 36.79 32.72 29.77 25.67 32.67 29.43 37.57 37.66 38.20 42.55 41.99 60.91
E 37.50 37.34 36.73 32.70 29.70 25.63 32.67 29.42 37.35 37.51 38.22 42.58 42.03 60.94
E-Var-U 37.45 37.32 36.69 32.52 29.68 25.46 32.56 29.22 37.40 37.57 38.32 60.66 45.93 230.18
VaR 37.46 37.33 36.71 32.53 29.67 25.47 32.61 29.24 37.42 37.58 38.24 42.75 42.12 62.17
CVaR 37.46 37.32 36.71 32.59 29.69 25.55 32.62 29.33 37.41 37.56 38.22 42.73 42.09 61.99
perfectforecast 38.42 38.23 37.30 33.01 30.31 26.04 33.16 29.81 36.43 36.64 37.61 42.24 41.68 59.39
Table5: AverageactualgainG(cid:101) (EUR/MWh)oftheconsideredstrategiesasanewmarket
player with an oracle forecast of intersection curves. Colour indicates the performance
row-wise (the greener, the better). With bold, we depicted the best values in each row.
38

Supply/Sell(thehigherthepricethebetter) Demand/Buy(thelowerthepricethebetter)
ledoM 1 10 100 1000 1%of 5%of 1%of 5%of 1 10 100 1000 1%of 5%of
Strategy
MW MW MW MW wind wind solar solar MW MW MW MW load load
IA-only 37.22 37.01 34.55 -37.59 23.69 -151.61 28.13 -52.56 37.47 37.70 40.08 100.42 59.55 989.44
TC-min 37.45 37.45 37.45 37.45 30.98 30.98 33.65 33.66 37.55 37.55 37.55 37.55 38.98 38.97
evian
E-NoImp 37.48 37.37 36.13 0.12 27.50 -67.09 31.19 -17.62 37.37 37.49 38.72 68.95 49.55 647.03
E-LinImp 37.48 37.40 37.33 37.53 30.84 30.28 33.52 33.63 37.37 37.47 37.61 37.34 38.89 38.53
E-LinImpMeff 37.45 37.45 37.51 37.65 31.09 30.89 33.68 33.73 37.55 37.54 37.45 37.26 38.75 38.61
E-Meff 37.44 37.43 37.50 37.89 31.08 31.39 33.70 33.90 37.54 37.52 37.47 37.10 38.67 38.06
E 37.48 37.43 37.42 37.85 30.97 31.32 33.64 33.87 37.37 37.46 37.51 37.12 38.70 38.07
E-Var-U 37.38 37.34 37.31 37.70 30.92 31.28 33.51 33.76 37.51 37.54 37.87 88.43 53.17 331.24
VaR 37.46 37.42 37.41 37.64 30.97 31.20 33.60 33.69 37.42 37.48 37.54 37.34 38.83 38.65
CVaR 37.45 37.41 37.43 37.78 31.01 31.32 33.63 33.83 37.39 37.47 37.54 37.28 38.75 38.98
trepxe
E-NoImp 37.52 37.41 36.17 1.84 27.17 -87.07 31.95 -8.77 37.33 37.45 38.65 67.48 48.61 671.17
E-LinImp 37.52 37.45 37.41 37.61 30.96 31.15 33.63 33.75 37.33 37.40 37.51 37.30 38.80 39.30
E-LinImpMeff 37.45 37.46 37.52 37.62 31.12 31.24 33.67 33.78 37.55 37.55 37.45 37.30 38.74 39.92
E-Meff 37.45 37.45 37.51 37.93 31.09 31.4 33.70 33.91 37.55 37.54 37.48 37.08 38.67 37.97
E 37.52 37.46 37.45 37.89 31.03 31.37 33.67 33.88 37.33 37.39 37.48 37.10 38.68 37.96
E-Var-U 37.47 37.45 37.48 37.79 31.08 31.28 33.65 33.80 37.38 37.45 37.63 51.50 41.93 176.09
VaR 37.47 37.45 37.47 37.69 31.03 31.21 33.64 33.72 37.41 37.46 37.47 37.26 38.78 38.42
CVaR 37.48 37.45 37.48 37.78 31.07 31.31 33.67 33.82 37.39 37.43 37.44 37.20 38.72 38.27
perfectforecast 38.44 38.35 38.09 38.29 31.73 31.87 34.23 34.33 36.41 36.50 36.81 36.69 38.26 37.40
Table 6: Average actual gain G(cid:101) (EUR/MWh) of the considered strategies as an existing
market player rebidding their portfolio v with an oracle forecast of intersection curves.
Colour indicates the performance row-wise (the greener, the better). With bold, we de-
picted the best values in each row.
39

|                    | IA-only        |     |     | 10% | IA-only            |       |     | 10% |
| ------------------ | -------------- | --- | --- | --- | ------------------ | ----- | --- | --- |
|                    | TC-min         |     |     |     | TC-min             |       |     |     |
|                    | E-NoImp        |     |     | 9%  | E-NoImp            |       |     | 9%  |
|                    | E-LinImp       |     |     | 8%  | E-LinImp           |       |     | 8%  |
| evian E-LinImpMeff |                |     |     |     | evian E-LinImpMeff |       |     |     |
|                    | E-Meff         |     |     | 7%  | E-Meff             |       |     | 7%  |
|                    | E              |     |     |     |                    | E     |     |     |
|                    | E-Var-U        |     |     | 6%  | E-Var-U            |       |     | 6%  |
|                    | VaR            |     |     |     |                    | VaR   |     |     |
|                    | CVaR           |     |     | 5%  | CVaR               |       |     | 5%  |
|                    | E - N oI m p   |     |     | 4%  | E - N oI           | m p   |     | 4%  |
| trepxe             | E - L in I m p |     |     |     | trepxe E - L in    | I m p |     |     |
| E-LinImpMeff       |                |     |     | 3%  | E-LinImpMeff       |       |     | 3%  |
|                    | E-Meff         |     |     |     | E-Meff             |       |     |     |
|                    | E              |     |     | 2%  |                    | E     |     | 2%  |
|                    | E-Var-U        |     |     |     | E-Var-U            |       |     |     |
|                    |                |     |     | 1%  |                    |       |     | 1%  |
|                    | VaR            |     |     |     |                    | VaR   |     |     |
|                    | CVaR           |     |     |     | CVaR               |       |     |     |
n ly m in m p m p Me ff Meff E ar-U Va R a R m p m p Me ff Meff E ar-U Va R VaR 0% n ly m in m p m p Me ff Meff E ar-U Va R a R m p m p Me ff Meff E ar-U Va R VaR 0 %
IA-o C - -N o I i n I p - E-V C V N o I i n I p - E-V C p-value IA-o C - -N o I i n I p - E-V C V N o I i n I p - E-V C p-va lu e
|                     | T E E - L n I m E | E - E - L n I | m E    |     |                       | T E E - L n I m E | E - E - L n I m E |     |
| ------------------- | ----------------- | ------------- | ------ | --- | --------------------- | ----------------- | ----------------- | --- |
|                     | L i               | L i           |        |     |                       | L i               | L i               |     |
|                     | E -               | E -           |        |     |                       | E -               | E -               |     |
|                     | naive             | expert        |        |     |                       | naive             | expert            |     |
|                     | (a) v             | =1 MW         | (sell) |     |                       | (b) v =1000       | MW (sell)         |     |
|                     |                   |               |        | 10% |                       |                   |                   | 10% |
|                     | IA-only           |               |        |     | IA-only               |                   |                   |     |
|                     | TC-min            |               |        | 9%  | TC-min                |                   |                   | 9%  |
|                     | E-NoImp           |               |        |     | E-NoImp               |                   |                   |     |
|                     | E-LinImp          |               |        |     | E-LinImp              |                   |                   |     |
| E-LinImpMeff        |                   |               |        | 8%  | E-LinImpMeff          |                   |                   | 8%  |
| evian               | E-Meff            |               |        |     | evian E-Meff          |                   |                   |     |
|                     |                   |               |        | 7%  |                       |                   |                   | 7%  |
|                     | E                 |               |        |     |                       | E                 |                   |     |
|                     | E-Var-U           |               |        | 6%  | E-Var-U               |                   |                   | 6%  |
|                     | VaR               |               |        |     |                       | VaR               |                   |     |
|                     | CVaR              |               |        | 5%  | CVaR                  |                   |                   | 5%  |
|                     | E - N oI m p      |               |        |     | E - N oI              | m p               |                   |     |
|                     | - L in I m p      |               |        | 4%  | - L in                | I m p             |                   | 4%  |
| trepxe E-LinImpMeff | E                 |               |        |     | trepxe E-LinImpMeff E |                   |                   |     |
|                     |                   |               |        | 3%  |                       |                   |                   | 3%  |
|                     | E-Meff            |               |        |     | E-Meff                |                   |                   |     |
|                     | E                 |               |        | 2%  |                       | E                 |                   | 2%  |
|                     | E-Var-U           |               |        |     | E-Var-U               |                   |                   |     |
|                     | VaR               |               |        | 1%  |                       | VaR               |                   | 1%  |
|                     | CVaR              |               |        |     | CVaR                  |                   |                   |     |
ly in p p ff Meff E ar-U R R p p ff Meff E ar-U R VaR 0% ly in p p ff Meff E ar-U R R p p ff Meff E ar-U R VaR 0 %
IA-o n - m I m I m Me Va V a I m I m Me Va p-value IA-o n - m I m I m Me Va V a I m I m Me Va p-va lu e
T C -N o L i n m p E - E-V C - N o L i n m p E - E-V C T C -N o L i n m p E - E-V C - N o L i n m p E - E-V C
|                     | E E - i n I    | E E - i n I |      |     |                     | E E - i n I | E E - i n I  |     |
| ------------------- | -------------- | ----------- | ---- | --- | ------------------- | ----------- | ------------ | --- |
|                     | E - L          | E - L       |      |     |                     | E - L       | E - L        |     |
|                     | naive          | expert      |      |     |                     | naive       | expert       |     |
|                     | (c) v          | =5% of      | wind |     |                     | (d) v       | =1% of solar |     |
|                     | IA-only        |             |      | 10% | IA-only             |             |              | 10% |
|                     | TC-min         |             |      |     | TC-min              |             |              |     |
|                     | E-NoImp        |             |      | 9%  | E-NoImp             |             |              | 9%  |
|                     | E-LinImp       |             |      | 8%  | E-LinImp            |             |              | 8%  |
| evian E-LinImpMeff  |                |             |      |     | evian E-LinImpMeff  |             |              |     |
|                     | E-Meff         |             |      | 7%  | E-Meff              |             |              | 7%  |
|                     | E              |             |      |     |                     | E           |              |     |
|                     | E-Var-U        |             |      | 6%  | E-Var-U             |             |              | 6%  |
|                     | VaR            |             |      |     |                     | VaR         |              |     |
|                     |                |             |      | 5%  |                     |             |              | 5%  |
|                     | CVaR           |             |      |     | CVaR                |             |              |     |
|                     | E - N oI m p   |             |      | 4%  | E - N oI            | m p         |              | 4%  |
|                     | E - L in I m p |             |      |     | E - L in            | I m p       |              |     |
| trepxe E-LinImpMeff |                |             |      | 3%  | trepxe E-LinImpMeff |             |              | 3%  |
|                     | E-Meff         |             |      |     | E-Meff              |             |              |     |
|                     | E-Var-U E      |             |      | 2%  | E-Var-U             | E           |              | 2%  |
|                     | VaR            |             |      | 1%  |                     | VaR         |              | 1%  |
|                     | CVaR           |             |      |     | CVaR                |             |              |     |
n ly m in m p m p Me ff Meff E ar-U Va R a R m p m p Me ff Meff E ar-U Va R VaR 0% n ly m in m p m p Me ff Meff E ar-U Va R a R m p m p Me ff Meff E ar-U Va R VaR 0 %
IA-o C - -N o I n I p - E-V C V N o I n I p - E-V C p-value IA-o C - -N o I n I p - E-V C V N o I n I p - E-V C p-va lu e
|     | T E - L i I m E | E - - L i I | m E   |     |     | T E - L i I m E | E - - L i I m E |     |
| --- | --------------- | ----------- | ----- | --- | --- | --------------- | --------------- | --- |
|     | E L i n         | E L i n     |       |     |     | E L i n         | E L i n         |     |
|     | E -             | E -         |       |     |     | E -             | E -             |     |
|     | naive           | expert      |       |     |     | naive           | expert          |     |
|     | (e) v =1000     | MW          | (buy) |     |     | (f) v           | =1% of load     |     |
Figure 12: Results of the G(cid:101) mean inequality test for remaining portfolios v in the setting
of a new market player. The plots present p-values — the closer they are to zero ( dark
→
green), the more significant the difference is between gains of X-axis strategy (better) and
| gains | of the Y-axis | strategy | (worse). |     |     |     |     |     |
| ----- | ------------- | -------- | -------- | --- | --- | --- | --- | --- |
40

|        | IA-only      |        |     |     |     | 10% |                     | IA-only        |     |     | 10% |
| ------ | ------------ | ------ | --- | --- | --- | --- | ------------------- | -------------- | --- | --- | --- |
|        | TC-min       |        |     |     |     |     |                     | TC-min         |     |     |     |
|        |              |        |     |     |     | 9%  |                     |                |     |     | 9%  |
|        | E-NoImp      |        |     |     |     |     |                     | E-NoImp        |     |     |     |
|        | E-LinImp     |        |     |     |     | 8%  |                     | E-LinImp       |     |     | 8%  |
| evian  | E-LinImpMeff |        |     |     |     |     | evian E-LinImpMeff  |                |     |     |     |
|        | E-Meff       |        |     |     |     | 7%  |                     | E-Meff         |     |     | 7%  |
|        |              | E      |     |     |     |     |                     | E              |     |     |     |
|        | E-Var-U      |        |     |     |     | 6%  |                     | E-Var-U        |     |     | 6%  |
|        |              | VaR    |     |     |     |     |                     | VaR            |     |     |     |
|        |              |        |     |     |     | 5%  |                     |                |     |     | 5%  |
|        | CVaR         |        |     |     |     |     |                     | CVaR           |     |     |     |
|        | E - N        | oI m p |     |     |     | 4%  |                     | E - N oI m p   |     |     | 4%  |
|        | E - L in     | I m p  |     |     |     |     |                     | E - L in I m p |     |     |     |
| trepxe | E-LinImpMeff |        |     |     |     | 3%  | trepxe E-LinImpMeff |                |     |     | 3%  |
|        | E-Meff       |        |     |     |     |     |                     | E-Meff         |     |     |     |
|        |              | E      |     |     |     | 2%  |                     | E              |     |     | 2%  |
|        | E-Var-U      |        |     |     |     |     |                     | E-Var-U        |     |     |     |
|        |              | VaR    |     |     |     | 1%  |                     | VaR            |     |     | 1%  |
|        | CVaR         |        |     |     |     |     |                     | CVaR           |     |     |     |
n ly m in m p m p Me ff Meff E ar-U Va R a R m p m p Me ff Meff E ar-U Va R VaR 0% n ly m in m p m p Me ff Meff E ar-U Va R a R m p m p Me ff Meff E ar-U Va R VaR 0 %
IA-o C - o I n I p - E-V C V o I n I p - E-V C p-value IA-o C - o I n I p - E-V C V o I n I p - E-V C p-va lu e
|        |              | T E -N - L i I m | E     | E - N - L i I m | E      |     |              | T E -N - L i   | I m E  | E - N - L i I m E |     |
| ------ | ------------ | ---------------- | ----- | --------------- | ------ | --- | ------------ | -------------- | ------ | ----------------- | --- |
|        |              | E L i n          |       | E L i n         |        |     |              | E L i          | n      | E L i n           |     |
|        |              | E -              |       | E -             |        |     |              | E -            |        | E -               |     |
|        |              | naive            |       | expert          |        |     |              | naive          |        | expert            |     |
|        |              | (a)              | v =10 | MW              | (sell) |     |              | (b)            | v =100 | MW (sell)         |     |
|        | IA-only      |                  |       |                 |        | 10% |              | IA-only        |        |                   | 10% |
|        | TC-min       |                  |       |                 |        |     |              | TC-min         |        |                   |     |
|        | E-NoImp      |                  |       |                 |        | 9%  |              | E-NoImp        |        |                   | 9%  |
|        | E-LinImp     |                  |       |                 |        |     |              | E-LinImp       |        |                   |     |
|        | E-LinImpMeff |                  |       |                 |        | 8%  | E-LinImpMeff |                |        |                   | 8%  |
| evian  |              |                  |       |                 |        |     | evian        |                |        |                   |     |
|        | E-Meff       |                  |       |                 |        | 7%  |              | E-Meff         |        |                   | 7%  |
|        |              | E                |       |                 |        |     |              | E              |        |                   |     |
|        | E-Var-U      |                  |       |                 |        | 6%  |              | E-Var-U        |        |                   | 6%  |
|        |              | VaR              |       |                 |        |     |              | VaR            |        |                   |     |
|        | CVaR         |                  |       |                 |        | 5%  |              | CVaR           |        |                   | 5%  |
|        | - N          | oI m p           |       |                 |        |     |              | - N oI m p     |        |                   |     |
|        | E - L in     | I m p            |       |                 |        | 4%  |              | E - L in I m p |        |                   | 4%  |
| trepxe | E            |                  |       |                 |        |     | trepxe       | E              |        |                   |     |
|        | E-LinImpMeff |                  |       |                 |        | 3%  | E-LinImpMeff |                |        |                   | 3%  |
|        | E-Meff       |                  |       |                 |        |     |              | E-Meff         |        |                   |     |
|        |              | E                |       |                 |        | 2%  |              | E              |        |                   | 2%  |
|        | E-Var-U      |                  |       |                 |        |     |              | E-Var-U        |        |                   |     |
|        |              | VaR              |       |                 |        | 1%  |              | VaR            |        |                   | 1%  |
|        | CVaR         |                  |       |                 |        |     |              | CVaR           |        |                   |     |
ly in p p ff Meff ar-U R R p p ff Meff ar-U R VaR 0% ly in p p ff Meff ar-U R R p p ff Meff ar-U R VaR 0 %
IA-o n m I m I m Me E Va V a I m I m Me E Va p-value IA-o n m I m I m Me E Va V a I m I m Me E Va p-va lu e
T C - -N o L i n m p E - E-V C N o L i n m p E - E-V C T C - -N o L i n m p E - E-V C N o L i n m p E - E-V C
|        |              | E E - n I |       | E - E - n I |       |     |                     | E E -          | n I    | E - E - n I |     |
| ------ | ------------ | --------- | ----- | ----------- | ----- | --- | ------------------- | -------------- | ------ | ----------- | --- |
|        |              | - L i     |       | - L i       |       |     |                     | - L i          |        | - L i       |     |
|        |              | E         |       | E           |       |     |                     | E              |        | E           |     |
|        |              | naive     |       | expert      |       |     |                     | naive          |        | expert      |     |
|        |              | (c)       | v =10 | MW          | (buy) |     |                     | (d)            | v =100 | MW (buy)    |     |
|        | IA-only      |           |       |             |       | 10% |                     | IA-only        |        |             | 10% |
|        | TC-min       |           |       |             |       | 9%  |                     | TC-min         |        |             | 9%  |
|        | E-NoImp      |           |       |             |       |     |                     | E-NoImp        |        |             |     |
|        | E-LinImp     |           |       |             |       | 8%  |                     | E-LinImp       |        |             | 8%  |
|        | E-LinImpMeff |           |       |             |       |     | E-LinImpMeff        |                |        |             |     |
| evian  | E-Meff       |           |       |             |       | 7%  | evian               | E-Meff         |        |             | 7%  |
|        | E-Var-U      | E         |       |             |       | 6%  |                     | E-Var-U E      |        |             | 6%  |
|        |              | VaR       |       |             |       | 5%  |                     | VaR            |        |             | 5%  |
|        | CVaR         |           |       |             |       |     |                     | CVaR           |        |             |     |
|        | E - N        | oI m p    |       |             |       |     |                     | E - N oI m p   |        |             |     |
|        | E - L in     | I m p     |       |             |       | 4%  |                     | E - L in I m p |        |             | 4%  |
| trepxe | E-LinImpMeff |           |       |             |       |     | trepxe E-LinImpMeff |                |        |             |     |
|        | E-Meff       |           |       |             |       | 3%  |                     | E-Meff         |        |             | 3%  |
|        |              | E         |       |             |       | 2%  |                     | E              |        |             | 2%  |
|        | E-Var-U      |           |       |             |       |     |                     | E-Var-U        |        |             |     |
|        |              | VaR       |       |             |       | 1%  |                     | VaR            |        |             | 1%  |
|        | CVaR         |           |       |             |       |     |                     | CVaR           |        |             |     |
ly in m p m p Me ff Meff E ar-U Va R a R m p m p Me ff Meff E ar-U Va R VaR 0% ly in m p m p Me ff Meff E ar-U Va R a R m p m p Me ff Meff E ar-U Va R VaR 0 %
IA-o n C - m o I n I p - C V o I n I p - C p-value IA-o n C - m o I n I p - C V o I n I p - C p-va lu e
T -N - L i I m E E-V - N - L i I m E E-V T -N - L i I m E E-V - N - L i I m E E-V
|        |              | E E L i n |       | E E L i n |      |     |                    | E E L i        | n     | E E L i n |     |
| ------ | ------------ | --------- | ----- | --------- | ---- | --- | ------------------ | -------------- | ----- | --------- | --- |
|        |              | E -       |       | E -       |      |     |                    | E -            |       | E -       |     |
|        |              | naive     |       | expert    |      |     |                    | naive          |       | expert    |     |
|        |              | (e)       | v =1% | of        | wind |     |                    | (f)            | v =5% | of solar  |     |
|        | IA-only      |           |       |           |      | 10% |                    | IA-only        |       |           | 10% |
|        | TC-min       |           |       |           |      |     |                    | TC-min         |       |           |     |
|        | E-NoImp      |           |       |           |      | 9%  |                    | E-NoImp        |       |           | 9%  |
|        | E-LinImp     |           |       |           |      |     |                    | E-LinImp       |       |           |     |
|        |              |           |       |           |      | 8%  |                    |                |       |           | 8%  |
| evian  | E-LinImpMeff |           |       |           |      |     | evian E-LinImpMeff |                |       |           |     |
|        | E-Meff       |           |       |           |      | 7%  |                    | E-Meff         |       |           | 7%  |
|        |              | E         |       |           |      |     |                    | E              |       |           |     |
|        | E-Var-U      |           |       |           |      | 6%  |                    | E-Var-U        |       |           | 6%  |
|        |              | VaR       |       |           |      |     |                    | VaR            |       |           |     |
|        | CVaR         |           |       |           |      | 5%  |                    | CVaR           |       |           | 5%  |
|        | - N          | oI m p    |       |           |      |     |                    | - N oI m p     |       |           |     |
|        | E            |           |       |           |      | 4%  |                    | E              |       |           | 4%  |
| trepxe | E - L in     | I m p     |       |           |      |     | trepxe             | E - L in I m p |       |           |     |
|        | E-LinImpMeff |           |       |           |      | 3%  | E-LinImpMeff       |                |       |           | 3%  |
|        | E-Meff       |           |       |           |      |     |                    | E-Meff         |       |           |     |
|        |              | E         |       |           |      | 2%  |                    | E              |       |           | 2%  |
|        | E-Var-U      |           |       |           |      |     |                    | E-Var-U        |       |           |     |
|        |              | VaR       |       |           |      | 1%  |                    | VaR            |       |           | 1%  |
|        | CVaR         |           |       |           |      |     |                    | CVaR           |       |           |     |
ly in p p ff Meff ar-U R R p p ff Meff ar-U R VaR 0% ly in p p ff Meff ar-U R R p p ff Meff ar-U R VaR 0 %
n m m m Me E Va V a m m Me E Va n m m m Me E Va V a m m Me E Va
IA-o C - -N o I L i n I m p E - E-V C N o I L i n I m p E - E-V C p-value IA-o C - -N o I L i n I m p E - E-V C N o I L i n I m p E - E-V C p-va lu e
|     |     | T E E - n I |      | E - E - n I |       |     |     | T E E - | n I   | E - E - n I |     |
| --- | --- | ----------- | ---- | ----------- | ----- | --- | --- | ------- | ----- | ----------- | --- |
|     |     | - L i       |      | - L i       |       |     |     | - L i   |       | - L i       |     |
|     |     | E           |      | E           |       |     |     | E       |       | E           |     |
|     |     | naive       |      | expert      |       |     |     | naive   |       | expert      |     |
|     |     | (g)         | v =1 | MW          | (buy) |     |     | (h)     | v =5% | of load     |     |
Figure 13: Results of the G(cid:101) mean inequality test for remaining portfolios v in the setting
| of  | a new | market | player. |     | For details | on interpretation |     | see Figure | 12. |     |     |
| --- | ----- | ------ | ------- | --- | ----------- | ----------------- | --- | ---------- | --- | --- | --- |
41

|                     | IA-only      |     | 10% | IA-only             |       |     | 10% |
| ------------------- | ------------ | --- | --- | ------------------- | ----- | --- | --- |
|                     | TC-min       |     |     | TC-min              |       |     |     |
|                     |              |     | 9%  |                     |       |     | 9%  |
|                     | E-NoImp      |     |     | E-NoImp             |       |     |     |
| E-LinImp            |              |     | 8%  | E-LinImp            |       |     | 8%  |
| evian E-LinImpMeff  |              |     |     | evian E-LinImpMeff  |       |     |     |
|                     | E-Meff       |     | 7%  | E-Meff              |       |     | 7%  |
|                     | E            |     |     |                     | E     |     |     |
|                     | E-Var-U      |     | 6%  | E-Var-U             |       |     | 6%  |
|                     | VaR          |     |     |                     | VaR   |     |     |
|                     |              |     | 5%  |                     |       |     | 5%  |
|                     | CVaR         |     |     | CVaR                |       |     |     |
|                     | E - N oI m p |     | 4%  | E - N oI            | m p   |     | 4%  |
| E                   | - L in I m p |     |     | E - L in            | I m p |     |     |
| trepxe E-LinImpMeff |              |     | 3%  | trepxe E-LinImpMeff |       |     | 3%  |
|                     | E-Meff       |     |     | E-Meff              |       |     |     |
|                     | E            |     | 2%  |                     | E     |     | 2%  |
|                     | E-Var-U      |     |     | E-Var-U             |       |     |     |
|                     | VaR          |     | 1%  |                     | VaR   |     | 1%  |
|                     | CVaR         |     |     | CVaR                |       |     |     |
n ly m in m p m p Me ff Meff E ar-U Va R a R m p m p Me ff Meff E ar-U Va R VaR 0% n ly m in m p m p Me ff Meff E ar-U Va R a R m p m p Me ff Meff E ar-U Va R VaR 0 %
IA-o C - o I n I p - E-V C V o I n I p - E-V C p-value IA-o C - o I n I p - E-V C V o I n I p - E-V C p-va lu e
|              | T E -N - L i I m E | E - N - L i I m E |     |              | T E -N - L i I m E | E - N - L i I m E |     |
| ------------ | ------------------ | ----------------- | --- | ------------ | ------------------ | ----------------- | --- |
|              | E L i n            | E L i n           |     |              | E L i n            | E L i n           |     |
|              | E -                | E -               |     |              | E -                | E -               |     |
|              | naive              | expert            |     |              | naive              | expert            |     |
|              | (a) v =10          | MW (sell)         |     |              | (b) v =100         | MW (sell)         |     |
|              | IA-only            |                   | 10% | IA-only      |                    |                   | 10% |
|              | TC-min             |                   |     | TC-min       |                    |                   |     |
|              | E-NoImp            |                   | 9%  | E-NoImp      |                    |                   | 9%  |
| E-LinImp     |                    |                   |     | E-LinImp     |                    |                   |     |
| E-LinImpMeff |                    |                   | 8%  | E-LinImpMeff |                    |                   | 8%  |
| evian        |                    |                   |     | evian        |                    |                   |     |
|              | E-Meff             |                   | 7%  | E-Meff       |                    |                   | 7%  |
|              | E                  |                   |     |              | E                  |                   |     |
|              | E-Var-U            |                   | 6%  | E-Var-U      |                    |                   | 6%  |
|              | VaR                |                   |     |              | VaR                |                   |     |
|              | CVaR               |                   | 5%  | CVaR         |                    |                   | 5%  |
|              | - N oI m p         |                   |     | - N oI       | m p                |                   |     |
|              | E - L in I m p     |                   | 4%  | E - L in     | I m p              |                   | 4%  |
| trepxe E     |                    |                   |     | trepxe E     |                    |                   |     |
| E-LinImpMeff |                    |                   | 3%  | E-LinImpMeff |                    |                   | 3%  |
|              | E-Meff             |                   |     | E-Meff       |                    |                   |     |
|              | E                  |                   | 2%  |              | E                  |                   | 2%  |
|              | E-Var-U            |                   |     | E-Var-U      |                    |                   |     |
|              | VaR                |                   | 1%  |              | VaR                |                   | 1%  |
|              | CVaR               |                   |     | CVaR         |                    |                   |     |
ly in p p ff Meff ar-U R R p p ff Meff ar-U R VaR 0% ly in p p ff Meff ar-U R R p p ff Meff ar-U R VaR 0 %
IA-o n m I m I m Me E Va V a I m I m Me E Va p-value IA-o n m I m I m Me E Va V a I m I m Me E Va p-va lu e
T C - -N o L i n m p E - E-V C N o L i n m p E - E-V C T C - -N o L i n m p E - E-V C N o L i n m p E - E-V C
|                     | E E - n I    | E - E - n I |     |                     | E E - n I  | E - E - n I |     |
| ------------------- | ------------ | ----------- | --- | ------------------- | ---------- | ----------- | --- |
|                     | - L i        | - L i       |     |                     | - L i      | - L i       |     |
|                     | E            | E           |     |                     | E          | E           |     |
|                     | naive        | expert      |     |                     | naive      | expert      |     |
|                     | (c) v =10    | MW (buy)    |     |                     | (d) v =100 | MW (buy)    |     |
|                     | IA-only      |             | 10% | IA-only             |            |             | 10% |
|                     | TC-min       |             | 9%  | TC-min              |            |             | 9%  |
|                     | E-NoImp      |             |     | E-NoImp             |            |             |     |
| E-LinImp            |              |             | 8%  | E-LinImp            |            |             | 8%  |
| E-LinImpMeff        |              |             |     | E-LinImpMeff        |            |             |     |
| evian               | E-Meff       |             | 7%  | evian E-Meff        |            |             | 7%  |
|                     | E-Var-U E    |             | 6%  | E-Var-U             | E          |             | 6%  |
|                     | VaR          |             | 5%  |                     | VaR        |             | 5%  |
|                     | CVaR         |             |     | CVaR                |            |             |     |
|                     | E - N oI m p |             |     | E - N oI            | m p        |             |     |
| E                   | - L in I m p |             | 4%  | E - L in            | I m p      |             | 4%  |
| trepxe E-LinImpMeff |              |             |     | trepxe E-LinImpMeff |            |             |     |
|                     | E-Meff       |             | 3%  | E-Meff              |            |             | 3%  |
|                     | E            |             | 2%  |                     | E          |             | 2%  |
|                     | E-Var-U      |             |     | E-Var-U             |            |             |     |
|                     | VaR          |             | 1%  |                     | VaR        |             | 1%  |
|                     | CVaR         |             |     | CVaR                |            |             |     |
ly in m p m p Me ff Meff E ar-U Va R a R m p m p Me ff Meff E ar-U Va R VaR 0% ly in m p m p Me ff Meff E ar-U Va R a R m p m p Me ff Meff E ar-U Va R VaR 0 %
IA-o n C - m o I n I p - C V o I n I p - C p-value IA-o n C - m o I n I p - C V o I n I p - C p-va lu e
T -N - L i I m E E-V - N - L i I m E E-V T -N - L i I m E E-V - N - L i I m E E-V
|                    | E E L i n    | E E L i n   |     |                    | E E L i n | E E L i n    |     |
| ------------------ | ------------ | ----------- | --- | ------------------ | --------- | ------------ | --- |
|                    | E -          | E -         |     |                    | E -       | E -          |     |
|                    | naive        | expert      |     |                    | naive     | expert       |     |
|                    | (e) v        | =1% of wind |     |                    | (f) v     | =5% of solar |     |
|                    | IA-only      |             | 10% | IA-only            |           |              | 10% |
|                    | TC-min       |             |     | TC-min             |           |              |     |
|                    | E-NoImp      |             | 9%  | E-NoImp            |           |              | 9%  |
| E-LinImp           |              |             |     | E-LinImp           |           |              |     |
|                    |              |             | 8%  |                    |           |              | 8%  |
| evian E-LinImpMeff |              |             |     | evian E-LinImpMeff |           |              |     |
|                    | E-Meff       |             | 7%  | E-Meff             |           |              | 7%  |
|                    | E            |             |     |                    | E         |              |     |
|                    | E-Var-U      |             | 6%  | E-Var-U            |           |              | 6%  |
|                    | VaR          |             |     |                    | VaR       |              |     |
|                    | CVaR         |             | 5%  | CVaR               |           |              | 5%  |
|                    | - N oI m p   |             |     | - N oI             | m p       |              |     |
|                    | E            |             | 4%  | E                  |           |              | 4%  |
| trepxe E           | - L in I m p |             |     | trepxe E - L in    | I m p     |              |     |
| E-LinImpMeff       |              |             | 3%  | E-LinImpMeff       |           |              | 3%  |
|                    | E-Meff       |             |     | E-Meff             |           |              |     |
|                    | E            |             | 2%  |                    | E         |              | 2%  |
|                    | E-Var-U      |             |     | E-Var-U            |           |              |     |
|                    | VaR          |             | 1%  |                    | VaR       |              | 1%  |
|                    | CVaR         |             |     | CVaR               |           |              |     |
ly in p p ff Meff ar-U R R p p ff Meff ar-U R VaR 0% ly in p p ff Meff ar-U R R p p ff Meff ar-U R VaR 0 %
n m m m Me E Va V a m m Me E Va n m m m Me E Va V a m m Me E Va
IA-o C - -N o I L i n I m p E - E-V C N o I L i n I m p E - E-V C p-value IA-o C - -N o I L i n I m p E - E-V C N o I L i n I m p E - E-V C p-va lu e
|     | T E E - n I | E - E - n I |     |     | T E E - n I | E - E - n I |     |
| --- | ----------- | ----------- | --- | --- | ----------- | ----------- | --- |
|     | - L i       | - L i       |     |     | - L i       | - L i       |     |
|     | E           | E           |     |     | E           | E           |     |
|     | naive       | expert      |     |     | naive       | expert      |     |
|     | (g) v       | =1 MW (buy) |     |     | (h) v       | =5% of load |     |
Figure 14: Results of the G(cid:101) mean inequality test for remaining portfolios v in the setting
of rebidding the portfolio. For details on interpretation see Figure 12.
42

1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − Tim−e,v=5%ofs−olar − − − −
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − Tim−e,v=1%ofw−ind − − − −
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − Tim−e,v=5%ofl−oad − − − −
0b
IA-only TC-min E E-NoImp E-LinImp E-LinImpMeff E-Meff
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − Tim−e,v=5%ofs−olar − − − −
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − Tim−e,v=1%ofw−ind − − − −
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − Tim−e,v=5%ofl−oad − − − −
0b
IA-only TC-min E E-Var-U VaR CVaR
Figure 15: The average daily weight of b in relation to the whole b strategy for remaining
0
portfolios v in the setting of rebidding the portfolio. The naive-based strategies are
excluded for better clarity
43

1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=1MW(sell)
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=10MW(sell)
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=100MW(sell)
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=1000MW(sell)
0b
IA-only TC-min E E-NoImp E-LinImp E-LinImpMeff E-Meff
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=1MW(sell)
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=10MW(sell)
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=100MW(sell)
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=1000MW(sell)
0b
IA-only TC-min E E-Var-U VaR CVaR
Figure 16: The average daily weight of b in relation to the whole b strategy for remaining
0
portfolios v in the setting of rebidding the portfolio. The naive-based strategies are
excluded for better clarity
44

1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=1MW(buy)
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=10MW(buy)
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=100MW(buy)
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=1000MW(buy)
0b
IA-only TC-min E E-NoImp E-LinImp E-LinImpMeff E-Meff
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=1MW(buy)
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=10MW(buy)
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=100MW(buy)
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=1000MW(buy)
0b
IA-only TC-min E E-Var-U VaR CVaR
Figure 17: The average daily weight of b in relation to the whole b strategy for remaining
0
portfolios v in the setting of rebidding the portfolio. The naive-based strategies are
excluded for better clarity
45

1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − Tim−e,v=1%ofs−olar − − − −
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − Tim−e,v=5%ofw−ind − − − −
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − Tim−e,v=1%ofl−oad − − − −
0b
IA-only TC-min E E-NoImp E-LinImp E-LinImpMeff E-Meff
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − Tim−e,v=1%ofs−olar − − − −
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − Tim−e,v=5%ofw−ind − − − −
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − Tim−e,v=1%ofl−oad − − − −
0b
IA-only TC-min E E-Var-U VaR CVaR
Figure 18: The average daily weight of b in relation to the whole b strategy for remaining
0
portfoliosv inthesettingofanewmarketplayer. Thenaive-basedstrategiesareexcluded
for better clarity
46

1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − Tim−e,v=5%ofs−olar − − − −
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − Tim−e,v=1%ofw−ind − − − −
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − Tim−e,v=5%ofl−oad − − − −
0b
IA-only TC-min E E-NoImp E-LinImp E-LinImpMeff E-Meff
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − Tim−e,v=5%ofs−olar − − − −
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − Tim−e,v=1%ofw−ind − − − −
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − Tim−e,v=5%ofl−oad − − − −
0b
IA-only TC-min E E-Var-U VaR CVaR
Figure 19: The average daily weight of b in relation to the whole b strategy for remaining
0
portfoliosv inthesettingofanewmarketplayer. Thenaive-basedstrategiesareexcluded
for better clarity
47

1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=1MW(sell)
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=10MW(sell)
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=100MW(sell)
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=1000MW(sell)
0b
IA-only TC-min E E-NoImp E-LinImp E-LinImpMeff E-Meff
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=1MW(sell)
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=10MW(sell)
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=100MW(sell)
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=1000MW(sell)
0b
IA-only TC-min E E-Var-U VaR CVaR
Figure 20: The average daily weight of b in relation to the whole b strategy for remaining
0
portfoliosv inthesettingofanewmarketplayer. Thenaive-basedstrategiesareexcluded
for better clarity
48

1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=1MW(buy)
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=10MW(buy)
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=100MW(buy)
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=1000MW(buy)
0b
IA-only TC-min E E-NoImp E-LinImp E-LinImpMeff E-Meff
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=1MW(buy)
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=10MW(buy)
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=100MW(buy)
0b
1.0
0.5
0.0
2018 01 2018 05 2018 09 2019 01 2019 05 2019 09 2020 01 2020 05 2020 09 2021 01
− − − − − − − − − −
Time,v=1000MW(buy)
0b
IA-only TC-min E E-Var-U VaR CVaR
Figure 21: The average daily weight of b in relation to the whole b strategy for remaining
0
portfoliosv inthesettingofanewmarketplayer. Thenaive-basedstrategiesareexcluded
for better clarity
49