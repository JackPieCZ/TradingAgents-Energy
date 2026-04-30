OR Spectrum (2023) 45:57–83
https://doi.org/10.1007/s00291-022-00698-5

ORIGINAL ARTICLE

Intraday power trading: toward an arms race in weather
forecasting?

Thomas Kuppelwieser1 · David Wozabal1

Received: 20 September 2021 / Accepted: 25 October 2022 / Published online: 7 November 2022
© The Author(s) 2022

Abstract
We  propose  the  first  speculative  weather-based  algorithmic  trading  strategy  on  a
continuous intraday power market. The strategy uses neither production assets nor
power  demand  and  generates  profits  purely  based  on  superior  information  about
aggregate output of weather-dependent renewable production. We use an optimized
parametric  policy  based  on  state-of-the-art  intraday  updates  of  renewable  produc-
tion forecasts and evaluate the resulting decisions out-of-sample for one year of trad-
ing based on detailed order book level data for the German market. Our strategies
yield significant positive profits, which suggests that intraday power markets are not
semi-strong  efficient.  Furthermore,  sizable  additional  profits  could  be  made  using
improved forecasts of renewable output, which implies that the quality of forecasts is
an important factor for profitable trading strategies. This has the potential to trigger
an arms race for more frequent and more accurate forecasts, which would likely lead
to increased market efficiency, more reliable price signals, and more liquidity.

Keywords  Policy optimization · Intraday power markets · Algorithmic trading ·
Weather-based trading · Stochastic optimization

1  Introduction

In the last decades, the electricity industry in many countries has seen rapid changes.
One  driver  of  these  developments  was  the  transition  from  a  highly  vertically  inte-
grated, state controlled sector of the economy to  a largely  competitive and  decou-
pled industry Pollitt (2019). Another reason is the climate crisis and the increasing
efforts to transition to a carbon neutral society. The electricity sector is the key to

 *  David Wozabal

david.wozabal@tum.de

Thomas Kuppelwieser
thomas.kuppelwieser@tum.de

1

School of Management, Technical University of Munich, Arcisstraße 21, 80333 Munich,
Germany

Vol.:(0123456789)1 3

58

T. Kuppelwieser, D. Wozabal

sustainable  energy  systems,  enabling  a  change  of  the  nature  of  energy  supply  by
sharply increasing production from variable renewable energy sources (VRES) such
as wind and photovoltaics.

In  the  majority  of  industrialized  countries  electricity  is  traded  on  a  range  of
future markets whose products differ in their time to maturity. Recently, the weather-
dependent  and  unpredictable  nature  of  VRES  production  has  increasingly  shifted
the  focus  to  markets  with  a  high  temporal  resolution  that  trade  close  to  delivery
when production forecasts are reasonably accurate.

Short-term trading is mostly organized in real-time markets or continuous intra-
day  markets.  While  the  former  is  the  prevailing  design  in  the  US  (Milligan  et  al.
2016), the latter is, for example, used in Europe. These volatile markets are attrac-
tive  for  firms  that  can  quickly  adapt  their  demand  or  production  profiles  and  can
thus  sell  their  flexibility  to  other  market  participants  with  balancing  needs  driven
by,  for  example,  forecast  errors  in  VRES  production.  Short-term  trading  thus  pro-
vides incentives to invest in flexible energy sources such as gas turbines and storage,
which are required to balance the intermittent production from ever growing VRES
capacities.

Due to the increasing size and sustained price variability, short-term markets are
not  only  interesting  for  flexibility  providers  but  increasingly  also  for  speculative
traders who neither own production assets nor  trade their  own electricity  demand.
The  essential  defining  characteristic  of  speculative  trading  on  electricity  markets
thus  is  that  any  open  position  has  to  be  closed  before  the  respective  product  goes
into delivery.

In  this  paper,  we  propose  a  trading  strategy  for  speculative  trading  on  continu-
ous  intraday  markets.  Our  approach  is  motivated  by  algorithmic  trading  strategies
in continuous financial markets that are triggered by signals indicating a change in
the fundamental value of an asset. Since, as discussed above, VRES production is an
important driver of short-term electricity trading, we use forecast errors of aggregate
VRES production as signals for our strategies. The rationale for this choice is that if
forecasts for VRES production are inaccurate, producers have to correct their posi-
tions taken on the day-ahead market, which, if the errors are large enough, causes a
shift in intraday prices (Kiesel and Paraschiv 2017; Kremer et al. 2020a, b).

While the literature on asset backed trading on intraday power markets is exten-
sive (see for example Boomsma et al. 2014; Kumbartzky et al. 2017; Séguin et al.
2017;  Bertrand  and  Papavasiliou  2019;  Wozabal  and  Rameseder  2020;  Rintamäki
et al. 2020), there is virtually no research on optimal bidding strategies for specula-
tive traders that have no assets of their own.

In the following, we review those papers that come closest to our trading strat-
egies.  Skajaa  et  al.  (2015)  analyze  a  wind  power  producer  participating  in  the
continuous  intraday  market  as  well  as  the  balancing  market  using  detailed  data
from  the  limit  order  book  (LOB)  as  well  as  several  updated  wind  power  fore-
casts.  Tankov  and  Tinsi  (2021)  propose  to  use  repeatedly  updated  probabilistic
forecasts  instead  of  point  forecasts  for  weather  related  variables.  Sánchez  de  la
Nieta et al. (2020) use several updated weather forecasts for bidding on the Span-
ish  day-ahead  market,  intraday  auctions,  and  imbalance  market.  Engmark  et  al.
(2018) propose a trading strategy for a hydro power producer on the day-ahead,

1 359

intraday  and  balancing  market.  Dideriksen  et  al.  (2019)  consider  trading  strat-
egies  for  a  hydropower  producer  on  the  intraday  market.  Koch  (2021)  uses  the
intraday market to build up a position to be cleared on the balancing market, thus
arbitraging  between  the  two  markets.  Kath  and  Ziel  (2018)  introduce  a  forecast
for the volume weighted continuous intraday price for 15-minutes contracts and
develop  a  strategy  to  choose  between  trading  on  the  day-ahead  auction  market
and the continuous intraday market. Monteiro et al. (2020) evaluate future trad-
ing strategies on the Spanish Mibel market based on long-term electricity futures.
Maciejowska  et  al.  (2019)  study  the  problem  of  a  small  VRES  producer  that
trades on the day-ahead and the intraday market. Wozabal and Rameseder (2020)
propose trading strategies for a storage that arbitrages between Spanish day-ahead
and  intraday  markets.  Furthermore,  Kath  and  Ziel  (2020)  explore  optimal  order
execution strategies with the aim to minimize liquidity cost and Glas et al. (2019,
2020)  study  optimal  VRES  trading  strategies  on  the  intraday  market  in  an  opti-
mal control setting. Finally, Bertrand and Papavasiliou (2019) use reinforcement
learning  to  optimize  a  Markovian  strategy  for  an  electricity  storage  on  the  Ger-
man intraday market for power.

We contribute to the literature in the following ways:

1.  While there is a growing literature investigating the impact of VRES production
forecast errors on intraday prices (e.g., Garnier and Madlener 2014; Kiesel and
Paraschiv 2017; Kremer et al. 2020a, b; Kulakov and Ziel 2019), we are the first
to propose a demonstrably profitable trading strategy based on this observation.
We take great care to accurately model market mechanisms, the exact clearing
algorithm, and the sequence of information. To the best of our knowledge Skajaa
et al. (2015); Martin and Otterson (2018); Engmark et al. (2018); Bertrand and
Papavasiliou (2019); Kuppelwieser and Wozabal (2020); Dideriksen et al. (2019)
are the only other papers that capture the realities of continuous trading in simi-
lar detail. In particular, apart from Skajaa et al. (2015); Engmark et al. (2018);
Bertrand and Papavasiliou (2019); Dideriksen et al. (2019); Koch (2021), this is
the first paper that evaluates a trading strategy based on detailed order book data,
which is different from the extant literature that discretizes the trading to 1 min
or 15 min brackets to be able to deal with the shear amount of order data (e.g.,
Glas et al. 2019, 2020; Kath and Ziel 2020).
  The resulting trading problem is characterized by substantial uncertainties
about the future state of the continuous market and a high frequency of arrival of
new order information, necessitating a large number of decisions which have to
be taken at random points in time. Consequently, given the complex information
structure of the problem and the number of decisions to be taken, finding optimal
decisions is clearly computationally intractable (Bertrand and Papavasiliou 2019).
We therefore propose a non-anticipative parametric policy that yields significant
positive profits in controlled out-of-sample experiments and uses sufficiently large
forecast errors of renewable production as trading signals.

2.  Our results show that intraday power markets are far from efficient. In particular,
it is possible to capitalize on information on day-ahead forecast errors of VRES

1 3Intraday power trading: toward an arms race in weather…
60

T. Kuppelwieser, D. Wozabal

output. This fact suggests that the market disseminates information slowly and in
an imperfect manner: While recent results found evidence that intraday electricity
markets are weak-form efficient (e.g., Oksuz and Ugurlu 2019; Narajewski and
Ziel 2020), our results illustrate that they violate the more restrictive semi-strong
version of the efficient market hypothesis, which states that it is impossible to
consistently generate abnormal returns using publicly available data (Malkiel and
Fama 1970).

3.  Next to demonstrating that strategies based on current state-of-the-art forecasting
of renewable production are profitable, we quantify the value of a perfect fore-
cast and conclude that there is potential for substantially increased profits from
weather-based strategies. This finding suggests that in the future the industry
might see an arms race in forecasting, similar to the arms race for speed observed
in the financial markets (e.g., Budish et al. 2015).

