The Nature of Power Spikes:
a regime-switch approach

Cyriel de Jong

ERIM REPORT SERIES RESEARCH IN MANAGEMENT

ERIM Report Series reference number

ERS-2005-052-F&A

Publication

Number of pages

Persistent paper URL

October 2005

30

Email address corresponding author

cjong@rsm.nl

Address

Erasmus Research Institute of Management (ERIM)
RSM Erasmus University / Erasmus School of Economics

 Erasmus Universiteit Rotterdam
 P.O.Box 1738
 3000 DR Rotterdam, The Netherlands
Phone:
Fax:

+ 31 10 408 1182
+ 31 10 408 9640

Email:
Internet:

info@erim.eur.nl
 www.erim.eur.nl

Bibliographic data and classifications of all the ERIM reports are also available on the ERIM website:
www.erim.eur.nl

ERASMUS  RESEARCH  INSTITUTE  OF  MANAGEMENT

REPORT SERIES

RESEARCH IN MANAGEMENT

ABSTRACT AND KEYWORDS

Abstract

Due  to  its  non-storable  nature,  electricity  is  a  commodity  with  probably  the  most  volatile  spot

prices,  exemplified  by  occasional  spikes.  Appropriate  pricing,  portfolio,  and  risk  management

models have to incorporate these characteristics, and the spikes in particular. We investigate the

nature of power spikes in a number of different markets. We test what time-series model is best

able to capture the dynamics of these disruptive spot prices. We use regime-switching models to

infer whether the price spikes should be treated as abnormal and independent deviations from

the ‘normal’ price dynamics or whether they form an integral part of the price process. We test

the time-series models on day-ahead markets in Europe and the US. We find that regimeswitch

models  are  better  able  to  capture  the  market  dynamics  than  a  GARCH(1,1)  or  Poisson  jump

model. We also find clear differences between the markets and attribute part of the differences

to the share of hydro-power in the total supply stack: hydro-power serves as an indirect means

Free Keywords

Availability

to store electricity, which has a dampening effect on spikes.

Power Prices, Spot Markets, Regime-switches, Volatility, Spikes, Risk

The ERIM Report Series is distributed through the following platforms:

Academic Repository at Erasmus University (DEAR), DEAR ERIM Series Portal

Social Science Research Network (SSRN), SSRN ERIM Series Webpage

Research Papers in Economics (REPEC), REPEC ERIM Series Webpage

Classifications

The electronic versions of the papers in the ERIM report Series contain bibliographic metadata
by the following classification systems:

Library of Congress Classification, (LCC) LCC Webpage

Journal of Economic Literature, (JEL), JEL Webpage

ACM Computing Classification System CCS Webpage

Inspec Classification scheme (ICS), ICS Webpage

The Nature of Power Spikes:
a regime-switch approach

Cyriel de Jong

Rotterdam School of Management at Erasmus University

Draft September 2005

Due  to  its  non-storable  nature,  electricity  is  a  commodity  with  probably  the  most
volatile spot prices, exemplified by occasional spikes. Appropriate pricing, portfolio,
and risk management models have to incorporate these characteristics, and the spikes
in  particular.  We  investigate  the  nature  of  power  spikes  in  a  number  of  different
markets. We test what time-series model is best able to capture the dynamics of these
disruptive  spot  prices.  We  use  regime-switching  models  to  infer  whether  the  price
spikes should be treated as abnormal and independent deviations from the ‘normal’
price dynamics or whether they form an integral part of the price process. We test the
time-series models on day-ahead markets in Europe and the US. We find that regime-
switch models are better able to capture the market dynamics than a GARCH(1,1) or
Poisson  jump  model.  We  also  find  clear  differences  between  the  markets  and
attribute part of the differences to the share of hydro-power in the total supply stack:
hydro-power serves as an indirect means to store electricity, which has a dampening
effect on spikes.

Keywords:  power  prices,  spot  markets,  regime-switches,  volatility,  spikes,
risk

All errors pertain to the author. Contact details: cjong@rsm.nl, tel. +31 10 408 2300.

1

1  Introduction

Now that many wholesale energy markets are deregulated, market participants have to

get used to an environment with very volatile prices and high uncertainty, far larger than in

any other commodity market. Electricity is a pure flow commodity with limited storability,

which strongly affects the behavior of electricity spot and derivatives prices. This lack of

flexibility causes spot prices to depend largely on local and temporal supply and demand

conditions. Typically, only a few large industrial customers have the flexibility to vary their

power demand in response to market conditions, whereas most power plants can gear up or

gear down generation only with a significant time lag. This time lag causes occasional

extreme price spikes, which revert within hours or days to a more stable level.

The peculiar characteristics of electricity prices have induced researchers to develop

special electricity price models that are at the heart of risk and portfolio management

applications: for the pricing of physical and financial contracts, and for the valuation of real

assets. Example models are described in Schwartz (1997), Hilliard and Reis (1998), Pilipovic

(1998), Pirrong and Jermakyan (1999, 2000), Lucia and Schwartz (2002), Bhanot (2000),

Deng (2000), Kholodnyi (2003), Knittel and Roberts (2001), Huisman and Mahieu (2001),

Escribano, Pena and Villaplana (2002), De Jong and Huisman (2003) and Geman and

Roncoroni (2004).

Despite the seemingly large number of papers, there is no single paper that provides a

convincing theoretical and empirical analysis of power spot prices.  Some papers focus on the

implications of spot price processes on forward and derivatives prices, which limits the

flexibility to develop a realistic spot price model. Other papers present potentially strong spot

price models, but avoid the empirical comparison with challenging other models in a wide

enough market sample. Because spot markets have strongly developed over time in many

regions, we believe it is imperative not to test a model also with relative recent data.

Furthermore, because market structures and price dynamics differ widely across regions,

enough different markets need to be tested. In fact, only Escribano, Pena and Villaplana

(2002) provide extensive empirical tests on a wide range of markets and including rather

recent time periods. However, missing in Escribano et al (2002) are the regime-switch

specifications that have recently shown promising results in Huisman and Mahieu (2001),

Deng (2000), Kholodnyi (2001) and De Jong and Huisman (2003). Typically, the price

process is divided into two regimes: one for the ‘normal’ process, one for the ‘spikes’. This

regime-separation is used to capture the systematic alternations between stable and unstable

2

states of demand and supply. In this paper we develop a number of representative regime-

switch models and empirically compare them with non-regime switch models in a variety of

markets while including recent data.

For understanding energy markets, we need a good understanding of both spot and

forward prices. Contrary to most other markets, spot and forward prices deserve a separate

analysis, because they cannot be easily linked. To speak with Pilipovic (1998), power prices

exhibit a ‘split personality’. Again due to the non-storability the market forces determining

short-term prices are very distinct from those determining longer-term prices. As a result the

spillover effects and correlation between them are very limited. That’s why in this paper we

analyze spot (day-ahead) prices without reference to the implication for forward prices.

Knowledge of the dynamics of spot prices, and the spike process in particular, is

important in valuing both financial and real assets. For example, flexible energy production

capacity provides an option to produce or not in the hours or days ahead. The value of such

flexible capacity is therefore equal to the value of a series of call options on the spot (short-
term) price1, and our price models provide a basis to value those assets. For a proper valuation

we need to know to what extent spikes can be treated as independent events, where

(in)dependence can be measured on a number of dimensions. First, dependence in probability
means that the occurrence of a spike impacts the probability of another spike2. Second,

dependence in size means that the size of a spike impacts the size of subsequent spike.

Finally, effect dependence means that spikes influence the price level in subsequent periods,

so is a combination of probability and size dependence. Regime-switch models are well-

suited to test for such independence, so we will do so in this paper.

The paper is built up as follows. First, in section 2, we discuss spot price models with

varying levels of independence for the spikes, and explain how parameters can be estimated.

In section 3 we analyze the prices in various day-ahead power markets and determine how

well the previously developed models capture their dynamics. Finally, we interpret the

empirical analysis in the light of the supply side of the power markets and find support for

lower spikes in markets with a large share of hydro-power.

1 If fuel costs are volatile as well, then a generation asset can be considered an option on the difference between
the electricity price and fuel costs, the spark spread.
2 This is the assumption of standard stochastic jump processes, where the spike intensity is constant or at most
seasonal.

3

2  Modeling spot electricity prices

In this section we discuss specifications for power spot prices. We derive the models

by gradually extending the basic mean-reverting specification (see e.g. Lucia and Schwartz,

2001) to include spikes. First, we present a standard stochastic jump model and explain how it

can be generalized to a regime-switch model. This allows us to incorporate the most

prominent features of electricity spot prices, mean-reversion and spikes, but still treat the

spikes as an integral part of the whole price process. We progressively separate the spikes

further from the rest of the process to finally arrive at a model where the spikes are truly

independent disruptions from the stable price process, similar to De Jong and Huisman

(2003).

All these models have in common that the spot price (actually a day-ahead price), Pt,

is divided into a predictable component f(t) and a stochastic component xt (Hamilton, 1994).

p

t

= ln

