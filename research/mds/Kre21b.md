royalsocietypublishing.org/journal/rsta

Research

Cite this article: Kremer M, Kiesel R,
Paraschiv F. 2021 An econometric model for
intraday electricity trading. Phil. Trans. R.
Soc. A 379: 20190624.
https://doi.org/10.1098/rsta.2019.0624

Accepted: 1 May 2020

One contribution of 11 to a theme issue ‘The
mathematics of energy systems’.

Subject Areas:
energy, power and energy systems,
mathematical finance, applied mathematics,
mathematical modelling

Keywords:
intraday electricity market, econometric
modelling, 15-min contracts, renewable power
forecasts, merit order curve, threshold
regression

Author for correspondence:
Marcel Kremer
e-mail: marcel.kremer@uni-due.de

An econometric model for
intraday electricity trading
Marcel Kremer1, Rüdiger Kiesel1,2 and
Florentina Paraschiv3,4

1Chair for Energy Trading and Finance, University of Duisburg-Essen,
Universitätsstraße 12, 45141 Essen, Germany
2Department of Mathematics, University of Oslo, PO Box 1053
Blindern, 0316 Oslo, Norway
3NTNU Business School, Norwegian University of Science and
Technology, 7491 Trondheim, Norway
4Institute for Operations Research and Computational Finance,
University of St. Gallen, Bodanstrasse, 6, CH-9000 St. Gallen,
Switzerland

MK, 0000-0001-9130-7670

This paper develops an econometric price model with
fundamental impacts for intraday electricity markets
of 15-min contracts. A unique dataset of intradaily
updated forecasts of renewable power generation is
analysed. We use a threshold regression model to
examine how 15-min intraday trading depends on
the slope of the merit order curve. Our estimation
results reveal strong evidence of mean reversion in
the price formation mechanism of 15-min contracts.
Additionally, prices of neighbouring contracts exhibit
strong explanatory power and a positive impact on
prices of a given contract. We observe an asymmetric
effect of renewable forecast changes on intraday prices
depending on the merit-order-curve slope. In general,
renewable forecasts have a higher explanatory power
at noon than in the morning and evening, but price
information is the main driver of 15-min intraday
trading.

This article is part of

the theme issue ‘The

mathematics of energy systems’.

1.

Introduction

Electronic supplementary material is available
online at https://doi.org/10.6084/m9.
figshare.c.5361961.

In recent years, the expansion of renewable energy
sources has been forged ahead massively across the
globe with a direct impact on electricity markets. As
electricity generation from renewable energy sources

Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2019.0624/373490/rsta.2019.0624.pdf
by guest
on 05 April 2026

2021 The Author(s) Published by the Royal Society. All rights reserved.

flat

steep

2

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

r
o
y
a
l
s
o
c
i
e
t
y
p
u
b

i

l
i
s
h
n
g
.
o
r
g
/
j
o
u
r
n
a
l
/
r
s
t
a

P
h

i
l
.

T
r
a
n
s
.

.
S
o
c
.

A
3
7
9

:

2
0
1
9
0
6
2
4

.

R

w/o RES
with RES

e
c
i
r
p

y
t
i
c
i
r
t
c
e
l
e

DPs

DPf

RES

demand

Figure 1. Merit order curve without (blue solid) and with (green dash-dotted) infeed from renewable energy sources (RES)
indicating a flat and steep merit-order regime (red dashed) with electricity price changes (cid:2)Pf and (cid:2)Ps, respectively. (Online
version in colour.)

cannot be predicted reliably in the long term, that is, days, weeks or months ahead, the future of
electricity trading is foreseen in short-term electricity markets. Energy supply companies thus face
the challenge of moving towards automatic trading, which requires the identiﬁcation of trading
strategies based on local demand and supply patterns as well as cross-border energy ﬂows.
The German market constitutes a pioneer among European electricity markets. Not only is the
German market the largest electricity market in Europe in terms of total trading volume [1], but
also novel developments and innovations (new contracts, reduction of lead time) are traditionally
introduced on the German market ﬁrst. In Germany, the most short-term electricity market is the
continuous intraday market, where hourly and 15-min contracts can be traded until 5 min before
the delivery of electricity begins. Intraday electricity markets are designed according to the needs
of energy supply companies to balance forecast errors of renewable power generation.

This paper investigates four research questions: (i) Which factors drive the intraday trading of
15-min contracts? (ii) How do forecast changes of renewable power generation affect the intraday
trading of 15-min contracts? (iii) Can we identify different regimes on the intraday market where
the price formation process behaves differently? (iv) How does intraday trading depend on the
time of day?

Like on any ﬁnancial market, there is a natural desire for pricing models of the basic securities.
To build as realistic models as possible, we require ex-ante information on the underlying price
drivers. More market-speciﬁcally, and in light of the design of intraday electricity markets,
forecast errors of renewable power production have to be taken into account. [2] deliver the ﬁrst
and only work fulﬁlling these prerequisites. Our article builds upon their work and develops an
econometric price model with fundamental impacts for continuous intraday markets of 15-min
contracts.

Our main modelling assumption is that the price formation process on the intraday electricity
market depends on the slope of the merit order curve. Figure 1 illustrates a merit order curve with
and without the infeed from renewable energy sources (RES). The merit order curve is a nonlinear
and convex function of the marginal costs of power plants depending on the generation capacity.
Equivalently, since the marginal costs of the last running power plant needed to cover demand set
the ﬁnal electricity price, the merit order curve may be interpreted as a function of the electricity
price depending on the electricity demand, too.

Let us consider the merit order curve without renewable power infeed (blue solid). When there
is low demand, only relatively cheap power generation technologies such as lignite-ﬁred power
plants are needed, whereas if demand is high, more expensive technologies such as gas-ﬁred

Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2019.0624/373490/rsta.2019.0624.pdf
by guest
on 05 April 2026

3

r
o
y
a
l
s
o
c
i
e
t
y
p
u
b

i

l
i
s
h
n
g
.
o
r
g
/
j
o
u
r
n
a
l
/
r
s
t
a

P
h

i
l
.

T
r
a
n
s
.

.
S
o
c
.

A
3
7
9

:

2
0
1
9
0
6
2
4

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

R

power plants might be required to satisfy demand. As exhibited in ﬁgure 1, if demand is low, the
slope of the merit order curve is relatively small and the market is said to be in a ﬂat merit-order
regime; however, if demand is high, the merit-order-curve slope is comparatively large and the
market is said to be in a steep merit-order regime.

Let us turn towards the merit order curve with renewable power infeed (green dash-dotted).
Since renewable energy sources have zero marginal costs, their infeed shifts the entire merit order
curve to the right. As a consequence, if demand is low (ﬂat regime), the electricity price decreases
by a small amount (cid:2)Pf ; however, if demand is high (steep regime), the electricity price decreases
as well but by a much larger amount (cid:2)Ps > (cid:2)Pf . We take into account this asymmetric effect of
renewable power infeed on electricity prices in our econometric model by incorporating the slope
of the merit order curve.

To model the merit order curve, two approaches have been proposed in the academic literature.
The ﬁrst approach models the merit order curve from the supply side via generation capacities
and marginal costs of power plants. While generation capacities are given by market transparency
data, one has to specify a model for the marginal costs of power plants. [3–5] model the marginal
costs as a function of fuel prices, CO2 emission allowances prices, emission intensities of fuel
types, power plant heat rates or thermal efﬁciencies, and other variable costs. As marginal costs
depend on a wide variety of factors, this approach is highly complex and subject to strong
modelling assumptions. The second approach models the merit order curve from the demand side
via electricity loads, or load forecasts, and electricity prices as proposed by [6,7]. While electricity
load is an indicator of total electricity demand, electricity prices are determined by the marginal
costs of the price-setting power plant (marginal power plant). As data for both electricity loads
and prices exist, this approach does not rely on modelling assumptions. Therefore, we follow the
demand-side approach.

The intraday electricity market of 15-min contracts has only recently come into the focus of
scientiﬁc research. To the best of our knowledge, only three studies existed hitherto. [2] provide
the ﬁrst econometric model for 15-min intraday prices. They model both deviations between day-
ahead and last intraday prices as well as continuous intraday prices in a threshold regression
context. They provide evidence that 15-min prices respond asymmetrically to intradaily updated
renewable forecast errors depending on the proportion of expected demand covered by
conventional energy sources. [8] study how the introduction of 15-min contracts has affected the
day-ahead and intraday market of hourly contracts. They ﬁnd that prices of hourly contracts
decreased and trading volumes increased. [9] present the ﬁrst forecasting study of 15-min prices
using an elastic net regression model. They conclude that prices in the intraday auction are much
easier to forecast than prices in the continuous trading.

