An optimal trading problem in intraday electricity markets ∗

René Aïd †

Pierre Gruet ‡

Huyên Pham §

January 20, 2015

Abstract

We consider the problem of optimal trading for a power producer in the context
of intraday electricity markets. The aim is to minimize the imbalance cost induced by
the random residual demand in electricity, i.e. the consumption from the clients minus
the production from renewable energy. For a simple linear price impact model and a
quadratic criterion, we explicitly obtain approximate optimal strategies in the intraday
market and thermal power generation, and exhibit some remarkable properties of the
trading rate. Furthermore, we study the case when there are jumps on the demand
forecast and on the intraday price, typically due to error in the prediction of wind power
generation. Finally, we solve the problem when taking into account delay constraints
in thermal power production.

JEL Classiﬁcation: G11, Q02, Q40

MSC Classiﬁcation: 35Q93, 49J20, 60H30, 91G80.

Key words: Optimal trading, power plant, intraday electricity markets, renewable energy,
market impact, linear-quadratic control problem, jumps, delay.

5
1
0
2

n
a
J

9
1

]

R
T
.
n
i
f
-
q
[

1
v
5
7
5
4
0
.
1
0
5
1
:
v
i
X
r
a

∗This study was supported by FiME (Finance for Energy Market Research Centre) and the “Finance et
Développement Durable - Approches Quantitatives” EDF - CACIB Chair. The authors would like to thank
Marc Ringeisen, Head of EDF R&D Osiris Department for insightful discussion on trading and intraday
market.

†EDF R&D and Finance for Energy Market Research Centre www.ﬁme-lab.org, rene.aid at edf.fr
‡LPMA, Université Paris Diderot, gruet at math.univ-paris-diderot.fr
§LPMA, Université Paris-Diderot and CREST-ENSAE, pham at math.univ-paris-diderot.fr

1

1

Introduction

The development of renewable energy sources in Europe as a response to global climate
change has led to an increase of exchange in the intraday electricity markets. For instance,
the exchanged volume on the European Energy Exchange (EEX) for Germany has grown
from 2 TWh in 2008 to 25 TWh in 2013. This increase is mainly due to the level of
forecasting error of wind production, which leads power producers owning a large share of
wind production to turn more than ever to intraday markets in order to adjust their position
and avoid penalties for their imbalances. The accuracy of forecasts for renewable power
production from wind and solar may vary considerably depending on the agreggation level
(local vs regional forecast) and the time horizon. For a complete survey on this problem, the
reader can consult Giebel et al. [5], and may have in mind that the root mean square error
(RMSE) of the error forecast for the production of a wind farm in six hours can reach 20% of
its installed capacity. Many diﬀerent intraday markets have been designed and are subject
to diﬀerent sets of regulation. But, in all cases, intraday markets oﬀer power producer the
possibility to buy or sell power for the next (say) 9 hours to 32 hours (case of the French
electricity market of EpexSpot). These trades can occur after the closing of the day-ahead
market or during the clearing phase of the day-ahead market.

The problem of trading management in the intraday electricity market for a balancing
purpose has already drawn the attention in the literature. Henriot [6] studied the problem
of how the intraday market can help a power producer to deal with the wind production
error forecast in a stylized discrete time model.
In his model, the power producer is a
wind producer who is trying to minimize her sourcing cost on the intraday market while
maintaining a balance position between her forecast production and her sales. Henriot’s
model takes into account the impact of the wind power producer on the intraday price with
a deterministic inverse demand function, and the intraday price is not a risk factor. The only
risk factor comes from the error forecast of the wind production and its auto-correlation.
Garnier and Madlener [4] studies the trade-oﬀ between entering into a deal in the intraday
market right now and postponing it in a discrete time decision model where intraday prices
follow a geometric Brownian model and wind production error forecast follows an arithmetic
Brownian motion. In their framework, the power producer is supposed to have no impact
on intraday prices. Liquidity risk is taken into account as a probability of not ﬁnding a
counter-party at the next trading window.

In this paper, we consider a power producer having at disposal some renewable energy
sources (e.g. wind and solar), and thermal plants (e.g. coal, gas, oil, and nuclear sources),
and who can buy/sell energy in the intraday markets. Her purpose is to minimize the
imbalance cost, i.e. the cost induced by the diﬀerence between the demand of her clients
minus the electricity produced and traded, plus the production and trading costs. In contrast
with thermal power plants whose generation can be controlled, the power generated from
renewable sources is subject to non controllable ﬂuctuations or risks (wind speed, weather
forecast) and is then considered here as a random factor just like the demand. We then call
the residual demand the demand minus the energy generated by renewable energy. Thus, the
problem of the power producer is to minimize the imbalance costs arising from her residual
demand by relying both on her own controllable thermal assets and on the intraday market.
As in [4], we assume that the power producer has access to a continuously updated forecast
of the residual demand to be satisﬁed at terminal date T and that this forecast evolves
randomly. Moreover, the intraday price for delivery at time T evolves also randomly and
is correlated with the residual demand forecast. However, compared with [4], the intraday

2

market can be used for optimization purposes. We develop a model that allows us to study
how power producers can take advantage of the interaction between the dynamics of the
residual demand forecast and the dynamics of the intraday prices.

Our model shares some links with optimal order execution problems, as introduced in
the seminal paper by Almgren and Chriss [2], and then largely studied in the recent lit-
erature, see e.g. the survey paper [9].
In our context, the original feature with respect
to this literature is the consideration of a random demand target and the possibility for
the agent to use her thermal power production. This connection with optimal execution
is fruitful in the sense that it allows us to take into account several features of intraday
markets while maintaining the tractability of the model suﬃciently high to allow analytical
solutions. Hence, we take into account liquidity risk through a market impact, both perma-
nent and temporary, on the electricity price generated by a power producer when trading
in the intraday market. As in optimal execution problems, this impact is always in the
adverse direction: when the producer sells, the price decreases and when she buys, the price
increases. Our setting is a continuous-time decision problem representing the possibility for
the producer to make a deal at each time she wants and not only at pre-speciﬁed windows.
Moreover, it is general enough as it permits us to study the limiting cases of a pure retailer
(no production function), a pure trader (no demand commitment) and an integrated player
(player owning both clients and generation), small or large.

The main goal of this paper is to derive analytical results, which provide explicit solutions
for the (approximate) optimal control, hence giving enlightening economic interpretations
of the optimal trading strategies. In order to achieve such analytical tractability, we have
to make some simplifying assumptions on the dynamics of the price process and of the
residual demand forecast, as well as on the cost function, assumed to be of quadratic form
meaning a simple linear growth of the marginal cost of production with respect to the
production level. We ﬁrst consider a simple model for a continuous price process with linear
impact, and demand forecast driven by an arithmetic Brownian motion, and neglect in a
ﬁrst step the delay of production when using thermal power plants. We then study an
auxiliary control problem by relaxing the nonnegativity constraint on the generation level,
for which we are able to derive explicit solutions. The approximation error induced by this
relaxation constraint is analyzed. In next steps, we consider more realistic situations and
investigate two extensions: (i) On one hand, we incorporate the case where the residual
demand forecast is subject to sudden changes, related to prediction error for wind or solar
power production, which may be quite important due to the diﬃculties for estimating wind
speed and forecasting weather, see [3]. This is formalized by jumps in the dynamics of the
demand process, and consequently also on the price process. Again, we are able to obtain
explicit solutions. Actually, the key tool in the derivation of all these analytical results is a
suitable treatment of the linear-quadratic structure of our stochastic control problem. (ii)
On the other hand, we introduce natural delay constraints in the production, and show how
the optimal decision problem can be explicitly solved by a suitable reduction to a problem
without delay.

Our (approximate) optimal trading strategies present some remarkable properties. When
the intraday price process is a martingale, the optimal trading rate inherits the martingale
property, which implies in particular that the net position of electricity shares has a constant
growth rate on average. Moreover, the optimal strategy consists in making at each time
the forecast marginal cost equal to the forecast intraday price. This property follows the
common sense of intraday traders. Consequently, if the producer has made sales or purchases

3

on the day-ahead such that her forecast marginal cost equals the day-ahead price and if the
initial condition of the intraday price is the day-ahead price, thus, on average, the producer
optimal trading rate is zero. This fact is no longer true when the demand forecast and the
price follow processes with jumps. In this case, the optimal trading rate is a supermartingale
or a submartingale depending on the relative probability and size of positive and negative
jumps on the price process. For this reason, contrary to the case without jumps, the power
producer may need to have a non-zero initial trading rate even if she has made sales or
purchases on the day-ahead such that her forecast marginal cost equals the day-ahead price
and if the initial condition of the intraday price is the day-ahead price. We also quantify
explicitly the impact of delay in production on the trading strategies. When the price
process is a martingale, the net inventory in electricity shares grows linearly on average,
with a change of slope (which is smaller) at the time decision for the production.

The outline of the paper is organized as follows. We formulate the optimal trading
problem in Section 2. In Section 3, we study the optimal trading problem without delay.
We ﬁrst solve explicitly the auxiliary optimal execution problem, and then study the ap-
proximation on the solution to the original problem, by focusing in particular on the error
asymptotics. We illustrate our results with some numerical tests and simulations. We extend
in Section 4 our results to the case where jumps in demand forecast may arise. In Section
5, we show how the optimal trading problem with delay in production can be reduced to a
problem without delay, and then leads to explicit solutions. Finally, the appendix collects
the explicit derivations of our solutions, which are justiﬁed by veriﬁcation theorems.

2 Problem formulation

We consider an agent on an intraday energy market, who is required to guarantee her
equilibrium supply/demand for a given ﬁxed time T : she has to satisfy the demand of her
customers by purchase/sale of energy on the intraday market at time T and also by means
of her thermal power generation. We denote by Xt the net position of sales/purchases of
electricity at time t ≤ T for a delivery at terminal time T , assumed to be described by
an absolutely continuous trajectory up to time T , and by qt = ˙Xt the trading rate: qt >
0 means an instantaneous purchase of electricity, while qt < 0 represents an instantaneous
sale at time t:

Xt = X0 +

(cid:90) t

0

qsds,

0 ≤ t ≤ T.

(2.1)

Given the trading rate, the transactions occur with a market price impact:

Pt(q) = ˆPt +

(cid:90) t

g(qs)ds + f (qt).

0
Here, ( ˆPt)t is the unaﬀected intraday electricity price process on a ﬁltered probability space
(Ω, F, F = (Ft)t∈[0,T ], P), carrying some part of randomness of the market, and following
the terminology in the seminal paper by Almgren and Chriss [2], the term f (qt) refers to
the temporary price impact, while (cid:82) t
0 g(qs)ds describes the permanent price impact. The
price ( ˆPt)t may be seen as a forward price, evolving in real time, for delivery at time T . Let
us then denote by Y the intraday electricity price impacted by the past trading rate q of
the agent, deﬁned by:

Yt

:= ˆPt +

(cid:90) t

0

g(qs)ds.

4

We assume that Yt is observable and quoted, which means actually that the agent is a large
trader and electricity producer, whose actions directly impact the intraday electricity price.
The case where the agent is a small producer can be also dealt with by simply considering
a zero permanent impact function g ≡ 0. Notice that the transacted price is equal to the
sum of the quoted price Y and the temporary price impact:

Pt(q) = Yt + f (qt).

(2.2)

The residual demand DT is the consumption of clients of the agent minus the production
from renewable energy at terminal date T , and we assume that the agent has access to a
continuously updated forecast (Dt)t of the residual demand. The agent can use her thermal
power production with a quantity ξ at cost c(ξ) in order to match as close as possible the
target demand DT . In practice, generation of electricity can not be obtained instantaneously
and needs a delay to reach a required level of production. Hence, the decision to produce
a quantity ξ should be taken at time T − h, where h ∈ [0, T ] is the delay. Thus, for a
controlled trading rate q = (qt)t ∈ A, the set of real-valued F-adapted processes satisfying
some integrability conditions to be precised later, a production quantity ξ ∈ L0
+(FT −h), the
set of nonnegative FT −h-measurable random variables, the total cost is:

(cid:90) T

0

qtPt(q)dt + C(DT − XT , ξ)

:=

(cid:90) T

0

qtPt(q)dt + c(ξ) +

η
2

(DT − XT − ξ)2. (2.3)

The ﬁrst term in (2.3) represents the total running cost arising from the trading in the
intraday electricity market, and the last term, where η > 0, represents the quadratic pe-
nalization when the net position in sales/purchases of electricity XT + ξ (including the
production quantity ξ at cost c(ξ)) at terminal date T does not ﬁt the eﬀective demand DT .
The objective of the agent is then to minimize over q and ξ the expected total cost:

minimize over q ∈ A, ξ ∈ L0

+(FT −h)

(cid:104) (cid:90) T

E

0

qtPt(q)dt + C(DT − XT , ξ)

(cid:105)
.

(2.4)

Remark 2.1 1) The penalization term in the objective function above is a simpliﬁcation of
the eﬀective penalization process that can be found in real electricity markets. For instance,
the penalization of imbalances in the French electricity market depends both on the sign
of the imbalance of the electricity system and on the price of imbalances (see [1, chap 2.,
sec. 2.2.1]). Nevertheless, the positive coeﬃcient η captures the main objective of the
penalization process. The agent has no incentive of being either too long or too short.

2) On real markets, trading ends some time before the date of delivery, at which the agent
has to ensure equilibrium (e.g. on the French electricity market, there is a delay of 45
minutes). We do not include that practical fact in our framework, by considering that the
delay is null for the sake of clarity. There is no mathematical consequence: it is enough to
have in mind that the delivery and production do not really take place at T , but at T plus
some delay.

3) The larger is η, the stronger is the incentive for the agent to be as close as possible
to the equilibrium supply-demand. At the limit, when η goes to inﬁnity, the agent is
formally constrained to ﬁt supply and demand. However, the limiting problem when η =
∞ is not mathematically well-posed since such perfect equilibrium constraint is in general
not achievable. Indeed, the demand at terminal date T is random, typically modelled via a
Gaussian noise, and the inventory X which is of ﬁnite variation, may exceed or underperform

5

