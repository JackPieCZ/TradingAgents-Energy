CHARLES UNIVERSITY

FACULTY OF SOCIAL SCIENCES

Institute of Economic Studies

Bachelor thesis

2017

Samuel B´ereˇs

CHARLES UNIVERSITY

FACULTY OF SOCIAL SCIENCES

Institute of Economic Studies

Samuel B´ereˇs

Impact of Czech intraday market
on the electricity prices

Bachelor thesis

Prague 2017

Author: Samuel B´ereˇs

Supervisor: doc. PhDr. Ladislav Kriˇstoufek Ph.D.

Academic Year: 2016/2017

Bibliographic note

B´EREˇS, Samuel. Impact of Czech intraday market on the electricity price.

Prague 2017. 46 pp. Bachelor thesis (Bc.) Charles University, Faculty of So-

cial Sciences, Institute of Economic Studies. Thesis supervisor doc. PhDr.

Ladislav Kriˇstoufek Ph.D.

Abstract

We analyse Czech intraday market for electricity and its impact on day-

ahead prices. We inspect eﬀect of fundamental drivers of price deviation

between intraday and day-ahead market in form of positive and negative

forecast errors and examine intraday price’s role in explaining next trading

period’s day-ahead price. Our ﬁndings suggest photovoltaic and load fore-

cast errors to be most statistically signiﬁcant fundamental factors, together

with autoregressive term and day-ahead price, determining intraday market

price deviation from day-ahead. Variables’ inﬂuences on intraday market

are in accordance with hypothesised expectations, except for the eﬀect of

export and excessive import of electricity to and from German TSO, 50

Hertz, and extreme day-ahead prices. We conﬁrmed symmetric eﬀects of

forecast errors on intraday price for all observed variables. In the second

part, intraday prices are found to be statistically signiﬁcant factor aﬀecting

next day’s day-ahead market price. The results support the conclusion that

Czech spot market for electricity possesses mean-reverting properties.

Keywords

electricity, intraday market for electricity, price modeling

Abstrakt

Analyzovali sme ˇcesk´y vn´utrodenn´y trh pre elektrick´u energiu a jeho vplyv

na ceny na dennom trhu. Presk´umali sme efekt fundament´alnych fakt-

orov cenovej odch´ylky vn´utrodenn´eho a denn´eho trhu vo forme kladnej

a z´apornej chyby v ich predpovedi a otestovali sme ´ulohu vn´utrodennej

ceny pri vysvetl’ovan´ı ceny na dennom trhu v nasleduj´ucom obchoduj´ucom

obdob´ı. V´ysledky anal´yzy ukazuj´u, ˇze chyby v predpovedi fotovoltaickej

v´yroby a zat’aˇzenia siete s´u najsigniﬁkantnejˇs´ımi fundament´alnymi faktormi,

spolu s autoregres´ıvnym ˇclenom a cenou na dennom trhu, urˇcuj´ucimi cenov´u

odch´ylku vn´utrodenn´eho a denn´eho trhu. Efekty pozorovan´ych premenn´ych

na vn´utrodenn´y trh s´u v s´ulade s predpokladan´ymi oˇcak´avaniami, s v´ynimkou

efektu v´yvozu a nadmern´eho dovozu elektriny zo strany nemeck´eho prev´adzk-

ovatel’a prenosovej s´ustavy, 50 Hertz, a efektu extr´emnych cien na dennom

trhu. Potvrdili sme symetrick´y efekt ch´yb v predpovedi na vn´utrodenn´e ceny

pre vˇsetky pozorovan´e premenn´e. V druhej ˇcasti anal´yzy boli vn´utrodenn´e

ceny identiﬁkovan´e ako ˇstatisticky dˆoleˇzit´y prvok ovplyvˇnuj´uci cenu denn´eho

trhu na nasleduj´uci deˇn. V´ysledky podporuj´u z´aver, ˇze ceny na ˇceskom

kr´atkodobom trhu pre elektrinu sa pribliˇzuj´u k ich strednej hodnote.

Kl’´uˇcov´e slov´a

elektrick´a energia, vn´utrodenn´y trh pre elektrick´u energiu, modelovanie ceny

Declaration of Authorship

I hereby proclaim that I wrote my bachelor thesis on my own under the

leadership of my supervisor and that the references include all resources and

literature I have used.

I grant a permission to reproduce and to distribute copies of this thesis

document in whole or in part.

Prague, 31 July 2017

Signature

Acknowledgment

I would like to express my sincere gratitude to doc. PhDr. Ladislav Kriˇstoufek

Ph.D. for his supervision and guidance of my thesis. His expertise and

insightful suggestions presented irreplaceable inputs during the process of

writing the thesis.

The Bachelor Thesis Proposal

Author

Samuel B´ereˇs

Supervisor

doc. PhDr. Ladislav Kriˇstoufek Ph.D.

Proposed topic

Impact of Czech intraday market on the electricity price aaaaaaa,,

Research question and motivation

Nature of the electricity makes it rather speciﬁc commodity. It cannot be

stocked, thus supply must equal demand at any time. Historically this was

mostly achieved by trading electricity on day-ahead market where trading

takes place 12 – 36 hours before the actual power delivery. Substantial

changes in sources of electric power across the Europe and considerable shift

towards the renewable sources which are unpredictable by nature caused sig-

niﬁcantly increased short-term volatility in prices and more frequent occur-

rence of imbalances in futures and day-ahead contracts and actual volume of

electricity in the grid. This situation drives electricity market participants’

want and need to trade electricity closer to the time of delivery in real

time. Consequently, the intraday market, which allows market participants

to trade the electric power until one hour before delivery, is becoming more

important in balancing supply and demand in the power market. The re-

search question of the thesis will be therefore focused on which determinants

play most important role on Czech intraday market and how intraday mar-

ket inﬂuences trading prices at day-ahead market.

Contribution

The main contribution of my thesis will consist in answering the question

whether the emerging intraday market in Czech Republic inﬂuences other

market for electricity and succeeds in supplementing the day-ahead market

by oﬀsetting forecast errors and imbalances between day-ahead contracts

and produced volume of electricity. Small research has been conducted on

German electricity market, yet there is no study focused on Czech market.

Results of potential intercorrelation of spot power markets might bring some

thought-provoking implications. Secondly, analysis will be conducted to ex-

amine price formation on Czech intraday market, more speciﬁcally, what

extent of intraday price can be explained by fundamental determinants such

as renewable generation and what is the role of day-ahead price.

Methodology

Because of autoregressive properties of electricity spot prices, autoregress-

ive time series model will be used in both part of the analysis. Hypotheses

for forecast errors of fundamental determinants will be elaborated based on

theoretical background and tested in intraday price regression. Renewables

will be assumed to play most signiﬁcant role aﬀecting deviation of intraday

prices from day-ahead’s. Regression of day-ahead prices on lagged intraday

prices will then reveal their explanatory power in Czech electricity spot mar-

ket. Adjustment for seasonality, peak and oﬀ-peak hours and trend will be

performed throughout analysis. Data will be gathered primarily from OTE,
ˇCEPS, ENTSOE and EEX.

Outline

1. Abstract

2. Introduction

3. Literature review

4. Czech power market

5. Data

6. Methodology and Hypotheses

7. Results and Discussion

8. Conclusion

Relevant literature

1. Pape, Christian, Simon Hagemann, and Christoph Weber.

‘Are Fun-

damentals Enough? Explaining Price Variations in the German Day-

Ahead and Intraday Power Market’. Energy Economics 54 (February

2016): 376–87.

2. Hagemann, S., 2015. Price Determinants in the German Intraday Mar-

ket for Electricity: An Empirical Analysis. Journal of Energy Markets

2015, 8, pp. 21-45.

3. Haas, Reinhard, Hans Auer, Gustav Resch, and Georg Lettner. ‘Chapter

5 - The Growing Impact of Renewable Energy in European Electricity

Markets A2 - Sioshansi, Fereidoon P.’ In Evolution of Global Electricity

Markets, 125–46. Boston: Academic Press, 2013.

4. Hagemann, Simon, and Christoph Weber.

‘An Empirical Analysis of

Liquidity and Its Determinants in the German Intraday Market for

Electricity’. SSRN Scholarly Paper. Rochester, NY: Social Science

Research Network, 8 October 2013

5. Clements, A. E., A. S. Hurn, and Z. Li. ‘Forecasting Day-Ahead Electri-

city Load Using a Multiple Equation Time Series Approach’. European

Journal of Operational Research 251, no. 2 (1 June 2016): 522–30.

6. Kiesel, Ruediger, and Florentina Paraschiv.

‘Econometric Analysis of

15-Minute Intraday Electricity Prices’. SSRN Scholarly Paper. Rochester,

NY: Social Science Research Network, 8 October 2015.

7. Weber, C. ‘Adequate Intraday Market Design to Enable the Integration

of Wind Energy into the European Power Systems’. Energy Policy 38,

no. 7 (2010): 3155–63.

Contents

List of Tables and Figures

1 Introduction

2 Literature review

2.1 Electricity spot price modelling . . . . . . . . . . . . . . . .

2.2 RES eﬀect on electricity spot prices . . . . . . . . . . . . . .

2.3

Intraday market . . . . . . . . . . . . . . . . . . . . . . . . .

3 Czech power market

4 Data

4.1

Intraday and day-ahead prices . . . . . . . . . . . . . . . . .

4.2 Renewable energy sources

. . . . . . . . . . . . . . . . . . .

4.3 Load . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

4.4 Cross border power exchange

. . . . . . . . . . . . . . . . .

4.5 Coal and Gas . . . . . . . . . . . . . . . . . . . . . . . . . .

4.6 CO2 allowance

. . . . . . . . . . . . . . . . . . . . . . . . .

5 Methodology and Hypotheses

5.1 Wind Forecast . . . . . . . . . . . . . . . . . . . . . . . . . .

5.2

Intraday market . . . . . . . . . . . . . . . . . . . . . . . . .

5.3 Day-ahead market

. . . . . . . . . . . . . . . . . . . . . . .

6 Results and Discussion

6.1 Wind Forecast . . . . . . . . . . . . . . . . . . . . . . . . . .

6.2

Intraday market . . . . . . . . . . . . . . . . . . . . . . . . .

6.3 Day-ahead market

. . . . . . . . . . . . . . . . . . . . . . .

7 Conclusion

References

Appendix

i

1

4

4

5

7

10

14

14

15

15

16

16

17

19

19

20

27

31

31

32

39

45

47

53

List of Tables

1

2

3

4

5

6

7

8

9

Gross generation and installed capacity by production type .

Overview of data used in the analysis . . . . . . . . . . . . .

Descriptive statistics of electricity spot prices

. . . . . . . .

Hypotheses summary for intraday analysis . . . . . . . . . .

Estimation for wind forecast . . . . . . . . . . . . . . . . . .

Descriptive statistics of wind FE . . . . . . . . . . . . . . . .

Regression results for spot price deviation . . . . . . . . . .

Regression results for spot price deviation with DAp spikes

and sinks

. . . . . . . . . . . . . . . . . . . . . . . . . . . .

