Glas et al. Journal of Mathematics in Industry            (2020) 10:3
https://doi.org/10.1186/s13362-020-0071-x

R E S E A R C H

Open Access

Intraday renewable electricity trading:
advanced modeling and numerical
optimal control

Silke Glas1, Rüdiger Kiesel2, Sven Kolkmann3, Marcel Kremer2, Nikolaus Graf von Luckner2, Lars Ostmeier3,
Karsten Urban4*

and Christoph Weber3

*Correspondence:
karsten.urban@uni-ulm.de
4Institute for Numerical
Mathematics, Ulm University, Ulm,
Germany
Full list of author information is
available at the end of the article

Abstract
As an extension of (Progress in industrial mathematics at ECMI 2018, pp. 469–475,
2019), this paper is concerned with a new mathematical model for intraday electricity
trading involving both renewable and conventional generation. The model allows to
incorporate market data e.g. for half-spread and immediate price impact. The optimal
trading and generation strategy of an agent is derived as the viscosity solution of a
second-order Hamilton–Jacobi–Bellman (HJB) equation for which no closed-form
solution can be given. We construct a numerical approximation allowing us to use
continuous input data. Numerical results for a portfolio consisting of three
conventional units and wind power are provided.

MSC: 49L99; 65K10; 91G80

Keywords: Intraday trading; Hamilton–Jacobi–Bellman equation; Numerical
optimization

1 Introduction

To counter global climate change, renewable power sources substituted fossil fuel plants

and provide now a substantial part of the electricity production. Due to the intermittency

of renewable power, short-term electricity contracts have gained importance on electric-
ity exchanges such as the European Power Exchange (EPEX Spota). In particular, contin-
uous intraday trading, which allows trading of contracts until 30 minutes before delivery,
is used to respond to short-term changes. The trading volume within the German intra-
day market (IDM) area increased from 26 TWh in 2014 to more than 50 TWh in 2018.

A similar trend has been observed in other market areas or countries in which some mar-

kets or sub segments, e.g., continuous trading of hourly products in Belgium (since July

2018) or the 30-min continuous trading in Germany and France (since April 2017), have

been developed. Another instrument for integrating renewable energy markets is the Xbid

project, which aims at establishing a common pan-European continuous intraday market

to strengthen liquidity. All these developments trigger a need for mathematical modeling

© The Author(s) 2020. This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use,
sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original
author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other
third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line
to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by
statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a
copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

Glas et al. Journal of Mathematics in Industry            (2020) 10:3

Page 2 of 17

of such trading as a basis for deeper understanding, optimization and control. Moreover,
a mathematical model is the basis for numerical simulations.

However, in contrast to day-ahead market (DAM) modeling, literature dedicated to the
continuous intraday electricity markets is scarce. In particular, appropriate mathematical
models describing the main characteristics of these short-term markets have not been de-
veloped so far. Most important price drivers have been identiﬁed in [10] explaining about
75% of the price variance, [20]. Moreover, strong statistical evidence was found that infor-
mation on the speciﬁc fundamental factors signiﬁcantly aﬀect the intraday prices, which
appear as transaction prices within a trading period, [13, 14].

Concerning mathematical modeling early work in the ﬁeld of integration of renewables
into short-term markets using stochastic optimization can be found in [18]. The mini-
mization of incurred intraday costs of wind producers while maintaining the balance of
production forecast and sales is considered in [11]. This short-term trading model also
considers the impact of the wind producer on prices without intraday price uncertainty,
however. A discrete time decision model with intraday prices following a geometric Brow-
nian model and wind production error forecast following an arithmetic Brownian motion
has been introduced in [7, 8]. In that framework, the power producer is supposed to have
no impact on intraday prices.

To overcome the aforementioned weaknesses, we have been inspired by [1] to model
the continuous intraday market for electricity. In [1], a Hamilton–Jacobi–Bellman (HJB)
equation was derived for determining an optimal trading strategy by modeling the dynam-
ics of the electricity market by stochastic diﬀerential equations (SDEs) and formulating a
corresponding value function to be optimized. The speciﬁc market model allows one to
solve the arising HJB analytically, i.e., the authors derive a solution formula.

The starting point of this paper (which builds upon and extends [9]) is a statistical anal-
ysis of EPEX SPOT data, which shows that some of the model assumptions in [1] are in
fact not satisﬁed under real market conditions. Thus, we introduce a more sophisticated
model. The arising HJB equation can no longer be solved analytically; the value function
is shown to be the unique viscosity solution of this HJB equation. Thus, we need an appro-
priate numerical scheme. From an economical point of view, the main new ingredients of
our model are:

1. Portfolio of renewable and conventional energy represented by a cost function that
reﬂects the stepwise merit order of a portfolio rather than a systemwide quadratic
function;

2. Pricing model using time-varying half-spread and being capable of representing

time-varying liquidity;

3. Approximation of market data for half-spread and instantaneous price impact;
4. Variable penalty depending on the state of the market at ﬁnal time;
5. The model relies on data which are observable on the market (see Sect. 3).
The main focus of this paper is a novel application-related modeling of the intraday
trading and the determination of a numerical approximation for this problem. We show
an example of a real-world problem, compute the optimal trading strategy and investigate
the impact of various involved parameters. The remainder of this paper is as follows: In
Sect. 2, we introduce the new model and the arising HJB equation and Sect. 3 details the
involved parameters, which we obtained from empirical analyses. In Sect. 4, we describe
the numerical method for determining the viscosity solution of the arising HJB. More-

Glas et al. Journal of Mathematics in Industry            (2020) 10:3

Page 3 of 17

over, we present corresponding numerical experiments. We ﬁnish by conclusions and an
outlook in Sect. 5.

2 A new mathematical model
In order to take both renewable and conventional generation into account, our model is
based upon the consideration of an agent owning both kinds of power plants and aiming
at selling a combination of renewableb and conventionally produced electricity. In detail,
depending on the weather forecast and the expected price at the ﬁnal time, such a combi-
nation of electricity is sold at the day-ahead market (DAM). With the result of this initial
trading, the agent starts to act on the continuous intraday trading market (IDM) aiming
at maximizing her proﬁt by determining an optimal trading strategy as well as an op-
timal production strategy of conventional power.c All quantities entering the model are
described below.

