Contents lists available at ScienceDirect

Energy Policy

journal homepage: http://www.elsevier.com/locate/enpol

Liquidity costs on intraday power markets: Continuous trading
versus auctions

Thomas Kuppelwieser , David Wozabal *

TUM School of Management, Technical University of Munich, Arcisstraße 21, 80333, Munich, Germany

A R T I C L E  I N F O

A B S T R A C T

Keywords:
Continuous market
Auction market
EPEX SPOT
GME MI
Double machine learning

We analyze liquidity costs on continuous and auction-based intraday power markets using a cost-of-round-trip
measure that works for both market designs. We use data from the Italian auction-based intraday market and
the  German  continuous  market  and present  descriptive  statistics  as  well  as  multivariate  regression  models  to
analyze determinants of liquidity costs in both markets. To test for differences in liquidity due to market design,
we employ a double machine learning technique controlling for several confounding variables. We show that
weekly  patterns,  yearly  seasonality, electricity  demand,  as  well  as  the  influence  of  temperatures  significantly
affect liquidity costs. Comparing liquidity costs in both market, we find that, overall, liquidity costs are lower on
the  Italian  market.  However,  Italian  costs  increase  towards  later  auctions,  while  the  costs  on  the  German
continuous intraday market decrease and reach their low close to physical delivery, where costs are lower than
on the last Italian market trading the corresponding products.

1. Introduction

In the last two decades electricity markets world-wide have moved
from  being  dominated  by  highly  vertically  integrated  monopolies  to
competitive markets populated by many diverse players. To satisfy these
companies’  requirements,  electricity  trading  takes  place  in  multi-
settlement  markets  that  allow  trading  products  with  different  tempo-
ral granularities and with different times to maturity. In particular, the
growing  share  of  variable  renewable  production  led  to  the  rising
importance of spot markets, making it possible to adapt traded positions
until close to delivery as new information arrives.

While in the US the day-ahead market is immediately followed by the
real-time balancing market (Ela et al., 2014), European market designs
feature  a  spot  market  that  is  split  into  a  day-ahead  market  and  an
intraday market where power can be traded until shortly before physical
delivery. Currently, there are two prevailing designs of intraday markets
in Europe. While most European countries use continuous trading, Italy,
Spain, and Portugal mainly use staggered intraday market auctions.

Clearly,  the  benefits  of  intraday  trading  are  closely  tied  to  the
liquidity of the market, i.e., the ability of firms to trade while experi-
encing only minimal adverse price effects. Furthermore, liquid markets
are less prone to market manipulation and gaming by pivotal players.

However,  liquidity  in  most  European  intraday  markets  remains

rather  low.  Weber  (2010)  finds  that markets  in  Germany  and  several
other European countries are not sufficiently liquid. Garnier and Madl-
ener (2015) conclude that due to this illiquidity, current intraday mar-
kets are of limited use in balancing short-term forecast errors in demand
and variable renewable production. It is therefore interesting to policy
makers  and  industry  professionals  alike  to  identify  factors  that  drive
liquidity  in  the  two  market  designs  and  understand  how  the  designs
themselves influence liquidity.

Consequently, the issue of liquidity in intraday markets has recently
attracted some attention in the academic literature. Weber (2010) an-
alyzes  the  integration  of  wind  energy  considering  different  European
market designs and finds that the intraday auctions in Spain are the most
attractive in terms of trading volume. Based on transaction data from the
German  intraday  market,  Hagemann  and  Weber  (2013)  investigate
liquidity  in  intraday  power  markets  using  established  measures  from
financial markets. Neuhoff et al. (2016) find that the additional auctions
for 15 min contracts in the German intraday markets increased liquidity
and market depth while reducing price volatility.

Balardy (2018) is one of the first, who uses the German limit order
book  (LOB)  data  to  analyze  liquidity  in  terms  of  bid-ask-spreads  and
market  depths.  The  author  finds  a  positive  relation  between  bid-ask
spreads and risk as well as a negative relation between bid-ask spread
and  adjustment  needs,  activity,  and  competition  in  the  market.  von

* Corresponding author.

E-mail addresses: thomas.kuppelwieser@tum.de (T. Kuppelwieser), david.wozabal@tum.de (D. Wozabal).

https://doi.org/10.1016/j.enpol.2021.112299
Received 11 March 2020; Received in revised form 28 March 2021; Accepted 6 April 2021

EnergyPolicy154(2021)112299Availableonline19April20210301-4215/©2021ElsevierLtd.Allrightsreserved.T. Kuppelwieser and D. Wozabal

Luckner  et  al.  (2017)  use  the  LOB  to  find  an  optimal  market  maker
pricing and analyze the market order intensity and the bid-ask spread.
Hagemann  and  Weber  (2015)  analyze  intraday  trading  volumes  on
auction-based  and  continuous  intraday  markets,  and  observe  higher
volumes on the auction-based intraday markets. The authors conclude
that  this  difference  is  not  due  to  the  difference  in  market  design  but
rather due to idiosyncratic factors affecting the two markets.

The literature on electricity forecasting is in many ways related to
our paper. Most models for price forecasts are time-series models using
exogenous  variables,  some  of  which  we  also  use  in  our  models.  For
example, as in Narajewski and Ziel (2020) and Uniejewski and Weron
(2018), we use time dummies for Saturday, Sunday and Monday, and
the  day-ahead  forecast  for  load,  solar  production  and  wind  power  as
covariates in our regression models. Marcjasz et al. (2020) use dummies
for  each  weekday,  forecasts  for  load,  solar  production  and  wind  pro-
duction  and  its  forecast  errors,  and  balancing  volumes.  Janke  and
Steinke (2019) use the forecastFs of demand and renewable production,
and hourly dummies for each hour.

Despite the importance of the topic, the literature analyzing liquidity
costs  in  intraday  power  markets  remains  scarce.  To  the  best  of  our
knowledge, this is the first paper to compare liquidity costs of the two
markets in a statistically sound way using the complete order book data
of  the  continuous  intraday  market  and  all  submitted  orders  of  the
intraday auction.

In this paper, we contribute to the discussion by the first analysis of
intraday electricity market liquidity that is based on a cost-of-round-trip
(CRT) measure which captures all quantitative aspects of liquidity both
in  auction  markets  as  well  as  for  continuous  trading.  We  provide  a
univariate  analysis  of  the  CRT  which  is  complemented  by  regression
models that explore possible drivers of liquidity costs on the German and
Italian market. We find that, depending on the market, liquidity cost are
driven by weekly patterns, yearly seasonalities, electricity demand, as
well as temperatures.

To directly compare the cost of liquidity and thus measure the impact
of  market  design,  we  use  a  state-of-the-art  double  machine  learning
method proposed in Chernozhukov et al. (2018) controlling for possible
confounding factors identified in the analysis for the CRT for the two
markets.  Comparing  the  two  markets,  by  and  large  the  Italian
auction-based market exhibits lower CRTs. We observe this result in a
univariate analysis and confirm it in a multivariate analysis controlling
for the confounding factors identified above. However, this effect gets
progressively  weaker  for  larger  traded  volumes  and  as  trading  time
approaches physical delivery. In particular, it can be observed that the
German continuous intraday market consistently exhibits lower costs for
high volumes close to delivery.

