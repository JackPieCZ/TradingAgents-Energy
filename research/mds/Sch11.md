|       |      |       |     | Munich |     | Personal |      | RePEc    | Archive |
| ----- | ---- | ----- | --- | ------ | --- | -------- | ---- | -------- | ------- |
| Power | Spot | Price |     | Models |     |          | with | negative |         |
Prices
| Schneider,  | Stefan                                 | and    | Schneider, |     | Stefan |      |       |     |     |
| ----------- | -------------------------------------- | ------ | ---------- | --- | ------ | ---- | ----- | --- | --- |
| E.ON Energy | Trading                                |        | SE         |     |        |      |       |     |     |
| December    | 2010                                   |        |            |     |        |      |       |     |     |
| Online at   | https://mpra.ub.uni-muenchen.de/29958/ |        |            |     |        |      |       |     |     |
| MPRA Paper  | No.                                    | 29958, | posted     |     | 27 Apr | 2011 | 09:42 | UTC |     |

Power spot price models with negative prices1
December 2010
Dr. Stefan Schneider
E.ON Energy Trading SE
Holzstraße 6
40221 Düsseldorf
Germany
Stefan.Schneider@eon.com
Abstract
Negative prices for electricity are a novelty in European power markets. At the German EEX spot
market negative hourly prices have since occurred frequently, down to values as extreme as minus
several hundred €/MWh. However, in some non-European markets as USA, Australia and Canada,
negative prices are a characteristic for a longer period already. Negative prices are in fact natural for
electricity spot trading: plant flexibility is limited and costly, thus, incurring a negative price for an
hour can nevertheless be economically optimal overall. Negative prices pose a basic problem to
stochastic price modelling: going from prices to log-prices is not possible. So far, this has been dealt
with by “workarounds”. However, here a thorough approach is advocated, based on the area
hyperbolic sine transformation. The transformation is applied to spot modelling of the German EEX,
the ERCOT West Texas market and the exemplary valuation of an option. It is concluded that the area
hyperbolic sine transform is well and naturally suited as a starting point for modelling negative power
prices. It can be integrated in common stochastic price models without adding much complexity.
Moreover, this transformation might be in general more appropriate for power prices than the log
transformation, considering fundamentals of power price formation. Eventually, a thorough
treatment of negative prices is indispensable since they significantly affect business.
Inhalt
Power spot price models with negative prices ....................................................................................... 1
Abstract ............................................................................................................................................... 1
Introduction ............................................................................................................................................. 2
Negative power prices ............................................................................................................................. 3
Modelling concept ................................................................................................................................... 4
1 This article is based on a talk delivered at the 2nd International Ruhr Energy Conference 2010 (INREC 2010).
The article has been submitted to “The Journal of Energy Markets” and is currently subject to review.

The area hyperbolic sine transformation ............................................................................................ 4
Basic stochastic differential equation and price distribution .............................................................. 5
Spot price modelling ................................................................................................................................ 6
Case EEX .............................................................................................................................................. 7
Scaling of hourly profiles ................................................................................................................. 7
Simulation results ............................................................................................................................ 9
Case ERCOT West ................................................................................................................................ 9
Extended area hyperbolic sine transformation ............................................................................... 9
Estimation and simulation results ................................................................................................. 10
An application example: a simple option on the spot price .................................................................. 11
Concluding remarks ............................................................................................................................... 13
References ............................................................................................................................................. 14
Figures and tables.................................................................................................................................. 15
Introduction
The German power exchange EEX permitted negative price outcomes for the spot auction in
autumn 2008. Since then, negative prices have occurred frequently, down to values as low
as -500 €/MWh, see Fig. 1. This has triggered considerable attention and debates, not only in
the energy trading business but even in the media. Paying money instead of demanding
when selling a commodity to a counterparty appears counterintuitive. However, this is a
natural consequence of the properties of the commodity power. Generally, this is because
generation of power is of limited flexibility due to technical and regulatory constraints.
When it is not possible for a generation facility to follow a demand slump closely, its
generation is sold off with discount, even down to negative prices.
For the modeller negative prices pose a basic problem: the usual initial transition from prices
to log prices is not possible. Surprisingly, (to the author’s best knowledge) no solution
dealing realistically with this issue has been proposed so far. Instead, the existing
approaches are workarounds. The simplest being just the exclusion of all negative
occurrences from analysis, or, introducing a shifted price with zero level at the observed
minimum price (eg, -500 €/MWh), see Sewalt and De Jong (2003) and Knittel and Roberts
(2001). The justifications given are that the workaround solution is supposed to be sufficient
or that negative prices do not really have an influence because they are relatively rare.
However, energy traders and business practitioners do not feel comfortable with this, see
Sprenger and Laege (2009). Quite the contrary, they notice a significant impact of negative

prices on the value of their position, eg, when holding a structured Off-Peak position2.
Looking again at the EEX price history of 2009 (Fig. 1), it indeed appears justified to consider
negative or downward jumps as having replaced the upwards spikes in the times before
economic downturn.
In this article a simple but effective way to deal realistically with negative (as well as positive)
spot prices is developed. Namely, replacing the log transformation by the area hyperbolic
sine transformation. An appealing feature of this approach is that it complicates stochastic
price modelling not seriously. Basic cases can still be expressed by closed-form expressions.
Moreover, indications are found that the log transformation is in general not well suited for
power prices, but the area hyperbolic sine transformation is, independently of the
occurrence of negative prices.
Negative power prices
In this section, a brief account of the economical and technical background of negative
power spot prices is given. For detailed overviews on this subjects see, eg, Dettmer and
Jacob (2009).
The German EEX spot exchange was the first market in Europe permitting negative prices.
The Scandinavian Nordpool spot followed in the end of 2009. However, outside Europe,
power markets permitting negative price are an established institution. The possibility of
negative prices was built in their design from the beginning on. Two striking examples are
ERCOT West Texas and AEMO, region South Australia. They exhibit very frequent, often
strongly negative prices.
Negative prices at EEX occur when very low demand coincides with high supply. Low
demand situations are constituted, eg, by public holidays and Sunday nights, amplified by
slumps in industrial activity due to the economic crisis. A typical high supply situation is
constituted by high wind power infeed. The grid operator, who has to take the wind
production with priority, then bids this power at EEX for a negative price to achieve market
clearing. Also, production from conventional power plants can be bid into the market for a
negative price. This is, eg, when the plant produces above the marginal generation costs for
matching the total demand in some hour. It can then nevertheless be economically optimal
to leave the plant online for that hour when the loss from the negative price is smaller than
the costs from a modified production schedule. An alternative production schedule would
have to take into account a number of factors incurring costs, eg, ramping costs, start-up
costs, costs for procuring energy from alternative sources during a mandatory downtime of
the plant. Another negative price situation is constituted by grid transmission bottlenecks,
eg, high wind production in Denmark cannot be sufficiently transported to hydro pump
storages in northern Scandinavia.
Summarizing, negative prices occur because production of power has limited flexibility for
economical, technical and regulatory reasons. When it is not possible for a power generation
facility to follow a demand slump closely, its generation is sold off with discount. This is why
it was consequential to allow for negative prices at EEX3. It was shown that this is
2 A profile with hourly varying loads in the low demand periods.
3 Before, spot auctions at EEX frequently attained no intersection of bid and offer curves, necessitating partial
market clearing only.