with positive probability the demand DT at terminal date T . Hence, in the scenario where
XT > DT , and since by nature the production quantity ξ is nonnegative, it is not possible
to realize the equilibrium XT + ξ = DT , even if there is no delay. In the sequel, we ﬁx η >
0 (which may be large, but ﬁnite), and study the stochastic control problem (2.4).

4) The optimization problem (2.4) shares somes similarities with the optimal execution
problem in limit order book studied in the seminal paper by Almgren and Chriss [2], and
then extended by many authors in the literature, see e.g. the survey paper [9]. The main
diﬀerence is that in the execution problem of equities, the target is to buy or sell a certain
number of shares, i.e. lead XT to a ﬁxed constant (meaning formally that η goes to inﬁnity)
while in our intraday electricity markets context, the target is to realize the equilibrium with
the random demand DT , eventually with the help of production leverage ξ. However, in
contrast with the case of constant target, it is not possible in presence of random target DT
to achieve perfectly the equilibrium, which justiﬁes the introduction of the penalty factor η
(cid:3)
as pointed out above.

The main aim of this paper is to provide explicit (or at least approximate explicit)
solutions to the optimization problem (2.4), which are easily interpreted from an economic
point of view, and also allow to measure the impact of the various parameters of the model.
In order to achieve this goal, we shall adapt our modeling as close as possible to the linear-
quadratic framework of stochastic control, and make the following assumptions: The energy
production cost function is in the quadratic form:

c(x) =

β
2

x2,

for some β > 0. Although simple, a quadratic cost function represents the increase of the
marginal cost of production with the level of production.

Remark 2.2 (Pure retailer) In the limiting case when β goes to inﬁnity, meaning an inﬁ-
nite cost of production, this corresponds to the framework where the agent never uses the
production leverage and only trades in the intraday-market by solving the optimal execution
problem:

minimize over q ∈ A

(cid:104) (cid:90) T

E

0

(cid:105)
.
qtPt(q)dt + C(DT − XT , 0)

(2.5)

(cid:3)

As in Almgren and Chriss, we assume that the price impact (both permanent and

temporary) is of linear form, i.e.

g(q) = νq,

f (q) = γq,

for some constants ν ≥ 0 and γ > 0. The unaﬀected intraday electricity price is taken as a
Bachelier model:

ˆPt = ˆP0 + σ0Wt,

(2.6)

where W is a standard Brownian motion, and σ0 > 0 is a positive constant. Such assumption
might seem a shortcoming at ﬁrst sight since it allows for negative values of the unaﬀected
price. However, in practice, for our intraday execution problem within few hours, negative

6

prices occur only with negligible probability. The martingale assumption is also standard
in the market impact literature since drift eﬀects can often be ignored due to short trading
horizon. The quoted price Y , impacted by the past trading rate q ∈ A, is then governed by
the dynamics:

The dynamics of the residual demand forecast is given by

dYt = νqtdt + σ0dWt.

dDt = µdt + σddBt,

(2.7)

(2.8)

where µ, σd are constants, with σd > 0, and B is a Brownian motion correlated with W :
d < W, B >t = ρdt, ρ ∈ [−1, 1].

From (2.2), one can then deﬁne the value function associated to the dynamic version of

the optimal execution problem (2.4) by:

v(t, x, y, d)

:=

inf
q∈At,ξ∈L0

+(FT −h)

J(t, x, y, d; q, ξ)

(2.9)

with

J(t, x, y, d; q, ξ)

(cid:104) (cid:90) T

:= E

t

qs(Y t,y

s + γqs)ds + C(Dt,d

T − X t,x

T , ξ)2(cid:105)

,

(2.10)

for (t, x, y, d) ∈ [0, T ] × R × R × R, where At denotes the set of real-valued processes q =
(qs)t≤s≤T s.t. qs is Fs-adapted and E(cid:2) (cid:82) T
s ds] < ∞, Dt,d is the solution to (2.8) starting
from d at t, and given a control q ∈ At, Y t,y denotes the solution to (2.7) starting from y
at time t, and X t,x is the solution to (2.1) starting from x at t.

t q2

In a ﬁrst step, we shall consider the case when there is no delay in the production, and
then show in the last section of this paper how to reduce the problem with delay to a no
delay problem. We shall also study the case when there are jumps in the residual demand
forecast.

3 Optimal execution without delay in production

In this section, we consider the case when there is no delay in production, i.e. h = 0. In this
case, we notice that the optimization over q and ξ in (2.4) is done separately. Indeed, the
production quantity ξ ∈ L0
+(FT ) is chosen at the ﬁnal date T , after the decision over the
trading rate process (qt)t∈[0,T ] is achieved (leading to an inventory XT ). It is determined
optimally through the optimization a.s. at T of the terminal cost C(DT − XT , ξ), hence in
feedback form by ξ∗

T = ˆξ+(DT − XT ) where

ˆξ+(d)

:= arg min

C(d, ξ) = arg min

ξ≥0
η
η + β

=

d1d≥0.

ξ≥0

(cid:2) β
2

ξ2 +

η
2

(d − ξ)2(cid:3)

The value function of problem (2.9) may then be rewritten as

v(t, x, y, d) = inf
q∈At

(cid:104) (cid:90) T

E

t

qs(Y t,y

s + γqs)ds + C+(Dt,d

T − X t,x

T )2(cid:105)

(3.1)

,

(3.2)

7

where

C+(d)

:= C(d, ˆξ+(d))
ηβ
η + β

1
2

=

d21d≥0 +

η
2

d21d<0.

(3.3)

and the optimal trading rate q∗ is derived by solving (3.2).

Due to the indicator function in C+, caused by the non negativity constraint on the
production quantity, there is no hope to get explicit solutions for the problem (3.2), i.e. solve
explicitly the associated dynamic programming Hamilton-Jacobi-Bellman (HJB) equation.
We shall then consider an auxiliary execution problem by relaxing the sign constraint on the
production quantity, for which we are able to provide explicit solution. Next, we shall see
how one can derive an approximate solution to the original problem in terms of this auxiliary
explicit solution, and we evaluate the error and illustrate the quality of this approximation
by numerical tests.

3.1 Auxiliary optimal execution problem

We consider the optimal execution problem with relaxation on the non negativity constraint
of the production leverage, and thus introduce the auxiliary value function

˜v(t, x, y, d)

:=

inf
q∈A,ξ∈L0(FT )

J(t, x, y, d; q, ξ),

for (t, x, y, d) ∈ [0, T ] × R × R × R. By same arguments as for the derivation of (3.2), we
have

˜v(t, x, y, d) = inf
q∈A

(cid:104) (cid:90) T

E

t

where

qs(Y t,y

s + γqs)ds + ˜C(Dt,d

T − X t,x
T )

(cid:105)
,

(3.4)

ˆξ(d)

:= arg min

ξ∈R

C(d, ξ) =

η
η + β

d,

˜C(d)

:= C(d, ˆξ(d)) =

1
2

ηβ
η + β

d2 =:

1
2

r(η, β)d2.

(3.5)

The function in (3.5) can be interpreted as a reduced cost function. Because the production
cost function and the penalization are both quadratic, they can be reduced to a single
production function where the imbalances are internalized by the producer.

By exploiting the linear-quadratic structure of the stochastic control problem (3.4), we

can obtain explicit solutions for this auxiliary problem.

8

Theorem 3.1 The value function to (3.4) is explicitly equal to:

˜v(t, x, y, d) =

r(η, β)( ν

2 (T − t) + γ)

(r(η, β) + ν)(T − t) + 2γ

(cid:0)(d − x)2 + 2µ(T − t)(d − x)(cid:1)

+

+

T − t
(r(η, β) + ν)(T − t) + 2γ
r(η, β)(T − t)
(r(η, β) + ν)(T − t) + 2γ

(cid:0) −

y2
2

+ r(η, β)µ(T − t)y(cid:1)

(d − x)y

(cid:16)

ln

1 +

(r(η, β) + ν)(T − t)
2γ

(cid:17)

+ γ

0 + σ2
σ2

dr2(η, β) − 2ρσ0σdr(η, β)

(cid:0)r(η, β) + ν(cid:1)2
dr(η, β)ν + 2ρσ0σdr(η, β) − σ2
σ2
0
2(cid:0)r(η, β) + ν(cid:1)

r(η, β)µ2(T − t)2( ν

2 (T − t) + γ)

(r(η, β) + ν)(T − t) + 2γ

,

+

+

(T − t)

for (t, x, y, d) ∈ [0, T ] × R × R × R, with an optimal trading rate given in feedback form by:

ˆqs = ˆq(cid:0)T − s, Dt,d

s − ˆX t,x,y,d
s
r(η, β)(µt + d) − y
(r(η, β) + ν)t + 2γ

.

ˆq(t, d, y)

:=

, ˆY t,x,y,d
s

(cid:1),

t ≤ s ≤ T

(3.6)

Here ( ˆX t,x,y,d, ˆY t,x,y,d, Dt,d) denotes the solution to (2.1)-(2.7)-(2.8) when using the feedback
control ˆq, and starting from (x, y, d) at time t. Finally, the optimal production leverage is
given by:

ˆξT = ˆξ(Dt,d

T − ˆX t,x,y,d

T

) =

η
η + β

(cid:0)Dt,d

T − ˆX t,x,y,d

T

(cid:1).

(3.7)

Skech of proof. We look for a candidate solution to (3.4) in the quadratic form:

˜w(t, x, y, d) = A(T − t)(d − x)2 + B(T − t)y2 + F (T − t)(d − x)y

+ G(T − t)(d − x) + H(T − t)y + K(T − t),

for some deterministic functions A, B, F , G, H and K. Plugging this ansatz into the
Hamilton-Jacobi-Bellman (HJB) equation associated to the stochastic control problem (3.4),
we ﬁnd that these deterministic functions should satisfy a system of Riccati equations, which
can be explicitly solved. Then, by a classical veriﬁcation argument, we check that this ansatz
˜w is indeed equal to ˜v, with an optimal feedback control derived from the argmax in the
(cid:3)
HJB equation. The details of the proof are reported in Appendix.

Remark 3.1 (Pure trader) By sending β to inﬁnity in the expression of the value function
˜v and of the optimal feedback control ˆq, and observing that r(η, β) goes to η, we obtain the

9

solution to the optimal execution problem (2.5) without leverage production:

vN P (t, x, y, d)

:= inf
q∈A

(cid:104) (cid:90) T

E

t

qs(Y t,y

s + γqs)ds + C(Dt,d

T − X t,x

(cid:105)
T , 0)

(3.8)

=

η( ν

2 (T − t) + γ)
(η + ν)(T − t) + 2γ

(cid:0)(d − x)2 + 2µ(T − t)(d − x)(cid:1)

+

+

T − t
(η + ν)(T − t) + 2γ
η(T − t)
(η + ν)(T − t) + 2γ

(cid:0) −

y2
2

+ ηµ(T − t)y(cid:1)

(d − x)y

(cid:16)

ln

1 +

(η + ν)(T − t)
2γ

(cid:17)

0 + σ2
σ2

dη2 − 2ρσ0σdη
(cid:0)η + ν(cid:1)2
dην + 2ρσ0σdη − σ2
σ2
0
2(cid:0)η + ν(cid:1)
ηµ2(T − t)2( ν

+ γ

+

+

2 (T − t) + γ)

,

(η + ν)(T − t) + 2γ

(T − t)

for (t, x, y, d) ∈ [0, T ] × R × R × R, with an optimal trading rate given in feedback form by:

ˆqN P
s

ˆqN P (t, d, y)

Interpretation:

= ˆqN P (cid:0)T − s, Dt,d
η(µt + d) − y
(η + ν)t + 2γ

:=

.

s − ˆX t,x,y,d
s

, ˆY t,x,y,d
s

(cid:1),

t ≤ s ≤ T

(cid:3)

1. The optimal trading rate ˆqs at time s ∈ [t, T ], given in feedback form by (3.6), is

decomposed in two terms: the ﬁrst one

r(η, β)
(r(η, β) + ν)(T − t) + 2γ

(cid:0)µ(T − s) + Dt,d

s − ˆX t,x,y,d
s

(cid:1)

is related to the trading rate in order to follow the trend of the demand, and to the
incentive to invest when the forecast of the residual demand is larger than the current
inventory. The second term

−

1
(r(η, β) + ν)(T − t) + 2γ

ˆY t,x,y,d
s

represents the negative impact of the quoted price on the investment strategy: the
higher the price is, the more the agent decreases her trading rate until she reaches
negative value meaning a resale of electricity shares. These eﬀects are weighted by
the constant denominator term depending on the penalty factor η, the marginal cost
production factor β, the temporary and permanent price impact parameters γ, ν, and
the time to maturity T − t.

10

2. By introducing the marginal cost function: c(cid:48)(x) = βx, and the process

ˆξs

:=

η
η + β

(cid:0)Dt,d

s + µ(T − s) − ˆX t,x,y,d

s

− ˆqs(T − s)(cid:1), t ≤ s ≤ T,

which is interpreted as the forecast production for the ﬁnal time T (recall expression
(3.7) of the ﬁnal production), we notice from the expression of the optimal trading
rate that the following relation holds:

ˆY t,x,y,d
s

+ ν ˆqs(T − s) + 2γ ˆqs = c(cid:48)( ˆξs),

t ≤ s ≤ T.

(3.9)

This relation means that at each time, the optimal trading rate is to make the forecast
intraday price plus marginal temporary impact (left hand side), which can be seen as
the marginal cost of electricity on the intraday market at time T , equal to the forecast
marginal cost of production. Here, the instantaneous impact γ appears as a marginal
cost of buying or selling, and the forecast at time s supposes that the optimal trading
(cid:3)
rate ˆqs is held constant between s and T .

We complete the description of the optimal trading rate by pointing out a remarkable

martingale property.

Proposition 3.1 The optimal trading rate process (ˆqs)t≤s≤T in (3.6) is a martingale.

Proof. By applying Itô’s formula to ˆqs = ˆq(T − s, Dt,d
since ˆq is linear in d and y, we have:

s − ˆX t,x,y,d
s

, ˆY t,x,y,d
s

), t ≤ s ≤ T , and