Our  findings  suggest  that  a  combination  of  several  auction-based
intraday  markets  with  continuous  trading  might  be  able  to  leverage
the benefits of both systems. In particular, auctions can be used to in-
crease liquidity and therefore decrease trading costs by pooling orders
for  products  which  are  far  from  delivery.  These  auctions  could  be
complemented by continuous trading close to delivery, where market
participants have the opportunity to trade the forecast errors for demand
and  variable  renewable  production  at  a  point  in  time  when  accurate
forecasts  are  available  (see  Ocker  and  Jaenisch,  2020,  for  a  similar
proposal).  In  fact,  Spain  already  implemented  such  a  hybrid  system
when it joined the cross-border intraday market project XBID in June
2018. This proposal is close to the literature on optimal implementations
of the European target model for a single coupled intraday market as laid
out in the European Commission Regulation (EU) 2015/1222. Bellen-
baum  et  al.  (2014)  discuss  different  intraday market  designs  meeting
these requirements and come to the conclusion, that a hybrid between
continuous trading and auctions potentially combines the advantages of
both designs. Similarly, Ehrenmann et al. (2019) propose to add addi-
tional  auction  markets  to  the  existing  continuous  market,  as  auction
markets are more suitable for small market participants. The authors see
a clear advantage of this setting, but the question remains at which time

of the day to introduce auction markets and how many. A possible so-
lution  that  leverages  the  advantages  of  both  continuous  trading  and
auctions is to have a large number of frequent auctions as proposed in
Budish et al. (2015) for financial markets and in Deutsche B¨orse Group
(2018)  for  the  intraday power  market. Such  a  design  would  alleviate
some of the problems of continuous trading while still providing market
participants with ample opportunities to trade.

The paper is organized as follows. In Section 2, we briefly describe
the Italian and German intraday markets. Section 3 describes the market
data and our set of explanatory variables. In Section 4, we introduce the
cost-of-roundtrip measure and specify the econometric models used to
determine the factors driving liquidity costs in both markets as well as
the application of double machine learning, which we use to determine
the  effect  of market  design  on liquidity  costs.  Section  5 discusses  the
empirical results. Finally, Section 6 concludes, discusses limitations and
policy implications.

2. Background: market designs in Germany and Italy

In this short section, we discuss the relevant facts about the Italian
auction-based intraday market and then proceed to discuss the German
continuous intraday market. We collect key characteristics of the two
markets for the year 2018 from ENTSO-E (2019); GME (2019); Burger
(2019) in Table 1, and calculated the Italian weighted prices based on
the national price. Note that the traded volumes of the day-ahead market
and  the  intraday  market  of  hourly  products  of  the  two  markets  are
comparable. Consumption and production of renewables are higher in
Germany, and Italy is a net importer of electricity while Germany gen-
erates high volumes for export, since it has significant overcapacities in
cheap base-load production. As a result, average spot market prices in
Germany are lower than in Italy.

2.1. The Italian IPEX

The Italian spot market offers a platform to trade electricity for de-
livery  in  hourly  granularity.  The  day-ahead  market  in  Italy  closes  at
noon  on  the  day  before  delivery  and  is  followed  by  seven  intraday
auction  markets,  called  MI  (mercato  infragiornaliero).  Bid  prices  are
constrained between €0 and €3000 while bid quantities are restricted to
multiples of 1 kWh. For more details see GME (2016).

The  Italian  power  grid  consists  of  the  six  market  zones  NORD,
CNORD, CSUD, SUD, SICI, and SARD. The MI markets are organized as
uniform price auctions that aggregate the bids of all zones. The left plot in
Fig. 1 shows the cleared volume and the clearing price of an exemplary
market session. If the resulting national market outcome is physically
infeasible due to lack of transmission line capacities between the zones,
the result is made feasible by altering the market outcome resulting in
different  zonal  prices  for  the  different  Italian  market  zones.  For  our
analysis,  we  disregard  this  complication,  by  only  considering  the  na-
tional  price,  which  considers  all  submitted  offers  without  taking  into
account the effects of transmission limits between zones.

Table 1
Summary of annual key characteristics of the two markets for 2018. The German
day-ahead volume includes Austria and Luxembourg and the trading volume for
the German continuous market is restricted to hourly products.

Quantity

Consumption (TWh)
PV infeed (TWh)
Wind infeed (TWh)
Imports (TWh)
Exports (TWh)
Day-ahead trading volume (TWh)
Intraday trading volume (TWh)
Volume weighted day-ahead price (€/MWh)
Volume weighted intraday price (€/MWh)

Italy

322.2
22.9
17.3
47.1
3.3
212.9
25.4
62.22
61.05

Germany

538.1
41.2
107.2
31.5
82.7
234.5
37.8
43.26
46.6

EnergyPolicy154(2021)1122992T. Kuppelwieser and D. Wozabal

Fig. 1. Clearing of the Italian MI3 intraday auction (left) and German continuous trading for the 13th h on the 15.04.2018. The yellow marker on the left signifies the
uniform clearing price of the auction. The markers on the right represent price ticks, i.e., instances when orders were cleared in the German market. (For inter-
pretation of the references to color in this figure legend, the reader is referred to the Web version of this article.)

Table 2 summarizes the characteristics of the Italian intraday mar-
ket. The lead-time, defined as the time between the last possibility to
trade the specific product and its physical delivery, range from 4.25 to
10.5 h. Since wind power forecasts significantly improve approaching
delivery (e.g., Hannele Holttinen, 2013), this relatively long lead-time
make  it  hard  to  incorporate  the  last  and  therefore  most  precise  pro-
duction forecasts.

2.2. The German EPEX SPOT market

The German day-ahead market closes at noon of the previous day
and is followed by an auction for quarter-hours of the next day at 3 p.m.
and a continuous intraday market. For a detailed description we refer to
the operational rules in EPEX (2019) and to Table 2 for a summary of
trading times.

In contrast to the Italian MI markets, the German intraday market is
based on continuous trading with a limit order book (LOB) much like in

2-hour and 1

financial markets. Next to hourly products 1
4-hour products
are  traded.  We  do  not  include  these  products  in  our  analysis,  since
shorter  deliveries  serve  different  purposes  than  hourly  products.  In
particular, firms use sub-hourly products to model the ramps of their
production or consumption, which is possible only to a small extent with
hourly  products.  To  be  comparable  to  the  Italian  market,  isolate  the
effect of market design on liquidity, and avoid diluting our analysis by
mixing in different aspects, we therefore only consider hourly products
in our analysis. The market for a specific product closes 30 min (or 5 min
within the control area) before delivery, which facilitates trading fore-
cast errors of fluctuating renewable energy sources.

Market participants can submit buy and sell offers for prices ranging
between  (cid:0) 9999.9€/MWh and 9999.9€/MWh, with a minimum bid size
of 0.1 MWh, and several specified order types (Martin et al., 2018). A
submitted bid/offer is cleared immediately if the price is better than the
best price of an offer/bid in the LOB. If there is no such matching order,
the new order is stored in the LOB and matched with orders arriving at a