Results of symmetry hypotheses . . . . . . . . . . . . . . . .

13

18

21

27

31

32

34

37

38

10 Regression results for day-ahead price with lagged intraday

prices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

40

11 Regression results for day-ahead price with lagged intraday

and day-ahead prices . . . . . . . . . . . . . . . . . . . . . .

12 Explanatory power of independent factors in DAp regression

13 Regression results for spot price deviation without autore-

41

44

gressive component . . . . . . . . . . . . . . . . . . . . . . .

54

14 Full regression results for day-ahead price with lagged intra-

day prices . . . . . . . . . . . . . . . . . . . . . . . . . . . .

55

15 Full regression results for day-ahead price with intraday and

day-ahead prices

. . . . . . . . . . . . . . . . . . . . . . . .

16 Regression results of independent factors on DAp residuals .

17 Regression results of exogenous independent factors on DAp

residuals . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

18 Regression results of intraday prices on DAp residuals . . . .

56

57

57

58

i

List of Figures

1

2

3

4

ACF and PACF functions of day-ahead price . . . . . . . . .

ACF and PACF functions of day-ahead price model residuals

ACF and PACF functions of wind generation . . . . . . . . .

ACF and PACF functions of price deviation between intraday

39

42

53

and day-ahead price

. . . . . . . . . . . . . . . . . . . . . .

53

ii

1

Introduction

In recent decades, power markets have experienced two major momentous

points. First, with liberalization of power markets, electricity has become

tradable commodity on various markets. Unlike other commodities, nature

of electricity makes it rather speciﬁc product to trade. Due to current lack

of technology capable of eﬃcient storage of electricity, there must be an

omnipresent balance between produced and consumed electric power. As a

consequence, demand for electricity has to equal supply at any time. Another

characteristic feature of electricity market is price-inelastic demand, with

perfectly inelastic demand in short run. These particularities of electricity

resulted in complex wholesale market and trading systems.

Second signiﬁcant moment in development of power markets was ex-

tensive implementation of intermittent renewable energy sources (RES), i.e.

wind and solar generation units. Since we focus on Czech power market

and there is no concentrating solar power (CSP) technology in use in Czech

Republic, we will later in the thesis use terms solar and photovoltaic (PV)

interchangeably. Development of RES generally increases volatility of gen-

erated electricity. Consequent higher volatility in price, in combination with

unique features of electricity, caused spot market to become vital part of

power market. Hence, spot market has become topic of extensive research

in pioneering RES countries, such as Germany. Czech day-ahead and intra-

day markets, although much smaller in size than German spot market, play

an important role when it comes to dealing with RES or load forecast error.

Especially intraday market, regardless of its size, represents last trading op-

portunity for market participants to balance their positions on the power

market.

The objective of this thesis is to analyse Czech intraday market for elec-

tricity in two ways. First, we will try to explain price formation with fun-

damental variables’ forecast errors and attempt to identify signiﬁcant de-

terminants of intraday prices. Second part will focus on observing eﬀect of

intraday price on other spot market price, in this case day-ahead price. Be-

1

cause day-ahead market closes before intraday prices for selected time period

are known, we cannot use intraday price from period t as an explanatory

variable, but rather price from period t − 24. Since day-ahead prices were

repeatedly proven to be dependent on previous value (Kristansen, 2012;

Ferkingstad et al., 2011), it is probable that lagged day-ahead prices will

have more signiﬁcant explanatory power than lagged intraday prices. Nev-

ertheless, it is worth examining whether intraday price takes part in price

formation of day ahead market and testing the hypothesis of intercorrelated

short-term markets.

For testing selected price determinants of intraday market, we will per-

form linear regression of time series data with autoregressive term as partial

adjustment aspect. For the second part of our twofold analysis, we will em-

ploy autoregressive model as well. During both estimations, we will control

for trend and monthly, weekly as well as peak hours (only during weekdays)

seasonality using dummy variables.

To the best of our knowledge, there is no literature covering Czech intra-

day market, hence this thesis will attempt to ﬁll the gap in the overview of

Czech spot market. The thesis intends to contribute to existing electricity

literature by identifying theoretical price determinants of Czech intraday

market, elaborating on Hagemann’s research (2015) by further developing

his hypotheses on neighbouring market. Moreover, it provides foundation

for further investigation of Czech intraday market. Lastly, by testing price

relation of Czech spot markets, it opens door for further research regarding

electricity inter-market correlation and price inﬂuence.

The remainder of this thesis is organised as follows. In section two, over-

view of relevant literature for the thesis is presented, covering already con-

ducted research in electricity spot price modelling, impact of renewables and

intraday market. Third section covers basic structure of Czech power mar-

ket, with focus on spot market and RES development. Next section provides

an overview of gathered time series data for empirical analysis. Section ﬁve

continues with methodology, models and estimators based on reviewed lit-

2

erature. Speciﬁc hypotheses with expected results are elaborated. Besides

presentation and interpretation of the results, section six provides a discus-

sion of expected and obtained empirical results. Finally, conclusion sum-

marises results and ﬁndings of the thesis and proposes direction for further

research opportunities.

3

2 Literature review

2.1 Electricity spot price modelling

Most research work regarding electricity spot market has been done on Nord

Power markets and German spot markets. Due to the development of Ger-

man power industry after 2011, considerable implementation of renewables,

importance of German electricity market as well as increase in transparency

and data availability from EPEX, great number of recent papers have fo-

cused on German electricity spot market. Ziel et al. (2014) published paper

which takes into account particularities of EPEX (most considerably load

and percentage of production from solar and wind generators) and developed

sophisticated VAR-TARCH time series model for modelling electricity spot

prices. Paraschiv et al.

(2014) examined eﬀect of developing renewable

energy on EEX day-ahead prices. Using state space model with changing

coeﬃcients, they concluded that prices continuously adapt to market funda-

mentals and that infeed from renewables causes spot price sensitivity to gas

decrease gradually after 2011 as this fuel is situated very high in merit order

curve. Overall ﬁndings show that day-ahead prices decreased due to substan-

tial implementation of renewables, yet consumer prices increased because of

additional feed-in tariﬀ used for promoting RES. Fundamental modelling is

based on a premise that electricity prices are result of joint performance of

fundamental variables (e.g. weather data, RES, load). Knittel and Roberts

(2005) used autoregressive moving average model with exogenious variables

(ARMAX) on Californian electricity prices including weather data such as

temperature and dummy variables for treating seasonality. Torro (2007)

switched to ARIMAX and expanded model by adding precipitation, reser-

voir level and diﬀerences between future and spot prices to forecast electricity

prices at Nord Pool.

Other researchers use autoregressive models when modelling and fore-

casting day-ahead electricity prices. AR model is often used as benchmark

model for spot price when comparing with diﬀerent approaches of spot price

estimation. Based on the work of Weron and Misiorek (2008), who ex-

4

amined twelve variations of AR models for day-ahead spot price forecasting,

research on modelling and forecasting Northern European day-ahead market

was conducted by Kristansen (2012) and Ferkingstad et al. (2011). Findings

of former research suggest hourly mean absolute percentage error ranging

from 8 to 11% for day-ahead prices at Nord Pool, while later research found

interconnection of Nordic and German electricity prices through gas prices.

Further approaches for modelling and forecasting electricity spot prices

can be divided into three streams. GARCH regression models is primarily

used on investigating electricity price volatility as for example in research

by Ketterer (2014) on the eﬀect of wind generation on price volatility or in

work of Kalantzis et Milonas (2013) who examined impact of futures trading

on spot price volatility in France and Germany. Other two approaches con-

cern threshold regression models and time-varying parameter models (Erni,

2012), nevertheless since these models are out of scope of this thesis, we will

not devote them more space.

2.2 RES eﬀect on electricity spot prices

Based on a mentioned research, importance of spot markets, and intraday

market as well, is closely related to the intermittency and continuity of

power supply. Hence research on eﬀect of renewables on spot prices play an

important role when we will later think of potential hypotheses for Czech

intraday market as well as relation between intraday and day-ahead market.

Ketterer’s paper on impact of wind generation on the electricity spot

prices in Germany (2014) shows that implementation of more renewables can

lead to decreased prices on spot market, but increases price volatility. Trend

of decreasing wholesale prices and increased volatility was again found and

conﬁrmed in simulation of further integration of renewable sources in next

decade. Green and Vasilakos (2011) found these results as a consequence of

increased proportion of wind power generation in Britain in 2020. P¨oyry’s

report (2011) concludes similar merit-order eﬀect which will result in de-

creased wholesale prices in North and West European power markets. Merit

5

order eﬀect related to the development of renewables (predominantly wind

and solar) refers to merit order curve, often used in energy sector to rank

types of electricity generation based on their price (marginal cost). Since

renewable sources have basically zero marginal costs, in theory, merit order

eﬀect (MOE) of renewables decreases wholesale prices, as well as reduces

electricity output of conventional power plants and pushes highest cost gen-

erators out of the market dispatch.

Described eﬀect was conﬁrmed in studies of Australian as well as Spanish

electricity markets. Forrest and MacGill (2013) examined the impact of

wind on Australian spot market prices and showed that wind energy sources

in Australia reduce dispatch of gas generation and recently also brown coal

generation. Gelabert et al.’s (2011) conclusion on the eﬀect of renewables

on prices at Spanish electricity market suggests that marginal increase of 1

GWh of electricity production from renewables results in price reduction of

almost 2 EUR/MWh. MOE in Germany was initially studied by Sensfus et

al. (2008) and results indicated strong impact of merit order eﬀect, exceeding

amount of additional tariﬀ for renewable energy. Wurzburg et al. (2013)

summarised MOE on various European markets concluding general price fall

due to increased RES production. Additionally, in their empirical analysis on

German-Austrian market, they found day-ahead electricity price decrease by

approximately 1 EUR/MWh for each GWh of RES. Results remained stable

both before and after deactivoation of seven nuclear power plants in 2011.

Tveten et al. (2013) focused solely on solar merit order eﬀect on German

electricity prices and found on average 7% decrease in prices, but more

importantly substantial decrease in average daily price variation by 23%.

Latest study of merit order eﬀect on Czech power market by Lun´aˇckov´a et

al (2017) divides renewable sources into two groups, solar energy and other

renewables. MOE is conﬁrmed for later group, but empirical results suggest

that solar energy does not cause Czech spot prices to decrease, contradicting

results from other European markets and concluding inappropriateness of

Czech policy towards solar energy.

6

2.3

Intraday market

Regarding the research focused on electricity intraday market, great portion

of the research was oriented on ideal market design of intraday market, so it

would fulﬁl its primary purpose to assist day-ahead market and ease integ-

ration of RES into power systems. Borggrefe and Neuhoﬀ (2011) explores

intraday market power designs in European countries and North America

and evaluate its capability of dealing with wind intermittency as wind fore-

cast error drops substantially 24h before delivery. Similar assessment of

European intraday market designs for wind integration was conducted by

Weber (2010). He proposed four alternatives for improving intraday mar-

ket design mostly oriented on increasing liquidity on intraday market. Furio

