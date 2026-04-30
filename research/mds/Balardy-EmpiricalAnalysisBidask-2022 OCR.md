An Empirical Analysis of the Bid-ask Spread in the Continuous
Intraday Trading of the German Power Market

Clara Balardy”

ABSTRACT

Liquidity is decisive for a well-functioning market. As most of the literature on the
subject is based on financial markets, the extrapolation of its insights to the power
market is  fragile. This paper shows the specificities of liquidity of the German
power market. Using the bid-ask spread as a proxy, thanks to the detailed order
book for the hourly contracts, I  first describe the evolution of the liquidity over
the trading session. The bid-ask spread has a “L-shaped” pattern over it.  Second,
1  identify the four main drivers of the bid-ask spread: the volatility,  the adjust-
ments’ need (forecast errors), the activity and the concentration of the market. I
find that an increase of the volatility or the market concentration increases the
bid-ask spread while an increase of the adjustments’ need or the market activity
decreases it.

Keywords: Bid-ask spread, Market depths, Continuous market, Power market

<https://doi.org/10.5547/01956574.43> 3.cbal

1. INTRODUCTION

Liquidity is  the major component of a well-functioning market. More liquid is  a market,
easier it is  for a market participant to find a trading counterpart to match its requirements. A  typical
proxy for liquidity is  the bid-ask spread that is  the difference between the lowest price for which a
seller is willing to sell a megawatt hour of electricity and the highest price that a buyer is  willing to
pay for it.

Market participants gain opportunities by exploiting the bid-ask spread which can be inter-
preted as a premium for immediate execution (Demsetz, 1968). For example, in a setup where the
best sell order is at 35€ per MWh and the best buy order is at 32€ per MWh, if the best buyer (resp.
seller) wants to be immediately executed, she has to increase (resp. decrease) her unit price by 3€. It
can also be interpreted as an implicit transaction cost; the smaller the bid-ask spread is,  the smaller
is the implicit transaction cost for the traders and so the end-consumers. Further, the bid-ask spread
is a showcase for the quality of the market.

Table 1: Example of an order book
Bid

Ask

Quantity
20

Price
35
36
39
2

Quantity
32
31
29
28
25

Price
4
15
7
9
30

a  Université Paris-Dauphine, PSL Rescarch University, LEDa, [SDFi].  E-mail: clara balardy@gmail com

The Energy Journal, Vol.  43, No.  3.  Copyright © 2022 by the IAEE. All rights reserved.

229

‘This content downloaded from
IIIII186.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC TIIIIIIT
All use subject to <https://about> jstor.org/terms

230/ The Energy Journal

The German market is  the most liquid continuous power market in Europe where about
53% of the German consumption was traded on in 2015. The same year, almost 20 millions of euros
were traded each week on the market. It is particularly interesting to study the bid-ask spread of the
German continuous power market because the market faces a growing attention in the public debate.
First, the continuous market has been playing a growing role in the integration of the renewable en-
ergy sources (RES); thus, the traded volume increased by about 170% from 2012 to 2018. It is then
a benchmark for the other European countries with a growing renewable capacity. Second, it is also
important to understand the liquidity of the market in the context of the European single intraday
coupling (SIDC) project where new countries are adopting continuous trading such as Spain or Italy.
Despite similarities between the continuous spot power market and the traditional financial
markets in their mechanisms, there are some major differences due to the physical aspect of power:
it  is  not storable and market participants  are balance responsible.'  In comparison to  the financial
markets, the power market has a lower liquidity, a higher volatility due to the renewable production,
a higher concentration and a highly inelastic demand (Dupuis et al.,  2016). Thus, the one-size-fits-
all approach is not straightforward and the results of the so-called microstructure literature may not
hold in the context of electricity markets. For example, in the financial literature, the pattern of the
bid-ask spread (“L-shaped” versus “U-shaped™) is  explained by the difference in the market mak-
ing process (Lhabitant and Gregoriou, 2008); this result cannot be transposed to the power market
because it does not have market makers. The reason behind the “L-shaped” pattern of the bid-ask
spread in the power market can be explained by the urge to trade close to the delivery: there is a peak
of activity during the last hours of the trading session.

This paper is relevant for the market participants in order to decide when to participate in
the market during the trading session in order to reduce their implicit transaction costs. It  is  also
relevant for the exchange as a guidance for market design. An example can be the introduction of
official market markers? in order to increase the liquidity of the market; thus, what would be a decent
level of bid-ask spread to ask market markers if the exchange wants to implement some? Marker
making is  currently implemented in the power future market in Germany. Last, it is useful for reg-
ulators in their understanding of the market to propose adequate monitoring tools. For example, in
assessing the impact of the concentration of the market on the liquidity.

From an academic perspective, the contribution of the paper is in threefold. First, the paper
assesses the impact of the renewable and the load forecast errors on the liquidity of the market. Be-
yond the negative and significant impact of the forecast errors on the bid-ask spread, it shows that
the market handles the uncertainty of the supply and the demand: it is  more liquid after a forecast
error. Second, a unique dataset is used and it allows to compute the concentration of the market as
well as assessing the impact of it  on the liquidity of the market. While the generation part of elec-
tricity is  highly concentration in Germany (Amanatidis, 2009), I  find that the concentration on the
continuous market is  moderate. Also, while the negative impact is  intuitive, this article quantifies
it and highlights that the supply concentration have a larger impact on the liquidity in comparison
to the demand concentration. Last, to the best of my knowledge, it is the first paper that studies the
bid-ask spread of a power market. The complete order book allows me to reconstitute the best order
streams (best bid, best ask, and market depths) each time a new event occurs in the power market

.  ““balance responsible party” means a market participant or its chosen representative responsible for its imbalances in
the  electricity market” (EU regulation 2019/943 of the European Parliament and of the Council of 5 June 2019 on the internal
market for electricity, Article 2(14))

1. Official market makers are participants that are active on both sides of the market and that should maintain a deter-

mined bid-ask spread in exchange of trading rebates.

All rights reserved. Copyright © 2022 by the IAEE.

‘This content downloaded from
IIIII186.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC TIIIIIIT
All use subject to <https://about> jstor.org/terms

Analysis of the Bid-ask Spreadin Continuous Intraday Trading of the German Power Market  /231

(i.e.,  new/modification/cancellation of an order in the order book). The model could be easily ex-
tended to other continuous markets.

In this article, I first do a dynamic analysis of the bid-ask spread and the market depths over
an average trading session at a granular level (microseconds). The market depth is the volume avail-
able in the order book. It can be divided into the buy depth and the sell depth. They respectively are
the total volume  available on the buy side and on the sell side at one moment of the trading session.
For example, in the setup proposed in figure 1, the sell depth is equal to 40 MW and the buy depth is
equal to 65 MW. Second, I  identify the main drivers of the bid-ask spread: the risk, the adjustments’
need, the activity and the concentration of the market.

The study yields three main findings. First, it  shows the “L-shaped” pattern of the bid-ask
spread during a trading session of a power market. Second, I  find an average bid-ask spread of 3€
per MWh over the trading session of the German power continuous market. Third, I  identify four
components of the spread: the risk,  the adjustments’ need, the activity, and the competition in the
market. Using a  fixed effect model, I  find a positive relation between the risk and the bid-ask spread
as well as a negative relation between the bid-ask spread and the adjustments’ need, the activity, and
the competition in the market.

The paper is organized as follows: the second section is dedicated to the relevant literature,
the third one is an overview of the current spot power market in Germany, the fourth section gives
some statistical insights on the bid-ask spread and the market depth in the German intraday power
market. The fifth part presents the data and the methodology used. Then, the sixth section displays
the empirical results. The last section is the conclusion.

1. RELEVANT LITERATURE

The present paper  straddles two streams of literature: the one related to the electricity mar-

kets and the one on market microstructure.

While the literature on the power markets is  dense, the literature on the continuous ones
is  limited and mainly focuses on two issues:  wind generation integration (how to handle forecast
errors) and market design. The closest literature to this paper is  the one on price formation in the
intraday continuous market. Hagemann (2015), Hagemann et al. (2016), Karanfil and Li (2017) and
Ziel (2017) model the price of this market. Weber (2010) is  the first to address the question of the
liquidity of the German continuous power market. He finds that the low liquidity might be the cause
of a poor market design and/or the absence of a real need for a continuous market. However, those
comments have to be balanced as the paper uses a dataset from 2007 when the yearly volume traded
on the continuous market was 1.4 TWh—almost 26 times less than the volume traded in 2015. Also,
the level of installed wind capacity more than doubled from 2007 to 2015; it increased the need
to adjust the renewable generation’s position close to the delivery time in order to be balanced at
delivery. Chaves-Avila et al. (2013) explain the low liquidity in the continuous power market as the
preference of producers to commit their generation long ahead of time because of ramping-up costs
and generation planning. Hagemann and Weber (2013) develop two models to explain the liquidity
of the German continuous power market. To the best of my knowledge, the work of Hagemann
and Weber (2013) is  the first paper that investigates the bid-ask spread in the German continuous
power market. However, their work neither uses the order book sent by the market participants or a
reconstitution of it  as input data for their models: they estimate the bid-ask spread using the trans-
actions data. Neuhoff et al. (2016) study the impact of an intraday auction before the opening of the
continuous market. They find a negative relation between volatility and the market depths as well

Copyright © 2022 by the TAEE.  All rights reserved.

‘This content downloaded from
IIIII186.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC TIIIIIIT
All use subject to <https://about> jstor.org/terms

232/ The Energy Journal

as a positive relation between the liquidity and the market depths of the 15-minute intraday auction
in Germany.

The microstructure can be defined as the branch of the finance that deals with the traders’
behavior and the market design. The study of the bid-ask spread is part of the microstructure litera-
ture, particularly of the sub-literature on price formation and price discovery.

Demsetz (1968) initiated the literature on the bid-ask spread. He defines market makers®
as immediacy providers in which the bid-ask spread is  a premium paid by a market participant for
immediate execution. The work of Demsetz highlights the negative relation between the volume and
the bid-ask spread. It is also raised in the paper of Copeland and Galai (1983) who model the bid-ask
spread using the volatility and the level of trading as explanatory variables.