Table 2
Operating times of the German and the Italian intraday markets. The table reports the traded products, the opening and closing times of the markets (d-1 indicating a
time on the day before delivery), the time when the results are announced, the list of products that are traded the last time on the respective market, as well as the lead
time for the products that are traded the last time. H indicates a hourly product, HH stands for half-hour and QH for a quarter-hourly product while D signifies the time
of delivery.

Market

Products

Opening

Closing

Results

Last Update

Lead-Time (h)

Italian Markets
MI1

MI2

MI3

MI4

MI5

MI6

MI7

German Markets
Intraday Auction

Continuous H

Continuous QH

Continuous HH

H1 (cid:0) H24
H1 (cid:0) H24

H5 (cid:0) H24

H9 (cid:0) H24

H13 (cid:0) H24

H17 (cid:0) H24

H21 (cid:0) H24

QH1 (cid:0) QH96
H1 (cid:0) H24

QH1 (cid:0) QH96

HH1 (cid:0) HH48

12:55 (d-1)

12:55 (d-1)

15:00 (d-1)

16:30 (d-1)

15:30 (d-1)

17:00 (d-1)

17:30 (d-1)

23:45 (d-1)

00:15 (d)

17:30 (d-1)

17:30 (d-1)

17:30 (d-1)

17:30 (d-1)

d-45

15:00 (d-1)

16:00 (d-1)

15:30 (d-1)

3:45 (d)

7:45 (d)

11:15 (d)

15:45 (d)

15:00 (d-1)

′
D-5

′
D-5

′
D-5

4:15 (d)

8:15 (d)

11:45 (d)

16:15 (d)

15:10 (d-1)
–

–

–

–
H1 (cid:0) H4

H5 (cid:0) H8

H9 (cid:0) H12

H13 (cid:0) H16

H17 (cid:0) H20

H21 (cid:0) H24

–
H1 (cid:0) H24

QH1 (cid:0) QH96

HH1 (cid:0) HH48

–

7

4

4

4

4

4

1
2
1
4
1
4
1
4
3
4
1
4

up to 10

1
2

up to 7

up to 7

up to 7

up to 7

up to 7

1
4
1
4
1
4
3
4
1
4

–

5
60
5
60
5
60

EnergyPolicy154(2021)1122993T. Kuppelwieser and D. Wozabal

later point in time. The right plot in Fig. 1 shows the best available bid
and ask price over time with each tick representing a match between a
newly placed order and an order in the order book generating a trade.

3. Data

In  Section  3.1,  we  discuss  the  market  data  which  we  use  for  the
Italian and German intraday market. In Section 3.2, we introduce vari-
ables which we use in Section 4 and Section 5 as controls in our com-
parison of the two market designs.

3.1. Market data

All offers submitted to the Italian intraday market are available on
the  website  of  the  Italian  Power  Exchange  (IPEX).  The  offers  contain
information about the side (sell or buy), product/hour, intraday market
(MI1-MI7),  zone,  price  and  volume  and  can  be  used  to  calculate  the
national price.

The  LOB  of  the  German  continuous  intraday  market  can  be  pur-
chased from EPEX SPOT SE. The data-set includes information about the
side (sell or buy), product/hour, validity period, control area, as well as
the  price  and  volume  of  every  submitted  bid/offer.  We  note  that  the
EPEX allows for the submission of so called iceberg orders, for which the
bid quantity is only gradually revealed as parts of the order get executed.
We  only  consider  those  parts  of  iceberg  orders  that  were  actually
executed in our analysis. For more information about the LOB-data we
refer to Martin et al., 2018.

The German intraday trading system was subject to frequent changes
in the recent years with effects on market liquidity, especially shortly
before delivery. In order to have a dataset with consistent market rules,
we restrict our analysis of both markets to the time from 20.11.2017, a
few days after the trading system M7 (version 6.0) was launched to the
15.06.2018, when the XBID project was introduced.

Table 3
Overview of data used in the analysis.

Variable

Frequency

Unit

Source

RS,I

t

FS,I

t

RW,I

t

FW,I

t

RD,I

t

FD,I

t

RS,G

t

FS,G

t

RW,G

t

FW,G

t

RD,G

t

FD,G

t

Dt
TI
t

TG
t

Wt

Italian solar
production
Italian solar forecast

Italian wind
production
Italian wind forecast

hourly

MWh

hourly

MWh

hourly

MWh

hourly

MWh

Italian demand

hourly

MWh

Italian demand
forecast
German solar
production
German solar
forecast
German wind
production
German wind
forecast
German demand

German demand
forecast
Daylight of Munich

Temperature of
Milan
Temperature of
Berlin
Weekends

hourly

MWh

-hourly

-hourly

-hourly

-hourly

1
4
1
4
1
4
1
4
1
4
1
4
daily

-hourly

-hourly

hourly

hourly

MWh

MWh

MWh

MWh

MWh

MWh

days
∘

C

∘

C

daily

Boolean

–

https://transparency.
entsoe.eu
https://transparency.
entsoe.eu
https://transparency.
entsoe.eu
https://transparency.
entsoe.eu
https://transparency.
entsoe.eu
https://transparency.
entsoe.eu
https://transparency.
entsoe.eu
https://transparency.
entsoe.eu
https://transparency.
entsoe.eu
https://transparency.
entsoe.eu
https://transparency.
entsoe.eu
https://transparency.
entsoe.eu
https://galupki.de

www.arpalombardia.it

www.dwd.de

3.2. Explanatory variables

Table 3 provides an overview of the variables which potentially have
an impact on the CRT and which we control in our comparison of the
two market designs in Section 5.

Motivated by Goodarzi et al. (2019); Kulakov and Ziel (2020) who
show  that  forecast  errors  in  renewable  production  influence  intrady
prices  and  by  Balardy  (2018)  who  observes  an  impact  of  renewable
energy  sources  on  bid-ask  spreads,  we  include  data  on  forecasts  and
actual  production  of  variable  renewables  in  both  countries.  Since  we
exclusively analyze hourly products, we consider the average over the
four  quarter-hourly  quantities  to  obtain  hourly  values.  We  use  the
day-ahead forecasts for renewable production as published by ENTSO-E.
While the forecasts used by individual market participants for trading
might be different, we think that the chosen forecast captures the overall
sentiment of the market well.

t  and Germany CG

Temperature influences power markets, because power is used for
temperature regulation of buildings. Hence, we introduce a heating- and
a cooling-function as described in Fan and Hyndman (2012) for Italy and
Germany. The cooling function of Italy CI
t  are defined
as max(Tt (cid:0) 19.5∘C, 0), where Tt  is the hourly temperature at time t in
Italy  (Milan)  or  Germany  (Berlin).  Analogously,  we  introduce  the
t  as min(Tt (cid:0) 17.5∘C, 0).
heating function for Italy HI
The choice of the two cities as temperature proxies is motivated by the
fact that Milan is the leading industrial city in Italy and Berlin is the
largest  German  city.  A  more  detailed  modeling  of  the  influence  of
temperatures  could  be  based  on  weighted  temperatures  from  several
areas in Germany and Italy as was for example done in Graf and Wozabal
(2013); Kovacevic and Wozabal (2014); Pape et al. (2016). However, for
the  purpose  of  this  paper  we  stick  to  the  abovementioned  simple
approach.

t  and Germany HG