P
t

=

( )
tf

+

x

t

(1)

The first component, f(t), accounts for predictable regularities, such as any genuine seasonal

behavior or trend, and is a deterministic function of time. We specify it later in the text. The

stochastic second component, xt, is the more interesting and we continue with its specification

below. In the remaining we refer to the stochastic part xt as the “log spot price”, or even the

“spot price”, but remember that in fact it is the log spot price from which predictable trends

have been removed.

2.1  Mean-reverting and stochastic jump models

A standard mean-reverting specification (Lucia and Schwartz, 2002) is relatively
successful in modeling commodities such as oil and gas3, but not in modeling electricity, due

to the presence of spikes. This holds especially true in markets with no or limited hydro-

power capacity, leaving practically no opportunity to store the commodity directly or

indirectly. In a discrete-time framework, which we use throughout this paper, the mean-

reverting model is in fact an auto-regressive process of order 1 (AR(1)):

Model 1 - mean-reverting:

dx

t

=

(
ma
1
1

-

x

t

1
-

)

+

es
1
t

3 See for example Pindyck (1999).

4

(2)

Modeling spikes in a satisfactory framework has turned out to be a major challenge for

researchers and practitioners in electricity markets. The most common approach is the

addition of a stochastic jump process to the mean-reverting process (Escribano et al, 2002,

Deng, 1999). Most common specifications for the jump are the normal distribution and a

compound normal process. In the latter case, the jumps Jt are each the sum of independently

and identically distributed normals Zt. The Poisson arrival process for the compound jumps

can produce strongly right-skewed jumps and appeared already in the early work of Merton
(1976) for modeling extreme stock price returns.

dx

t

=

(
ma
2
2

-

x

t

1
-

)

+

es
2
t

+

n

t(cid:1)

i

=

0

Z

t

with

Z

t
n

~

~

t

)

N

(
S
S
,
sm
2
2
(
)2
POI
l

(3a)

When we let the arrival intensity of the Poisson jumps approach zero, and its multiplication

with the expected jump size approach a constant

(
l
2

ﬁ

,0

S ﬁ
ml
2
2

c

)

, we observe that this

model nests a model with normally distributed jumps. Please note as well that in a stochastic

jump model the jumps are written down as an integral part of the price process. So, in a

stochastic jump model, a spike has a lasting effect on subsequent prices.

However, we rewrite this in a notation that is split up in a jump process and a spike

process. Although this might be a bit unusual for stochastic jump models, it eases comparison

to regime-switch models:

Model 2 – Stochastic Poisson jumps:
mean-reverting state M:

dx

t

=

(
ma
2
2

-

x

t

1
-

)

+

es
2
t

spike state S, when nt>0:

dx

t

=

(
ma
2
2

-

x

t

1
-

)

+

es
2
t

+

probability

M
p
2

-=

S
1 p
2

(3b)

n

t(cid:1)

i

=

0

Z

t

Z

t
n

~

~

t

)

N