(2011) tried to cover Spanish intraday market, explaining its design (six con-

secutive trading sessions organised in an auction make it unique in Europe),

prices and evolution of traded volume from 2000 to 2010. In his estimations,

he conﬁrmed diﬀerence in peak and oﬀ-peak hours’ prices, daily seasonality,

highest willingness to pay for electricity in last hours before delivery and

positive relationship between price and volume of electricity traded.

Hagemann and Weber (2013) attempted to explain liquidity determinants

at German intraday market. Developing two distinct models, liquidity is far

better explained by trading model, assuming proﬁt-maximizing trading be-

haviour than fundamental merit-order model. Later, Hagemann and Weber

(2015) tried to examine the liquidity at European intraday markets by ob-

serving trading volume at national markets in comparison with forecasted

volume of their benchmark model. Model results lead to two conclusions;

small market players typically do not participate in continuous exchange

on intraday markets (with exception for Germany) and higher liquidity at

auction-based market design cannot be attributed to market design, rather

to country speciﬁc market peculiarities. Regarding further research of elec-

tricity intraday market, Garnier and Madlener (2014) formulated a model

for optimized trading strategy of balancing forecast error of renewables. The

bidding model, using options valuations and dynamic programming, outper-

7

forms on average other eﬃcient alternatives by more than 6%.

Literature concerning modelling of electricity intraday prices is even more

limited. Very recently, work of Karanﬁl and Li (2017) suggested that wind

and conventional generation forecast errors play fundamental role in de-

viation of intraday and day-ahead prices in Danish power market. They

concluded that gap between intraday and day-ahead prices is negatively

inﬂuenced by renewable forecast error, whereas an unexpected increase in

combined heat and power (CHP) generation leads to higher intraday prices

and wider deviation from day-ahead prices. Kiesel and Paraschiv (2017)

were ﬁrst to examine German 15-minutes intraday prices. They were ﬁrst

to use updated intraday forecasting errors to investigate bidding behaviour.

The changes in behaviour as well as inﬂuence of errors on prices are in ac-

cordance with intuition, intraday prices increases with negative forecast error

and vice versa, nevertheless the price adjustment is shown to be asymmetric.

Pape et al. (2016) used fundamental modelling approach to explain prices in

German intraday market. Results indicated that chosen fundamental vari-

ables explained 75 % of price variance. Furthermore, results suggest that

including day-ahead prices may improve explaining power of intraday price

modelling. Researchers conclude that diﬀerences in modelled and actual

prices might be caused by disregarded start-up costs, market state (extreme

cases of excessive supply or capacity scarcity) and traders’ behaviour as they

tend to predict prices based on past price information from the markets.

Most relevant research for the ﬁrst part of our analysis was conducted by

Hagemann (2015). He studied price formation process of German intraday

prices for two years (2010 - 2011) and tried to identify determinants of

price diﬀerence between day-ahead and intraday prices. Empirical results

are generally in accordance with theoretical sign and magnitude expectation

of individual price determinants. Regression indicates stronger impact on

intraday prices during the night which can be explained by steeper demand

and supply curves at night.

In summary, research explaining spot price determinants and forecast-

8

ing spot prices is well developed, primarily for day-ahead market. Despite

the growing importance of electricity intraday market, research oriented on

explaining price formation and interrelation of intraday market with other

markets is fairly limited. To the best of our knowledge, the only research dir-

ectly approaching this question has been done on German power market two

years ago, and Czech intraday market has not been studied by any researcher

yet. We will build up on previous hypotheses for German market, adjust

them with regard to current market situation and test them on Czech power

market. Later inﬂuence of intraday prices on next day’s day-ahead prices

will be examined and so we will contribute to overview of Czech electricity

spot market.

9

3 Czech power market

In this section, we will provide a quick overview on structure of Czech power

market. Focus will be given to wholesale market, speciﬁcally Czech spot

market, its development, peculiarities and share of RES in generation.

Over the last decades, electricity markets in most part of the world have

been deregulated. This means less government control of power sector and

introduction of competition to originally monopolistic market for electric

power. Besides development of retail sector and wholesale market for elec-

tricity, deregulation led to vertically unbundled power generation and trans-

mission and distribution sector.

Deregulation of Czech electricity market occurred in numerous phases.

The process started in 2002 and full liberalization of electricity market was

achieved in 2006 (Vitner, 2006). As described above, that means vertical

separation of speciﬁc power sectors and end-customers were no longer obliged

to consume electricity from local supplier but rather gained freedom of choice

regarding electricity provider. Electricity became tradable commodity on

both long-term and short-term electricity markets. Long-term market is
organised by PXE (Power Exchange Central Europe) and ˇCMKBK (Czech

Moravian Commodity Exchange Kladno). Primary product traded at these

exchanges are futures, contracts to consume or deliver a certain amount of

electricity at agreed time in the future for agreed price today (KU Leuven

Energy Institute, 2015). Following continuous trading scheme, futures on

PXE are traded anonymously in form of months (up to 6), quarters (up to

4) or years (up to 3) ahead contracts and are divided to base load futures,

covering all day, and peak load futures (PXE, 2016). While many researchers

consider double peak intraday periods, PXE and OTE follows only single

peak period from 8 a.m. to 8 p.m. and the rest is considered as oﬀ-peak

hours. In order to maintain consistency with market operator’s approach

and data, we will use single peak structure later in empirical analysis.

Like most of European electricity markets, Czech market for electricity

follows price based approach (Luˇn´aˇckov´a et al., 2017), under which short-

10

run marginal cost (SRMC) equals price of additionally produced MWh of

electricity and power plant choose not to produce if price is below its SRMC

(Cramton, 2013). Together with practically perfectly inelastic demand in

short run, this creates market conditions in which short-term market plays

vital role. Czech short-term regulated market is organised by OTE and di-

vided into block market, day-ahead market, intraday market and balancing

market with regulation energy. We will not discuss block market and bal-

ancing market as these are not primary focus of this thesis and their size

regarding annual traded volume is fairly small. More on these markets can

be found in OTE reports and website (OTE, 2016).

Czech day-ahead market for electricity, a platform for trading electricity

one day before physical delivery, was launched in 2002, one year after found-

ation of OTE. From 1.2.2009, OTE became the single market operator for

Czech electricity spot market (until 2009, short-term electricity trading was

organised by both OTE and PXE). Czech day-ahead market is coupled with

Slovak (since 2009), Hungarian (since 2012) and Romanian (since 2014) day-

ahead market (OTE, 2014). This means that bids from participants on all

four markets are matched jointly without need for acquiring transmission

capacity. In contrast to future contracts, for which most of the trades hap-

pen on exchange (around 93%, PXE Fact book 2015), on day-ahead market,

most of trades are closed over the counter (around 70 %, OTE 2016). Over

the counter trading (OTC), is decentralised form of bilateral agreement on

volume and price of electricity before actual delivery, independent of mar-

ket operator intervention. Although OTC prices are not publicly disclosed,

it is reasonable to assume that prices of OTC trading do not signiﬁcantly

deviates from prices at regulated market, since market participants would

trade only on platform, which yields higher proﬁt. Day-ahead trading is or-

ganised as daily anonymous auction, with participants asking buying/selling

bids for particular hours of the following day with market closing at 11 a.m.

Market operator then sets ﬁnal spot price for each hour of the day before

2:30 p.m., based on a current market situation, available information and

11

business terms of OTE (OTE, 2017). Using this price determination scheme,

market operator can control for demand and supply equilibrium, since after

closure of the day-ahead market, after-trading scheduled generation has to

equal forecasted demand plus net export. From economic theory, day-ahead

market price should be equal to marginal cost of production of last power

plant on merit order curve needed to cover market demand (Joskow and

Kahn, 2001; Karakatsani and Bunn, 2008). Increasing importance of day-

ahead market can be observed on yearly rising proportion of traded volume.

In 2016, electricity volume traded on Czech day-ahead spot market totalled

to record high of 20.14 TWh (OTE, 2016).

After day-ahead closure, Czech intraday market opens daily at 3 p.m.

and closes separately for each hourly period 60 minutes before delivery.

Intraday market allows its participants to balance discrepancies and de-

viations from scheduled day-ahead nominations in case of sudden electricity

scarcity/surplus, mostly due to improved RES forecast, change in demand,

updated cross border ﬂow or unexpected power plant outages. Trading at

intraday market is organised through notice board, where market parti-

cipants anonymously send their buying/selling bid with exact volume and

price they are willing to pay. Unlike most European intraday markets, where

these bids are continuously cleared (Germany, France, Belgium), in Czech

intraday market bids have to be accepted by another participant through

OTE trading platform. Moreover, as opposed to most of European markets,

Czech short-term market is opened also during weekends and national hol-

idays. Despite its small share on overall traded volume (544.7 GWh; OTE,

2016), intraday market in particular, gained its importance after implement-

ation of intermittent generation units that are represented primarily by solar

and wind power plants.

With concerns for climate change, Czech Republic introduced ﬁrst Act on

promotion of electricity production from renewable energy sources back in

2005 (IEA, Act No. 180/2005). This was adopted with aim to reach the EU

indicative target for 2010 - 8% share of RES on gross national consumption

12

and presented with support scheme for renewable sources in form of feed-in

tariﬀ. TSO was obliged to preferentially connect RES to transmission system

and producers were guaranteed to receive so called “green bonus” from TSO.

The amount of bonus was set annually by Energy regulatory oﬃce (ERU)

and diﬀered based on a RES production type. Green bonus was guaranteed

to stay ﬁxed for every MWh produced for a whole year. Market incentives in

combination with signiﬁcant decrease in price of photovoltaic technology in

2009, resulted in solar boom in Czech power market in years 2010, 2011. As a

consequence, quick achievement of EU indicative target for 2020 - 13% share

of RES in gross consumption was reached, however cost of support scheme

has become excessive burden for both end-consumers and state budget. As

a result, solar tax of 26% for solar producers was introduced for years 2011 -

2013, later extended (IEA, Act No. 165/2012) and followed by cancellation

of solar support scheme after 2013. Because of the market situation in years

2010 - 2013 and already achieved EU target, it is reasonable to assume

that Czech power market will not experience any major renewable boom in

upcoming years. Czech power sector remains dominated by thermal (mostly

lignite) and nuclear power, which combined account for 83,8% of annual

electricity production and 68,8% of installed capacity (Table 1).

Table 1: Gross generation and installed capacity by production type

Generation (GWh)

Capacity (MW)

2015

2016

2015

2016

Nuclear

26 840.8

24 104.2

4 290.0

4 290.0

Thermal

44 819.2

45 704.1

10 741.9

10 850.0

Combined Cycle

2 749.0

4 049.2

1 363.3

1 363.5

Gas Fired

3 572.1

3 613.9

855.9

874.0

Hydro

1 794.8

2 000.5

1 087.5

1 090.2

Pumped Storage

1 276.0

1 201.5

1 171.5

1 171.5

Wind

572.6

497.0

280.6

282.0

Photovoltaic

2 263.8

2 131.5

2 074.9

2 067.9

Total

83 888.4

83 301.9

21 865.7

21 989.0

Source: ERU, 2016 Yearly report on the operation of Czech electricity grid.