Prices  on  power  markets  follow  a  seasonal  and  weekly  pattern.
Hence,  as  in  Kovacevic  and  Wozabal  (2014)  and  Graf  and  Wozabal
(2013), we use a variable containing the length of daylight Dt  in units of
days to capture annual seasonality of the observations. As these quan-
tities are similar for both countries, we use the day-length of Munich
located  in  the  south  of  Germany  for  both  markets.  Moreover,  as  in
Narajewski  and  Ziel  (2020)  and  Uniejewski  and  Weron  (2018)  we
introduce  dummy  variables  Wt = (WMon
) for  Monday,  Sat-
urday, and Sunday for weekends Wt  to model weekly price patterns.

, WSun
t

, WSat
t

t

To  capture  the  overall  market  size  and  therefore  the  scarcity  of
supply in a given period t, we use the forecast as well as the actual de-
mand for Italy and Germany. An alternative way to capture the scarcity
in an electricity system would be the so called load-supply-ratio (LSR) as
defined  by  Pape  et  al.  (2016).  The  LSR  takes  into  account  detailed
modeling  of  supply  and  demand  and  is  a  more  accurate  measure  of
scarcity than mere electricity demand. However, the demand is easier to
include in our analysis, since it requires much less detailed data.

4. Methodology

In this section, we first detail how we measure liquidity costs in the
two markets by a cost-of-round-trip measure in Section 4.1. In Section
4.2, we introduce a multivariate regression model to analyze the impact
of  possible  confounding  factors  in  the  comparison  of  the  two  market
designs. Finally, in Section 4.3, we discuss a double machine learning
method  in  order  to  measure  whether  the  continuous  markets  in  Ger-
many or the auction markets in Italy lead to higher CRTs.

4.1. Liquidity measures

Market liquidity describes the possibility to quickly buy or sell an
asset without affecting the market price. This rather vague definition of
liquidity does not lend itself to a quantitative analysis of the phenome-
non.  In  fact,  there  is  no  single  established  quantitative  measure  of

EnergyPolicy154(2021)1122994T. Kuppelwieser and D. Wozabal

liquidity in the literature that captures all aspects of market liquidity.

Hagemann and Weber (2013) introduced six dimensions of liquidity
for  continuous  energy  markets  using  established  measures  from  the
literature  on  financial  markets.  The  first  dimension  is  tightness  and  is
measured using bid-ask spreads defined as the difference between the
best bid and best ask price. The second dimension is resiliency describing
the  market’s  ability  to  bounce  back  to  an  equilibrium  price  after  a
temporary distortion. The third dimension is price impact or market depth
and  describes  the impact  of  large orders  which  might  require several
offers  beyond  the  best  price  to  be  cleared.  The  fourth  dimension  is
known  as  short-run  price  volatility.  The  fifth  dimension  captures  delay
and search costs describing the propensity of traders to delay trades to
obtain better prices. The sixth dimension describes trading activity in
the  form  of  traded  volume,  number  of  trades,  and  number  of  active
traders.

Irvine et al. (2000) introduced a CRT-measure as the per dollar cost of
roundtrip  trade  of  D  dollars.  In  particular,  the  number  of  shares  that
corresponds to the dollar amount D are calculated based on the best-bid
and best-ask, and afterwards the LOB is used to calculate the resulting
cost of buying and selling the determined number of shares. Since the
interpretation in terms of quantities is more natural in power markets,
we modify this definition by proposing a CRT measure which depends
on  volume  V  instead of  the  amount  of  money and  captures all  afore-
mentioned cost related  dimensions of  liquidity.  Moreover, we  modify
the  measure  to  be  applicable  to  both  continuous  trading  as  well  as
auction markets.

Conceptually,  the  CRT  is  the  per  unit  cost  incurred  by  buying  a
certain quantity V of power and then immediately selling it again. Note
that in a liquid market CRT is close to zero. Choosing a small V yields
measurements  close  to  the  bid-ask  spread  while  larger  volumes
increasingly  measure  the  depth  of  the  order  book  plus  all  additional
costs.

More formally, we define a volume oriented measure by sorting the
buy- and sell side of the LOB at each point in time t by price to obtain ⋯
< Pt
< Pt
< ⋯, where Pt
(cid:0) 0  is the highest bid-
(cid:0) 1
(cid:0) 2
price and Pt
0  is the lowest ask-price. We denote the corresponding bid
quantities by Qt
i . For a given quantity V in MWh, we define how much of
an order i would be cleared when placing a market order of size V by

< Pt
1

< Pt
0

< Pt
2

< Pt

(cid:0) 0

instead of per unit cost when clearing the auction modified in this way.
We then subtract the hypothetical sell price of V units which we calcu-
late adding a market order of size V on the sell side instead and divide
the result by V.

The  resulting  CRT-measure  of  the  auction  market  consists  of  one
value for each market and volume. In contrast, the CRT-measure of a
certain product in a continuous market is a function of time and poten-
tially changes with each modification of the LOB. As is illustrated in the
right panel of Fig. 1 large market orders might lead to temporary extreme
values of the CRT-measure distorting our measurement. We therefore use
the mean over 15 min instead of CRTt(V) at any fixed time t. To this end,
we consider a discrete form of the continuous time varying CRT-measure
by considering averages over 15 min intervals before time τ

CRTτ(V) =

∫ τ

τ(cid:0) 15

1
15

CRTt(V) dt =

1
15

∑N

k=2

CRTtk (V) + CRTtk(cid:0) 1 (V)
2

(tk (cid:0)

tk(cid:0) 1),

where t1, …, tN are the N points in time where the LOB changes in the 15-
min time interval [τ (cid:0) 15,τ]. In the following, we use the index τ in CRTτ
to refer to a 15-min average and CRTt to refer to an instantaneous CRT at
time t.  The computed  average thus  reflects  the expected  CRT a  trader
would have to pay, if she picks a random trading time in the given time
interval.

The Italian intraday market has seven fixed times when the market is
cleared. We use clearing times of MI2 to MI7 to analyze the two markets,
i.e.,  measure  the  CRT  for  the  German  markets  at  the  times  when  the
Italian markets are cleared. The reason for the exclusion of MI1 is that
the  German  intraday  auction  closes  nearly  at  the  same  time  as  MI1,
which results in less liquidity on the continuous market at this point in
time and thus a distortion. We compare the CRT of the remaining Italian
intraday  auctions  with  the  mean  German  CRT  over  the  15  min
before  the  closing  of  the  Italian  intraday  auction.  To  this  end,  we
define  D I
h  as  the  closing  times  of  the  Italian  intraday  markets,
where  the  hourly  product  h  is  traded.  For  example,  D I
= {16 : 30}
1
= {16 : 30, 23 : 45, 3 : 45, 7 : 45, 11 : 15, 15 : 45}, where the
while D I
24
first two time stamps are from the day before delivery.

The German continuous intraday market allows participants to trade
until 30 min before physical delivery on a national market. Hence, we
will also compare the first two 15-min CRT-means within the last hour of

(

(

Q

t
i(V) = min

max

V (cid:0)

∑i(cid:0) 1

k=0

)

)

(

(

Qt

k, 0

, Qt
i

, Q

t
(cid:0) i(V) = min

max

V (cid:0)

)

)