+ (µ − ˆq)

(cid:3)(T − s, Dt,d

s − ˆX t,x,y,d
s

, ˆY t,x,y,d
s

)ds

dˆqs = (cid:2) −

+

+

∂ ˆq
∂t
∂ ˆq
∂d
∂ ˆq
∂y

+ ν ˆq

∂ ˆq
∂ ˆq
∂d
∂y
s − ˆX t,x,y,d
s

(T − s, Dt,d

, ˆY t,x,y,d
s

)σddBs

(T − s, Dt,d

s − ˆX t,x,y,d
s

, ˆY t,x,y,d
s

)σ0dWs,

from the dynamics (2.1), (2.8), and (2.7) of ˆX t,x,y,d, Dt,d and ˆY t,x,y,d. Now, from the explicit
expression of the function ˆq(t, y, d), we see that

−

∂ ˆq
∂t

+ (µ − ˆq)

∂ ˆq
∂d

+ ν ˆq

∂ ˆq
∂y

= 0,

and so:

dˆqs =

r(η, β)σd
(r(η, β) + ν)(T − s) + 2γ

dBs −

σ0
(r(η, β) + ν)(T − s) + 2γ

dWs,

(3.10)

which shows the required martingale property.

(cid:3)

Remark 3.2 Recall that in the classical optimal execution problem as studied in [2], the
optimal trading rate is constant. We retrieve this result in their framework which corres-
ponds to the case where σd = 0 (constant demand target), β = ∞ (there is no production),
and η = ∞ (constraint to lead XT to the ﬁxed target), see Remark 2.1 4).
Indeed, in
these limiting regimes, we see from (3.10) that dˆqs = 0, meaning that {ˆqs, t ≤ s ≤ T } is
constant. In our framework, this is generalized to the martingale property of the optimal

11

trading rate process, which implies that the optimal inventory { ˆX t,x,y,d
constant growth rate in mean, i.e. dE[ ˆX t,x,y,d
time t given by ˆq(T − t, d − x, y).

s
is constant equal to the initial trading rate at

, t ≤ s ≤ T } has a

s
ds

]

As a consequence of this martingale property, if the producer already satisﬁes the relation
(3.9) in the day-ahead market, and if the initial intraday price is the day-ahead price, her
initial trading rate on the intraday market will be zero. And thus, on average, her trading
rate will be zero.

The martingale property of the trading rate process is actually closely related to the
martingale dynamics of the unaﬀected price ˆP in (2.6). As we shall see in Section 4 where
we consider jumps on price, making ˆP a sub or super martingale, the optimal trading rate
(cid:3)
will inherit the converse sub or super martingale property.

3.2 Approximate solution

We go back to the original execution problem with the non negativity constraint on the
production quantity. As pointed out above, there is no explicit solution in this case, due
to the form of the terminal cost function C+. The strategy is then to use the explicit
control consisting in the trading rate ˆq derived in (3.6), and of the truncated nonnegative
production quantity:

˜ξ∗
T

:= ˆξT 1

ˆξT ≥0

= ˆξ+(Dt,d

T − ˆX t,x,y,d

T

),

(3.11)

with ˆξT deﬁned in (3.7) from the auxiliary problem. In other words, we follow the trading
rate strategy ˆq determined from the problem without constraint on the ﬁnal production
quantity, and at the terminal date use the production leverage if the ﬁnal inventory ˆX t,x,y,d
is below the terminal demand Dt,d
T , by choosing a quantity proportional to this spread
T − ˆX t,x,y,d
Dt,d
. The aim of this section is to measure the relevance of this approximate
strategy (ˆq, ˜ξ∗
T ) ∈ A × L0
+(FT ) with respect to the optimal execution problem (2.9) by
estimating the induced error:

T

T

E1(t, x, y, d)

:= J(t, x, y, d; ˆq, ˜ξ∗

T ) − v(t, x, y, d),

for (t, x, y, d) ∈ [0, T ] × R × R × R. We also measure the approximation error on the value
functions:

E2(t, x, y, d)

:= v(t, x, y, d) − ˜v(t, x, y, d).

Notice that if ˆξT ≥ 0 a.s., i.e. Dt,d
T = ˆξT ,
then clearly (ˆq, ˆξT ) would be the solution to (2.9), and so E1(t, x, y, d) = E2(t, x, y, d) = 0.
Actually, these errors depend on the probability of the event: { ˆX t,x,y,d
T }, and we
have the following estimate:

a.s. (which is not true), and so ˜ξ∗

T ≥ ˆX t,x,y,d

> Dt,d

T

T

Proposition 3.2 For all (t, x, y, d) ∈ [0, T ] × R × R × R, we have

0 ≤ Ei(t, x, y, d) ≤

ηr(η, β)
2β

V (T − t)ψ

(cid:16) m(T − t, d − x, y)
(cid:112)V (T − t)

(cid:17)

,

i = 1, 2,

(3.12)

where

ψ(z)

:= (z2 + 1)Φ(−z) − zφ(z),

z ∈ R,

12

with φ = Φ(cid:48) the density of the standard normal distribution, and

m(t, d, y)

:=

(νt + 2γ)(µt + d) + yt
(r(η, β) + ν)t + 2γ

,

(3.13)

V (t)

:=

(cid:90) t

0

0s2 + σ2
σ2

d(νs + 2γ)2 + 2ρσ0σds(νs + 2γ)
(cid:2)(r(η, β) + ν)s + 2γ(cid:3)2

ds ≥ 0.

(3.14)

Proof. By deﬁnition of the value functions v and ˜v, recalling that (ˆq, ˆξT ) is an optimal
control for ˜v, and since (ˆq, ˜ξ∗

+(FT ), we have:

T ) ∈ A × L0

J(t, x, y, d; ˆq, ˆξT ) = ˜v(t, x, y, d) ≤ v(t, x, y, d) ≤ J(t, x, y, d; ˆq, ˜ξ∗

T ),

for all (t, x, y, d) ∈ [0, T ] × R × R × R. This clearly implies that both errors E1 and E2 are
nonnegative, and

max(E1(t, x, y, d), E2(t, x, y, d)) ≤ E(t, x, y, d) := J(t, x, y, d; ˆq, ˜ξ∗
We now focus on the upper bound for E. By deﬁnition of J in (2.10), ˆξT and ˜ξ∗
and (3.11), we have

T ) − J(t, x, y, d; ˆq, ˆξT ).

T in (3.7)

(cid:104)
C(Dt,d
E(t, x, y, d) = E
(cid:104)
= E

C(Dt,d

T

T − ˆX t,x,y,d
T − ˆX t,x,y,d
− C(Dt,d

T

, ˜ξ∗

T ) − C(Dt,d

T − ˆX t,x,y,d

T

(cid:105)
, ˆξT )

, ˆξ+(Dt,d

))

T − ˆX t,x,y,d
T
, ˆξ(Dt,d

T − ˆX t,x,y,d
T
) − ˜C(Dt,d

T − ˆX t,x,y,d
T
(cid:105)
)

T − ˆX t,x,y,d

T

(cid:105)
))