In the theoretical part of the literature,  the bid-ask spread reflects three components: the
transaction or the order processing costs* (Roll,  1984), the adverse selection costs®  (Glosten and
Milgrom,  1985), and the inventory costs® (Stoll,  1978). Glosten and Harris (1988) and Kim and
Ogden (1996) model the spread with both the inventory and the order processing costs. Glosten
(1987) models the role of information asymmetries by separating the effect of order processing
from the effect of adverse selection. The models of Stoll (1989) and Huang and Stoll (1997) present
an estimation of the bid-ask spread with all three components. Hasbrouck (2004) proposes a Roll
estimator’ using a Markov chain and a Monte-Carlo simulation. Chen et al.  (2019) extend the Roll
model where only the transaction prices are needed as input for the model.

The empirical literature in microstructure also uses these three components of the spread.
Schultz (2000) applies the Roll estimator to a dataset from the NASDAQ. The adverse selection
paradigm was first  empirically applied by Glosten and Harris (1988) to  the NYSE based on an
indicator variable for trade initiation. Madhavan et al. (1997) develop a model called MRR that de-
composes the spread in two components: the adverse selection and the order processing. This model
has led to a multitude of papers on different markets such as future exchanges (Huang, 2004, Ryu,
2011), stock exchanges (Angelidis, and Benos, 2009), Exchange Trading Funds or ETS (Ivanov,
2016) or the European climate exchange (Mizrach and Otsubo, 2013). Many studies find empirical
evidence of the inventory cost such as Hasbrouck and Sofianos (1993), Manaster and Mann (1996),
or Madhavan and Sofianos (1998). Huang and Stoll (1996) estimate and compare the spreads of the
NASDAQ and the NYSE from the three elements. Huang and Stoll (1997) quantitatively estimate
the impact of the three components. They find that the bid-ask spread can be explained by the order
processing for 61.8%, the average inventory cost for 28.7%, and the average adverse-information
for 9.6%. McInish and Wood (1992) empirically estimate the bid-ask spread of the NYSE with four
components: activity, risk,  information, and competition based on the previous work of Schwartz
(1988). The econometric model of this paper is  inspired by the work of McInish and Wood (1992).
The present paper adapts the definitions to the power market that has specific characteristics.

order with the highest price and the sell order with the lowest

1. A market maker is a market participant who have orders at the best price limits on both side of the order book: the buy
price.
2. The transaction or order processing costs are measured in Roll (1984) as the first-order serial covariance of a price

change.

1. The adve:
2. The inventory costs are incurred by the imbalance between  the volume bought and the volume sold by a market par-

ction costs are due to the asymmetry of information between traders.

ticipant.

1. The Roll estimator is an estimation of the bid-ask spread using the time series of the trades.

All rights reserved. Copyright © 2022 by the IAEE.

‘This content downloaded from
IIIII186.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC TIIIIIIT
All use subject to <https://about> jstor.org/terms

Analysis ofthe Bid-ask Spreadin Continuous Intraday Trading of the German Power Market / 233

1. THE INTRADAY POWER MARKET

In power markets, the financial flow goes along with the physical one: the market partici-

pants do not buy “papers™ but electricity that will then be injected into the grid.

Power trading can be divided into  two categories:  the one occurring bilaterally  (Over-
the-Counter—OTC) and the one taking place on an exchange. An exchange differs from the OTC
because it is an organized marketplace with uniform rules and it proposes standardized contracts
(Geman, 2005). The trades that occur on an exchange are anonymous and transparent. The power
spot market takes place between the long-term market (forwards, futures) and the balancing market
operated by the Transmission System Operators (TSOs). The commodity spot trading differs from
long-term trading because of the immediate delivery of the product (i.e.,  electricity, gas, gold, cot-
ton, currencies, etc.)  or with a minimum lag (due to technical constraints) between the trade and
the delivery (Geman, 2005). On the electricity spot market, the contract unit is the megawatt for a
certain amount of time (15, 30 or 60 minutes). Contract are also called “products”.

Figure 1: Transaction volume of the German continuous market

h
W
T

n

 i
e
m
u
l
o
V

2011

20

Year

205

2017

In Germany, the Energy Industry Act (1998) unbundled the generation and the supply of
electricity from the network segment—transmission and distribution. The German spot power mar-
ket was created in 2000 by the LPX—Leipzig Power Exchange, and is now operated by EPEX
SPOT. It is the most liquid spot market in Europe: traders moved 302 TWh (terawatt-hour) on the
market in 2015 which represented 53% of the country’s electricity consumption. The continuous
intraday market (IDM) accounted for 36.3 TWh the same year and has increased since its creation
as illustrated in figure 1.

The German spot power market is divided into three sub-markets: the day-ahead market
(DAM), the 15-minute intraday auction, and the continuous intraday market (IDM). The DAM is a
uniform price auction that occurs every day at noon. The 24 contracts exchanged on the DAM are
hourly contracts for the next day. The period called “intraday” starts right after the day-ahead auc-
tion and lasts until delivery. The 15 minutes call auction is a uniform price auction that occurs every
day at  15:00 in Germany. The 96 traded contracts are 15-minute products for delivery on the next
day. The continuous market for hourly contracts starts at 15:00 the day before delivery and closes 5

Copyright © 2022 by the TAEE.  All rights reserved.

‘This content downloaded from
IIIII186.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC TIIIIIIT
All use subject to <https://about> jstor.org/terms

234/ The Energy Journal

minutes® before delivery. For example, the product 2 of tomorrow (D+1) (ie. an hour of electricity
between 1:00 and 2:00) is available for trading from 15:00 today until 00:55 tomorrow. The duration
of the trading session for a contract is between 9 and 32 hours.

Figure 2: The German spot power market

15:00
Intraday
auction in

From 15:00 to 5 minutes before delivery
Intraday continuous market (H)

From 15:30 to 5 minutes before delivery

From 16:00 to 5 minutes before delivery
Intraday continuous market (QH)

T
Day before delivery

T
Delivery day

The continuous market runs continuously 24 hours a day,  7 days a week, all  year long.
Thus, a market participant can trade up to 32 hourly contracts at the same time. This market allows
participants to  adjust their position and to  optimize their portfolio close to delivery. Scharff and
Amelin (2016) justify the need for an intraday market in three points:  it reduces the unbalanced
costs, it helps to optimize market participants’ production and consumption schedules, and it pro-
motes flexibility.

Market participants can submit limit price orders for a given contract to the exchange at
any time during the trading session.’ A limit order is composed of a price and a quantity. The price

1. Trading was first possible up to 45 minutes before delivery, then 30 minutes before delivery, and since June 2017 up to

5 minutes before delivery. This paper uses data from 2015 when the gate closure was 30 minutes before delivery.

1. Orders can be sent as

single orders or within a group of orders. Limit orders can have execution and validity restric-
Exccution restrictions include fill-or-kill (FOK—either the order is immediately and entirely exceuted or cancelled
tions.
in its entirety”), immediate-or-cancel (I0C—the order is
either immediately executed or automatically cancelled; the order
can be partially executed and any unexecuted quantity is cancelled”), linked fill-or-kill (LFOK—linked orders ar cither all
immediately and entirely exceuted or all cancelled in their entirety”), and all-or-none (AON—"the order is  exccuted com-
pletely or not at all”). Validity restrictions include “good for session” (“the order is delcted on the trading end date and time
of the contract unless it is matched, deleted, or deactivated beforehand”), “good-till-date” (“the order is deleted on the date
and time specified by the exchange member when placing the order unless itis matched, deleted, or deactivated beforchand”),
or iceberg (“large order s divided into several smaller orders which are entered in the order book sequentially”). Groups of
orders can be of twotypes: block orders or basket orders. Blocks orders “combine several expires with aminimum oftwo con-
tiguous expires on the same delivery day which depend on each other for their execution”. A block order can be predefined or
user-defined. In Germany, there are two predefined blocks: base-load that covers  hours 1  to 24 and peak load that covers hours
91020 during business days. User-defined block orders are designed by market participants. They can only use the  same type
of contract to compose their block. The exceution restriction
AON is applied by default for blocks. Basket orders are a group
of orders which allows users to submit a set of orders all at once (max. 100 orders). One basket can contain quarter-hourly as
well as hourly and half hourly products. There are three possible constraints: linked (“either all orders are fully executed or
none at all”), valid (“all orders must be valid, or all will be rejected”), and none  (*treat all orders in basket as separate orders).
‘The tool that I use does not take into account block orders as they have their own order book, different from the order book
of the hourly products.

All rights reserved. Copyright © 2022 by the IAEE.

‘This content downloaded from
IIIII186.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC TIIIIIIT
All use subject to <https://about> jstor.org/terms

Analysis of the Bid-ask Spreadin Continuous Intraday Trading of the German Power Market / 235

is the minimum (maximum) price at which they are willing to sell (buy) the associated quantity. The
orders are listed by price: increasing order on the sell side and decreasing order on the buy side as
illustrated in table 1.  The IDM is  continuous in its  matching procedure:' orders are matched when
they arrive in the order book if there is a counterpart in the market with whom the price and the vol-
ume requirements match." Orders can either be fully or partially executed if only part of the match
is  possible. An order is  executed at or above (under) the specified price for a seller (buyer):  the
transaction price is  the price of the order that was first posted in the order book. There is no market
price as each transaction that occurs on the IDM has a different price (pay-as-bid principle). If there
is no matching possibility, then the order remains in the order book. Members can also withdraw or
modify their orders during the trading session.

The process presented above represents the local (within a country) order book; however,
countries  in  Europe are  interconnected. Under the  capacity constraint on a border, the  capacity
available will allow the best orders from a source country with a maximum volume of the capacity
constraint to be visible in the order book of a sink country and vice versa. For example, if the inter-
connection capacity available at time t for a specific product p is 20 MWh from Germany to France;
so at that time, a volume of 20 MWh of the best sell orders from the German order book will be
displayed on the French order book of product p. Simultaneously, a volume of 20 MWh of the best
buy orders from the French order book will be visible on the German order book for the concerned
contract. The capacity is  implicitly'? given and not priced in the market. The order book does not
display if the orders are local or cross-border.

Table 2: Descriptive statistics of the continuous market, per contract