economically rational in order to optimize market clearing, see Viehmann and Sämisch
(2009).
It remains to be seen if other markets follow the model of EEX and Nordpool. Especially,
when considering that European power markets are getting more and more integrated.
Interestingly, for another commodity, natural gas (delivered to NBP), there were some
negative prices in the past. The situation was analogous to power: a production facility (a gas
field) provided excess production in a low demand period which could not be sufficiently
adapted for technical reasons.
Modelling concept
The area hyperbolic sine transformation
Stochastic modelling of power prices usually starts with log transforming x ln pof the
original prices p. Instead, I propose to replace the log transformation by the area hyperbolic
sine transformation:
 p
xsinh1  (1)
  
, where is an offset anda scale parameter. The behaviour of this function compared to
the natural logarithm is depicted in Fig. 2. The most important property is the asymptotic log
behaviour
 
sinh1p ln p p2 1 sign(p)ln  2| p| 
for | p|4. The log function is a good approximation for small | p|2already. The
positive and negative log-like parts are connected by an approximately linear part at| p|0.
The transformation appears to be a natural choice because it preserves the log behaviour
which is a proven method. However, it is now presupposed that the properties of prices
p 0are a “mirror image” of p 0. We recall a basic rationale for the log transformation:
the volatility/variability of prices increases with the absolute price level: dp ~ p. This is why
dp
returns (t)or log returns ln p(t)ln p(t1)are studied. It appears to be plausible that
p
this is also the case for negative power prices: |dp|~| p|for p 0. This can be substantiated
by studying bid / ask curves of EEX spot auctions, see Fig. 3. As it is well known the curves
are getting steeper when going to high prices and thus the spot price gets more variable/
spiky when the auction outcome (intersection of curves) moves into that price region. We
see that the same holds for the negative price region. Note: this finding already rules out the
„shift zero price level down to a negative lowest level” approach to the problem.
4 The offset and scale parameter are temporarily omitted. The discussed properties do not qualitatively depend
on these, of course.

Basic stochastic differential equation and price distribution
As a start, it is necessary to understand basic stochastic and statistical features of modelling
built on the area hyperbolic sine function5:

sinh1p
x

To this end, the same standard route as for the log transformation can be taken: analysing a
basic model for the spot price process, the Ornstein-Uhlenbeck (OU) process:

|     | dxk(mx)dt | dW |     (2)  |     |
| --- | ------------ | ----- | -------- | --- |

, with kand mthe mean reversion rate and level, W the standard Wiener process and
volatility .
By means of the Ito formula and standard relations for hyperbolic functions we get the
stochastic differential equation

|             |     |           |         |        |
| ------------ | --- | --------- | -------- | ------ |
| dp           |     |           | p        |        |
| k(msinh1 |     | p)0.52 |          |        |
|             |     |           | dtdW |   (3)  |
| 1 p2       |     |           | 1 p2   |        |
|             |     |           |         |        |

This is relatively similar to the SDE for the log case

dp
|     |          |           |         |     |
| --- | --------- | --------- | -------- | --- |
|     |  k(mln | p)0.52 | dtdW  |     |
p

Both SDE generate the same dynamics for large  p. Additionally, (3) exhibits a linear form
dp  L(p)dtdW for small | p|. There is an explicit probability distribution solution to
(3). The stationary distribution to the OU process for x:
2
N(m,2
|     | x ~ N(m, | )  | )   |     |
| --- | -------- | --- | --- | --- |
|     |          | 2k  | OU  |     |
reads

 2
|        | 1     |    | sinh1 pm  |     |
| ------ | ----- | --- | ------------ | --- |
|        |       |   |     (4)     |     |
| f(p)  |       | exp |              |     |
|        |       |    | 22         |     |
|       | 2 1 | p2  |              |     |
|        |       |    |             |     |
|        | OU    |     | OU           |     |

for  p. f is known as the Johnson SU distribution (Johnson et al 1994). Summarizing, it has to
be pointed out that switching from the log to the hyperbolic sine transformation has not
qualitatively complicated the analysis. We still get a closed-form solution, the Johnson
distribution replacing the log-normal distribution.

5 Stochastic processes involving the hypebolic sine have been employed before to model volatility smiles.
However, prices in that context are strictly positive and described by ordinary returns, see Brigo et al (2003)
and Carr et al (1999).

Fig. 4 depicts typical examples of the Johnson distribution for different means and variances,
overlaid with log-normal distributions with the same mean and variance with respect
to p(not feasible for negative means). Additionally, empirical histograms of EEX spot prices
are displayed. For large (positive) mean and large variance, both the Johnson and log-normal
distribution cannot be distinguished, as expected. Empirically, this case corresponds to the
histogram of typical high price hour types (working day, early evening). A right-skewed,
upward spiking (fat tail) behaviour is observed. Going to typical lowest price hour types
(Sundays and holidays, deep night), the opposite is observed: left-skewed and downward
spiking. This is (qualitatively) matched by a specification of the Johnson distribution, but of
course not by a log-normal type distribution.
Spot price modelling
It now needs to be analysed how the hyperbolic sine transformation integrates with state-
of-the-art spot price models and if the simulation results are satisfactorily able to reproduce
the spot price histories with negative prices.
As the state-of-the-art spot price model the “independent spike model” is taken, see De Jong
(2006) and De Jong and Schneider (2009). The model produces daily spot prices by means of
a three-regime switching process, regimes for normal prices and upward and downward
spikes. This is the model formulated as a discrete time process:

| Mean-reverting regime M: dxM |     | ( | xM | ) |     |
| ---------------------------- | --- | ---- | --- | ----- | --- |
|                              |     | t    |     | t1   | t   |

|     |     | n 1 |     |     |     |
| --- | --- | ---- | --- | --- | --- |
t
| Spike regimes: xS |   | Z   |     |     |     |
| ----------------- | ---- | ---- | --- | --- | --- |
|                   | t    | t,i  |     |     |     |
i1
| High spike regime: | Z   | N(H,H), | n   | POI(H), | H 0  |
| ------------------ | --- | --------- | --- | -------- | ------ |
|                    | ~   |           |     | ~        |        |
|                    | t,i |           | t   |          |        |

| Low spike regime: | Z N(L,L), |     | n   | POI(L), | L 0  |
| ----------------- | ----------- | --- | --- | -------- | ------ |
|                   | ~           |     |     | ~        |        |
|                   | t,i         |     | t   |          |        |