2.1 Day-ahead and intraday electricity trading
Consider a delivery hour h on day d. The day before, d – 1, the day-ahead auction takes
place with gate closure at 12 noon. In this auction, each participant can oﬀer (ask) or
request (bid) a certain demand of electricity at a speciﬁc price. Then, a clearing price is
set and power is exchanged accordingly. Next, the continuous intraday trading starts at
3 p.m. on day d – 1 and closes half an hour before the actual delivery hour h, see Fig. 1.

2.2 Dynamics of the electricity market
The dynamics of the market includes the forecasted renewable power production and the
price process. The latter one is inﬂuenced by the current trading activity of the agent. We
use stochastic processes and derive stochastic diﬀerential equations (SDEs), see [19] for
background.

2.2.1 Renewable production forecast
By D = (Dt)0≤t≤T we denote the forecasted production of renewable produced electricity
during the trading session. Following the idea of [15, 22], we assume that forecast updates
are a consequence of new information and hence lead to random changes in t. Therefore,
the uncertainty is modeled by means of the dynamics

dDt = σD dWt,D,

(1)

where σD is the volatility and (Wt,D)0≤t≤T is a standard Brownian motion. For the sake
of simplicity, this variable is unbounded, whereas in the real world, there are restrictions

Figure 1 Scheme of continuous intraday trading

Glas et al. Journal of Mathematics in Industry            (2020) 10:3

Page 4 of 17

by zero (no wind) and the maximum capacity of the wind farm. We denote by Dt,d the
solution of the SDE starting from d (the current capacity) at t.

2.2.2 Agent’s position
The ﬁnancial position resulting from the agent’s trading activity is denoted by X =
(Xt)0≤t≤T . The agent participates in the intraday market (IDM) with continuous trading
at rate qt ∈ Q := (qmin, qmax) ⊂ R, where qt > 0 implies actively buying and qt < 0 implies
actively selling.d The dynamics of her ﬁnancial position are then

dXt = qt dt

(2)

and we denote by Xq;t,x the solution of the SDE starting from x at t depending on the
current trading rate qt. For t = 0, x0 is the amount of electricity sold on the day-ahead
market.

2.2.3 Permanently impacted mid price
First, we denote by Y = (Yt)0≤t≤T the permanently impacted mid price, i.e., the sum of
the mid price of energy and the permanent impact of the agent’s trading, the latter one
modeled by some function ψ : R → R. The dynamics of Y is modeled by the SDE

(cid:2)
μY + ψ(qt)

(cid:3)

dYt =

dt + σY dWt,Y ,

(3)

where μY is the drift, σY is the volatility and (Wt,Y )0≤t≤T is a standard Brownian motion.
We denote by Y q;t,y the solution of the SDE starting from y at time t depending on qt.

2.2.4 Transaction costs
When actively buying (selling) on the IDM, there are costs in addition to the permanent
impact. Those are referred to as transaction costs and will be incorporated in our model.

2.2.5 Execution price
The execution price is the price the agent pays (receives) when actively buying (selling). We
require a more advanced approach of the pricing model as in [1], where the half-spread
(see below) and its time variability as well as the time variability of the execution costs are
ignored. Incorporating these eﬀects, the execution price depends on several quantities to
be introduced now.

The half-spread is deﬁned as the half of diﬀerence of the best ask and the best bid price.
This data is observable on the market. While in reality the bid-ask spread and hence also
the half-spread is stochastic, we model it in terms of a deterministic function h : [0, T] →
R+, which reﬂects the typical shape over the trading period.

The other component of our model for the execution price is the execution cost reﬂect-
ing the costs that are incurred due do executing limit orders with prices worse than the
best price when buying (selling) actively. While they are also stochastic in reality, they
will be described in terms of a deterministic function ϕ : [0, T] × (qmin, qmax) → R which
reﬂects the typical shape over the trading period.

With all these quantities at hand, the execution price Pq;t,y = (Pq;t,y

s

)0≤s≤T is modeled as

Pq;t,y
s

:= Y q;t,y
s

+ sign(qs)h(s) + ϕ(t, qs),

(4)

Glas et al. Journal of Mathematics in Industry            (2020) 10:3

Page 5 of 17

where (as usual)
⎧
⎨

sign(qs) :=

|qs|
qs
0,

,

if qs (cid:6)= 0,

otherwise.

⎩

Hence, (4) means that the execution price is the permanently impacted mid price plus
(minus) the time-varying half-spread and plus the time-varying execution costs, which
extends the model in [1].

2.3 The proﬁt: the objective function for optimization
It is the aim of the agent to maximize her proﬁt consisting of the running and the ter-
minal proﬁt explained next. This will later serve as the objective function for the arising
optimization problem.

2.3.1 Running proﬁt
The total running proﬁt from the continuous trading in the intraday market is given by

f q(s; t, y) := –qsPq;t,y

s

with the trading rate q = (qt)0≤t≤T .

(5)

2.3.2 Terminal proﬁt
The proﬁt gained at the end of the trading period consists of scheduling conventional
power production which incurs costs and placing a ﬁnal market order.

and maximum generation capacity κ max

Conventionally produced energy At the end of the trading session, the agent chooses
how much electricity ξ ∈ R+
0 she will produce during the delivery period. For doing so,
she has n conventional units available with each being able to operate between their spe-
ciﬁc minimum κ min
, i = 1, . . . , n. The marginal
costs ci of unit i, i.e., the costs for producing 1 MWh of electricity, are assumed to be
time-independent (constant). The chosen strategy of the agent thus consists of deciding
to activate or deactivate unit i (modeled by a binary variable ai ∈ {0, 1}) and choosing the
respective amount ξi ∈ [κ min
] for each unit. Thus, the resulting amount of produced
electricity is

, κ max
i

i

i

i

n(cid:7)

ξ =

aiξi.

i=1

(6)

A straightforward strategy would be that the agent will activate her units in ascending
order of marginal costs, starting with the ‘cheapest’ one. The arising total cost of power
production then reads

C : R+
0