Weighted price (€/MWh)
Number of trades
Number of orders
Active members on both side

Min
84.60
14
109
29

Quartile |
25.12
169
599
43

Median
31.53
247
945
51

Mean
31.85
267.5
1072
50.95

Quartile 3
39.52
345
1373
59

Max
12016
907
6724
77

Table 2 displays some descriptive statistics  on the trades of the German continuous mar-
ket from January 1,  2015, to December 31, 2015. The mean daily price is  31.85¢/MWh. The mean
daily number of trades per contract is  267.5 while the mean daily number of orders per contract is
1072: on average, a member sends 4 orders for 1  execution (trade). There is  on average 51 active
members" in the market which represents around a quarter of the members registered on the market.

1. BID-ASK SPREAD AND MARKET DEPTH OVER THE TRADING SESSION

This section first provides the data description of the the bid-ask spread and the market
depths of the German continuous electricity market. Then, I  examine the behavior of these two
variables during an average trading session. The data used for this dynamic analysis is fine-grained
(milliseconds of the trading session).

1. Order
2. Amarket participant is called “initiator” of the trade if he or she submits a new order in the order book and is called

erial processing, in general within milliscconds.

ent to the market are processed one at the time-

“aggressor” when he or she hits the price of an existing order in the order book.

1. The energy is sold along with the interconnection capacity.
2. Amarket participant is considered as active if he sends at least one order during the trading session.

Copyright © 2022

by the TAEE. All rights reserved.

‘This content downloaded from
IIIII186.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC TIIIIIIT
All use subject to <https://about> jstor.org/terms

236/ The Energy Journal

4.1Data

The complete order book contains only the German local orders and does not account for
cross-border or block orders. It covers a period of a year from January 1,  2015 to December 31,
2015. Each line of the dataset displays an order that a market participant sent to the power exchange
during a continuous trading session. It includes a range of variables: the delivery date, the delivery
instrument (specific hour, half hour, or quarter hour), the name of the member who sent the order,
the side of the order (buy or sell), the day and time when the order was sent, as well as the day and
the time when the order was executed/cancelled/deactivated/expired/modified, the price,  and the
quantity asked/offered by the market participant. This dataset serves as input for the reconstitution
tool that was first developed by the Product and Market Development team of EPEX SPOT by using
the software R. The tool computes the best order stream (best bid and ask prices) and the market
depths each time there is  a change in the order book during the trading session. The R code sorts
market orders and creates a row each time there is  a change in the order book that affects the bid-
ask spread and/or the market depths. Each line of the output displays the particular contract and the
associated delivery date, the date and time of trading, the best buy (highest) and sell (lowest) prices
at that time, the respective quantities at the best prices—it can be the sum of two orders or more. The
last information the output shows is  the buy and the sell depths. In other terms, it displays the first
line of the order book and the market depths for both the buy and sell sides—information that can
be seen by the participants at the time they trade. I  then compute the bid-ask spread at each moment
of the trading session as the difference between the best ask and the best bid:

BAS,, = bestask,, — bestbid,,

)

where #'  is  a vector of three dimensions composed of the delivery date, the trading date,  and the
trading time; 7 is the contract concerned and 7 € {1;24}.

4.2 Descriptive statistics

Table 3 presents  the descriptive statistics  for the bid-ask spread and the market depths
aggregated at the contract level (per delivery date and delivery hour) for the year 2015. The mean
bid-ask spread is  3.52€/MWh which is  slightly more than the mean bid-ask spread of 2.97€/MWh
find by Hagemann and Weber (2013). The mean bid-ask spread is  about 350 times the tick size
(0.01€/MWh). It is  much bigger than the spread in the securities market which is  only a few times
the tick size; nonetheless it is smaller than the spread in the French intraday power market where the
average bid-ask spread is about 1,100 times the tick size in 2015 for local order book."* The values
of the bid-ask spread is  overestimated due to  the absence of cross-border orders in the dataset. If
cross-border data would be added, the spread would not be impacted or would be lower: an order
from a neighboring country can only impact the bid-ask spread by either proposing a sell price lower
than the best ask or a buy price above the best bid.

For comparison, Ryu (2011) estimates the bid-ask spread at 4-5% of the price on the
KOSPI 2000 (index performance of the Korea Stock Exchange) for a period of about 2 years from
2002 to 2004. A survey on the equity market by Angel, Harris and Spatt (2013) find that the effective
spread on the NASDAQ (resp. NYSE) between 2010 and 2013 is  about 2.5 cents (resp. 1.5 cents).

1. The value of the French local bid-ask spread is calculated by the author, using the EPEX SPOT data.

All rights reserved. Copyright © 2022 by the IAEE.

‘This content downloaded from
IIIII186.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC TIIIIIIT
All use subject to <https://about> jstor.org/terms

Analysis ofthe Bid-ask Spreadin Continuous Intraday Trading of the German Power Market / 237

The limited liquidity of the power market is  due to the physical aspect of electricity, the fact that it
is not storable and that the traders are selected—they have to be balance responsible.

Table 3: Descriptive statistics of the bid-ask spread and the market depths, per contract

Bid-ask spread €MWh)
Buy depth (MWh)
Sell depth (MWh)

Min
096
74.91
111.9

Quartile 1
251
557.58
5409

Median
314
772.63
758.5

Mean
3.52
854.96
8286

Quartile 3
3.99
1156.92
11294

Max
31.09
4639.20
2049.0

The average bid-ask spread is higher during the weekends (+ 13%) because of the decrease
of the demand as well as the decrease of the number of participants. The distribution of the bid-ask
spread is displayed in the appendices (figure 7). I  observe peaks of frequency of the bid-ask spread
every 5 cents per MWh. This observation highlights the use of price steps of 5 cents by the mem-
bers."

In order to get some insights on the case where the bid-ask spread is high (top 25%), I  use a
subset of the data where the spread is above 4€/MWh. In this subset, lower depths exist (respectively
~17% and ~21% in comparison to the mean buy and sell depths) which is consistent with the nega-
tive correlation between the bid-ask spread and the depths explained later in this section. Off-peak
products (before 8:00 or after 20:00) and weekends are over-represented in the subset. This result
is reasonable because during off-peak hours, the liquidity and the number of active participants are
lower, which is  also valid for weekends. From the observed subset, I  also find a higher sell price
(+8,5% on average) and a lower buy price (-2% on average).

The buy and sell depths are respectively 855 MWh and 829 MWh on average per contract
and 25% of the time they are respectively above 1157 MWh and 1129 MWh. The same argument on
the lack of the cross-border data applies to the market depths: they are underestimated; the market
depths could only be above the result as a cross-border order can only increase the volume in the
order book. The mean depths are higher for the base-load contracts (from 8:00 to 20:00) in compar-
ison to the off-peak contracts. The distributions of the depths'® aggregated at the contract level are
bi-modal. On the one hand, when I  study the subset that only includes the high mode (depth above
900 MWh), the spread is on average low (2.58€/MWh), the forecasted wind generation high (+12%
in comparison to the overall mean) and there is an overepresentation of business days and peak con-
tracts—the most liquid ones. On the other hand, in the subset that includes only the low mode (depth
below 900 MWh), the reverse is  true:  I  find high bid-ask spread, low wind generation’s forecast as
well as an overepresentation of weekends and off-peak contracts.

Using observations at the milliseconds level, the correlations between the bid-ask spread
and the market depths are weak: ~0.16 with the buy depth and —~0.11 with the sell depth. However,
when aggregating the values at the minute level, the correlation increases particularly for the morn-
ing hours where the mean correlation for the contracts 1  to  11 is  —0.66. I  observe that at a higher
frequency scale, the correlation breaks down: each order added or removed from the order book
does not have an impact on the bid-ask spread; a new order is not always at the limit price. However,
when I  aggregate the values, I  observe a negative correlation: when the volume in the order book
increases, the bid-ask spread tends to decrease. These correlations are negative which is reasonable
and consistent with the literature.  This negative relation is  also observable by looking at the evo-

1. In the period studicd, the tick size of the continuous market was 0.01€/MWh. It  has been 0.10€/MWh since June

2.

3. The distribution of the buy and the sell depths are displayed in figures 8 and 9 of the appendices.

Copyright © 2022 by the TAEE.  All rights reserved.

‘This content downloaded from
IIIII186.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC TIIIIIIT
All use subject to <https://about> jstor.org/terms

238/ The Energy Journal

lution of the depths and the bid-ask spread over an average trading session.'” When aggregating at
the hourly level, the correlation between the bid-ask spread and the depths are high: the correlation
between the bid-ask spread and the buy (resp. sell) depth is ~0.83 (resp. ~0.86).

4.3 Dynamic analysis

This subsection describes the evolution of the bid-ask spread and the market depths over

an average trading session.

Figure 3 represents the evolution of the bid-ask spread over an average trading session
aggregated at the minute level for the product 8 (60 minutes of power from 7:00 to 8:00)."* The bid-
ask spread decreases over the trading session. This result is  valid for all the 24 contracts studied.
This decrease is due to the strong uncertainty away from the delivery time. During the last hours in
which a contract can be traded, I observe the lowest values of the bid-ask spread. As the contract gets
closer to the delivery, the uncertainty linked to the production decreases and so does the spread. The
volume traded on the continuous market increases over time and 80% of the volume is traded during
the last three hours of the trading session. The continuous market is mainly used to adjust positions,
previously taken, in continuous manner and close to the delivery of the contract. The adjustments’
need are due to the arrival of new information such as a new weather forecast, a new load forecast,
or an unplanned outage. The longer the trading session is (from 8,5 hours for the contracts 1  to 31,5
hours for the contract 24), the smoother is  the curve of the bid-ask spread over time. At the end of
the trading session, the bid-ask spread increases a bit due to the decrease of the volume of the order
book.

To sum up, the bid-ask spread has a “L-shape” pattern over the trading session and is  on

average of 3.5¢/MWh.

Figure 3: The bid-ask spread over an average trading session for the product 8

201

h
W
M
R
U
E

n
i

d
a
e
r
p
s

d
e
t
o
u
Q

Re=060

Trading time (minutes)

1. Figure 3 and figure 4 illustrate the behavior
2. Figure 10 in the appendices illustrates the  evolution of the bid-ask spread over an average trading