In  our  numerical  case  study,  we  consider  the  German  intraday  power  market.  We
first  examine  the  insample  performance  of  our  policy  for  18  months  of  trading  to
identify sensible ranges for our parameters and for the timing of trading decisions.
We find a trade-off between the quality of the signal that is required to trigger the
strategy  and  the  size  of  the  traded  position.  Generally  speaking,  profits  per  trade
rise in the quality of the signal. However, if trading is restricted to only those prod-
ucts with high quality signals, trading occurs infrequently reducing overall profits. A
similar trade-off can be observed for the size of the position: while profits initially
rise with larger positions, the marginal profit per additional traded MWh is dimin-
ishing due to liquidity costs that increase in order size.

Furthermore, we find that one of the most important aspects of the trading strat-
egy is how it deals with the lack of liquidity that plagues intraday power markets. In
particular, a trader that seeks to capitalize on informational advantages in forecast-
ing would ideally want to trade as early as possible on this information. However,
since there is usually very little trading activity until 2-3 h before gate closure, such
a strategy is running the risk of being unprofitable due to high transaction costs. We
show  how  patient  strategies  based  on  a  sequence  of  limit  orders  can  significantly
reduce liquidity costs and outperform simpler impatient strategies based on market
orders.

In  an  out-of-sample  study,  we  evaluate  our  strategies  for  one  year  of  trad-
ing.  The  results  show  that  the  proposed  policies  yield  significant  positive  profits
for  both  hourly  and  quarter-hourly  products,  where  the  former  is  characterized  by
larger volumes, higher profits, and more volatile profits per product, while the latter
yields  lower  profits  and  also  trades  less  volumes.  These  differences  can  mostly  be
explained by the higher liquidity of hourly products.

We show that the potential additional earnings for a strategy which is based on a
perfect  intraday  forecast  of  VRES  production  are  significant,  increasing  profits  by
one order of magnitude or, more specifically, from €200,000 to 2 million for hourly
products  and  from  €60,000  to  €300,000  for  quarter-hourly  products.  Hence,  there
is a strong incentive to invest in better forecasts and more frequent updates during
the  day  –  a  situation  which  might  trigger  an  arms  race  in  short-term  forecasting
of renewable output. As opposed to the arms race for speed observed in the share

1 361

market (e.g., Budish et al. 2015), this development has the potential to increase mar-
ket liquidity in early hours of intraday trading, the accuracy of price discovery, and
therefore ultimately welfare.

The rest of the paper is organized as follows: In Sect. 2, we describe the relevant
features of intraday power markets and discuss liquidity and the impact of VRES.
Section 3 is dedicated to our trading policy. Section 4 describes the setting of our
case study, while Sect. 5 discusses its results. Finally, Sect. 6 concludes the paper
and discusses implications as well as avenues for further research.

2   Intraday markets

In  this  section,  we  first  describe  the  typical  market  design  of  continuous  intraday
power markets in Sect. 2.1, focusing on the German continuous intraday market as
one of the most liquid markets. Secondly, we discuss the influence of renewable gen-
eration on prices in Sect. 2.2. Finally, we investigate market liquidity and its depend-
ency on time to delivery in Sect. 2.3.

2.1   Market design

Most spot markets for power consist of a day-ahead market that allows market par-
ticipants  to  trade  electricity  one  day  ahead  of  delivery  and  a  short-term  market,
which gives participants the possibility to adjust their positions until shortly before
physical delivery. Short-term markets are usually either organized as real-time mar-
kets  or  as  intraday  markets.  Prominent  examples  of  the  former  include  most  US
power markets (Milligan et al. 2016), while European short-term markets fall in the
latter category (Shinde and Amelin 2019).

In Europe, there are currently two competing types of intraday trading systems:
auction  markets  and  continuous  intraday  trading.  In  2015,  the  EU  decided  on  the
long-term goal to couple all European intraday markets in a large continuous mar-
ket  in  order  to  facilitate  a  secure  energy  supply,  competitiveness,  and  fair  prices
(European Commission 2015). While most European countries already transitioned
to continuous intraday markets that are compatible with the joint European design,
some countries such as Italy, Spain, and Portugal still use auction markets. In this
paper,  we  are  interested  in  continuous  intraday  markets  and  for  the  ease  of  expo-
sition  focus  on  the  European  market  design  and  its  implementation  in  Germany
hosted by the EPEX, the largest power exchange in Europe (see Viehmann 2017, for
a detailed description). However, we note that other markets are very similar in the
features crucial for the analysis in this paper.

With  the  build  up  of  capacities  in  intermittent  and  unpredictable  production,
short-term  trading  on  intraday  markets  is  increasingly  gaining  traction  (EPEX
2020b).  As  a  result,  liquidity  of  the  German  intraday  market  has  been  improving
in the last years with growing trading volumes, but also an increased prevalence of
automated trading (EPEX 2020b). In particular, due to the short-term nature of the

1 3Intraday power trading: toward an arms race in weather…62

T. Kuppelwieser, D. Wozabal

continuous intraday market, marketing of flexible power sources and electricity stor-
age as well as position closing is often relegated to trading algorithms.

On the German intraday market power can be traded on a national market until
30 minutes before physical delivery. After that, the national market closes and four
separate  markets,  one  for  every  control  area,  open  where  market  participants  can
trade for delivery in that area until 5 minutes before physical delivery. The intraday
market opens shortly after the clearing of the day-ahead market and allows to trade
hourly, half-hourly, and quarter-hourly products. Market participants submit orders
to the limit order book which are cleared continually. If for a market participant the
combined orders from spot and future markets deviate from the actual physical pro-
duction or consumption at gate closure of the intraday market, the residual quantities
are settled on the balancing market. The price charged or paid for these deviations is
the so-called symmetric reBAP (Bundesnetzagentur 2012).

Each buy and sell order on the intraday market for a given product contains basic
information about quantity, limit price, and validity time. A market order is cleared
immediately  against  the  best  available  order  in  the  limit  order  book,  while  a  limit
order is only executed with matching orders on the other side of the market up to
a certain price (the limit). If this is not possible, the order is kept in the limit order
book until its end validity date to be cleared with future orders. If the quantities of
two  matched  orders  do  not  agree,  the  order  with  the  higher  order  quantity  is  only
partially  cleared  and  remains  in  the  order  book  with  a  correspondingly  reduced
quantity (EPEX 2020a).

Market  participants  can  add  the  usual  order  qualifiers  such  as  all-or-nothing,
immediate-or-cancel,  or  fill-or-kill.  Additionally,  iceberg  orders  are  allowed  for
which  only  a  fraction  of  the  order  quantity  is  visible  to  other  market  participants.
As soon as the visible quantity is cleared, the next part of the order is automatically
placed in the LOB (EPEX 2020a).

The state of the LOB changes with the placement of a new order, with the modifi-
cation of an order, and at the end-validity-time of an active order. The limit price of
the order with the lowest sell price is called best-ask, while the order with the high-
est buy price defines the best-bid, and the difference between the two prices is the
bid-ask-spread.

2.2   The influence of renewable generation

Because electricity is bought by most consumers for a price that is only infrequently
updated,  short-term  consumption  is  inelastic.  Furthermore,  due  to  limited  storage,
supply and demand have to be matched instantaneously. Consequently, supply and
demand shocks can lead to massive shifts in short-term prices (Weron 2014).

One frequent source of supply shocks is the deviation of produced wind and solar
power from its forecast levels. Typically, owners of VRES sell electricity on the day-
ahead market one day before delivery based on forecasts of wind speeds and solar
irradiation.  If  those  forecasts  turn  out  to  be  incorrect,  the  residual  quantities  have
to be traded on the intraday market or resolved on the balancing markets. Since the

1 363

latter offers less favorable prices, VRES producers have an incentive to balance fore-
cast errors on the intraday market as best as they can.

In particular, if a trader sold too much energy on the day-ahead market she will
try to buy back missing energy on the continuous intraday market as soon as more
accurate forecasts become available and the error becomes apparent thereby increas-
ing  demand.  An  analogous  situation  occurs  if  too  little  energy  was  sold,  which
induces an increased supply, leading to downward pressure on the intraday prices.
Due to the rapid expansion of VRES capacities in many countries and the high cor-
relation  of  forecast  errors  for  VRES  production  within  a  market  zone,  large  unex-
pected  aggregate  deviations  from  production  forecast  are  frequently  observed  and
significantly  influence  the  intraday  price  (Karanfil  and  Li  2017;  Kiesel  and  Para-
schiv 2017; Goodarzi et al. 2019; Kulakov and Ziel 2019; Hu et al. 2021; Spodniak
et al. 2021).

Traditionally  weather  forecasts  are  based  on  large  computationally  expensive
models  that  depend  on  satellite  images  and  high  altitude  measurements  of  planes
and weather balloons, which are only collected every couple of hours. These fore-
casts are therefore updated too infrequently to be used as inputs for algorithmic trad-
ing strategies on the intraday market.

However,  recently,  several  providers  specialized  in  combining  these  traditional
global weather forecasts with real-time production data and local weather models to
offer  frequent  updates  of  forecasts  for  renewable  production  of  single  plants.  Cur-
rently,  there  are  many  providers  such  as  Enfor,  ConWX,  Meteologica,  Gnarum,
enercast,  weathernews,  or  windsim  that  compete  to  provide  more  accurate  VRES
power production forecasts and more frequent updates.

2.3   The role of liquidity

Liquid markets are necessary for the successful implementation of the trading strate-
gies considered in this paper. The observations in this section therefore inform the
discussions in the later sections. For a more comprehensive treatment of the liquid-
ity of the German intraday market, we refer to Kuppelwieser and Wozabal (2020).