|     |     | 1MH | ML | MH | ML |
| --- | --- | ------ | ---- | --- | --- |

 
| Markov transition matrix:  |     |    | HM | 1HM | 0   |
| --------------------------- | --- | --- | --- | ----- | --- |
 
|     |     |    |     |     | 1LM |
| --- | --- | --- | --- | --- | ------ |
|     |     |     | LM |     | 0      |
 

The normal price process is an OU process with mean-reversion level and rate and. The
(log) prices in the spike regimes are directly drawn from fat-tailed distributions (Poisson
compounded Gaussians). For further explanations, especially on the parameter estimation
method, see the articles.
Besides applying the area hyperbolic sine transformation it is necessary to remove the
deterministic component from the (daily) prices:

|     |     |     |        | sinh1p |    |
| --- | --- | --- | ------ | --------- | --- |
|     |     |     | s x  | x'        |     |
|     |     |     | t t    | t         | t   |

The day type specific components are captured by dummy variables1 (t), D={Mon, .., Fri,
D
Sat/Bridge days, Sun/holidays} being the day type set. Seasons and trends are captured by a
moving average MA(t) x'(t')G(tt'), G(tt')being a Gaussian convolution kernel with
standard deviation of 20 days. This choice of the standard deviation is appropriate to
capture winter-summer effects as well slowly moving fundamentals. Additionally, for the
moving average calculation spikes from the price series are removed beforehand, applying a

standard 3 standard deviation iterative method. This is because the MA(t)is meant to refer
to the mean-reverting level of the normal price process. The coefficients of the components
bMA(t), d 1 (t) are finally estimated by linear regression.
i D
Case EEX
As a first case study, the EEX hourly price history from Oct 2008 – the point in time from
which on negative prices have been possible – till Jan 2010 are modelled. The modelling
consists of two stages. First, the independent spike model is employed to produce scenarios
of daily prices. Secondly, the daily prices are endowed with hourly profiles by means of a
historical price sampling and re-scaling method. Fig. 5 shows the historical daily as well as
hourly prices of the period. The two day which visibly stick out from the daily price series
have been removed (Oct and Dec 2009). These days, the only ones so far at EEX with a
negative price of the full day, are exceptionally strong downward spikes. It does not yet
appear to be meaningful to define an own regime or distributions for this kind of extreme
event at this point in time, based on two examples only so far. Nevertheless, there are still
many days in the truncated history with quite negative hourly prices.
The parameter estimation is accomplished as described above and the determined
parameters are shown in Tab. 1 . Up spiking is marginal, but down spiking is pronounced (see
the values of the normal-to-spike regime jumping probability MX and the Poisson
parameters). This is, of course, plausible, since as stated above, downward jumps have
replaced the upwards spikes in the times before economic downturn.
Scaling of hourly profiles
A simulated daily price is converted into 24 hourly prices by drawing an appropriately similar
day from history and matching it to the day’s price by a scaling transformation. Beforehand,
the EEX historical days are tagged by month, day type D and spike regime. The historical
spike regime characterisation is provided by the parameter estimation algorithm. It outputs
a triple of probabilities6 for each day, indicating this day’s price being in one of the regimes.
For simulated day with price psim the spike regime is definite and, so, among all historical
t
days with matching month and day type a historical regime probability weighted random
choice is carried out. The historical hourly profileShist then is transformed to Ssimsuch that
h t,h
average price equals the day’s price,Ssim  psim. In the past, with positive prices only, there
t,h t
psim
was a simple way to transform: multiplying each hour by a factorC  t 7. Thereby, in
Shist
h
terms of hourly price differences, Offpeak hour prices are shifted a bit, Peak hours prices
strongly, which is realistic. However, when some hours ofShist are negative, the
h
transformation yields an implausible result. Imagine the case of a “stronger market” in
simulation than in history, psim  phist. The factor transformation, the Cbeing >1, would
t t
6
The estimator’s output are likelihoods which are converted into probabilities
7 A similar sampling re-scaling method has been employed in Culot et al (2006) for power spot market modeling
(no negative power prices in Europe at that time).

shift positive hour upwards which is correct. However, negative hours would take on even
more negative prices which is of course the opposite of what is observed on a real market.
The search for a plausible new transformation has been guided by the following
considerations. The factor transformation preserves log normal distributions, which is the
basic price distribution for the positive prices only world, assuming a log transformation on
the prices and a basic OU model for the price process. So, if all hours of a historical day are
distributed log-normally, lnShist N(mhist,hist), scaling with the factor C yields new log
~
|     |     |     |     | h   | h   | h   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
normal distributions lnSsim ~ N(mhist lnC,hist) with equally shifted means. This principle
|     |     |     |     | h   | h   | h   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is transferred to the hyperbolic sine transformation and Johnson distribution world. We
again consider a sample day. Find a such that

sinh1 Shist ~ N(mhist,hist)  sinh1 Ssim sinh1 Shist ~ N(mhist ,hist)
|     |     | h   |     | h h |     | h   |     |     | h   | h   | h   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| and Ssim |    | psim. With sinh1 |     |  we get  |     |     |     |     |     |     |     |     |
| -------- | --- | ------------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
|          | t,h | t                  |     |            |     |     |     |     |     |     |     |     |

|     |     |     |    |     |    |     |    |    |     |    |    |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Ssim sinh sinh1sinh1 Shist cosh sinh1 Shist Shist cosh sinh1
|     | h   |     |     |     | h   |     |     | h   | h   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

by means of an addition theorem. In contrast to the log normal case the sine hyperbolic case
cannot explicitly be solved for . Instead, we simplify by noticing |sinhx||coshx|, an
approximation which is very good already for small | x|, eg,| x|2. Thus, we can
approximate:

|     |     |     |     |     |     |          |     |            |        |         |     |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | ---------- | ------- | -------- | --- | --- |
|     |     |     |     |     |     | Shist |     | Shistcosh | sinh1 | forShist |     | 0  |
|     |     |     |     |     |     |         | h   | h          |         |          | h   |     |
|     |     |    |     |    |    |        |     |            |        |         |     |     |
Ssim sinh1Shist sinh1 (Shist)Shistcosh sinh1 forShist
|     |  cosh |     |     | S cosh |     |    |     |     |     |     |     | 0  |
| --- | -------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| h   |          |     |     | h h     |     |     |     | h h |     |     |     | h   |

|     |     |     |     |     |     | 0  | forShist | 0  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |    |          | h   |     |     |     |     |

The approximation does in fact not need to be very exact because for the purpose of solving
for  we only need price means:

|      |         | 1              |     |                   |        | 1          |     |                   |     |     |     |     |
| ---- | ------- | -------------- | --- | ----------------- | ------ | ---------- | --- | ----------------- | --- | --- | --- | --- |
|      |         | Shist         |     |                   |        | Shist     |     |                   |     |     |     |     |
| psim | Ssim   |               |     | (coshsinh1) |        |            |     | (coshsinh1) |     |     |     |     |
|      | h       |                | h   |                   |        |            | h   |                   |     |     |     |     |
|      |         | 24             |     |                   |        | 24         |     |                   |     |     |     |     |
|      |         | S h hist0     |     |                   |        | S h hist0 |     |                   |     |     |     |     |
|      | 1       |                |     |                   | 1      |            |     |                   |     |     |     |     |
|      | |Shist | |coshsinh1 |     |                   | Shist |            |     |                   |     |     |     |     |