13

4 Data

We gathered data for later empirical analysis from various sources, mainly
using Czech transmission system operator ( ˇCEPS) database, Czech elec-

tricity and gas market operator (OTE), European Network of Transmis-

sion System Operators for Electricity (ENTSOE) transparency platform and

European Energy Exchange (EEX) market data as sources of highest cred-

ibility. We decided to use the latest data possible over the span of 2 years,

hence our dataset contains data from January 2015 to May 2017 (in January

2015, ENTSOE launched transparency platform and made various energy

data available to the public). It is worth mentioning that year 2016 was leap

year, thus had 366 days.

4.1

Intraday and day-ahead prices

Electricity spot prices represent vital part in both regression analyses. Elec-

tricity intraday price on Czech power market is hourly updated, publicly

available information provided by OTE. Hourly data for both intraday prices

as well as corresponding traded volume can be obtained from OTE website,

in form of Yearly report packages. Regarding previously discussed market

design of Czech intraday market, prices are reported as weighted average

price per MWh. Since intraday prices were reported in CZK/MWh until

August 2016 and in EUR/MWh from 24.8.2016 onwards, we will use Czech

National Bank daily conversion rates for data from earlier period in order to

achieve desired consistency. We opt for EUR prices due to easier comparison

with the prices from day-ahead market as well as simpler comparison with

research on other European spot power markets. Data will be ﬁrstly used as

component of dependent variable in explaining price determinants of devi-

ation of intraday price from day-ahead price and later tested for hypothesis

of intraday prices’ impact on day-ahead prices.

Day-ahead prices are obtained from the same source, with two minor

diﬀerences. Due to diﬀerent market design than intraday market, price is

reported as a marginal price and is published directly in EUR/MWh, pre-

14

sumably because of coupled markets with Slovakia, Hungary and Romania.

Extreme day-ahead prices will be used for testing hypotheses on intraday

price formation and day-ahead prices are expected to exhibit strong autore-

gressive properties in second model estimation.

4.2 Renewable energy sources

We obtained hourly day-ahead generation forecast for solar energy in Czech

Republic from ENTSOE transparency platform. This will be later used to

compute solar generation forecast error as diﬀerence between actual hourly

realised PV generation and PV generation forecast. Real generation data
are publicly available on ˇCEPS website. In order to achieve consistency in
data from ENTSOE and ˇCEPS, we have to work with hourly aggregate av-

erage data, since day-ahead forecast is published only for average generation

for particular hour. Under the assumption that on intraday market, diﬀer-

ence between realised generation from solar power plants and solar forecast

available one hour before delivery is negligible, we will be able to test eﬀect

of positive and negative forecast error on intraday electricity prices.

As far as wind power production is concerned, data for wind generation

forecast are not available for Czech Republic. As a consequence, we would

not be able to calculate wind forecast error. Although, wind power genera-

tion units represent only 1,28% of Czech installed capacity (Table 1), wind

has been repeatedly proven to be important fundamental factor for spot

market (Ketterer, 2014; Forrest and MacGill, 2013). Unlike solar, intermit-

tency of wind is present also during night and causes higher ﬂuctuation of

intraday prices. Thus, we will estimate wind generation forecast based on

large sample of historical hourly realised wind generation values obtained
from ˇCEPS. Methodology of this estimation will be outlined in next section.

4.3 Load

We will also consider load forecast and forecast error. Similarly, to renewable

forecast error, load forecast error is deﬁned as a deviation of realised mean

15

load value from forecasted value of load (Haubrich 2008). Hourly data of

realised load values as well as day-ahead forecast of load can be obtained
from ˇCEPS database. ˇCEPS deﬁne brutto load as:

Load = Generation (brutto) + Import − Export − Absorbed energy (1)

Load values in this dataset include consumption by power plant auxiliary

as well as network loses. Load forecast is usually considered as appropriate

proxy for supply of electricity that is expected by system operator. Due

to consistency in methodology of forecasting and measuring load as well as

intention to capture supply in terms of all electricity produced by power
plants, we prefer to use data from ˇCEPS rather than data provided by

ENTSOE.

4.4 Cross border power exchange

We will also include inﬂow/outﬂow of electricity from/to neighbouring coun-

tries. Since the transmission grid is most developed on the border with Ger-

many and at the same time, Germany is one of the most advanced European

country in terms of renewable power sources, we will include electricity in-

ﬂow/outﬂow with German TSO 50 Hertz in our analysis. According to
ˇCEPS data, 50 Hertz repeatedly imports more electricity than is originally

planned and is assumed to occasionally use Czech Republic transmission bor-

der for transferring excess electricity from renewables from North to South

Germany, in case German transmission network is used close to its capacity.

4.5 Coal and Gas

For second estimation, we have to consider fundamental drivers of day-ahead

electricity prices. Based on yearly report of Czech energy regulatory oﬃce

(ERU, 2016), coal accounts for 50.36% of Czech annual electricity generation

(lignite leading with 43,5%). Together with nuclear power, they account for

base load generation of Czech power market, hence presumably play immense

role in electricity price formation. However, characteristics of lignite do not

make it tradable commodity and lignite powered generation units tend to

16

be built in close proximity of lignite mines. For this reason, reference price

for lignite is generally unavailable for all electricity markets.

Closest data to trading coal prices we were able to obtain are daily

auctioned Amsterdam-Rotterdam-Antwerp (ARA) future contracts for coal

from EEX market data website. Published settlement prices in USD per

ton (USD/t) will be converted in EUR/t for comparability and consistency

with rest of data. These prices will be used as reference price for base load

fossil fuel production units. Similarly to Paraschiv et al. (2014), we will use

coal’s latest available price of front-month future contract before electricity

auction.

Although gas production may seem negligible in Czech power market

(only 4.11%; ERU, 2016), when considering its operational ﬂexibility and

high fuel cost per MWh, gas is located on the right end of merit order curve.

Consequently, during high demand periods or peak hours, gas production

price is likely to act as a price-setting energy source. That is why, we need

to reﬂect gas trading price when modelling day-ahead prices. Daily data

for spot trading price in form of reference prices are provided by CEGH

(Central European Gas Hub) and Czech Gas Exchange operated by PXE

(Power Exchange Central Europe). Gas spot reference price is calculated as

“weighted average of all trades concluded during the trading session on the

CEGH Czech Gas Spot Market” (PXE, Gas spot reference price) and uses

following formula in case that no trade occurred during trading session:

P rice =

Pz

i=1

Bidi+Aski
2

z

4.6 CO2 allowance

;

z − number of constellations

(2)

With coal being dominant electricity generator in Czech Republic, it is neces-

sary to control for the prices of CO2 allowances when estimating day-ahead

electricity prices. Acting as an additional expense to production cost of

power plant, price of CO2 allowances can lead to so called “fuel switch”

and adjust shape of merit order curve. After introduction of EU Emission

Trading Scheme (ETS) in 2005, operating under the cap and trade system,

17

which guarantees that emissions are reduced where it cost the least, and

after scheme revision for phase 3 (2013-2020), which replaced national cap

system with EU-wide cap, we can say that prices for CO2 allowances have

become uniﬁed for all EU members plus Norway, Lichtenstein and Iceland.

We will use data from EEX on European Carbon Index - ECarbix, which

is published on daily basis by EEX and calculated as “exchange-based price

for the current market value for EU emission allowances (EUA) in the third

trading period” (EEX, Indices).

Table 2: Overview of data used in the analysis

Variable

Description

Unit

Source

Volume weighted average intraday price

EUR/MWh

Marginal day-ahead price

EUR/MWh

Solar day-ahead generation forecast

Generation output of solar power plants

Wind

Generation output of wind power plants

Day-ahead Total Load Forecast

Total brutto load

Scheduled cross-border power ﬂow (50 Hertz)

Actual cross-border power ﬂow (50 Hertz)

OTE

OTE

ENTSOE
ˇCEPS
ˇCEPS
ˇCEPS
ˇCEPS
ˇCEPS
ˇCEPS

MW

MW

MW

MW

MW

MW

MW

IDp

DAp

PV

Load

GER

Gas*

Coal*

Gas spot reference price

EUR/MWh

PXE

Latest available price of the front-month

ARA futures contract

EUR/t

EEX

CO2∗

Latest available price of ECarbix index

EUR/tCO2

EEX

Note: Variables have hourly granularity; * marks daily granularity

18

5 Methodology and Hypotheses

Following threefold section outlines methods and econometric techniques

used in the thesis. We will opt for autoregressive model in all three parts,

as electricity prices and wind generation appear to be autocorrelated with

their lagged values.

5.1 Wind Forecast

Before focusing on spot market prices, we need to deal with lack of day-

ahead forecast for wind generation as we anticipate renewable sources to

play signiﬁcant role explaining electricity spot prices. Especially wind is

considered main factor of intraday market volatility and unexpected price

movements in countries with high percentage of wind generation such as

Germany.

With no access to meteorological information about wind speed and dir-

ection, we will use past realised wind generation as input for our forecast.

Unlike for physical forecasting model, historical data from wind generation

units can be used as input for statistical models (Lei et al., 2009). Xiaodan

et al. (2013) examined time series models (AR, ARMA) for short-term wind

power generation predictions and concluded eﬀectiveness of proposed meth-

ods, especially in case of unavailability of forecast data. Prediction errors

appeared to occur in time series turning points due to high randomness of

wind speed, nonetheless, when using big enough dataset of high frequency

data, time series model managed to give appropriately accurate output for

data points.

In order to ensure reasonably large sample for forecasting, we decided to

use ﬁrst ﬁve months of hourly data on wind generation, from January 2015

to May 2015 as input in autoregressive model (AR(p)). Our forecast for

wind generation will be obtained in three following steps:

1. Selection of parameter p will be based on Autocorrelation function

(ACF) and Partial autocorrelation function (PACF).

19

2. OLS minimization process will be used to estimate model coeﬃcients.

3. Estimated coeﬃcients and p lagged values will be used to calculate wind

generation forecast for the following hour.

Shape of ACF and PACF functions (Appendix, Figure 3) suggests to

include two lagged values, hence we use following AR(2) model:

windt = α + β1windt−1 + β2windt−2 + (cid:15)t

(3)

5.2

Intraday market

Based on a research publication by Hagemann (2015), in which price de-

terminants of German electricity intraday market are examined, we will try

to determine signiﬁcant factors which inﬂuence price change between Czech

intraday and day-ahead market for electricity.

In order to analyse price

formation on intraday market, we may establish price diﬀerence between

intraday and day-ahead market as our dependent variable.

dif pt = IDpt − DApt

(4)

Note: dif p - deviation of intraday price from day-ahead price in hour t; IDp, DAp - variables from

Table 2

It is justiﬁable to use deviation from day-ahead price for the following

reason. By characteristics of intraday market, which is used only after day-

ahead market is closed, intraday prices move based on updated, more precise

information and forecasts. Hence, deviation from day-ahead price captures

development of market situation compared to known day-ahead forecasts.

Descriptive statistics in Table 3 may give us a quick look at diﬀerences

between both prices.

20