Liquid  markets  allow  trading  for  fair  prices  at  low  transaction  costs  and  with
little  scope  for  price  manipulation  by  dominant  players.  While  traded  volumes  on
the  German  continuous  intraday  market  have  been  continuously  increasing  in  the
last  years,  the  liquidity  of  the  market  is  still  rather  limited  at  times.  Most  orders
are placed shortly before the market closes and consequently, liquidity is typically
low at the beginning of the trading session, increases toward physical delivery, and
decreases again shortly before the market closes.

As can be seen by comparing panel 1 with panel 2 and 3 of Fig. 1, the liquidity
of  the  intraday  power  market  is  significantly  worse  than  that  of  financial  markets.
The comparison reveals that, relative to the price, the bid-ask-spread for a share of a
large company is roughly 50 times smaller than the bid-ask spread of the continuous
power market during its most liquid period. Inspecting the lower two plots depicting
bid and ask prices on the German intraday market for a typical trading session of an
hourly product, we recognize the characteristic L-shape in the bid-ask spread with

1 3Intraday power trading: toward an arms race in weather…64

e
r
a
h
S
/
$

226

224

222

220

50

40

30

90

80

70

T. Kuppelwieser, D. Wozabal

AMAZON 2012-06-21

10:00

11:00

12:00

13:00

14:00

15:00

H12 2017-12-12

Ask
Bid

Ask
Bid

Jun 21, 2012

Dec 11, 16:00

Dec 11, 20:00

Dec 12, 00:00

Dec 12, 04:00

Dec 12, 08:00

H12 2018-12-12

Ask
Bid

Dec 11, 16:00

Dec 11, 20:00

Dec 12, 00:00

Dec 12, 04:00

Dec 12, 08:00

2017

2018