(
S
S
,
sm
2
2
(
)2
POI
l

   prob.

=S
p
2

(
)2
exp l
-

(3c)

Although stochastic jump models are popular in modeling FX and stock returns, they

do not seem to be well suited for electricity prices: in electricity markets, spikes are typically

short-lived and die out quickly. In a mean-reverting stochastic jump process this can only be

achieved by an unrealistically high mean reversion parameter that forces prices back to

normal levels after a spike (see for a discussion of this point Geman and Roncoroni (2004)

5

and Huisman and Mahieu (2001)). Furthermore, the jump arrival process is constant through

time, whereas in electricity markets we typically observe alternating periods of high and

periods with low jump frequency. So, jump arrival probabilities should ideally be time-

dependent (stochastic).

2.2  Regime-switch models

The requirement of stochastic jump arrival probabilities directly leads to regime-

switch models as natural candidates. These models have shown potential, because they allow

for distinct time-series behavior in different periods of time. The basic regime model has the

following simple specification (Hamilton, 1989):

x =
t

tr
x
t

(4)

Here  tr  is a latent variable representing the regime of the process in time period t. The

distinguishing characteristic is that this latent regime variable is not imposed ex ante, but

stochastically depends on previously realized price levels. For example, in a two-regime

framework, we assume that the spot price of electricity can be in one out of two regimes at

each point in time, a normal and a spike regime. Then, the probability of a spike regime at any

point in time depends on the regime in the previous point in time, so actually on the previous

price levels. Typically, if the previous price (or prices) was quite extreme (high probability

that it was a spike), the current price is more likely to come from the spike regime as well.

The benefits of regime-switches can easily be seen when we extend the stochastic

jump model (2) with regime-switches. The primary change is that the probability of jumps is

no longer fixed and equal to

1

-

(
)2
exp
l-

, but dependent on the current regime4.

Model 3 – regime switches with stochastic Poisson jumps:

mean-reverting regime M:

dx

t

=

(
ma
3
3

-

x

t

1
-

)

+

es
3
t

spike regime S:

dx

t

=

(
ma
3
3

-

x

t

)
- +
1

n

1
+

t(cid:1)

i

1
=

Z

t

with

Z

t
n

Markov transition matrix:

=P
3

(cid:7)
1
(cid:5)
(cid:6)

S
p
-
3
M
p
3

S
p
3
M
-
p
3

(cid:4)
(cid:2)
(cid:3)

1

~

~

t

N

(
S
S
,
sm
3
3
(
)3
POI
l

)

(5a)

(5b)

(5c)

4 The only other change is that we equate the variance of the first jump to the variance of the other jumps. This is
because (cid:1)2(cid:2)t has dropped from equation (3c) and incorporated as the first jump in equation (5b).

6

At any point in time the price process is either in regime (or ‘state’) M or in regime S.

However, contrary to a stochastic jump model, the probability that a certain state prevails is

not constant, but dependent on the previous state, a stochastic entity. These probabilities are

derived from the Markov transition matrix. With two regimes, the Markov transition matrix (cid:3)
is a 2x2 matrix. The element in column j and row i contains the probability (cid:4)ij of going from

regime i in period t to regime j in period t+1 (i,j = M,S). In practice, the current regime is not

directly observable, but determined through an adaptive probabilistic process using Bayesian

inference. More particularly, based on the posterior probabilities of the current regime, we can

calculate the prior probability of the next regime being of a certain type. As a result, this

regime-switch model is an extension of stochastic jump model in the sense that it has regime-

switch probabilities that stochastically adapt themselves to the previously observed prices. In

particular, just like model 1 is a nested version of model 2, so is model 2 a nested version of

model 3.

Unfortunately, model 3 cannot be expected to fit all spot prices well, because it still

assumes that spikes are always directed upwards (or at least in one direction), and a strong

mean-reversion is required to let them revert to ‘normal’ prices. Both Deng (1999) and

Huisman and Mahieu (2001) therefore propose a regime-switch model with an extra regime to

pull prices down. Using the same Poisson arrival process as before, this leads to the following

three-regime model:

Model 4: Regime switches with three regimes and stochastic Poisson jumps:
(
ma
4
4

mean-reverting regime M:

es
4
t

dx

-

+

=

x

)

t

t

1
-

(6a)

spike regimes:

dx

t

=

(
ma
4
4

-

x

t

)
- +
1

n

1
+

t(cid:1)

Z

t

with

n

t

~

POI

(
)4
l

  (6b)

Up regime U:

Down regime D:

Z

Z

~
t N

~
t N

Markov transition matrix:

=P
4

)S
(
S
4 ,
sm+
4
)S
(
S
4 ,
sm-
4
(cid:7) -
S
S
1
pp
4
4
(cid:5)
0
0
(cid:5)
(cid:5)
**
1
0
(cid:6)

i

1
=

0
*
1
0

(cid:4)
(cid:2)
(cid:2)
(cid:2)
(cid:3)

M

U
D

(6c)

This three-regime model contains a ‘normal’ mean-reverting regime M, an ‘up’-regime U and

a ‘down’-regime D. The down-regime always immediately follows after the up-regime (see
the 1* in the Markov transition matrix) and forces prices back to ‘normal’ levels. Similarly,

7

the normal regime always immediately follows the down regime (see the 1** in the Markov

transition matrix). This specification avoids that the mean-reversion parameter has to be set

arbitrarily large to move spikes back to normal levels. Nevertheless, the model’s major

drawback is that it does not allow for multiple consecutive spikes, which are frequently

observed in electricity markets (see Figure 2) and crucial for risk management purposes and

derivative valuation: it is unrealistic to assume that an up-spike is always directly followed by

a down-spike and a normal price.

Geman and Roncoroni (2004) therefore come up with a different solution. Their

model is also combination of a mean-reverting process and a jump process.

dx

t

=

(
ma

-

x

t

)
1 se
+
t
-

+

(
xh

t

1
-

)

(cid:215)

J

t

h
t

=

(
xh

t

1
-

)

=

(cid:10)
(cid:9)
(cid:8)

+

1

-

1

if

if

x

t
x

G<=

1
-

G>

t

1
-

(7a)

(7b)

Jumps are characterized by their time of occurrence, their size and their sign. The jump sizes

are modeled as increments of a compound jump process. The jump sign (ht) is assumed to be

positive when the spot price is below some threshold level (cid:5) and negative otherwise. This

barrier for the jump sign plays a central role. First, it allows for both upward and downward

jumps. Second, the jump-sign specification makes the sign stochastic (contrasting e.g.

Escribano et al., 2002). Furthermore, the time-dependence is more realistic than the forced

downward jump directly after an upward jump in Deng (1999) and Huisman and Mahieu

(2001), because it admits a series of consecutive extreme price spikes.

Although this time-dependent specification is attractive, it has one major drawback,

which is the deterministic nature of the jump probability and sign. In fact, the time-

dependence is still quite limited, because the switch from upward to downward signs is

abrupt, whereas we prefer the sign to be probabilistic. This is possible with a regime-

specification that inherits the nice features of the Roncoroni-Geman model. Then we have two

states: one with a low expected price and one with a high expected price. We furthermore

assume that the second regime may have a right-skewed distribution; therefore we model the

error term again as Poisson jumps. The switch from low to high price regimes is comparable

to model 4, but without the requirement that prices directly move back after an upward spike.

The similarity with model 3 (regime switch model with Poisson jumps) is also apparent. In

fact, the only difference is that the prices in the second regime now revert back to a higher

level. The data will have to determine whether this is more realistic than a constant mean-

reverting level or not.

8

Model 5 – regime switches with exponential Poisson up and down jumps:

regime M:

dx

t

(
ma
5
5

=

-

x

t

1
-

)

+

es
5
t

regime S:

dx

t

=

S
mma
5
5

+

5

(

-

x

t

)
- +
1

n

t(cid:1)

i

=

0

Z

t

with

Z

t
n

Markov transition matrix:

=P
5

(cid:7)
1
(cid:5)
(cid:6)

S
p
-
5
M
p
5

S
p
5
M
-
p
5

(cid:4)
(cid:2)
(cid:3)

1

~

~

t

N

(
S
S
,
sm
5
5
(
)5
POI
l

(8a)

)

 (8b)

(8c)

In this model, although price returns are independent in the two regimes, price levels

are dependent on previous price levels. We would like to investigate whether it isn’t more

logical to assume that spikes are truly abnormal events, completely independent from other

price levels. For example, if there is a generator outage, prices may be high for some time

period, but once the generator is repaired, prices may continue as normal. Therefore, we

investigate a model with two independent regimes: a ‘normal’ mean-reverting regime and a

single spike regime. Again we assume a compound Poisson process for the spikes, which

eases comparison with the previous models. This is a generalization of the regime-switch

model proposed by De Jong and Huisman (2003), which relies on normally distributed spikes,

and permits more extreme spikes. It might seem surprising that we omit an explicit downward

price movement as in Deng (1999), Huisman and Mahieu (2001) or Geman and Roncoroni

(2004). However, the model does not need a regime to pull prices down to normal levels,

because it is assumed that price levels in the two regimes are independent from each other.

Consequently, the sharp price changes result from the move from the one regime to the other

rather than from an explicitly formulated price return.

Model 6 – Regime switches with independent spikes:

mean-reverting regime M:

dx

M
t

(
ma
6
6

=

-

x

M
1
t
-

)

+

es
6
t

spike regime S:

S
x
t

=

m
6

+

Z

,
it

+

n

t(cid:1)

i

=

0

Z

,
it

with

~

~

N

(
S
S
,
sm
6
6
(
)6
POI
l

)

Z

,
it
n
t

Markov transition matrix:

=P
6

(cid:7)
1
(cid:5)
(cid:6)

S
p
-
6
M
p
6

S
p
6
M
-
p
6

(cid:4)
(cid:2)
(cid:3)

1

(9a)

(9b)

(9c)

The independence of the regimes is exemplified by the exclusion of any common price in the

specification: the mean-reverting price  Mx does not play a role in the specification of the spike

9

price

Sx  and vice versa. This means that there are always two processes, even though only

one is observed at a time. Whether this total independence assumption is realistic, will be

verified later by comparing the model fit with those of models 3 and 5 in a number of

European and US spot markets.

2.3  Parameter estimation

All the models can be calibrated through maximization of the likelihood function. We

describe the derivation of the likelihood function for the most complex regime-switch model

6 with independent spikes. The loglikelihood of the other models can then be derived, either

as special cases or on the basis of other straightforward adaptations.

The likelihood of a regime-switch and a jump model is the weighted average of the

likelihood of the price process in each regime (or state), conditioned on that regime. The

weights are equal to the prior probability that the process is in the particular regime. In a

standard jump model the prior probabilities are constant and equal to the jump intensity. In a

regime-switch model, the prior probabilities are updated after each price realization

depending on the transition probabilities and the relative sizes of the previous likelihoods. It is

therefore necessary to define both a prior probability (

priorr ) and posterior probability

posterior

(

r

). The likelihood

L

( )
q

( )(cid:213)=
tL
q

t

 under parameter set (cid:1) can then be determined as

follows (with subscript r indicating the regime):

(cid:1)

prior
t

posterior
1(cid:1)
= -
t

P(cid:215)

r

prior
,
tr

(cid:215)

L

(cid:1)

r

L

,
tr

( )
q
,
tr
( )
q

prior
r
,
tr

(cid:215)

L

,
tr

( )
q

r

posterior
,
tr

=

L
t

( )
q

=

(cid:1)

r

          (10a)

          (10b)

          (10c)

The updating of the weights directly shows the difference of a regime-switching model

compared to a stochastic jump model. In fact, a jump model is a special regime-switch model

with fixed weights.

We can derive the likelihoods of the various regime-switch models by calculating the

likelihoods conditioned on the regimes. We assumed that jump sizes from all models are

10

compound normals. As a result, we use the normal density and plug in the error term, which is

the difference between observed price (xt) and conditionally expected price.

Of the likelihoods for the two regimes of model 6, the one of the spike regime,

( )qS
tL

,

is the easier to derive and independent of the previous price realizations. Combining the

density of the normal distribution with the Poisson arrival process yields:

S
L
t

( )
q

¥

= (cid:1)

i

1
=

1
i
l
-
-
l
)
!1
-