→ R+

0 , C(ξ ) =

n(cid:7)

i=1

aiciξi,

(7)

which is a piecewise linear but discontinuous function, the derivative of which is a sum of
piecewise constants and a number of Delta distributions.

Glas et al. Journal of Mathematics in Industry            (2020) 10:3

Page 6 of 17

Final market order Furthermore, the agent also has the option to place a ﬁnal buy or sell
market order. In fact, obtaining values for DT , XT and YT , the agent optimally tries to reach
her desired demand for power by buying/selling the amount ξ + XT + DT ∈ R, i.e., what
has been traded already minus conventional and renewable production, by a ﬁnal market
order. The costs associated with the ﬁnal market order are the costs due to crossing the
half-spread h(T) and the costs due to potentially executing limit orders with prices worse
than the best bid/ask price. The latter costs are modeled by the function α : R → R.

Terminal payoﬀ It turns out to be convenient to introduce the variable Zt := Xt + Dt,
i.e., the sum of the forecasted production from renewables and what has been sold by the
agent so far. This, in particular reduces the dimension of the optimization problem to be
solved numerically, which is crucial for eﬃciency. The terminal payoﬀ/proﬁt then reads

g(ξ , YT , ZT ) := –C(ξ ) + (ξ + ZT )

(cid:2)
YT – sign(ξ + ZT )h(T) + α(ξ + ZT )

(cid:3)
.

(8)

2.4 The resulting optimization problem
Now, we have all ingredients at hand to formulate the optimization problem in terms of a
HJB equation.

2.4.1 Value function
The value function corresponds to the agent’s cash, so that an optimal strategy yields max-
imal cash. Denoting by Zq;t,z the solution of the SDE dZt = dDt + dXt = qt dt + σD dWt,D
starting from z at t, the resulting value function V : [0, T] × U → R reads for Q :=
(qmin, qmax), see, e.g. [24, Ch. 4],

V (t, y, z) :=

E

sup
(q,ξ )∈Q×R

(cid:8)(cid:9)

T

t

f q(s; t, y) ds + g

(cid:2)

ξ , Y q;t,y
T

, Zq;t,z
T

(cid:10)
(cid:3)

,

(9)

where U := Y × Z ⊂ R2 is a closed convex set (usually a rectangle, in order to ensure well-
posedness of the optimization in (9), [6]). In fact, from our above modeling, we would ob-
tain Y = Z = R (range of values for the execution price and energy production). However,
without additional conditions, the optimization problem is not well-posed on such un-
bounded domains. Moreover, the numerical solution using standard discretization tech-
niques is—at least—not straightforward on unbounded domains and would require so-
phisticated schemes, see e.g. [12].

In order to overcome these diﬃculties, we deﬁne U in terms of closed sets (intervals) Y
and Z and cut-oﬀ the problem on their boundaries. This requires to set boundary condi-
tions to ensure well-posedness to be explained below.

2.4.2 The Hamilton–Jacobi–Bellman (HJB) equation
Following the well-known dynamic programming principle (e.g. [24, Ch. 4]), we derive the
HJB equation: Find V : [0, T] × U → R, V = V (t, y, z), such that

1
∂tV + μY ∂yV +
2
(cid:2)
(cid:11)
–

+ sup
q(t)∈Q

σ 2
Y ∂yyV +

(cid:2)

y + sign

q(t)

1
σ 2
D∂zzV
2
(cid:3)
h(t) + ϕ

(cid:2)
t, q(t)

(cid:3)(cid:3)

q(t) + q(t)∂zV + ψ

(cid:2)
q(t)

(cid:3)
∂yV

(cid:12)

= 0,

(10)

Glas et al. Journal of Mathematics in Industry            (2020) 10:3

Page 7 of 17

for (t, y, z) ∈ [0, T) × U with terminal condition V (T, y, z) = g(T, y, z) for all (y, z) ∈ U . Note,
that in (10) we used the notation q(t) instead of the previously used qt for the following
reason: In the numerical realization, we treat q as a function q(t) and not as stochastic
process qt.

One can show that (10) with terminal and Dirichlet boundary conditions is well-posed
and that the unique viscosity solution is the value function in (9), [5]. Due to the form of
(10), we cannot expect a ﬁrst-order condition for the control q and we have to resort to
numerical solvers.

2.4.3 Boundary conditions
As already mentioned above, we need to truncate the HJB to a bounded domain U , which
requires to prescribe appropriate boundary conditions on ∂U . Such an approach is well-
known also from numerical option pricing when solving the Black–Scholes (BS) equation.
In that case, the deﬁnition of corresponding Dirichlet boundary conditions is canonical
since small errors in the boundary values cause only small errors in the solution on all of
U (i.e., the BS equation is stable w.r.t. boundary values). The situation for the HJB equa-
tion is fundamentally diﬀerent as small changes in the Dirichlet data immediately severely
change the solution on the whole domain. Hence, the deﬁnition of appropriate boundary
conditions is a delicate task.

We are going to describe our approach to prescribe appropriate boundary conditions.
Our point of departure is the before-mentioned IDM-model in [1], which uses a much
simpler HJB as the one derived above. This causes the fact that the HJB in [1] allows for a
closed formula for the solution. We consider such a somehow simpler HJB, solve it explic-
itly and use the boundary values of that HJB as Dirichlet data for our more sophisticated
HJB. Of course, one could also use other simpliﬁed models as long as the resulting bound-
ary conditions turn out to be meaningful. To be speciﬁc, we consider a simpler HJB model
consisting of the following ingredients and simpliﬁcations:

1. By omitting the sign-part in (10) and replacing it by the positive sign, the function

within the supremum is diﬀerentiable.

2. We replace h(t) by ¯h := h(T), i.e., the half-spread at the terminal time.
3. The next simpliﬁcation concerns the temporary price impact ϕ. The most simple
situation would be a linear approximation, e.g., ϕ(t, q) := kq, i.e., stationary and
linear in q. Here, k ∈ R+ is a constant, which has been derived by approximating our
mid price data with a second order polynomial p and then setting k := p(T).

4. The permanent price impact vanishes, i.e., ψ ≡ 0.