Fig. 1   Financial markets vs EPEX SPOT: The three plots show the best-bid and the best-ask of one trad-
ing session. The upper plot shows the Amazon share (AMZN) traded on Nasdaq, the middle plot shows
prices  for  the  product  H12  which  delivers  power  from  11:00  to  12:00  on  the  12.12.2018  as  traded  on
EPEX and the lower plot shows the same product one year after to highlight the increase in trading activ-
ity. The data on the Amazon share has been obtained from LobsterData (https:// lobst erdata. com/)

large differences between the two prices which suddenly falls to a low value close to
delivery as also observed by Balardy (2018). We note that the market for half-hourly
and quarter-hourly products is even thinner than that for hourly products (e.g., Nara-
jewski  and  Ziel  2020).  The  comparison  of  the  two  plots  in  panel  2  and  3  reveals
evidence for an increase in liquidity between the years 2017 and 2018. Finally, the
high  volatility  of  the  intraday  price  during  the  trading  session,  makes  the  market
attractive for speculative trading.

3   Trading strategy

Our trading strategy rests on the assumption that a large number of VRES plants sell
their forecast production on the day-ahead market and use the intraday market to re-
balance their positions so as to take into account updated production forecasts on the
day of delivery. The idea behind the strategies discussed in this section is to capital-
ize on early intraday updates of aggregate VRES production forecasts for the whole
of Germany by anticipating the direction of the correction in prices.

To  get  an  accurate  measurement  of  profits,  we  evaluate  the  proposed  strategy
based on detailed limit order book data. In particular, we do not merely rely on tick
data or a discretized version of the market as for example in Glas et al. (2019, 2020);
Kath and Ziel (2020), but take into account the exact rules of continuous intraday
market  clearing  as  well  as  detailed  data  on  orders  by  other  market  participants  to
calculate the price at which we buy and sell electricity.

We are interested in trading strategies that work without physical assets or elec-
tricity demand, implying that every product has to be traded separately and positions

1 3have to be closed before gate closure. We base our algorithms for the product that
delivers electricity in period t on the updates in the forecast of renewable production
s hours before delivery

65

t = f DA
𝜀s

t − f s

t

,

(1)

t

  is  the  day-ahead  forecast  of  renewable  production  in  t  while  f s

where  f DA
t   is  the
updated forecast at time t − s . The quantity 𝜀s
t is thus the best estimate of the forecast
error  in  aggregate  VRES  production  at  time  t  which  is  available  at  time t − s .  We
adopt  the  convention  that  f 0
t   the  true  forecast
error of the day-ahead forecast.

t   is  the  actual  production,  making  𝜀0

Our algorithm takes the form of a classic algorithmic trading strategy on financial
markets and uses 𝜀s
t as a signal that can be used to infer a change in the fundamental
value of the product, i.e., electricity to be delivered in period t. This is based on the
assumption that traders that first become aware of the errors in forecasts can capital-
ize on this knowledge by trading accordingly. For example, as a result of a positive
𝜀s
t , a trader would buy electricity on the intraday market anticipating a rise in prices
once the rest of the market becomes aware of the shortage.

However,  unlike  signals  in  financial  markets  like  earning  announcements  or
prices of other assets, which can be regarded as public information as soon as they
are revealed, information on VRES forecast errors is gradually improved as increas-
ingly better forecasts become available.1 In particular, the notion of a trader reacting
first makes much less sense than for signals typically used for high frequency trading
on shares markets, since orders cannot be placed as soon as information arrives and
the decision when to act on updated forecasts becomes important. Traders thus face
a trade-off between the reliability of the signal and the speed of the reaction.

To define our strategy, we specify a traded quantity, a price for which we place
orders, as well as the timing of orders. We depict the sequence of events in Fig. 2.
The  strategy  is  triggered  by  the  arrival  of  a  new  forecast  for  VRES  production  at
time t1 , which is a pre-defined length of time s before delivery of a product t, i.e.,
t1 = t − s . If the forecast error 𝜀s
t is large enough, we build up a position in the time
interval [t1, t2] .  Subsequently,  we  hold  the  position  until t3 > t2  and  finally  unwind
the position in the time interval [t3, t4] , where t4 is close to gate closure. Note that
since we assume that the trader does not have a physical asset, we require the posi-
tion  to  be  closed  at  the  end  of  trading  to  avoid  open  positions  on  the  balancing
market.

More specifically, we open a position of size V ± > 0 if the signal 𝜀s

t observed at
 depending on the sign of the deviation. We thus define

time t1 exceeds a threshold 𝛥±
the traded quantity at time t1 as

1  Forecasts of renewable production do not always get better with the passage of time (Tankov and Tinsi
2021). However, since they tend to get better on average as gate closure approaches, it is inconsequential
if forecasts get worse in some rare instances as long as in aggregate the proposed strategy is profitable.

1 3Intraday power trading: toward an arms race in weather…66

T. Kuppelwieser, D. Wozabal

Fig. 2   Schematic depiction of the sequence of events of the proposed trading strategy for the case where
energy is bought

xt1

=

V +,
−V −,
0,

if 𝜀s
> 𝛥+
t
if 𝜀s
< −𝛥−
t
otherwise,

(2)

⎧
⎪
⎨
⎪
⎩

where positive quantities correspond to buying of electricity, i.e., we buy V +
 MWh
of electricity if forecasts are corrected downward by more than a threshold 𝛥+
.

Apart from the traded quantity V ±

 , we also need to specify a price to place an
order.  We  investigate  two  strategies:  an  impatient  strategy  using  market  orders
and a patient strategy based on limit orders. If market orders are used, the price
is set to ±9 999€/MWh, which is the maximum/minimum price the trading system
allows, i.e., the quantity xt1 is always immediately cleared at time t1 regardless of
the price, provided the order book on the opposing side of the market is not too
small to cover the full quantity xt1 . If a market order cannot be (fully) cleared due
to a lack of market depth, we remove it from the order book and the second trad-
ing  phase  operates  with  the  correspondingly  smaller  position.  Similarly,  at  time
t4  the  position  is  closed  using  market  orders.  Choosing  this  impatient  strategy
thus  makes  sure  that  a  position  is  opened  as  soon  as  possible  and  closed  at  the
last possible moment. The downside is that if market depth is insufficient, trading
might happen at unfavorable prices.

> 𝛥+

In contrast, the patient strategy places limit orders and accepts a delay in order
execution in exchange for potentially more favorable prices. The strategy places
an order that outbids the other orders in the system by a small margin 𝛿 > 0 . For
example,  if 𝜀s
 ,  i.e.,  we  are  seeking  to  buy,  we  set  the  price  to  be  the  best
t
bid plus 𝛿 €. If an order with a higher price is added to the order stack at time t′
with t1 < t′ < t2 by another party, we update the price of our order to ensure that
we outbid the best bid by 𝛿 €. We continue in this fashion until either the whole
quantity is traded or time t2 > t1 comes at which point we remove the order from
the system.

1 3
67

We start closing the position at t3 by again setting the price such that the order
is on top of the respective side of the order book and update prices as new orders
arrive. Finally, if the position is not closed at time t4 > t3 , we place a market order
to close the position. If the order cannot be fully cleared against orders in the LOB
at t4 , the rest of the order is cancelled and the residual quantity is cleared on the bal-
ancing market.

Note  that  opposed  to  the  patient  strategy  the  impatient  strategy  incurs  the  full
bid-ask spread. For example, if the intention is to buy, then an order on the ask side
of the market is accepted instead of placing orders on the bid side as it is done when
using limit orders. Similarly, when closing the position with a market order an exist-
ing  bid  is  accepted  instead  of  placing  an  ask  order  in  the  system.  Hence,  loosely
speaking the patient strategy avoids the bid-ask spread for the price of delayed order
execution.

In order to calculate the resulting profit, we denote by T1 the set of time points at
which the LOB changes in the period [t1, t2] , by T2 the set of time points when the
LOB changes after t3 until the end of trading of the product at t4 , and by V𝜏 as the
quantity  traded  as  consequence  of  order  stack  changes  at  times 𝜏 ∈ T ∶= T1 ∪ T2 .
Further, for 𝜏 ∈ T  , we denote by P𝜏 as the volume weighted average per MWh price
for which the quantity at time 𝜏 is traded.

The profit and loss of the strategy in period t can thus be calculated as follows

Πt =

V𝜏P𝜏 + Rt

V𝜏 − F

V𝜏

,

(3)

|

|

𝜏∈T
∑

𝜏∈T
∑

𝜏∈T
∑
where Rt is the symmetric balancing market price for period t and F is the per MWh
trading fee.2 Note that fees on the EPEX are exclusively payable for cleared volumes
while modifications of limit orders are not charged. However, the number of modi-
fications is limited to avoid an overload of the trading system. For this purpose, the
order-to-trade ratio (OTR), defined by the number of order changes divided by the
number of placed orders, is limited to 100 by the EPEX.

Note that the above profit does not account for the cost of the forecast. Hence, Πt
can also be interpreted as the maximum price a speculative trader that employs the
above strategy would be willing to pay for the forecast.

4   Case study: setup and data

In this section, we discuss the LOB data and the forecasts of renewable output that
we use in the case study in Sects. 4.1 and 4.2, respectively. In Sect. 4.3, we discuss
how we use the data to calibrate the parameters of our strategy.

2  Clearly, after straightforward modifications to (3), the strategy would work in the same way with asym-
metric balancing prices.

1 3Intraday power trading: toward an arms race in weather…68

T. Kuppelwieser, D. Wozabal

4.1   Limit order book data

We  use  German  LOB  data  for  the  years  2017  and  2018  as  input  for  the  clearing
algorithm. The data consists of all submitted orders including information on order
changes  with  timestamps  in  milliseconds  resolution.  To  test  our  strategies,  we
implement the exact EPEX clearing algorithm in JAVA. To enable a concise discus-
sion of results, we limit our attention to hourly and quarter-hourly products and do
not consider half-hourly products.

Since  intraday  markets  in  Europe  are  increasingly  interconnected,  some  orders
in our observation period are cleared against orders from neighboring countries at
times  when  transmission  capacities  permit  cross-border  trading.  We  use  the  same
idea as Martin and Otterson (2018) to deal with this issue by reconstructing the cor-
responding foreign orders using the clearing logs included with the limit order book
data. In particular, we check for a counterpart for each executed order in the German
LOB. If such a counterpart cannot be found, we add an order with the correspond-
ing price and quantity to the German order book as described in Martin and Otter-
son (2018), making sure that we can reconstruct published prices with our clearing
algorithm. In the considered period there are 47 000 560 orders for hourly products,
1 405 055  ( 2.9% )  of  which  were  cleared  against  foreign  orders.  For  quarter-hourly
products  there  are  139 169 564  orders  with  1 495 763  ( 1.06% )  of  orders  cleared
against orders from other markets.

We identify orders for which order quantities are updated immediately after the
volume  was  fully  cleared  as  iceberg  orders.  These  orders  are  treated  as  iceberg  in
our algorithm with the overall quantity that is seen in cleared trades.

The algorithm calculates a clearing at each modification of the limit order book,
i.e., if a new order is added, an active order is updated, or an order reaches its end-
validity-time.  If  multiple  orders  with  the  same  price  arrive  simultaneously,  orders
with lower ids are cleared first.

Similar to the results in Martin and Otterson (2018), the prices and cleared quan-
tities  computed  by  our  clearing  algorithm  show  a  good  match  with  the  historical
transaction  data  published  by  the  EPEX.  We  thus  are  able  to  accurately  evaluate
how the market would have cleared additional orders added to the LOB by our trad-
ing strategies, which enables us to conduct a historical backtesting.

4.2   Forecasts of renewable output

In order to execute our strategies, we require the signals 𝜀s
t defined in (1), which are
defined  based  on  aggregated  historical  forecasts  of  solar  and  wind  power  produc-
tion in Germany kindly provided by Meteologica.3 Our data consists of day-ahead
forecasts  available  at  11  a.m.  the  day  before  delivery,  the  latest  available  intraday
forecast before gate closure, and intraday forecasts with an offset of 8, 5, and 3 hours
before the delivery of a product from July 2017 until December 2018.

3  http:// www. meteo logica. com/

1 3104

Hourly forecast-errors of intraday updates for wind and pv

69

Day-Ahead at 11:00

offset=8 hours

offset=5 hours

offset=3 hours

best intraday forecast

104

Quarter-hourly forecast-errors of intraday updates for wind and pv

1

0.5

0

-0.5

-1

h
W
M

h
W
M

1

0.5

0

-0.5

-1

Day-Ahead at 11:00

offset=8 hours

offset=5 hours

offset=3 hours

best intraday forecast

Fig. 3   Forecast errors of intraday forecasts for hourly and quarter-hourly products traded on the German
intraday power market between July 2017 and December 2018. The best forecast refers to the last fore-
cast before delivery whose exact timing slightly varies with the product

To assess the forecast errors, we use data on realized production of solar plants
and  wind  parks  for  the  four  German  control  areas  as  provided  by  ENTSOE.4  Box
plots of the forecast errors are provided in Fig. 3. We observe an increasing average
accuracy with smaller offsets as better weather forecasts and measurements of real-
ized production become available.

Our strategy is based on the expectation that errors in day-ahead forecasts are pre-
dominantly traded on the intraday market and therefore have the potential to change
intraday  prices  for  power,  i.e.,  can  be  used  as  valid  signal  for  changes  in  the  true
fundamental value of the product. Consequently, for our strategy, the most important
aspect of forecasts is whether the sign of the error of the day-ahead VRES forecast
can be predicted from the updated intraday forecasts.

|

|

𝜀s
t

t  is correctly predicted by 𝜀s

We investigate this aspect in Table  1, which displays how often the sign of the
forecast error 𝜀0
t depending on the magnitude of the sig-
 . In line with expectations, the precision of the forecast increases as the
nal, i.e.,
data is restricted to products with higher absolute values of 𝜀s
t for all s and for both
types  of  products.  It  can  also  be  observed  that  shorter  time  to  gate  closure  yields
a consistently higher hit rate. However, the increase in accuracy is only moderate.
Hence, it seems that earlier signals are not much worse while at the same time give
traders more time to react and ensure that the resulting trades are among the first that
are  based  on  updated  information.  Finally,  comparing  hourly  with  quarter-hourly
products, we observe that the latter yield worse forecasts of the sign of 𝜀0
t  in most
cases, but the differences are minute.

4  https:// trans paren cy. entsoe. eu/

1 3Intraday power trading: toward an arms race in weather…70

T. Kuppelwieser, D. Wozabal

Table 1   Distribution of the size of absolute forecast errors (in MWh) in intervals (%) and fraction of cor-
rect predictions (hits) of the sign of the forecast error 𝜀0

t  based on the magnitude of the signals 𝜀s
t

Hourly contracts
s = 8

s = 5

s = 3

Quarter hourly contracts
s = 8

s = 5

s = 3

%

Hits %

Hits %

Hits %

Hits %

Hits %

100.0

87.6

76.4

66.3

58.3

50.4

25.7

13.6

7.3

71.2

73.8

76.3

77.9

79.6

81.2

89.0

93.9

97.2

100.0

90.3

80.8

72.0

64.0

56.8

31.6

17.5

9.7

74.5

76.8

79.0

81.0

82.7

84.2

90.2

94.3

97.1

100.0

91.5

83.4

75.5

68.5

61.9

36.1

20.8

12.1

77.9

80.0

82.1

83.8

85.4

87.0

92.4

96.1

97.8

100.0

87.6

76.3

66.5

58.1

50.7

26.0

13.8

7.5

71.1

73.6

75.8

77.6

79.3

80.7

88.5

93.1

96.9

100.0

90.3

80.8

72.2

64.2

57.2

31.7

17.7

9.9

74.2

76.4

78.7

80.6

82.3

83.8

89.9

94.1

96.4

100.0

91.7

83.5

75.8

68.5

62.0

36.4

21.0

12.3

Hits

77.4

79.7

81.7

83.4

85.1

86.5

92.0

95.5

97.6

𝜀s
t

>0
|
|
>100

>200

>300

>400

>500

>1000

>1500

>2000

4.3   Calibration and evaluation of the policy

We generate counterfactual profits for our strategies in an as-if valuation of market
clearing based on the available LOB data. To that end, we inject orders generated by
the trading strategy introduced in Sect. 3 into the order book and then clear the mar-
ket according to the rules of continuous trading. Note that this introduces changes
relative to the historically observed traded quantities and prices and yields the prof-
its that could have been made, if the strategy was used. Of course, a limitation of
these experiments is that, by the very nature of our analysis and the available data,
we cannot take into account the effect that the orders placed by the strategy would
have had on the behavior of other market participants.

As discussed in the previous subsection, we use data on intraday updates of day-
ahead forecasts for VRES production as signals for our strategy. Based on a prelimi-
nary analysis of trading profits and in order to facilitate the discussion of results, we
only use the forecast published 8 hours before delivery for our policies, i.e., consider
𝜀8
t   as  signal.  This  is  also  supported  by  the  results  in  Sect.  4.2,  which  show  only  a
moderate improvement of the hit rate for later forecasts.

Furthermore,  the  choice 𝜀8

t   has  two  additional  advantages:  Firstly,  it  allows  the
policy to start trading relatively early on the updated information before most other
traders update their expectations on renewable production. Secondly, the long period
from  the  arrival  of  the  forecast  until  gate  closure  gives  the  patient  strategy  ample
time to build up the position and thereby avoid excessive liquidity costs.

We thus fix the time t1 to start the algorithm at 8 hours before delivery and set
t2 such that the policy has 5 hours to build up the position. After that, the policy
waits for 115 minutes and then starts closing the position at t3 , 65 minutes before
delivery. If the position is not closed at t4 , 35 minutes before delivery, we place a
market order to close the remaining position. Note that since the liquidity shortly
before gate closure is markedly better than in the early hours of trading, we are

1 371

able  to  choose  the  interval [t3, t4]  relatively  short  in  comparison  to [t1, t2] .  The
choice of timing and the 8 hour forecast as signal remains constant for all hourly
and quarter-hourly products and all variants of the strategy.

Having  fixed  t1, … , t4 ,  we  optimize  our  strategies  by  choosing  the  remain-
ing  parameters  𝛥± = (𝛥+, 𝛥−)  and  V ± = (V +, V −)  to  maximize  profits  using
historical  training  data  on  days  d ∈ D1 .  In  particular,  we  define  a  set  of  pos-
thresholds  L = {100 ⋅ i ∶ 0 ≤ i ≤ 20} ⊆ ℕ  and  a  set  of  volumes
sible
to
for  hourly  products  and
be
V = {1, 2, 3, 4} ∪ {5 ⋅ i ∶ 1 ≤ i ≤ 6} ⊆ ℕ for quarter-hourly products. We then use
a simple grid search separately for hourly and quarter-hourly products to solve

traded  V = {1, 5} ∪ {10 ⋅ i ∶ 1 ≤ i ≤ 30} ⊆ ℕ

( ̄𝛥±, ̄V ±) ∈ arg max

Πd(𝛥±, V ±) ∶ V ± ∈ V × V, 𝛥± ∈ L × L

}