e
(
i

exp

x

t

(cid:10)
(cid:11)
(cid:9)
(cid:11)(cid:8)

-

(cid:20)
(cid:18)
(cid:18)
(cid:19)

--

S
i
mm
S

2
i
s

2
i
sp

S

2

(cid:17)
(cid:15)
(cid:15)
(cid:16)

(cid:14)
(cid:11)
(cid:13)
(cid:11)(cid:12)

(11)

Model 6 is taken as an example, because its mean-reverting likelihood is rather complex due

to the assumption of independent spikes in combination with the mean-reversion of the first

regime. More particularly, in the mean-reverting loglikelihood for model 6, the conditional

mean depends on the mean-reverting price of the previous period, which is latent if the

previous period was a spike. This means that if prices were in a spike yesterday, we do not

know from what level they have to revert today (if today is a ‘normal’ period). The

conditional likelihood for the mean-reverting regime depends on the last observed mean-

reverting price. We therefore define the event that on day t the last mean-reverting price was i

periods back with qt = i (so prices j =1,…, i-1 periods back were spikes) and obtain the mean-
reverting likelihood5 for the model with independent spikes:

M
L
t

( )
q

=

¥

(cid:1)

i

1
=

M
L
t

(
q

|

q
t

)
i
(cid:215)=

Pr

[
q
t

=

]

i

          (12a)

ln

M
L
t

(
q

|

q
t

)
-==

i

(
M
x
t

-
2
Var

[
M
xE
t
[
M
x
t

|

X
X

t

|

t

-

-

i

2

]
)
,
q
i
]
,
q

-

1
2

ln

Var

[
M
x
t

|

X

t

-

i

]
,
q

-

1
2

2ln

p

          (12b)

If we look i periods back, in the likelihood equation we use the conditional expectation and

the conditional (higher) variance of the log spot price. These expected values and variances

can be determined recursively as follows:

[
M
xE
t

|

X

t

-

i

Var

[
M
x
t

|

X

t

(
1
-+

]
,
amq
=
M
(
]
(
,
1
1
-+=
q

-

i

)
a
(cid:215)
)
(cid:215)

2

)
a

[
M
xE
1
t
-

|

X

t

-

i

Var

[
M
x
1
t
-

|

X

]q
,
]q
,

-

i

t

          (13a)

          (13b)

5 In the calculation of Equation (11) we limit the summation to ten past periods, because the sum of the posterior
probabilities then approaches 1 very closely in our data.

11

and

[
M
xE
t
i
+-

|1

X

t

-

i

and

Var

[
M
x
i
t
+-

1 |

X

t

]
,
amq
=
M
]
2
s=-
i
M

(
1
-+

a

) M
x
t

-

i

          (13c)

          (13d)

The likelihood of the whole process equals the weighted sum of the likelihoods of the two

regimes. The weights are determined by each regime's prior probability as defined in Equation

(10a). This completes the specification and calibration of the complex mean-reverting regime
model with independent spikes.

3  Data

We collected hourly spot data from six European and two US electricity markets

where data was readily available or easy to obtain: Nord Pool Elspot (Scandinavia), EEX

(Germany), APX (Netherlands), Powernext (France), EXAA (Austria), OMEL (Spain), PJM

(US), and New England Pool (US). These data cover the most liquid markets in Europe,

where our sample includes some 36% (Table 1) of total generating capacity, and two major
markets in the US, including the largest6. The well-known Palo Verde (US), California

Oregon Border (US) and British UKPX markets are not included, because data is not freely

available, and because the UKPX is an hour-ahead instead of a day-ahead market. Several

other markets (Italian Mercato Elettrico, Slovenian Borzen, Romanian Opcom, Polish Gielda)

are excluded, because liquidity is too low or the available history is too short.

[INSERT TABLE 1 APPROXIMATELY HERE]

We use price data up to March 2004. Powernext data starts in January 2002 and

EXAA data starts in April 2002; in the other six markets data start in January 2001. In

modeling power spot prices it is customary to aggregate the hourly prices into baseload

(equally weighted average of the 24 hours) and peakload (equally weighted average of the

hours with the largest load). Peak hours generally run from around 7:00 or 8:00 in the

morning to 20:00 or 23:00 in the evening, depending on the working hours, climate and

culture where the power exchange is located. Figures 1a-d show the baseload price

developments. In the figures, the prices are capped to 100 € /MWh or 100 $/MWh to keep

them readable, but the high volatility, mean-reversion and spikes prominently appear

nonetheless.

6 PJM covers a huge control area with the states of Delaware, Illinois, Indiana, Kentucky, Maryland, Michigan,
New Jersey, Ohio, Pennsylvania, Tennessee, Virginia, West Virginia and the District of Columbia.

12

[INSERT FIGURE 1 APPROXIMATELY HERE]

[INSERT TABLE 2 APPROXIMATELY HERE]

Table 2 shows an overview of the baseload price characteristics. We report

distributional statistics of the natural logarithm of spot price instead of the spot price itself,

because the price models are expressed in natural logarithms as well, and because the third

and fourth moment of the price levels are very unstable. Taking natural logarithms of prices

puts a heavy weight on a few very low prices, a common problem in modeling electricity

prices, so we decided to replace prices below 7.50 with 7.50 (0.3% of the sample). Still

however, both the log prices and log returns are clearly non-normally distributed, as shown by

the levels of skewness and excess kurtosis often far away from zero. The maximum log prices

and returns provide further evidence for this non-normality: the maximum log prices and

logreturns are a multiple of 4 to 12 of the standard deviation, far larger than the factor of

around 3.3 that the normal distribution suggests.

These extreme right tails of spot price levels are a way to describe the spikes, our

primary subject of interest. Right tail behavior of the log returns is studied in more detail in

Figure 2, where we compare the observed frequency of returns exceeding 100% with the

corresponding normal probability: the normal distribution suggests a far lower frequency than

we actually observe.

[INSERT FIGURE 2 APPROXIMATELY HERE]

Peakload characteristics are similar, but even more extreme, so we just report a few

facts. Average peakload prices are between 14 and 26% higher than baseload prices. Standard

deviations are slightly higher for baseload log prices and log returns, but skewness and

kurtosis are on a similar level. The spikes of peak prices are however more pronounced: the

maximum is often twice as high for the peakload price than for the baseload price and tail

frequencies are generally higher. Since peakload prices are economically important and

exhibit even more pronounced spikes, we include them in our analysis.

[INSERT FIGURE 3 APPROXIMATELY HERE]

13

Integration between electricity markets is an explicit goal for the European Union.

Integration is a result of similar seasonal developments in demand, cross-border transport and

similar developments in fuel costs. The German EEX, Dutch APX and French Powernext are

clearly integrated, with correlations in log price levels all above 70%. So are the two

neighboring US markets, with a correlation of 69% (Figure 3). In Europe the prices of EXAA

in Austria, OMEL in Spain and Nord Pool in Scandinavia show less correlation with other

markets. This can be explained both by their geographical location, on average further away
from the other markets, and the larger share of hydropower supply7. These three markets have

large hydro shares, ranging from 29% for Spain, and 51% for Scandinavia, to even 66% for

Austria (Table 3). Hydro shares in the two US markets under consideration are very low:
below 4% in NEPOOL and below 10% in PJM8.

Though the markets have a high volatility and seasonality in common, differences can

be large. The Scandinavian Nord Pool market, liberalized since the early 90’s contains hydro

supply of over 50%, predominantly located in Norway. Nord Pool exhibits extreme price

levels, but less extreme returns, with the standard deviation of returns lowest overall (10%).

This is a consequence of the abundance of hydro stations, capable of easily adjusting

production in the short term, but not so well in the long term. The Winter of 2002-2003, when

low reservoir levels and a cold Winter pushed prices above the 100 € /MWh bar for more than

a week, serves as a prominent example. Quite similar price behavior is observed in the

Spanish market (OMEL), where hydro is also a major energy source (29%). Most extreme

price behavior is observed in the Dutch APX market, with both the highest absolute price

level (660 € /MWh) and the highest change in price level on a single day (354%: on 11 August

2003 prices moved from 19 to 660, stayed high for two more days, then went back to 51

€ /MWh). Not surprisingly, the Dutch market has no reservoir-hydro power itself, nor any

significant hydro nearby. Although with largely different types of power stations (much

coal/lignite-fired power in Germany, much nuclear power in France) the EEX and Powernext

do not differ much from the Dutch APX. It is probably primarily their larger size and

proximity to hydropower in neighboring countries that helps to dampen the largest spikes. In

Europe, at first sight, the Austrian EXAA does not fit well into the picture: despite its

significant hydro share (66%), it still exhibits large daily fluctuations, similar in size to

Germany and France. However, the Austrian market is closely linked with neighboring

7 Hydropower serves as a buffer to dampen price shocks and availability is very dependent on local weather
conditions.
8 US capacity data could only be found on the level of federal region, administered by the Energy Information
Administration (www.eia.doe.gov). Of the 10 US federal regions, region 1 exactly corresponds to the NEPOOL
market. However, the PJM market is an incomplete combination of regions 2 to 5. Since regions 3 and 5 cover
most of PJM, we took the average of these regions for estimating the hydro share in PJM (Table 1).

14

countries such as Germany, so its national flexibility is often used to help out these other

countries. The two northeastern US markets, PJM and New England Pool, exhibit comparable

and rather extreme behavior in price levels and price returns.

The division in baseload, peakload and off-peak prices reflects part of the seasonality

during a day, but prices also exhibit considerable seasonality during a week. In general, prices

(and electricity consumption) are lowest on Sundays, but sometimes also slightly lower on

Wednesdays or Saturdays. We incorporate this feature in our price models with dummies for

Sundays (including public holidays), Saturdays and Wednesdays. Another feature we include

in the trend part of the price models (Equation 1) is the seasonality over the year. A first

indication that this can be quite pronounced is the negative correlation in log price levels

between the Spanish market and those of Nord Pool and the two northeastern US markets. In

Spain, electricity demand and price levels are highest in Summer, when temperatures are high

and air-conditioners working hard. In the other three markets, the demand pattern follows a

different cycle, mainly because of heating demand in cold Winters. After some

experimentation and to avoid overfitting, we include just one sinusoidal function in the

periodic part of the price models, characterized by a location and a size parameter. This leads

to the following specification for the trend, which is estimated jointly with the parameters of

the stochastic part of the price process:

( )
tf

=

ff
+
1

0

Sun

t

+

f
2

Sat

t

+

Wed
j
3

t

+

f
4

sin

(cid:20)
(cid:18)
f
5
(cid:19)

2
t
p
(cid:215)
25.365

(cid:17)
(cid:15)
(cid:16)

(14)

The model does not include inflation. This could easily be accounted for by adding a linear

factor, but in our data there is no support for systematically increasing or decreasing prices, so

we refrain from doing so.

15

4  Empirical results

Overall, we have a diverse sample of market structures and market prices. In this

section we will try to find out how this shows up in the model calibrations. In particular, we

will analyze the spikes and measure the level of independence of the spikes from the other

prices.

4.1  Estimation results

The parameter estimates and loglikelihoods are displayed in Tables 3-5 for baseload and

peakload prices. We discuss baseload estimates below in detail and note that the

characteristics of the peakload estimates are very similar.

Are the jump models any good?

In this paper we specified a mean-reverting model (1) and extended it with Poisson-normal

jumps (2) and four different regime-switch specifications. A natural contester of jump

specifications are (G)ARCH specifications, of which the GARCH(1,1) is most popular. As a

starter we therefore need to see how well GARCH(1,1) volatility dynamics capture the

variations in the spot electricity prices. At first, the likelihood ratio tests, based on the

maximized loglikelihoods (Table 3) show that the GARCH(1,1) is a worthwhile replacement

of the constant variance assumption. With values between 27 and more than 500, the

likelihood ratio test statistic is far above the 1% critical value of 11.34, so the constant

variance assumption can be rejected. Nevertheless, replacing the GARCH(1,1) with normally

or Poisson-normally distributed jumps (model 2) yields an even much higher likelihood in

each and every market, with an equal number of parameters. Apparently, the variance in

prices changes not so gradually as GARCH models assume, but rather abruptly, as the jump

and regime-switch models assume. This result justifies the choice for jump and regime

models in this paper, rather tan (G)ARCH-type models.

Do the regime-switch models perform better than jump models?

Our second concern is to establish whether the regime-switch models better capture the

dynamics of spot electricity prices than jump models. Therefore, we compare them to the

jump-model 2, which can be considered a special case of and nested in regime-switch model

3, as we argued earlier. Again, the results leave little room for doubt (Table 3): the likelihood

ratio test statistics are between 29 and 199 in 7 out of 8 markets (1% critical value is 6.63).

16

Only in the PJM market, the test statistic is rather low, corresponding to a p-value of just

above 5%. Maybe with one exception, the seemingly small adjustment of dynamic switching

probability pays off well, at the cost of only one extra parameter. Furthermore, the regime-

switch specification allows for more subtle alternatives that we analyze in turn.

What regime-switch model is best?

All regime-switch models under analysis have one regime with mean-reverting prices to

capture the price dynamics under ‘normal’ market circumstances. The differences are in the

spike specification and particularly in the way the model switches from spikes to ‘normal’

prices. On average, it appears that the very similar models 3 and 5 yield the best model fit.

They achieve almost identical loglikelihoods that are highest in all markets except OMEL,

where the independent spikes do slightly better. Of course, the maximization of the model fit

should not be the only criteria to judge a model. In this paper, we are also very much

concerned how the spikes are estimated: are they clearly different from the normal prices and

how often do they occur?

The spikes

From the time-series graphs we noticed already that prices on the APX and EEX exhibit the

clearest upward spikes. In the regime-switch models their expectations (Table 5) can be

calculated as (cid:6)S*(1+(cid:7)). This statistic constitutes the difference of the log price in the spike

regime with the mean-reverting regime. It is on average equal to 0.24 on the APX and 0.04 on

the EEX. The other markets show either economically insignificant spikes or, in the case of

OMEL, PJM, EXAA and Nordpool, even negative spikes. Since three of these four markets

(PJM is the exception) have a large share of hydropower (Table 1), we are inclined to think

that this leads to stronger downward adjustments of prices than of upward adjustment of

prices. Stated differently, with hydropower it is relatively easy to increase production in the

short term and this may account for the negative spikes.

In several markets one cannot even truly speak of spikes, because they occur with a high

frequency on average: 47% for EXAA, 36% for PJM and 31% for OMEL.  However, some

models are more successful than others in separating spikes from the other prices. Model 4

(with the 3 regimes) and model 6 (with independent spikes) assign a low probability of 11-

14% to spikes on average. Correspondingly, the expected absolute size of the spikes (in log

terms) in these two models is largest as well. Especially model 6 with independent spikes

successfully separates the size of spikes from the size of the mean-reverting prices: the

17

absolute difference is 0.34 compared to a difference for the other models in the range of 0.05-

0.09.

Of the 4 regime-switch models, the ones with the worst fit on average, model 4 and 6 (Table

3); are at the same time the models that separate the spikes most clearly from the mean-

reverting price process. So, there seems to be a trade-off between the goal to optimize model

fit and the goal to identify spikes clearly by imposing some logical restrictions. It should be

noted that additional restrictions may also yield lower spike frequencies in model 5 (high and

low price regime). Actually, this model builds on the model of Geman and Roncoroni (2004),

which defines the threshold for spikes ex ante. Whereas we let the data implicitly determine

the level of the threshold, an ex ante defined threshold can be raised arbitrarily high to yield a

lower number of spikes (high prices).

What are the differences between the markets?

The differences between the markets that we observed in the time-series graphs (Figure 1) and

the tail behavior graphs (Figure 2) show up in the parameter estimates. The Dutch APX

market exhibits the most pronounced upward jumps: the average jump size is rather large and

jumps occur infrequently. On the larger EEX it is much harder to clearly distinguish upward

spikes in all specifications. The spikes do however have high volatility and thus merely seem

to account for volatility varying (abruptly) over time. The two US markets, PJM and New

England, also have a relatively low share (below 10%) of hydropower. Yet, these markets

have no exceptional spikes and the spikes can even be negative in some model specifications,

just as in the markets with large shares of hydro power (Powernext, EXAA, OMEL and Nord

Pool). One possible reason is that the demand side of the markets is more price-responsive in

the United States than in Europe. This in turn may relate to the fact that these markets have

been liberalized longer ago and customers (primarily large industrial end users) are more

accustomed to reducing their demand in periods of high prices, thus avoiding extreme spikes.

Another possible reason is that the two US markets have a supply side that is more flexible

than appears from the share of hydropower, either because there are connections to

hydropower in neighboring regions or because there is more flexibility in the other generation

capacity. Finally, a possible reason is that these markets work more efficiently, meaning that

information is incorporated in the prices more quickly and that there is more competition

between the suppliers, making it more difficult to change very high prices at any time.

[INSERT TABLE 3-5 APPROXIMATELY HERE OR ELSEWHERE IN CHAPTER 4]

18

5  Concluding remarks

This paper presents a convincing case for the use of regime-switch models to describe power

spot prices. The models under analysis had a limited number of parameters, but were

nevertheless able to capture the price dynamics significantly better than a GARCH and a

jump-model. The regime-switch model that closely resembles a jump model yield the best

model fit, but other specifications may be desirable to better separate spikes from the rest of

the prices. This depends on the type of application.

The models for daily power baseload and peakload described in this paper may be used in

various risk management and valuation applications in energy markets. However, other

applications in these areas require models that describe power prices up to the (half-)hourly

frequency or relate the dynamics in the spot prices to those in the forward market. Further

research is needed to establish how regime-switch models could be applied in those areas as

well.

19

6  References

Bessembinder, H. and M.L. Lemmon, 2002, “Equilibrium pricing and optimal hedging in

electricity forward markets”, Journal of Finance, 57, p. 1347-1382

Kholodnyi, V.A., 2003,  “A non-Markovian process for power prices with spikes and

valuation of European contingent claims on power”, Research and Analytics Group TXU Energy

Trading

Bhanot, K., 2000, “Behavior of power prices: implications for the valuation and hedging of

financial contracts”, Journal of Risk, 2:3, p. 43-62

Bjerksund, P., Rasmussen, H. and G. Stensland, 2000, “Valuation and risk management in the

Norwegian electricity market”, discussion paper 20/200, Norwegian School of Economics and

Business Administration

Clewlow, L. and C. Strickland, 1999, “Valuing energy options in a one factor model fitted to

forward prices”, working paper, University of Sydney

Deng, S., 2000, “Stochastic models of energy commodity prices and their applications: mean

reversion with jumps and spikes”, working paper, University of California Energy Institute

Escribano, A., J.I. Pena and P. Villaplana, 2002, “Modeling electricity prices: international

evidence”, working paper, Universidad Carlos III de Madrid

Fleten, S.E. and J. Lemming, “Constructing forward prices in electricity markets”, working

paper, Riso National Laboratory Denmark

Geman, H. and A. Roncoroni, 2004, “Understanding the fine structure of electricity prices”,

Journal of Business (forthcoming)

Hamilton, J.D., 1989, “A new approach to the economic analysis of non-stationary time series

and the business cycle”, Econometrica, 57, p. 357-384

Hamilton, J.D., 1994, “Time Series Analysis”, Princeton University Press

Harvey, A.C., 1989, “Forecasting, structural time series and the Kalman filter”, Cambridge

University Press, Cambridge

Hilliard, J.E. and J. Reis, 1998, “Valuation of commodity futures and options under stochastic

convenience yields, interest rates, and jump diffusions in the spot”, Journal of Financial and

Quantitative Analysis, 33:1, p. 61-86

Huisman, R. and R. Mahieu, 2001, “Regime jumps in power prices”, Energy & Power Risk

Management, September

Johnson and Barz, 1999, “Selecting stochastic processes for modeling electricity prices”,

Energy Modeling and the Management of Uncertainty, Risk Publications

Kaminski, V., 1997, “The challenge of pricing and risk managing electricity derivatives”, The

US Power Market, p. 149-171, Risk Publications

Knittel, C.R. and M. Roberts, 2001, “An empirical examination of deregulated electricity

prices”, working paper, University of California Energy Institute

20

Koekebakker, S. and F. Ollmar, 2001, “Forward curve dynamics in the Nordic electricity

market”, working paper, Agder University College, Denmark

Longstaff, F.A. and E.S. Schwartz, 2001, “Valuing American options by simulation: a simple

least-square approach”, Review of Financial Studies, 14:1, p. 113-147

Longstaff, F.A., P. Santa-Clara and E.S. Schwartz, 2001, “Throwing away a billion dollars:

the cost of sub-optimal exercise strategies in the swaption market”, Journal of Financial Economics,

62:1, p. 39-66

Lucia, J. and E.S. Schwartz, 2002, “Electricity prices and power derivatives: evidence from

the Nordic Power Exchange”, Review of Derivatives Research 5, p. 5-50

Merton, R.C., 1976, “Option pricing when underlying stock returns are discontinuous”,

Journal of Financial Economics 3, p. 224-244

Miltersen, K. and E.S. Schwartz, 1998, “Pricing of options on commodity futures with

stochastic term structures of convenience yields and interest rates”, Journal of Financial and

Quantitative Analysis, 33:1, p. 33-59

Pilipovic, D., 1998, “Energy risk: valuing and managing energy derivatives”, McGraw Hill,

New York

Pindyck, R.S., 1999, “The long-run evolution of energy prices”, The Energy Journal, 20:2

Pirrong, C. and M. Jermakyan, 1999, “Valuing Power and Weather Derivatives on a Mesh

Using Finite Difference Methods”, Energy Modeling and the Management of Uncertainty, Risk Books

Pirrong, C. and M. Jermakyan, 2000, “The price of power: The valuation of power and

weather derivatives”, working paper, Washinton University

Ramezani, C.A. and Y. Zeng, 2004, “An empirical assessment of the double exponential

jump-diffusion process”, working paper, California Polytechnic

Schwartz, E.S., 1997, “The stochastic behavior of commodity prices: implications for

valuation and hedging”, Journal of Finance 52:3, p. 923-973

21

Tables and figures:

Exchange

Capacity

Fossil fuel

Nuclear

Hydro

Share of hydro

Netherlands
Germany
France
Spain
Austria
Nord Pool
New England
PJM

APX
EEX
Powernext
OMEL
EXAA
Nord Pool
NEPOOL
PJM*

20,965
126,531
116,380
63,819
17,842
90,672
6,866
82,040

19,251
79,533
26,920
31,098
5,971
24,810
2,463
62,302

449
20,643
63,400
7,581
0
12,112
3,968
15,169

37
9,895
25,110
18,241
11,729
46,451
249
4,261

0.2%
7.8%
21.6%
28.6%
65.7%
51.2%
3.6%
5.2%

Table 1: Generation capacity in MW. 2003 numbers for Europe (Source: Eurelectric - Union of the European
electric industry) and 2000 numbers for the US (Source: EIA – Energy Information Administration). Apart from
total capacity, the table displays fossil-fuel fired capacity (oil, gas, coal, lignite), nuclear capacity and hydro
capacity (run of river, reservoir, pump-hydro). Other generation forms than these three major categories (e.g.
wind, solar) are relatively limited.

22

2
3

A
P
X

,

E
E
X

,

P
o
w
e
r
n
e
x
t
,

O
M
E
L

,

P
J
M

,

N
e
w
E
n
g
l
a
n
d
,

E
X
A
A
a
n
d
N
o
r
d
P
o
o
l
.

F
i
g
u
r
e

1
a
-
d
:

B
a
s
e
l
o
a
d

s
p
o
t

p
r
i
c
e
s

i
n

/

M
W
h
o
r

$
/
M
W
h
(
c
a
p
p
e
d

t
o
1
0
0
)

f
o
r

t
h
e

v
a
r
i
o
u
s
m
a
r
k
e
t
s
u
n
d
e
r

a
n
a
l
y
s
i
s
:

Jan-01

Mar-01

May-01

Jul-01

Sep-01

Nov-01

Jan-02

Mar-02

May-02

Jul-02

Sep-02

Nov-02

Jan-03

Mar-03

May-03

Jul-03

Sep-03

Nov-03

Jan-04

Mar-04

E
X
A
A

N
o
r
d
P
o
o

l

Prices EUR/MWh

P
J
M

N
w
E
n
g

l

Prices USD/MWh

O
M
E
L

P
o
w
e
r
n
e
x
t

Prices EUR/MWh

Prices EUR/MWh

E
E
X

A
P
X

0

1
0

2
0

3
0

4
0

5
0

6
0

7
0

8
0

9
0

1
0
0

0

1
0

2
0

3
0

4
0

5
0

6
0

7
0

8
0

9
0

1
0
0

0

1
0

2
0

3
0

4
0

5
0

6
0

7
0

8
0

9
0

1
0
0

0

1
0

2
0

3
0

4
0

5
0

6
0

7
0

8
0

9
0

1
0
0

Jan-01

Mar-01

May-01

Jul-01

Sep-01

Nov-01

Jan-02

Mar-02

May-02

Jul-02

Sep-02

Nov-02

Jan-03

Mar-03

May-03

Jul-03

Sep-03

Nov-03

Jan-04

Mar-04

Jan-01

Mar-01

May-01

Jul-01

Sep-01

Nov-01

Jan-02

Mar-02

May-02

Jul-02

Sep-02

Nov-02

Jan-03

Mar-03

May-03

Jul-03

Sep-03

Nov-03

Jan-04

Mar-04

Jan-01

Mar-01

May-01

Jul-01

Sep-01

Nov-01

Jan-02

Mar-02

May-02

Jul-02

Sep-02

Nov-02

Jan-03

Mar-03

May-03

Jul-03

Sep-03

Nov-03

Jan-04

Mar-04

€

APX

EEX  Pwrnext  OMEL

PJM  Nw Engl  EXAA  Nord Pl

  start period
  # observ.
  peak hours

Jan-01
1185
8-23

Jan-01
1185
9-20

Jan-02
821
8-20

Jan-01
1185
10-23

Jan-01
1185
8-23

Jan-01  Apr-01
1185
8-22

731
8-20

Jan-01
1185
-

  average
  st.dev.
  skewness
  kurtosis
  maximum

  st.dev.
  skewness
  kurtosis

  maximum

3.41
0.52
1.30
3.96
6.49

0.48
0.77
5.19

3.54

3.17
0.38
0.13
2.52
5.48

0.36
0.98
3.66

2.37

3.16
0.40
-0.01
3.21
5.74

0.36
0.95
6.38

2.78

Log Prices

3.61
0.29
0.00
-0.01
4.74

3.46
0.37
0.62
1.41
5.50

Log Returns
0.23
0.19
0.13
0.62
3.11
1.72

0.83

1.10

3.71
0.35
0.54
3.50
5.91

0.20
-1.19
22.67

1.32

3.23
0.39
-0.20
1.51
5.11

0.37
0.55
2.46

2.17

3.29
0.37
1.00
1.83
5.70

0.10
1.62
28.01

1.19

Table 2: Summary statistics for baseload log spot prices and log returns

24

.

5
4
>
e
c
i
r
p
g
o

l

y
t
i
l
i

b
a
b
o
r
P

Tail behaviour of log prices

5%

4%

3%

2%

1%

0%

APX

EEX Pnext OMEL PJM

Sample

Normal distribution

Nw
Engl

EXAA Nord
Pool

Right tail behaviour of log returns

%
0
0
1
>
n
r
u
t
e
r
y
t
i
l
i

b
a
b
o
r
P

7%

6%

5%

4%

3%

2%

1%

0%

APX

EEX Pnext OMEL PJM

Sample

Normal distribution

Nw
Engl

EXAA Nord
Pool

Figure 2a and 2b: Right tail behavior of log prices and log returns: sample frequency versus normal distribution

25

Baseload

APX
EEX
Pnext
OMEL
PJM
New Engl
EXAA
Nord Pool

APX
1.00
0.43
0.63
0.12
0.04
0.06
0.46
0.17

EEX

Pnext

OMEL

PJM

New Engl

EXAA

Nord Pool

1.00
0.66
0.26
0.23
0.19
0.59
0.20

1.00
0.24
0.16
0.14
0.60
0.12

1.00
-0.24
-0.35
0.24
-0.40

1.00
0.63
0.17
0.17

1.00
0.13
0.29

1.00
-0.01

1.00

Figure 3: Correlations between baseload prices of the various spot markets

GARCH(1,1)

0

MR

1

JD-POI

JD-POI

3 regime

high-low

indep.

2

3

4

5

6

Regime switch

APX

EEX

Powernext

OMEL

PJM

New England

EXAA

Nord Pool

Average

-0.3031

-0.3287

-0.1639

-0.0977

-0.1663

-0.0966

-0.1233

0.1906

0.1306

0.6583

0.1448

0.3812

-0.0303

1.2965

0.1515

0.0658

0.6470

0.1152

0.2788

-0.1611

1.0783

0.2877

0.1987

0.7261

0.1589

0.5190

-0.0278

1.4687

0.3091

0.2167

0.7498

0.1605

0.5680

0.0879

1.5526

0.2910

0.2169

0.7176

0.1458

0.5195

-0.0520

1.3608

0.3089

0.2159

0.7497

0.1596

0.5678

0.0892

1.5526

0.2824

0.1980

0.7605

0.1309

0.5540

0.0119

1.4859

0.3086

0.2309

0.3959

0.4434

0.3792

0.4434

0.4125

Table 3a: Loglikelihoods of the models (described in the text) for baseload prices. The corresponding parameter
estimates are in Table 5a.

GARCH(1,1)

0

MR

1

JD-POI

JD-POI

3 regime

high-low

indep.

2

3

4

5

6

Regime switch

APX

EEX

Powernext

OMEL

PJM

New England

EXAA

Average

-0.3918

0.0224

-0.0474

0.4771

0.0846

0.2931

-0.4213

-0.0152

-0.1143

0.4676

0.0524

0.0958

-0.2477

-0.1789

-0.2645

-0.1774

-0.2076

0.1416

0.0434

0.5631

0.0988

0.3479

0.1696

0.0653

0.5848

0.1001

0.3961

0.1448

0.0613

0.5542

0.0847

0.3442

0.1695

0.0649

0.5846

0.0986

0.3959

0.1438

0.0463

0.6008

0.0902

0.3965

-0.1957

-0.3152

-0.1718

-0.0737

-0.2182

-0.0736

-0.1472

-0.0357

0.1108

0.1519

0.1009

0.1518

0.1318

Table 3b: Loglikelihoods of the models (described in the text) for peakload prices. The corresponding parameter
estimates are in Table 5b.

26

PANEL A:

Probability of a spike

PANEL B:
Expected size of a spike
(log)

PANEL C:
Absolute expected size of
a spike (log)

APX

EEX

Pwrnext

OMEL

PJM

Nw Engl

EXAA

Nord Pl

Average

APX

EEX

Pwrnext

OMEL

PJM

Nw Engl

EXAA

Nord Pl

Average

APX

EEX

Pwrnext

OMEL

PJM

Nw Engl

EXAA

Nord Pl

Average

BASELOAD

PEAKLOAD

JD-POI  3 regime  high-low

indep.

JD-POI  3 regime  high-low

indep.

3

4

5

6

3

4

5

6

39%

17%

27%

39%

52%

29%

61%

25%

10%

5%

11%

10%

13%

5%

32%

4%

40%

17%

27%

39%

59%

29%

62%

25%

19%

4%

7%

12%

4%

8%

43%

16%

44%

22%

25%

45%

50%

37%

44%

10%

5%

10%

12%

13%

7%

35%

46%

22%

26%

44%

61%

38%

39%

20%

10%

11%

12%

13%

12%

45%

36%

11%

37%

14%

38%

13%

39%

18%

0.166

0.025

-0.028

0.221

0.014

0.046

0.247

0.051

-0.018

0.861

0.177

0.171

0.218

0.046

-0.017

0.274

0.023

0.013

0.308

0.075

-0.001

0.754

0.403

0.233

-0.009

-0.015

-0.015

-0.169

-0.012

-0.010

-0.015

-0.237

0.099

-0.116

0.112

-0.339

0.109

-0.121

0.114

-0.516

-0.010

-0.060

0.002

0.122

0.098

0.045

-0.023

0.112

-0.010

-0.085

-0.540

0.054

0.162

0.099

-0.018

0.304

0.068

-0.440

0.017

-0.354

0.023

0.052

0.036

-0.010

0.055

0.063

0.076

0.072

0.166

0.025

0.028

0.009

0.099

0.010

0.060

0.002

0.221

0.014

0.046

0.015

0.116

0.122

0.098

0.045

0.247

0.051

0.018

0.015

0.112

0.023

0.085

0.017

0.861

0.177

0.171

0.169

0.339

0.112

0.540

0.354

0.218

0.046

0.017

0.012

0.109

0.010

0.054

0.274

0.023

0.013

0.010

0.121

0.162

0.099

0.308

0.075

0.001

0.015

0.114

0.018

0.068

0.754

0.403

0.233

0.237

0.516

0.304

0.440

0.050

0.085

0.071

0.340

0.066

0.100

0.086

0.412

Table 4: Characteristics of the spikes in the regime-switch models, as described in the text. The
probability of a spike (panel A) is the unconditional probability that the process is in the spike regime.
The expected size of a spike panel B) is the difference of the expected log price in the spike regime
compared to the ‘normal’ mean-reverting regime. Panel C contains the absolute value of the numbers
in panel B.