Table 3: Descriptive statistics of electricity spot prices

Min

1st Qu.

Median

Mean

3rd Qu.

Max

dif p

IDp

DAp

-67.7000

-42.6500

-25.0000

-7.5500

21.6500

24.7100

0.5194

32.3200

32.0100

1.3300

34.6900

33.3600

8.9600

44.9700

40.0700

211.0000

238.3000

141.0000

Std Deviation

13.6519

18.6428

14.4406

Skewness

Kurtosis

ADF test

KPSS test

0.9507

1.0619

1.1446

10.7494

6.7647

7.8204

-19.0540

-14.1010

-12.6490

(0.01)

(0.01)

(0.01)

0.2179

1.2142

2.0579

(0.01)

(0.01)

(0.01)

Note: p-values in parentheses, KPSS test for trend-stationarity

Obtained results show us that range of intraday prices is much larger than

in case of day-ahead prices, with intraday maximum and minimum prices

being almost twice the values from day-ahead market. Occurrence of such

extreme values suggests larger impact of last minute market development

on intraday prices than on day-ahead prices.

Interquartile range can be

considered as reference for usual price range on both markets. Since intraday

market have larger interquartile range, it can be perceived as conﬁrmation

of intraday market being more price sensitive. Median price of both markets

is around 32 EUR/MWh, suggesting similarities of the markets if expected

market conditions turn out accurate. Slightly higher mean on both markets

indicate few more extreme observations in upper range of electricity spot

prices.

Relatively small and roughly symmetric interquartile range of price devi-

ation reveals that the two consecutive spot markets often end up with similar

prices. However maximum and minimum values suggest extreme losses for

market participants in case of severely incorrect forecasts. As mean and

21

median are close to zero, it proves that intraday price does not diﬀerentiate

from day-ahead price if forecasts are accurate. This supports the theory

of intraday price formation being based on day-ahead price and updated

market situation. We can also conclude that under same market conditions,

prices on intraday market tend to be slightly higher than on day-ahead mar-

ket as both mean and median are positive values and third quartile is bigger

than absolute value of ﬁrst quartile. This seems reasonable, since balancing

position few hours before delivery is expected to be more expensive than on

previous day.

Standard deviations are high for all electricity price variables, indicating

relatively wide range of values, with biggest dispersion of values on intraday

market. Based on a result of skewness and kurtosis, Czech spot prices and

their diﬀerence seem to deviate from normal distribution. All three variables

appear to have fat-tailed distribution, as they are leptokurtic and exhibit

positive skewness.

In accordance with literature on electricity spot price properties, both

day-ahead and intraday prices are found non-stationary and without unit-

root. Their deviation also manages to reject null hypothesis of unit root

(Dickey and Fuller, 1979), but null hypothesis for trend stationarity (spot

price deviation is proved to follow trend pattern in next section) still has to

be rejected (Kwiatkowski et al., 1992).

Since both day-ahead and intraday prices were repeatedly proven to be

correlated with previous hours values, it is reasonable to expect price de-

viation to be autocorrelated as well. We will deploy ARX (1) model as a

partial adjustment for autocorrelation (similarly to Woo et al., 2011) and fo-

cus on explaining price deviation with forecast errors of fundamental drivers,

which are assumed to have signiﬁcant inﬂuence on electricity market after

day-ahead market closure. For our intraday analysis, we will assume realised

values to act as proxy for intraday forecasts that is known one hour before

delivery, since these forecasts are not available. Based on previous work on

German (Hagemann and Weber, 2013) and Danish (Karanﬁl and Li, 2017)

22

intraday markets, we identiﬁed fundamental determinants to be solar, wind,

load and cross border ﬂow. For each factor, we diﬀerentiate between positive

and negative forecast error as this allows to make more elaborated inference

about variables impact on price deviation. To pursue consistency in inter-

pretation of estimation, we will use nonnegative values of forecast errors.

Finally, day-ahead price will be included in order to test hypothesis about

intraday price peaks and sinks. Equation 5 summarises estimation model

for spot price deviation.

dif pt = α + β1dif pt−1 + β2pos PVfet + β3neg PVfet + β4pos windfet

+ β5neg windfet + β6pos loadfet + β7neg loadfet

(5)

+ β8pos GERf et + β9neg GERf et + β10DApt + (cid:15)t

In spite of using diﬀerences, deviation between intraday and day-ahead

market may be suspected to move in seasonal patterns or follow trend. Thus,

we will test variables for trend pattern and monthly, weekly and daily sea-

sonality. We expect to ﬁnd trend and seasonal dummy variables insigniﬁcant

and work with original dataset. Moreover, we might have to deal with serial

correlation as well as heteroskedasticity in model residuals. If this will be

the case, Gauss-Markov assumptions are violated and we are not eligible to

draw valid inference, as error terms are no longer uncorrelated and uniform.

Although linear regression should not lead to biased coeﬃcient estimates,

this would give us biased standard errors, more likely to be underestimated

(Petersen, 2008). According to Wooldridge (2015), it is recommended to use

Newey-West heteroskedasticity and autocorrelation consistent estimator to

compute robust standard errors.

Before conducting analysis and examining hypotheses, we will test our

dataset for stationarity, using Augmented Dickey-Fuller (ADF) test and

Kwiatkowski-Phillips-Schmidt-Shin (KPSS) test. Under null hypothesis of

ADF test, presence of unit root in dataset will be tested and KPSS test

then decides on stationarity of variables, with null hypothesis being station-

ary data.

We will now present hypotheses for speciﬁc fundamental variables and

23

elaborate on their theoretical background (Table 4 summarises expected re-

gression results). As far as lagged price deviation is concerned, we expect

it to give our model partial-adjustment character in scaling estimated coef-

ﬁcient and adjusting signiﬁcance of included fundamental variables. Based

on signiﬁcance of ﬁrst lag in ACF and PACF functions (Appendix, Figure

4), we anticipate dif pt−1 to have large explanatory power in estimation and

strong eﬀect on dependent variable.

Renewable generation depends entirely on weather conditions, hence we

can assume it to be exogeneous random variable. Hagemann and Weber

(2013) concluded that renewable forecast errors act as main source of liquid-

ity on German intraday market for electricity and therefore we anticipate

it to play important role in our estimation for Czech market. Capacit-

ies of both renewable production types remained nearly unchanged from

2015 (ERU, 2016), hence generation as well as forecast error is comparable

throughout the years.

Our hypothesis regarding solar generation forecast error is based on fol-

lowing assumptions and implications. When positive forecast error occurs,

actual solar generation is higher than expected during day-ahead trading,

thus participants will try sell additional electricity from solar generation

units and cause intraday price to decrease as a consequence of sudden ex-

cessive supply. In terms of our dependent variable, positive forecast error

will decrease intraday price, causing price diﬀerence to decrease in value.

For negative forecast error, we can apply reverse logic and assume increase

in intraday price as well as increase in value of price deviation.

Since TSO does not disclose data on day-ahead generation forecast for

wind on Czech market (most likely due to negligible capacity; see Table 1),

we constructed AR(2) model to obtain wind generation forecast as described

in the ﬁrst part of methodology. This allows us to determine forecast error

of wind generation. Negative forecast error is expected to push intraday

prices up, potentially creating short-term supply shortage and causing de-

ployment of additional generation units on right end of merit order curve,

24

while opposite eﬀect is anticipated for positive forecast error. Nonetheless,

we need to bear in mind that wind generation in Czech market might not

appear as signiﬁcant as in other European markets, due to its very limited

capacity.

In our estimation, we will also include load forecast error, as system load

is strongly aﬀected by time of the day and random eﬀects (e.g. weather),

consequently inﬂuencing electricity spot price in deregulated markets (Ag-

garwal et al. 2011). Assuming load is appropriate proxy for supply of elec-

tricity, we can work with load forecast error as variable covering unexpected

movements on supply side of market. We can anticipate price surge in times

of lower load than expected (supply shortage) and price decline for supply

surplus. We assume the same hypotheses as for PV and wind generation,

since they are directly inﬂuencing supply side of electricity. However, load is

inﬂuenced by more aspects than just RES generation (unexpected outages,

export/import, transmission losses, losses in production etc.), therefore the

eﬀect of load error forecast on price deviation is more complex than that of

sole RES generation.

We will consider eﬀect of import and export of electricity on Czech in-

traday price and deviation from day-ahead price. As stated in paper by

Jorgensen and Ropenus (2008) on West Danish electricity market with high

wind penetration, intraday cross border trading is gaining importance, espe-

cially with trend of market coupling. Even though Czech intraday market is

not coupled for now, we will examine impact of cross border ﬂow from and to

North Germany which is known for high number of renewable power plants

and intermittent wind generation. Forecast error in this case is deﬁned as

actual cross border ﬂow minus planned cross border ﬂow with German TSO

50 Hertz, which operates most renewable power plants in North and Eastern

Germany.

We have deliberately chosen neighbour TSO with highest ratio of RES

generation as well as highest ratio of imported electricity to Czech Repub-

lic. For this transmission border, we can test hypothesis that in case of

25

excessive wind generation, 50 Hertz tries to export electricity (positive fore-

cast error) and sell it at Czech intraday market, which consequently pushes

prices down. More traditional hypothesis would assume shortage of elec-

tricity and increased intraday prices on Czech market, which consequently

result in additional import from Germany (which presumably oﬀer cheapest

foreign electricity, depending on RES). However, purpose of the choice of

cross border exchange with 50 Hertz was to test unconventional hypothesis

in the ﬁrst place. Negative forecast error (Czech Republic importing less

electricity from Germany or exporting more electricity than planned) indic-

ates electricity surplus that should lower intraday prices.

Final hypotheses will concern intraday prices behaviour dependent on

day-ahead prices. First, we need to test the signiﬁcance of day-ahead price

in our regression.

If day-ahead price appears to be statistically signiﬁc-

ant variable, we will test hypotheses regarding intraday market response to

extreme prices on day-ahead market. For following analysis, “high” and

“low” day-ahead price variables will be created as day-ahead price times

dummy variable which is 1 if the price is equal to mean day-ahead price

plus/minus two standard deviation of day-ahead price sample and 0 other-

wise. Re-estimation of equation 5 with added “high” and “low” day-ahead

price variables will be performed to examine following hypotheses.

During hours of high demand, such as peak period, day-ahead prices are

generally higher than usual. Due to convex shape of merit order curve, any

additional increase in supply is extremely costly and requires deployment of

production units at right end of merit order. Moreover, in short run such

as intraday market, merit order curve is steeper than in long-run and only

technologies with immediate start-up period can be used e.g. gas turbines,

which are costlier than unused lignite or coal plants. Thus, our hypothesis is

that during high prices periods at day-ahead market, intraday prices will be

very sensitive to additional demand and likely to exceed day-ahead prices.

Low day-ahead prices tend to occur in case of base load production being

suﬃcient for given hour or high RES generation forecast. Assuming that

26

electricity demand does not descend under certain base load level, increase

in demand for electricity on intraday market is more likely than further

decrease in demand. In second case, forecast of extensive RES generation

is more likely to have negative forecast error and result in supply shortage.