Thus, the simpliﬁed HJB now takes the form

∂tv + μY ∂yv +

σ 2
Y
2

∂yyv +

σ 2
D
2

(cid:11)
–(y + ¯h + kq)q + q∂zv

∂zzv + sup
q∈Q

(cid:12)

= 0.

(11)

In (11), we can explicitly determine the supremum by ﬁnding the root of the ﬁrst-order
derivative w.r.t. q of the term in {· · · }. The corresponding ﬁrst-order necessary conditions
yield the optimal control as follows (recall from 3. that k > 0)

∗

q

=

–y – ¯h + ∂zv
2k

.

Glas et al. Journal of Mathematics in Industry            (2020) 10:3

Page 8 of 17

Inserting this optimal control into (11) yields the following PDE for the unknown v as a
function of (t, y, z)

∂tv + μY ∂yv +

σ 2
Y
2

∂yyv +

σ 2
D
2

∂zzv +

1
4k

(y + ¯h – ∂zv)2 = 0.

(12)

To solve (12), we make the following polynomial ansatz

v(t, y, z) =

(cid:7)

|i|≤2

ai(T – t)yi1 zi2 ,

i = (i1, i2), i1, i2 ∈ N0, |i| := i1 + i2,

i.e., a polynomial of degree 2 with the coeﬃcient functions ai : [0, T] → R to be deter-
mined. Plugging this form of v into (12) yields a system of six Riccati equations for the
unknown functions ai, i.e.,

˙a02(T – t) –

˙a20(T – t) –

˙a11(T – t) +

1
4k
1
4k
1
k

(cid:2)

–2a02(T – t)

(cid:3)

2

= 0,

(cid:2)

(cid:3)
–a11(T – t) + 1

2

= 0,

a02(T – t)

(cid:3)
(cid:2)
–a11(T – t) + 1

= 0,

˙a01(T – t) + μY a11(T – t) –

˙a10(T – t) + μY a20(T – t) –

1
k
1
2k

a02(T – t)

(cid:2)
h – a01(T – t)

(cid:3)

= 0,

(cid:2)

(cid:3)(cid:2)

(cid:3)

–a11(T – t) + 1

h – a01(T – t)

= 0,

˙a00(T – t) + μY a10(T – t) + σ 2

Y a20(T – t) + σ 2

Za02(T – t) –

h – a01(T – t)

(cid:3)
2

= 0.

(cid:2)

1
4k

In order to solve this system of ordinary diﬀerential equations, we need initial conditions
for the functions ai. Due to the arguments (T – t) in all those functions, the desired initial
conditions boil down to terminal conditions of v, i.e., the function g in (8). Recall, that g
in particular contains the function C in (7), which is piecewise polynomial but discontin-
uous (see, e.g. Fig. 6 for an example of such a function—clearly exhibiting jumps), which
prohibits a closed form solution of the Riccati system. Thus, we use a least squares approx-
imation of g in terms of the above polynomial v(T, y, z). Doing so, we obtain initial values
for the above mentioned functions, say ai(0) = ai,0. With these values at hand, we solve the
initial-value problem of the Riccati system by Maple™ and obtain v. The boundary values
of v w.r.t. the variables y and z are then used as Dirichlet conditions for (10).

3 Data
Our model described above relies on several parameters, which we summarize in Table 1.
In this section, we describe how this data can be obtained from market observations and
empirical data analysis.

3.1 Generation portfolio
As mentioned before, the agent’s portfolio consists of renewable and conventional gener-
ation capacity. We describe how to retrieve realistic market data.

Glas et al. Journal of Mathematics in Industry            (2020) 10:3

Page 9 of 17

Table 1 Parameters involved in our model

Wind energy Dt

Conventional units

Prices Yt, Pt
Payoﬀ g
Proﬁt f
Value function V

, κ max
i

σD
D0
n
ci
κ min
i
μY
σY
ψ
Y0
h
ϕ
α

Volatility
Initial value

Number of agent’s conventional units
Marginal costs of conventional units, i = 1, . . . , n
Minimal/maximal capacity of units i = 1, . . . , n

Drift of permanently impacted mid price
Volatility of permanently impacted mid price
Permanent price impact of agent’s trading
Initial value
Half-spread function
Execution cost function
Penalty function

Table 2 Unit Parameters for the conventional units i = 1, 2, 3, n = 3

Marginal cost
Minimal capacity
Maximal capacity

ci
κ min
i
κ max
i

Unit

[e/MWh]
[MW]
[MW]

Hard coal
i = 1

25
250
500

CCGT
i = 2

35
100
400

OCGT
i = 3

60
60
600

3.1.1 Renewable electricity standard (RES) portfolio
We equip the sample agent’s portfolio with 500 MW of aggregated renewable generation
capacity. As mentioned before, for the sake of simplicity and due to limited availability of
historical data, we restrict the aggregated capacity to arise solely from wind farms. Fur-
thermore, following [17], we assume that the wind farms in the portfolio are dissimilarly
located within the considered hypothetical market area. This last assumption allows us to
estimate the parameter σD for Dt in (1) using aggregated forecast data, which is, in contrast
to site-speciﬁc data, publicly available.

Speciﬁcally, we choose hourly wind power forecasts for the French market area provided
by [21]. To be able to transfer the characteristics of the historical data set to our current
application, we ﬁrst normalize all forecasts on the average installed capacity per month.
We then determine all updates between two adjacent forecasts of the same forecast path.
Finally, we observe a volatility of approximately 0.01 per installed MW and hour (2016:
0.008, 2017: 0.008, 2018: 0.010) in the data. With respect to the renewable generation ca-
pacity of 500 MW, we therefore set σD = 5 MW.e Finally, we choose D0 also from publicly
available data.

3.1.2 Conventional generation
For the agent’s conventional portfolio, we consider n = 3 units, namely a hard coal ﬁred
plant, a combined cycle gas turbine (CCGT) and an open cycle gas turbine (OCGT), with the
parameters shown in Table 2. The marginal costs ci of each unit represent idealized values
for the respective technology class. They also consider that an increase in ﬂexibility—here
the reduction of the so-called deadband between zero and production at minimal capacity
κ min
i —reduces the eﬃciency of the unit. Moreover, we assume that the start-up decision
ai ∈ {0, 1} of a unit does not require a lead time.