Qt

k, 0

, Qt
(cid:0) i

.

∑(cid:0) 0

k=(cid:0) i+1

We then define the cost-of-round-trip measure for a fixed value V as

CRTt(V) =

∑

1
t
Pt
k(V)
kQ
V
⏟̅̅̅̅̅̅̅̅̅̅⏞⏞̅̅̅̅̅̅̅̅̅̅⏟
average cost

k

(cid:0)

∑

Pt

1
t
.
(cid:0) k(V)
(cid:0) kQ
V
⏟̅̅̅̅̅̅̅̅̅̅̅̅̅⏞⏞̅̅̅̅̅̅̅̅̅̅̅̅̅⏟
average revenue

k

(1)

In a continuous market it is possible to execute the buy and sell de-
cisions that are  used to define  the CRT, making equation  (1) directly
applicable. However, we note that, in principle, a trader in a continuous
market has the option to spread her trades over a longer period of time,
waiting for more orders on the other side of the market to arrive. In this
way, some of the liquidity costs measured by the CRT can be avoided at
the cost of the risk of adversely changing prices during the extended time
of bidding. The CRT on the continuous intraday market can therefore be
seen as an overestimation that accurately reflects liquidity costs only for
an impatient trader placing market orders.

To  use  the  CRT  in  an  auction  market,  we  add  a  market  order  for
buying  V  units  to  the  existing  orders  and  record  the  marginal  price

the German continuous intraday market with the CRT-measure of the
last  available  market  of  the  Italian  intraday  auction  for  the  corre-
sponding  product.  Correspondingly,  the  points  in  time  which  we
consider for the German market are D G
h

∪ {h (cid:0) 60, h (cid:0) 45}.

= D I
h

We generate observations corresponding to V = 0.1MWh, which is
the smallest value that can be traded on the German intraday markets as
well as for V = 5MWh, 10 MWh, 15 MWh and 50 MWh. On some days
the order book does not contain orders of combined size V on either the
bid or the ask side at a time ti ∈ [τ (cid:0) 15,τ]. For our analysis, we calculate
over 313 million clearings for the German market. In 0.0466% of these
cases at least one side of the limit order book is empty and we exclude
these timestamps in our calculation of the 15-min intervals. In further
0.0804% of the cases not the whole quantity V is available on at least one
side  of  the  market.  To  define  CRT  for  these  cases,  we  use  the  last
available price to clear the remaining quantity in order to calculate a
CRT.

EnergyPolicy154(2021)1122995T. Kuppelwieser and D. Wozabal

4.2. Analysis of the CRT

In this section, we analyze the impact of the variables described in
Section 3.2 on the CRTs of the two markets. To this end, we define an
index J = (V, h, τ) for every volume V, product h = 1,…,24, and time to
delivery τ ∈ D G
h  and construct the following linear regression
models for Italy and Germany

h  or τ ∈ D I

CRT G

J = XG

J βG

J + εG

J

and CRT I

J = XI

J βI

J + εI

J ,

(2)

where
(cid:0)

XG
J =

XJ , CG

J , HG

J , RW,G

J

, FW,G
J

, RS,G
J

, FS,G
J

, RD,G
J

, FD,G
J

)

(cid:0)

XI
J =

XJ , CI

J , HI

J , RW,I

J

, FW,I
J

, RS,I

J , FS,I

J

, RD,I
J

, FD,I
J

)
,

J  and  CRTI

XJ = (1, WJ , DJ ) are the regressors that are market independent, and
CRTG
J  are  the  CRTs  of  the  German  and  Italian  market,
respectively.  All  regressors  are  standardized  by  subtracting  the  mean
and  dividing  by  the  standard  deviation.  The  standardization  helps  to
simplify  the  interpretation  of  the  effects  of  covariates  with  different
scales.

We estimate the models in equation (2) separately, for every index
J . This yields 420 models for the Italian intraday auction market, and
660  models  for  the  German  continuous  intraday  market,  because  we
additionally  analyze  the  two  15-min  intervals  shortly  before  physical
delivery for the German market. For example, for h = 1, we compare
the liquidity cost on the two 15-min intervals that start 60 min and 45
min  before  physical  delivery  on  the  German  market  with  the  latest
available intraday market in D I

1, i.e., MI2.

4.3. Double/debiased machine learning

In this section, we describe how we compare the impact of the two
market  designs  on  the  CRT  while  controlling  for  the  impact  of  con-
founding variables. In particular, we directly compare the CRT in the
two  markets while  controlling for linear  and non-linear effects  of the
regressors introduced in Section 3.2. For this purpose, for every volume
V, product h, and every trading time τ ∈ D G
h , we combine the data on
CRTG
J  by stacking the two vectors on
top of each other. For τ ∈ D G
h
last market where the hour was traded on an Italian intraday market.

h, we use the CRTs of the corresponding

J  into a combined CRTC

J  and CRTI

\D I

We then define a sparse matrix

(

XJ

XJ

XC
J =

)

XG
J

0

0
XI
J

by  padding  market  specific  observations  with  zeros.  We  compute  all
quadratic interactions to capture non-linear effects obtaining
(

)

YF
J

Y G
J

0

0
Y I
J

,

J  and YI

J  consist of interactions that contain a market specific

where YG
variable  for  Germany  and  Italy,  respectively,  while  YF
J  contains  in-
teractions of variables  in XJ . Next, we delete all columns with fewer
than 10 observations different from zero.

We then replace the zeros of the sparse submatrices with the corre-

sponding mean to obtain
⎛

⎞

YF
J

⎜
⎝

Y G
J
G
J

Y

⎟
⎠.

Y

I
J
Y I
J

(3)

We  standardize  (3)  by  subtracting  the  mean  and  dividing  by  the

standard deviation and denote the resulting matrix by YC

J .

Note that replacing the zeros by the respective means in (3) ensures
that there is no variable in YC
J , which has a different mean for the subset
for Italian and German observations. We introduce a dummy variable G
that takes the value 1 for CRT values from the German market and 0 for
data  from  the  Italian  market.  Using  these  regressors,  we  specify  a
combined linear model

CRT C

J = αJ GJ + Y C

J βC

J + εJ ,

(4)

which is able to control for interactions between the variables and non-
linear effects. Moreover, all regressors have mean zero and the intro-
duced dummy variable GJ  is the only available variable to describe the
systematic differences in CRTs between the two countries.

Our aim is to obtain consistent estimates of the effect of the market
design  αJ  as  well  as  confidence  intervals.  Equation  (4)  has  many  re-
gressors  and  we  are  no  longer  able  to  apply  OLS  due  to  overfitting.
Hence,  we  would  have  to  select  a  subset  of  regressors  using  a  model
selection  mechanism  and  then  estimate  the  coefficient  α  from  the
reduced model. However, as pointed out by Leeb and P¨otscher (2005),
model  selection  distorts  inference  and  especially  small  parameters
cannot be estimated consistently. Additionally, the same data set would
be used twice: the first time for model selection and the second time to
estimate αJ  and its p-value in the resulting regression. Another naive
method would be to estimate the model (4) using a LASSO regression
and directly analyze αJ . However, the resulting estimates are biased due
to the L1-regularization term introduced in LASSO.