of the bid-ask spread and the sell depth over an average trading session.
session  for the
For example, during
products 5, 9,  13 and 17. These
ent as the hours concemed have different profils
is no solar generation. In contrast, product 13 represents the hour where
contract 5, the demand for power is low and there
solar production is the highest and the demand is high. The product 9 represents a peak hour where the demand is the highest.
However, the “L-shaped” pattern is obscrvable across the contracts.

contracts are difft

All rights reserved. Copyright © 2022 by the IAEE.

‘This content downloaded from
IIIII186.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC TIIIIIIT
All use subject to <https://about> jstor.org/terms

Analysis ofthe Bid-ask Spreadin Continuous Intraday Trading of the German Power Market / 239

Figure 4: The sell depth over an average trading session for the product 8

4000

H

w
a
n
i
h
t
p
e
d
l
l
o
S

g

1000

o

%0

Trading time (minutes)

R2-070

70

Figure 4 shows the evolution of the sell depth over an average trading session for the prod-
uct 8. The buy and the sell depths increase over the trading session. They have a reverse shape in
comparison to the bid-ask spread. The correlation between the buy and the sell depths, using the
data set at its lowest granularity (milliseconds), is 0.95. As the time gets closer to the delivery, more
quantities are added to the order book. The highest liquidity during the trading session occurs at
the end of it.  The reason behind this result is the growing need for trading because of the arrival of
new information as well as the increasing pressure to be balanced. An important liquidity can be
translated by a more important matching opportunities, which is  consistent with the fact that 80%
of the market volume is  traded during the last three hours before delivery. At the opening of the
trading session, market depths are around 500 MW (125 MWh) no matter which product is  traded.
For off-peak products (before 8:00 or after 20:00), the average buy and sell depths are respectively
786 MWh and 769 MWh while for peak products (between 8:00 and 20:00), the average depths are
respectively 936 MWh and 899 MWh. The market depths for off-peak products tend to increase to a
lower level in comparison with the depths of peak products because the economic activity is  lower
at those hours. At the end of most  trading sessions, I observe a decrease of the market depths particu-
larly 30 minutes before the gate closure due to the decrease in market opportunities: the cross-border
trading closes an hour before delivery. This decrease could also be explained by the activity of the
traditional producers who want to fix  their production few hours before delivery for operational
purposes but also due to the large inflexibility of some power plants. It can also be explained by the
absence of cross-border trading during the hour before delivery that can be translated into a decrease
of market opportunities for a market participant.

First,  I  find a mean (local) bid-ask spread of 3.5¢/MWh in the German intraday power
market. The spread is  large at the beginning of the session and decreases as the end of the session
approaches. Second, I  find the average (local) buy and sell market depths at respectively 855 MWh
and 829 MWh. Both depths increase along the trading session.

1. Figure 11 in the appendices illustrates the  scll depth of the contracts 2,9,  13 and 17.

Copyright © 2022 by the TAEE.  All rights reserved.

‘This content downloaded from
IIIII186.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC TIIIIIIT
All use subject to <https://about> jstor.org/terms

240/ The Energy Journal

1. DATA Al  METHODOLOGY

The present section is divided in two parts. The first subsection introduces the four hypoth-
esis to be tested as well as the datasets that are used to check them. The second section is dedicated
to the methodology/econometric specification.

5.1 Hypothesis and data

This study uses various datasets: the firm-level energy bids on the continuous market or or-
der book (source: EPEX SPOT), the day-ahead auction’s aggregated curves (source: EPEX SPOT),
the solar and the wind forecasts (source: Eurowind), the actual wind and solar generation (source:
EEX transparency platform) as well as the forecast and the actual load (source: ENTSO-E transpar-
ency platform). From the order book, I  construct®” a novel dataset with the bid-ask spread and the
market depths at each moment of each trading session of the year 2015. The order book data that I
use is highly confidential and includes market participants’ identifiers which permits me to compute
the concentration ratio (HHI index). Due to the frequency of the data (from the milliseconds for the
bid-ask spread to once an hour for the actual wind generation), I  choose to aggregate all the variables
at the daily level for each contract. In the rest of the paper, I  will refer to  as the delivery date and
i the contract.

The aim of the econometric specification is  to find the main drivers of the bid-ask spread
of the German continuous power market. The bid-ask spread was chosen as a proxy for liquidity
as it represents an implicit transaction cost for the market participants. Using the outcome from the
reconstitution tool, I  compute the mean bid-ask per day and per contract (BAS,).

In order to find the main drivers of the bid-ask spread, I use the methodology from Mclnish
and Wood (1992) who use the four following explanatory components: the risk, the information, the
activity and the competition on the market.

Hypothesis 1:  There is a positive relationship between the bid-ask spread and the risk or
the volatility of the market. When the volatility is  high, there is  more risk and uncertainty on the
market; in this situation, the buyers are willing to buy at a lower price and the sellers are willing to
sell at a higher price in order to hedge the risk linked to the volatility; they wants a risk premium.
Therefore, the bid-ask spread should increase. The volatility is measured in this paper by the elastic-
ity of the supply curve of the day-ahead market, the elasticity of the demand curve of the day-ahead
market and the weighted price standard deviation of the transaction.

The slopes of the demand and the supply curves around the equilibrium point can be in-
terpreted as the elasticities. When the elasticity increases (slope tends to infinity), a small change in
quantity has an important impact on the price; thus, it increases the volatility of the market and the
bid-ask spread should increase. When the inelasticity on one side of the market increases (slope goes
to zero), the bid-ask spread should decrease.

The elasticities, ES;; (supply elasticity) and ED;; (demand elasticity), are calculated using
the aggregate curves of the German day-ahead market. Those variables represent an approximation
of the elasticities  around the equilibrium. The supply elasticity  (respectively demand elasticity)
is  the slope of the linear interpolation of the supply (respectively demand) curve between the two
points. Those points correspond to the equilibrium volume (Q*) of the auction plus or minus 500
MWh. Figure 5 illustrates the concept of the calculation. The slopes are computed as follow:

1. The reconstitution

tool is explained in section 4.1.

All rights reserved. Copyright © 2022 by the IAEE.

‘This content downloaded from
IIIII186.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC TIIIIIIT
All use subject to <https://about> jstor.org/terms

Analysis of the Bid-ask Spreadin Continuous Intraday Trading of the German Power Market / 241

Figure 5: An example of aggregated curves of the DAM (25/10/2015—product 9)

onwn

P

00 €MWH   Volume: 28,102 MWh

s000

500

000

3500

3000

500 MWh

+500 MWh

ES, =  ;[

SOOHQX L300,

P'(Q"-500)—p*(Q" +500)

ED, -]

[0 —500]-[Q" +500]

(0" ~500)

- p” (0" +500)

@

3

where p*  is  the supply price, and p  is  the demand price at the points (0'-500) and (Q"+500). The
elasticity represents the average price variation around the equilibrium; it measure the impact of a
quantity variation of I  MWh on the price.

The second proxy variable for the volatility is  the weighted (by the volume) price stan-
dard deviation. It measures the variability of the price around its average. When the weighted price
standard deviation increases, the volatility increases and the bid-ask spread should get wider as the
price’s expectations of the sellers and buyers fluctuate more. It is computed as followed:

where

“)

)

Copyright © 2022 by the TAEE.  All rights reserved.

‘This content downloaded from
IIIII186.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC TIIIIIIT
All use subject to <https://about> jstor.org/terms

242/ The Energy Journal

N is  the number of observations,  M  is  the number of nonzero weights, v;  is  the volume

(weight), p;  is the price of the transaction, and p* is the weighted mean of the price.

Hypothesis 2:  There is a negative relationship between the bid-ask spread and the need for
adjustments. When the demand or the supply diverge from their initial forecasts, the positions of the
market participants may change, and they need to adjust them; therefore, it increases the volume in
the market. The renewable production (wind and solar generation) and the load forecast errors are
used to measure the need for adjustments from both the supply and the demand side.

Kiesel and Paraschiv (2017) find a significant effect of the wind and the solar forecast er-
rors on the prices of the continuous market. When the supply changes consecutive to a change in the
forecast of the renewable, the bid-ask spread is  expected to decrease. When an intermittent power
supplier faces a positive shock in his production, he will produce more than he planned and so he
will need to sell the extra production. The reverse is also true: when an intermittent supplier faces a
negative shock of her production; if she already committed her production, she will need to buy the
difference on the market.

In order to assess the impact of the wind and the solar forecast errors, I  subtract the wind
(solar) forecast (WF, and SF,) to the wind (solar) generation (WG, and SG,). I  use the wind (solar)
generation—at delivery, as a proxy for the forecast at the gate closure—30 minutes before the deliv-
ery. The intuition behind it is  that the forecast 30 minutes before delivery is  the same as the actual
value thanks to its  closeness in  time. The chosen forecast is  issued at  14:00 (“PREV4”) the day
before delivery: it  is  after the DAM and before the beginning of the intraday market. The relative
forecast errors are expressed in percentage of variation and are defined as:

AV

%100

_WG, -WF,

2
s _SG,=SFy 410
it
it

(6)

@

Inspired by Ziel (2017), I  split the above equations depending on the algebraic sign of the

shock. A positive shock is defined as:

WE = max(A] 0}

SFE = max{A;,0}

and a negative shock is defined as:

WF =max(-Ay] 0}

SiE  = max{-Aj, 0}

®)

©

(10)

an

When the demand (load) changes, I  expect the bid-ask spread to decrease: retailers sell
their extra quantity on the market if the load decreases and they buy quantities from the market if
the load increases in order to meet their commitment. The load forecast error is computed with the
same methodology as the wind and the solar forecast errors:

(12)

All rights reserved. Copyright © 2022 by the IAEE.

‘This content downloaded from
IIIII186.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC TIIIIIIT
All use subject to <https://about> jstor.org/terms

Analysis ofthe Bid-ask Spreadin Continuous Intraday Trading of the German Power Market / 243

where LG, is the actual load and LF;; the forecasted one at 14:00 the day before delivery. I then split
the forecast error depending of the algebraic sign of the shock:

LF = max{AL,0}

L = max{-AL, 0}

(13)

(14)