3.2 Mid price drift
We assume that the drift of the mid price on the IDM consists of two parts as implied by
(3), namely mid price changes due to time evolution on one hand and mid price changes

Glas et al. Journal of Mathematics in Industry            (2020) 10:3

Page 10 of 17

Figure 2 Scattering of net order ﬂow (buying minus
selling) versus diﬀerence between volume-weighted
average price on the IDM and price on DAM for all
contracts with delivery start at 12 noon in Q2/2016

due to agent’s trading (causing irreversible price impacts) on the other. Building upon [4],
we perform an empirical analysis of these two parts. In particular, we study price changes
over longer periods of time as well as their relation to net order ﬂow (i.e., buy minus sell).
While in that study mid price changes and net order ﬂow are considered over periods of
ﬁve minutes, we consider the diﬀerences between the day-ahead market (DAM) prices
and volume-weighted average IDM pricesf as well as the net order ﬂow over the entire
trading window. While we conjecture the DAM prices to be close to the mid prices after
market opening, the volume-weighted average IDM prices are usually diﬀerent from the
mid price before end of trading. Nevertheless, we prefer mid prices as we reckon that they
better reveal the evolution of the price over a longer period of time and also mirror the
relation of this evolution to net order ﬂow.

Of course, the observed price changes appear between the beginning and the end of the
IDM trading. As a consequence, the data does not show whether either of the components
typically changes over the trading window. Concerning the (deterministic) dependence of
the price on time, we simply choose a linear dependence, i.e., constant drift as μY (t) ≡ μY .
Next, we assume a linear relation of order ﬂow and price change, which is at least not
contradicted by the scatter plot in Fig. 2. Thus, we assume ψ(qt) = bqt for the permanent
price impact with a constant b ∈ R.

We obtain estimates for b and μY from least squares ﬁts to the data. For b, we get
0.0017e/MWh2 and signiﬁcance at a 0.1% level, indicating that the net order ﬂow has a
positive impact on the price change. The drift μY is obtained as 0.0433e/MWh per hour
and to be signiﬁcant at a 1% level, indicating that the price slightly tends to increase over
time. Concerning the sign of the drift, we ﬁnd mixed evidence in the literature, [10, 14].

3.3 Transaction costs
As we pointed out earlier, it is a major diﬀerence between our model and previous research
that we also include transaction costs. The data analysis on which their modeling is based
is presented below. We recall that transaction costs include execution costs modeled by
the function ϕ and the half-spread h, see (4).

3.3.1 Data
We use order book data from the EPEX SPOT-operated market for hourly delivery con-
tracts with Germany/Austriag as delivery area from the second quarter of 2016 (referred
to as Q2/2016 in the following) to empirically analyze the transaction costs mentioned in
Sect. 2.2. The dataset comprises (i) all orders with Germany or Austria as delivery area
which entered into the order book, (ii) all orders with Germany or Austria as delivery area

Glas et al. Journal of Mathematics in Industry            (2020) 10:3

Page 11 of 17

which caused execution of an order resting in the order book with delivery area other than
Germany or Austria and (iii) all orders with delivery area other than Germany or Austria
which caused execution of an order in the order book with Germany or Austria as delivery
area.

Hence, not all orders in the order book for the German/Austrian delivery area which
were visible for market participants are contained in the dataset. Based upon these data,
we are now going to describe how we obtained values for the quantities entering the trans-
action costs.

3.3.2 Half-spread
In identifying typical half-spread functions h entering the optimization problem, we build
on research on bid-ask spreads (BAS) on the NYSEh stock market. In [16], the pattern of
BAS of NYSE stocks over a trading day is analyzed. To this end, the authors divide each
trading day in their sample into one-minute intervals and compute for each interval and
stock what they refer to as the time-weighted BAS to be explained next. Consider some
time interval Ii := (Ti–1, Ti] ⊂ [0, T] and assume that the BAS changes Ni times at Ti–1 <
t(i)
1 < · · · < t(i)
≤ Ti, where we denote the BAS on (t(i)
j+1) by BASj, j = 0, . . . , Ni setting
Ni
j
0 := Ti–1 and t(i)
t(i)
Ni+1 := Ti. Then, the time-weighted BAS on that interval Ii, denoted by
BASi, is deﬁned as

, t(i)

BASi :=

1
Ti – Ti–1

Ni(cid:7)

j=0

(cid:2)
(cid:2)
min

BASj

t(i)
j+1, Ti

(cid:3)

(cid:2)
– max

t(i)
j

, Ti–1

(cid:3)(cid:3)

.

Then, [16] suggests to determine BASi for each interval of the trading day and for all stocks
in their sample. In this paper, we adopt the approach in [16] and divide the trading period
into intervals of 5-minute length. Furthermore, we only consider the hourly delivery con-
tracts with delivery starting at 12 noon in Q2/2016. The resulting data is visualized in
Fig. 3 as a two-dimensional histogram of all the BASi in the sample for the last 17.5 hours
of trading. The blue line reﬂects the means of the BASi in each interval.

We observe a signiﬁcant decrease of the mean time-weighted BAS from ≈8e to
≈5e/MWh at the beginning of the time window and a subsequent nearly constant be-
havior for about ten hours. Given a tick size of 0.1e/MWh (Q2/2016), it is remarkable
that this plateau is ﬁfty times higher than the tick size. Five hours before the end of the
trading, the mean time-weighted BAS decreases to ≈1e/MWh followed by a sharp in-
crease to reach the ﬁnal ≈2e/MWh. The pattern over the last ﬁve trading hours is quite
similar to the crude reverse J shape reported in [16] for NYSE stocks.

Figure 3 Two-dimensional histogram of 5-minute
time-weighted bid-ask spreads over the last 17.5 hours of
the trading period, means per interval (blue) and
degree-7 polynomial ﬁt (red line) to the data for all
contracts with delivery start at 12 noon in Q2/2016

Glas et al. Journal of Mathematics in Industry            (2020) 10:3

Page 12 of 17