Hence, most cases of extremely low day-ahead prices should lead to higher

prices on intraday market.

Moreover, electricity is known to be homogeneous product, thus change

by 1 MW in forecast errors in either direction should result in similar eﬀect

on electricity price. We assume symmetrical eﬀect in terms of magnitude

for positive and negative forecast errors of independent variables. This hy-

pothesis will be tested in a following way.

|βposF E| − |βnegF E| = 0

(6)

Table 4: Hypotheses summary for intraday analysis

Positive FE Negative FE

βposF E<0

βnegF E>0

βposF E<0

βnegF E>0

βposF E<0

βnegF E>0

PV

Wind

Load

50 Hertz border

βposF E<0

βnegF E<0

Day-ahead price

βhighDAp>0

βlowDAp>0

Note: Variables will be additionally tested for symmetry. Day-ahead prices will be

tested in second estimated model

5.3 Day-ahead market

Understanding price behaviour on intraday market, we will analyse inﬂu-

ence and explanatory power of intraday prices on day-ahead market. We

are interested in question whether information about intraday price from

previous trading period signiﬁcantly inﬂuences and helps to explain current

day-ahead price. Signiﬁcance of results of day-ahead price regression on

intraday prices from previous day will be compared to regression on both

intraday and day-ahead prices from previous trading session as explaining

27

variables.

Autocorrelation with lagged price values is suggested by extensive liter-

ature for hourly day-ahead spot price for electricity. Woo et al. (2011) or

Neubarth et al. (2006) used autoregressive model observing impact of wind

power generation on electricity spot market price levels on Texas market

and German power market respectively. AR modelling is considered funda-

mental for econometric analysis of electricity spot prices according to Weron

and Misiorek (2008), Ferkingstad et al. (2011) or Kristiansen (2012). We

will hence use autoregressive model of order p with exogenous variables,

ARX(p). Speciﬁcation of lag length will be determined by examining ACF

and PACF functions of day-ahead prices. In order to preserve information

about dynamics of electricity spot prices, we will not change our dataset

in any way that would inﬂuence results of ACF and PACF functions, when

establishing appropriate number of lagged values.

Both dependent and independent variables will be tested for stationarity

using ADF test for unit root and KPSS test for stationarity of dataset. Since

many of the variables are hourly or daily prices of electricity or commodities,

we expect to reject null hypothesis of stationary data as suggested by numer-

ous literature on electricity prices (Knittel and Roberts, 2005; Escribano et

al., 2011; etc). However, we are still able to obtain valid estimation results

and draw correct inference if model residuals pass both ADF and KPSS test.

When it comes to prices, it is always reasonable to consider logarithmic

transformation and interpret results as elasticity. However, in our case, both

day-ahead and intraday prices are occasionally negative. Since there is no

logarithmic transformation of data for both positive and negative values that

would not distort results or inﬂuence number of chosen lagged values, we will

keep nominal price values for further analysis.

Apart from autoregressive terms in our estimation, denoted in equation

7 as DApt−i and lagged intraday prices, IDpt−j, we will include exogenous

variables aﬀecting electricity spot price, in order to avoid issue of endogen-

eity from omitted variables. RES forecast (PV and wind), load forecast,

28

fossil fuel prices as well as prices of CO2 allowances on spot market are con-

sidered fundamental factors when it comes to electricity spot price (Woo et

al., 2011; Parashiv et al., 2014). Paper by Weron and Misiorek (2008), in

which diﬀerent adjusted AR models on California’s and Nordic spot market

were compared, found evidence that load as an exogenous variable usually

contribute to better performing model for spot prices. Thus, load forecast

available during day-ahead trading will be included. We will denote these

factors as Xrt; r = 1...6. Data on cross border trade ﬂows are intentionally

omitted from our set of exogenous variables as they are often determined or

at least inﬂuenced by spot prices (Ketterer, 2014).

Model will be adjusted for trend and seasonal patterns by adding time

variable t and three sets of seasonal dummies accounting for monthly sea-

sonality - Mkt; k = 1...11 with January as reference; weekly - W endt, dif-

ferencing between weekdays and weekends; and daily seasonality in form of

single peak period from 8 a.m. to 8 p.m. - P eakt, with oﬀ-peak as reference

group.

The estimation model equation for testing intraday price impact on day-

ahead market then looks as follows:

DApt = α + ΣβiDApt−i + ΣγjIDpt−j + ΣδrXrt

+ φt + ΣµkMkt + νW endt + ηP eakt + (cid:15)t

(7)

Normality of residuals will be formally tested by Jarque-Bera test with

null hypothesis of normality. In case of rejection of null hypothesis, we can

still consider estimation asymptotically valid, since we are working with large

sample of hourly observations and attempt to capture as many dependent

variables as possible. Thus, we might assume error term (cid:15)t and model re-

siduals to be asymptotically normally distributed based on a theory behind

Central Limit Theorem (CLT). In case of suspected violation of assumption

of no serial correlation and homoscedasticity in model residuals, recommen-

ded Newey-West HAC estimator will be used again to recalculate robust

standard errors.

After obtaining coeﬃcient estimates and signiﬁcance levels for above de-

29

scribed model, we will add lagged day-ahead prices matching included in-

traday prices hours and re-estimate the model. Our hypothesis for intraday

prices’ signiﬁcance is that they may contain next day spot price information

to limited extent since they are aﬀected by day-ahead prices (as shown in

ﬁrst part of analysis). However, we do not expect them to be statistically

signiﬁcant once lagged day-ahead prices for same hours are added as these

are directly autocorrelated with dependent variable and encompass at least

same information about day-ahead market as lagged intraday prices.

As far as the rest of exogenous factors are concerned, we will brieﬂy

comment on estimated coeﬃcients and discuss reasons for obtained results,

nevertheless we remain focused on intraday price’s impact on day-ahead

market.

30

6 Results and Discussion

In this section, results of empirical analysis following described methodology

will be displayed. Furthermore, presented hypotheses and relations between

variables will be discussed.

6.1 Wind Forecast

First, we need to validate results of our AR(2) wind generation forecast

model. Original estimation of model using dataset of historical values from

January to May 2015 yielded results presented in Table 5:

Table 5: Estimation for wind forecast

Estimate

Std. Error

t-value

p-value

Intercept

wind 1

wind 2
R2

F (3618)

1.5599

1.3532

-0.3746

0.9734

66240

0.2472

0.0154

0.0154

6.3111

87.7842

<0.0001 ***

<0.0001 ***

-24.3050

<0.0001 ***

Adj. R2

p value (F)

0.9734

<0.0001

ADF test

-15.6170

p-value (ADF)

0.01

KPSS test

0.4755

p-value (KPSS)

0.0461

Note: *** signiﬁcance at 1%, ** signiﬁcance at 5%, * signiﬁcance at 10% ; Trend

insigniﬁcant, R-squared with trend included = 0.9734

Having threshold stationary residuals without unit root, we calculated

ﬁrst wind generation forecast for 01.06.2015 00:00 - 01:00 in following way.

ˆwind f ort = 1.5599 + 1.3532wind gent−1 − 0.3746wind gent−2

(8)

After obtaining original estimation and ﬁrst wind generation forecast for

01.06.2015 (91.31 MW), we moved our estimation dataset by one hour, so

that the last sample value would include wind generation from 01.06.2015

00:00 - 01:00 and we could re-estimate wind generation forecast for next hour.

The process was repeated for every hour until 31.05.2017 23:00 - 00:00 based

on the most recent ﬁve months dataset of hourly wind generation, available

prior estimated hour.

31

Calculating wind forecast error using estimated forecast and observing its

descriptive statistics in Table 6, we see interquartile range to be narrow as

well as symmetric and both mean and median to be close to 0. Additionally,

obtained variable passes tests for stationarity, thus we can conclude that our

estimation of wind generation forecast is satisfactory for further application

in analysis.

Table 6: Descriptive statistics of wind FE

Min

1st Qu.

Median

Mean

3rd Qu.

Max

Wind FE

-75.4000

-3.9940

-0.4798

-0.0279

3.8230

59.1100

Std Deviation

8.4584

Skewness

Kurtosis

ADF test

KPSS test

0.1668

7.2744

-24.5090

(0.01)

0.3112

(0.1)

Note: p-values in parentheses, KPSS test for level stationarity

6.2

Intraday market

In order to draw causal inference from our time series dataset, regressions

on time trend and seasonal dummies were performed on all variables. Even

though these features are very common in energy related variables, we did

not expect to ﬁnd them signiﬁcant in price deviation or forecast errors as dif-

ferencing usually eliminates monthly, weekly or daily patterns. With excep-

tion of wind forecast error, both time trend and seasonal dummies appeared

jointly signiﬁcant.

In prices and cross border ﬂow, we observe quadratic

trend.

32

For further analysis, we will use detrended and deseasonalised variables

obtained as residuals of regressions on trend and seasonality. By using re-

siduals, we should also work with more stationary dataset. To conﬁrm this,

ADF test will be performed on all residuals of interest. We are able to re-

ject null hypothesis of unit root in all cases on 99% conﬁdence interval. To

challenge robustness of ADF results and conﬁrm stationary dataset, we will

perform KPSS test for level stationary data as we already treated trend-

ing data. Test managed to not reject null hypothesis of stationary data at

least at 90% conﬁdence interval for all residuals expect for positive German

border ﬂow forecast error.

Conﬁrming stationarity, we can continue to estimate main ARX(1) re-

gression as presented in equation 5, only with residuals to eliminate pos-

sible spurious regression problem and seasonal patterns. Estimated model

is tested for suspected serial correlation and heteroskedasticity. Breusch-

Godfrey LM test conﬁrms presence of serial correlation on 99% conﬁdence

interval. Furthermore, Breusch-Pagan test aﬃrms that variance of error

terms is dependent on independent variables, thus heteroskedasticity is an

issue in our regression. Newey-West HAC estimator is used to compute

robust standard errors. This will widen standard error range and aﬀect

coeﬃcients’ level of signiﬁcance but does not change estimates.

Normality of model residuals is formally tested by Jarque-Bera test, res-

ulting in rejection of null hypothesis of normality at 99% conﬁdence interval.

Since our dataset consists of 17 248 observations, we can assume asymptotic

properties of model and still obtain unbiased estimation. To validate results

of estimation, we need to check stationarity of model residuals. ADF and

KPSS test are conducted and conclude stationary residuals without unit root

at 99% and 90% conﬁdence interval respectively. Table 7 presents results of

regression using Newey-West estimator.

33

Table 7: Regression results for spot price deviation

Estimate

Std. Error

t-value

p-value

Intercept

resdif p 1

resposP V f e

resnegP V f e

resposwindf e

resnegwindf e

resposloadf e

resnegloadf e

resposGERf e

resnegGERf e

resDAp
R2

F(17246)

0.0003

0.7449

-0.0133

0.0132

-0.0212

0.0271

-0.0036

0.0063

0.0005

0.0005

-0.0717

0.6149

2753

0.0879

0.0129

0.0012

0.0015

0.0126

0.0129

0.0005

0.0023

0.0002

0.0013

0.0098