|     |     | h   |     |     | h   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 24  |     |     |     | 24  |     |     |     |     |     |     |     |
|     | h   |     |     |     | h   |     |     |     |     |     |     |     |
resulting in
|     |     |     |     | Ssim | |Shist|coshsinh1Shist |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | h     | h                            |     |     | h   |     |     |     |     |

, which can easily be solved numerically for .
Fig 6 shows two examples of applying the transformation. For an hourly profile with positive
prices only, the new transformation and the old factor transformation yield basically the
same result (left). For the profile containing negative prices the new transformation only
yields a plausibly looking result (right).

Simulation results
The simulated trajectories, for daily as well as for hourly prices, resemble the historical
trajectories very well, see Fig 7. The goodness is confirmed by comparing price statistics and
their moments, Fig. 8 and Tab 2. Only the kurtosis of the historical hourly prices is not fully
captured which is, however, a typical issue affecting virtually all power spot price models.
Case ERCOT West
ERCOT West is a power grid zone in Western Texas. This market region is specific insofar as it
has quite a high share of wind power production, in conjunction with low population density
and restricted transmission to other regions. The price plots, Fig 9, show extremely volatile
and spiky quarter-hourly prices, strong spikes occurring for positive as well as negative
prices. Even the daily prices are remarkably volatile and spiky, with a lot of days exhibiting
completely negative average price.
Here, the aim is to reproduce the daily prices from Jan 2008 – Feb 2010 (the history is
chosen to be roughly the same time period as for EEX). Modelling is restricted to daily prices
because the quarter-hourly structure is too irregular to be captured with the means applied
in this work. Further, it can be seen from the price plot that the time series is structurally
changing, being significantly more spiky and negative in the first half of the period. This will
be subjected to a simplification, see below, since the overarching aim of this work is to show
how to generally integrate negative prices into stochastic spot price modelling, not yet
dealing with very specific features.
Extended area hyperbolic sine transformation
When applying the hyperbolic sine transformation x' sinh1p  as in EEX case above, we
t
t
get an unsatisfying result, see Fig 10. Compared to the original time series the downward
spikes are strongly amplified whereas the upward spikes suppressed, comparatively. The
transformation does not preserve the characteristics of the data8. This is because the
 
sinh1 p transformation effectively, compared to range of price levels p, behaves step-
like, see Fig 11. The main body of prices are around a mean level at p 0 therefore gets
compressed, the downward spikes crossing the axis gets torn away. So, one should look for a
less disruptive transformation around p 0. To this end the original form of the
transformation (1) is reconsidered:
 p
x'sinh1 
  
where offset and scalecan be chosen arbitrarily. For 0and1the stochastic
process characteristics stay the same. The Johnson distribution is still the basic solution to
the OU process. Here, 20and30 are taken, see Fig 11. This shifts the turning point
to the mean level of prices and widens the linear part of the transformation. Now, the
transformed time series x' looks much more “natural”, see Fig 10. The choice of values for
t
8 Nevertheless, a parameter estimation for the spot price model was carried out on this data. This is, however,
only successful when the model’s spike regimes are endowed with a more extremer and fat-tailed distribution.

andhad been ad hoc, guided by the appearance of the data9. In a naive fashion, the
parameterization of the transformation here is somewhat similar to the idea of the Box-Cox
transformation, providing an appropriate local transformation for every price level p.
Interestingly, Weron (2008) has already remarked – though for a set-up with positive power
prices only – that the log transformation does not appear appropriate for power prices. It
produces artificial downward spikes for p 0, although those prices are not judged as
extraordinarily jumping from an expert’s view. He then employs no transformation to the
data at all (thus, equivalent to the trivial linear transformation). This, however, produces the
drawback of leaving spikes undamped and requires therefore special distributions for the
spike regime.
The transformation elaborated in this work combines the advantages of both the log and the
linear approach. The choice of andproduces a linear regime of the transformation
encompassing the main, non-spiking range of prices. In the positive and negative spike price
range, however, the transformation behaves again log like, allowing for the “conventional”
modelling.
Why is the modified area hyperbolic sine transformation working well? It is posited that this
is because the transformation function reflects fundamental economics of power prices. The
linear range of the function coincidences with the middle part of the generation stack (merit
order curve). There, we find the variable power generation cost function of mid-load
producing plants (hard coal, CCGT). This function increases with little curvature,
approximately linear with demand, and is not sensitive to changes in demand or supply.
Contrasting, the upper generation stack, consisting of plants with high costs (eg, gas
turbines), is strongly curved upwards and sensitive to load changes. This can cause upward
spikes. The lower end of the stack contains generation with variable costs close to 0,
amongst others, base load plants (lignite, nuclear) and wind generation. There is no
curvature, but the inflexible, must-run characteristics of these generation types nevertheless
makes them sensitive to load changes and can lead to spot auction offers far below
production costs (as shown above).
Estimation and simulation results
Concerning the initially described irregularities in the ERCOT price history some
modifications and simplifications have been made in parameter estimation and simulation,
compared to the standard method for the EEX case.
The change of spike intensity over time is not accounted for (by, eg, parameters changing
over time). Instead, a constant parameter set is estimated from a “homogenized” history.
This means, only the distribution of historical prices is fitted, discarding the original day-to-
day estimation based on a Bayesian scheme. Since we know that the model price
distribution is a mixture of a normal (the mean-reverting regime) and two compound normal
distributions (the spike regimes), most spot price model parameters can be estimated by
maximum likelihood estimation on the price distributions. One further step is needed. We
need the day-to-day regime switching probabilities for the Markov matrix, but only know the
total probability of the process being in the spike regime from the mixture-of-distributions
weights. To this end the average time the process stays in the spike regime is estimated. All
9 Clearly, in the future there should be a mathematical method in place for determining the parameter values,
see Conclusions.