Figure 4 Histogram of the relation between market order volume and execution costs applying a linear
model, dividing the time into 15-minute intervals and the coeﬃcients into intervals of 0.002e/MWh2

In order to model the temporal behavior of the BASi, we employ a polynomial of degree
seven according to the Akaike information criterion (AIC) [2], which is depicted by the
red line in Fig. 3. This polynomial is the half-spread function h mentioned in the previous
section. Clearly, this has a signiﬁcant smoothing eﬀect and could e.g. be replaced by other
approximations as well.

3.3.3 Execution costs
The execution price in (4) depends on the typical half-spread and the typical execution
costs, which reﬂect the negative impact on the price realized by a market participant when
buying or selling with market orders. For the empirical analysis of the execution costs we
need to consider the order book. Similar to the analysis for the half-spread, we start by de-
termining time-weighted prices and volumes over 5-minute intervals on the diﬀerent order
book levels.i Given some time-weighted price on an order book level, it may occur that
the time-weighted price on a lower level is better. Therefore, we sort prices and volumes
in descending/ascending order on the buy/sell side. This approach requires the availabil-
ity of the entire order book over the trading period. Otherwise, missing data techniques
could possibly be used.

We assume a linear relationship between trading rate and execution costs,

ϕ(t, qt) = k(t)qt,

(13)

with the parameter (function) k(t). For estimating k(t), we build upon [4] and analyze how
the order books absorb market orders of diﬀerent sizes. To this end, we consider market
orders with volume 1, . . . , 200 MWh for each interval and market side. Then, we collect
those order book levels required to cover the volume of the market order. We multiply
the order book level prices in that collection by their volumes, sum them up and divide by
the volume of the market order. From the resulting price we subtract the best price on the
same market side to obtain the respective market order’s execution costs. Then, we ﬁt a
linear model by least squares to obtain k(t). Considering again hourly delivery contracts
with delivery start at 12 noon in Q2/2016, Fig. 4 shows the obtained values for k(t) in the
form of two-dimensional histograms as well as means per time interval (blue line).

Similar to the average half-spread, the average execution costs exhibit a decline after
market opening to 0.025–0.05e/MWh2. After a rather stable ≈10 hours period, they fur-
ther decline to ≈0.01e/MWh2. We observe a slight increase just before the end of trading.

Glas et al. Journal of Mathematics in Industry            (2020) 10:3

Page 13 of 17

Hence, the shape of the average execution costs is rather similar to that of the average half-
spread. We model the typical temporal behavior of the execution costs with a polynomial
of degree six for the buy side and degree eleven for the sell side (according to the AIC).

Remark 1 Note that the above approach is not compatible with the model in (13). For
determining a model for the execution costs, we compared market orders and the order
book. However, the agent’s action in our model is trading at some rate. Of course, in reality,
market participants will not act by trading at some rate, but merely actively place market
orders by some strategy. This means, we cannot observe how diﬀerent rates enter the order
book. On the other hand, the above approach is mainly used to calibrate parameters for
our model.

A possible strategy to remedy this shortcoming could be to determine a relation between
execution costs in some time interval and a constant trading rate (instead of the volume
itself ). For example, for execution costs evolving from a 1 MWh market order, a trading
rate of 1/5 MWh per minute would be required to yield that volume after 5 minutes of
trading.

3.3.4 Terminal order book
At the end of the trading period, we assume that the agent liquidates remaining inventory
by means of a ﬁnal market order (instead of letting the volume run into the balancing
market as is done in [1]). This means that we need a typical order book at the end of
trading for calibrating our model.

To this end, we consider the buy and sell side separately and determine for each contract
the diﬀerence between the prices on the diﬀerent order book levels and the best price.
Then, we average all these price diﬀerences and volumes on the same order book level.
The results are shown in Fig. 5.

Given that the average volumes associated with the best bid and ask are around 16 MWh,
typically there is still some volume at the end of trading which can be sold/bought at zero
execution costs. The volumes associated with the order book levels beyond the best-price
level slightly increase. While the average price diﬀerences associated with the best bid
and ask are obviously 0e/MWh, in absolute terms they are ≈1e/MWh for the ﬁrst level,
≈5e/MWh on the ﬁfth level and 20–30e/MWh on the tenth level. Hence, prices beyond
the best level obviously worsen quite substantially.

(cid:10)

≤ 0 (δpsell

We consider both the typical order book on the buy and sell side at the end of trading
to specify the penalty function α. Recall, that δξ := ξ + XT + DT denotes the ‘untraded’
amount (for which a penalty needs to be paid) with ξ being deﬁned by (6). Furthermore,
we only consider the ﬁrst L levels of both the buy and sell order book and truncate the
volume on the last level (L) such that the overall volume is 100 MWh on both market
sides. Let δpbuy
≥ 0) denote the diﬀerence between the price on the (cid:10)-th buy
(sell) order book level and the price on level zero, (cid:10) = 1, . . . , L. Furthermore, let λbuy
, λsell
(cid:10)
be the maximum volume available on respective side of the (cid:10)-th order book level. Then,
α is deﬁned as
⎧
⎪⎪⎪⎨
–
(cid:14)
⎪⎪⎪⎩
0,

buy
(cid:10) max{0,min{λ
δξ
(cid:10) max{0,min{λsell
(cid:10)

if δξ < 0,

if δξ > 0,

α(δξ ) =

L
(cid:10)=1 δpsell

(cid:10)–1
ν=1 λsell
ν

L
(cid:10)=1 δp

else.

(cid:10)–1
ν=1 λ

(14)

δξ ,

buy
(cid:10)

buy
ν

,δξ –

,δξ –

(cid:14)

(cid:14)

(cid:14)

}}

}}

1

(cid:10)

(cid:10)

,

Glas et al. Journal of Mathematics in Industry            (2020) 10:3

Page 14 of 17

Figure 5 Cumulative volume on the diﬀerent levels of the buy (left) and sell (right) order book and diﬀerence
between price on an order book level and best price for all contracts in the sample. The thick red line reﬂects
the mean cumulative volume and price diﬀerence on the diﬀerent order book levels. Plots are cut oﬀ at
cumulative volume of 100 MWh