0.0040

57.5850

-11.249

8.740

-1.6780

2.0920

-7.7640

2.7020

2.5540

0.4060

0.9970

<0.0001 ***

<0.0001 ***

<0.0001 ***

0.0933 *

0.0365 **

<0.0001 ***

0.0068 ***

0.0106 **

0.6845

-7.3060

<0.0001 ***

Adj. R2

p-value (F)

0.6146

<0.0001

Breusch–Godfrey test

64.4370

p-value (BG)

<0.0001

Breusch-Pagan test

172.9500

p-value (BP)

<0.0001

Jarque-Bera test

ADF test

KPSS test

983050

-18.5380

0.1208

p-value (JB)

<0.0001

p-value (ADF)

0.01

p-value (KPSS)

0.1

Note: *** signiﬁcance at 1%, ** signiﬁcance at 5%, * signiﬁcance at 10%

As indicated by ACF and PACF functions for price deviation, dif pt−1
is strongly inﬂuencing dependent variable. Furthermore, obtained R2 for

estimated ARX(1) model of 0.6149 indicates signiﬁcant explanatory power

of lagged price deviation. For better perspective, we remove dif pt−1 term,

re-estimate model (full estimation in Appendix, Table 13) and compare ob-

tained R2 to our original estimation. Re-estimated model yields R2 0.0971,

which is in accordance with Hagemann’s paper on German intraday market

(2015), in which he used similar intraday price determinants and chose not

to include autoregressive term. R2 in his estimation was equal to 0.1277

for overall regression and around 0.2 for speciﬁc block periods of a trading

day. Moreover, results of re-estimated model conﬁrms theory that similarly

to electricity spot prices, price deviation of consecutive spot markets is to

34

great extent explained by its lagged values.

Coeﬃcients for solar forecast errors indicate that solar generation is stat-

istically signiﬁcant in intraday market price formation. P-values smaller

than 0.0001 for both forecast errors suggest that intraday market is extens-

ively used to oﬀset solar forecast errors and balance participants’ position.

Since forecast error is 0 during night time, displayed coeﬃcients, estimated

for whole day, are likely to underestimate eﬀect of solar forecast errors during

sunshine and peak hours around noon. Nonetheless, we prove hypotheses

for both PV forecast errors to be valid as unexpected surplus of solar pro-

duction causes intraday prices to decline and the opposite holds for loss of

solar generation.

Sign of wind generation surplus or shortage estimates are in accordance

with our initial expectations as well, thus we can aﬃrm both hypotheses for

wind forecast error. Negative forecast error exhibits slightly bigger impact on

intraday market prices than positive forecast error (although it will be shown

that symmetry cannot be rejected). In other words, for market participants,

cost of covering unexpected lack of wind generation is greater than beneﬁt

of extra wind production. As assumed before, variables turn out to be less

statistically signiﬁcant, with p-value 0.0933 and 0.0365 respectively, which

is mostly caused by negligible importance of wind generation units in Czech

Republic. Nonetheless, we can reject null hypothesis of βresposwindf e and

βresnegwindf e equal to 0 at 10% and 5% signiﬁcance level.

First and foremost, results of load forecast error approve its usage as

electricity supply proxy. In case of supply shortage intraday price and con-

sequently price deviation seems to increase, while supply surplus on intraday

market pushes price deviation down. As data for forecasted and realised
load obtained from ˇCEPS tend to underestimate predicted load in its fore-

cast most of the time, positive forecast error is yielded in more than 91%

of observations. Negative forecast error therefore might be expected to turn

out less signiﬁcant. However, even under Newey-West estimator, negative

forecast error for market load maintains same level of statistical signiﬁcance

35

as positive forecast error and has slightly bigger eﬀect on intraday price in-

crease, proving that shortage of electricity supply in general, not only wind

generation, tends to have larger impact on participants’ behaviour and will-

ingness to pay for balancing their market position.

We have to reject the hypothesis about positive forecast error of 50 Hertz

border ﬂow. This means that Germany is not using Czech intraday mar-

ket on divesting their excessive RES electricity and relation of cross border

electricity ﬂow with German TSO and Czech spot market follows more tra-

ditional scheme. In times of supply shortage, if possible, TSO can decide

to import more electricity from Germany instead of deploying more costly

generation units of last resort. This still results in increase of spot intra-

day price, although the increase is much more subtle than deployment of

balancing generation units.

We cannot reject null hypothesis of lower-tailed test, βresnegGERf e equal

0, even at 90% conﬁdence interval. Thus, we conclude that negative fore-

cast error of cross border ﬂow with 50 Hertz has no signiﬁcant eﬀect on

intraday price and spot price deviation. Since the exchange with 50 Hertz

was purposefully chosen because of its prevailing higher volume of imported

electricity to Czech Republic than is originally scheduled, insigniﬁcance of

negative forecast error could have been anticipated.

As expected, day-ahead price turned out to be extremely signiﬁcant in ex-

plaining intraday price formation. In order to test eﬀect of day-ahead prices

spikes and sinks, we created additional variables highDAp and lowDAp as

described in methodology and treated them for trend and seasonality as

rest of variables. Results of re-estimated model with added highDAp and

lowDAp variables are presented in Table 8.

36

Table 8: Regression results for spot price deviation with DAp spikes and sinks

Estimate

Std. Error

t-value

p-value

Intercept

resdif p 1

resposP V f e

resnegP V f e

resposwindf e

resnegwindf e

resposloadf e

resnegloadf e

resposGERf e

resnegGERf e

resDAp

reshighDAp

reslowDAp
R2

F(17244)

0.0003

0.7445

-0.0134

0.0133

-0.0210

0.0270

-0.0036

0.0061

0.0005

0.0006

-0.0537

-0.0157

0.0064

0.6151

2296

0.0878

0.0129

0.0012

0.0015

0.0126

0.0129

0.0005

0.0024

0.0002

0.0013

0.0118

0.0059

0.0143

0.0040

57.6310

0.9971

<0.0001 ***

-11.3880

<0.0001 ***

8.8690

-1.6660

2.0840

-7.6690

2.5940

2.5530

0.5020

-4.5590

-2.6310

0.4450

Adj. R2

<0.0001 ***

0.0958 *

0.0372 **

<0.0001 ***

0.0095 ***

0.0106 **

0.6158

<0.0001 ***

0.0085 ***

0.6561

0.6148

p-value (F)

<0.0001

Breusch–Godfrey test

64.3520

p-value (BG)

<0.0001

Breusch-Pagan test

173.0900

p-value (BP)

<0.0001

Jarque-Bera test

ADF test

KPSS test

982030

-18.5190

0.1289

p-value (JB)

<0.0001

p-value (ADF)

0.01

p-value (KPSS)

0.1

Note: *** signiﬁcance at 1%, ** signiﬁcance at 5%, * signiﬁcance at 10%

Residuals of regression were conﬁrmed to be stationary without unit root

by ADF and KPSS test and Newey-West estimator was used again to recal-

culate robust standard errors as Breusch-Godfrey and Breusch-Pagan test

indicated serial correlation and heteroskedasticity.

We previously discussed that load forecast error is in most cases positive,

hence excessive supply is much more likely to occur than further demand

spike during extremely high day-ahead prices. As a result, intraday prices

tend to decline in case of high day-ahead prices, which is in accordance

with results for load forecast error. Furthermore, incorrectly underestimated

RES forecasts causing high day-ahead prices and excessive RES supply on

37

intraday market are in line with estimated coeﬃcient for highDAp as well.

Therefore, we reject our original hypothesis about high day-ahead prices’

eﬀect on intraday market.

We conclude that low day-ahead price has no eﬀect on spot price de-

viation as we cannot reject null hypothesis βresnegGERf e equal 0 of upper

tailed test, even at 90% conﬁdence interval. Such result suggests that intra-

day prices neither tend to decrease under base load price level, nor bounce

back to higher intraday prices as a consequence of low prices on day-ahead

market. Occurrence of negative intraday prices is therefore more likely to

be explained by intense deviation of forecasted and realised values of fun-

damental drivers of intraday market and by unexpected severe decrease in

demand for electricity. The latter case shows that base load generation units

does not have self-suﬃcient ramping down mechanisms and causes TSO to

artiﬁcially lower intraday price to incentivise certain participants to negat-

ively balance market (Agora report, 2014).

Overall, we can conclude that price extremes on intraday market does

not occur in succession on day-ahead spikes and sinks, but tend to be result

of extreme forecast errors of intraday determinants.

Estimation of included variables conﬁrms symmetric eﬀect of opposite

forecast errors on homogeneous product such as electricity. Even though,

we see negative forecast errors to have slightly larger impact on prices than

positive forecast errors e.g. in case of wind and load, this diﬀerence seems to

be marginal and coeﬃcients for opposite forecast errors in general appear to

be symmetric. Formal two-tailed tests are conducted to explore hypotheses

based on equation 6. Null hypothesis assuming coeﬃcients’ symmetry is

not rejected for any tested variable (p-values of F statistics in Table 9).

Symmetry is conﬁrmed even in case of highDAp and lowDAp, for which we

did not expect to ﬁnd any.

Table 9: Results of symmetry hypotheses

PV FE Wind FE Load FE 50 Hertz FE DAp extremes

p-value (F)

0.9814

0.6916

0.3853

0.9269

0.5738

38

6.3 Day-ahead market

For our day-ahead price analysis, ﬁrst, appropriate order p in our ARX(p)

model needs to be determined. Based on drawn ACF and PACF functions

for day-ahead prices (Figure 1), it seems that prices for two previous hours

greatly inﬂuence current day-ahead price. Furthermore, lagged prices from

previous day appears to be signiﬁcant in explaining day-ahead price. The

latter observation suggests that hypothesis for day-ahead and intraday price

inﬂuence from previous day might be valid theory to test.

Figure 1: ACF and PACF functions of day-ahead price

In accordance with ﬁnding of Kristoufek and Lunackova (2013), results

of ADF and KPSS test reject null hypothesis of unit root and conclude non-

stationarity of day-ahead prices, both on 99% conﬁdence interval. Similar

results were obtained for rest of variables, with unit root being rejected

for every variable and stationarity not rejected only in case of wind forecast.

Since our primary goal is to explain spot market relation and price dynamics,

we will not opt for using ﬁrst diﬀerences in order to treat non-stationary

dataset. For the same reason, trend and seasonality will be included in ﬁnal

regression and will not be treated separately for each variable as in the case

of intraday price analysis. As mentioned in methodology, our estimation

and ﬁndings will be valid, only if residuals of regression will be stable over

time and pass tests for not containing unit root and being stationary.

Estimation based on equation 7 for day-ahead market yielded results

presented in Table 10. Newey-West HAC estimator is again adopted, based

on results of Breusch-Godfrey and Breusch-Pagan test.

39

Table 10: Regression results for day-ahead price with lagged intraday prices

Estimate

Std. Error

t-value

p-value

Intercept

DAp 1

DAp 2

P V

wind

load

gas

coal

co2

IDp 24

IDp 25
R2

F(17208)

-16.1900

1.1330

1.3590

0.0249

-0.3624