(cid:104)
C+(Dt,d
= E

=

ηr(η, β)
2β

T

T − ˆX t,x,y,d
(cid:104)(cid:0)Dt,d
E

T − ˆX t,x,y,d

T

(cid:1)21

Dt,d

T − ˆX t,x,y,d

T

(cid:105)
,

<0

(3.15)

from the deﬁnitions and expressions of C+ and ˜C in (2.3), (3.3) and (3.5). Now, from (3.10)
and by integration, we obtain the explicit (path-dependent) form of the optimal trading
rate control:

ˆqs = ˆqt +

−

(cid:90) s

t
(cid:90) s

t

r(η, β)σd
(r(η, β) + ν)(T − u) + 2γ
σ0
(r(η, β) + ν)(T − u) + 2γ

dBu

dWu,

t ≤ s ≤ T,

with ˆqt = ˆq(T − t, d − x, y). We then obtain the expression of the ﬁnal spread between
demand and inventory:

Dt,d

T − ˆX t,x,y,d

T

= d − x + µ(T − t) +

(cid:90) T

σddBs −

(cid:90) T

t

ˆqsds

= m(T − t, d − x, y) +

t
(cid:90) T

t

σd(ν(T − s) + 2γ)
(r(η, β) + ν)(T − s) + 2γ

dBs

+

(cid:90) T

t

σ0(T − s)
(r(η, β) + ν)(T − s) + 2γ

dWs,

by Fubini’s theorem, and with

m(t, d, y)

:= d + µt − tˆq(t, d, y),

13

T − ˆX t,x,y,d
which is explicitly written as in (3.13) from the expression (3.6) of ˆq. Thus, Dt,d
follows a normal distribution law with mean m(T − t, d − x, y) and variance V (T − t) given
by (3.14), and from (3.15), we deduce that

T

E(t, x, y, d) =

ηr(η, β)
2β

V (T − t)ψ

(cid:16) m(T − t, d − x, y)
(cid:112)V (T − t)

(cid:17)

,

while the probability that the ﬁnal inventory is larger than the terminal demand is:

P(cid:2)Dt,d

T − ˆX t,x,y,d

T

< 0(cid:3) = Φ

(cid:16)

−

m(T − t, d − x, y)
(cid:112)V (T − t)

(cid:17)

.

(3.16)

(cid:3)

Error asymptotics. We now investigate the accuracy of the upper bound in (3.12)

¯E(T − t, d − x, y)

:=

ηr(η, β)
2β

V (T − t)ψ

(cid:16) m(T − t, d − x, y)
(cid:112)V (T − t)

(cid:17)

.

It is well-known (see e.g. Section 14.8 in [10]) that

zΦ(−z) ≤ φ(z), ∀z ∈ R,

(3.17)

from which we easily see that ψ is non increasing, convex, and ψ(∞) = 0. Thus, ¯E(T −
t, d − x, y) decreases to zero for large m(T − t, d − x; y) or small V (T − t). We shall study
its asymptotics in three limiting cases (i) the time to maturity T − t is small, (ii) the initial
demand spread d − x is large, (iii) the initial quoted price y is large. We prove that the
error bound ¯E(T − t, d − x, y), and thus E1(t, x, y, d), E2(t, x, y, d), converge to zero at least
with an exponential rate of convergence in these limiting regimes:

Proposition 3.3

(i) For all (x, y, d) ∈ R × R × R with d > x, we have

(T − t) ln ¯E(T − t, d − x, y) ≤ −

lim sup
T −t↓0

1
2

(cid:16) d − x
σd

(cid:17)2

.

(ii) For all (t, y) ∈ [0, T ) × R, we have

lim sup
d−x→∞

1

(d − x)2 ln ¯E(T − t, d − x, y) ≤ −

1
2

m2
∞(T − t)
V (T − t)

,

(3.18)

(3.19)

where

m∞(t) =

νt + 2γ
(cid:0)r(η, β) + ν(cid:1)t + 2γ

(iii) For all (t, x, d) ∈ [0, T ) × R × R, we have

lim sup
y→∞

1
y2 ln ¯E(T − t, d − x, y) ≤ −

1
2

n2
∞(T − t)
V (T − t)

,

(3.20)

where

n∞(t) =

t
(r(η, β) + ν)t + 2γ

.

14

Proof. From (3.17), we have:

0 ≤ ψ(z) ≤ z−1φ(z), ∀z > 0.

Notice that in the three asymptotic regimes (i) (with d − x > 0), (ii), and (iii), the quantity
m(T − t, d − x, y) is positive, and we thus have:

¯E(T − t, d − x, y) ≤

ηr(η, β)
2β

3
2

V (T − t)
m(T − t, d − x, y)

φ

(cid:16) m(T − t, d − x, y)
(cid:112)V (T − t)

(cid:17)

.

(3.21)

d(T − t), i.e. V (T − t)/σ2

(i) For small time to maturity T − t, we see that m(T − t, d − x, y) converges to d − x > 0,
while V (T − t) ∼ σ2
d(T − t) converges to 1. This shows from (3.21)
that, when T − t goes to zero, the error bound ¯E(T − t, d − x, y), converges to zero at least
with an exponential rate of convergence, namely the one given by (3.18).
(ii) For large demand spread d − x, we see that m(T − t, d − x, y) ∼ m∞(T − t)(d − x), i.e.
the ratio m(T − t, d − x, y)/m∞(T − t)(d − x) converges to 1 when d − x goes to inﬁnity.
This shows from (3.21) that, when d − x goes to inﬁnity, the error bound ¯E(T − t, d − x, y),
converges to zero at least with an exponential rate of convergence, namely the one given by
(3.19).
(iii) For large y, we see that m(T − t, d − x, y) ∼ n∞(T − t)y, i.e. the ratio m(T − t, d −
x, y)/n∞(T − t)y converges to 1 when y goes to inﬁnity. This shows from (3.21) that, when
d − x goes to inﬁnity, the error bound ¯E(T − t, d − x, y) converges to zero at least with an
(cid:3)
exponential rate of convergence, namely the one given by (3.20).

Interpretation. Recall from (3.16) that

P(cid:2)Dt,d

T < ˆX t,x,y,d

T

(cid:3) = Φ

(cid:16)

−

m(T − t, d − x, y)
(cid:112)V (T − t)

(cid:17)

,

and thus following the same arguments as in the above proof, we have:

(i)

(ii)

lim sup
T −t↓0

(T − t) ln P(cid:2)Dt,d

T < ˆX t,x,y,d

T

(cid:3) = −

1
2

(cid:16) d − x
σd

(cid:17)2

,

(3.22)

for all (x, y, d) ∈ R × R × R with d > x. We observe that the rate in the rhs of (3.18)
(or (3.22)) depends only on the demand volatility σd and the initial demand spread
d − x. Moreover, it is all the larger, the smaller σd is, and the larger d − x is. This
means that the terminal demand will stay with very high probability above the ﬁnal
inventory once we are near from the maturity with a low volatile demand, initially
larger than the inventory, in which case, the explicit strategy (ˆq, ˜ξ∗
T ) approximates
very accurately the optimal strategy (q∗, ξ∗

T ).

lim sup
d−x→∞

1

(d − x)2 ln P(cid:2)Dt,d

T < ˆX t,x,y,d

T

(cid:3) = −

1
2

m2
∞(T − t)
V (T − t)

,

(3.23)

for all (t, y) ∈ [0, T ) × R, The rate in the rhs of (3.19) (or (3.23)) is all the larger, the
smaller the volatilities σ0 and σd of the electricity price and demand are. Again, we

15

have the same interpretation than in the asymptotic regime (i), and this means that
the explicit strategy (ˆq, ˜ξ∗
T ) approximates very accurately the optimal strategy (q∗, ξ∗
T )
in the limiting regime when the initial demand spread is large, and the volatilities are
small.

(iii)

lim sup
y→∞

1

y2 ln P(cid:2)Dt,d

T < ˆX t,x,y,d

T

(cid:3) = −

1
2

n2
∞(T − t)
V (T − t)

,

(3.24)

for all (t, x, d) ∈ [0, T ) × R × R. In the limiting regime where the initial quoted price y
is large, the agent has a strong incentive to sell energy on the intraday market, which
leads to a ﬁnal inventory staying under the ﬁnal demand with high probability, and
thus to a very accurate approximate strategy (ˆq, ˜ξ∗
T ). As in case (ii), this accuracy is
strengthened for small volatilities σ0 and σd of the electricity price and demand. (cid:3)

3.3 Numerical results

3.3.1 Numerical tests

We measure quantitatively the accuracy of the error bound derived in the previous paragraph
with some numerical tests. Let us ﬁx the following parameter values: σ0 = 1/60 e·(MW)−1 ·
s−1/2, σd = 1000/60 MW·s−1/2, β = 0.002 e·(MW)−2, η = 200 e·(MW)−2, µ = 0 MW·s−1,
ν = 10−10e·(MW)−2, γ = 10−10e·s·(MW)−2 and ρ = 0.8.

We start from the initial time t = 0, with a zero inventory X0 = 0, and vary respectively
the maturity T , the initial demand D0 and the initial price Y0. We compute the probability
for the ﬁnal inventory to exceed the ﬁnal demand P[ ˆXT > DT ], the approximate value
function ˜v(0, X0, Y0, D0), and the error bound ¯E(T, D0 − X0, Y0). The results are reported
in Table 1 when varying T , in Table 2 when varying D0 and in Table 3 when varying Y0.

T (h) P[ ˆXT > DT ]

1
8
24
50

< 10−16
< 10−16
< 10−16
7.72 × 10−13

˜v(0, X0, Y0, D0) (e)
1.88 × 106
1.88 × 106
1.89 × 106
1.90 × 106

¯E(T, D0 − X0, Y0) (e)
< 10−16
< 10−16
4.16 × 10−12
2.48 × 10−4

Table 1: Y0 = 50 e·(MW)−1 and D0 = 50000 MW

Table 1 shows that for time to maturity less than T = 24h, the probability for the ﬁnal
inventory to exceed the ﬁnal demand is very small, and consequently the error bound is
rather negligible. When the time horizon increases, the agent has the possibility to spread
over time her trading strategies for reducing the price impact, and purchase more energy,
in which case the probability for the ﬁnal inventory to exceed the demand increases.

Table 2 shows that the probability for the ﬁnal inventory to exceed the ﬁnal demand,
and the error bound are not much sensitive to the variations of the initial positive demand
D0. Actually, the main impact is caused by the initial stock price, as observed in Table 3.

For small initial electricity price Y0, the agent will buy more energy in the intraday
market and produce less. Therefore, the inventory will overtake with higher probability the
demand, in which case the approximate value function can be signiﬁcantly diﬀerent from
the original one, as observed from the error bound in Table 3 for Y0 = 20.

16

D0 (MW) P[ ˆXT > DT ]

500
5000
50000
500000

< 10−16
< 10−16
< 10−16
< 10−16

˜v(0, X0, Y0, D0) (e)
−5.86 × 105
−3.62 × 105
1.89 × 106
2.44 × 107

¯E(T, D0 − X0, Y0) (e)
4.16 × 10−12
4.16 × 10−12
4.16 × 10−12
4.16 × 10−12

Table 2: T = 24 h and Y0 = 50 e·(MW)−1

Y0 (e·(MW)−1) P[ ˆXT > DT ]

500
50
40
30
20

< 10−16
< 10−16
9.51 × 10−15
4.57 × 10−10
2.23 × 10−5

˜v(0, X0, Y0, D0)(e)
2.51 × 106
1.89 × 106
1.61 × 106
1.29 × 106
9.13 × 105

¯E(T, D0 − X0, Y0) (e)
< 10−16
4.16 × 10−12
3.80 × 10−4
1.30 × 10−2
1.26 × 103

Table 3: T = 24 h and D0 = 50000 MW

3.3.2 Simulations

We plot trajectories of some relevant quantities that we simulate with the following set of pa-
rameters: σ0 = 1/60 e·(MW)−1·s−1/2, σd = 1000/60 MW·s−1/2, β = 0.002 e·(MW)−2, η =
100 e·(MW)−2, µ = 0 MW·s−1, ρ = 0.8, ν = 4.00 × 10−5e·(MW)−2, γ = 2.22e·s·(MW)−2,
T = 24h, X0 = 0, D0 = 50000 MW and Y0 = 50 e·(MW)−1.

For such parameter values, the probability P[ ˆXT > DT ] is bounded above by 10−16, the

error ¯E(0, D0 − X0, Y0) is bounded by 2.82 × 10−10e, and

˜v(0, X0, Y0, D0) = 1916700e.

The executed strategy (ˆq, ˆξ∗

T ) can then be considered as very close to the optimal strategy.
Figure 1 represents the evolution of the trading rate control (ˆqt)t∈[0,T ] derived in (3.6) for
a given trajectory of price and demand, and this is consistent with the martingale property
as shown in Proposition 3.1. Figure 2 represents a simulation of the quoted price ˆYt with
impact and of the unaﬀected price ˆPt. Due to the buying strategy, i.e. positive ˆq, we
observe that the quoted price ˆY is larger than ˆP . In Figure 3, we plot the evolution of the
optimal inventory ( ˆXt)t∈[0,T ), and of the forecast residual demand (Dt)t∈[0,T ]. We see that
ˆXt is increasing, with a growth rate which looks constant as pointed out in Remark 3.2. At
ﬁnal time, if ˆXT < DT (which is the case in our simulation), the agent uses her production
leverage ˆξT , and achieves a ﬁnal inventory: ˆXT + ˆξT , which is represented by the peak at
time T . From the expression (3.7) of ˆξT , the ﬁnal imbalance cost is equal to

DT − ˆXT − ˆξT =

β
η + β

(DT − ˆXT ),

and is then positive, as shown in Figure 3.

17

Figure 1: Evolution of the trading rate control ˆq

Figure 2: Simulation of the quoted impacted price ˆY and of the unaﬀected price ˆP .

Figure 3: Evolution of the inventory ˆX and of the forecast residual demand D.

18

Control0.250.300.350.400.450.500.550.600100002000030000400005000060000700008000090000Price without impactPrice with impact495051525354555657580100002000030000400005000060000700008000090000Intraday inventory and final productionForecast residual demand010000200003000040000500006000001000020000300004000050000600007000080000900004 Jumps in the residual demand forecast

In this section, we incorporate the case where the residual demand forecast is subject to
sudden changes induced by prediction errors on renewable production, which may be quite
large. Our aim is to study the impact on the strategies obtained in the previous section,
and we shall also neglect the delay in thermal plants production.

t , N −

t )t≥0 with intensity λ > 0, where N +
t

The sudden changes in the demand forecast are modeled via a compound Poisson process
Nt = (N +
is the counting process associated to
positive jumps of the demand forecast with size δ+ > 0, occurring with probability p+ ∈
[0, 1], while N −
is the counting process associated to negative jumps of the demand forecast
t
with size δ− < 0, occurring with probability p− = 1 − p+. We denote by δ := δ+p+ + δ−p−
the mean of the jump size of the demand forecast. The dynamics of the residual demand
forecast D is then given by:

dDt = µdt + σddBt + δ+dN +

t + δ−dN −
t ,

(4.1)

where we add a jump component with respect to the model in (2.8). Moreover, as soon as
a jump in the residual demand forecast occurs, this is impacted into the intraday electricity
price since the main producers are assumed to have access to the whole updated forecast.
We thus model the unaﬀected electricity price by:

ˆPt = ˆP0 + σ0Wt + π+N +

t + π−N −
t ,

(4.2)

where we add with respect to the Bachelier model in (2.6) a jump component of size π+
> 0 (resp. π− < 0) when the jump on residual demand is positive (resp. negative), which
means that a higher (resp.
lower) demand induces an increase (resp. drop) of price. We
denote by π := π+p+ + π−p− the mean of the jump size of the intraday price. Given a
trading rate q ∈ A, the dynamics of the quoted price Y is then governed by

dYt = νqtdt + σ0dWt + π+dN +

t + π−dN −
t .

(4.3)

By considering this simpliﬁed modeling of demand forecast subject to sudden shift in
terms of a Poisson process, we do not have additional state variables with respect to the
no jump case of the previous section. Let us then denote by v = v(λ)(t, x, y, d) the value
function to the optimal execution problem (2.4) with cost functional J = J (λ)(t, x, y, d, q, ξ),
where we stress the dependence in λ for taking into account jumps in demand forecast. The
value function in the no jump case derived in the previous section is denoted by v = v(0).
As in the case with no jumps, there is no explicit solution to v(λ) due to the non negativity
constraint on the ﬁnal production: we shall ﬁrst study the auxiliary execution problem
without sign constraint on the ﬁnal production, then provide an approximate solution to
the original one with an estimation of the induced error approximation, and with some
numerical illustrations. We compare the results with the no jump case by focusing on the
impact of the jump components.

4.1 Auxiliary optimal execution problem

Similarly as in Subsection 3.1, we consider the optimal execution problem without non
negativity constraint on the ﬁnal production, denoted by ˜v = ˜v(λ)(t, x, y, d).

As in Theorem 3.1 for the case of the value function ˜v(0) without jumps, we have an

explicit solution to this auxiliary problem.

19

Theorem 4.1 The value function to the auxiliary optimization problem is explicitly given
by:

˜v(λ)(t, x, y, d)
= ˜v(0)(t, x, y, d)

+

−

λ
2

λ
2

+λγ

r(η, β)(T − t)(cid:0)π(T − t) + 2δ(ν(T − t) + 2γ)(cid:1)
(cid:0)r(η, β) + ν(cid:1)(T − t) + 2γ

(d − x)

(T − t)2(cid:0)π − 2r(η, β)δ(cid:1)
(cid:0)r(η, β) + ν(cid:1)(T − t) + 2γ
p+(π+ − r(η, β)δ+)2 + p−(π− − r(η, β)δ−)2
(cid:0)r(η, β) + ν(cid:1)2

y

(cid:16)

ln

1 +

(r(η, β) + ν)(T − t)
2γ

(cid:17)

p+((π+)2 − r(η, β)δ+(2π+ + νδ+)) + p−((π−)2 − r(η, β)δ−(2π− + νδ−))
r(η, β) + ν

(T − t)

−

+

λ
2
λr(η, β)
2

+

+

+

2νµδ + λ((p+)2δ+(π+ + νδ+) + (p−)2δ−(π− + νδ−))
r(η, β) + ν

(T − t)2

+λ2γr(η, β)

r(η, β)δ2 + 2νp+p−δ+δ− − ((p+)2δ+π+ + (p−)2δ−π−)
(r(η, β) + ν)(cid:0)(r(η, β) + ν)(T − t) + 2γ(cid:1)
λ2π2
48γ

2λγr2(η, β)µδ

(T − t)3

(r(η, β) + ν)(cid:0)(r(η, β) + ν)(T − t) + 2γ(cid:1) (T − t)2 −
2νδ+δ− + δ−π+ + δ+π−
λ2p+p−r(η, β)
(r(η, β) + ν)(T − t) + 2γ
2

(T − t)3

(T − t)2

1
8

4r(η, β)µλπ − λ2π2
(r(η, β) + ν)(T − t) + 2γ

(T − t)3,

for (t, x, y, d) ∈ [0, T ] × R × R × R, with an optimal trading rate given in feedback form by:

ˆq(λ)
s

ˆq(λ)(t, d, y)

= ˆq(λ)(T − s, Dt,d

:= ˆq(0)(t, d, y) + λ

s − ˆX t,x,y,d
, ˆY t,x,y,d
),
s
s
r(η, β)δt + π
4γ (r(η, β) + ν)t2

t ≤ s ≤ T

= ˆq(0)(t, d + λδt, y +

(r(η, β) + ν)t + 2γ
λπ
λ
4γ
2

πt) +

t,

(4.4)

where ˆq(0) is the optimal trading rate given in (3.6) in the case with no jump in the demand
forecast. Here ( ˆX t,x,y,d, ˆY t,x,y,d, Dt,d) denotes the solution to (2.1)-(4.3)-(4.1) when using the
feedback control ˆq(λ), and starting from (x, y, d) at time t. Finally, the optimal production
quantity is given by:

ˆξ(λ)
T

=

η
η + β

Proof. See Appendix.

(cid:0)Dt,d

T − ˆX t,x,y,d

T

(cid:1).

(4.5)

(cid:3)

Interpretation. The expression of the optimal trading rate ˆq(λ)

s

, s ∈ [t, T ], as

ˆq(λ)
s

= ˆq(0)

s + λ

r(η, β)δ(T − s) + π

4γ (r(η, β) + ν)(T − s)2

(r(η, β) + ν)(T − s) + 2γ

,

20

, ˆY t,x,y,d
s

s − ˆX t,x,y,d
s

s = ˆq(0)(T − s, Dt,d

where ˆq(0)
) represents the optimal trading rate that the
agent would use if she believes that the demand forecast will not jump, shows that under
the information knowledge about jumps, the agent will purchase more (resp. less) electricity
shares and this impact is all the larger, the larger the intensity λ of jumps, and the positive
(resp. negative) mean δ and π of jump size in demand forecast and price are. On the other
hand, the expression of ˆq(λ)

as the sum of two terms:

s

ˆq(λ)
s

= ˆq(0)(cid:0)T − s, Dt,d

s + λδ(T − s), ˆY t,x,y,d

s

+

λ
2

π(T − s)(cid:1) +

λπ
4γ

(T − s),

(4.6)

can be interpreted as follows. The ﬁrst term is analog to the optimal trading rate in the no
jump case, with an adjustment λδ(T − s) in the demand, which represents the expectation
of the demand jump size up to the ﬁnal horizon, and an adjustment λ
2 π(T − s) on the
price, which represents half of the expectation of the price jump size up to the ﬁnal horizon.
The second term, λπ
4γ (T − s), is deterministic, and linear in time, and we shall see on the
simulations for some parameter values that it can be dominant with respect to the ﬁrst
stochastic term. Moreover, notice that the equilibrium relation (3.9) in the no jump case
between forecast intraday price and forecast marginal cost of production does not hold
anymore in the presence of jumps, except at terminal date T :

ˆY t,x,y,d
T

+ 2γ ˆq(λ)
T

= c(cid:48)( ˆξ(λ)

T ).

(4.7)

(cid:3)

The unaﬀected price ˆP in (4.2) is no more a martingale in presence of jumps, except
when π = 0. It is actually a supermartingale when π < 0 (predominant negative jumps),
and submartingale when π > 0 (predominant positive jumps). The next result shows that
the optimal trading rate inherits the converse submartingale or supermartingale property
of the price process.

Proposition 4.1 The optimal trading rate process (ˆq(λ)
if π > 0, and a submartingale if π < 0. More precisely, the process {ˆq(λ)
s ≤ T } is a martingale.

)t≤s≤T in (4.4) is a supermartingale
2γ (s − t), t ≤

s + λπ

s

Proof. Notice that N ±
t
compensated martingale Poisson process ˜N ±
the trading rate process ˆq(λ)
s = ˆq(λ)(T − s, Dt,d

is a Poisson process with intensity λp±, and let us introduce the
t = Nt − λp±t. By applying Itô’s formula to
s − ˆX t,x,y,d
), t ≤ s ≤ T , and from the
s

, ˆY t,x,y,d
s

21

dynamics (2.1), (4.1) and (4.3), we have:

dˆq(λ)
s

=

(cid:104)

−

∂ ˆq(λ)
∂t

∂ ˆq(λ)
∂d

+ (µ − ˆq(λ))

+ ν ˆq(λ) ∂ ˆq(λ)
∂y
+ λp+(cid:0)ˆq(λ)(., . + δ+, . + π+) − ˆq(λ)(cid:1)
+ λp−(cid:0)ˆq(λ)(., . + δ−, . + π−) − ˆq(λ)(cid:1)(cid:105)
∂ ˆq(λ)
∂d
∂ ˆq(λ)
∂y

s − ˆX t,x,y,d
s

s − ˆX t,x,y,d
s

(T − s, Dt,d

(T − s, Dt,d

, ˆY t,x,y,d
s

, ˆY t,x,y,d
s

+

+

)σddBs

)σ0dWs

(T − s, Dt,d

s − ˆX t,x,y,d
s

, ˆY t,x,y,d
s

)ds

+ (cid:2)ˆq(λ)(T − s, Dt,d

+ (cid:2)ˆq(λ)(T − s, Dt,d

s

s− + δ+ − ˆX t,x,y,d
− ˆq(λ)(T − s, Dt,d
s− + δ− − ˆX t,x,y,d
− ˆq(λ)(T − s, Dt,d

, ˆY t,x,y,d
s−
s− − ˆX t,x,y,d
s
, ˆY t,x,y,d
s−
s− − ˆX t,x,y,d

s

s

+ π+)

, ˆY t,x,y,d
s−
+ π−)

, ˆY t,x,y,d
s−

)(cid:3)d ˜N −
s .

)(cid:3)d ˜N +
s

Now, from the expression (4.4) of ˆq(λ)(t, d, y), we see that:

−

∂ ˆq(λ)
∂t

+ (µ − ˆq(λ))

∂ ˆq(λ)
∂d

+ ν ˆq(λ) ∂ ˆq(λ)
∂y

+λ(cid:0)p+ ˆq(λ)(., . + δ+, . + π+) + p− ˆq(λ)(., . + δ−, . + π−) − ˆq(λ)(cid:1) = −

λπ
2γ

,

and then:

dˆq(λ)
s

= −

λπ
2γ

ds

+

+

r(η, β)σd
(r(η, β) + ν)(T − s) + 2γ
r(η, β)δ+ − π+
(r(η, β) + ν)(T − s) + 2γ

This proves the required assertions of the proposition.

dBs −

d ˜N +

s +

σ0
(r(η, β) + ν)(T − s) + 2γ
r(η, β)δ− − π−
(r(η, β) + ν)(T − s) + 2γ

dWs

d ˜N −

s . (4.8)

(cid:3)

Remark 4.1 The above supermartingale (or submartingale) property implies in particular
that the mean of the optimal trading rate process (ˆq(λ)
)0≤s≤T is decreasing (or increasing)
in time, and so that the trajectory of the optimal inventory mean E[ ˆX 0,x,y,d
], 0 ≤ s ≤ T , is
concave (or convex). Moreover, from the martingale property of ˆq(λ)
2γ s, 0 ≤ s ≤ T , we
have: E[ˆq(λ)
2γ s for 0 ≤ s ≤ T . Fix d, x, y, and let us then denote by
s
¯s(λ) := 2γ
λπ ˆq(λ)(T, d − x, y), which is explicitly written as:

] = ˆq(λ)(T, d − x, y) − λπ

s
s + λπ

s

¯s(λ) =

T
2

+

1
λπ

(cid:0)r(η, β)µ + λ(r(η, β)δ − π

2 )(cid:1)T + r(η, β)(d − x) − y

1 + (r(η,β)+ν)T

2γ

We have the following cases:

22

]