days’ prices are labelled as spikes if their normalized likelihoods of belonging to the spike
price distributions is >0.5. The parameters are shown in Tab. 3. One spike regime was
discarded by the estimation. Both upwards and downwards spikes are captured by a single,
wide distribution, which seems a more parsimonious modelling of the strongly volatile price
dynamics than two distinct spike modes. The pronounced spikiness can be seen from the
high value of about 20% for the probability of jumping from the normal into the spike
regime.
Another model modification had to be applied to the simulation regarding the significant
inhomogenity of the deterministic price level (which, as for the EEX case, is estimated and
then re-added to the simulation stochastic process). If in the simulation a price level
combines with a spike in way that does not correspond to a historical situation (as described
above: all stochastic parameters including spikes are made uniform over the complete
period), some spikes with unrealistically large amplitudes are produced (0.5%of all
prices). These are capped and floored to the historically observed absolute maximum and
minimum. Otherwise, two or three of those events strongly distort the moments of the
simulated price distribution.
The simulated trajectories, see Fig 12, reveal that the “average dynamics” is matched. The
effect of artificial parameter homogeneity can be observed: some spikes occur at
(historically) wrong times (other trajectories match better).  The moments of simulated and
historical price distributions match satisfyingly, see Tab 4 (although less well than for the EEX
case).
An application example: a simple option on the spot price
Knowing that the power market can exhibit very low or even negative prices in the future a
market participant seeks to protect himself against the risk. Eg, a power generator can
purchase a strip of, eg, daily put options on the spot price to secure minimum revenues for
his production. The payoff function for the option for day T is the expected value

|     |     |     |         |     |       |     |     |
| --- | --- | --- | -------- | ---- | ------- | --- | --- |
|     |     |     | V E max | (K  | p(T)),0 |     |     |

, given a strike Kand maturity time T10. Here, it is shown how this put option value can be
calculated in the hyperbolic sine framework and how values differ from a conventional log
approach.
In order to make the central effect clear the initially introduced simple OU process11 is again
employed, omitting a specific spike regime treatment. As shown above the stationary price
| distribution  | p(T) is the Johnson distribution ( |     |     | p):  |     |     |     |
| ------------- | ---------------------------------- | --- | --- | ------ | --- | --- | --- |

|     |       |     |        |       |        | p  |  2   |
| --- | ----- | --- | ------ | ----- | -------- | ----- | ------ |
|     |       |     |        |       |         |      |       |
|     |       |     |        |       | sinh1 | m   |       |
|     |       |     |        |       |        |       | SU   |
|     |       |     | 1      |       |         |    |       |
|     | f (p) |    |        | exp |          |       |       |
|     | SU    |     |        |       |          | 2 2  |        |
|     |       |     |  p | 2     |         |       |       |
S U
|     |     |  2 | 1 |    |    |     |    |
| --- | --- | ----- | --- | --- | --- | --- | --- |
SU
|     |     |     |    |   |    |     |    |
| --- | --- | --- | --- | --- | --- | --- | --- |

10 For reasons of simplicity, an interest rate of 0 is assumed.
11 A deterministic component is omitted.

 p
, here formulated for the full area hyperbolic sine transformation x sinh1 . When
|     |     |     |     |     |     |     |     |     |     |   |    |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
starting out with the log transformation x ln p, ( p 0), the usual log-normal distribution

|     |     |     |     |     | 1   |     |     | ln pm | 2  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------ | ---- | --- | --- | --- |
|     |     |     |     |     |     |     | exp |        |     |     |     |     |
|     |     |     | f   | (p) |    |     |       |        | LN   |     |     |     |
|     |     |     |     | LN  |     |     |      |        |     |     |     |     |
|     |     |     |     |     |    | 2p |       | 2 2   |      |     |     |     |
|     |     |     |     |     | LN  |     |      | L      | N   |     |     |     |

results. For V there are explicit formulas for both the log and the hyperbolic case. For the log
case it is the usual expression:

 

|     |     |     |     |     | V   |   | d   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | LN  | LN  |     |     |     |     |     |

, with  being the cumulative standard normal distribution function and
|     | m  | lnK |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
SU
| d  |     |     | . For the hyperbolic case we get:  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
LN

LN

V ...
SU
|     |     |    |   | m  |   |     |    |    |   |   |   |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.5exp 0.52  exp  d  exp m  d   d K d
|     |     |     | SU  | SU  | SU  | SU  |     | SU  | SU  | SU  | SU  | SU  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

K 
|       | m  | sinh1 |     |     |    |     |     |     |     |     |     |     |
| ----- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|       |     | SU       |    |    |    |     |     |     |     |     |     |     |
| withd |    |          |     |     | .   |     |     |     |     |     |     |     |
| SU    |     |          |    |     |     |     |     |     |     |     |     |     |
SU
We assume that we know the maturity spot price  p(T)distribution’s expected value
|    |     |    |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
mE p(T)  and standard deviation 12.  We then can fit both the log-normal and the
Johnson distribution, comparing the option values based on either assumption. We have

2 
|   | ln   | 1     ,   m |     | lnm0.52 |     |     |      |     |     |     |     |     |
| --- | ----- | ------------- | --- | ----------- | --- | --- | ---- | --- | --- | --- | --- | --- |
| LN  |  m2 |               |    | LN          |     | LN  |      |     |     |     |     |     |


And

|     |    |     | m | 2  | m | 4  | m | 2  |     |     |     |     |
| --- | --- | --- | ---- | --- | ---- | --- | ---- | ---- | --- | --- | --- | --- |
2
|          |    |      |         |     |       |     |     |        |     |     |     |     |
| -------- | --- | ---- | ------- | --- | ----- | --- | --- | ------- | --- | --- | --- | --- |
|        | ln  | 2    | 2      | 1 |       |    |     |      ,  |     |     |     |     |
| SU       |    | 2   | 2      |     | 4    |     | 2  |        |     |     |     |     |
|          |    |      |         |     |       |     |     |        |     |     |     |     |
|          |     | m |        |     |     |     |     |         |     |     |     |     |
| sinh1 |     |      | 0.52 |     |       |     |     |         |     |     |     |     |
| m        |     |      | exp    |     |      |     |     |         |     |     |     |     |
| SU       |     |     |         |     | SU    |     |     |         |     |     |     |     |
|          |     |     |         |     |      |     |     |         |     |     |     |     |

|     |     |     |     |     |     |     |   |     |     |   and   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- |
An exemplary calculation is carried out with E p(T) 40,K 10, 5,10,...,50
20,30. The results are shown in Fig 13. To begin with,V is much bigger than
SU

12 From the forward curve and a market volatility indicator.