0.01699

0.0002

0.0014

0.0001

0.0658

0.0185

0.1430

0.0077

0.0072

-0.0031

-0.0129

0.0023

0.1470

0.0191

0.2169

0.0576

-0.0593

0.9266

9049

-11.9070

<0.0001 ***

45.5260

-21.3260

-17.4990

-9.4210

17.8640

2.2340

1.0310

1.5160

7.4940

<0.0001 ***

<0.0001 ***

<0.0001 ***

<0.0001 ***

<0.0001 ***

0.0255 **

0.3026

0.1294

<0.0001 ***

-8.2110

<0.0001 ***

Adj. R2

p-value (F)

0.9265

<0.0001

Breusch–Godfrey test

342.1300

p-value (BG)

<0.0001

Breusch-Pagan test

981.6000

p-value (BP)

<0.0001

Jarque-Bera test

ADF test

KPSS test

218210

-11.6340

0.0699

p-value (JB)

<0.0001

p-value (ADF)

0.01

p-value (KPSS)

0.1

Note: *** signiﬁcance at 1%, ** signiﬁcance at 5%, * signiﬁcance at 10%

Full estimate with trend and seasonal dummies can be found in appendix, Table 14

Even though Jarque-Bera test strongly reject null hypothesis of normality

in regression residuals, results of ADF na KPSS test conﬁrm asymptotically

valid estimation output by rejecting unit root and not rejecting stationary

residuals.

Hypothesis about previous trading day intraday prices is conﬁrmed as p-

value for both intraday price included is lower than 0.0001. Thus, we know

that intraday price aﬀect next day’s spot price, but for now, we cannot say

whether it is because of information from day-ahead market that is passed

on intraday price or intraday market itself is signiﬁcant factor inﬂuencing

day-ahead price. For that reason, we will add lagged day-ahead prices from

previous trading day and re-estimate regression (Table 11) to see whether

40

intraday prices loses certain level of signiﬁcance.

Table 11: Regression results for day-ahead price with lagged intraday and day-ahead

prices

Estimate

Std. Error

t-value

p-value

Intercept

DAp 1

DAp 2

P V

wind

load

gas

coal

co2

IDp 24

IDp 25

DAp 24

DAp 25
R2

F(17206)

-13.1600

1.0550

-0.2522

-0.0024

-0.0104

0.0019

0.1314

0.0152

0.1667

0.0159

-0.0169

0.3290

-0.3261

0.9353

9563

1.3080

0.0196

0.0141

0.0002

0.0012

0.0001

0.0544

0.0153

0.1193

0.0043

0.0047

0.0210

0.0169

-10.0610

<0.0001 ***

53.7860

-17.9230

-12.8290

-8.6090

14.2740

2.4180

0.9950

1.3970

3.6970

-3.5830

15.6450

<0.0001 ***

<0.0001 ***

<0.0001 ***

<0.0001 ***

<0.0001 ***

0.0156 **

0.3196

0.1625

0.0002 ***

0.0003 ***

<0.0001 ***

-19.3020

<0.0001 ***

Adj. R2

p-value (F)

0.9352

<0.0001

Breusch–Godfrey test

163.3200

p-value (BG)

<0.0001

Breusch-Pagan test

954.0800

p-value (BP)

<0.0001

Ljung-Box test

Jarque-Bera test

ADF test

KPSS test

680.1200

267890

-15.6070

0.0673

p-value (LB)

p-value (JB)

<0.0001

<0.0001

p-value (ADF)

0.01

p-value (KPSS)

0.1

Note: *** signiﬁcance at 1%, ** signiﬁcance at 5%, * signiﬁcance at 10%

Full estimate with trend and seasonal dummies can be found in appendix, Table 15

Newey-West estimator was used to treat persistent issue with residuals’

serial correlation and heteroskedasticity. Residuals were again conﬁrmed to

be stationary without unit root by ADF and KPSS test. Furthermore, addi-

tional Ljung-Box test, together with ACF and PACF functions of regression

residuals are performed and plotted. Ljung-Box test conﬁrmed persistent

autocorrelation in residuals as we would need to include up to 29 lagged val-

41

ues to account for whole autoregressive properties, based on original ACF

and PACF functions. Nevertheless, presented model managed to capture

most signiﬁcant autoregressive components and determined clear relation

between day-ahead and lagged intraday prices, which was our primary ob-

jective.

In Figure 2, obtained ACF and PACF functions of residuals are

presented to further inspect how satisfactorily was autoregressive feature of

day-ahead prices accounted for in estimation.

Figure 2: ACF and PACF functions of day-ahead price model residuals

Based on a result of re-estimated regression, we can conclude that intra-

day prices are proved to be inﬂuential factor of next trading day electricity

spot price on Czech power market. As expected, day-ahead prices from pre-

vious trading day appears to aﬀect spot price in stronger magnitude than

intraday prices. Even though, much of the impact of intraday prices in ori-

ginal estimation was caused by omitting day-ahead prices, intraday prices

preserved same level of statistical signiﬁcance, with p-value equal to 0.0002

and 0.0003 respectively.

Furthermore, in both estimations, we observe that both day-ahead and

intraday prices from previous trading day have opposite symmetrical eﬀect.

Such results indicate that when dependence on historical prices will shift spot

price strongly in one direction, dependence on consecutive historical value

will drive shift in opposite direction, back to original, potentially mean value

(unless the price is negative). These results support theory of mean-reverting

electricity spot price, which was previously conﬁrmed for Czech electricity

42

market by Kristoufek and Lunackova (2013). Moreover, symmetrical coeﬃ-

cients do not appear in most recent lagged prices, but rather as the eﬀect of

prices from previous day. This suggest that mean-reverting property does

require certain amount of time to aﬀect Czech electricity spot price.

Observing results for rest of exogenous factors, we can conclude that

ﬁndings are in accordance with majority of the relevant literature. In both

estimations, RES forecast for both solar and wind pushes day-ahead prices

down with more expected RES generation.

In contrast, load forecast be-

ing supply proxy, drive day-ahead prices up, with larger supply causing

deployment of costlier generation unit on right end of merit order curve.

As expected, increase in prices of primary energy sources and emission al-

lowances cause electricity spot price to rise. Statistical signiﬁcance of these

variables is naturally anticipated to be lower on spot market than that of

RES and load forecast. Since coal and other base load fossil fuels are mostly

traded in futures contract or bilaterally via forwards, their insigniﬁcance in

explaining electricity day-ahead price is in line with our expectation (we

also have to bear in mind that coal future price serves only as reference for

base load fossil fuel generation units’ production costs). Slightly unexpected

result is not rejecting null hypothesis of upper-tailed test for βco2 equal to

0 and consequent insigniﬁcance of emission allowance prices. This might

be caused by very low trading prices (median value in two year dataset is

5.580 EUR/t and maximum is 8.630 EUR/t), which do not force emitters to

consider allowance price as signiﬁcant deciding factor. We should also bear

in mind that most polluting electricity sources are not primarily traded on

spot market.

To assess goodness of ﬁt of the model and justify chosen exogenous vari-

ables, we need to perform additional regressions. First, we need to eliminate

trend and seasonality in dependent variable in order to observe what per-

centage of detrended and deseasonalised price is explained by chosen factors.

Residuals of purged day-ahead prices are regressed on exogenous variables

and lagged intraday prices as shown in equation 9.

43

resDApt = α + β1IDpt−24 + β2IDpt−25 + ΣβrXrt + (cid:15)t

(9)

If intraday prices are removed from estimation, we can observe true ex-

planatory power of additionally chosen independent factors on Czech elec-

tricity day-ahead prices. Diﬀerence in R2 of the ﬁrst two estimations from

Table 12 reveals, by what percentage, inclusion of intraday prices improves

explanatory power of independent variables. Regression of residuals on in-

traday prices in third column then shows percentage of day-ahead prices

explained by sole intraday prices from previous trading session.

Table 12: Explanatory power of independent factors in DAp regression

IDpt−24 + IDpt−25 + ΣXrt

ΣXrt

IDpt−24 + IDpt−25

R2
Adj. R2

0.3125

0.3122

0.2660

0.2658

0.1454

0.1453

Note: Full estimation output of these partial regressions can be found in appendix,

Table 16,17,18

44

7 Conclusion

In this thesis, we have inspected Czech intraday market for electricity. After

a quick overview of relevant literature and Czech power market, notably

Czech spot market, in analytical part of the thesis, we focused on examining

electricity intraday price formation process and later on intraday price’s

impact on next trading day’s day-ahead price. Analysis was conducted on

two-year dataset from June 2015 to May 2017 as ﬁrst ﬁve months of 2015

were used for wind generation forecast estimation.

In the ﬁrst section of analytical part, we concentrated on price formation

on intraday market by explaining deviation between intraday and day-ahead

prices by fundamental variables’ forecast errors in ARX(1) time series model.

Expected eﬀects on intraday prices were conﬁrmed in case of RES and load

forecast errors, supporting price increasing impact in case of unexpected

supply shortage and decreasing prices when actual supply exceeds forecast

values. Solar, together with load forecast error appear to be most statist-

ically signiﬁcant determinants of intraday price deviation from day-ahead

price, although the size of their eﬀect on intraday market is subtler than

wind’s. We inferred that persistently greater import of electricity from Ger-

many than planned can subtly increase spot intraday prices. Nonetheless,

50 Hertz seems to be the most rational choice of neighbour TSO to import

from because of high RES generation, which is precisely forecasted during

intraday trading and consequent most competitive price.

We managed to dispute occurrence of extreme intraday prices as a con-

sequence of price spikes on day-ahead market. We conclude that negative

prices on intraday market are more result of not foreseen intense RES sur-

plus or negative demand shocks, but are not connected to low or negative

day-ahead prices. Furthermore, in accordance with homogenous properties

of electricity, symmetry of forecast errors’ eﬀects on intraday market was

conﬁrmed for all observed variables.

In the second part of the analysis, we managed to establish relation

between electricity day-ahead and intraday market and conﬁrm impact of

45

intraday prices on next day’s day-ahead price. Compared to included autore-

gressive components of day-ahead price, intraday prices have rather subtle

eﬀect on next trading period’s day-ahead prices, in terms of coeﬃcients’

magnitude. Nevertheless, empirical analysis showed that intraday prices are

statistically signiﬁcant even with day-ahead prices included in model estim-

ation and that including intraday prices in estimation have non-negligible

impact on its R2. Moreover, results supported mean-reverting properties

of electricity day-ahead prices on Czech power market. Eﬀect of remaining

factors in estimation were in accordance with our expectations and extensive

previous research results, with PV, wind and load forecasts having crucial

signiﬁcance on day-ahead market.

Additional research on intraday market might be interested in exploring

merit order eﬀect on intraday market. However, this study would need to

take place in countries with signiﬁcant RES production and well-established

intraday market, such as Germany or North European countries. Addition-

ally, further intercorrelation of power markets in Czech Republic remains

topic for future investigation. Apart from price, more areas of interest might

be inspected, such as power markets’ volatility.

It could be also tested,

whether connections between markets have any additional value in forecast-

ing markets for electricity.