In order to avoid biased estimates for αJ , we use a double machine
learning procedure by Chernozhukov et al. (2018) as implemented in
STATA.  The  method  uses  Neyman-orthogonal  moments/scores  to
eliminate the regularization bias and cross-fitting to eliminate the bias
resulting from over-fitting of nuisance functions. In particular, we use
LASSO regression for model selection in (4) where the penalty param-
eter is chosen using 10-fold cross validation. We resample 10 times for
the calculation of an unbiased estimate ̃αJ  for the parameter αJ  in the
selected models. We refer to StataCorpLLC (2019) for a detailed expo-
sition of the method.

5. Results and discussion

In  this  section,  we  first  consider  a  descriptive  analysis  of  CRT  in
Section 5.1. In Section 5.2, we construct two linear regression models to
analyze the impact of confounding variables on the liquidity costs of the
two markets. Finally, we analyze the difference of the two market de-
signs using double-machine learning in Section 5.3.

5.1. Univariate and bivariate analysis of CRT

h and D G

The  descriptive  statistics  of  the  CRT-measures  are  summarized  in
Table  4. The first  panel reports  the  average CRTs  as measured  at the
points in time D I
h  which we use in our comparisons between the
markets.  However,  since  trading  in  the  German  continuous  intraday
market occurs mostly within the last 3 h before delivery, we also define a
trading  volume  weighted  CRT,  which  allows  us  to  compare  CRTs  of  a
specific product over longer periods of time as

CRTV,h =

∑

τ

∑

CRTV,h,τQh,τ
τQh,τ

,

where Qh,τ  is the traded volume for product h and time to delivery τ. The
above  sum  is  over  all  quarter  hours  τ  where  a  specific  product  h  is
traded. Similarly, when computing CRTV,h  for the Italian markets, the
cleared volumes for each auction market and the corresponding calcu-
lated CRTs are used. The results of these computations are reported in
the lower panel of Table 4.

The analysis reveals that the CRT for all volumes is higher for the
German market on average for both ways of measurement. Comparing

EnergyPolicy154(2021)1122996T. Kuppelwieser and D. Wozabal

Table 4
Descriptive statistics of CRT-measures and traded-volumes CRT-measures from 17.11.2017 to 15.06.2018.

Subset

N

mean

std

min

25%

50%

75%

max

Average CRTs at DI

h  and DG
h

27453
27453
27453
27453
27453
17471
17471
17471
17471
17471

GER, 0.1 MWh
GER, 5 MWh
GER, 10 MWh
GER, 15 MWh
GER, 50 MWh
ITA, 0.1 MWh
ITA, 5 MWh
ITA, 10 MWh
ITA, 15 MWh
ITA, 50 MWh
Trading Volume Weighted CRTs
4991
GER, 0.1 MWh
4991
GER, 5 MWh
4991
GER, 10 MWh
4991
GER, 15 MWh
4991
GER, 50 MWh
4991
ITA, 0.1 MWh
4991
ITA, 5 MWh
4991
ITA, 10 MWh
4991
ITA, 15 MWh
4991
ITA, 50 MWh

5.85
6.25
6.69
7.18
10.66
1.26
2.13
2.74
3.33
6.45

1.99
2.20
2.38
2.56
3.90
0.84
1.36
1.71
2.05
3.84

6.27
6.67
7.00
7.34
10.24
1.72
2.68
3.29
3.88
6.65

1.23
1.33
1.42
1.49
2.09
0.62
0.93
1.13
1.32
2.35

0.10
0.10
0.10
0.10
0.10
0.01
0.01
0.01
0.01
0.01

0.55
0.62
0.72
0.81
1.32
0.01
0.01
0.01
0.01
0.01

2.40
2.81
3.00
3.40
5.65
0.25
0.50
0.67
0.92
2.18

1.24
1.40
1.54
1.69
2.67
0.43
0.73
0.95
1.15
2.21

4.50
4.90
5.02
5.62
8.51
0.72
1.22
1.72
2.11
4.50

1.64
1.83
1.99
2.17
3.37
0.70
1.15
1.46
1.73
3.32

7.50
7.95
8.33
8.93
12.85
1.59
2.82
3.60
4.34
8.26

2.34
2.60
2.79
3.00
4.52
1.07
1.75
2.18
2.63
4.84

137.70
147.50
162.75
168.50
198.55
27.63
38.08
46.79
50.45
63.47

14.32
24.31
35.52
39.55
58.61
5.98
8.29
9.49
12.10
21.25

Fig. 2. Boxplots of CRTs grouped by trading time and volume.

the maxima of the distributions, we observe that the corresponding CRTs
for the German market far exceed the maximal CRTs observed in the
Italian markets. However, the results for the averages are not entirely
driven by the right tail of the distribution as the analysis of the other
quantiles reveals. Another interesting observation is that while the CRT
for the Italian market increases sharply with V, this effect is much less
pronounced on the German market, where costs are high even for small
volumes due to the bid-ask spread on the German market.

The univariate analysis along the dimension volume does not capture
changes with the time to delivery. Hence, we show the dependence of
the results on the time to delivery in the boxplots in Fig. 2 for the CRTs
calculated  at  D I
h . We  note that liquidity costs  on  the  Italian
market are low during the first two auction markets, and are relatively
high for the MI4 and MI7. The German CRTs decrease towards 1 h before
physical  delivery  and  increase  afterwards  –  this  L-shape  was  also
observed in Balardy (2018).

h  and  D G

5.2. Effects in the individual markets

In this section, we analyze the effect of the explanatory variables XI
and XG  as introduced in Section 4.2 on the CRT in the respective mar-
kets. In order to do so, we fit the linear regression models (2) using the
fitlm  function  as  implemented  in  MATLAB  R2017a.  We  consider  the
same  data-set  as  used  in  the  previous  section  grouped  by  volume,
product, and time to delivery.

We consider a regressor to be significant in a regression, if its p-value
is smaller than 0.05 and order the regressors according to the number of
models  that  they  are  significant  in.  The  upper  row  of  plots  in  Fig.  3
shows the distribution of coefficients of the four regressors which are
most often significant in the estimated models for the Italian market. The
lower four plots repeat this analysis for the German market.

For  Germany,  the  most  important  regressor  is  the  seasonality  Dt
modeled  as  the  length  of  daylight,  which  has  a  significant  positive
impact  in  371  out  of  660  models.  As  the  estimated  coefficients  are
unambiguously negative, this implies lower liquidity costs in summers.

EnergyPolicy154(2021)1122997T. Kuppelwieser and D. Wozabal

Fig. 3. Distribution of the top 4 significant estimates of the selected controls of Italy (above) and Germany (below). The x-axis of the plots represents the values of the
estimated coefficients.

The  next  most  significant  regressor  is  the  forecast  demand  FD,G,
which is significant in 244 models and has also a clearly negative co-
efficient implying that higher (forecast) demands lead to more trading,
which in turn decreases liquidity costs.

The last two depicted regressors are the dummies for Sundays and
Saturdays which are significant in 243 and 239 models, respectively. On
a first glance, the negative signs of the estimated regressors might seem
surprising, since there is less trading on the weekend lowering liquidity
costs. However, this effect is already captured by the regressor FD,G  so
that the weekend dummies only measure the weekly patterns which do
not directly depend on demand. The dummies for Saturday and Sunday,
thus allow for a more moderate increase in liquidity costs on these days
as would be modeled by the effect of lower demand alone.