27

APX

EEX

Powernext

OMEL

PJM

Nw England

EXAA

Nord Pool

(cid:8)
(cid:6)
(cid:1)
(cid:6)S
(cid:1)S
(cid:7)
(cid:4)S
(cid:4)M
(cid:8)
(cid:6)
(cid:1)
(cid:6)S
(cid:1)S
(cid:7)
(cid:4)S
(cid:4)M
(cid:8)

(cid:6)

(cid:1)

(cid:6)S

(cid:1)S

(cid:7)

(cid:4)S

(cid:4)M

(cid:8)
(cid:6)
(cid:1)
(cid:6)S
(cid:1)S
(cid:7)
(cid:4)S
(cid:4)M
(cid:8)
(cid:6)
(cid:1)
(cid:6)S
(cid:1)S
(cid:7)
(cid:4)S
(cid:4)M
(cid:8)
(cid:6)
(cid:1)
(cid:6)S
(cid:1)S
(cid:7)
(cid:4)S
(cid:4)M
(cid:8)
(cid:6)
(cid:1)
(cid:6)S
(cid:1)S
(cid:7)
(cid:4)S
(cid:4)M
(cid:8)
(cid:6)

MR

JD-POI

JD-POI

3 regime

high-low

Independ.

Regime-switch

1
0.3773
3.5607
0.3361