s
ds

• ¯s(λ) ≤ 0 and π > 0: this may arise for large y, or d << x, or r(η, β)δ << π/2. In this
extreme case, dE[ ˆX 0,x,y,d
] ≤ 0 for 0 ≤ s ≤ T , i.e. the trajectory of E[ ˆX 0,x,y,d
],
0 ≤ s ≤ T , is decreasing, which means that the agent will “always” sell electricity
shares since she takes advantage of high price, in order to decrease her inventory for
approaching the demand, and because in average, the jump size of the demand is
much lower than the positive jump size of the price.

= E[ˆq(λ)

s

s

]

s
ds

• ¯s(λ) ≤ 0 and π < 0: this may arise for small y, or d >> x, or r(η, β)δ >> π/2. In this
extreme case, dE[ ˆX 0,x,y,d
] ≥ 0 for 0 ≤ s ≤ T , i.e. the trajectory of E[ ˆX 0,x,y,d
],
0 ≤ s ≤ T , is increasing, which means that the agent will “always” buy electricity
shares since she takes advantage of low price, in order to increase her inventory for
approaching the demand, and because in average, the jump size of the price is much
lower than the jump size of the demand.

= E[ˆq(λ)

s

s

• ¯s(λ) ≥ T and π > 0: this may arise for r(η, β)δ >> π/2, d >> x or small y. In this
other extreme case, the trajectory of E[ ˆX 0,x,y,d
], 0 ≤ s ≤ T , is increasing, which means
that the agent will “always” buy electricity shares at low price in order to approach
the residual demand at ﬁnal time.

s

• ¯s(λ) ≥ T and π < 0: this may arise for r(η, β)δ << π/2, d << x or large y. The
trajectory of E[ ˆX 0,x,y,d
], 0 ≤ s ≤ T , is decreasing, which means that the agent will
“always” sell electricity shares at high price in order to approach the residual demand
at ﬁnal time.

s

• 0 < ¯s(λ) < T : in this regular case, it is interesting to comment on the two subcases:

– if π > 0, the trajectory of s (cid:55)→ E[ ˆX 0,x,y,d

] is increasing for s ≤ ¯s(λ) and then
decreasing for ¯s(λ) < s ≤ T . This means that the agent starts by purchasing
electricity shares for taking proﬁt of the positive price jumps (which have more
impact than the negative price jumps as p+π+ + p−π− > 0), and then resells
shares in order to achieve the equilibrium relation (4.7).

s

– if π < 0, i.e. the negative jumps have more impact than the positive ones: the

agent starts by selling electricity shares and then purchases shares.

4.2 Approximate solution

We turn back to the original optimal execution problem with the non negativity constraint
on the ﬁnal production, and as in Section 3.2, we use the approximate strategy consisting
in the trading rate ˆq(λ) derived in (4.4), and of the truncated nonnegative ﬁnal production:

(cid:3)

˜ξ(λ),∗
T

:= ˆξ(λ)
T

1

(λ)
ˆξ
T

≥0

= ˆξ+(Dt,d

T − ˆX t,x,y,d

T

),

T given in (4.5). We measure the relevance of this strategy (ˆq(λ), ˜ξ(λ),∗

T

with ˆξ(λ)
by estimating the induced error:

) ∈ A×L0

+(FT )

E (λ)
1

(t, x, y, d)

:= J (λ)(t, x, y, d; ˆq(λ), ˜ξ(λ),∗

T

) − v(λ)(t, x, y, d),

23

for (t, x, y, d) ∈ [0, T ] × R × R × R, and also measure the approximation error on the value
functions:

E (λ)
2

(t, x, y, d)

:= v(λ)(t, x, y, d) − ˜v(λ)(t, x, y, d).

Proposition 4.2 For all (t, x, y, d) ∈ [0, T ] × R × R × R, we have

0 ≤ E (λ)

i

(t, x, y, d) ≤

ηr(η, β)
2β

(cid:104)
V (T − t)E

ψ

(cid:16) m(λ)(T − t, d − x, y) + Σ−,t
(cid:112)V (T − t)

T

(cid:17)(cid:105)

(4.9)

for i = 1, 2, where ψ, m, V are deﬁned in Proposition 3.2,

(cid:16)
m(λ)(t, d, y) = m

(cid:17)
− r(η, β)δ(cid:1)t

(4.10)

t, d, y + λ(cid:0) π
2
r(η, β)δ − π
r(η, β) + ν

+ λ

(cid:104)

t −

2γ
r(η, β) + ν

(cid:16)

ln

1 +

r(η, β) + ν
2γ

(cid:17)(cid:105)
t

,

and

Σ−,t
T

=

(cid:90) T

t

δ−(ν(T − s) + 2γ) + π−(T − s)
(r(η, β) + ν)(T − s) + 2γ

dN −

s ≤ 0, a.s.

Proof. By the same arguments as in Proposition 3.2, we have

0 ≤ E (λ)

i

(t, x, y, d) ≤ E (λ)(t, x, y, d) := J (λ)(t, x, y, d; ˆq(λ), ˜ξ(λ),∗

T

) − J (λ)(t, x, y, d; ˆq(λ), ˆξ(λ)

T ),

for i = 1, 2, and

E (λ)(t, x, y, d) =

ηr(η, β)
2β

(cid:104)(cid:0)Dt,d
E

T − ˆX t,x,y,d

T

(cid:1)21

Dt,d

T − ˆX t,x,y,d

T

(cid:105)

,

<0

(4.11)

for (t, x, y, d) ∈ [0, T ] × R × R × R. Now, recall from (4.8) that:

dˆq(λ)
s

= −λ

+

+

+

(cid:104) π
2γ

r(η, β)δ − π
(r(η, β) + ν)(T − s) + 2γ
r(η, β)σd
(r(η, β) + ν)(T − s) + 2γ
r(η, β)δ+ − π+
(r(η, β) + ν)(T − s) + 2γ

dN +

dBs −

s +

(cid:105)

ds

σ0
(r(η, β) + ν)(T − s) + 2γ
r(η, β)δ− − π−
(r(η, β) + ν)(T − s) + 2γ

dWs

dN −
s ,

where we write the dynamics directly in terms of the Poisson processes N ±. By integration,
we deduce the (path-dependent) expression of ˆq(λ)

, t ≤ s ≤ T :

s

ˆq(λ)
s

= ˆq(λ)

t −
(cid:90) s

+

t
(cid:90) s

t

+

λπ
2γ

(s − t) +

λ(cid:0)r(η, β)δ − π(cid:1)
r(η, β) + ν

ln

r(η, β)σd
(r(η, β) + ν)(T − u) + 2γ
r(η, β)δ+ − π+
(r(η, β) + ν)(T − u) + 2γ

dBu −

dN +

u +

t
(cid:90) s

t

(cid:16) (r(η, β) + ν)(T − s) + 2γ
(r(η, β) + ν)(T − t) + 2γ
(cid:90) s

(cid:17)

σ0
(r(η, β) + ν)(T − u) + 2γ

dWu

r(η, β)δ− − π−
(r(η, β) + ν)(T − u) + 2γ

dN −
u ,

24

with ˆq(λ)
demand and inventory:

t = ˆq(λ)(T − t, d − x, y). We thus obtain the expression of the ﬁnal spread between

Dt,d

T − ˆX t,x,y,d

T

= d − x + µ(T − t) +

(cid:90) T

t

σddBs +

(cid:90) T

t

δ+dN +

s +

(cid:90) T

t

δ−dN −

s −

(cid:90) T

t

ˆq(λ)
s ds

= m(λ)(T − t, d − x, y)

(cid:90) T

+

t
(cid:90) T

t
(cid:90) T

t

+

+

dBs +

σd(ν(T − s) + 2γ)
(r(η, β) + ν)(T − s) + 2γ
δ+(ν(T − s) + 2γ) + π+(T − s)
(r(η, β) + ν)(T − s) + 2γ
δ−(ν(T − s) + 2γ) + π−(T − s)
(r(η, β) + ν)(T − s) + 2γ

σ0(T − s)
(r(η, β) + ν)(T − s) + 2γ

dWs

(cid:90) T

t

dN +
s

dN −
s ,

(4.12)

by Fubini’s theorem, and where

m(λ)(t, d, y)

:= d + µt − tˆq(λ)(t, d, y) +

−

λ(cid:0)r(η, β)δ − π(cid:1)
r(η, β) + ν

(cid:90) t

0

λπ
2γ

(cid:90) t

0

sds

ln

(cid:16) (r(η, β) + ν)s + 2γ
(r(η, β) + ν)t + 2γ

(cid:17)

ds,

is explicitly written as in (4.10) after some straightforward calculation. Denoting by ∆t,x,y,d
the continuous part of Dt,d
consisting in the three ﬁrst terms in the rhs of (4.12),
T , Σ−,t
and by Σ+,t

the jump parts consisting in the two last terms of (4.12), so that

T − ˆX t,x,y,d

T

T

T

Dt,d

T − ˆX t,x,y,d

T

= ∆t,x,y,d
T

+ Σ+,t

T + Σ−,t
T ,

T

we notice that ∆t,x,y,d
variance V (T − t), independent of Σ±,t
T . Then, conditionally on Σ±,t
a normal distribution law with mean m(λ)(T − t, d − x, y) + Σ+,t
V (T − t), and this implies from (4.11) that:

follows a normal distribution law with mean m(λ)(T − t, d − x, y) and
follows
T , and variance

T , Dt,d
T + Σ−,t

T − ˆX t,x,y,d

T

E (λ)(t, x, y, d) =

≤

ηr(η, β)
2β

ηr(η, β)
2β

(cid:104)
V (T − t)E

ψ

(cid:16) m(λ)(T − t, d − x, y) + Σ+,t

T + Σ−,t

T

(cid:112)V (T − t)

(cid:104)
V (T − t)E

ψ

(cid:16) m(λ)(T − t, d − x, y) + Σ−,t
(cid:112)V (T − t)

T

(cid:17)(cid:105)

,

since Σ+,t

T ≥ 0 a.s. and ψ is non-increasing.

(cid:17)(cid:105)

(cid:3)

Comments on the approximation error. Let us discuss about the accuracy of the
upper bound in (4.9):

¯E (λ)(T − t, d − x, y)

:=

ηr(η, β)
2β

(cid:104)
V (T − t)E

ψ

(cid:16) m(λ)(T − t, d − x, y) + Σ−,t
(cid:112)V (T − t)

T

(cid:17)(cid:105)

,

First, notice that m(λ)(T − t, d − x, y) + Σ−,t
in the limiting
regimes where T − t goes to zero, d − x or y goes to inﬁnity. Therefore, by dominated
convergence theorem, ¯E (λ)(T − t, d − x, y) converges to zero in these limiting regimes as in

T ∼ m(T − t, d − x, y) a.s.

25

the no jump case. However, we are not able to derive an asymptotic limit as in the no
jump case of Proposition 3.3, except when Σ−,t
T = 0, i.e. δ− = π− = 0, fo which we get
the same asymptotic limit. Actually, in the presence of negative jumps on the demand, it
is intuitively clear that our approximation should be less accurate than in the no jump case
since the probability for the residual demand to stay above the ﬁnal inventory is decreasing.
Anyway, the explicit strategies (ˆq(λ), ˜ξ(λ),∗
) still provide a very accurate approximation of
the optimal strategies at least in these limiting regimes, as illustrated in the next paragraph.

T

4.3 Numerical results

We plot trajectories of some relevant quantities that we simulate with the same set of pa-
rameters as in Paragraph 3.3.2: σ0 = 1/60 e·(MW)−1 · s−1/2, σd = 1000/60 MW·s−1/2, β =
0.002 e·(MW)−2, η = 200 e·(MW)−2, µ = 0 MW·s−1, ρ = 0.8, ν = 4.00 · 10−5e·(MW)−2,
γ = 2.22e·s·(MW)−2, T = 24h, X0 = 0, D0 = 50000 MW and Y0 = 50 e·(MW)−1. More-
over, we ﬁx the probability of positive jumps, p+ = 1 (then all jumps are positive: p− = 0),
and the following values for the jump components: λ = 1.5/(3600 · 24) s−1, π+ = 10
e·(MW)−1, δ+ = 1500 MW.

For such parameter values, we observe two occurrences of jumps on the trajectories of the
demand of price. Moreover, the probability P[ ˆXT > DT ] is bounded above by 2.92 × 10−16,
the error ¯E (λ)(0, D0 − X0, Y0) is bounded by 2.66 × 10−5e, and

˜v(λ)(0, X0, Y0, D0) = 2020950e.

t

T

The executed strategy (ˆq(λ), ˆξ(λ),∗
) can then be considered as very close to the optimal
strategy. This has to be compared with the numerical result obtained in the previous
section in the no jump case where we obtained a lower expected total cost: ˜v(0, X0, Y0, D0)
= 1916700e.

Figure 4 represents the evolution of the trading rate (ˆq(λ)

)t∈[0,T ], and we see that it
is decreasing consistently with the supermartingale property in Proposition 4.1. Actually,
we observe that the deterministic part in (4.6), which is linear in time, dominates the
stochastic part. The interpretation of the strategy is the following: since positive price
jumps are expected, the agent purchases a large number of shares in electricity with the
hope to sell it later at a higher price thanks to the possible occurrence of a positive jump.
At the price jump times, which can be visualized in Figure 5, we notice that the control
ˆq(λ) reacts by a decrease in the trading rate. The reaction to the second jump is more
sensible than to the ﬁrst jump since it occurs a short time before the ﬁnal horizon T , where
the objective is also to achieve the equilibrium relation (4.7) between price and marginal
cost. Finally, we observe clearly in Figure 6 the concavity of the trajectory of the optimal
inventory process ( ˆXt)t∈[0,T ), as expected from Remark 4.1. This emphasizes the double
objective of the agent: on one hand, the purchase of electricity shares for taking proﬁt of
the positive price jumps, and on the other hand the resale of electricity shares for attaining
the equilibrium relation between price and marginal cost at terminal date. We also plot the
production ˆξT at the ﬁnal time T on Figure 6, and observe as in the no jump case that the
imbalance cost DT − ˆXT − ˆξT is positive.

26

Figure 4: Evolution of the trading rate control ˆq(λ)

Figure 5: Simulation of the quoted impacted price ˆY and of the unaﬀected price ˆP

Figure 6: Evolution of the inventory ˆX and of the forecast residual demand D

Next, we plot trajectories with the same set of parameters, but with p+ = 0.3 (i.e.
p− = 0.7), π− = −10 e·(MW)−1, δ− = −1500 MW. There are, in average, more negative
than positive jumps. Now

˜v(λ)(0, X0, Y0, D0) = 1756330e.

Figure 7 shows that the trading rate (ˆq(λ)

)t∈[0,T ] is increasing, which is consistent with
the submartingale property in Proposition 4.1: the deterministic part in (4.6) dominates
the stochastic part. Since negative jumps are more expected than negative jumps are, the

t

27

Control-2.0-1.5-1.0-0.50.00.51.01.52.00100002000030000400005000060000700008000090000Price without impactPrice with impact45505560657075800100002000030000400005000060000700008000090000Intraday inventory and final productionForecast residual demand01000020000300004000050000600000100002000030000400005000060000700008000090000agent ﬁrst sells a large number of shares in electricity with the hope to buy it later at a lower
price thanks to the possible occurrence of jumps, that should be mainly negative. Here,
the control reacts to the negative price jumps by an increase in the trading rate. Finally,
in Figure 9 we observe the convexity of the trajectory of the optimal inventory ( ˆXt)t∈[0,T )
process, as expected from Remark 4.1. We also plot the production ˆξT at the ﬁnal time T
on that ﬁgure.

Figure 7: Evolution of the trading rate control ˆq(λ)

Figure 8: Simulation of the quoted impacted price ˆY and of the unaﬀected price ˆP

Figure 9: Evolution of the inventory ˆX and of the forecast residual demand D

28

Control-0.50.00.51.01.52.00100002000030000400005000060000700008000090000Price without impactPrice with impact303540455055600100002000030000400005000060000700008000090000Intraday inventory and final productionForecast residual demand-10000010000200003000040000500006000001000020000300004000050000600007000080000900005 Delay in production

In this section, we consider the more realistic situation when there is delay in the production,
assumed to be ﬁxed equal to h ∈ [0, T ], and we denote by v = vh the value function to the
associated optimal execution problem, as deﬁned in (2.9), where we stress the dependence
in the delay h. Our aim is to show how one can reduce the problem with delay to a suitable
problem without delay, and then solve it explicitly. We shall consider the problem without
jumps on demand forecast and price, but the same argument also works for the case with
jumps.

5.1 Explicit solution with delay

For simplicity of presentation, and without loss of generality, we shall focus on the derivation
of the value function vh(t, x, y, d) for an initial time t = 0, and ﬁxed (x, y, d) ∈ R × R × R.
Given a control trading rate q ∈ A, and from pathwise uniqueness for the solution to the
dynamics (2.1), (2.7), (2.8), we observe that for any ξ ∈ L0(FT −h):






T −h,X 0,x
X 0,x
T + ξ = X
T
T −h,Y 0,y
Y 0,y
T −h
T = Y
T

T −h+ξ

a.s.

, D0,d

T = D

T −h,D0,d
T

T −h

a.s.

(5.1)

To alleviate notations, we shall omit the dependence in the ﬁxed initial conditions (x, y, d),
and simply write Xs = X 0,x
s , for s ≥ 0, vh = vh(0, x, y, d), and
J(0; q, ξ) = J(0, x, y, d; q, ξ) for the the cost functional in (2.10). By the tower property of
conditional expectations and from (5.1), the cost functional can be written, for all q ∈ A, ξ
∈ L0(FT −h), as:

, Ds = D0,d

, Ys = Y 0,y

s

s

J(0; q, ξ)
(cid:104) (cid:90) T −h

= E

0
(cid:104) (cid:90) T −h

≥ E

0

(cid:105)
(cid:0)Ys + γqs)ds + c(ξ) + J(T − h, XT −h + ξ, YT −h, DT −h; q, 0)