By and large the German market shows clear effects and the corre-
sponding regressors are significant in many of the considered models,
which  underlines  the  importance  of  considering  these  variables  as
controls when we measure the effect of market design on liquidity costs
in Section 4.3.

The  situation  for  the  Italian  models  is  not  nearly  as  clear  cut.
Generally  speaking,  the  proposed  regressors are  significant  much  less
often and the signs are more ambiguous making easy explanations of the
results harder. This is in line with Hagemann and Weber (2015), who
find  that the trading volume on the Italian auction market cannot be
explained very well by fundamental variables.

The  most  important  regressor  for  the  Italian  market  is  cooling  CI
which  significantly  affects  liquidity  in  64  out  of  420  models  for  the
Italian market with a mostly positive sign implying that the increased
demand by  air-conditioning, which is  widely used in Italy, leads to a
positive impact on liquidity cost on hot days.

The length of daylight DI, which is significant in 57 models is the
second most important regressor in Italy. As the figure shows, the esti-
mated coefficients are mostly positive indicating a positive impact of the
length of daylight on the CRT. This implies a seasonal effect with higher
liquidity cost in summers. This is in contrast to the German situation,
where the effect on the seasonal variable is reversed.

The Sunday dummy is significant in 55 models. The sign of the re-
gressor is rather ambiguous and hard to interpret, since, similar to the
German market, there is an interaction with the realized demand, which

is also contained among the top 4 regressors.

Lastly, the realized demand RD,I

t  affects the CRT on the Italian market
significantly in 40 models, where it mostly has a negative effect on the
CRT.

5.3. Comparison of market designs

Our aim in this section is to analyze the difference of the CRTs of the
two  markets  controlling  the  effect  of  confounding  variables.  For  that
purpose, we use the function xporegress of STATA StataCorpLLC (2019)
to estimate the models presented in Section 4.3.

The output of our analysis is an estimate, a valid confidence interval,
and the corresponding p-value for the parameter α in model (4). Table 5
summarizes the results in form of a heatmap showing estimates and p-
values. The columns indicate different hourly products, while the rows
indicate time to delivery. To distinguish between the different quantities
V, we divide the table into five panels.

We compare CRTs for products with the same time to delivery, and
the  CRTs  for  the  two  15  min  intervals  on  the  German  continuous
intraday market before delivery of a specific product with the last auc-
tion  market in  Italy where  the  corresponding product  is  traded. Cells
marked grey indicate products that can not be compared, since they are
no longer traded on the Italian market. A cell is colored red if the esti-
mate for αJ  in the corresponding model is positive, i.e., the CRT in the
Italian market is lower than in the German market. Analogously, cells
are colored blue if αJ  is negative. The intensity of the color reflects the
magnitude of the p-value with more intense coloring for lower p-values,
i.e., more significant results as indicated in the color map in the last row
of the table.

As expected from the univariate results in Section 5.1, the majority of
cells are red indicating higher cost of liquidity on the German market.
Comparing  the  overall  results  of  the  five  different  panels,  this  effect
weakens  for  higher  volumes  V,  indicating  that  the  German  market  is
relatively less affected by large volume bids as can also be seen in Fig. 2.
Observing the first rows of the five panels, it becomes clear that there
is a strong influence of the time to delivery on the estimated parameter
αJ . In particular, the Italian market has clearly lower liquidity cost at
the  time  of  clearing  of  the  first  two  Italian  intraday  markets  for  all

EnergyPolicy154(2021)1122998T. Kuppelwieser and D. Wozabal

Table 5
Results in €/MWh using all possible combinations until quadratic terms with standardized regressors and re-sampling (10).

volumes  V.  However,  looking  at  single  columns  corresponding  to
products h = 1, …, 24, this effect weakens as trading times move closer
to delivery. These results are consistent with the analysis in Fig. 2 and
the fact that traded volumes tend to decrease for later Italian auction
markets, while the German market is most active close to delivery.

The last two rows of every panel compare the first two 15-min in-
tervals in the last hours before delivery in the German market with the
last Italian auction market where the respective hour can be traded. In
these 15-min intervals the German market reaches its highest liquidity
and  exhibits  significantly  lower  liquidity  cost  as  the  Italian  markets,
except for small volumes.

In summary, the German market gets relatively more liquid towards
physical delivery, with higher liquidity in the German market close to

delivery and for larger volumes V. This is also supported by looking at
single rows where we mostly observe increasing estimates for αJ  with
increasing products h = 1, …, 24.

Looking at the first non-gray blocks in every row corresponding to
MI3-MI7, i.e., the hours that can be traded the last time on an Italian
market, we observe that liquidity cost on the Italian market is higher
than on the German market. These markets  are the last possibility to
trade forecast updates of renewable energy sources in the corresponding
hours and trading volumes are correspondingly relatively high. Appar-
ently, the high CRTs are thus a consequence of tight market situations
caused  by  either  large  demands  or  large  free  production  capacities
flooding the market for low prices.

EnergyPolicy154(2021)1122999T. Kuppelwieser and D. Wozabal

6. Conclusions and policy implications

References

This  article  explores  liquidity  costs  of  the  German  continuous
intraday market and the Italian auction-based intraday market. For that
purpose, we introduce a cost-of-round-trip measure to analyze liquidity
costs. Grouping the data of each market by volume and trading time, we
compare cost of liquidity in the two markets using descriptive statistics.
Secondly, we analyze the impact of several explanatory variables on the
two markets separately. Thirdly, we compare the two market designs by
controlling the impact of the confounding variables.

We find that liquidity costs are generally lower in the Italian auction
market,  whereby  the  difference  tends  to  decrease  with  the  traded
quantity of power and as trading gets closer to physical delivery. The
latter finding is consistent with the L-shape of the German bid-ask spread
observed by Balardy (2018).

Our  results  show  that  the  cost  of  liquidity  in  both  countries  is
influenced by weekly and yearly seasonalities, temperatures via cooling
demand, and the overall demand for electricity.

Our study has some limitations. Firstly, the German market provides
the possibility to place iceberg orders, i.e., orders where the full volume
is not visible but gets revealed gradually as parts of the order are cleared.
The existence of a significant amount of these invisible orders might lead
us to underestimate the liquidity and correspondingly overestimate the
CRT on the German market. Secondly, the CRT on the Italian intraday
auction markets might be higher due to zonal prices in Italy in auctions
where there is congestion of transmission lines between market zones.
Our analysis suggests that a hybrid system might leverage the ad-
vantages of both market designs and decrease liquidity costs on intraday
markets (Bellenbaum et al., 2014; Ehrenmann et al., 2019; Ocker and
Jaenisch, 2020). In particular, auction markets for hours far from de-
livery might help to increase liquidity by pooling orders, while contin-
uous intraday markets starting close to delivery would be an optimal
tool to integrate forecast errors for the output from variable renewables
shortly  before  physical  delivery.  A  similar  design  was  recently  intro-
duced for the Spanish intraday market and it is planned for the Italian
market as well. Alternatively, one could use a system of frequent batch
auctions  as  proposed  in  Budish  et  al.  (2015);  Deutsche  B¨orse  Group
(2018) to combine the advantages of continuous trading and auctions.