This article extends the existing literature along a number of dimensions: ﬁrst, we explore a
novel and unique dataset of high-frequency transaction data and linked fundamental supply and
demand data. Intradaily updated forecasts of renewable power generation (solar, wind) constitute
the heart of our data collection. These are the same real-time renewable forecasts as available to
traders on the intraday market. As such, this is the most extensive dataset used in the empirical
literature to study the price formation process on intraday electricity markets. Hence, our dataset
allows for a more realistic model speciﬁcation than proposed in previous research.

Second, we suggest the ﬁrst econometric price model for 15-min contracts that incorporates
the slope of the merit order curve. This is a substantial improvement over [2] as electricity prices
react asymmetrically to renewable forecast changes depending on the merit-order-curve slope: if
the merit order is steep, electricity prices change more severely in the wake of renewable forecast
errors than if the merit order is ﬂat. Moreover, our econometric model solely involves ex-ante
market knowledge.

Third, and to the best of our knowledge, this is the ﬁrst work studying the inﬂuence of
neighbouring 15-min contracts on the price dynamics of a given contract. This is motivated by
the fact that adjacent contracts are driven by similar market information.

This paper is organized as follows: in §2, we lay out our dataset and perform an empirical
analysis of intraday transaction data of 15-min contracts. In §3, we present our econometric model

Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2019.0624/373490/rsta.2019.0624.pdf
by guest
on 05 April 2026

as well as the threshold regression. In §4, we calibrate our econometric model to market data and
discuss the estimation results. We offer our conclusions in §5.

4

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

r
o
y
a
l
s
o
c
i
e
t
y
p
u
b

i

l
i
s
h
n
g
.
o
r
g
/
j
o
u
r
n
a
l
/
r
s
t
a

P
h

i
l
.

T
r
a
n
s
.

.
S
o
c
.

A
3
7
9

:

2
0
1
9
0
6
2
4

.

R

2. Stylized facts

In this section, we lay out our dataset and empirically analyse transaction prices and trading
volumes of 15-min contracts.

(a) Data

We investigate high-frequency trade and linked fundamental data of all 96 15-min contracts
traded on the German continuous intraday power market at EPEX SPOT SE. Our observation
period spans from 1 January to 31 December 2015. The trade data of 15-min contracts involve
transaction prices and trading volumes from the continuous intraday trading session with a
1-min time resolution and are provided by [10]. This, however, does not imply that we observe
one transaction every minute, but it may take a multiple of one minute until the subsequent
transaction is observed. In case of multiple transactions within the same trading minute, we
compute the volume-weighted average price for that minute. The continuous trading session for
15-min contracts opens daily at 16:00 and, in 2015, ends 45 and 30 min before delivery begins,
respectively.1,2 Furthermore, we use market clearing prices of 15-min contracts traded in the
German 15-min intraday auction at EPEX SPOT SE, which takes place daily at 15:00, provided
by [13]. The auction data may also be obtained via the R package emarketcrawlR by [14]. We
shall denote a 15-min contract by HhQq with h = 0, . . . , 23 and q = 1, . . . , 4; e.g. contract H13Q1
refers to the delivery period 13:00–13:15.

As fundamental data, we include intraday wind and solar power forecasts and expected
demand. The intraday renewable power forecasts involve intradaily updated forecasts of wind
and solar power production in Germany, which are the same real-time renewable forecasts as
available to traders on the intraday market. These forecasts are updated every 15 min, where each
update contains a forecast time series for the following eight days in a 15-min time resolution,
provided by [15]. As such, the intraday renewable power forecasts constitute a unique dataset
and, to the best of our knowledge, have solely been analysed by [2]. As an indicator of expected
electricity demand, we use the day-ahead total load forecast for each quarter-hour on the
following day in Germany, which is published daily at 10:00 and is provided by [16].

(b) Hourly seasonality

(i) Transaction prices

Figure 2 illustrates the volume-weighted average transaction price of 15-min contracts during
peak hours and off-peak hours for summer and winter. We identify an hourly seasonality of
volume-weighted average prices for both peak and off-peak hours as well as for summer and
winter.3 The hourly seasonality exhibits a sawtooth-like shape: for the peak-hour contracts H8Q1–
H13Q4, the average price of the ﬁrst 15-min contract within each hour is the highest and it
declines until the last 15-min contract within that hour, which has the lowest average price.
Conversely, for contracts H14Q1–H18Q4, the lowest average price is present for the ﬁrst 15-min
contract which increases up to the highest average price for the last 15-min contract in a given
hour.

1EPEX SPOT SE reduced the lead time on the German continuous intraday power market for hourly and 15-min contracts
from 45 to 30 min before delivery on 16 July 2015 [11].

2On 14 June 2017, the lead time within the four German control zones was locally further reduced to 5 min before delivery [12].

3The hourly seasonality preserves for unweighted average transaction prices both qualitatively and quantitatively: The
seasonal averages of unweighted and volume-weighted average prices differ by roughly 2% only.

Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2019.0624/373490/rsta.2019.0624.pdf
by guest
on 05 April 2026

5

r
o
y
a
l
s
o
c
i
e
t
y
p
u
b

i

l
i
s
h
n
g
.
o
r
g
/
j
o
u
r
n
a
l
/
r
s
t
a

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

P
h

i
l
.

T
r
a
n
s
.

.

R

.

.

.

.

.

.
S
o
c
.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

A
3
7
9

:

2
0
1
9
0
6
2
4

(a)

f
o

e
g
a
r
e
v
a

l
a
n
o
s
a
e
s

e
g
a
r
e
v
a

d
e
t
h
g
i
e
w
-
e
m
u
l
o
v

)
h
W
M
R
U
E
(

/

s
e
c
i
r
p

n
o
i
t
c
a
s
n
a
r
t

50

40

30

20

(b)

50

40

30

20

f
o

e
g
a
r
e
v
a

l
a
n
o
s
a
e
s

e
g
a
r
e
v
a

d
e
t
h
g
i
e
w
-
e
m
u
l
o
v

)
h
W
M
R
U
E
(

/

s
e
c
i
r
p

n
o
i
t
c
a
s
n
a
r
t

summer
winter

H20Q1

H0Q1

H4Q1

H8Q1

summer
winter

H8Q1

H12Q1

H16Q1

H20Q1

quarter-hourly contract

quarter-hourly contract

Figure 2. Volume-weighted average transaction price of 15-min contracts during peak hours (a) and off-peak hours
(b) averaged over summer (red dashed) and winter (blue solid). (Online version in colour.)

The hourly seasonality pattern and its change around noon may be explained by electricity
generation from solar energy: in the ﬁrst half of the day, the sun rises and less electricity from
solar energy is produced during the ﬁrst quarter-hour when compared with the last quarter-
hour within each hour. If a (renewable) electricity supplier sold an hourly contract on the day-
ahead market, it has to buy electricity for the ﬁrst quarter-hour on the intraday market to meet its
obligation since less electricity is produced from solar energy than it has sold (buy pressure); thus
prices increase. In the last quarter-hour, however, more solar electricity is generated than it has
sold on the day-ahead market and so it wants to sell the surplus on the intraday market to avoid
entering the balancing energy market (sell pressure); hence prices decrease. In the second half of
the day, after the sun has reached its highest level (around 14:00 in Germany), more solar power is
generated during the ﬁrst than in the last quarter-hour in each hour. Thus, there is a sell pressure
in the ﬁrst and a buy pressure in the last quarter-hour of an hour, and the pattern is reversed. The
existence of buy and sell pressure is underpinned by the hourly seasonality of trading volumes
described in §ii.

Similarly, the sawtooth-shaped hourly seasonality of volume-weighted average prices is found
during off-peak hours. For contracts H20Q1–H1Q4, the average price of the ﬁrst and last quarter-
hourly contract within an hour is highest and lowest, respectively, while for contracts H4Q1–
H6Q4, this is reversed. The hourly seasonality at night stems from the electricity demand proﬁle
in conjunction with established hourly delivery positions from the day-ahead auction (see [17] for
a detailed discussion).

Overall, during peak hours, average transaction prices are lower in summer than in winter
apart from a few exceptions. In the afternoon and evening hours, that is, for contracts H14Q1–
H19Q4, we ﬁnd larger deviations between summer and winter average prices than in morning
and noon hours. During off-peak hours, average prices are fairly similar during both seasons
most of the time and only slightly lower in winter than in summer.

(ii) Trading volumes

Figure 3 shows the total trading volume of 15-min contracts during peak hours and off-peak
hours averaged over the year. We only present the yearly average of total trading volumes as
the distinction between summer and winter does not provide additional information. Similar
to transaction prices, we observe an hourly seasonality of total trading volumes for both peak
and off-peak hours. The hourly seasonality of trading volumes has a U-shape: larger total
trading volumes are found for the ﬁrst and last 15-min contract within each hour of the day,
while the second and third 15-min contract in an hour always exhibit lower trading volumes.
More speciﬁcally, the last 15-min contract entails the largest trading volume, while the second
15-min contract involves the lowest trading volume in an hour. The U-shaped hourly seasonality
supports our hypothesis of buy and sell pressure for the marketing of solar power in the ﬁrst and
last quarter-hour during peak hours, respectively.

Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2019.0624/373490/rsta.2019.0624.pdf
by guest
on 05 April 2026

6

r
o
y
a
l
s
o
c
i
e
t
y
p
u
b

i

l
i
s
h
n
g
.
o
r
g
/
j
o
u
r
n
a
l
/
r
s
t
a

P
h

i
l
.

T
r
a
n
s
.

.
S
o
c
.

A
3
7
9

:

2
0
1
9
0
6
2
4

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

R

(a)

f
o

e
g
a
r
e
v
a

y
l
r
a
e
y

)