0.3038
3.2960
0.2080

0.3171
3.2791
0.2266

0.1451
3.6840
0.1267

0.1889
3.4469
0.2156

0.1581
3.7285
0.1831

0.3883
3.2900
0.2843

0.0259
3.3302

2
0.4432
3.3688
0.1535
0.1195
0.3584
0.7068
0.3481

0.2801
3.2844
0.1451
0.0133
0.3953
0.3045
0.1002

0.2913
3.2917
0.1372
-0.0189
0.2990
0.5548
0.2154

0.1082
3.7627
0.0521
-0.0094
0.1182
0.6481
0.5670

0.1284
3.0354
0.1187
0.0937
0.2281
0.1336
0.4972

0.0828
3.7592
0.0909
-0.0075
0.2499
0.7557
0.2083

0.4364
3.4107
0.1207
-0.0950
0.4348
0.0001
0.3653

0.0058
2.9151

3
0.4078
3.3634
0.1462
0.0964
0.3658
0.7214
0.0785
0.1226

0.2594
3.2712
0.1401
0.0142
0.2817
0.7924
0.0318
0.1571

0.2795
3.2947
0.1303
-0.0182
0.2932
0.5397
0.1126
0.3043

0.1040
3.7162
0.0708
-0.0057
0.1436
0.6234
0.1015
0.1562