qs

(5.2)

(cid:105)
(cid:0)Ys + γqs)ds + c(ξ) + vN P (T − h, XT −h + ξ, YT −h, DT −h)

,

qs

by deﬁnition (3.8) of the value function vN P for the optimal execution problem without
production, i.e. the pure retailer problem. Since q is arbitrary in A, this shows that:

J(0; q, ξ)

inf
q∈A

≥ inf
q∈A

(cid:104) (cid:90) T −h

E

0

(cid:0)Ys + γqs)ds + c(ξ) + vN P (T − h, XT −h + ξ, YT −h, DT −h)

qs

(cid:105)
,

(5.3)

for all ξ ∈ L0(FT −h). Now, given q ∈ A, and ξ ∈ L0(FT −h), let us consider the trading rate
ˆqN P,ξ in AT −h solution to the pure retailer problem: vN P (T − h, XT −h + ξ, YT −h, DT −h),
hence starting at time T − h from an inventory XT −h + ξ. By considering the process ˜q ∈
A deﬁned by: ˜qs = qs for 0 ≤ s < T − h, and ˜qs = ˆqN P,ξ
, for T − h ≤ s ≤ T , we then obtain
from (5.2):

s

J(0; ˜q, ξ)
(cid:104) (cid:90) T −h

= E

0

(cid:105)
(cid:0)Ys + γqs)ds + c(ξ) + vN P (T − h, XT −h + ξ, YT −h, DT −h)

,

qs

(5.4)

29

which proves together with (5.3) the equality:

J(0; q, ξ)

inf
q∈A

= inf
q∈A

(cid:104) (cid:90) T −h

E

0

(cid:0)Ys + γqs)ds + c(ξ) + vN P (T − h, XT −h + ξ, YT −h, DT −h)

qs

(cid:105)
,

(5.5)

for all ξ ∈ L0(FT −h). Therefore, vh = inf q∈A,ξ∈L0

+(FT −h) J(0; q, ξ) can be written as:

vh =

inf
q∈A,ξ∈L0

+(FT −h)

(cid:104) (cid:90) T −h

E

0

(cid:0)Ys + γqs)ds

qs

(cid:105)
+ c(ξ) + vN P (T − h, XT −h + ξ, YT −h, DT −h)

.

(5.6)

In other words, the original problem with delay in production is formulated as an opti-
mal execution problem without delay, namely with ﬁnal horizon T − h, and terminal cost
function:

Ch(x, y, d, ξ)

:= c(ξ) + vN P (T − h, x + ξ, y, d).

Notice from the explicit expression of vN P in Remark 3.1 that this cost function Ch does
not depend on T , and is in the form:

Ch(x, y, d, ξ) = Ch(0, y, d − x − ξ, 0) = c(ξ) + vN P (T − h, 0, y, d − x − ξ).

The optimization over q and ξ in (5.6) is done separately: the production ξ ∈ L0
+(FT −h) is
decided at time T − h, after the choice of the trading rate (qs) for 0 ≤ s ≤ T − h (leading
to an inventory XT −h), and is determined optimally from the optimization a.s. at T − h
of the terminal cost Ch(XT −h, YT −h, DT −h, ξ). It is then given in feedback form by ξ∗
T −h =
ˆξh,+(DT −h − XT −h, YT −h) where

ˆξh,+(d, y)

:= arg min

ξ≥0

Ch(0, y, d − ξ, 0) = arg min

ξ≥0

(cid:2)c(ξ) + vN P (T − h, 0, y, d − ξ)(cid:3),

hence explicitly given from the expression of vN P in Remark 3.1 by:

ˆξh,+(d, y) = ˆξh(d, y)1 ˆξh(d,y)≥0,

ˆξh(d, y)

:=

η
η + β

(cid:104) (νh + 2γ)(µh + d) + hy
(r(η, β) + ν)h + 2γ

(cid:105)
.

(5.7)

The problem (5.6) is then rewritten as

vh = inf
q∈A

(cid:104) (cid:90) T −h

E

qs

0

(cid:0)Ys + γqs)ds + C+

(cid:105)
h (DT −h − XT −h, YT −h)

,

(5.8)

where

C+

h (d, y)

:= Ch(0, y, d − ˆξh,+(d), 0).

Notice that when h = 0, we retrieve the expressions in the no delay case: ˆξ0,+ = ˆξ+ in
(3.1), C+
0 = C+ in (3.3) and v0 = v in (3.2). As in the no delay case, there is no explicit
solution to the HJB equation associated to the stochastic control problem (5.8). We then