CRediT authorship contribution statement

Thomas  Kuppelwieser:  Data  curation,  Visualization,  Writing  –
original draft, Validation, Software, Formal analysis. David Wozabal:
Conceptualization, Methodology, Supervision, Writing – original draft,
Writing – review & editing, Formal analysis.

Declaration of competing interest

The authors declare that they have no known competing financial
interests or personal relationships that could have appeared to influence
the work reported in this paper.

Acknowledgements

The  authors  thank  three  anonymous  referees  for  many  insightful
comments which helped to substantially improve the paper, psaier.en-
ergies  for  providing  the  German  EPEX  SPOT  Limit  Order  Book,  and
Phinergy for providing the submitted offers of the Italian intraday auc-
tions in an easy accessible format.

Balardy, C., 2018. An empirical analysis of the bid-ask spread in the German power

continuous market, working paper.

Bellenbaum, J., Bucksteeg, M., Kallabis, T., Pape, C., Weber, C., 2014. Intra-day Cross-

zonal Capacity Pricing. Study on behalf of Ofgem.

Budish, E., Cramton, P., Shim, J., 2015. The high-frequency trading arms race: frequent
batch Auctions as a market design response. Q. J. Econ. 130 (4), 1547–1621.
Burger, B., 2019. Net Public Electricity Generation in Germany in 2018. Report.

Fraunhofer Institute for Solar Energy Systems, ISE. https://www.ise.fraunhofer.de
/content/dam/ise/en/documents/News/Stromerzeugung_2018_2_en.pdf.

Chernozhukov, V., Chetverikov, D., Demirer, M., Duflo, E., Hansen, C., Newey, W.,

Robins, J., 2018. Double/debiased machine learning for treatment and structural
parameters. Econom. J. 21 (1), C1–C68.

Deutsche B¨orse Group, 10, 2018. Continuous Auction Market Model: A Proposal for the
Future European Intraday Power Market. Technical Report. Deutsche B¨orse AG.
Ehrenmann, A., Henneaux, P., Küpper, G., Bruce, J., Klasman, B., Schumacher, L., 2019.
The Future Electricity Intraday Market Design. Tech. rep., European Commission.
Ela, E., Milligan, M., Bloom, A., Botterud, A., Townsend, A., Levin, T., 2014. Evolution of

Wholesale Electricity Market Design with Increasing Levels of Renewable
Generation. Technical Report. National Renewable Energy Lab. (NREL).

ENTSO-E, June, 2019. Statistical FACTSHEET 2018. Report, ENTSO-E. URL. https://ee
publicdownloads.entsoe.eu/clean-documents/Publications/Statistics/Factsheet/ent
soe_sfs2018_web.pdf.

EPEX, 2019. Epex spot operational rules. In: https://www.epexspot.

com/en/download/#rules-fees-processes [Online; accessed 16-December-2019.
Fan, S., Hyndman, R.J., 2012. Forecasting electricity demand in australian national

electricity market. In: 2012 IEEE Power and Energy Society General Meeting. IEEE,
pp. 1–4.

Garnier, E., Madlener, R., 2015. Balancing forecast errors in continuous-trade intraday

markets. Energy Syst. 6, 361–388.

GME, 2016. Documento di consultazione 05/2016. https://www.mercatoelettrico.org/
it/MenuBiblioteca/Documenti/20160606_DCO_Nuovi_MI.pdf [Online; accessed 07-
December-2019.

GME, 2019. GME Bilancio d’Esercizio 2018. Report, Gestore dei Mercati Energetici S. p.

A. URL. https://www.mercatoelettrico.org/En/MenuBiblioteca/Document
i/20190618BilancioGME2018.pdf.

Goodarzi, S., Perera, H.N., Bunn, D., 2019. The impact of renewable energy forecast

errors on imbalance volumes and electricity spot prices. Energy Pol. 134, 110827.

Graf, C., Wozabal, D., 2013. Measuring competitiveness of the EPEX spot market for

electricity. Energy Pol. 62, 948–958.

Hagemann, S., Weber, C., 01, 2013. An empirical analysis of liquidity and its

determinants in the German intraday market for electricity. SSRN Electron. J.
Hagemann, S., Weber, C., 2015. Trading volumes in intraday markets: Theoretical

reference model and empirical observations in selected European markets. In: EWL
Working Paper 03/15. University of Duisburg-Essen, Chair for Management Science
and Energy Economics.

Hannele Holttinen, J.M.S.S., 2013. Wind Power Forecasting Accuracy and Uncertainty in

finland. Discussion Papers of Diw Berlin, VTT Technology 95.

Irvine, P., Benston, J., Kandel, E.G., 05, 2000. Liquidity beyond the inside spread:
measuring and using information in the limit order book. SSRN Electron. J.
Janke, T., Steinke, F., 2019. Forecasting the price distribution of continuous intraday

electricity trading. Energies 12 (22).

Kovacevic, R., Wozabal, D., 2014. A semiparametric model for electricity spot prices. IIE

Trans. 46, 344–356.

Kulakov, S., Ziel, F., 2020. The impact of renewable energy forecasts on intraday

electricity prices. Econom. Energy Environ. Pol. 10 (1).

Leeb, H., P¨otscher, B.M., 2005. Model selection and inference: facts and fiction. Econom.

Theor. 21 (1), 21–59.

Marcjasz, G., Uniejewski, B., Weron, R., 2020. Beating the naïve––combining lasso with

naïve intraday electricity price forecasts. Energies 13, 1667.

Martin, H., Otterson, S., June, 2018. German intraday electricity market analysis and

modeling based on the limit order book. In: 2018 15th International Conference on
the European Energy Market (EEM), pp. 1–6.

Narajewski, M., Ziel, F., 2020. Ensemble forecasting for intraday electricity prices:

simulating trajectories. Appl. Energy 279, 115801.

Neuhoff, K., Ritter, N., Salah-Abou-El-Enien, A., Vassilopoulos, P., 2016. Intraday

Markets for Power: Discretizing the Continuous Trading? Discussion Papers of DIW
Berlin 1544. DIW Berlin, German Institute for Economic Research.

Ocker, F., Jaenisch, V., 2020. The way towards european electricity intraday auctions –

status quo and future developments. Energy Pol. 145.

Pape, C., Hagemann, S., Weber, C., 2016. Are fundamentals enough? explaining price

variations in the German day-ahead and intraday power market, 01 Energy Econ. 54.
StataCorpLLC, 2019. Stata lasso reference manual release 16. https://www.stata.com/

manuals/lasso.pdf [Online; accessed 16-December-2019.

Uniejewski, B., Weron, R., 2018. Efficient forecasting of electricity spot prices with

expert and lasso models. Energies 11 (8).

von Luckner, N., Cartea, A., Jaimungal, S., Kiesel, R., 2017. Optimal Market Maker

Pricing in the German Intraday Power Market, Working Paper.

Weber, C., 2010. Adequate intraday market design to enable the integration of wind

energy into the european power systems. Energy Pol. 38 (7), 3155–3163.

EnergyPolicy154(2021)11229910