0.1349
3.0718
0.1173
0.0878
0.2523
0.1227
0.4091
0.3806

0.0772
3.7639
0.0841
-0.0056
0.2227
0.7481
0.0653
0.1605

0.3925
3.4482
0.0892
-0.0257
0.2467
1.3366
0.0281
0.0183

0.0085
3.3156

28

4
0.3233
3.4521
0.2012
0.2023
0.6281
0.0901
0.1004

0.2725
3.2778
0.1503
0.0077
0.3779
0.7986
0.0457

0.2916
3.2822
0.1398
0.0299
0.3396
0.5381
0.1141

0.1159
3.6883
0.0900
-0.0093
0.1896
0.6115
0.1021

0.1535
3.4087
0.1689
-0.1015
0.2989
0.1437
0.1296

0.0950
3.7561
0.1148
0.0697
0.3599
0.7507
0.0467

0.4489
3.3749
0.1400
0.0405
0.2706
1.4122
0.3194

0.0117
3.0994

5
0.4064
3.3637
0.1446
0.1411
0.3525
0.7539
0.0784
0.1155

0.2593
3.2708
0.1399
0.0285
0.2804
0.7880
0.0324
0.1572

0.2791
3.2886
0.1304
-0.0121
0.2956
0.5234
0.1133
0.3059

0.1038
3.7107
0.0715
-0.0092
0.1449
0.6104
0.0976
0.1548

0.1312
3.0600
0.1142
0.0321
0.1359
2.5022
0.4469
0.3108

0.0772
3.7637
0.0841
-0.0132
0.2225
0.7464
0.0654
0.1594

0.3917
3.4486
0.0893
-0.0352
0.2410
1.4235
0.0260
0.0162

0.0085
3.3185

6
0.2968
3.4261
0.1759
0.6321
0.6588
0.3625
0.0592
0.2556

0.2182
3.2926
0.1561
0.1150
0.7407
0.5381
0.0274
0.6095

0.1989
3.2629
0.1608
0.1113
0.6600
0.5381
0.0463
0.6243

0.0610
3.6967
0.0854
-0.1046
0.2206
0.6115
0.0660
0.4824

0.1567
3.4728
0.1990
-0.2967
0.1918
0.1437
0.0234
0.5492

0.0642
3.7158
0.1037
0.0639
0.6534
0.7507
0.0410
0.4518