Hypothesis 3:  There is a negative relationship between the bid-ask spread and the activity
on the market. 1  expect that when the activity on the market increases, the bid-ask spread should
be narrowed. Indeed, when the load (demand) is high, the volume available on the market should
increase (higher liquidity) and therefore the bid-ask spread should be narrowed.

T use the forecasted load as a proxy for the activity on the market.
Hypothesis 4:  There is a negative relationship between the bid-ask spread and the com-
petition in the market. When the concentration of the market decreases, the competition increases
and there is  less asymmetry of information due to the smaller market shares; the spread should then
decrease.

In  order to  measure the  concentration of the  market,  the  Herfindahl-Hirschman Index
(HHI) is computed on both sides of the market. This index captures the concentration and measures
the market competitiveness.

HHI=Y5?

where

Si

(1s)

(16)

where s; is the market share of the firm 7 (the volume traded by the firm over the total volume of the
market) and m is  the number of firms.

Table 4 gives the descriptive statistics of the variables described above for the year 2015.
The variables are at the contract level (a specific delivery date and delivery hour). The average bid-
ask spread per contract is  3.5€/MWh which is about 10% of the weighted average price (WAP) for
the same period. The mean weighted standard deviation of the price is 4.15€/MWh or 11.5% of the
mean WAP. The mean slopes of the buy and sell curves of the DAM are respectively equal to 0.026
and 0.010. The average hourly load is  247 GWh. The average concentration ratio is  1087 for the
demand and 1034 for the supply. While the European Commission (Amanatidis, 2009) finds a HHI
between 1800 and 5000 (highly concentrated market) for the power generation in Germany, I  find
that the German continuous market is less concentrated than the production. The mean HHIs of the
continuous market correspond to a moderate concentration.

5.2 Methodology

This subsection describes the econometric specification used to explain the average bid-ask

spread per contract.

Due to the configuration of the dataset, the panel data methods are the most appropriated
because the dataset combines information on individuals® behaviors (contracts) and over time (de-
livery date). The contracts are independent as each of them are traded individually by the market

Copyright © 2022 by the TAEE.  All rights reserved.

‘This content downloaded from
IIIII186.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC TIIIIIIT
All use subject to <https://about> jstor.org/terms

244/ The Energy Journal

s
i
s
o
p
m
y

S
O
U
M
O
N
S

x
o

€
a
m
a
n
g

w
n
p
a
y

A

T

a
m
m
m
n
g

w
y

(
[
9
4
9
]

J
2
R
.
1
)
U
0
D
)

S
A
[
Q
R
L
I
L
A

)
 J

O

S
I
N
S
H
E
)
S

I
A
N
A
L
D
S
I
(
 :
F

A
[
q
L
L

a
1
q
u
i
,

9
5
'
0
¢

S
E
T
0
T
6
1

#

8
7
9
6

6
r
t
h
L

£
9
8
°
1
6
€

0
0
1
1
1

L
v
L
'
E

1
5
9
6

0
z
8
'
€
l

0
r
9
p
1

8
1

8
€
8
'
6

8
0
9
T
1

S
I
S
E

0
5
0
°
0
1

8
5
8
8

6
0
9

L
L
O
'
9
L

€
9
8
7

8
L
E
Y

(
3

6
E
L
'
T

0
L
8
°
T

9
0
1
0

8
L
6
'
T

T

£
6
0
°
1
€

£
V
L
'
S
S
E

7
6
6
0

L
E
T
O

£
1
0
°
8
6

T
0
r
'
6
L
E

P
I
S
'
S
L

€
1
L
'
6
1

£
0
1
1
C

0
0
0
°
0
0
6
+
€
6

0
0
0
L
S
6
S
T
E

L
S
T
'
L
Y
L
S

6
9
L
°
6
5
1
S

$
6
6
'
€

Y
I
L
Y

9
1
0
'
0

1
1
0
0

9
€
6
T
1

0
0
0
0

y
T
s
'
6
1

0
L
T
L

S
O
V

0
6
1

1
7
6
°
6
L
T
1

0
0
0
'
8
¥
S
S
S
T

L
O
S
0
6
1
1

L
E
T
'
E

o
r
E
'
e

9
0
0
0

L
0
0
°
0

0
0
0
0

0
0
0
0

6
8
t

0
0
0
°
0

L
L
T
O

0
0
0
0

9
0
9
9
6

#

2
2
0
6

0
0
0
°
1
¥
8
9
)
T

8
1
S
'
€

P
S
I
'
Y

9
2
0
0

0
1
0
0

S
E
L
9

S
E
0
°
S
T

T
%
€
9
'
s

0
9
8
1

S
9
€
°
1

8
8
4
'
1
9
7
€

Y
E
P
'
L
S
0
1

9
T
6
T
E
G
P
T

£
5
T
H
E
0
1

0
1
§
'
T

w
E
T

7
0
0
°
0

0
0
0

0
0
0
0

0
0
0
0

0
0
0
°
0

0
0
0
0

0
0
0
0

0
0
0
0

L
O
L
'
E
S
L

£
6
8
'
6
0
L

0
0
0
T
6
T
I
I
T

$
9
6
°
0

1
L
5
°
0

1
0
0
°
0

1
0
0
0

0
0
0
0

0
0
0
0

0
0
0
0

0
0
0
0

0
0
0
0

0
0
0
0

0
0
0
°
T
O
S
S
E
L

8
0
0
1
0

L
£
2
9
'
9
6
€

(
U
M
W
N
A
I
N
E
)

A
o
p

(
U
M
I
N
/
I
N
E
)

p
e
a
s
d
s

s
e
-

p
r
e
l

P
i
s

2
o
u
d

A
p
u
s
e
(
o

p
a
r
y
B
i
o
m

p
u
r
w
a
q

A
o
n
s
e
y
 K
i
d
d
n
g

(
%
)

(
%
)

(
%
)

(
%
)

1
1
0

1
5
8
9
0
1
0
}

F
e
[
0
S

4
1
2
1
5
2
3
0
1
0
}

J
E
[
0
S

2
A
N
E
T
O
N

A
N
I
S
O
G

"
1
1
2

"
1
1
2

1
5
L
2
1
0
J

1
5
L
9
1
0
J

P
U
I
A

P
U
I
A

1
1
9

1
1
2

}
S
E
d
2
1
0
J

1
S
E
9
1
0
}

E
O
]

P
E
O
]

A
A
B
I
S
O
G

A
A
B
I
S
O
G

d
A
N
I
S
O
G

I
A
B
I
S
O
Y

(
U
M
W
)
 1
5
2
9
0
1
0
)

p
r
O
'
]

p
u
e
w
a
p
—
T
H
H

A
d
d
n
s
—
T
H
H

All rights reserved. Copyright © 20,

by the IAEE.

This content downloaded from

IR 6.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC I

All use subject to <https://about> jstor.org/terms

Analysis of the Bid-ask Spreadin Continuous Intraday Trading of the German Power Market / 245

participants. They also have their own specificities. Figure 6 shows the heterogeneity across con-
tracts.

Figure 6: The heterogeneity across contracts

1171
1

1

N
&
i,  !
3=

\\\

7T
e

T

T
Yy

R

T
4 05155 050058 05558
10
6
2 3

8

7

9

5

4

N
\I
h  T
\f D  T
T  AT  L

/1

4  9055 05 5050054  05  g  S s

1  2  13  W  15

16  W  18  1  2  21  2  2  %

product

1  compare the fixed effects model with the pooled OLS model using the F-test, and con-
clude that the fixed effects model is  a better choice. I  then compare the fixed effects model with a
random one using the Hausman test. The fixed effects model is more appropriated.

Using the Levin-Li-Chu test for panel data, I  find that none of the variables has a unit root;
however, when I  perform a stationarity test (Kwiatkowski-Phillips-Schmidt-Shin or KPSS test) for
each group, I  find that most of the variables are not stationary. In this sense, a first difference model
is used to stationarize each variable. An additional KPSS test on each of the first difference variable
confirms the stationarity of them.

The Breusch-Pagan test detects heteroskedasticity in the model. It  can cause bias in the
results of the standard deviations in the variables’ estimations that use an OLS estimator; I  then pro-
duce HAC (Heteroskedasticity and Autocorrelation Consistent) standard errors for the OLS models.
The Breusch-Godfrey/Wooldridge test identifies serial correlation in the panel model. For this rea-
son, a feasible generalized least square (FGLS) estimator is used as it “allows the error co-variance
structure inside every group of observations to be fully unrestricted and is  therefore robust against
any type of intra-group heteroskedasticity and serial correlation” (Croissant and Millo, 2008).

1  explain the daily  average bid-ask  spread per contract as  a  function  of the volatility
(weighted price standard deviation and elasticities), the need for adjustments (relative wind, solar
and load forecast errors), the activity (load) and the competition (HHI) on the market and estimate
the equation below:

ABAS, =  a,

+fAc, + BAES, + BAED,
+PAWE + BASTE + FAWE + fASE
+BALE + fALE
+BAL,
+, AHHI + 3, AHHI
+1,
winter

+,

+1,

an

Copyright © 2022 by the TAEE.  All rights reserved.

‘This content downloaded from
IIIII186.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC TIIIIIIT
All use subject to <https://about> jstor.org/terms

246 / The Energy Journal

Table S: Definition of the notations

Definition
Notation
Weighted price standard deviation of the trades (EUR/MWh)
o
Elasticity of the supply
ES,
Elasticity of the demand
ED,
wrE
Positive wind forecast error (% or MWh)
S  Positive solar forecast error (% or MWh)
wrE
Negative wind forecast error (% or MWh)
S  Negative solar forecast error (% or MWh)
LF
Positive load forecast error (% or MWh)
P  Negative load forecast error (% or MWh)
Forecasted load (MWh)
L,
Herfindahl index for the demand side
HHI?
Herfindahl index for the supply side
HHI;
Dummy variable for summer
Lipner
Dummy variable for winter
1

A summer and a winter binary variables are included in order to capture the seasonal ef-
fects. The mid-season (spring and fall) binary variable is not included in order to avoid collinearity
issues.