30

consider the approximate control problem where we relax the non negativity constraint
on the production, i.e. ˜vh = inf q∈A,ξ∈L0(FT −h) J(0; q, ξ). Therefore by following the same
arguments as above, the corresponding value function is written as:

˜vh = inf
q∈A

(cid:104) (cid:90) T −h

E

0

(cid:105)
(cid:0)Ys + γqs)ds + ˜Ch(DT −h − XT −h, YT −h)

,

qs

(5.9)

where

˜Ch(d, y)

:= Ch(0, y, d − ˆξh(d), 0).

From the explicit expressions of ˆξh in (5.7) and vN P in Remark 3.1, it appears after some te-
dious but straightforward calculations that the auxiliary terminal cost function ˜Ch simpliﬁes
remarkably into:

˜Ch(d, y) = ˜v0(T − h, 0, y, d) + Kh,

where ˜v0 is the auxiliary value function without delay explicitly obtained in Theorem 3.1,
and Kh is a constant depending only on the delay h and the parameters of the model, given
explicitly by

Kh =

η2
2

0 + σ2
σ2

dν2 + 2ρσ0σdν

(η + β)(η + ν)(r(η, β) + ν)
(cid:16)

0 + σ2
σ2

h

+ γ

− γ

0 + σ2
σ2

dη2 − 2ρσ0σdη
(η + ν)2
dr2(η, β) − 2ρσ0σdr(η, β)

(η + ν)h
2γ
(cid:16)

1 +

ln

(cid:17)

ln

1 +

(r(η, β) + ν)2

(r(η, β) + ν)h
2γ

(cid:17)

.

One easily checks that Kh = 0 for h = 0, and Kh is increasing with h (actually the derivative
of Kh w.r.t. h is positive), hence in particular Kh is nonnegative. Plugging into (5.9), we
then get

˜vh = inf
q∈A

(cid:104) (cid:90) T −h

E

0

(cid:105)
(cid:0)Ys + γqs)ds + ˜v0(T − h, XT −h, YT −h, DT −h)

qs

+ Kh. (5.10)

Therefore, by using the dynamic programming principle for the control problem ˜v0 =
˜v0(0, x, y, d) in (3.4), we obtain this remarkable relation

˜vh = ˜v0 + Kh,

(5.11)

which explicitly relates the (approximate) value function with and without delay. As ex-
pected from the very deﬁnition of ˜vh, this relation implies that ˜vh − ˜v0 is nonnegative, and
is increasing in h. This is consistent with the intuition that when making the production
choice in advance, we do not take into account the future movements of the price and of
the residual demand, which should therefore lead to an average positive correction of the
cost. More precisely, the relation (5.11) gives an explicit quantiﬁcation of the delay impact
via the term Kh (which does not depend on the state variables x, y, d) in function of the
various model parameters. Moreover, the optimal control of the stochastic control problem
(5.10) over [0, T − h) is explicitly given by the optimal control (ˆqs)0≤s≤T −h of problem ˜v0
without delay in Theorem 3.1.

Let us now consider the following strategy (ˆqh,+, ˜ξh,∗

T −h) ∈ A × L0

+(FT −h) for the original

problem vh with delay:

31

• Before T − h, follow the trading strategy ˆqh,+

s = ˆqs, s < T − h, corresponding to the
solution of the auxiliary problem without delay as if production choice is made at time
T , and leading to an inventory ˆXT −h, and an impacted price ˆYT −h.

• At time T − h, choose the production quantity:

˜ξh,∗
T −h

:= ˆξh,+(DT −h − ˆXT −h, ˆYT −h).

• Between time T −h and T , follow the trading strategy ˆqh,+

, T −h ≤ s ≤ T ,
corresponding to the solution of the problem without production, and starting at T −h
from an inventory ˆXT −h + ˜ξh,∗

T −h.

N P, ˜ξh,∗
T −h
s = ˆq
s

In order to estimate the quality of this approximate strategy with respect to the optimal
trading problem vh, measured by

E h
1

:= J(0; ˆqh,+, ˜ξh,∗

T −h) − vh,

we shall compare it with the following strategy (ˆqh, ˆξh

T −h) ∈ A × L0(FT −h):

• Before T − h, follow the trading strategy ˆqh

s = ˆqs, s < T − h, corresponding to the
solution of the auxiliary problem without delay as if production choice is made at time
T , and leading to an inventory ˆXT −h, and an impacted price ˆYT −h.

• At time T − h, choose the “production” quantity (which can be negative):

T −h = ˆξh(DT −h − ˆXT −h, ˆYT −h).
ˆξh

• Between time T − h and T , follow the trading strategy ˆqh

, T − h ≤ s ≤ T ,
corresponding to the solution of the problem without production, and starting at T −h
from an inventory ˆXT −h + ˆξh

T −h

T −h.

N P, ˆξh
s = ˆq
s

Then, by construction and following the arguments (see in particular (5.4), (5.9), (5.10))
leading to the expression (5.11) of ˜vh, we see that (ˆqh, ˆξh
T −h) is the optimal solution for ˜vh,
i.e. ˜vh = J(0; ˆqh, ˆξh
T −h), we deduce
that

T −h). On the other hand, since ˜vh ≤ vh ≤ J(0; ˆqh,+, ˜ξh,∗

max(vh − ˜vh, E h

1 ) ≤ ¯E h := J(0; ˆqh,+, ˜ξh,∗

T −h) − J(0; ˆqh, ˆξh

T −h).

Now, from the expression (5.4) of J, and by same arguments as in the proof of Proposition 3.2
(see the derivation of relation (3.15)), we have

(cid:104)
¯E h = E
(cid:104)
= E

h (DT −h − ˆXT −h, ˆYT −h) − ˜Ch(DT −h − ˆXT −h, ˆYT −h)
C+
vN P (T − h, 0, ˆYT −h, DT −h − ˆXT −h − ˜ξh,∗
− vN P (T − h, 0, ˆYT −h, DT −h − ˆXT −h − ˆξh

T −h) + c( ˜ξh,∗
T −h)
T −h) − c( ˆξh

(cid:105)

T −h)

(cid:105)

=

ηr(η, β)
2β

(r(η, β) + ν)h + 2γ
(η + ν)h + 2γ

Vh(T )ψ

(cid:16) m(T, d − x, y)
(cid:112)Vh(T )

(cid:17)

32

where m and ψ are deﬁned as in (3.12), and

Vh(T ) =

(cid:90) T

h

0s2 + σ2
σ2

d(νs + 2γ)2 + 2ρσ0σds(νs + 2γ)
(cid:2)(r(η, β) + ν)s + 2γ(cid:3)2

ds.

We recover when h = 0 the expression in Proposition 3.2 of the error in the no delay case,
and notice that ¯E h decreases when the delay increases:
indeed, the error comes from the
trading procedure before deciding how much to produce, which is dictated by the auxiliary
problem, in which the ﬁnal “production” can be negative. After T − h, the followed control
is optimal, as there remains no production decision at some further date. The shorter the
period before making the production decision is, the weaker the error is.

Let us ﬁnally discuss some properties of the (approximate) optimal trading strategy
ˆqh,+. Recalling from Proposition 3.1 that the optimal trading rate is a martingale in the no
delay case, we see by construction of (ˆqh,+
)0≤s≤T that it is a martingale on [0, T − h) and
a martingale on [T − h, T ]. Moreover, for any s ∈ [T − h, T ], and t ∈ [0, T − h), we have

s

E(cid:2)ˆqh,+
s

|Ft

N P, ˜ξh,∗
(cid:3) = E(cid:2)E(cid:2)ˆq
T −h
s

|FT −h
(cid:104) η(µh + DT −h − ˆXT −h − ˜ξh,∗

(cid:3)|Ft

(cid:3) = E(cid:2)ˆq

N P, ˜ξh,∗
T −h
T −h

(cid:3)

|Ft

T −h) − ˆYT −h

= E

= E

= E

(η + ν)h + 2γ
(cid:104) η(µh + DT −h − ˆXT −h − ˆξh
(η + ν)h + 2γ
(cid:104) ˆξh
E

η
(η + ν)h + 2γ

+

T −h − ˜ξh,∗

T −h

(cid:105)

(cid:12)
(cid:12)Ft

T −h) − ˆYT −h

(cid:105)

(cid:12)
(cid:12)Ft

(cid:105)

(cid:12)
(cid:12)Ft

(cid:105)

(cid:12)
(cid:12)Ft

+

(cid:104) r(η, β)(µh + DT −h − ˆXT −h) − ˆYT −h
(r(η, β) + ν)h + 2γ
(cid:104) ˆξh
η
E
(η + ν)h + 2γ
η
(cid:3) +
(η + ν)h + 2γ
(cid:104) ˆξh
1 ˆξh
E

T −h − ˜ξh,∗
(cid:104) ˆξh
E

η
(η + ν)h + 2γ

T −h<0

(cid:12)
(cid:12)Ft

(cid:12)
(cid:12)Ft

T −h

T −h

(cid:105)

T −h − ˜ξh,∗
(cid:105)

T −h

= E(cid:2)ˆqT −h|Ft

= ˆqt +

(cid:105)

(cid:12)
(cid:12)Ft

≤ ˆqt = ˆqh,+

t

.

(5.12)

where we used the tower rule for conditional expectations, the martingale property and the
explicit expression of qN P, ˜ξh,∗
T −h in Remark 3.1, the deﬁnition of ˆξh
T −h, the martingale property
and explicit expression of ˆq in Theorem 3.1, and ﬁnally the fact that ˜ξh,∗
T −h = ˆξh
T −h≥0.
This shows in particular the supermartingale property of ˆqh,+ over the whole period [0, T ].
Notice that the same arguments as for the derivation of (5.12) shows the martingale property
over the whole period [0, T ] of the optimal trading strategy ˆqh associated to the auxiliary
problem ˜vh. Moreover, by the martingale property of ˆqh,+ on [0, T − h), and relation (5.12),
we see that the (approximate) optimal inventory process ˆX h,+ with trading rate ˆqh,+ has
on average, a growth rate dE[ ˆX h,+

, which is piecewise constant, equal to:

1 ˆξh

T −h

]

s
ds

E[ˆqh,+
s

] =

(cid:40) ˆq0,
ˆq(h)
0

:= ˆq0 +

η
(η+ν)h+2γ

E(cid:2) ˆξh

T −h

1 ˆξh

T −h<0

(cid:3) < ˆq0,

for 0 ≤ s < T − h
for T − h ≤ s ≤ T,

33

with ˆq0 = r(η,β))(µT +d−x)−y

(r(η,β)+ν)T +2γ

, and

ˆq(h)
0

= ˆq0 −

ηr(η, β)
β((η + ν)h + 2γ)

(cid:112)Vh(T ) ˜ψ

(cid:16) m(T, d − x, y)
(cid:112)Vh(T )

(cid:17)

,

where

˜ψ(z)

:= φ(z) − zΦ(−z),

z ∈ R

is a nonnegative function, as pointed out in (3.17).

5.2 Numerical results

We plot ﬁgures showing relevant trajectories with the same parameters as in Section 3.3.2.
We add a delay h = 4 hours: the production choice has to be made four hours before the
end of the trading period. We have

˜vh(0, X0, Y0, D0) = 1925460e,

which is slightly higher than the value ˜v0(0, X0, Y0, D0) = 1916700e without delay.
On Figure 10, we see that at time T − h, the positive production choice ˜ξh,∗

T −h is made,
and then we go on buying shares on the intraday market in order to go nearer to the demand
forecast, with a smaller slope of trading rate. On Figure 11, which represents the control
process without the last hour of trading (because oscillations then become overwhelming),
we see that after date T − h, as we do not plan to use ﬁnal production leverage any more,
the approximate optimal control process ˆqh,+ oscillates a lot as we are approaching the end
of trading time. We can compare with Figure 1 to assert that qualitatively, the control
in the problem with no production oscillates more than the one in the problem with ﬁnal
production, as in the former problem, the intraday market is the only way to seek to reach
the equilibrium.

Figure 10: Evolution of the inventory ˆX (with production choice at time T − h) and of the forecast
residual demand D

34

Contracts bought on marketForecast residual demand01000020000300004000050000600000100002000030000400005000060000700008000090000Figure 11: Evolution of the trading rate control ˆqh,+ without the last hour

A Appendix

A.1 Proof of Theorem 3.1

The Hamilton-Jacobi-Bellman (HJB) equation arising from the dynamic programming as-
sociated to the stochastic control problem (3.4) is:






(cid:2)q

+ inf
q∈R

∂˜v
∂˜v
∂t
∂d
˜v(T, x, y, d) = ˜C(d − x) = 1

∂˜v
∂x

∂˜v
∂y

+ νq

+ µ

+

1
2

∂2˜v
∂y2 +

1
σ2
0
2
2 r(η, β)(d − x)2.

σ2
d

∂2˜v
∂d2 + ρσ0σd

∂2˜v
∂y∂d

+ q(y + γq)(cid:3) = 0,

The argmin in HJB is attained for

˜q(t, x, y, d) = −

1
2γ

(cid:2) ∂˜v
∂x

+ ν

∂˜v
∂y

+ y(cid:3),

and the HJB equation is rewritten as:






+ µ

∂2˜v
∂˜v
∂˜v
1
σ2
∂y2 +
0
∂t
∂d
2
˜v(T, x, y, d) = 1
2 r(η, β)(d − x)2.

σ2
d

1
2

+

∂2˜v
∂d2 + ρσ0σd

∂2˜v
∂y∂d

−

1
4γ

(cid:2) ∂˜v
∂x

+ ν

∂˜v
∂y

+ y(cid:3) = 0,

(A.1)

We look for a candidate solution to HJB in the form

˜w(t, x, y, d) = A(T − t)(d − x)2 + B(T − t)y2 + F (T − t)(d − x)y

+ G(T − t)(d − x) + H(T − t)y + K(T − t),

(A.2)

for some deterministic functions A, B, F , G, H and K. Plugging the candidate function ˜w
into equation (A.1), we see that ˜w is solution to the HJB equation iﬀ the following system
of ordinary diﬀerential equations (ODEs) is satisﬁed by A, B, F , G, H and K:






A(cid:48) + 1

B(cid:48) + 1

4γ (−2A + νF )2 = 0
4γ (2νB − F + 1)2 = 0
2γ (−2A + νF )(2νB − F + 1) = 0
2γ (−2A + νF )(−G + νH) = 0
2γ (2νB − F + 1)(−G + νH) = 0
4γ (−G + νH)2 = 0

dA + ρσ0σdF ) + 1

F (cid:48) + 1
G(cid:48) − 2µA + 1

H (cid:48) − µF + 1
0B + σ2

K(cid:48) − µG − (σ2

35

Control0.100.150.200.250.300.350100002000030000400005000060000700008000090000with the initial conditions A(0) = 1
K(0) = 0. We ﬁrst solve the Riccati system relative to the triple (A, B, F ), and obtain:

2 r(η, β), B(0) = 0, F (0) = 0, G(0) = 0, H(0) = 0,

(cid:40)

A(t) =
B(t) = − 1
2

r(η,β)( ν
(r(η,β)+ν)t+2γ ,

2 t+γ)

t

(r(η,β)+ν)t+2γ , F (t) =

r(η,β)t
(r(η,β)+ν)t+2γ .

(A.3)

Then we solve the ﬁrst-order linear system of ODE relative to the pair (G, H), which leads
to the explicit solution:

G(t) = 2µtA(t),

and H(t) = −2r(η, β)µtB(t).

(A.4)

Finally, we explicitly obtain K from the last equation:

K(t) = γ

0 + σ2
σ2

dr2(η, β) − 2ρσ0σdr(η, β)

(cid:0)r(η, β) + ν(cid:1)2

(cid:16)

ln

1 +

(r(η, β) + ν)t
2γ

(cid:17)

+

dr(η, β)ν + 2ρσ0σdr(η, β) − σ2
σ2
0
2(cid:0)r(η, β) + ν(cid:1)

t +

r(η, β)µ2t2( ν
2 t + γ)
(r(η, β) + ν)t + 2γ

.

(A.5)

By construction, ˜w in (A.2) with A, B, F , G, H and K explicitly given by (A.3)-(A.4)-
(A.5), is a smooth solution with quadratic growth condition to the HJB equation (A.1).
Moreover, the argmin in HJB equation for ˜w is attained for

˜q(t, x, y, d) = −

+ ν

1
2γ

+ y(cid:3)

(cid:2) ∂ ˜w
∂x

∂ ˜w
∂y
r(η, β)(µ(T − t) + d − x) − y
(r(η, β) + ν)(T − t) + 2γ

=

=: ˆq(T − t, d − x, y).

s

Notice that ˆq is linear, and Lipschitz in x, y, d, uniformly in time t, and so given an initial
state (x, y, d) at time t, there exists a unique solution ( ˆX t,x,y,d, ˆY t,x,y,d, Dt,d)t≤s≤T to (2.1)-
(2.7)-(2.8) with the feedback control ˆqs = ˆq(T − s, Dt,d
), which satisﬁes:
E[supt≤s≤T | ˆX t,x,y,d
|ˆqs|2ds]
< ∞, hence ˆq ∈ At. We now call on a classical veriﬁcation theorem (see e.g. Theorem 3.5.2
in [8]), which shows that ˜w is indeed equal to the value function ˜v, and ˆq is an optimal
control. Finally, once the optimal trading rate ˆq is determined, the optimal production is
obtained from the optimization over ξ ∈ R of the terminal cost C(Dt,d
, ξ), hence
given by: ˆξT = η
(cid:3)
).

s − ˆX t,x,y,d
s
s |2] < ∞. This implies in particular that E[(cid:82) T

T − ˆX t,x,y,d

|2+| ˆY t,x,y,d
s

, ˆY t,x,y,d
s

|2+|Dt,d

T − ˆX t,x,y,d

η+β (Dt,d

T

T

t

A.2 Proof of Theorem 4.1

The Hamilton-Jacobi-Bellman (HJB) integro-diﬀerential equation arising from the dynamic
programming associated to the stochastic control problem ˜v = ˜v(λ) with jumps in the dy-
namics of Y and D is:

(cid:2)q

+ inf
q∈R

∂˜v(λ)
∂x


∂˜v(λ)
1

+
∂t
2
+ λ(cid:2)p+˜v(λ)(t, x, y + π+, d + δ+) + p−˜v(λ)(t, x, y + π−, d + δ−) − ˜v(λ)(t, x, y, d)(cid:3) = 0

˜v(λ)(T, x, y, d) = ˜C(d − x) = 1

∂2˜v(λ)
∂d2 + ρσ0σd

∂2˜v(λ)
∂y2 +

∂2˜v(λ)
∂y∂d

∂˜v(λ)
∂y

∂˜v(λ)
∂d

+ νq

+ µ

σ2
d

σ2
0

1
2

2 r(η, β)(d − x)2.

+ q(y + γq)(cid:3)

36

Notice that with respect to the no jump case, there is in addition a linear integro-diﬀerential
term in the HJB equation (which does not depend on the control), and the argmin is attained
as in the no jump case for

˜q(λ)(t, x, y, d) = −

1
2γ

(cid:2) ∂˜v(λ)
∂x

+ ν

∂˜v(λ)
∂y

+ y(cid:3).

The HJB equation is then rewritten as

+ µ

∂˜v(λ)
∂d


∂2˜v(λ)
∂˜v(λ)
+ y(cid:3)

∂d2 + ρσ0σd
∂t
+ λ(cid:2)p+˜v(λ)(t, x, y + π+, d + δ+) + p−˜v(λ)(t, x, y + π−, d + δ−) − ˜v(λ)(t, x, y, d)(cid:3) = 0

˜v(λ)(T, x, y, d) = 1

∂2˜v(λ)
∂y2 +

(cid:2) ∂˜v(λ)
∂x

∂2˜v(λ)
∂y∂d

∂˜v(λ)
∂y

1
4γ

+ ν

σ2
d

σ2
0

1
2

1
2

+

−

2 r(η, β)(d − x)2.

(A.6)

We look again for a candidate solution to (A.6) in the form

˜w(λ)(t, x, y, d) = Aλ(T − t)(d − x)2 + Bλ(T − t)y2 + Fλ(T − t)(d − x)y

+ Gλ(T − t)(d − x) + Hλ(T − t)y + Kλ(T − t),

(A.7)

for some deterministic functions Aλ, Bλ, Fλ, Gλ, Hλ and Kλ. Plugging the candidate
function ˜w(λ) into equation (A.6), we see that ˜w(λ) is solution to the HJB equation iﬀ the
following system of ordinary diﬀerential equations (ODEs) is satisﬁed by Aλ, Bλ, Fλ, Gλ,
Hλ and Kλ:






λ + 1

A(cid:48)
λ + 1

4γ (−2Aλ + νFλ)2 = 0
4γ (2νBλ − Fλ + 1)2 = 0
2γ (−2Aλ + νFλ)(2νBλ − Fλ + 1) = 0
2γ (−2Aλ + νFλ)(−Gλ + νHλ) − λ(2δAλ + πFλ) = 0
2γ (2νBλ − Fλ + 1)(−Gλ + νHλ) − λ(2πBλ + δFλ) = 0

λ + 1
F (cid:48)

B(cid:48)

λ − 2µAλ + 1
G(cid:48)
λ − µFλ + 1
H (cid:48)

K(cid:48)

λ − µGλ − (σ2

dAλ + ρσ0σdFλ) + 1
4γ (−Gλ + νHλ)2
−λ[(p+(δ+)2 + p−(δ−)2)Aλ + (p+(π+)2 + p−(π−)2)Bλ

0Bλ + σ2

+(p+δ+π+ + p−δ−π−)Fλ + δGλ + πHλ] = 0

with the initial conditions Aλ(0) = 1
2 r(η, β), Bλ(0) = 0, Fλ(0) = 0, Gλ(0) = 0, Hλ(0) = 0,
Kλ(0) = 0. We ﬁrst solve the Riccati system relative to the triple (Aλ, Bλ, Fλ), which is
the same as in the no jump case, and therefore obtain: Aλ = A, Bλ = B, Fλ = F as in
(A.3). Then we solve the ﬁrst-order linear system of ODE relative to the pair (Gλ, Hλ),
which involves the jump parameters λ, π and δ, and get:

Gλ(t) = G(t) +

Hλ(t) = H(t) −

λ
2
λ
2

r(η, β)t(πt + 2δ(νt + 2γ))
(r(η, β) + ν)t + 2γ

,

(π − 2r(η, β)δ)t2
(r(η, β) + ν)t + 2γ

,

37

where G and H are given from the no jump case (A.4). Finally, after some tedious but
straightforward calculations, we explicitly obtain Kλ from the last equation:

Kλ(t) = K(t) + λγ

p+(π+ − r(η, β)δ+)2 + p−(π− − r(η, β)δ−)2
(cid:0)r(η, β) + ν(cid:1)2

(cid:16)

ln

1 +

(r(η, β) + ν)t
2γ

(cid:17)

−

+

λ
2
λr(η, β)
2

p+((π+)2 − r(η, β)δ+(2π+ + νδ+)) + p−((π−)2 − r(η, β)δ−(2π− + νδ−))
r(η, β) + ν

t

2νµδ + λ((p+)2δ+(π+ + νδ+) + (p−)2δ−(π− + νδ−))
r(η, β) + ν

t2

+ λ2γr(η, β)

r(η, β)δ2 + 2νp+p−δ+δ− − ((p+)2δ+π+ + (p−)2δ−π−)
(r(η, β) + ν)(cid:0)(r(η, β) + ν)t + 2γ(cid:1)

t2

+

+

+

2λγr(η, β)2µδ

(r(η, β) + ν)(cid:0)(r(η, β) + ν)t + 2γ(cid:1) t2 −
2νδ+δ− + δ−π+ + δ+π−
λ2p+p−r(η, β)
(r(η, β) + ν)t + 2γ
2

t3

λ2π2
48γ

t3

1
8

4r(η, β)µλπ − λ2π2
(r(η, β) + ν)t + 2γ

t3,

with K in (A.5). The function ˜w(λ) in (A.7) may thus be rewritten as the sum of ˜w in
(A.2) and another function of t, d − x and y, and is by construction a smooth solution
with quadratic growth condition to the HJB equation (A.6). Moreover, the argmin in HJB
equation for ˜w(λ) is attained for

˜q(λ)(t, x, y, d) = −

1
2γ

(cid:2) ∂ ˜w(λ)
∂x

+ ν

∂ ˜w(λ)
∂y

+ y(cid:3)

=

r(η, β)(µ(T − t) + d − x) − y
(r(η, β) + ν)(T − t) + 2γ
r(η, β)δ(T − t) + π

+ λ

4γ (r(η, β) + ν)(T − t)2

(r(η, β) + ν)(T − t) + 2γ

=: ˆq(λ)(T − t, d − x, y).

s = ˆq(λ)(T − s, Dt,d

Again, notice that ˆq(λ) is linear, and Lipschitz in x, y, d, uniformly in time t, and so given an
initial state (x, y, d) at time t, there exists a unique solution ( ˆX t,x,y,d, ˆY t,x,y,d, Dt,d)t≤s≤T to
(2.1)-(4.3)-(4.1) with the feedback control ˆq(λ)
s − ˆX t,x,y,d
), which
s
satisﬁes: E[supt≤s≤T | ˆX t,x,y,d
s |2] < ∞, see e.g. Theorem 1.19 in [7]. This
s
implies that E[(cid:82) T
|2ds] < ∞, hence ˆq(λ) ∈ At. We now call on a classical veriﬁcation
t
theorem for stochastic control of jump-diﬀusion processes (see e.g. Theorem 3.1 in [7]),
which shows that ˜w(λ) is indeed equal to the value function ˜v(λ), and ˆq(λ) is an optimal
control. Finally, once the optimal trading rate ˆq(λ) is determined, the optimal production is
obtained from the optimization over ξ ∈ R of the terminal cost C(Dt,d
, ξ), hence
given by: ˆξ(λ)
(cid:3)
).

T − ˆX t,x,y,d

|2 +| ˆY t,x,y,d
s

|2 +|Dt,d

, ˆY t,x,y,d
s

|ˆq(λ)
s

T = η

η+β (Dt,d

T − ˆX t,x,y,d

T

T

38

References

[1] R. Aïd. Electricity Derivatives. Springer Briefs in Quantitative Finance. Springer-Verlag, 2015.

[2] R. Almgren and N. Chriss. Optimal execution of portfolio transactions. Journal of Risk, 3:5–39,

2000.

[3] A. Bensoussan, P. Bertrand and A. Brouste. A generalized model approach to seasonal aspects

of wind speed modeling. Journal of Applied Statistics, 41(8):1694–1707, 2014.

[4] E. Garnier and R. Madlener. Balancing forecast errors in continuous-trade intraday markets.

FCN WP 2/2014, RWTH Aachen University School of Business and Economics, 2014.

[5] G. Giebel, G. Kariniotakis, R. Brownsword, M. Denhard and C. Draxl. The state-of-the-art in
short-term prediction of wind power. A literature overview. 2nd Edition. In Deliverable Report
D1.2 of the Anemos Project (ENK5-CT-2002-00665), 2011.

[6] A. Henriot. Market design with centralised wind power management: handling low-predictability

in intraday markets. The Energy Journal, 35(1):99–117, 2014.

[7] B. Øksendal and A. Sulem. Applied stochastic control of jump diﬀusions. Universitext. Springer,

Berlin, second edition, 2007.

[8] H. Pham. Continuous-time stochastic control and optimization with ﬁnancial applications, Vol.

61 of Stochastic Modelling and Applied Probability. Springer-Verlag, Berlin, 2009.

[9] A. Schied and A. Slynko. Some mathematical aspects of market impact modeling. In Surveys
in stochastic processes, EMS Ser. Congr. Rep., pages 153–179. Eur. Math. Soc., Zürich, 2011.

[10] D. Williams. Probability with martingales. Cambridge mathematical text, 1991.

39