0.1358
3.4750
0.1026
-0.2237
0.4653
1.4122
0.0160
0.0212

0.0048
3.5507

(cid:1)
(cid:6)S
(cid:1)S
(cid:7)
(cid:4)S
(cid:4)M

0.0823

0.0324
0.0114
0.1461
0.1308
0.1955

0.0304
0.0009
0.1054
0.7687
0.0485
0.1449

0.0499
0.0246
0.1663
0.8437
0.0406

0.0304
0.0094
0.1053
0.7576
0.0488
0.1443

0.0410
-0.3542
0.2715
0.0000
0.0750
0.3819

Table 5a: Parameter estimates for baseload prices of the models as described in the text. The
corresponding loglikelihoods are in Table 3.

MR

1

0.3930

3.7797

0.3687

0.3726

3.5249

0.2457

0.3774

3.5068

0.2713

0.191

3.829

0.152

0.2028

3.6152

0.2296

APX

EEX

Powernext

OMEL

PJM

(cid:8)

(cid:6)

(cid:1)
(cid:6)S
(cid:1)S

(cid:7)
(cid:4)S
(cid:4)M

(cid:8)

(cid:6)

(cid:1)
(cid:6)S
(cid:1)S

(cid:7)
(cid:4)S
(cid:4)M

(cid:8)

(cid:6)

(cid:1)
(cid:6)S
(cid:1)S

(cid:7)
(cid:4)S
(cid:4)M

(cid:8)

(cid:6)

(cid:1)
(cid:6)S
(cid:1)S

(cid:7)
(cid:4)S
(cid:4)M

(cid:8)

(cid:6)

(cid:1)
(cid:6)S
(cid:1)S

(cid:7)
(cid:4)S
(cid:4)M

Nw England  (cid:8)
(cid:6)

0.2229

3.8651

JD-POI

JD-POI

3 regime

high-low

Independ.

Regime-switch

2

0.5112

3.5301

0.1559

0.1574

0.3633

0.8002

0.3762

0.3457

3.4989

0.1640

0.0404

0.4739

0.2809

0.1073

0.3526

3.5077

0.1618

3

0.4603

3.5212

0.1396

0.1218

0.3686

0.7876

0.1003

0.1261

0.3296

3.4828

0.1513

0.0258

0.3103

0.7878

0.0370

0.1341

0.3368

3.5012

0.1505

-0.0217

-0.0103

0.4426

0.2833

0.1775

0.133

3.884

0.062

-0.008

0.139

0.880

0.520

0.1341

3.2029

0.1250

0.0954

0.2420

0.1685

0.4937

0.1210

3.8996

0.3550

0.6599

0.0926

0.2730

0.126

3.868

0.072

-0.006

0.156

0.875

0.173

0.215

0.1367

3.2150

0.1244

0.0962

0.2705

0.1318

0.4319

0.4262

0.1032

3.8946

29

4

0.3449

3.6525

0.2218

0.2537

0.6749

0.0798

0.1025

0.3385

3.4990

0.1692

0.0129

0.4417

0.7857

0.0523

0.3353

3.4962

0.1637

0.0079

0.4269

0.6627

0.0983

0.145

3.831

0.101

-0.005

0.211

0.863

0.118

0.1617

3.5808

0.1795

-0.1037

0.3142

0.1682

0.1309

0.1259

3.8810

5

0.4602

3.5225

0.1386

0.1725

0.3620

0.7838

0.0998

0.1183

0.3302

3.4843

0.1509

0.0422

0.3080

0.7879

0.0373

0.1318

0.3391

3.4972

0.1497

-0.0004

0.3530

0.6600

0.0958

0.2745

0.125

3.862

0.072

-0.008

0.157

0.874

0.171

0.215

0.1393

3.2416

0.1179

0.0340

0.1470

2.3646

0.4768

0.3053

0.1025

3.8945

6

0.3415

3.6176

0.1916

0.6984

0.6811

0.0798

0.0564

0.2235

0.2849

3.5006

0.1650

0.2257

0.6903

0.7857

0.0245

0.2199

0.2242

3.4758

0.1698

0.1404

0.7371

0.6627

0.0587

0.4897

0.078

3.843

0.094

-0.127

0.293

0.863

0.094

0.663

0.1813

3.6718

0.2263

-0.4413

0.1255

0.1682

0.0064

0.0416

0.0771

3.8296

EXAA

(cid:1)
(cid:6)S
(cid:1)S

(cid:7)
(cid:4)S
(cid:4)M

(cid:8)

(cid:6)

(cid:1)
(cid:6)S
(cid:1)S

(cid:7)
(cid:4)S
(cid:4)M

0.2198

0.4318

3.5105

-0.3316

0.1013

-0.0115

0.2967

0.7145

0.2325

0.3584

3.6115

0.0816

-0.0157

0.4021

0.2974

0.5449

0.0874

-0.0059

0.2452

0.7111

0.0797

0.1353

0.3978

3.5287

0.4559

0.0337

0.0846

0.5958

0.0159

0.0206

0.1282

0.0959

0.3835

0.6910

0.0668

0.4721

3.5777

0.1658

0.0461

0.3260

1.1483

0.3469

0.0870

-0.0107

0.2434

0.7161

0.0804

0.1316

0.3954

3.5568

0.4557

0.0427

0.0837

0.5917

0.0145

0.0223

0.1095

0.1797

0.6273

0.6910

0.0669

0.5099

0.1910

3.7088

0.1119

-0.2209

0.5333

0.9900

0.0318

0.0391

Table 5b: Parameter estimates for peakload prices of the models as described in the text. The
corresponding loglikelihoods are in Table 3.

30

Publications in the Report Series Research∗ in Management

ERIM Research Program: “Finance and Accounting”

2005

Royal Ahold:  A Failure Of Corporate Governance
Abe De Jong, Douglas V. Dejong, Gerard Mertens en Peter Roosenboom
ERS-2005-002-F&A
http://hdl.handle.net/1765/1863

Capital Structure Policies in Europe: Survey Evidence
Dirk Brounen, Abe de Jong and Kees Koedijk
ERS-2005-005-F&A
http://hdl.handle.net/1765/1923

A Comparison of Single Factor Markov-Functional and Multi Factor Market Models
Raoul Pietersz, Antoon A. J. Pelsser
ERS-2005-008-F&A
http://hdl.handle.net/1765/1930

Efficient Rank Reduction of Correlation Matrices
Igor Grubišić and Raoul Pietersz
ERS-2005-009-F&A
http://hdl.handle.net/1765/1933

Generic Market Models
Raoul Pietersz and Marcel van Regenmortel
ERS-2005-010-F&A
http://hdl.handle.net/1765/1907

The price of power: valuing the controlling position of owner-managers in french ipo firms
Peter Roosenboom and Willem Schramade
ERS-2005-011-F&A
http://hdl.handle.net/1765/1921

The Success of Stock Selection Strategies in Emerging Markets: Is it Risk or Behavioral Bias?
Jaap van der Hart, Gerben de Zwart and Dick van Dijk
ERS-2005-012-F&A
http://hdl.handle.net/1765/1922

Sustainable Rangeland Management Using a Multi-Fuzzy Model: How to Deal with Heterogeneous Experts’ Knowledge
Hossein Azadi, Mansour Shahvali, Jan van den Berg and Nezamodin Faghih
ERS-2005-016-F&A
http://hdl.handle.net/1765/1934

A Test for Mean-Variance Efficiency of a given Portfolio under Restrictions
Thierry Post
ERS-2005-032-F&A
http://hdl.handle.net/1765/6729

Testing for Stochastic Dominance Efficiency
Oliver Linton, Thierry Post and Yoon-Jae Whang
ERS-2005-033-F&A
http://hdl.handle.net/1765/6726

Wanted: A Test for FSD Optimality of a Given Portfolio
Thierry Post
ERS-2005-034-F&A
http://hdl.handle.net/1765/6727

How Domestic is the Fama and French Three-Factor Model? An Application to the Euro Area
Gerard A. Moerman
ERS-2005-035-F&A
http://hdl.handle.net/1765/6626

Bond underwriting fees and keiretsu affiliation in Japan
Abe de Jong, Peter Roosenboom and Willem Schramade
ERS-2005-038-F&A
http://hdl.handle.net/1765/6725

Sourcing of Internal Auditing: An Empirical Study
Roland F. Speklé, Hilco J. van Elten and Anne-Marie Kruis
ERS-2005-046-F&A
http://hdl.handle.net/1765/6891

The Nature of Power Spikes: a regime-switch approach
Cyriel de Jong
ERS-2005-052-F&A

‘New’ Performance Measures: Determinants of Their Use and Their Impact on Performance
Frank H.M. Verbeeten
ERS-2005-054-F&A

∗   A complete overview of the ERIM Report Series Research in Management:

https://ep.eur.nl/handle/1765/1

ERIM Research Programs:
LIS  Business Processes, Logistics and Information Systems

  ORG Organizing for Performance
  MKT  Marketing

F&A  Finance and Accounting
STR  Strategy and Entrepreneurship