One may be concerned about the endogeneity problem that may arise with the weighted
standard deviation variable, particularly due to its  aggregation at the daily level. Instrumental vari-
ables are  commonly used to  address this  issue; however, I  cannot find  any robust instrumental
variable for the volatility. I  compute the correlation and the covariance between the weighted price
standard deviation and the error term of the regression. Both are null. On top of that, I  perform the
Granger causality test using data at the milliseconds level and find that “the volatility causes the bid-
ask spread”. The reverse does not hold. For the reason mentioned above, I  discard the endogeneity
hypothesis in the model.

1. RESULTS

This section describes and discusses the results of the panel data model. The model is  first
run on the whole dataset. Then, I  split the data in peak (between 8:00 and 20:00) and off-peak (be-
fore 8:00 or after 20:00) contracts. The results are displayed in table 5.

Volatility—The weighted price standard deviation has a positive impact on the bid-ask
spread, particularly during off-peak hours. When the volatility increases by 1€/MWh, the bid-ask
spread tends to increase by 3 cents. An increase of the volatility by 1€/MWh during the trading ses-
sion of an off-peak contract, increases the bid-ask spread by 11.5 cents per MWh; while, the impact
is  only of 2 cents per MWh for peak contracts. The volatility has a stronger impact on the bid-ask
spread during off-peak contracts.

An increase of the elasticities of the demand and the supply also has a positive impact on
the bid-ask spread. As the aggregated curves get more elastic, a small change in the quantity leads
to an important change of the price. The higher the elasticity (slope tends to infinity) is, higher is the
volatility and so the spread. The slope of the supply curve has a stronger effect on the bid-ask spread
than the slope of the demand curve. Overall, when the slope of the supply curve increases by 0.1, the
bid-ask spread increases by 97 cents per MWh while an increase of the slope of the demand curve by
0.1 increases the spread by only 7 cents per MWh. This difference can be explained by the inelastic-

All rights reserved. Copyright © 2022 by the IAEE.

‘This content downloaded from
IIIII186.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC TIIIIIIT
All use subject to <https://about> jstor.org/terms

Analysis of the Bid-ask Spreadin Continuous Intraday Trading of the German Power Market / 247

ity of the demand. The elasticities do not have a  significant impact on peak contracts. Interestingly,
the demand elasticity has a negative impact on the bid-ask spread during off-peak hours; thus, when
the elasticity increases by 0.1, the bid-ask spread decreases by 5 cents. The supply elasticity does
not have a significant impact on the bid-ask spread during off-peak hours.

Need for adjustments—The variation of the fundamentals (load, wind and solar) have a sig-
nificant impact on the bid-ask spread. The uncertainty linked to the forecast errors brings additional
volatility to the market but at the same time, a forecast error creates a need to trade and therefore
an increase of the volume/market depths. This second explanation seems to gain over the first one.
Looking at the results, most of the load, wind or solar forecast errors (positive or negative) have a
negative impact on the bid-ask spread.

A negative load forecast error has a positive impact on the bid-ask spread while a positive
load forecast error has a negative impact on the bid-ask spread. The positive impact may be due
to the behaviors of the suppliers who remove their orders from the order book they need to buy
less from the market and so they increase the bid-ask spread. However, this positive effect is not
observed when the analysis is splitted between peak and off-peak contracts: a negative load forecast
error does not have a significant impact during the peak hours and has a negative impact during the
off-peak hours. When there is a negative load forecast error of 1% for an off-peak hour, the bid-ask
spread of the contract increases by 1  cent per MWh.

When the wind positive (resp. negative) forecast error increases by 1%, the bid-ask spread
tends to decreases by 0.5 cent/MWh (resp. 0.2 cent/MWh). A 1% negative solar forecast error have
an impact of —0.2 cent per MWh on the bid-ask spread. A positive solar forecast error has a negative
but negligeable impact on the bid-ask spread. The difference between a positive wind forecast error
and a positive solar forecast error can be explained by the difference of behavior of the TSOs who
market the solar production while the aggregators market the wind production. The aggregators
may adjust their position on the market after a positive forecast error while the TSOs may net their
volume; for example, by using it to buy their grid losses. The difference between the positive and
the negative wind forecast error may be due to the activity of the agreggators: they are liquidity
providers or trade’s originators in the case of a positive forecast error (ie. they send an order at a
limit  price  to the order book) while they are more trade’s agressors or liquidity demanders (they will
hit an order already in the order book) in the case of a negative forecast error in order to buy some
volume. While a wind forecast error is not significant during peak contracts, they are significant for
off-peak contracts which contain most of the night hours. Ziel (2017) find a stronger impact of the
forecast errors on prices during the night.

Activity—When the load increases by 1  GWh, the bid-ask spread decreases by 1  cent per
MWh. When the load is high, during business days for example, there is an increase of the trading’s
need and so more volume/orders are sent to the market. This result holds independently of the type
of contract (peak versus off-peak).

Competition—When the concentration on the sell side increases by 100, the bid-ask spread
increases by about 3 cents/MWh while it only increases by 1  cent/MWh when the concentration on
the buy side increases by 100. This result is  intuitive as an increase of the concentration goes along
with a decrease of the number of market participants as well as an increase of the market power of
some firms. The bigger influence of the concentration on the sell side may be due to the inelasticity
of the demand for power.

Copyright © 2022 by the TAEE.  All rights reserved.

‘This content downloaded from
IIIII186.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC TIIIIIIT
All use subject to <https://about> jstor.org/terms

248 / The Energy Journal

(
l
z
l
<
p
a

s

-

-

o

o

o

-

-

s
w
a
d
-

g
o

J
o
u
q

P
i
s

p
o
o
u
d
s

y
s
0
-

p
i
g

2
j
q
u
i
a
o
n
1
u
a
p
i
a
d
a
d

d
p
w
i
n
s
g

(
z
l
<
)
d

J
e
a
d

J
o
u
r

P
i
g

a
p
u
n
s
g

(
z
l
<
)
a

4

J
o
1
g

P
i
g

A
p
u
n
s
s

“
1
0
)
e
w
n
s
?

S
O
 A

[
P
u
e
d
1
)
 S
u
r
s
n

s
)
[
N
s
A
Y

:
9

A
[
q
E
L

8
7
1
0
0
0

6
1
2
0
0
0

S
0
1
1
0
°
0
-

8
€
0
0
0
°
0
-

#

5
0
0
0

#

7
0
0
0

0
S
1
6
£
C

£
5
0
1
0
0

0
5
1
1
0
°
0

9
6
5
1
1
°
0

1
8
5
1
5
0
~

0
L
0
1
8
T
-

S
L
I
T
O
'
0
-

6
V
8
0
°
0
-

-

o

1
6
8
0
0
0

8
6
4
8
5
0

0
6
9
1

0
L
L
0
0
°
0

£
6
5
1
0
°
0

0
0
0
0
0
0

L
L
1
0
0
0

1
5
1
0
0
0

$
€
5
0
0
°
0

£
6
1
2
0
'
0

L
L
6
O
Y
'
0

0
8
0
L
1
°
T

L
E
S
T
0
'
0
-

T
€
1
1
0
°
0
-

0
0
0
0
0
°
0

T
6
0
0
0
°
0
-

9
6
1
0
0
°
0
-

#

7
5
0
0
°
0

e

e

e

e

e

I

e

e

e

0
0
0
0
0
0

2
0
0
0
0
0

#

0
0
0
0
°
0

£
5
E
r
0

0
L
T
8
T
T

1
0
0
0
0
0
~

1
0
0
0
0
0

9
2
0
0
0
0

8
2
6
0
6
0
~

0
€
L
5
9
°
T
-

e

o

e

0
0
0
0
0
0

£
0
0
0
0
°
0

9
0
0
0
0
0

£
0
L
E
S
°
0

0
0
Z
8
5
'
1

1
0
0
0
0
°
0
-

8
0
0
0
0
°
0

0
£
0
0
0
°
0

$
P
L
T
T
O

8
E
8
8
L
°
0

e

e

e

£
7
£
0
0
°
0

w
1
0

8
5
L
T
8
°
0

6
5
£
0
0
°
0

6
£
£
0
0
°
0

0
0
0
0
0
°
0

S
7
0
0
0
°
0

6
2
0
0
0
°
0

£
5
0
0
0
°
0

0
0
0
0
0
0

1
0
0
0
0
0

1
0
0
0
0
0

0
S
+
2
T
0

T
8
5
9
9
°
0

0
8
1
€
0
0

1
6
L
9
9
°
0

O
I
L
Y
L
'
G

L
8
€
1
0
°
0
-

L
I
E
T
0
'
0

0
0
0
0
0
0

9
1
2
0
0
°
0
-

S
1
5
0
0
°
0

1
0
0
0
0
°
0
-

6
0
0
0
0
°
0

$
£
0
0
0
°
0

0
r
S
1
0
°
0
-

9
T
8
L
0
°
0

(
U
A
W
A
I
N
G
)

'
A
%
p

(
%
)

(
%
)

(
%
)

2
7
3

p
r
o
j

9
7
3

3
v
[
0
s

(
%
)

(
%
)

"
3
 w
j
o
s

9
7
3

p
u
I
m

(
%
)

"
3

p
u
t
m

2
A
E
F
O
N

A
n
I
S
O
d

a
a
n
e
s
o
N

o
A
I
s
o
q

2
A
E
S
O
N

6
1
2
0
0
°
0
-

P
i
s

A
p
u
s
e
|
p
u
r
a
g

2
d
u
d
 p
a
r
S
i
o
m

2
7
 p
e
o
]

A
y
o
n
s
e
p
o

A
1
d
d
n
g

a
A
n
I
s
o
q

(
U
M
W
)
 1
5
8
9
9
1
0
)

p
e
o
'
]