V for large . This is trivial because f (p)then comprises negative prices as opposed to
LN SU
f (p). However, V V holds for all , both valuations do not coincidence for the case
LN SU LN
of a positive prices only distribution. The explanation comes from the form of the price
distribution. The Johnson distribution attributes a bigger mass to small prices p 0. This
result indicates that the option valuation based on the hyperbolic sine framework should
always be considered to avoid undervaluation, being aware of the fact that every power spot
market exhibits a substantial amount of prices p 0, even if negative prices are not
permitted.
Concluding remarks
It is increasingly recognized that negative prices are an inherent feature of the commodity
power. Constraints on the supply side limit the flexibility of a generation facility and forces to
sell off production with discount in case of demand slumps. This is why permitting negative
bid, offers and auction results in the power spot market is economically reasonable.
Several non-European power markets pioneered, the European markets EEX and Nordpool
have introduced negative prices recently. It is an exciting question if with the ongoing
European market integration the concept is going to spread to other regional markets. Eg, a
formal spot market coupling is on the way to be realized between Germany/Scandinavia and
France/Belgium/Netherlands.
It is obvious that under these circumstances the so far prevailing tendency to deal with the
“problem” by “workarounds” or exclusion/negligence is to be abandoned and sound
integration into the various stochastic power price modelling frameworks needs to be
achieved.
The solution proposed in this article is to replace the usual initial log transformation of prices
by the area hyperbolic sine transformation. Several arguments were provided to support this
approach. Firstly, the choice is natural, leaving the transformation for positive prices almost
unchanged and mirroring the logarithm feature to the negative price axis. This choice is
equivalent with the finding that the price dynamics in negative price region is analogous to
the one in the positive region, volatility basically depending on the absolute price level.
Secondly, combining the hyperbolic sine transformation with stochastic models does not
significantly increase the difficulty of treatment compared to the log case. Interestingly, an
analogue to the log-normal distribution as a theoretical “basic distribution” is found: the
Johnson distribution. This is consistent with the difficulty argument since it is also a closed
form expression. This convenient characteristics has been exploited for the valuation of an
option in the last section.
Thirdly, the area hyperbolic sine transformation exhibits a connection to fundamentals of
power prices, the generation stack and its production cost function. This is, eg, constituted
by a linear regime of transformation for the moderate (normal) price regime. It has been
noted before (Weron, 2008) that the log transformation does not work well in that price
regime, producing artificial distortions. Here, it was found that the area hyperbolic sine
transformation as an effective combination of linear and log transformation performs well,
preserving the characteristics of the data.
Summing up, it is posited that the introduction of the area hyperbolic sine transformation is
the natural step for power price modelling as response to the permit of negative prices at
power spot exchanges. This is also supported by the fact that the transformation can be
applied to power markets with positive prices only equally well.

There is one important issue for negative power prices to be dealt with in future work. The
power markets are not yet in a “steady state” regarding the handling of negative price
occurrences. The changing nature of these occurrences was an issue in this work for the case
of ERCOT West. It is also obvious when comparing EEX 2010 data with 2009. The frequency
and severity of negative occurrences is strongly reduced in 2010 compared to 2009. This is
on the hand attributed to a learning effect of energy traders, eg, changed power plant
production schedules. On the other hand, this is due to changing regulations concerning
renewable energy (eg, wind) marketing. So, it is difficult to anticipate currently how a steady
market state in the future could look like and the energy trading business is reliant on close-
to-the-market modelling activities on this subject.
References
Brigo, D., Mercurio, F. and Sartorelli, G., 2003, “Alternative Asset-Price Dynamics and Volatility Smile,
Quantitative Finance 3 (3), pp. 173-183
Carr, P., Tari, M. and Zariphopoulou, T. , 1999, “Closed form option valuation with smiles”, Working
paper
Culot, M., Goffin, V., Lawford, S. , de Menten, S. and Smeers, Y., 2006, “An Affine Jump Diffusion
Model for Electricity”, Seminars, Groupement de Recherche en Economie Quantitative d’Aix-
Marseille
De Jong, C., 2006, “The nature of power spikes: a regime-switch approach”, Studies in non-linear
dynamics and econometrics 10 (3), article 3
De Jong, C. and Schneider, S., 2009, “Cointegration between gas and power spot prices”, The Journal
of Energy Markets 2(3), pp. 27-46
Dettmer, F. and Jacob, M., 2009, „Stunden, in den Strom kein „Gut“ ist“, emw 5, p. 70-72
Johnson, N. L., Kotz, S. and Balakrishnan, N., 1994, “Continuous Univariate Distributions”, Volume 1,
(Second Edition), John Wiley & Sons
Knittel, C.R. and Roberts, M.R., 2001, “An empirical examination of deregulated electricity prices”,
PWP-087 Working paper, University of California, Energy Institute
Sewalt, M. and De Jong, C., 2003, „Negative prices in electricity markets”, Commodities Now, June
2003, p. 74-77
Sprenger, S. and Laege, E., 2009, „Negative Spotpreise an der EEX – Analyse und Auswirkungen auf
das Risikomanagement eines Energieerzeugers“, Working paper, E.ON Energy Trading SE
Viehmann, J. and Sämisch, H., 2009, „Windintegration bei negativen Strompreisen“,
Energiewirtschaftliche Tagesfragen 59(11), p. 49-51
Weron, R., 2008, “Heavy-Tails and Regime-Switching in Electricity Prices”, Mathematical Methods of
Operations Research 69(3)

Figures and tables
EEX hourly prices
2500
2000
1500
1000
500
0
-500
-1000
2002 2004 2006 2008 2010
hWM/€
EEX hourly prices - Christmas 2009
100
50
0
-50
-100
-150
-200
12/20 12/27
hWM/€
Fig. 1: The history of EEX hourly prices.
area hyperbolic sine transformation
5
arsinh(p)
4 [-]ln([-]p)
3
2
1
0
-1
-2
-3
-4
-5
-50 -40 -30 -20 -10 0 10 20 30 40 50
Fig. 2: Price transformation sinh1p along with ln(p)and ln(p)for comparison.