,

(4)

{

d∈D1
∑

where Πd(𝛥±, V ±) is the sum of profits Πt as defined in (3) for all products t that go
into delivery on day d using the parameters V ±
 . For the calculation, we set
the  trading  fees  to  0.125€/MWh  (EPEX  2020a)  and  use  the  quarter-hourly  reBAP
prices available from https:// www. regel leist ung. net/ as balancing prices.

 and 𝛥±

The choice of 𝛥±

 determines whether the algorithm acts on a relatively weak
signals, i.e., for small values of 𝜀s
t , or whether a strong signal is required to open
a  position  at t1 .  Clearly,  for  small 𝛥±
  the  strategy  trades  products  for  which  the
forecast error might only have a small effect on prices, resulting in a high chance
that  prices  move  in  the  opposite  direction  due  to  the  influence  of  other  factors
such as plant outages or changes in demand. Furthermore, for small estimates of
t , the probability that the actual forecast error 𝜀0
the forecast error 𝜀s
t  has the oppos-
ing sign is significantly greater than for larger forecast errors as illustrated in the
discussion  in  Sect.  4.2.  For  example,  if  𝜀8
t   takes  a  small  positive  value  8  hours
before  delivery,  forecasting  that  there  will  be  shortage  in  production,  the  actual
day-ahead forecast error 𝜀0
t  might still be negative, i.e., VRES producers might be
long.

In contrast, larger values on 𝛥±

 make the strategy react only to strong signals
increasing the chance that forecast errors 𝜀0
t  and are driv-
ing prices in the anticipated direction in the time window [t3, t4] . However, if 𝛥±
 is
chosen too large, then the strategy will rarely open a position decreasing overall
profits. The optimization in (4) thus seeks to navigate this trade-off by choosing
optimal parameters 𝛥±
.

t  have the same sign as 𝜀8

The  second  set  of  parameter  chosen  in  (4)  are  the  traded  volumes V ±

 .  Large
volumes will generate large profits if signals are reliable and the liquidity of the
market is high, while small orders that incur less transaction costs are preferable
if  markets  are  illiquid.  Note  that  due  to  the  rules  for  building  up  a  position,  it
might be that even though V ±
 is large only smaller quantities are actually traded
in some hours, where the market is illiquid.

In the next section, we will investigate profits obtained from applying our pol-
icy  calibrated  using  a  set  of  training  days D1  to  some  (possibly)  different  set  of
days D2 ,  which  are  used  as  test  data.  If D1 = D2 ,  then  the  measured  profits  are

1 3Intraday power trading: toward an arms race in weather…72

T. Kuppelwieser, D. Wozabal

insample  profits,  i.e.,  the  policy  is  calibrated  using  the  same  data  that  is  used
to evaluate profits. If D1 ∩ D2 = � , the profits for the days D2 are out-of-sample
profits.

5   Results and discussion

In  this  section,  we  present  the  results  of  a  case  study  using  1.5  years  of  German
LOB data from 01.07.2017 until 31.12.2018. In Sect. 5.1, we explore the in-sample
profits  made  by  optimally  parameterized  patient  and  impatient  policies  for  hourly
and quarter-hourly contracts using both the actual forecast error 𝜀0
t  . In
Sect. 5.2, we focus on the more profitable patient strategies and partition the data in
calibration and test sets optimizing implementable policies, which we evaluate out-
of-sample for the year 2018.

t  as well as 𝜀8

We consider exclusively products where the day-ahead forecast, the 8-hour ahead
forecast, as well as the actual production of renewables are available. Furthermore,
we exclude the third hour on the 29.10.2017 and 28.10.2018 due to data problems
connected  with  day-light  saving  and  the  whole  of  the  27.10.2018  due  to  missing
LOB  data.  Additionally,  we  exclude  69  hourly  and  190  quarter-hourly  products
due to an empty LOB shortly before the market closes. This leaves us with 12 492
hourly  and 50 055  quarter-hourly  products  for  the  period  between  01.07.2017  and
31.12.2018,  excluding  in  total 5%  of  hourly  products  and  4.85%  of  quarter-hourly
products.

5.1   Insample results

In  this  section,  we  analyze  the  optimal  parameter  choice  for V ±
  as  well  as
optimal profits, setting both the training data, D1 , and the test data, D2 , to the period
ranging from 01.07.2017 to 31.12.2018. Since we use the same data to calibrate the
parameters and calculate the profits, the resulting optimal policy violates non-antic-
ipativity  and  is  therefore  not  practically  implementable.  In  particular,  in  reality,  a
trader is forced to choose a trading strategy ex-ante, without knowing market out-
comes. The results in this section can therefore be regarded as a in-sample evalua-
tion of optimal profits.

  and 𝛥±

As  discussed  in  the  previous  section,  we  start  building  up  a  position  8  hours
before  delivery  for  every  hourly  and  quarter-hourly  product  in  the  observation
period and optimize both the patient and impatient trading strategy. To that end, we
evaluate the profit separately for products with positive and negative forecast error
for  the 21 × 32 = 672  (for  hourly  products)  and 21 × 10 = 210  (for  quarter-hourly
products) parameter combinations in L × V . The parameters of the policy are kept
constant for all products in the observation period.

We  start  by  analyzing  the  patient  strategies  based  on  actual  forecast  errors  𝜀0
t  .
Figure  4  shows  how  the  choice  of  parameters  influence  the  profits  for  the  patient
strategy  with  the  red  triangles  marking  the  maximum  profit.  Observing  results  for
fixed thresholds 𝛥±
 , it can be seen that, as expected, higher volumes lead to higher

1 3Hourly products

0>0
t

Profit for hourly products

0<0
t

73

105

15

10

5

2000

1000

Threshold in MWh

0

0

105

15

10

5

200

100

300

2000

1000

Volume in MWh

Threshold in MWh

0

0

300

200

100

Volume in MWh

Quarter-hourly products

0>0
t

Profit for quarter-hourly products

0<0
t

105

1
0
-1
-2
-3

2000

1000

Threshold in MWh

0

0

105

2

0

-2
2000

1000

20

10

30

Volume in MWh

Threshold in MWh

0

0

30

20

10

Volume in MWh

Fig. 4   Optimal profits of the patient trader for real forecast errors for hourly products (above) and quar-
ter-hourly products (below)

Table 2   Profits of insample strategies in €  for hourly contracts (H) and quarter-hourly contracts (QH)

Actual ( 𝜀0
t )

Patient

Impatient

Forecast ( 𝜀8
t )

Patient

Impatient

QH

H

QH

H

QH

H

QH

H

Positive

Profit

192659

1686492

−48892

65167

48438

10

300

1

20

4

V +

𝛥+

V −

𝛥−

Negative

Profit

214774

1560323

−17350

3684

52589

10

270

1

1

4

Overall

Profit

407433

3246816

−66242

68852

101027

488418

−34703

5775

300

1000

2000

1600

0

1000

2000

2000

700

1100

2000

2000

200

1200

2000

1600

157222

200

−30937

168

1

1

331196

270

−3766

5607

1

20

overall profits but due to limited liquidity, the increase is not linear and from a cer-
tain  threshold  on,  there  is  even  a  decrease  in  profits  for  increasing V ±
 .  Similarly,
there is a sweet-spot for the required strength of the signal: Profits are initially rising
in the threshold 𝛥±
 and then start to fall again illustrating the trade-off between fre-
quent trading on weaker signals and infrequent trading on stronger signals.

The  profits  and  the  optimal  parameter  choices  for  the  considered  policies  are
listed in the first panel of Table 2. The results show that, at least in-sample, a trading
strategy that is based on a hypothetical 100% accurate intraday update of the day-
ahead forecast of renewable output yields significant positive profits for both hourly
and quarter hourly products.

Looking  at  the  profits  in  detail,  two  observations  can  be  made.  Firstly,
hourly contracts are one order of magnitude more profitable than quarter-hourly

1 3Intraday power trading: toward an arms race in weather…74

105

1

0

-1
2000

Hourly products

8>0
t

Profit for hourly products

8<0
t

T. Kuppelwieser, D. Wozabal

105

3

2

1

0

-1
2000

1000

300

200

100

Volume in MWh

Threshold in MWh

0

0

300

200

100

Volume in MWh

1000

Threshold in MWh

0

0

Quarter-hourly products

8>0
t

Profit for quarter-hourly products

8<0
t

104

4

2

0

-2

-4
2000

1000

Threshold in MWh

0

0

104

4

2

0

-2

-4
2000

1000

20

10

30

Volume in MWh

Threshold in MWh

0

0

30

20

10

Volume in MWh

Fig. 5   Optimal profits of the patient trader for forecast errors with an offset of 8 hours for hourly prod-
ucts (above) and quarter-hourly products (below)

contracts  although  there  are  4  times  more  products  of  the  latter.  Looking  at  the
optimal parameter choices and in particular at the low quantities traded for quar-
ter hourly products, it becomes clear that this is mostly due to missing liquidity
for  quarter-hourly  products,  which  start  to  affect  profits  already  for  much  lower
volumes than this is the case for hourly products. Secondly, we can observe that
the  patient  trading  strategy  based  on  limit  orders  performs  significantly  better
than the impatient strategy which places market orders. In particular, the results
suggest  that  the  impatient  strategy  does  not  work  at  all  for  quarter  hourly  prod-
ucts and only produces moderate profits for hourly products. Again, this is due to
the high liquidity costs in the market which has to be fully born by the impatient
strategy.

Next, we analyze the policy for the more realistic case that the signal is based
on an updated forecast instead of the actual production, i.e., we use 𝜀8
t  instead of
𝜀0
t  as a signal. We again plot the relationship of the parameters of the patient strat-
egy and the profit in Fig. 5. The plot exhibits many of the same characteristics as
Fig. 4 with the difference that higher volumes V ±
 lead more quickly to less prof-
its, i.e., optimal volumes tend to be smaller. This is due to the lower quality of the
signal which in many cases leads to a lower than expected forecast error causing
losses for policies that bid too aggressively based on 𝜀8
t .

Turning  to  the  value  of  the  strategy  in  panel  2  of  Table  2,  we  observe  that,
compared to the strategy based on 𝜀0
t  , profits are significantly lower for the patient
trader  and  stagnate  at  low  levels  for  the  impatient  trader.  Again,  as  for  𝜀0
t  ,  the
hourly  strategies  yield  higher  profits  but  the  relative  gap  is  smaller  than  for  the
perfect forecast. Although the signal is of a lower quality, surprisingly, the opti-
mal parameters are rather similar to those found for 𝜀0
t  , although optimal volumes
tend to be slightly lower, explaining parts of the lower profits.

1 3Table 3   Amount of net capital invested per day for the different trading strategies

Hour

Patient

Impatient

Quarter Hour

Patient

Impatient

Mean

Max

Min

−22163

−57795

−68

−2246

404

1597

−141

−276

5798

117889

0

5277

21450

49375

2613

4069

−210712

−387446

−1015

−23798

−24865

−33657

−19710

−10835

𝜀8
t
𝜀0
t
𝜀8
t
𝜀0
t
𝜀8
t
𝜀0
t
𝜀8
t
𝜀0
t

75

Std

40655

75280

159

4015

6256

10711

1047

1424

The  difference  between  the  profits  of  the  strategies  based  on  𝜀0

t   can  be
interpreted as a lower bound on the value of improved forecasting, which is substan-
tial for the patient trader.

t   and  𝜀8

To  put  the  profits  in  perspective,  we  evaluate  daily  capital  requirements  as  the
sum of the cost of opening the positions for all products traded on a day, netting out
positive and negative costs. The results are displayed in Table 3 and indicate that, on
average, the strategy requires a negative amount of capital with low positive maxi-
mal values. The profits displayed in Table 2 can therefore be realized with a small
amount of risk capital and offer a high return on investment.

5.2   Out‑of‑sample results

In  this  section,  we  evaluate  strategies  out-of-sample  in  the  time  period  from
01.01.2018 until 31.12.2018. More specifically, we study non-anticipative strategies,
i.e., make sure that decisions at any point in time only depend on information avail-
able at that time (Shapiro et al. 2009). Since the impatient strategy performs poorly
in-sample,  we  exclusively  focus  on  the  patient  strategy  for  the  experiments  in  this
section.

 and V ±

We use a rolling window setting for the out-of-sample evaluation and re-optimize
the parameters 𝛥±
 every day using the last six months of data for the calibra-
tion. More specifically, we start our evaluation on the 01.01.2018 using 180 days of
training data spanning the period from 04.07.2017 until 30.12.2017 to calibrate 𝛥±
and V ±
 by grid search as in (4). We then evaluate the profits of the resulting strategy
on  the  01.01.2018  and  proceed  to  the  02.01.2020  by  including  the  31.12.2017  in
the training sample while removing the 04.07.2017 and retrain our policy to obtain
out-of-sample profits for the 02.01.2020. In this manner, we build up out-of-sample
profits for every product traded in the year 2018.

Figure 6 shows the results of our experiment for hourly products. The first panel
displays the development of cumulative profits of the strategy based on the signal 𝜀8
t
and 𝜀0
t  , it becomes clear that while profits over one year
of trading are significantly positive and close to €200,000, there are single days with
large losses and extended time periods where the strategy did not generate profits.

t  . Looking at the graph for 𝜀8

1 3Intraday power trading: toward an arms race in weather…
T. Kuppelwieser, D. Wozabal

Cumulative Profit

76

8
t
0
t

105

2

1.5

1

0.5

0
Jan

Long position

Short position

h
W
M

200
0
-200

Jan

Feb

Mar

Apr

May

104

2

0

-2
Jan

2000
0
-2000

Feb

Mar

Apr

May

Feb

Mar

Apr

May

Jun

Jul
Open volumes

Aug

Sep

Oct

Nov

Dec

Jun
Aug
Jul
Value of open positions

Sep

Oct

Nov

Dec

Jun

Jul
Transactions on balancing market

Aug

Sep

Oct

Nov

Dec

106
2

1.5

1

0.5

0
Jan

2018

2018

2018

2018

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Fig. 6   Cumulative profit of the optimal insample and out-of-sample strategy for hourly products in the
first  panel.  Panels  2  and  3  display  the  opened  volume  and  the  financial  value  of  the  positions  held  by
the out-of-sample strategy. Panel 4 shows daily payments on the balancing market for the out-of-sample
strategy

Comparing with the profits based on 𝜀0
t  , we see that, as in the insample results, a per-
fect intraday update of the forecast increases the profits by one order of magnitude.
Furthermore, the strategy that is based on 𝜀0
t  exhibits a much smoother increase in
cumulative profits with fewer losses. This suggests that the losses for 𝜀8
t  are mainly
due to inaccurate forecasts and suggests that better forecasts can not only increase
the profits of the strategy but also reduce the variance of daily profits and therefore
the inherent risk of trading.

Turning our attention to panel 2 and 3 of Fig. 6, which display the size and the
value  of  the  open  position  after  time  t2  for  the  strategy  based  on  𝜀8
t  ,  we  see  that
the strategy takes long and short positions of up to 200 MWh with a roughly equal
share of long and short positions. The position values suggest that the capital at risk
for  single  products  does  not  exceed  €20,000.  It  can  also  be  observed  that  there  is
a change in the strategy within the observation period: in the first few months the
algorithm triggers frequently and short positions tend to be smaller than long posi-
tions. In the summer months, there is generally less trading activity, possibly due to
lower wind production which lead to smaller forecast errors.

Finally, the last panel of Fig. 6 displays netted daily payments from balancing for
products for which the position cannot be closed until gate closure. As can be seen,
there are only 7 days with a requirement for balancing. In most of these instances
the payment is negative, i.e., the trader has to pay to the grid operator for balancing.
However, as balancing is rare and none of the single payments to the balancing mar-
ket exceed €5,000, we conclude that balancing fees are not a major driver of profits
for the chosen strategy.

Figure  7  presents  an  analogous  analysis  for  trading  of  quarter-hourly  products.
The  plot  of  the  cumulative  profits  of  the  strategy  reveals  that,  consistent  with  the
insample results, the strategy is less profitable for quarter-hourly products than for

1 3Cumulative Profit

77

105
3

2

1

8
t
0
t

104

6

4

2

0
Jan

Long position

Short position

h
W
M

20
0
-20

Jan

Feb

Mar

Apr

May

1000

0

-1000

Feb

Mar

Apr

May

Jun

Jul
Open volumes

Aug

Sep

Oct

Nov

Dec

0
Jan

2018

Jun
Aug
Jul
Value of open positions

Sep

Oct

Nov

Dec

2018

2018

2018

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

4000
2000
0
-2000

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Fig. 7   Cumulative  profits,  traded  volumes,  value  of  traded  positions,  and  daily  balancing  payments  for
quarter-hourly products (see Fig. 6 for a more detailed description of panels)

hourly products. As with the insample results and the results on hourly products, the
strategy based on perfect forecast is one order of magnitude more profitable than the
strategy based on 𝜀8

t  and at the same time is less volatile.

A closer look at the cumulative profits over time reveals that, although the trad-
ing  of  quarter-hourly  products  yields  only  roughly  one  fourth  of  the  profits  that
can be earned with hourly products, individual earnings for each product fluctuate
much less than in the case for hourly products. This is due to the generally smaller
positions taken by the optimal strategies which lead to less exposure to market risk
as  evidenced  by  panels  2  and  3  of  Fig.  7.  Observing  these  plots  also  reveals  that
there are less seasonal trends in the traded quantities for the quarter-hourly strategy.
Finally,  the  last  panel  of  the  figure  documents  that,  similar  to  the  case  for  hourly
products, balancing occurs infrequently and therefore only plays a minor role.

Table 4 provides detailed figures for overall profits, balancing costs, and summary
statistics for profits per product for both hourly and quarter-hourly trading. Looking
at the summary statistics of profits per product confirms that trading quarter-hourly
products yields profits with a lower dispersion and therefore lower capital require-
ment.  Furthermore,  conducting  t  tests,  we  see  that  all  average  per-product  profits
are significantly greater than zero at least at the 0.05% level and, due to their lower
standard deviation, the significance is greatly increased for quarter-hourly products.

t   as  opposed  to 𝜀8

We  observe  that  the  number  of  traded  products  is  nearly  twice  as  high  for  the
strategies  based  on 𝜀0
t  .  Furthermore,  due  to  the  lower  thresholds
for  trading,  the  relative  amount  of  traded  products  is  larger  for  the  quarter-hourly
products. Despite this and the fact that there are more quarter-hourly products, the
number  of  single  trades  that  get  cleared  as  result  of  our  strategy  is  nearly  as  high
for hourly products as for quarter-hourly products. This is due to the larger quanti-
ties traded for the hourly products which often cannot be cleared at once but require
trades with several of counter-parties dispersed over a longer time span.

1 3Intraday power trading: toward an arms race in weather…78

T. Kuppelwieser, D. Wozabal

Table 4   Descriptive statistics
for the profits of different
strategies and the number of
traded products and trades

Hour
𝜀8
t

𝜀0
t

Quarter Hour
𝜀8
t

𝜀0
t

Profit

194385 2087823 62724

297656

Balancing Costs

−9865

31202

4214

Mean

Standard Deviation

p value of t test

Minimum

1% quantile

10% quantile

Median

90% quantile

99% quantile

Maximum

Number of products

Number of traded products

8055

8.52

99

22.29

239.43

968

2110

1.8

44

0.0316

0.0000 0.0000

0.0000

−21220 −93030 −1731 −2717

−2814 −3740

−394

−929

0

522

3137

0

1824

5600

15908

32174

8288

2853

8288

4732

−98

−22

0

28

118

1836

33189

21425

−246

−30

0

69

300

3518

33187

21044

Number of individual trades 136863 311802

223593 367719

6   Conclusion and outlook

In  this  paper,  we  propose  a  simple  parametric  trading  strategy  for  continuous
intraday  trading  on  power  markets  based  on  intraday  updates  of  forecast  VRES
production. Our strategy generates significant out-of-sample profits for one year
of  trading  by  an  arbitrage  trader  that  owns  no  production  assets,  has  no  own
demand, and operates on the German intraday market.

Our results show that one of the most important factors to consider when trad-
ing  on  the  intraday  markets  is  the  lack  of  liquidity  and  the  resulting  transaction
costs. In particular, any algorithmic trading strategy has to cope with the limited
liquidity  of  the  market,  which  on  the  one  hand  side  drives  price  variability  and
thereby  may  favorably  influence  profits  but  on  the  other  side  makes  it  harder  to
capitalize on informational advantages, as any speculative trading strategy has to
overcome the bid-ask spread.

We  mitigate  these  problems  by  designing  a  patient  trading  strategy  that  uses
limit  orders  instead  of  market  orders  and  allows  for  an  extended  time  to  trade
waiting for favorable orders to arrive on the respective other side of the market.
We show that this patience is key to making profits and that the impatient strategy
incurs substantial liquidity costs that absorb most of the profit that can be gener-
ated with weather related information.

Additionally,  our  results  demonstrate  that  the  German  intraday  market  for
power  is  not  semi-strong  efficient,  since  publicly  available  data  on  renewable
power  production  forecasts  can  be  used  to  define  a  trading  strategy  that  gener-
ates  significant  profits  while  requiring  a  relatively  small  amount  of  risk  capital.

1 379

Furthermore, there would be a substantial potential for even more profitable trad-
ing if forecasts were to further improve.

Clearly, since there is a finite amount of money to be earned with weather-based
trading,  the  presented  strategy  is  self-cannibalizing,  i.e.,  the  profits  depend  on
how  many  other  traders  employ  similar  strategies.  However,  this  is  the  case  with
any  algorithmic  trading  policy  and  therefore  does  not  make  the  approach  obsolete
but rather implies that only the most competent traders are able to capitalize on the
respective signal.

This  implies  that  trading  strategies  similar  to  the  one  presented  in  this  paper,
could be a driver for continued innovations in short-term forecasting of VRES pro-
duction as traders compete in the accuracy of their forecasts. This might trigger an
arms race in forecasting with market participants trying to capitalize on ever improv-
ing  forecasts.  Algorithmic  traders  would  consequently  help  the  market  to  process
information more efficiently thereby generating price signals of a higher quality and
at the same time improve market liquidity.

Additional  market  liquidity  would  in  turn  make  weather-based  trading  easier
and  more  profitable  as  is  demonstrated  by,  for  example,  the  higher  profits  gener-
ated  by  our  algorithm  for  the  more  liquid  hourly  products  as  opposed  to  the  less
liquid quarter-hourly products. Hence, such a trend could, at least for a while, feed
itself and therefore has the potential to lead to a much more responsive intraday mar-
ket. Therefore, as opposed to the arguably adverse welfare effects of the arms race
for speed that characterizes algorithmic trading on financial markets (Budish et al.
2015), this development would likely unlock positive welfare effects.

In our study, we take great care to evaluate the proposed trading strategy as real-
istically as possible. To that end, we use detailed limit order book data on submit-
ted orders to calculate profits based on an exact implementation of the EPEX clear-
ing algorithm. Furthermore, we make sure that all our policies are non-anticipative,
enforcing a strict separation of training and test data.

However, there are still some limitations in our study. Most importantly, we work
with historical order data to compute counterfactual profits of our strategy in an as-if
fashion. This analysis by design cannot take into account the reaction of other mar-
ket participants to our trading strategy. A completely different experimental design
simulating market outcomes, using either artificial agents or laboratory experiments
with human traders, would be required to overcome this shortcoming.

Another  shortcoming  of  our  analysis  concerns  the  quality  of  the  order  book
data.  In  particular,  we  only  use  German  orders  even  if  a  small  amount  of  orders
is cleared via cross-border trades. Although we  reconstruct the  foreign  orders that
were historically cleared against German orders, we cannot completely capture the
influence that cross-border trading would have had on our results. However, due to
transmission line restriction, the fraction of German orders cleared with orders from
other countries is rather small (below 5%) and we therefore think that our results are
robust with respect to this influence.

Furthermore, the order book data supplied by the EPEX is imperfect in many
ways  impeding  a  fully  accurate  what-if  analysis.  In  particular,  the  end  validity
date of cleared orders is overwritten with the clearing time which makes it impos-
sible to reconstruct the actual end-validity dates of cleared orders. Additionally,

1 3Intraday power trading: toward an arms race in weather…80

T. Kuppelwieser, D. Wozabal

it  is  hard  to  correctly  identify  iceberg  orders  and  market  orders  from  the  data.
However, since, apart from very few exceptions, our implementation of the clear-
ing algorithm correctly reconstructs historically observed prices, we are confident
that the cumulative impact of these issues on our results is negligible.

This  work  opens  some  avenues  for  further  research  in  weather-based  auto-
mated  trading  algorithms  on  intraday  power  markets.  In  particular,  it  is  easy  to
conceive improvements in the proposed trading strategies.

One  obvious  example  is  the  inclusion  of  maximum  and  minimum  prices  to
build up a position as additional parameters of the strategy, preventing trades at
unfavorably high or low prices. For similar reasons, basing the strategy on proba-
bilistic forecasts instead of point forecasts (e.g., Pinson et al. 2007; Tankov and
Tinsi 2021) might help to avoid trading on noisy signals with a high variance that
are  at  risk  to  be  substantially  off.  The  policy  can  probably  also  be  improved  by
taking into account several forecasts and dynamically adapting the orders in the
LOB as well as the positions to newly arriving information.

Furthermore,  it  would  be  interesting  to  extent  the  strategy  to  a  broader  set-
ting, which incorporates assets such as renewable generation or electricity storage
as well as possibly other markets including balancing markets and the day-ahead
market.

This and other possible refinements would lead to a larger number of parameters
and  would  therefore  necessitate  a  more  sophisticated  optimization  approach.  Pos-
sible improvements in this direction could be based on machine learning techniques
such as artificial neural networks or reinforcement learning (e.g., Bertrand and Papa-
vasiliou  2019).  Alternatively,  one  could  employ  state-of-the  art  black  box  solvers
such as CMAES (see Hansen et al. 2010) to find optimal parameters.

Another large area of improvement is in the use of data. Firstly, it is conceivable
that  the  quality  of  the  order  book  data  will  improve  in  the  coming  years  making
more accurate analysis of the profits possible and mitigate most of the data related
problems described above. Furthermore, as more data becomes available the train-
ing of strategies will become easier and the results more reliable. Secondly, a more
careful  selection  of  training  data  might  benefit  the  performance  of  the  algorithm.
For the present paper, we simply use the last 180 days of data to train our strategy
for  all  products.  This  implies  that  data  from  different  times  of  the  day,  weekdays,
and seasons is used indiscriminately to train the strategy for all products in the test
data. Making sure that the training data matches the test data more closely and thus
enabling  different  strategies  for  different  weekdays,  seasons,  and  products  has  the
potential to increase trading profits.

Acknowledgements  We are thankful to Meteologica for kindly allowing us to use their renewable pro-
duction  forecasts,  which  are  central  to  the  trading  strategies  proposed  in  this  article.  In  particular,  we
want to express our gratitude to Edoardo Giacomin who was enormously helpful in obtaining and under-
standing the forecasts.

Funding  Open Access funding enabled and organized by Projekt DEAL.

Data availability and materials  The data that support the findings of this study are available from Meteo-
logica ( forecasts of renewable production) as well as from the EPEX Spot (order book data) but restric-
tions apply to the availability of these data, which were used under license for the current study, and so

1 381

are not publicly available. Data on forecasts are however available from the authors upon request and with
permission of Meteologica.

Open Access  This  article  is  licensed  under  a  Creative  Commons  Attribution  4.0  International  License,
which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long
as  you  give  appropriate  credit  to  the  original  author(s)  and  the  source,  provide  a  link  to  the  Creative
Commons licence, and indicate if changes were made. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line
to the material. If material is not included in the article’s Creative Commons licence and your intended
use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permis-
sion directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/
licenses/by/4.0/.

References

Balardy C (2018) An empirical analysis of the bid-ask spread in the German power continuous mar-

ket. Working paper

Bertrand G, Papavasiliou A (2019) Adaptive trading in continuous intraday electricity markets for a

storage unit. IEEE Trans Power Syst

Boomsma TK, Juul N, Fleten S-E (2014) Bidding in sequential electricity markets: the Nordic case.

Eur J Oper Res 238(3):797–809

Budish E, Cramton P, Shim J (2015) The high-frequency trading arms race: frequent batch auctions as

a market design response. Q J Econ 130(4):1547–1621 (7)

Bundesnetzagentur  (2012)  Beschluss  bk6-12-024.  https:// www. regel leist ung. net/ ext/ static/ rebap.

[Online; Accessed 21-Febrary-2021]

Dideriksen AF, Sekkesæter S, Fleten S-E, Aasgõrd EK, Skjelbred H-I (2019) Operational use of mar-
ginal cost curves for a hydropower producer trading in the intraday market. In: 2019 16th Inter-
national conference on the European energy market (EEM), pp 1–6

Engmark E, Sandven H, Fleten S-E, Klæboe G (2018) Stochastic multistage bidding optimisation in
an intraday market with limited liquidity. In: 2018 15th International conference on the european
energy market (EEM), pp 1–5

EPEX  (2020a)  Epex  spot  operational  rules.  https:// www. epexs pot. com/ sites/ defau lt/ files/ downl oad_

center_ files/ EPEX% 20SPOT% 20Mar  ket% 20Rul es_6. zip. [Online; accessed 21-November-2020]

EPEX (2020b) Epex spot annual report 2019. https:// www. epexs pot. com/ sites/ defau lt/ files/ downl oad_
center_ files/ Epex- spot- 2019_ 200703_ Planc  he. pdf. [Online; Accessed 22-November-2020]
European  Commission  (2015)  Commission  regulation  2015/1222.  https:// eur- lex. europa. eu/ legal-

conte nt/ EN/ TXT/? uri= CELEX% 3A320 15R12 22. [Online; Accessed 22-November-2020]

Garnier E, Madlener R (2014) Balancing forecast errors in continuous-trade intraday markets. SSRN

Electron J 6:01

Glas S, Kiesel R, Kolkmann S, Kremer M, von Luckner NG, Ostmeier L, Urban K, Weber C (2019)
Intraday  renewable  electricity  trading:  Advanced  modeling  and  optimal  control.  In  Progress  in
industrial mathematics at ECMI 2018, pp 469–475. Springer

Glas S, Kiesel R, Kolkmann S, Kremer M, von Luckner NG, Ostmeier L, Urban K, Weber C (2020)
Intraday renewable electricity trading: advanced modeling and numerical optimal control. J Math
Ind 10(1):3

Goodarzi S, Perera HN, Bunn D (2019) The impact of renewable energy forecast errors on imbalance

volumes and electricity spot prices. Energy Policy 134:110827

Hansen  N,  Auger  A,  Ros  R,  Finck  S,  Pošík  P  (2010)  Comparing  results  of  31  algorithms  from  the
black-box optimization benchmarking bbob-2009. In: Proceedings of the 12th annual conference
companion on Genetic and evolutionary computation, pp 1689–1696

Hu X, Jaraitė J, Kažukauskas A (2021) The effects of wind power on electricity markets: a case study

of the Swedish intraday market. Energy Econ 96

Karanfil F, Li Y (2017) The role of continuous intraday electricity markets: The integration of large-

share wind power generation in Denmark. Energy J 38(2)

1 3Intraday power trading: toward an arms race in weather…82

T. Kuppelwieser, D. Wozabal

Kath  C,  Ziel  F  (2018)  The  value  of  forecasts:  quantifying  the  economic  gains  of  accurate  quarter-

hourly electricity price forecasts. Energy Econ 76:411–423

Kath  C,  Ziel  F  (2020)  Optimal  order  execution  in  intraday  markets:  minimizing  costs  in  trade

trajectories

Kiesel R, Paraschiv F (2017) Econometric analysis of 15-minute intraday electricity prices. Energy Econ

64:77–90

Koch  Christopher  (2021)  Intraday  imbalance  optimization:  incentives  and  impact  of  strategic  intraday

bidding behavior. Energy Syst 13:409–435

Kremer M, Kiesel R, Paraschiv F (2020) An econometric model for intraday electricity trading. Philos

Trans Royal Soc A 379:20190624

Kremer  M,  Kiesel  R,  Paraschiv  F  (2020b)  Intraday  electricity  pricing  of  night  contracts.  Energies

13(17):4501–0

Kulakov S, Ziel F (2019) The impact of renewable energy forecasts on intraday electricity prices. Energy

J 10

Kumbartzky N, Schacht M, Schulz K, Werners B (2017) Optimal operation of a CHP plant participating
in the German electricity balancing and day-ahead spot market. Eur J Oper Res 261(1):390–404
Kuppelwieser T, Wozabal D (2020) Liquidity costs on intraday power markets: continuous trading versus

auctions. Working paper

Maciejowska K, Nitka W, Weron T (2019) Day-ahead vs. intraday-forecasting the price spread to maxi-

mize economic benefits. Energies 12(4):631

Malkiel BG, Fama EF (1970) Efficient capital markets: a review of theory and empirical work. J Financ

25(2):383–417

Martin H, Otterson S (June 2018) German intraday electricity market analysis and modeling based on the
limit order book. In: 2018 15th international conference on the European energy market (EEM), pp
1–6

Milligan M, Frew BA, Bloom A, Ela E, Botterud A, Townsend A, Levin T (2016) Wholesale electricity
market  design  with  increasing  levels  of  renewable  generation:  Revenue  sufficiency  and  long-term
reliability. Electr J 29(2):26–38

Monteiro C, Fernandez-Jimenez LA, Ramirez-Rosado IJ (2020) Predictive trading strategy for physical

electricity futures. Energies 13(14):3555

Narajewski  M,  Ziel  F  (2020)  Econometric  modelling  and  forecasting  of  intraday  electricity  prices.  J

Commod Mark 19:100107

Oksuz I, Ugurlu U (2019) Neural network based model comparison for intraday electricity price forecast-

ing. Energies 12(23):4557

Pinson  P,  Chevallier  C,  Kariniotakis  G  (2007)  Trading  wind  generation  from  short-term  probabilistic

forecasts of wind power. IEEE Trans Power Syst 22:1148–1156

Pollitt M (2019) The european single market in electricity: an economic assessment. Rev Ind Organ pp

1–25

Rintamäki T, Siddiqui AS, Salo A (2020) Strategic offering of a flexible producer in day-ahead and intra-

day power markets. Eur J Oper Res 284(3):1136–1153

Shapiro A, Dentcheva D, Ruszczyśki A (2009) Lectures on stochastic programming: modeling and the-

ory. MOS-SIAM series on optimization. SIAM, Philadelphia

Shinde P, Amelin M (2019) A literature review of intraday electricity markets and prices. In: 2019 IEEE

Milan PowerTech, pp 1–6 (2019). https:// doi. org/ 10. 1109/ PTC. 2019. 88107 52

Skajaa  A,  Edlund  E,  González  M  (2015)  Intraday  trading  of  wind  energy.  IEEE  Trans  Power  Syst

30(6):3181–3189

Spodniak P, Ollikka K, Honkapuro S (2021) The impact of wind power and electricity demand on the

relevance of different short-term electricity markets: the Nordic case. Appl Energy 283

Sánchez de la Nieta A, Paterakis NG, Gibescu M (2020) Participation of photovoltaic power producers in
short-term electricity markets based on rescheduling and risk-hedging mapping. Appl Energy 266
Séguin S, Fleten S-E, Côté P, Pichler A, Audet C (2017) Stochastic short-term hydropower planning with

inflow scenario trees. Eur J Oper Res 259(3):1156–1168

Tankov P, Tinsi L (2021) Decision making with dynamic probabilistic forecasts. Technical report, Avail-

able at arXiv https:// arxiv. org/ abs/ 2106. 16047

Viehmann  J  (2017)  State  of  the  German  short-term  power  market.  Zeitschrift  für  Energiewirtschaft

41(2):87–103

Weron R (2014) Electricity price forecasting: A review of the state-of-the-art with a look into the future.

Int J Forecast 30(4):1030–1081

1 3Wozabal D, Rameseder G (2020) A Stochastic Optimization Approach for Optimal Bidding of a Virtual

Power Plant on the Spanish Spot Market for Electricity. Eur J Oper Res 280(2):639–655

Publisher’s Note  Springer Nature remains neutral with regard to jurisdictional claims in published maps
and institutional affiliations.

83

1 3Intraday power trading: toward an arms race in weather…