p
u
e
w
o
p
—
[
H
H

A
d
d
n
s
—
T
H
H

A
w
w
n
p

A
w
m
p

 o
y

s
o
w
u
n
g

T
h
6
¢

7
8
9
7

7
9
8

1
0
0
>
4

s
 ‘
5
0
0
>
4
 1
1
0
>
 4

2
0
0
8

S
U
O
N
E
A
I
S
G
O
 J
O

J
a
q
u
I
n
y

Allrights reserved. Copyright © 20.

by the IAEE.

This content downloaded from

IR 6.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC I

All use subject to <https://about> jstor.org/terms

Analysis ofthe Bid-ask Spreadin Continuous Intraday Trading of the German Power Market / 249

7 REMARKS AND CONCLUSION

The continuous market is getting more and more attention in the literature as well as in the
public debate thanks to  (i)  the growing renewable capacity that increases the willingness to trade
very close to delivery and (ii) the single intraday coupling or XBID project which aims to harmonize
the cross-border intraday trading across Europe. The market quality and so the liquidity is  of major
importance for institutions but also market participants. This paper brings to light the behavior of
the liquidity along a trading session and find the main drivers of this liquidity.

While the literature on the bid-ask spread is dense, it remains applied to the financial mar-
kets. The power market has its  own specificities  that question the one-size-fit-all approch of the
model. The present paper, based on this  literature,  investigates the bid-ask spread of the German
continuous market taking into account those specificities.

First,  I  observe a “L-shaped” behavior of the bid-ask spread over an average trading ses-
sion of the German intraday market. There is a strong dispersion of the bid-ask spread at the begin-
ning of the trading session which then diminishes as the delivery time approaches. The dispersion
highlights the uncertainty away from the delivery time mainly due to the intermittent renewable
generation. On average, the local bid-ask spread is 3.5€ per MWh. The reverse shape applies for the
market depths that increase over the trading session.

Second, I  explain the bid-ask spread by four components: the risk,  the information, the
activity and the competition on the market. I  find that the risk and volatility of the market increase
the bid-ask spread. A fundamental (wind, solar or load) forecast error leads to a decrease of the bid-
ask spread by bringing more liquidity to the market except for the case of a negative load forecast
error which has a positive effect on the bid-ask spread probably due to the strategy of the suppliers.
Interestingly, I observe that a demand (load) versus a supply (wind or solar) shock does not have the
same impact on the bid-ask spread: a load forecast error has a stronger impact on the bid-ask spread
than a fundamental one. When the activity on the market increases, the spread tends to decrease, in
line with the positive relationship between the concentration on the market and the bid-ask spread.
The main results of the financial literature hold such as the positive relation between the
volatility and the bid-ask spread or the negative relation between the market activity and the bid-ask
spread. However, some results are specific to the power market such as the impact of a forecast error
that has a positive effect on the liquidity of the market. I  find a higher competition in the wholesale
market in comparison to the competition in the generation as well as a positive relationship between
the bid-ask spread and the concentration. The effort of promoting competition and a variety of actors
on the market should continue.

The question of the impact of the participants that do not have production assets or cus-
tomers—such as banks or trading houses, on the market liquidity is  an interesting question to in-
vestigate. Further work might include an extension of the model to other intraday power markets.
The model can also be enriched by including cross-border data.  Last but not least,  further work
could characterize the determinants of the bid-ask spread in a less aggregated form over the trading
session.

ACKNOWLEDGM  S

The author wants to thank the three anonymous referees for their comments that helped to
improve an earlier version of the manuscript. She would also like to thank EPEX SPOT, Pr. Bertrand
Villeneuve and Pr.  David Ettinger as well as the chair European Electricity Market for their sup-

Copyright © 2022 by the TAEE.  All rights reserved.

‘This content downloaded from
IIIII186.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC TIIIIIIT
All use subject to <https://about> jstor.org/terms

250/ The Energy Journal

port. The last thank you goes to the participants of the following conferences for their constructive
comments and remarks: YEEES Seminar—Spring 2017, 40th IAEE International Conference, 15th
IAEE European Conference, EDFLab, Commodities Market Winter Workshop 2018 (Nantes), and
the PhD. day at Dauphine University.

This paper has benefited from the  support of the Chaire European Electricity  Markets
(CEEM) of the Université Paris-Dauphine under the aegis of the Foundation Paris- Dauphine, sup-
ported by RTE, EDF, EPEX Spot and Total Direct Energie. The views and opinions expressed in
this paper are those of the authors and do not necessarily reflect those of the partners of the CEEM.

REFERENCES

Amanatidis, G. (2019). “European Policics on Climate and Encrgy towards 2020, 2030 and 2050.”
Angel, 1.1, L.E. Harris, and C.S. Spatt (2013). “Equity Trading in the 21st Century: An Update, June 21.” New York: Knight

Capital Group.

Angelidis, T. and A. Benos (2009). “The components of the bid-ask spread: The case of the Athens stock exchange.” Euro-

pean Financial Management 15(1):  112-144. https:/doi.org/10.1111/j.1468-036X.2007.00416 x.

Chaves-Avila, J.P, R.A. Hakvoort, and A. Ramos (2013). “Short-term strategics for Dutch wind power producers to reduce

imbalance costs.”  Energy Policy 52:  573-582. hitps://doi.org/10.1016/j.cnpol.2012.10.011.

Chen, X,, O. Linton, S. Schneeberger, and Y. Yi (2019). “Semiparametric estimation of the bid-ask spread in extended roll

models.”  Journal of Econometrics 208(1): 160-178. <https://doi.org/10.1016/.jcconom.2018.09.010>.
Copeland, T.E. and D. Galai (1983). “Information cffects on the bid-ask spread.” The Journal

of Finance 38(5):  1457-1469.

hitps://doi.org/10.1111/1.1540-626 1.1983.503834.x.

Demsetz,  H.  (1968).  “The  cost  of transacting.”  The  Quarterly Journal of Economiics  82(1):  33-53.  hitps://doi.

0rg/10.2307/1882244.

Dupuis, D.J.,  G. Gauthier, F. Godin, et al. (2016). “Short-term hedging for an electricity retailer.” The Energy Joumnal 37(2):

31-59. hitps:/doi.org/10.5547/01956574.37.2.ddup.

Geman, H. (2005). Commodities and commodity derivatives: pricing and modeling agricultural, metals and energy. West

Sussex, England: Wiley Finance.

Glosten, L.R. (1987). “Components of the bid-ask spread and the statistical properties of transaction prices.” The Journal of

Finance 42(5):  1293-1307. <https://doi.org/10.1111/j.1540-6261.1987.tb04367.x>.

Glosten, LR. and L.E. Harris (1988). “Estimating the components of the bid/ask spread.” Journal of Financial Economics

21(1): 123-142. hitps://doi.org/10. 1016/0304-405X(88)90034-7.

Glosten, L.R. and PR. Milgrom (1985). “Bid, ask and transaction prices in a specialist market with heterogencously informed

traders.”  Journal of Financial Economics 14(1): 71-100. <https://doi.org/10.101> 6/0304-405X(85)90044-3.

Hagemann, S. (2015). “Price determinants in the german intraday market for electricity: an empirical analysis.”  Journal of

Energy Markets. hitps://doi.org/10.21314/JEM.2015.128.

Hagemann, S. and C. Weber (2013). “An empirical analysis of liquidity and its determinants in the German intraday market

for electricity.” hitps://doi.org/10.2139/ssm.2349565.

Hasbrouck, J. (2004). “Liquidity in the futures pits: Inferring market dynamics from incomplete data.” Journal of Financial

and Quantitative Analysis 39(2): 305-326. hitps://doi.org/10.1017/S0022109000003082.

Hasbrouck, J. and G. Sofianos (1993). “The trades of market makers: An empirical analysis of NYSE specialists.” The Jour-

nal of Finance 48(5): 1565-1593. <https://doi.org/10.1111/.1540-6261.1993.tb0S> 121.x.

Huang, R.D. and H.R. Stoll  (1996). “Dealer versus auction markets: A paired comparison of execution costs on NASDAQ and

the  NYSE.” Journal of Financial Economics 41(3): 313-357. hitps://doi.org/10.1016/0304-405X(95)00867-E.

Huang, R.D. and HR. Stoll (1997). “The components of the bid-ask spread: A general approach.” The Review of Financial

Studies 10(4): 995-1034. <https://doi.org/10.1093/¢fs/10.4.995>.

Huang, Y.C. (2004). “The components of bid-ask spread and their determinants: TAIFEX versus SGX-DT.” The Journal of

Futures Markets 24(9): 835. hitps://doi.org/10.1002/fut 20113.

Ivanov, S.I. (2016). “Analysis of ETF bid-ask spread components.” The Quarterly Review of Economics and Finance 61:

249-259. <https://doi.org/10.1016/j.qref.2016.02.004>.

Karanfil, . and Y. Li (2017). “The Role of Continuous Intraday Electricity Markets: The Integration of Large-Share Wind

fkar.
Power Generation in Denmark.” The Energy Journal 38(2). hitps://doi.org/10.5547/01956574.38.2.

All rights reserved. Copyright © 2022 by the IAEE.

‘This content downloaded from
IIIII186.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC TIIIIIIT
All use subject to <https://about> jstor.org/terms

Analysis ofthe Bid-ask Spreadin Continuous Intraday Trading of the German Power Market  /251

Kiesel, R. and F. Paraschiv (2017). “Econometric analysis of 15-minute intraday clectricity prices.” Energy Economics 64:

77-90. hitps://doi.org/10.1016/j.eneco.2017.03.002.

Kim, S.-H. and J.P. Ogden (1996).  “Determinants of the components of bid-ask spreads on stocks.  European Financial Man-

agement 2(1):  127-145. https:/doi.org/10.1111/1.1468-036X.1996.tb00032.x.

Lhabitant, E-S. and G.N. Gregoriou (2008). Stock market liquidity: implications for market microstructure and asset pricing.

Volume 420, John Wiley & Sons.

Madhavan, A., M. Richardson, and M. Roomans (1997). “Why do sceurity prices change? A transaction-level analysis of

NYSE stocks.” The Review of Financial Studies 10(4): 1035-1064. <https://doi.org/10.1093/cfs/10.4.1035>.

Madhavan, A. and G. Sofianos (1998). “An empirical analysis  of NYSE specialist trading.”

Journal of Financial Economics

48(2): 189-210. hitps://doi.org/10.1016/S0304-405X(98)00008-7.

Manaster, S.  and S.C. Mann (1996). “Life in the pits:  Competitive market making and inventory control.” The Review of

Financial Studies 9(3): 953-975. hitps://doi.org/10.1093/rfs/9.3.953.

Melnish, T:H. and R.A. Wood (1992). “An analysis of intraday pattems in bid/ask spreads for NYSE stocks.” The Journal of

Finance 47(2): 753-764. <https://doi.org/10.1111/1.1540-6261.1992.th04408.x>.

Mizrach, B. and Y. Otsubo (2014). “The market microstructure of the European climate exchange.” Journal of Banking &
jbankfin 2013.11.001.
Finance 39: 107-116. <https://doi.org/10.1016/j>
Neuhoff, K., N. Ritter, A. Salah-Abou-El-Enien, and P. Vassilopoulos (2016). “Intraday markets for power: Discretizing the

continuous trading?” hitps:/doi.org/10.2139/ssrn.2723902.

Pape, C., S. Hagemann, and C. Weber (2016). “Are fundamentals enough? Explaining price variations in the German day-

ahead and intraday power market.” Energy Economics 54: 376-387. hitps://doi.org/10.1016/j.cneco.2015.12.013.

Roll, R. (1984). “A simple implicit measure of the cffective bid-ask spread in an efficient market.” The Journal of Finance

39(4):  1127-1139. <https://doi.org/10.1111/1.1540-6261.1984.th03897.x>.

Ryu, D. (2011). “Intraday price formation and bid-ask spread components:  A new approach using a cross-market model.”

Journal of Funires Markets 31(12): 1142-1169. <https://doi.org/10.1002/fut>  20533.

Scharff, R. and M. Amelin (2016). “Trading behaviour on the continuous intraday market Elbas.” Energy Policy 88: 544-557.

Schultz, P. (2000). “Regulatory and legal pressures and the costs of Nasdaq trading.” The Review of Financial Studies 13(4):

hitps://doi.org/10.1016/j.cnpol.2015.10.045.

917-957. hitps://doi.org/10.1093/rfs/13.4.917.

Schwartz, R.A. (1988). Equity markets: Structure, trading,  and performance. Harpercollins College Div.
Stoll, H.R. (1978). “The supply of dealer services in sccurities markets.” The Journal of Finance 33(4):  1133-1151. hitps:/

doi.org/10.1111/j.1540-6261.1978.tb02053 x.

Stoll, H.R. (1989). “Inferring the components of the bid-ask spread: Theory and empirical tests.” The Journal of Finance

44(1):  115-134. <https://doi.org/10.1111/j.1540-6261.1989.tb02407.x>.

Weber, C. (2010). “Adequate intraday market design to enable the integration of wind energy into the European power sys-

6/j.cnpol. 2009.07.040.
tems.” Energy Policy 38(7): 3155-3163.  <https://doi.org/10.101>

Zicl, F.  (2017). “Modeling the impact of wind and solar power forecasting errors on intraday electricity prices.” In “European
the,” IEEE 1-5. <https://doi.org/10.1109/EEM.2017.798> 1900.

Energy Market (EEM), 2017 14thInternational Conferenceon

Copyright © 2022

by the TAEE. All rights reserved.

‘This content downloaded from
IIIII186.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC TIIIIIIT
All use subject to <https://about> jstor.org/terms

252/ The Energy Journal

APPENDIX

Table 7: Abbreviations table

Abbreviation
TWh
MWh
DM
LPX
TSO
NYSE
MRR
NASDAQ
o1C
DAM
FOK
10C
LFOK
AON
CWE
BAS
MW
WAP
ED
ES
GWh
oLs
FGLS

Detailed factor
Terawatt-Hour
Megawatt-Hour
IntraDay Market
Leipzig Power Exchange
Transmission System Operator
New-York Stock Exchange
Madhavan, Richardson and Roomans
National Association of Securities Dealers Automated Quotations
Over-The-Counter
Day-Ahead Market
Fill-Or-Kill
Immediate-Or-Cancel
Linked Fill-Or-Killed
AlLOr-None
Central Western Europe
Bid-Ask Spread
Megawatt
Weighted Average Price
Demand Elasticity
Supply Elasticity
Gigawatt-Hour
Ordinary Least Squares
Feasible Generalized Least Squares

Figure 7: Distribution of the bid-ask spread

03-

00-

0

E

10

Bid-ask spread

15

2

All rights reserved. Copyright © 2022 by the IAEE.

‘This content downloaded from
IIIII186.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC TIIIIIIT
All use subject to <https://about> jstor.org/terms

Analysis ofthe Bid-ask Spreadin Continuous Intraday Trading of the German Power Market / 253

Figure 8: Distribution of the buy depth at the contract level

y
t
i
s
n
e
d

0.0005

0.0000

]