W
M

(

s
e
m
u
l
o
v

g
n
i
d
a
r
t

l
a
t
o
t

1000

800

600

400

200

(b)

f
o

e
g
a
r
e
v
a

y
l
r
a
e
y

)

W
M

(

s
e
m
u
l
o
v

g
n
i
d
a
r
t

l
a
t
o
t

1000

800

600

400

200

H8Q1

H12Q1

H16Q1

H20Q1

H20Q1

H0Q1

H4Q1

H8Q1

quarter-hourly contract

quarter-hourly contract

Figure 3. Total trading volume of 15-min contracts during peak hours (a) and off-peak hours (b) averaged over the year. (Online
version in colour.)

(a)

1 × 104

s
e
d
a
r
t

.
o
n

3

2

1

0

1 × 106

(b)

)

W
M

[
(

e
m
u
l
o
v

g
n
i
d
a
r
t

l
a
t
o
t

1.0

0.8

0.6

0.4

0.2

0

3

1
2
hour to gate closure

0

3

1
2
hour to gate closure

0

Figure 4. Time evolution of the number of trades (a) and total trading volume (b) through the trading session towards gate
closure. (Online version in colour.)

15-min contracts during off-peak hours are generally associated with less trading volume
than peak-hour contracts. Total trading volumes are particularly low for contracts H0Q1–H5Q4.
However, the U-shaped hourly seasonality of trading volumes is persistent during off-peak hours.
The hourly seasonality at night results from the electricity demand proﬁle along with established
hourly day-ahead positions [17].

(c) Liquidity evolution

(i) Gate closure

Figure 4 displays the temporal evolution of liquidity of 15-min contracts over the trading session
towards gate closure. As measures for market liquidity, we use the number of trades and total
trading volume aggregated over all 15-min contracts and all trading sessions. Due to low liquidity
far from gate closure, we focus on the last three trading hours prior to gate closure. We note that
EPEX SPOT SE reduced the lead time on the German intraday power market for hourly and
15-min contracts from 45 to 30 min before delivery on 16 July 2015 [11]. Thus, to avoid effects
due to the shift of lead time, we synchronize our trade time series with respect to gate closure by
shifting the trade time stamps of 15-min contracts maturing before 16 July 2015 by 15 min.

The number of trades increases from 952 3 h to gate closure to 3054 1 h to gate closure.
Subsequently, the number of trades rises further and more than doubles to 7080 half an hour
to gate closure. 15 min to gate closure, the number of trades jumps to 16 593 while 13 min before
gate closure it reaches a local maximum of 28 378. The surge of trading activity around 15 min

Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2019.0624/373490/rsta.2019.0624.pdf
by guest
on 05 April 2026

r
o
y
a
l
s
o
c
i
e
t
y
p
u
b

i

l
i
s
h
n
g
.
o
r
g
/
j
o
u
r
n
a
l
/
r
s
t
a

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

P
h

i
l
.

T
r
a
n
s
.

.

R

.

.

.

.

.

.
S
o
c
.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

A
3
7
9

:

2
0
1
9
0
6
2
4

1 × 104

7

1 × 103

(a)

s
e
d
a
r
t

.
o
n

5

4

3

2

1

0

(b)

)

W
M

(

e
m
u
l
o
v

g
n
i
d
a
r
t

l
a
t
o
t

6

4

2

0

0

0.5

1.0
hour from gate opening

1.5

2.0

0

0.5

1.0
hour from gate opening

1.5

2.0

Figure 5. Time evolution of the number of trades (a) and total trading volume (b) after gate opening. (Online version in colour.)

to gate closure may be associated with the fact that a given contract becomes the front 15-min
contract. The maximum value of 30 512 trades is observed 1 min to gate closure.

The total trading volume increases from 12 GW to 48 GW between 3 and 1 h to gate closure.
Thereafter, trading volume almost triples to 135 GW half an hour to gate closure. 15 and 13 min
before gate closure, total trading volume raises to 261 GW and 314 GW, respectively, which
coincides with becoming the front 15-min contract. A comparison with the number of trades at
these points in time in ﬁgure 4 reveals that indeed a vast number of transactions is executed but
with comparatively low trading volumes. The total trading volume peaks at 960 GW one minute
to gate closure.

Thus, we observe that liquidity of 15-min contracts rises severely within the last trading hour
prior to gate closure: on average, roughly 68% of the number of transactions are executed and
roughly 74% of the total trading volume is transferred. The reason why the majority of trading
takes place close to gate closure is that forecasts of fundamentals, particularly renewable power
forecasts, become more and more precise regarding the delivery period of a given 15-min contract.
Hence, it is desirable to trade as close to delivery beginning as possible. [18,19] document an
increasing liquidity towards gate closure for hourly contracts on the German intraday electricity
market, too.

We identify a small but distinct rise in liquidity every 15 min. This is particularly pronounced
for the number of trades but present for the total trading volume, too. Consequently, an increased
amount of transactions with relatively little trading volume is conducted periodically. We argue
that the 15-min periodicity in liquidity originates from newly arriving renewable forecast updates.
As described in §a, renewable forecasts are updated in 15-min intervals. New forecasts will not
have changed much after 15 min and thus traders only make minor adjustments to their positions
by trading little volume. Moreover, we observe that trading activity increases at isolated points
in time and dies out immediately until the next increase. Therefore, we conclude that renewable
forecast updates are reﬂected in prices of 15-min contracts within one trading minute.

(ii) Gate opening

Figure 5 illustrates the temporal development of liquidity of 15-min contracts after gate opening
at 16:00. The number of trades amounts to 4718 just after gate opening and decreases to 705 12 min
after gate opening. 15 min after gate opening, the number of trades reaches its maximum value
of 5309, which drains within the next trading minute. Similarly, liquidity jumps to 2276 trades
30 min after gate opening and falls back to its prior level within two trading minutes. Thereafter,
liquidity approaches a fairly stable level of 185 trades, on average, between 1 and 2 h after gate
opening.

Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2019.0624/373490/rsta.2019.0624.pdf
by guest
on 05 April 2026

The total trading volume peaks at 58 GW shortly after gate opening and steadily declines to
5.6 GW 12 min after gate opening. 15 min after gate opening, total trading volume rises to 13 GW
while it amounts to 3.5 GW 30 min after gate opening. Comparing trading volume and the number
of trades at these points in time shows that the surge in trading activity involves relatively little
trading volume. Subsequently, the total trading volume keeps a quite constant and low level
around 1.5 GW until 2 h after gate opening.

Thus, liquidity of 15-min contracts is high close to gate opening and drops substantially during
the ﬁrst 12 trading minutes. This behaviour may be explained by the fact that market participants
initialize their positions. In the sequel, little volume is traded and thereby only minor adjustments
are made to the open positions. Generally, liquidity remains poor until the last trading hour prior
to gate closure as the forecasts of fundamentals are still relatively inaccurate.

3. Methodology

We aim at modelling the asymmetric response of 15-min intraday electricity prices to explanatory
variables, in particular, to renewable forecast changes depending on the slope of the merit order
curve. We suggest an extension of the econometric model by [2] to overcome its weaknesses and
employ a threshold regression model to calibrate our model to market data.

(a) Extended econometric model

We reﬁne the econometric model by [2] along three dimensions by incorporating supplementarily:
(i) the slope of the merit order curve, (ii) price changes of neighboring 15-min contracts, (iii) the
15-min intraday auction price. For a given 15-min contract i = 1, . . . , 96, the model speciﬁcation
reads

8

r
o
y
a
l
s
o
c
i
e
t
y
p
u
b

i

l
i
s
h
n
g
.
o
r
g
/
j
o
u
r
n
a
l
/
r
s
t
a

P
h

i
l
.

T
r
a
n
s
.

.
S
o
c
.

A
3
7
9

:

2
0
1
9
0
6
2
4

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

R

+ η(i)
4
− P(i)

(cid:2)P(i)
t

= α(i)
0

+

m(cid:2)

τ =1

τ (cid:2)P(i)
α(i)

t−τ +

n(cid:2)

j=−n,
j(cid:2)=0

β(i)
j

(cid:2)P

(i+j)
t

+ η(i)
1

ξ (i) + η(i)

2 PAuc,(i) + η(i)

3 V(i)

t

(cid:2)wn,(i)
t

+ η(i)
5

p,(i)
(cid:2)w
t

+ η(i)
6

(cid:2)sn,(i)
t

+ η(i)
7

(cid:2)s

p,(i)
t

+ η(i)
8

(cid:3)

(cid:2)t(i) + (cid:8)(i)
t

,

(3.1)

(i+j)
t

t

= P(i)
t

= min((cid:2)w(i)
t

t−1 denotes the transaction price change between times t and t − 1, (cid:2)P

where (cid:2)P(i)
t
the last observed price change at time t of neighbouring contract i + j, ξ (i) the slope of the
merit order curve, PAuc,(i) the 15-min intraday auction price, V(i)
the trading volume at time
t
p,(i)
t, (cid:2)wn,(i)
= max((cid:2)w(i)
, 0) and (cid:2)w
, 0) negative and positive wind power forecast
t
t
t
changes, respectively, where (cid:2)w(i)
− w(i)
t−1 is the last available wind power forecast change
t
p,(i)
at time t, (cid:2)sn,(i)
= max((cid:2)s(i)
, 0) negative and positive solar power
t
t
forecast changes, respectively, where (cid:2)s(i)
− s(i)
= s(i)
t−1 is the last available solar power forecast
t
t
change at time t, and (cid:2)t(i) the interarrival time between two consecutive transactions conducted
at times t and t − 1 of contract i.

= w(i)
t
, 0) and (cid:2)s

= min((cid:2)s(i)
t

(i+j)
t

The ﬁrst sum in equation (3.1) covers m lagged price changes (cid:2)P(i)

t−τ , τ = 1, . . . , m, that is,
autoregressive terms. To determine the number of lags, we use the partial autocorrelation of
price changes and choose m = 3. The second sum in equation (3.1) captures the price change
, j = −n, . . . , n, j (cid:2)= 0, at time t of n 15-min contracts maturing before and n 15-min contracts
(cid:2)P
maturing after contract i. For example, if n = 2 and i = H13Q1, the price change of contracts
H12Q3, H12Q4, H13Q2, H13Q3 is included. The intraday auction price PAuc,(i) remains constant
during the continuous trading session of a given contract i and can be considered as an estimate
of the initial price of contract i in the continuous trading. Moreover, we distinguish between
p
t , (cid:2)s
positive and negative wind and solar power forecast errors (cid:2)w
t , respectively,
as we expect them to have opposite effects on electricity price changes (cid:2)Pt: positive renewable
forecast errors should decrease electricity prices, whereas negative renewable forecast errors
should increase electricity prices. We control for the interarrival time (cid:2)t since transactions do

p
t and (cid:2)wn

t , (cid:2)sn

Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2019.0624/373490/rsta.2019.0624.pdf
by guest
on 05 April 2026

9

r
o
y
a
l
s
o
c
i
e
t
y
p
u
b

i

l
i
s
h
n
g
.
o
r
g
/
j
o
u
r
n
a
l
/
r
s
t
a

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

P
h

i
l
.

T
r
a
n
s
.

.

R

.

.

.

.

.

.
S
o
c
.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

A
3
7
9

:

2
0
1
9
0
6
2
4

not take place at equidistant points in time, but it may take one minute or several hours until the
next trade is conducted.

We use the slope of the merit order curve ξ (i) as threshold variable instead of the demand
quota compared to [2]. The demand quota is deﬁned as the ratio of the expected demand and
the expected conventional capacity. As such, the demand quota quantiﬁes the proportion of
expected demand which is expected to be met by conventional power generation capacities; or,
put another way, how much the expected conventional capacity does cover expected demand.
One weakness of the demand quota is that it does not recognize whether the market is in a ﬂat
or steep merit-order-curve regime. Proportionally speaking, a high expected demand and high
expected conventional capacity lead to the same value of the demand quota as low demand and
low capacity. Another weakness is that the demand quota aggregates expected capacities over
all conventional generation technologies. Thus, it loses information on the price-setting power
plant and the slope of the merit order curve. We overcome these limitations in our extended
econometric model (3.1).

We estimate ξ (i) from empirical intraday auction prices PAuc,(i) and expected demands, or total
load forecasts, (cid:9)(i) in the spirit of [6,7]. This approach is reasonable for describing the slope of the
merit order curve since the level of intraday auction prices reﬂects the marginal costs of power
plants needed to cover expected demand. [6,7] construct a merit order curve for the electricity
spot market as a whole, independent of the contract, from hourly day-ahead prices and hourly
load forecasts. We, however, determine a merit order curve for each 15-min contract i individually
and thus arrive at a more ﬁne-grained picture. We ﬁt a function f ((cid:9)) to the price-load data and call
f ((cid:9)) the empirical merit order curve.4 Then, we take the derivative of the empirical merit order
((cid:9)) to obtain empirical
curve f
merit-order-curve slopes ξ (i) = f

d(cid:9) and substitute empirical expected demands (cid:9)(i) into f

((cid:9)) = df ((cid:9))

((cid:9)(i)).

(cid:3)

(cid:3)

(cid:3)

The slope of the merit order curve ξ (i) remains constant during the trading session of a given
contract i. The value of ξ (i) can be determined daily around 15:10, after the publication of the
intraday auction results, and hence before continuous trading begins. Thus, ξ (i) indicates whether
the market is in a ﬂat or steep merit-order regime before continuous trading begins and the
corresponding intraday price model can be chosen ex-ante. This is an attractive feature of our
econometric model for practical applications.

(b) Threshold regression

We use the threshold regression model introduced by [20] to calibrate our econometric model
to market data. The threshold regression model is able to reveal asymmetries in the impact of
explanatory variables with respect to a speciﬁed threshold variable. The basic concept of the
threshold regression involves two steps: ﬁrst, the entire sample is split into two subsamples, also
referred to as groups, classes, or regimes, at a certain threshold value of a designated threshold
variable; second, a linear regression model is estimated on each subsample separately.

}n
More formally, suppose we observe the sample {yi, xi, qi
i=1, where yi is the dependent variable,
∈ Rm collects the independent variables, and qi denotes the threshold variable. The threshold

xi
regression model reads

(cid:4)

θ (cid:3)
1 xi
θ (cid:3)
2 xi

=

yi

≤ γ

> γ

+ ε
if qi
i,
+ ε
if qi
i,
≤ γ } + θ (cid:3)

,

= θ (cid:3)

1{qi

1 xi

2 xi
∈ Rm collect the regression parameters, 1 denotes the
where γ is the threshold parameter, θ
indicator function, and ε
i is the error term. Thus, the observed sample is split into two subsamples
along the threshold variable qi at a speciﬁc value γ . By design, the threshold regression model (3.2)
allows the regression parameters in θ

2 to vary between the regimes.

1, θ

(3.2)

1, θ

i ,

2

1{qi

> γ } + ε

i = 1, . . . , n,

4[6] call f empirical price load curve.

Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2019.0624/373490/rsta.2019.0624.pdf
by guest
on 05 April 2026

10

r
o
y
a
l
s
o
c
i
e
t
y
p
u
b

i

l
i
s
h
n
g
.
o
r
g
/
j
o
u
r
n
a
l
/
r
s
t
a

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

P
h

i
l
.

T
r
a
n
s
.

.

R

.

.

.

.

.

.
S
o
c
.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

A
3
7
9

:

2
0
1
9
0
6
2
4

data
fit

)
h
W
M
R
U
E
(

/

c
u
A
P
e
c
i
r
p

n
o
i
t
c
u
a

40

20

0

40

50

60

70

expected demand l (GW)

Figure 6. Empirical merit-order-curve function f ((cid:9)) = ea (cid:9)+b (red) fitted to the empirical intraday auction price PAuc,(i)
function of expected demand (cid:9)(i)
colour.)

as a
d (blue) observed on days d = 1, . . . , T, for 15-min contract i = H13Q4. (Online version in

d

The regression parameters θ

2, γ can be estimated by least squares and jointly minimize
the sum of squared errors function. A detailed description of the estimation of the regression
parameters is provided in Section A in the electronic supplementary material. We use the R
package thrreg developed by [21] to estimate the threshold regression model.

1, θ

4. Estimation results

We estimate the parameters of the extended econometric model (3.1) by the threshold regression
described in §b for all 96 15-min contracts.5 Here a selection of 15-min contracts representative
for morning, noon, and evening hours is analysed, that is, H7, H13, H18, Q1–Q4 each. For all
contracts, the merit-order-curve slope ξ is used as threshold variable.

d

versus empirical expected demands (cid:9)(i)

(a) Merit-order-curve slope
We estimate the slope of the merit order curve ξ (i) of 15-min contract i based on intraday
auction prices PAuc,(i) and corresponding expected demands (cid:9)(i). As both PAuc,(i) and (cid:9)(i) are
provided in quarter-hourly resolution, we are able to determine a merit order curve for each
15-min contract i individually. Figure 6 depicts a scatter plot of empirical intraday auction
prices PAuc,(i)
d observed on days d = 1, . . . , T, for contract
i = H13Q4. We ﬁlter out a total of 13 negative auction prices. We observe a positive relationship
between intraday auction prices and expected demands: PAuc,(i)
d increases. For
high levels of demand, more expensive generation technologies are in use which puts upward
pressure on prices. In particular, we may identify two clusters: one cluster encompasses expected
demands (cid:9) < 58 GW, and the other cluster comprises (cid:9) ≥ 58 GW. These clusters reﬂect low and
high electricity demand on weekends and weekdays, respectively. Overall, the data points exhibit
a fairly wide range of variation which stems from the strongly varying expectation of renewable
power infeed.

increases as (cid:9)(i)

For the empirical merit order curve f ((cid:9)), we use the exponential function f ((cid:9)) = ea (cid:9)+b following
[7]. Of course, other choices for f ((cid:9)) are possible, but we want to keep our model as simple as
possible. We ﬁt the exponential function f ((cid:9)) to the empirical intraday auction price PAuc,(i) as a
function of expected demand (cid:9)(i). Technically, we minimize the sum of squared errors between
((cid:9)) implied by the choice of a parameter set Φ = {a, b}, and the
the logarithm of the function f

Φ

d

5The estimation time of the threshold regression amounts to roughly one minute per contract.

Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2019.0624/373490/rsta.2019.0624.pdf
by guest
on 05 April 2026

Table 1. Parameter estimates of a, b of the empirical merit-order-curve function f ((cid:9)) = ea (cid:9)+b for 15-min contracts H7, H13,
H18, Q1–Q4 each.

11

parameter

a

estimate

contract

s.e.

b

estimate

s.e.

0.036

0.029

(0.004)

(0.268)
H7Q1
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
(0.134)
H7Q2
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
(0.125)
H7Q3
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
(0.130)
H7Q4
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
H13Q1
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

(0.002)

(0.002)

(0.002)

(0.002)

(0.141)

0.940

0.045

0.045

0.022

0.961

2.194

1.632

1.412

H13Q2
H13Q3

H13Q4

H18Q1

H18Q2

H18Q3

H18Q4

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

(0.003)
(0.004)

(0.006)

(0.005)

(0.003)

(0.002)

(0.002)

1.214
0.548
−0.856
−0.372
1.246

2.546

3.074

(0.201)
(0.217)

(0.389)

(0.313)

(0.160)

(0.109)

(0.140)

0.037
0.045

0.065

0.061

0.039

0.021

0.013

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

r
o
y
a
l
s
o
c
i
e
t
y
p
u
b

i

l
i
s
h
n
g
.
o
r
g
/
j
o
u
r
n
a
l
/
r
s
t
a

P
h

i
l
.

T
r
a
n
s
.

.
S
o
c
.

A
3
7
9

:

2
0
1
9
0
6
2
4

.

R

logarithm of the empirical intraday auction price PAuc,(i)

d

((cid:9)(i)
d ),

min
Φ

T(cid:2)

d=1

| log(PAuc,(i)
d

((cid:9)(i)

d )) − log( f

Φ

((cid:9)))|2.

(4.1)

The least-squares ﬁt for contract i = H13Q4 is shown in ﬁgure 6. The parameter estimates of a, b
for contracts H7, H13, H18, Q1–Q4 each, are reported in table 1.

We observe an hourly seasonality of the parameter estimates ˆa,

ˆ
b. For contracts H4Q1–H14Q4,
ˆ
the estimates ˆa,
b increase and decrease from the ﬁrst to the last 15-min contract within an
ˆ
hour, respectively, whereas for contracts H15Q1–H2Q4, the estimates ˆa,
b decrease and increase,
respectively. Thus, the curvature of the empirical merit order curve f ((cid:9)) grows from Q1 to Q4 in
each hour during morning and noon hours, whereas it declines from Q1 to Q4 during afternoon
and evening hours. This hourly seasonality may be associated with rising and falling demand
in the ﬁrst and second half of the day, respectively, following human activity [22]. Consequently,
in the ﬁrst half of the day, more expensive power plants are needed to cover demand in the last
than in the ﬁrst quarter-hour in each hour, whereas in the second half of the day, more expensive
power plants are operated in the ﬁrst than in the last quarter-hour per hour.

Eventually, we take the derivative of the ﬁtted merit-order-curve function f

((cid:9))/d(cid:9)
((cid:9)) to obtain empirical merit-order-curve

((cid:9)) = df

(cid:3) Φ

Φ

and substitute empirical expected demands (cid:9)(i)
slopes ξ (i)
d

d ) on days d = 1, . . . , T, for 15-min contract i.

d into f

((cid:9)(i)

= f

(cid:3) Φ

(cid:3) Φ

(b) Model calibration

The estimation results of all 15-min contracts in hour H13 are presented in table 2, while the
estimation results of contracts in hours H7 and H18 may be found in Tables B.1 and B.2 in the
electronic supplementary material, respectively. The threshold test shows strong evidence for a
threshold effect in the slope of the merit order curve ξ for all contracts in hours H13 and H7,

Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2019.0624/373490/rsta.2019.0624.pdf
by guest
on 05 April 2026

12

r
o
y
a
l
s
o
c
i
e
t
y
p
u
b

i

l
i
s
h
n
g
.
o
r
g
/
j
o
u
r
n
a
l
/
r
s
t
a

P
h

i
l
.

T
r
a
n
s
.

.
S
o
c
.

A
3
7
9

:

2
0
1
9
0
6
2
4

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

R

while in hour H18, it suggests a statistically signiﬁcant threshold effect for contracts Q2 and Q3.6
A merit-order-curve slope of ξ = 1 (EUR/MWh)/GW implies that a change of 1 GW in expected
demand causes a change of 1 EUR/MWh in the intraday auction price. Regime 1 corresponds to
a market in which the merit order curve is ﬂat, whereas Regime 2 reﬂects a market in which
the merit order curve is steep. For all contracts, the total sample is split into subsamples of
reasonable size and allows for a sound interpretation of the estimation results. The adjusted R2
ranges between 11% and 22%.

The estimated coefﬁcients of lagged price changes (cid:2)Pt−1, (cid:2)Pt−2, (cid:2)Pt−3 are highly statistically
signiﬁcant and negative in both regimes for all contracts in hours H13 and H7. In hour H18, the
higher-order autoregressive terms show less statistical signiﬁcance. The negative coefﬁcients of
lagged price changes suggest mean reversion in the price formation process of 15-min contracts.
As such, they reﬂect the so-called ‘learning effect’ or ‘participant conduct’ [23,24]. Our results
conﬁrm previous ﬁndings of [2] for morning and evening contracts. For noon contracts, by
contrast, they ﬁnd that autoregressive terms have less explanatory power and intraday trading is
primarily driven by renewable forecast changes. We, however, provide evidence of a signiﬁcant
mean reversion effect for noon contracts in 2015.

t

t

t

t

, . . . , (cid:2)P(i+2)

, . . . , (cid:2)P(i+2)

Overall, in hour H13, the estimated coefﬁcients of price changes of neighboring contracts
are highly statistically signiﬁcant and positive in both regimes for all

(cid:2)P(i−2)
contracts. In hour H7, the estimated coefﬁcients of (cid:2)P(i−2)
are highly statistically
signiﬁcant and positive in the steep merit-order regime for all contracts as well as in the ﬂat regime
for contracts Q3 and Q4. Thus, price changes of neighbouring contracts have strong explanatory
power and a positive effect on one another. Moreover, we observe that price changes of the nearest
neighbours i ± 1 have a stronger impact on price changes of contract i than price changes of next-
nearest neighbours i ± 2.7 In particular, for the ﬁrst 15-min contract Q1 in an hour, price changes
(cid:2)P(i+1)
of the following contract Q2 have the greatest inﬂuence, whereas for the last contract Q4
in that hour, price changes (cid:2)P(i−1)
of the preceding contract Q3 exhibit the largest impact. Hence,
15-min contracts within the same hour are the most important price drivers. In hour H18, the
coefﬁcients of (cid:2)P(i−2)

are rarely statistically signiﬁcant.
The coefﬁcients of the intraday auction price PAuc are not signiﬁcant for all contracts and
regimes. This is not surprising since PAuc can merely be considered as an estimate of the initial
price of a 15-min contract in the continuous trading. Thus, it is not expected that PAuc affects
continuous trading beyond the ﬁrst price.

, . . . , (cid:2)P(i+2)

t

t

t

t

In hour H13, the coefﬁcients of trading volume Vt are signiﬁcant in the ﬂat merit-order regime
for all contracts and in the steep regime for contracts Q1 and Q4. Independent of the regime, they
are negative for Q1 and Q2 and positive for Q3 and Q4. This sign proﬁle reﬂects the joint hourly
seasonality of transaction prices and trading volumes described in §b: as more solar power is
generated than the hourly average in Q1 and Q2, there is sell pressure at the beginning of the
hour and intraday prices decrease. Conversely, buy pressure increases intraday prices at the end
of the hour (Q3 and Q4) when below-average solar power is produced. In hour H7, the coefﬁcients
of Vt are signiﬁcant for all contracts and regimes and we observe the opposite sign pattern: for
contracts Q1 and Q2, the coefﬁcients are positive, whereas for Q3 and Q4, they turn negative
independent of the regime. Thereby, the positive and negative coefﬁcients reﬂect buy and sell
pressure at the beginning and end of the hour, respectively. In hour H18, the coefﬁcients of Vt are
not signiﬁcant. In general, we do not ﬁnd an asymmetric adjustment of intraday price changes
(cid:2)Pt to trading volumes Vt.

Overall, the coefﬁcients of negative wind forecast changes (cid:2)wn

t are signiﬁcant and negative in
the steep merit-order regime for all contracts. The negative sign is economically meaningful as
electricity prices should increase if less wind power is forecasted. In hour H13, the coefﬁcients of

6We indicate the statistical signiﬁcance level of the threshold test by superscript asterisks at the threshold variable in the
regression tables.

7The terms nearest and next-nearest neighbours are motivated from physics where a nearest- and next-nearest-neighbour
interaction exists.

Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2019.0624/373490/rsta.2019.0624.pdf
by guest
on 05 April 2026

Table 2. Estimation results of the extended econometric model (3.1) for intraday price changes (cid:2)Pt of 15-min contracts
H13Q1–4.

13

H13Q1
regime 1
ξ ∗∗ ≤ 0.689
estimate
−1.504
2.610

H13Q2
regime 1
ξ ∗∗∗ ≤ 0.912
estimate
−0.201
0.931

regime 2
ξ ∗∗∗ > 0.912
estimate

s.e.

s.e.

regime 2
ξ ∗∗ > 0.689
s.e.
estimate
(1.643) −0.867
(2.672)
1.021
(0.040) −0.311∗∗∗
(0.030) −0.131∗∗∗
(0.035) −0.088∗∗∗
(0.025)

variable

s.e.

variable

t

(0.911)

(0.025)

const
ξ

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

0.304
(1.225)
(1.622) −0.371
(0.034) −0.322∗∗∗
(0.028) −0.132∗∗∗
(0.032) −0.021
(0.027)

(1.054)
(0.018) (cid:2)Pt−1 −0.332∗∗∗
(0.015) (cid:2)Pt−2 −0.172∗∗∗
(0.015) (cid:2)Pt−3 −0.058∗
(0.010) (cid:2)P(i−2)
(0.012) (cid:2)P(i−1)
(0.016) (cid:2)P(i+1)
(0.011) (cid:2)P(i+2)
(0.006)

(0.734)
const
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
ξ
(0.548)
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
(cid:2)Pt−1 −0.363∗∗∗
(0.023)
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
(cid:2)Pt−2 −0.188∗∗∗
(0.016)
(cid:2)Pt−3 −0.120∗∗∗
(cid:2)P(i−2)
0.064∗∗
t
(cid:2)P(i−1)
0.063∗∗
t
(cid:2)P(i+1)
0.144∗∗∗
t
(cid:2)P(i+2)
0.049∗∗
t
PAuc
0.000
−0.025∗∗∗
Vt
(cid:2)wn
−0.528
t
(cid:2)wp
−0.554
t
(cid:2)sn
0.852
t
(cid:2)sp
−2.842∗∗∗
t
0.098∗∗∗
(cid:2)t

(0.015)
(0.006) −0.017∗∗∗
(0.378) −1.135∗∗∗
(0.421) −0.688∗∗
(0.362) −1.604∗∗∗
(0.513) −1.860∗∗∗
0.058∗∗∗
(0.029)

0.006
(0.021)
(0.010) −0.007
(0.280) −1.179∗∗∗
(0.346) −0.228
(0.344) −1.750∗∗∗
(0.398) −1.485∗∗∗
(0.029)

0.093∗∗∗
0.212∗∗∗
0.109∗∗∗
0.021
−0.011
−0.022∗
−0.564
−0.390
0.181
−2.629∗∗∗
0.029

0.020
0.051∗∗∗
0.136∗∗∗
0.036∗∗∗
0.002

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

0.053∗∗∗
0.168∗∗∗
0.140∗∗∗
0.042

t
PAuc
Vt

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

(0.020)

(0.030)

(0.034)

(0.034)

(0.007)

(0.007)

(0.024)

(0.024)

(0.025)

(0.202)

(0.188)

(0.016)

(0.016)

(0.376)

(0.014)

(0.021)

(0.374)

0.027

t

t

t

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

(0.003)
(0.208) (cid:2)wn
t
(0.247) (cid:2)wp
t
(0.417) (cid:2)sn
t
(0.403) (cid:2)sp
(0.016) (cid:2)t
#Obs
R2
adj

#Obs
R2
adj

3131

9922

0.201

H13Q3

0.190

2759

9284

0.188

H13Q4

0.198

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

r
o
y
a
l
s
o
c
i
e
t
y
p
u
b

i

l
i
s
h
n
g
.
o
r
g
/
j
o
u
r
n
a
l
/
r
s
t
a

P
h

i
l
.

T
r
a
n
s
.

.
S
o
c
.

A
3
7
9

:

2
0
1
9
0
6
2
4

.

R

s.e.
(0.986)

variable
const
ξ

regime 1
ξ ∗∗ ≤ 1.324
estimate
−0.687
1.016

regime 1
ξ ∗∗∗ ≤ 0.995
estimate
−0.396
−0.111

regime 2
ξ ∗∗ > 1.324
s.e.
estimate
(0.390) −1.215
(0.497)
0.707
(0.024) −0.306∗∗∗
(0.024) −0.165∗∗∗
(0.018) −0.080∗∗∗
(0.017)

variable
s.e.
(0.377)
const
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
ξ
(0.204)
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
(cid:2)Pt−1 −0.287∗∗∗
(0.019)
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
(cid:2)Pt−2 −0.143∗∗∗
(0.014)
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
(cid:2)Pt−3 −0.058∗
(cid:2)P(i−2)
0.061∗∗∗
t
(cid:2)P(i−1)
0.059∗∗∗
t
(cid:2)P(i+1)
0.147∗∗∗
t
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
(cid:2)P(i+2)
0.075∗∗
(0.014)
t
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
PAuc
(0.006)
Vt

(0.649)
(0.023) (cid:2)Pt−1 −0.331∗∗∗
(0.021) (cid:2)Pt−2 −0.176∗∗∗
(0.017) (cid:2)Pt−3 −0.095∗∗∗
(0.017) (cid:2)P(i−2)
(0.031) (cid:2)P(i−1)
(0.029) (cid:2)P(i+1)
(0.014) (cid:2)P(i+2)
(0.008)

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
(0.022)
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

0.044
0.147∗∗∗
0.230∗∗∗
(0.019)
0.044
(0.017) −0.004
0.014
(0.006)

regime 2
ξ ∗∗∗ > 0.995
s.e.
estimate
(0.541) −0.183
(0.800) −0.196
(0.027) −0.298∗∗∗
(0.025) −0.135∗∗∗
(0.023) −0.071∗∗∗
0.043∗∗∗
(0.018)
0.168∗∗∗
0.062∗∗∗
0.061∗∗∗
0.010∗
0.013∗∗∗

0.038
0.114∗∗∗
0.069∗∗∗
0.045∗∗
0.011
0.012∗

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

−0.016
0.012∗

t
PAuc
Vt

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

(0.004)

(0.005)

(0.016)

(0.018)

(0.014)

(0.021)

(0.021)

(0.021)

(0.013)

(0.013)

(0.013)

t

t

t

(0.003)
(Continued.)

Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2019.0624/373490/rsta.2019.0624.pdf
by guest
on 05 April 2026

Table 2. (Continued.)

14

r
o
y
a
l
s
o
c
i
e
t
y
p
u
b

i

l
i
s
h
n
g
.
o
r
g
/
j
o
u
r
n
a
l
/
r
s
t
a

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

P
h

i
l
.

T
r
a
n
s
.

.

R

.

.

.

.

.

.
S
o
c
.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

A
3
7
9

:

2
0
1
9
0
6
2
4

H13Q3
regime 1
ξ ∗∗ ≤ 1.324
estimate
−1.029
−0.094
0.133
−1.967∗∗∗
−0.011
5626

regime 2
ξ ∗∗ > 1.324
estimate

regime 2
ξ ∗∗∗ > 0.995
estimate

variable

variable
(cid:2)wn
t
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
(cid:2)wp
(0.222)
t
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
(cid:2)sn
(0.406)
t
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
(cid:2)sp
(0.496)
t
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
(cid:2)t
(0.019)

s.e.
(0.396) −1.188∗∗∗
(0.329) −0.407
(0.377) −2.403∗∗∗
(0.481) −0.259
(0.028) −0.031

s.e.
(0.333) −0.753∗∗∗
(0.184) −0.594∗∗
(0.355) −2.276∗∗∗
(0.319) −0.943
0.027
(0.021)

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

(0.231)

s.e.

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#Obs
R2
0.129
adj
∗p < 0.1; ∗∗p < 0.05; ∗∗∗p < 0.01.

7190

0.214

11261

0.182

s.e.
(0.205) (cid:2)wn
t
(0.261) (cid:2)wp
t
(0.437) (cid:2)sn
t
(0.474) (cid:2)sp
(0.021) (cid:2)t
#Obs
R2
adj

t

H13Q4
regime 1
ξ ∗∗∗ ≤ 0.995
estimate
−1.473∗∗∗
−0.366
−0.211
−1.232
−0.068∗
3893

0.144

p
positive wind forecast changes (cid:2)w
t are only signiﬁcant and negative in the steep regime for Q1
p
and Q3. In hour H7, the coefﬁcients of (cid:2)w
t are signiﬁcant and negative in the ﬂat regime for all
contracts as well as in the steep regime for Q1 and Q2, while in hour H18, they are signiﬁcant and
negative in both regimes for Q3. The negative coefﬁcients imply that electricity prices decline in
the wake of rising wind power infeed, which is consistent with our intuition. No asymmetry in the
coefﬁcients of wind forecast changes between the regimes is observed. We conclude that generally
forecast errors of wind power generation contribute to pricing intraday electricity contracts.

The coefﬁcients of negative solar forecast changes (cid:2)sn

t are signiﬁcant and negative in the steep
merit-order regime, but not signiﬁcant in the ﬂat regime for contracts in hours H13 and H7. In
hour H18, the coefﬁcients of (cid:2)sn
t are signiﬁcant in both regimes for Q3. In the steep regimes,
the coefﬁcients of (cid:2)sn
t are at least two times larger by absolute value than in the ﬂat regimes.
This reﬂects the fact that renewable forecast changes affect electricity prices more severely in the
steep than in the ﬂat merit-order regime. In hour H13, the coefﬁcients of positive solar forecast
p
changes (cid:2)s
t are signiﬁcant and negative in both regimes for contracts Q1 and Q2. In hour H7, the
p
coefﬁcients of (cid:2)s
t are signiﬁcant and negative in both regimes for Q4, while in hour H18, they are
generally not signiﬁcant. The negative coefﬁcients of both negative and positive forecast errors of
solar power production are reasonable: a lower expectation of solar power infeed should increase
electricity prices, whereas a larger prediction of solar power decreases electricity prices.

Generally, renewable forecast changes are more signiﬁcant in the steep than in the ﬂat merit-
order regime. When the market is in the steep merit-order regime, market participants rely on the
use of more expensive power generation technologies, which puts additional pressure on them to
balance the volatile renewable energies on the intraday market.

Eventually,

intraday trading of 15-min contracts is driven by both price-related and
fundamental variables at noon, while the price-related variables have a slight surplus importance.
For morning and evening contracts, however,
intraday price changes are predominantly
inﬂuenced by past, idiosyncratic price information and the price information of neighbouring
contracts.

5. Conclusion

impacts for intraday
This paper develops an econometric price model with fundamental
electricity markets of 15-min contracts. We analyse a novel and unique dataset of high-frequency
transaction data, fundamental supply and demand data, and intradaily updated forecasts of wind

Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2019.0624/373490/rsta.2019.0624.pdf
by guest
on 05 April 2026

and solar power generation. The nature of our dataset allows the model speciﬁcation to solely
include ex-ante market information.

15

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

r
o
y
a
l
s
o
c
i
e
t
y
p
u
b

i

l
i
s
h
n
g
.
o
r
g
/
j
o
u
r
n
a
l
/
r
s
t
a

P
h

i
l
.

T
r
a
n
s
.

.
S
o
c
.

A
3
7
9

:

2
0
1
9
0
6
2
4

.

R

We perform an empirical exploration of transaction prices and trading volumes of 15-min
contracts. Empirical evidence suggests that, on average, transaction prices of 15-min contracts
exhibit a sawtooth-shaped and trading volumes a U-shaped hourly seasonality. Moreover,
liquidity increases sharply within the last trading hour before gate closure. Our empirical analysis
also indicates that renewable forecast updates are reﬂected in intraday prices within one trading
minute.

We reﬁne the econometric model by [2] along three dimensions by incorporating: (i) the slope
of the merit order curve, (ii) price changes of neighbouring 15-min contracts, (iii) the 15-min
intraday auction price. We calibrate our econometric model to market data for a selection of
morning, noon, and evening contracts. A threshold regression model is used to examine how
15-min intraday trading depends on the slope of the merit order curve.

Our estimation results reveal that autoregressive price changes up to the third order are
highly statistically signiﬁcant and negative, independent of the time of day. This behaviour
provides clear evidence of mean reversion in the price formation mechanism of 15-min contracts.
Additionally, price changes of neighbouring contracts exhibit strong explanatory power and a
positive impact on price changes of a given 15-min contract. We observe an asymmetric effect
of positive and negative renewable forecast changes on intraday prices depending on the merit-
order-curve slope: Renewable forecasts affect electricity prices more severely in the steep than
in the ﬂat merit-order regime. In general, renewable forecast changes have a higher explanatory
power for pricing noon than morning and evening contracts, but price information is the key
driver of 15-min intraday trading. Overall, we conclude that the importance of inﬂuencing factors
on the intraday electricity market has changed from fundamental towards trade-related factors.

As our econometric model exclusively involves ex-ante market knowledge, it allows to develop
trading strategies for intraday electricity markets, tailor-made for each contract. Furthermore,
it helps to design forecasting models for single intraday transaction prices in the continuous
trading—to our knowledge, an unexplored territory of scientiﬁc research hitherto. Moreover, our
article provides a valuable step towards the optimization of the bidding behaviour on intraday
markets. Eventually, our insights should prove useful to energy companies within the process of
automating intraday electricity trading.

Data accessibility. The intraday transaction data [10,13] and renewable power forecast data [15] are obtained via
a (Uni-)Vendor contract and cannot be made publicly available due to contractual conditions. The 15-min
intraday auction data may be obtained via [14]. The load data may be downloaded from [16]. Code is publicly
available at [21].
Authors’ contributions. M.K., R.K. and F.P. conceived of and designed the study; M.K., R.K. acquired the data;
M.K. and F.P. prepared the data; M.K. analysed the data, performed the statistical analysis and drafted
the manuscript; M.K., R.K. and F.P. critically revised the manuscript. All authors read and approved the
manuscript and agree to be held accountable for the work performed therein.
Competing interests. We declare we have no competing interests.
Funding. F.P. thanks the funding from Adolf Øiens Donasjonsfond Energizing New Computational Frontiers
(grant no. L10079) and the Isaac Newton Institute for Mathematical Sciences for its hospitality during the
programme ‘The mathematics of energy systems’ which was supported by the Engineering and Physical
Sciences Research Council (EPSRC) (grant no. EP/R014604/1). This work has been performed within
the +CityxChange (Positive City ExChange, https://cityxchange.eu/) project under the Smart Cities and
Communities topic which was supported by the European Union’s Horizon 2020 Research and Innovation
programme (grant no. 824260). F.P.’s research was ﬁnancially supported by Innosuisse as part of the activities
within SCCER CREST.

References
1. European Energy Exchange AG. EEX Annual Report 2015; 2016. (Accessed on 1 March 2019).
https://www.eex.com/ﬁleadmin/EEX/Downloads/Newsroom/Publications/Annual_
Reports/eex-gb-2015-en-data.pdf.

Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2019.0624/373490/rsta.2019.0624.pdf
by guest
on 05 April 2026

2. Kiesel R, Paraschiv F. 2017 Econometric analysis of 15-minute intraday electricity prices.

Energy Econ. 64, 77–90. (doi:10.1016/j.eneco.2017.03.002)

16

r
o
y
a
l
s
o
c
i
e
t
y
p
u
b

i

l
i
s
h
n
g
.
o
r
g
/
j
o
u
r
n
a
l
/
r
s
t
a

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

P
h

i
l
.

T
r
a
n
s
.

.

R

.

.

.

.

.

.
S
o
c
.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

A
3
7
9

:

2
0
1
9
0
6
2
4

3. Pape C, Hagemann S, Weber C. 2016 Are fundamentals enough? Explaining price
variations in the German day-ahead and intraday power market. Energy Econ. 54, 376–387.
(doi:10.1016/j.eneco.2015.12.013)

4. Kallabis T, Pape C, Weber C. 2016 The plunge in German electricity futures prices–
280–290.

fundamental model. Energy Policy

95,

analysis using a parsimonious
(doi:10.1016/j.enpol.2016.04.025)

5. Beran P, Pape C, Weber C. 2019 Modelling German electricity wholesale spot prices with
a parsimonious fundamental model–validation & application. Utilities Policy 58, 27–39.
(doi:10.1016/j.jup.2019.01.008)

6. Burger M, Klar B, Müller A, Schindlmayr G. 2004 A spot market model for pricing derivatives

in electricity markets. Quant. Finance 4, 109–122. (doi:10.1088/1469-7688/4/1/010)

7. He Y, Hildmann M, Herzog F, Andersson G. 2013 Modeling the merit order curve of the
European energy exchange power market in Germany. IEEE Trans. Power Syst. 28, 3155–3164.
(doi:10.1109/TPWRS.2013.2242497)

8. Märkle-Huß J, Feuerriegel S, Neumann D. 2018 Contract durations in the electricity market:
causal impact of 15 min trading on the EPEX SPOT market. Energy Econ. 69, 367–378.
(doi:10.1016/j.eneco.2017.11.019)

9. Kath C, Ziel F. 2018 The value of forecasts: quantifying the economic gains of accurate quarter-
hourly electricity price forecasts. Energy Econ. 76, 411–423. (doi:10.1016/j.eneco.2018.10.005)
10. European Energy Exchange AG. EPEX SPOT DE/AT 15-minute continuous intraday market

transaction data; 2016. https://www.eex.com.

11. EPEX SPOT SE. Press release: EPEX SPOT and ECC successfully reduce lead time
(Accessed on Jan 16, 2020). https://www.epexspot.

on all
com/sites/default/ﬁles/download_center_ﬁles/2015-07-16_EPEX%20SPOT_Lead%20time
%20reduction.pdf.

intraday markets; 2015.

12. EPEX SPOT SE. Press release: Exchange Council approves the introduction of 15-minute
contracts on the Belgian and Dutch market – Trading until delivery to be launched on the
German market on 14 June 2017; 2017. (Accessed on Jan 16, 2020). https://www.epexspot.
com/sites/default/ﬁles/download_center_ﬁles/170612_EPEX%20SPOT_Exchange%20
Council.pdf.

13. European Energy Exchange AG. EPEX SPOT DE 15-minute intraday auction market data;

2016. https://www.eex.com.

14. Wagner T. 2018 emarketcrawlR: Crawling energy market data at EPEX SPOT (intraday
trading, intraday auction, day-ahead auction). R package version 0.1.0. https://github.com/
wagnertimo/emarketcrawlR.

15. EWE TRADING GmbH. Intradaily updated forecast data of wind and solar power generation;

2016. https://www.ewe.com.

16. European Network of Transmission System Operators for Electricity Transparency Platform.

Day-ahead total load forecast data; 2016. https://transparency.entsoe.eu.

17. Kremer M, Kiesel R, Paraschiv F. 2020 Intraday electricity pricing of night contracts. Energies

13, 4501. (doi:10.3390/en13174501)

18. Glas S, Kiesel R, Kolkmann S, Kremer M, von Luckner NG, Ostmeier L, Urban K, Weber
C. 2020 Intraday renewable electricity trading: Advanced modeling and numerical optimal
control. J. Math. Industry 10, 1–17. (doi:10.1186/s13362-020-0071-x)

19. Graf von Luckner N, Kiesel R. 2020 Modeling Market Order Arrivals on the Intraday Market
for Electricity Deliveries in Germany with the Hawkes Process. (Accessed on 31 January 2020).
https://ssrn.com/abstract=3526795.

20. Hansen BE. 2000 Sample splitting and threshold estimation. Econometrica 68, 575–603.

(doi:10.1111/1468-0262.00124)

21. Kremer M. 2020 thrreg: Threshold Regression Model. R package version 0.1.0. https://github.

com/mlkremer/thrreg.

22. Paraschiv F. 2013 Price dynamics in electricity markets. In Handbook of Risk Management
in Energy Production and Trading (eds R Kovacevic, GC Pﬂug, MT Vespucci) vol. 199 of
International Series in Operations Research & Management Science, pp. 47–69. Boston, MA:
Springer.

Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2019.0624/373490/rsta.2019.0624.pdf
by guest
on 05 April 2026

23. Karakatsani NV, Bunn DW. 2010 Fundamental and behavioural drivers of electricity price

volatility. Stud. Nonlinear Dyn. Econ. 14, 1–40.

17

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

r
o
y
a
l
s
o
c
i
e
t
y
p
u
b

i

l
i
s
h
n
g
.
o
r
g
/
j
o
u
r
n
a
l
/
r
s
t
a

P
h

i
l
.

T
r
a
n
s
.

.
S
o
c
.

A
3
7
9

:

2
0
1
9
0
6
2
4

.

R

24. Frauendorfer K, Paraschiv F, Schürle M. 2018 Cross-border effects on Swiss electricity prices

in the light of the energy transition. Energies 11, 2188. (doi:10.3390/en11092188)

Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2019.0624/373490/rsta.2019.0624.pdf
by guest
on 05 April 2026