| 002              |             |     |           | 002              |             |     |     |     |
| ---------------- | ----------- | --- | --------- | ---------------- | ----------- | --- | --- | --- |
| ]WM/€[ ecirP 001 |             |     |           | ]WM/€[ ecirP 001 |             |     |     |     |
| 0                |             |     |           | 0                |             |     |     |     |
| 001-             |             |     |           | 001-             |             |     |     |     |
| 002-             |             |     |           | 002-             |             |     |     |     |
|                  | Volume [MW] |     |           |                  | Volume [MW] |     |     |     |
|                  |             |     |           |                  |             |     |     |     |
Fig. 3:  Bid/demand (grey) and ask/supply (red) curves of hours 1 (left) and 14 (right) for the
EEX auctions of Dec 26th, 2009 (schematically re-drawn).

Probability distributions - mean: 80, stddv 40 Probability distributions - mean: 1, stddv 2 Probability distributions - mean: -20, stddv 20
| 0.014            |     |     | 1.6 |            |     | 0.05  |         |     |
| ---------------- | --- | --- | --- | ---------- | --- | ----- | ------- | --- |
| Johnson          |     |     |     | Johnson    |     |       | Johnson |     |
| 0.012 log normal |     |     | 1.4 | log normal |     | 0.045 |         |     |
0.04
1.2
| 0.01 |     |     |     |     |     | 0.035 |     |     |
| ---- | --- | --- | --- | --- | --- | ----- | --- | --- |
1
| 0.008 |     |     |     |     |     | 0.03  |     |     |
| ----- | --- | --- | --- | --- | --- | ----- | --- | --- |
|       |     |     | 0.8 |     |     | 0.025 |     |     |
0.006
|       |     |     | 0.6 |     |     | 0.02  |     |     |
| ----- | --- | --- | --- | --- | --- | ----- | --- | --- |
| 0.004 |     |     |     |     |     | 0.015 |     |     |
0.4
0.01
| 0.002 |     |     | 0.2 |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- |
0.005
-010 0 -80 -60 -40 -20 0 20 40 60 80 100   -010 0 -80 -60 -40 -20 0 20 40 60 80 100   -010 0 -80 -60 -40 -20 0 20 40 60 80 100
EEX hourly prices, working days, early evening
| 70  |     |     |     |     | EEX hourly prices, Sunday/holidays, deep night hours |     |     |     |
| --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- |
120
60
100
50
80
40
| qerf |     |     |     | qerf 60 |     |     |     |     |
| ---- | --- | --- | --- | ------- | --- | --- | --- | --- |
30
40
20
| 10   |       |     |         | 20   |           |                |       |     |
| ---- | ----- | --- | ------- | ---- | --------- | -------------- | ----- | --- |
| 0    |       |     |         | 0    |           |                |       |     |
| 0 50 | 100   | 150 | 200 250 | -600 | -500 -400 | -300 -200 -100 | 0 100 |     |
|      | €/MWh |     |         |      |           | €/MWh          |       |     |
Fig. 4: Qualitative comparison of empirical spot price distributions and theoretical
distributions. Theoretical distributions: Johnson and log-normal with same mean and
standard deviation (except for the negative mean case, right).

|     | EEX hourly prices |     | EEX daily prices |     |     |
| --- | ----------------- | --- | ---------------- | --- | --- |
150
600
400
100
200
| hWM/€ |     |     | hWM/€ |     |     |
| ----- | --- | --- | ----- | --- | --- |
| 0     |     |     | 50    |     |     |
-200
0
-400
| -600 |     |     | -50 |     |     |
| ---- | --- | --- | --- | --- | --- |
Q4-08 Q1-09 Q2-09 Q3-09 Q4-09 Q1-10 Q4-08 Q1-09 Q2-09 Q3-09 Q4-09 Q1-10
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
Fig. 5:  EEX hourly and daily price history from Oct 2008 till Jan 2010, time period as taken for
modelling.

Transformation of historical hourly profiles Transformation of historical hourly profiles
| 70  |     |     | 100 |     |     |
| --- | --- | --- | --- | --- | --- |
original
60 hyperbolic sine scaling
simple factor scaling
50
50
0
40
| hWM/€ |     |     | hWM/€ |     |     |
| ----- | --- | --- | ----- | --- | --- |
30
-50
20
-100
original
| 10  |     |     |     | hyperbolic sine scaling |     |
| --- | --- | --- | --- | ----------------------- | --- |
simple factor scaling
| 0           |             |       | -150        |             |       |
| ----------- | ----------- | ----- | ----------- | ----------- | ----- |
| 00:00 06:00 | 12:00 18:00 | 00:00 | 00:00 06:00 | 12:00 18:00 | 00:00 |
|             |             |       |             |             |       |
Fig 6:  Scaling transformations of historical hourly price profiles EEX to new daily average
prices (20 €/MWh for both cases). Left: simple factor scaled profile hidden by practically
identical hyperbolic sine scaled profile.

EEX hourly prices, simulated
| EEX daily prices, simulated |     | 500 |     |
| --------------------------- | --- | --- | --- |
140
400
120
| 100 |     | 300       |     |
| --- | --- | --------- | --- |
| 80  |     | hWM/€ 200 |     |
hWM/€
100
60
0
40
| 20  |     | -100 |     |
| --- | --- | ---- | --- |
| 0   |     | -200 |     |
Q4-08 Q1-09 Q2-09 Q3-09 Q4-09 Q1-10 Q4-08 Q1-09 Q2-09 Q3-09 Q4-09 Q1-10

| EEX daily prices |     |       | EEX hourly prices |
| ---------------- | --- | ----- | ----------------- |
| 140              |     | 500   |                   |
| 120              |     | 400   |                   |
| 100              |     | 300   |                   |
| 80               |     | 200   |                   |
| hWM/€            |     | hWM/€ |                   |
| 60               |     | 100   |                   |
| 40               |     | 0     |                   |
| 20               |     | -100  |                   |
| 0                |     | -200  |                   |
Q4-08 Q1-09 Q2-09 Q3-09 Q4-09 Q1-10 Q4-08 Q1-09 Q2-09 Q3-09 Q4-09 Q1-10

Fig 7: Exemplary simulated and historical trajectories.

EEX deseasonalized daily prices
EEX deseasonalized daily prices, simulated
| 4000 |     | 90  |     |
| ---- | --- | --- | --- |
80
3500
70
3000
60
2500
50
qerf
2000
40
1500
30
| 1000 |     | 20  |     |
| ---- | --- | --- | --- |
| 500  |     | 10  |     |
| 0    |     | 0   |     |
-1 -0.8 -0.6 -0.4 -0.2 0 0.2 0.4 0.6 0.8 1 -1 -0.8 -0.6 -0.4 -0.2 0 0.2 0.4 0.6 0.8 1

Hourly prices, simulated Negative prices only EEX hourly prices Negative prices only
| 1400 | 50  |      |     |
| ---- | --- | ---- | --- |
|      |     | 2500 | 50  |
|      | 45  |      | 45  |
1200
|      | 40  | 2000 | 40  |
| ---- | --- | ---- | --- |
| 1000 | 35  |      | 35  |
| 800  | 30  | 1500 | 30  |
|      | 25  |      | 25  |
600
|     | 20  | 1000 | 20  |
| --- | --- | ---- | --- |
|     | 15  |      | 15  |
400
|     | 10  | 500 | 10  |
| --- | --- | --- | --- |
200
|     | 5   |     | 5   |
| --- | --- | --- | --- |
| 0   | 0   | 0   | 0   |
-200 0 200 400 -200 -150 -100 -50 0 -200 0 200 400 -200 -150 -100 -50 0

Fig 8: Histograms of daily (x) and hourly prices (the above exemplary simulated scenario
only for hourly prices). Left: simulation, right: historical.

|     | ERCOT West daily prices |     | ERCOT West quarter hourly prices |     |     |
| --- | ----------------------- | --- | -------------------------------- | --- | --- |
400
2500
350
2000
300
1500
250
1000
200
| WM/$ |     |     | WM/$ 500 |     |     |
| ---- | --- | --- | -------- | --- | --- |
150
0
100
-500
50
-1000
0
-1500
-50
| 2008 | 2009 | 2010 | -2000 2008 | 2009 | 2010 |
| ---- | ---- | ---- | ---------- | ---- | ---- |

Fig 9:  EROCT West market clearing price history Jan 2008 – Feb 2010.

|     | arsinh(p), ERCOT daily price |     | arsinh((p-20)/30), ERCOT daily price  |     |     |
| --- | ---------------------------- | --- | ------------------------------------- | --- | --- |
6
6
| 4    |      |      | 4    |      |      |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 2    |      |      | 2    |      |      |
| 0    |      |      | 0    |      |      |
| -2   |      |      | -2   |      |      |
| -4   |      |      | -4   |      |      |
| 2008 | 2009 | 2010 | 2008 | 2009 | 2010 |

 p
Fig 10:  Applying the arsinh transformation x'sinh1 to ERCOT daily prices. Left:
|     |     |     |    |     |     |
| --- | --- | --- | ----- | --- | --- |
0,1. Right: 20,30.

|     | 4   |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
3
2
1
0
-1
-2
-3
arcsinh((p-20)/30)
arcsinh(p)
-4
|     | -50 0 | 50 100 150 | 200 250 300 350 | 400 |     |
| --- | ----- | ---------- | --------------- | --- | --- |

Fig 11:  Depiction of arcsinh transformations as applied above.

|      | Daily prices, simulated |     |     |      |      |     | ERCOT West daily prices |     |     |      |
| ---- | ----------------------- | --- | --- | ---- | ---- | --- | ----------------------- | --- | --- | ---- |
| 400  |                         |     |     |      | 400  |     |                         |     |     |      |
| 350  |                         |     |     |      | 350  |     |                         |     |     |      |
| 300  |                         |     |     |      | 300  |     |                         |     |     |      |
| 250  |                         |     |     |      | 250  |     |                         |     |     |      |
| 200  |                         |     |     |      | 200  |     |                         |     |     |      |
| WM/$ |                         |     |     |      | WM/$ |     |                         |     |     |      |
| 150  |                         |     |     |      | 150  |     |                         |     |     |      |
| 100  |                         |     |     |      | 100  |     |                         |     |     |      |
| 50   |                         |     |     |      | 50   |     |                         |     |     |      |
| 0    |                         |     |     |      | 0    |     |                         |     |     |      |
| -50  |                         |     |     |      | -50  |     |                         |     |     |      |
| 2008 | 2009                    |     |     | 2010 | 2008 |     | 2009                    |     |     | 2010 |

Fig 12:  Exemplary simulated and historical trajectory ERCOT.

|     | 5   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
area hyperbolic sine
|     | 4.5 | log normal |     |     |     |     |     |     |     |     |
| --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
4
3.5
eulav noitpo tup 3
2.5
2
1.5
1
0.5
0
|     | 10  | 15  | 20  | 25  | 30 35 | 40  | 45  | 50  |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
std dev prices

|       | Probability distributions - std dev price: 10 |     |            |     |      | Probability distributions - std dev price: 50 |     |     |            |     |
| ----- | --------------------------------------------- | --- | ---------- | --- | ---- | --------------------------------------------- | --- | --- | ---------- | --- |
| 0.045 |                                               |     |            |     | 0.03 |                                               |     |     |            |     |
|       |                                               |     | Johnson    |     |      |                                               |     |     | Johnson    |     |
| 0.04  |                                               |     | log normal |     |      |                                               |     |     | log normal |     |
0.025
0.035
| 0.03 |     |     |     |     | 0.02 |     |     |     |     |     |
| ---- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
0.025
0.015
0.02
| 0.015 |     |     |     |     | 0.01 |     |     |     |     |     |
| ----- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
0.01
0.005
0.005
| 0   |     |     |     |     | 0   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -50 | 0   | 50  |     | 100 | -50 |     | 0   | 50  |     | 100 |

|     | p   |     |     |     |     |     | p   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig 13:  Top: Value of the put option over standard deviation (p(T)) of the spot price at
maturity.  Bottom: Johnson and log-normal distribution of p(T) for two exemplary (p(T)).

EEX
| Time-series parameters: |     |      | Switch probabilities |       |     |
| ----------------------- | --- | ---- | -------------------- | ----- | --- |
| Normal regime           |     | 0,42 | from N to H          | 0,95% |     |
α
|     | μ   | 0,02 | from H to N | 71,15% |     |
| --- | --- | ---- | ----------- | ------ | --- |
|     |     | 0,11 | from N to L | 1,93%  |     |
σ
| High-spike regimμH |     | 0,35 | from L to N | 78,50% |     |
| ------------------ | --- | ---- | ----------- | ------ | --- |
|                    | σH  | 0,06 |             |        |     |
|                    | λH  | 0,10 |             |        |     |
| Low-spike regimμL  |     | 0,24 |             |        |     |
|                    | σL  | 0,04 |             |        |     |
|                    | λL  | 2,00 |             |        |     |
Tab. 1:   Parameter estimates for the (daily) spot price model, case EEX.

EEX
|     | historical prices | simulated prices |     |     |     |
| --- | ----------------- | ---------------- | --- | --- | --- |
daily arsinh prices, deseasonalized
| mean               | 0,00  |     |       |     |     |
| ------------------ | ----- | --- | ----- | --- | --- |
| standard deviation | 0,18  |     | 0,18  |     |     |
| skewness           | -1,88 |     | -1,56 |     |     |
| kurtosis           | 13,03 |     | 11,19 |     |     |
daily prices
| mean               | 44,74 |     | 44,86 |     |     |
| ------------------ | ----- | --- | ----- | --- | --- |
| standard deviation | 17,69 |     | 17,68 |     |     |
| skewness           | 1,51  |     | 1,44  |     |     |
| kurtosis           | 5,92  |     | 5,93  |     |     |
hourly prices
| mean               | 44,74 |     | 44,83 |     |     |
| ------------------ | ----- | --- | ----- | --- | --- |
| standard deviation | 24,46 |     | 23,94 |     |     |
| skewness           | 1,89  |     | 1,57  |     |     |
| kurtosis           | 20,02 |     | 10,36 |     |     |

Tab 2: Statistics of historical and simulated prices EEX. Simulation figures aggregated from
100 scenarios.

ERCOT
| Time-series parameters: |     |      | Switch probabilities |        |     |
| ----------------------- | --- | ---- | -------------------- | ------ | --- |
| Normal regime           | α   | 0,59 | from N to S          | 21,39% |     |
|                         | μ   | 0,03 | from S to N          | 60,62% |     |
|                         | σ   | 0,32 |                      |        |     |
| Spike regime            | μS  | 0,00 |                      |        |     |
|                         | σS  | 0,74 |                      |        |     |
|                         | λ   | 0,50 |                      |        |     |

Tab 3: Parameter estimates for the (daily) spot price model, case ERCOT.

ERCOT
historical prices simulated prices
daily arsinh prices, deseasonalized
| mean               |       | 0,04 |
| ------------------ | ----- | ---- |
| standard deviation | 0,53  | 0,52 |
| skewness           | -0,43 | 0,19 |
| kurtosis           | 6,49  | 5,51 |
daily prices
| mean               | 39,40 | 40,63  |
| ------------------ | ----- | ------ |
| standard deviation | 32,40 | 32,83  |
| skewness           | 2,50  | 2,73   |
| kurtosis           | 18,39 | 19,78  |
Tab 4:  Statistics of historical and simulated prices ERCOT. Simulation figures aggregated
from 100 scenarios.