1000

2000

buy_depth

3000

4000

Figure 9: Distribution of the sell depth at the contract level

00015

00010,

]

00005,

00000

500

1600
sell_depth

1500

2000

Copyright © 2022

by the TAEE. All rights reserved.

‘This content downloaded from
IIIII186.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC TIIIIIIT
All use subject to <https://about> jstor.org/terms

254/ The Energy Journal

Figure 10: Bid-ask spread over an average trading session for various products

I
a0

:

5

h
W
M
R
U
E

n
i

d
a
e
r
p
s

d
e
t
o
u
Q

1800

0000

0600

200

Trading time

Figure 11: Sell depth over an average trading session for various products

5

]

s

40001

20001

40001

2000

W
M

n
i

h
t
p
e
d

l
l
e
S

1800

o0

o500

1200

1800

o0

g0

1200

Trading time

All rights reserved. Copyright © 2022 by the IAEE.

‘This content downloaded from
IIIII186.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC TIIIIIIT
All use subject to <https://about> jstor.org/terms

Analysis ofthe Bid-ask Spreadin Continuous Intraday Trading of the German Power Market / 255

L
1
0
%

£
6
0
°
0

L
5
0
'
0

1
4
0
°
0

2
0
0
0

0
£
0
'
0

1
0
0
0

2
1
0

6
6
0
°
0

n
z
o

0
£
0
'
0

0
0
0
'
1

0
0
0
0

1
0
0

£
2
0
°
0

T
1
0
%

L
0
0
%
0

8
0
0
0

8
0
0
0

8
L
0
%
0

8
L
0
0

T

0
0
0
1

0
£
0
%
0

C
I
H
H
V

G
I
H
H
V

v

L
£
0
0
%
0

1
5
0
°
0

1
o

o

1
8
1
0

T
1
0
%

£
6
0
°
0

0
1
0
0

9
1
0
0

0
0
0
1

a
u
r
o

1
o

I
V

X
}

€
1
0
0

6
1
0

S
5
0
°
0

S
H
0
°
0

0
1
0
°
0

2
0
0

0
6
2
0

0
0
0
1

9
1
0
°
0

L
0

6
6
0
0

2
V

£
2
0
°
0

9
£
0
%
0

8
1
0
0

£
2
0
°
0

6
0
0
0

#

0
0
'
0

8
2
0
0

0
0
0
'
1

0
6
2
0

0
1
0
'
0

8
L
0
°
0

2
1
0

2
2
8
V

2
 M
V

S
V

z
r
 M
V

‘
a
a
v

5
0
0
0

0
£
0
%
0

$
1
0
°
0

P
E
0
°
0

0
r
0
%
0

1
0
0
°
0

0
0
0
1

8
2
0
0

2
0
0

£
6
0
°
0

8
0
0
0

1
0
0
°
0

7
0
0
0

9
1
0
0

9
0
0
0

0
1
0
0

T
1
0
%

0
0
0
1

1
0
0
°
0

7
0
0
0

0
1
0
0

T
1
0
%

8
0
0
0

0
£
0
%
0

L
1
1
0
0

$
0
0
°
0

1
0
0

6
1
7
0

0
0
0
°
1

T
1
0
'
0

0
7
0
0

6
0
0
0

S
H
0
°
0

L
8
1
°
0

L
£
0
0
°
0

2
0
0
0

9
£
0
%
0

9
0
0
°
0

6
5
0
0

0
0
0
'
1

6
1
2
0

0
1
0
0

€
0
0

£
2
0
°
0

5
5
0
0

T
E
r

T
1
0
'
0

1
4
0
°
0

2
0
0

€
0
0
0

0
0
0
1

6
5
0
0

S
1
0
0

9
0
0
0

$
1
0
°
0

9
£
0
°
0

6
1
0
0

1
o

£
2
0
°
0

L
5
0
%
0

‘
s
a
v

9
5
0
0

0
0
0
1

£
0
0
°
0

9
8
0
0

5
0
0
0

9
1
0
0

0
£
0
%
0

8
1
0
0

€
1
0

1
5
0
°
0

1
0

£
6
0
°
0

o
y

0
0
0
1

9
5
0
°
0

2
0
0

9
0
0
0

L
1
1
0
0

7
0
0
0

£
2
0
°
0

$
0
0
°
0

0
0

L
£
0
0
°
0

0
0
0
0

L
1
0
0

“
s
a
v

‘
a
z
v

o
y

2
 M
V

<
2
i
S
V

2
 M
V

I

—
2
i
S
V

v

v

G
I
H
H
Y

(
I
H
H
V

Copyright © 2022 by the TAEE.  All rights reserved.

X
L
U
J
R
U

U
O
P
R
R
L
I
O
)
)

:
§

J
[
q
E
L

This content downloaded from

IR 6.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC I

All use subject to <https://about> jstor.org/terms

IAEE

International Association for
ENERGY ECONOMICS

Membership in the International Association for Energy Economics is open to anyone worldwide
who has an interest in the fields of energy or energy economics. Our membership consists of those
working in both the public and private sectors including government, academic and commercial.
Our current member base consists of 3900+ members in over 110 nations, with 28 nations having
local affiliate organization.

‘We are an independent, non-profit, global membership organization for business, government,
academic and other professionals concerned with energy and related issues in the international
community. We advance the knowledge, understanding and application of economics across all
aspects of energy and foster communication amongst energy concerned professionals.

‘We are proud of our membership benefit offerings, which include access to a rich library of
energy economics related publications and proceedings as well as a robust line-up of webinars,
podcasts and conferences.  Learn more about the benefits of membership at:
<https://www.iaee.org/en/membership/benefits.aspx>

In addition to traditional membership, we offer student and institutional memberships.

‘This content downloaded from
IIIII186.49.238.177 on Wed, 29 Apr 2026 10:27:52 UTC TIIIIIIT
All use subject to <https://about> jstor.org/terms