It is easily seen that α is continuous at δξ = 0. The sign in (14) results from (8) and the
motivation that the penalty α should lower the agent’s proﬁt. This implies that α should
be positive if the agent needs to buy and negative if she needs to sell at the end of the
trading period.

4 Numerical solution of the HJB equation
In this section, we describe our numerical method for (approximately) solving the aris-
ing HJB. Moreover, we report on results of a sample numerical experiment concerning
(10) using the following data: U := [–50, 250] × [–1645, 145] ⊂ R2 and T = 17.5 h arising
from reasonable market data. We have of course validated and tested our implementation
on various other scenarios. Dirichlet boundary conditions are prescribed as described in
Sect. 2.4.

We use a ﬁnite diﬀerence discretization from [23] with 56 × 301 points in space and
100 points in time. In particular, central diﬀerences are used for the approximation of the
ﬁrst-order terms with additional artiﬁcial diﬀusion, which results in a stable, consistent
and monotone scheme converging to the viscosity solution, [23]. We use the well-known
policy iteration [3] in every time-step and the control is maximized over a discrete set
(as no ﬁrst-order conditions are available). Finally, the optimal conventional generation is
computed as the maximum value of (8) w.r.t. ξ using Matlab’sj intlinprog with the interior
point method.

4.1 Data
We use the artiﬁcial data μY := 0.0, σD := σY := 0.1.k The functions ϕ(·, ·) and h(·) are least-
squares 5th order polynomial approximations of market data from Q2/2015 (ψ(t) = 0).
The penalty is chosen as market data as α(x) := 0.5 · (|x| – 20)χ20<|x|≤45 + ((|x| – 45) +
12.5)χ45<|x|≤145.

Our results for the optimal conventional generation ξ are displayed in Fig. 6. Let us
comment on the case where ZT = –500 MWh. As long as the ﬁnal mid price is be-
low 25e/MWh, the agents buys the maximal amount of 145 MWh (recall, that y ∈
[–1645, 145]) and uses the power plant with the lowest marginal costs (hard coal) ac-
cordingly, i.e., the remaining 355 MWh. Once the ﬁnal mid price is 25 to 35e/MWh (i.e.,
above the marginal cost of hard coal, but below the marginal cost of CCGT) it is opti-
mal to produce at maximum capacity with the cheapest conventional power plant (i.e.,

Glas et al. Journal of Mathematics in Industry            (2020) 10:3

Page 15 of 17

Figure 6 Optimal conventional generation ξ as a function of YT and ZT (left) as well as for some values of ZT
(right; the lines correspond to those on the left graph)

Figure 7 Optimal trading rate over the trading window t ∈ [0, 17.5] for Zt ≡ –499.4 MWh and
Yt ≡ 59.25e/MWh (left) as well as Yt ≡ 13.98e/MWh (right)

500 MWh by hard coal) and no ﬁnal market order is required. If the ﬁnal mid price ex-
ceeds 35e/MWh, the agent sells as much electricity as possible (145 MWh) and produces
exactly that amount with the CCGT plant at 35e/MWh, which is possible because its ca-
pacity is 100-400 MW. Finally, no matter how high the ﬁnal mid price is, the OCGT unit
with the highest marginal cost is not used, since there is not enough sell volume on the
market. These results are clearly reasonable.

4.2 Trading rate
Figure 7 shows the optimal trading rate over the trading window t ∈ [0 h, 17.5 h]. In
both cases, we ﬁx Zt ≡ –499.4 MWh (the non-integer numbers arise from the discretiza-
tion w.r.t. y and z). For the mid price, we choose Yt ≡ 59.25e/MWh (left) and Yt ≡
13.98e/MWh (right). In the left plot, the trading rate is negative (selling), which is rea-
sonable since Zt ≡ –499.4 MWh means that the agent has only marketed the cheapest
power plant and Yt ≡ 59.25e/MWh means that the execution price is above the marginal
costs of the second cheapest power plant. Note, that the absolute value of the trading
rate substantially increases around 15 h, since half-spread and immediate price impact
are minimal there. In the right plot, the execution price is below the marginal costs of
the cheapest power plant, the agent buys electricity and reduces the production of the
marketed power plant.

5 Conclusion and outlook
We have introduced an extended model for the intraday market of renewable electric-
ity. As opposed to earlier research, our more sophisticated approach does not allow for a
closed solution formula for the desired optimal trading strategy as a function of time. We

Glas et al. Journal of Mathematics in Industry            (2020) 10:3

Page 16 of 17

thus used a numerical scheme for approximately solving the arising Hamilton–Jacobi–
Bellman (HJB) equation. The parameters within the HJB equation are market data which
we showed to be available by an empirical analysis.

The availability of a numerical approximation scheme allows us now to extend our model
to all market participants, so that regulatory constraints can be determined e.g. for reach-
ing desired environmental goals. Moreover, we will use our scheme to further investigate
optimal strategies within economically particular relevant market scenarios.

Acknowledgements
We are grateful to Constantin Greif (Ulm) for cooperation within AEIT, in particular concerning the numerical simulation.

Funding
This work was funded by the German Federal Ministry for Economic Aﬀairs and Energy within the project Analytics and
Empirics of Intraday Trading of Electricity (AEIT).

List of abbreviations
AIC, Akaike information criterion; BAS, bid-ask spreads; BS, Black–Scholes (equation); CCGT, combined cycle gas turbine
(unit); DAM, day-ahead market; EPEX, European Power Exchange; HJB, Hamilton–Jacobi–Bellman (equation); IDM,
intraday market; NYSE, New York Stock Exchange; OCGT, open cycle gas turbine (unit); PDE, partial diﬀerential equation;
RES, renewable electricity standard; SDE, stochastic diﬀerential equations.

Availability of data and materials
The datasets used and/or analyzed during the current study are available from the corresponding author on reasonable
request.

Competing interests
The authors declare that they have no competing interests.

Authors’ contributions
The empirical analysis for the mathematical model was mainly performed by RK, MK and NL. The construction of the
numerical scheme was done by SG and KU; the coding is due to SG. Economical interpretation was due to NL, SK, LO and
CW. All authors read and approved the ﬁnal manuscript.

Author details
1Department of Computer Science, Cornell University, Ithaca, USA. 2Chair of Energy Trading and Finance, University of
Duisburg-Essen, Essen, Germany. 3Chair for Management Science & Energy Economics, University of Duisburg-Essen,
Essen, Germany. 4Institute for Numerical Mathematics, Ulm University, Ulm, Germany.

Endnotes

a www.epexspot.com
b In our numerical experiments, we consider wind energy.
c Note, that we do not simultaneously optimize day-ahead and intraday trading.
d By actively buying or selling we mean trading with market orders instead of limit orders. A limit order is a type of

order to buy or sell an item at a speciﬁed price or better.

e Note, that the hourly value given above may be adapted to time-wise granularity other than 60 minutes by the use

of the square-root-of-time rule.

f These are transaction prices multiplied with transaction volumes divided by the overall transaction volume.
g Splitting into two separate market areas took eﬀect only in October 2018.
h New York Stock Exchange
i Limit orders contain both price and volume. An order book level is made up by all limit orders on one side of the

market with the same price. The price of a level is the price of the included limit orders and the volume of the level
is the sum over the volumes of corresponding limit orders.

j MathWorks™, mathworks.com
k This is done for visualization purposes; we could of course also have used market data.

Publisher’s Note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional aﬃliations.

Received: 14 October 2019 Accepted: 27 January 2020

References
1. Aïd R, Gruet P, Pham H. An optimal trading problem in intraday electricity markets. Math Financ Econ.

2016;10(1):49–85. https://doi.org/10.1007/s11579-015-0150-8.

Glas et al. Journal of Mathematics in Industry            (2020) 10:3

Page 17 of 17

2. Akaike H. Statistical predictor identiﬁcation. Ann Inst Stat Math. 1970;22:203–17.
3. Bellman R. Dynamic programming. Princeton: Princeton University Press; 1957.
4. Cartea Á, Jaimungal S. Incorporating order-ﬂow into optimal execution. Math Financ Econ. 2016;10(3):339–64.

https://doi.org/10.1007/s11579-016-0162-z.

5. Crandall MG, Lions P-L. On existence and uniqueness of solutions of Hamilton–Jacobi equations. Nonlinear Anal.

1986;10(4):353–70.

6. Fleming WH, Soner HM. Controlled Markov processes and viscosity solutions. 2nd ed. Berlin: Springer; 2006.

(Stochastic modelling and applied probability; vol. 25). ISBN 0-387-26045-5.

7. Garnier E, Madlener R. Balancing forecast errors in continuous-trade intraday markets. Energy Syst. 2015;6(3):361–88.
8. Garnier E, Madlener R. Day-ahead versus intraday valuation of demand-side ﬂexibility for photovoltaic and wind

power systems. FCN working paper 17/2014. 2014. https://doi.org/10.2139/ssrn.2556210.

9. Glas S, Kiesel R, Kolkmann S, Kremer M, Graf von Luckner N, Ostmeier L, Urban K, Weber C. Intraday renewable
electricity trading: advanced modeling and optimal control. In: Faragnó I et al, editors. Progress in industrial
mathematics at ECMI 2018. Berlin: Springer; 2019. p. 469–75. (Mathematics in industry; vol. 30).

10. Hagemann S. Price determinants in the German intraday market for electricity: an empirical analysis. EWL working

paper 18/2013. 2015. https://doi.org/10.2139/ssrn.2352854.

11. Henriot A. Market design with centralized wind power management: handling low-predictability in intraday markets.

Energy J. 2014;35(1):99–117.

12. Kestler S, Urban K. Adaptive wavelet methods on unbounded domains. J Sci Comput. 2012;53(2):342–76.
13. Kiesel R, Kremer M, Paraschiv F. A fundamental model for intraday electricity trading. LEF working paper. 2020.

https://ssrn.com/abstract=3489214.

14. Kiesel R, Paraschiv F. Econometric analysis of 15-minute intraday electricity prices. Energy Econ. 2017;64:77–90.
15. Kolkmann S, Ostmeier L, Weber C. Modelling multivariate intraday forecast update processes for wind power.

Unpublished working paper, University of Duisburg-Essen. 2019.

16. McInish TH, Wood RA. An analysis of intraday patterns in bid/ask spreads for NYSE stocks. J Finance.

1992;47(2):753–64.

17. Miettinen JJ, Holttinen H. Characteristics of day-ahead wind power forecast errors in Nordic countries and beneﬁts of

aggregation. Wind Energy. 2017;20(6):959–72. https://doi.org/10.1002/we.2073.

18. Morales JM, Conejo AJ, Pérez-Ruiz JA. Economic valuation of reserves in power systems with high penetration of

wind power. IEEE Trans Power Syst. 2009;24(2):900–10.

19. Øksendal B. Stochastic diﬀerential equations: an introduction with applications. 6th ed. Berlin: Springer; 2003.

(Universitext). ISBN 3-540-04758-1. https://doi.org/10.1007/978-3-642-14394-6.

20. Pape C, Weber C, Hagemann S. Are fundamentals enough? Explaining price variations in the German day-ahead and

intraday power market. Energy Econ. 2016;2016(54):376–87.

21. Le reseau de transporte d’electricite (RTE). Portail Clients: Prévisions de production éolienne en France. 2019.

https://clients.rte-france.com/lang/fr/visiteurs/vie/previsions_eoliennes.jsp.

22. Samuelson PA. Proof that properly anticipated prices ﬂuctuate randomly. Ind Manage Rev. 1965;6(2):41–9.
23. Steck S, Urban K. A reduced basis method for the Hamilton–Jacobi–Bellman equation within the European Union
Emission Trading Scheme. In: Hamilton–Jacobi–Bellman equations. Berlin: de Gruyter; 2018. p. 175–96. (Radon ser.
comput. appl. math.; vol. 21).

24. Yong J, Zhou XY. Stochastic controls: Hamiltonian systems and HJB equations. Berlin: Springer; 1999. (Applications of

mathematics (New York); vol. 43). ISBN 0-387-98723-1. https://doi.org/10.1007/978-1-4612-1466-3.

