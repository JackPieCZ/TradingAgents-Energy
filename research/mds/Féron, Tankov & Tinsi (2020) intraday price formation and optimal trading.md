Article
Price Formation and Optimal Trading in Intraday
Electricity Markets with a Major Player

Olivier Féron 1

, Peter Tankov 2,* and Laura Tinsi 1,2

Electricité de France R&D, 91120 Palaiseau, France; olivier-2.feron@edf.fr (O.F.); laura.tinsi@ensae.fr (L.T.)

1
2 CREST, ENSAE, Institut Polytechnique de Paris, 91120 Palaiseau, France
* Correspondence: peter.tankov@ensae.fr

Received: 9 November 2020; Accepted: 2 December 2020; Published: 7 December 2020

Abstract: We study price formation in intraday electricity markets in the presence of intermittent
renewable generation. We consider the setting where a major producer may interact strategically
with a large number of small producers. Using stochastic control theory, we identify the optimal
strategies of agents with market impact and exhibit the Nash equilibrium in a closed form in the
asymptotic framework of mean ﬁeld games with a major player.

Keywords: intraday electricity market; renewable energy; mean ﬁeld games; major player

1. Introduction

The structure of electricity markets around the world has been profoundly transformed by the
push towards liberalization in the late 90s and, more recently, by the massive arrival of renewable
energy production. Distribution has been separated from production, and, where, in the past, a single
producer could own the entire generation capacity of a given country or region, now a patchwork of
small, often renewable, generators competes with a big historical producer.

The aim of this paper is to develop an equilibrium model for intraday electricity markets where
a big producer with a signiﬁcant market share competes with a large number of small renewable
producers. The large producer and the small producers both use the intraday markets in order to
compensate their production and demand forecast errors, creating feedback effects on the market
price. The large producer can act strategically, anticipating the impact of its decisions on the market
prices and, thus, on the behavior of the small agents. The small agents are not strategic, and each one
has a negligible effect on the market; however, the behavior of all small agents taken together has a
signiﬁcant market impact. The large player has the ﬁrst-mover advantage, but it does not observe the
forecast of the minor players. These, in turn, have the information advantage, since they observe the
forecast of the major player as well as their own forecast. This leads to a stochastic leader-follower
game, where players interact through the market price. We place ourselves in the linear-quadratic
setting, exhibit the unique Nash equilibrium for this game in closed form in the framework of mean
ﬁeld games with a major player, and provide explicit formulas for the market price and the strategies
of the agents. For a game with a ﬁnite number of players, we show how an ε-Nash equilibrium can be
constructed from the mean ﬁeld game solution.

This paper is a companion paper to Féron et al. (2020), where a similar model is developed for
the case of identical agents with symmetric interactions, and we refer the readers to that paper for
a detailed review of literature on the stochastic and econometric modeling of intraday electricity
markets. Here, we simply mention that a similar linear-quadratic setting with linear market impact
has been used in order to determine optimal strategies for a single energy producer by Aïd et al. (2016)
and Tan and Tankov (2018), while Bouchard et al. (2018) found an analytic expression for the
equilibrium price in a linear-quadratic model of the stock market with symmetric interactions and

Risks 2020, 8, 133; doi:10.3390/risks8040133

www.mdpi.com/journal/risks

risks(cid:1)(cid:2)(cid:3)(cid:1)(cid:4)(cid:5)(cid:6)(cid:7)(cid:8)(cid:1)(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:6)(cid:7)Risks 2020, 8, 133

2 of 21

perfect information. We also mention the recent paper of Aïd et al. (2020), where an equilibrium
in complete information setting for a ﬁnite number of agents is derived in the intraday electricity
market. This paper is close in spirit to the complete information framework of Féron et al. (2020),
but it allows for treating the case of heterogeneous agents in conditions of uncertain production with
possible outages and uncertain demand. However, the complete information setting, where each agent
observes all other agents’ forecasts, does not seem to be realistic in electricity markets. The incomplete
information setting, where each agent only observes its own forecast and the aggregate forecast, may
not be tractable for a ﬁnite number of agents. Nevertheless, in Féron et al. (2020), it has been shown
that explicit solutions may be found in the mean ﬁeld limit, where the number of agents is sent to
inﬁnity, and the inﬂuence of every single agent on the entire market becomes negligible. The use
of mean ﬁeld theory for stochastic control with partial information has also recently been proposed
by Bensoussan and Yam (2019), in a formal fashion, in order to solve the associated Zakai equation.

The mean ﬁeld games (MFG) are stochastic differential games with inﬁnitely many players
and symmetric interactions. The seminal papers of Lasry and Lions (2007) and Huang et al. (2006)
characterized the Nash equilibrium in this framework through a coupled system of a
Hamilton–Jacobi–Bellman (HJB) and a Fokker–Planck (FP) equation. Carmona and Delarue (2018)
developed an alternative probabilistic approach that was inspired by the Pontryagin principle and
related the mean ﬁeld game solution to a McKean–Vlasov Forward Backward Stochastic Differential
Equation (FBSDE). The asymptotic results that were obtained in mean ﬁeld games can be used
to construct approximate equilibria (ε-Nash equilibria) for games with a ﬁnite number of players.
Alternatively, the equilibria of N-player games can be shown to converge to the corresponding weak
mean ﬁeld equilibria Lacker (2020).

While the original MFG setting involves symmetric agents, Huang (2010) introduced linear-quadratic
mean ﬁeld games with a major player. Nourian and Caines (2013) developed this approach in a general
framework. In both papers, the mean ﬁeld is exogenous to the actions of the major player. In contrast
to these two papers, Bensoussan et al. (2016) and Carmona and Zhu (2016) considered the endogenous
case, where the major player can inﬂuence the mean ﬁeld. In Bensoussan et al. (2016), this leads to
a leader-follower setting, also known as Stackelberg game. The authors derived a HJB equation and a
FP equation in order to characterize the solution in the general case, while the linear quadratic setting
was tackled with a stochastic maximum principle approach. More recently, Lasry and Lions (2018)
introduced a master equation accounting for this kind of major player model. Cardaliaguet et al. (2020)
showed that the two previous approaches (Lasry and Lions 2018; Carmona and Zhu 2016) lead to the
same Nash equilibria.

(2020),

Financial markets and energy systems with many small interacting agents are a natural domain of
applications of MFG. Casgrain and Jaimungal (2020) applied the MFG theory to optimal trade execution
with price impact and terminal inventory liquidation condition, Fujii and Takahashi (2020), used this
theory to ﬁnd an equilibrium price under market clearing conditions. In Casgrain and Jaimungal (2020)
and Fujii and Takahashi
the authors used the extended mean ﬁeld setting in
order to deal with heterogeneous sub-populations of agents and incomplete information
for Casgrain and Jaimungal (2020). Alasseur et al. (2020) developed a model for the optimal
management of energy storage and distribution in a smart grid system through an extended MFG.
Shrivats et al. (2020) recently applied the theoretical setting that was developed in Casgrain and
Jaimungal (2020) to the case of trading in solar renewable energy certiﬁcate markets. Financial markets
with a major player, leader–follower interactions, and terminal inventory constraint were recently
analyzed in (Evangelista and Thamsten 2020; Fu and Horst 2020). In Fu and Horst (2020), the authors
consider a Brownian ﬁltration, impose a zero terminal inventory constraint and characterize the
equilibrium in terms of a McKean-Vlasov FBSDE. In Evangelista and Thamsten (2020), the authors
study a market with a ﬁnite number of small players and a major player with ﬁrst-mover advantage
and information asymmetry, and characterize the solution in terms of a McKean–Vlasov FBSDE in a
more general setting than that of Fu and Horst (2020).

Risks 2020, 8, 133

3 of 21

Among the cited papers, our methods and ﬁndings are the closest in spirit to (Bensoussan et al.
2016; Evangelista and Thamsten 2020; Fu and Horst 2020). The main novelty of our paper is the
application of the linear quadratic MFG with a major player to the analysis of electricity markets
in the presence of renewable production; however, we also make a number of contributions to the
mathematical theory. When compared to the article Bensoussan et al. (2016), which, of course, solves a
more general problem, without focusing on a speciﬁc application, our paper allows a much more
general dynamics for the driving processes (general semimartingales) and does not require an a priori
bound on the strategies in order to prove the existence of the Nash equilibrium in the presence of a
major player. Unlike the articles (Evangelista and Thamsten 2020; Fu and Horst 2020), which also study
leader-follower games in ﬁnancial markets, we consider a stochastic terminal constraint, characterize
the equilibrium in explicit form, and show how an ε-Nash equilibrium for the ﬁnite-player game may
be constructed from a mean ﬁeld game solution.

The paper is organized, as follows. In Section 2, we introduce the model and brieﬂy recall the
mean ﬁeld game solution obtained in Féron et al. (2020) in the case of identical agents. In Section 3,
we present the main results of this paper in the setting allowing for the presence of a major player,
whose inﬂuence on the market is not negligible in the MFG limit. In Section 4, we show how the
limiting MFG solution may be used in order to construct an approximate Nash equilibrium in a
Stackelberg game with one major player and N minor players. Finally, in Section 5, equilibrium price
trajectories and the effect of market parameters on the price characteristics are illustrated with the
simulated data.

2. Preliminaries

In this paper, we place ourselves in the intraday market for a given delivery hour starting at time
T, where time 0 corresponds to the opening time of the market (in EPEX Intraday this happens at
3 p.m. on the previous day). In reality, trading stops a few minutes before delivery time (e.g., 5 min. for
Germany). However, for the sake of simplicity, we assume that market participants can trade during
the entire period [0, T]. In the market, there are agents (producers or consumers) that are assumed to
have taken a position in the day-ahead market and use the intraday market in order to manage the
volume risk that is associated to the imperfect demand/production forecast. These forecasts represent
the best estimate of the additional demand as compared to the position taken by the agent in the
spot market: to avoid imbalance penalties, the intraday position of the agent at the delivery date
must, therefore, be equal to the realized demand, or, in other words, the last observed value of the
demand forecast.

We consider the case of a Stackelberg game, where an agent, called a “major agent”, faces a large
number of smaller agents, called “minor agents”. We directly place ourselves in the setting of mean
ﬁeld games with a major player, that is, we assume that the number of small agents in the market is
inﬁnite, and the inﬂuence of each small agent on the market is negligible. Therefore, the aggregate
impact of the minor agents on the market is modelled through a mean ﬁeld.

Each agent observes the common national demand forecast and the demand forecast of the major
player. In addition, the small agents also observe their individual demand forecasts, which are not
observed by the other agents. Thus, the common ﬁltration of the market contains information about
the forecast of the major player and the common part of the forecasts of the minor players, but the
small agents beneﬁt from a private information advantage when compared to the major player.

The demand forecast process and position of the generic minor agent are given, respectively,
by X := (Xt)0≤t≤T and φ := (φt)0≤t≤T, while the forecast process and position of the major agent are
given, respectively, by (X0
t )t∈[0,T]. Note that the position and forecast of the minor and
major agents are not expressed in the same units. Indeed, in the mean ﬁeld game limit considered
in this paper, we assume that the market is very large, so that the position of every minor agent as
compared to the market size is negligible, but the major agent takes up a nonzero share of the market,
so that φ0 and X0 denote the position and forecast of the major agent normalized by the market size.

t )t∈[0,T] and (φ0

Risks 2020, 8, 133

4 of 21

We denote, by F, the ﬁltration that contains all information available to the generic minor agent
and by F0 the ﬁltration, which contains all information available to the major agent. This ﬁltration
contains the information about the fundamental price, the information about the demand forecast
of the major agent, and potentially some information regarding the demand forecast of the generic
minor agent (the common noise), but, in general, not the full individual demand forecast of the generic
minor agent.

(cid:82)

Throughout the paper and for any F-adapted process (ζt)t∈[0,T], we will denote ¯ζt = E[ζt|F 0
t (dx), where: µζ

t ] =
R xµζ
In view of the convergence results of Proposition 9 and
Proposition 10 in Féron et al. (2020), the (normalized) aggregate position of all minor agents is given
by the expectation of φ with respect to the common noise: ¯φt = E[φt|F 0
t ].

:= L(ζt|F 0

t ).

t

We assume that the market price (Pt)t∈[0,T] is given by the fundamental price (St)t∈[0,T] plus
a weighted combination of the aggregate position of the minor agents and the position of the
major agent:

Pt = St + a ¯φt + a0φ0
t ,

∀t ∈ [0, T]

where a and a0 are positive weights, which reﬂect the size of the major agent relative to the combined
size of all minor agents and overall strength of the market impact. Thus, the impact of each minor
agent on the entire market is negligible, but the aggregate position of all minor agents and the position
of the major agent both have a nonzero impact.

We say that the strategy of the generic minor agent ( ˙φt)t∈[0,T] is admissible if it is F-adapted and
t )t∈[0,T] is admissible if it is F0-adapted
square integrable. Similarly, the strategy of the major agent ( ˙φ0
and square integrable. The instantaneous cost of trading for the major agent and the generic minor
agent are deﬁned, respectively, by:

˙φ0
t Pt +

α0(t)
2

( ˙φ0

t )2,

and

˙φtPt +

α(t)
2

( ˙φt)2,

∀t ∈ [0, T]

(1)

In both instantaneous costs, the ﬁrst term represents the actual cost of buying the electricity
and the second term represents the cost of trading, where α(.) and α0(.) are continuous strictly positive
functions on [0, T], reﬂecting the variation of market liquidity at the approach of the delivery date.

The objective function of the minor agent has the following form:

J MF(φ, ¯φ, φ0) := −E

(cid:20)(cid:90) T

0

α(t)
2

t + (St + a ¯φt + a0φ0
˙φ2

t ) ˙φtdt +

(φT − XT)2

(cid:21)

,

λ
2

while the objective function of the major agent writes,

J MF,0(φ0, ¯φ) := −E

(cid:20)(cid:90) T

0

α0(t)
2

2

˙φ0
t

+ (St + aφt + a0φ0

t ) ˙φ0

t dt +

λ0
2

(φ0

T − X0

T)2

(2)

(3)

(cid:21)

.

Note that this formulation implies (as is the case in real markets) that the major agent pays a much
lower trading cost per unit traded and a much lower imbalance penalty than the minor agents. Indeed,
if the major agent paid the same quadratic cost/penalty as the minor agents, since the position of the
major agent is very large, the quadratic trading cost/penalty would grow much faster than the linear
part (the middle term in the formula), and the limiting formula would degenerate, in the sense that the
trading strategy would be independent from the price. In order to obtain a nondegenerate expression
in terms of the normalized trading strategy of the major agent, we must, therefore, assume that the
actual trading cost and penalty are also renormalized. The quantities α0(t) and λ0 are, thus, different
from α(t) and λ, since they are of different nature: α(t) and λ apply to the actual strategy of the generic
agent, while α0(t) and λ0 apply to the normalized strategy of the major agent. The different nature of
trading costs for minor and major agents is conﬁrmed by other authors (Donier et al. 2015): while the
minor agents post their orders immediately in the order book, the major agent splits its orders into
many small chunks in order to minimize the trading costs.

Risks 2020, 8, 133

5 of 21

To close this introductory section, we brieﬂy recall one of the main results (Theorem 7)
from Féron et al. (2020), which characterizes the mean ﬁeld equilibrium in the setting of identical
agents; in other words, we assume that a0 = 0 until the end of this section.

Deﬁnition 1 (mean ﬁeld equilibrium). An admissible strategy ˙φ∗ := ( ˙φ∗
in the setting of identical agents if it maximizes the functional (2) with a0 = 0 and satisﬁes ¯φ = ¯φ∗.

t )t∈[0,T] is a mean ﬁeld equilibrium

We make the following assumption.

Assumption 1.

•
•
•

The process S is square integrable and adapted to the ﬁltration F0.
The process X is a square integrable martingale with respect to the ﬁltration F.
The process X that is deﬁned by Xt := E[Xt|F 0
respect to the ﬁltration F.

t ] for 0 ≤ t ≤ T is a square integrable martingale with

Note that, if X is an F-martingale, then X is by construction an F0-martingale, but it may not

necessarily be a martingale in the larger ﬁltration F.

The following theorem characterizes the mean ﬁeld equilibrium in the identical agent setting.
In the theorem, we decompose the individual demand forecast, as follows: Xt = Xt + ˇXt,
where Xt = E (cid:2)Xt|F 0

(cid:3), and we use the following shorthand notation:

t

∆s,t :=

It :=

(cid:90) t

s
(cid:90) t

0

η(u, t)
α(u)
η(s, t)
α(s)

du with η(s, t) = e

− (cid:82) t
s

a
α(u) du

Ssds,

(cid:101)It := E

(cid:20)(cid:90) T

0

η(s, T)
α(s)

Ssds

(cid:12)
(cid:12)
(cid:12)Ft

and (cid:101)∆s,t :=
(cid:21)

(cid:90) t

s

α−1(u)du

.

(4)

Theorem 1. Under Assumption 1, the unique mean ﬁeld equilibrium in the setting of identical agents is
given by

(cid:34)

φ∗
t = −It + λ

∆

0,t

(cid:101)I0 + X0
1 + λ∆
0,T

+

(cid:90) t

0

∆s,t

+(cid:101)∆

0,t

ˇX0
1 + λ(cid:101)∆

0,T

+

(cid:90) t

0

(cid:101)∆s,t

d ˇXs
1 + λ(cid:101)∆s,T

.

d(cid:101)Is + dXs
1 + λ∆s,T
(cid:35)

The equilibrium price has the following form:

Pt = St − aIt + aλ

(cid:34)

∆

0,t

(cid:101)I0 + X0
1 + λ∆
0,T

+

(cid:90) t

0

∆s,t

d(cid:101)Is + dXs
1 + λ∆s,T

(cid:35)

.

(5)

(6)

3. A Game of a Major and Minor Agents

In this section, we proceed to characterize the Nash equilibrium in the Stackelberg mean ﬁeld
game with a major player. Because a single minor agent has an inﬁnitesimal impact on the market
and cannot inﬂuence the mean ﬁeld or the strategy of the major agent, the problem of the generic
minor agent is to maximize J MF(φ, ¯φ, φ0) for ﬁxed ¯φ and φ0. On the other hand, by modifying her
strategy φ0, the major agent may inﬂuence the strategies of the minor agents and, thus, also the mean
ﬁeld ¯φ. This leads to the following deﬁnition of mean ﬁeld equilibrium. As in the preceding section,
the “consistency condition” in this deﬁnition simply translates the fact that the aggregate position ¯φ of
all minor agents is given by the expectation of the representative agent strategy φ with respect to the
common noise.

Risks 2020, 8, 133

6 of 21

Deﬁnition 2 (Stackelberg mean ﬁeld equilibrium). We call the triple φ∗, ¯φ∗, φ0∗ Stackelberg mean ﬁeld
equilibrium for the game with a major and minor players if the following holds:

i.

φ∗ and φ0∗ are admissible strategies for, respectively, the representative minor and the major players,
the consistency condition ¯φ∗
t ] is satisﬁed for all t ∈ [0, T] and for any other admissible
strategy for the representative minor player φ,

t = E[φ∗

t |F 0

J MF(φ, ¯φ∗, φ0∗) ≤ J MF(φ∗, ¯φ∗, φ0∗)

ii.

For any other triple (φ, ¯φ, φ0) satisfying condition i.,

J MF,0(φ0, ¯φ) ≤ J MF,0(φ0∗, ¯φ∗).

(7)

Assumption 2.
martingale with respect to the ﬁltration F0.

In addition to Assumption 1, we also assume that the process X0 is a square integrable

We start with the characterization of the optimal strategy for the minor agent.

Proposition 1 (Minor representative agent). Let ¯φ and φ0 be ﬁxed. The minor agent strategy φ maximizes (2)
over the set of admissible strategies if and only if:

˙φt = −

Yt + St + aφt + a0φ0
t
α(t)

,

∀t ∈ [0, T],

(8)

where Y is a F-martingale that satisﬁes YT = λ(φT − XT).

Proof. The proof follows from the ﬁrst step of the proof of Theorem 1 (see Theorem 7
in Féron et al. (2020)), taking (cid:101)S = S + a0φ0 as fundamental price instead of S.

The problem of the major agent is more complex, since the minor agents observe the major agent’s
actions and modify their strategies accordingly, which means that the mean ﬁeld ¯φ depends on the
major agent’s strategy φ0, and the problem of the major agent effectively becomes a stochastic control
problem. We start with a reformulation of the deﬁnition of Stackelberg equilibrium in terms of ¯φ and
φ0 only.

Lemma 1. Let ( ¯φ∗, φ0∗) be F0-adapted square integrable processes. There exists φ∗, such that (φ∗, ¯φ∗, φ0∗) is
a Stackelberg mean ﬁeld equilibrium if and only if the couple ( ¯φ∗, φ0∗) satisﬁes the following conditions:

i.

For every F0-adapted square integrable process ν,

(cid:20)(cid:90) T

E

0

νt{α(t) ˙¯φ∗

t + St + a0φ0∗

t + a ¯φ∗

t }dt + λ( ¯φ∗

T − XT)

(cid:21)

νtdt

(cid:90) T

0

= 0.

ii.

For every other couple (φ0, ¯φ) satisfying the condition i, the inequality (7) holds true.

Proof. First assume that (φ∗, ¯φ∗, φ0∗) is a Stackelberg mean ﬁeld equilibrium. Subsequently, for every
F0-adapted square integrable process ν,

J MF(φ∗ +

(cid:90) ·

0

νsds, φ

∗

, φ0∗) ≤ J MF(φ∗, φ

∗

, φ0∗).

Risks 2020, 8, 133

7 of 21

Developing the functionals we get,

α(t)ν2

t dt +

(cid:19)2(cid:35)

(cid:18)(cid:90) T

0

λ
2

νtdt

(cid:34)

E

1
2

+ E

(cid:90) T

0
(cid:20)(cid:90) T

(cid:110)

νt

α(t) ˙φ∗

t + St + a ¯φ∗

t + a0φ0∗
t

(cid:111)

dt + λ(φ∗

T − XT)

(cid:21)

νtdt

(cid:90) T

0

≥ 0,

0

and, since ν is arbitrary, we see that this is equivalent to

(cid:20)(cid:90) T

E

0

(cid:110)

νt

α(t) ˙φ∗

t + St + a ¯φ∗

t + a0φ0∗
t

(cid:111)

dt + λ(φ∗

T − XT)

(cid:21)

νtdt

(cid:90) T

0

= 0.

Taking conditional expectations and using Fubini’s theorem, we then obtain condition i. of

the lemma.

Assume now that conditions i. and ii. of the lemma hold true, and let φ∗ be given by Proposition 1
t . Let Y∗ be
t ]. It remains to show that ˜φ∗
t |F 0
T − XT). By integration by parts, condition i. of the lemma is

applied to the couple ( ¯φ∗, φ0∗). Deﬁne ˜φ∗
t
an F0-martingale satisfying Y∗
equivalent to

T = λ( ¯φ∗

:= E[φ∗

t = ¯φ∗

(cid:20)(cid:90) T

E

(cid:110)

νt

α(t) ˙¯φ∗

t + Sta0φ0∗

t + a ¯φ∗

t + Y∗
t

(cid:21)

(cid:111)

dt

= 0,

and since ν is arbitrary,

0

α(t) ˙¯φ∗

t + St + a0φ0∗

t + a ¯φ∗

t + Y∗

t = 0,

for all t. On the other hand, by Proposition 1, while taking the expectation with respect to F0, we get
that there exists a F0-martingale (cid:101)Y with (cid:101)YT = λ( ˜φ∗

T − XT), and such that

α(t) ˙˜φ∗

t + St + a0φ0∗

t + a ¯φ∗

t + (cid:101)Yt = 0.

Substracting this expression from the previous one, we obtain

α(t)( ˙¯φ∗

t − ˙˜φ∗

t ) + Y∗

t − (cid:101)Yt = 0,

T − (cid:101)YT = λ( ¯φ∗
Y∗

T − ˜φ∗
T)

Thus,

t − ˜φ∗
¯φ∗

t =

(cid:90) t

0

(cid:101)Ys − Y∗
s
α(s)

ds

and, therefore, using the terminal condition and the martingale property,

(cid:101)Yt − Y∗

t = E[ (cid:101)YT − Y∗

T|F 0

t ] = λ

(cid:90) t

0

(cid:101)Ys − Y∗
s
α(s)

ds + λ( (cid:101)Yt − Y∗
t )

(cid:90) T

t

ds
α(s)

.

The unique solution of this linear equation is (cid:101)Yt = Y∗

t for all t, and, therefore, ˜φ∗

t = ¯φ∗

t for all t.

The following proposition provides a martingale characterization of the Stackelberg mean

ﬁeld equilibrium.

Proposition 2. Let ( ¯φ∗, φ0∗) be F0-adapted square integrable processes. There exists φ∗, such that (φ∗, ¯φ∗, φ0∗)
is a Stackelberg mean ﬁeld equilibrium if and only if

˙φ0∗
t = −

M0

t + St + aφt − a0Nt
α0(t)

,

∀t ∈ [0, T],

(9)

Risks 2020, 8, 133

8 of 21

where M0 is an F0-martingale and N is an absolutely continuous F0-adapted process, and there exists
an F0-martingale M, and an F0-martingale Y, such that the following system of equations is satisﬁed:






T = a0NT + a0φ0

M0
t + α(t) ˙Nt − aNt = 0,
Mt − aφ0
Yt + α(t) ˙¯φt + St + a ¯φt + a0φ0

T + λ0(φ0

T − X0
T)

t = 0,

MT = aφ0

T + (a + λ)NT
YT = λ( ¯φT − XT)

(10)

Proof. The optimization problem of the major agent consists in maximizing the objective function (3)
under the constraint of Lemma 1, part i. Following the methodology of Bensoussan et al. (2016), let us
introduce the Lagrangian for this constrained optimization problem, which writes:

L(φ0, ¯φ, ν) = E

+ E

(cid:20)(cid:90) T

0
(cid:20)(cid:90) T

0

α0(t)
2
(cid:110)

2

˙φ0
t

+ (St + aφt + a0φ0

t ) ˙φ0

t dt +

(cid:21)

λ0
2

(φ0

T − X0

T)2

νt

α(t) ˙¯φt + St + a0φ0

t + a ¯φt

(cid:111)

dt + λ( ¯φT − XT)

(cid:21)

νtdt

,

(cid:90) T

0

where ν is a square integrable F0-adapted process. We claim that φ0 is the solution of the problem (3) if
and only if there exist ν and ¯φ, such that (φ0, ¯φ) maximizes the Lagrangian L(·, ·, ν), and ¯φ satisﬁes the
constraint of Lemma 1. Indeed, let (φ0, ¯φ, ν) be such a triple and (φ0(cid:48), ¯φ(cid:48)) be another pair of strategies
satisfying the constraint of Lemma 1. Subsequently,

L(φ0, ¯φ, ν) ≥ L(φ0(cid:48), ¯φ(cid:48), ν),

and, since both ¯φ and ¯φ(cid:48) satisfy the constraint of Lemma 1, this implies that inequality (7) holds true.
0 νsds. The ﬁrst order

We now turn to the problem of maximizing the Lagrangian. Let Nt = (cid:82) t

condition for φ0 writes: there exists a martingale M0, such that

M0

t + α0(t) ˙φ0

t + St + a ¯φt − a0Nt = 0,

M0

T = a0NT + a0φ0

T + λ0(φ0

T − X0

T).

The ﬁrst order condition for ¯φ writes: there exists a martingale M, such that

Mt − aφ0

t + α(t) ˙Nt − aNt = 0,

MT = aφ0

T + (a + λ)NT.

Finally, the last condition is given by the constraint that ¯φ is optimal for the generic minor agent.

Hence, conditioning (8) by the common noise, there exists a martingale Y, such that

Yt + α(t) ˙¯φt + St + a ¯φt + a0φ0

t = 0,

YT = λ( ¯φT − XT).

From Proposition 2, it follows that the existence and uniqueness of the Stackelberg equilibrium
reduces to the existence and uniqueness of the solution of the linear system of coupled BSDEs
Equation (10).

The following theorem provides an explicit characterization of the equilibrium in the

Stackelberg setting.

Theorem 2 (Explicit solution). Let Ξt = (φ0
the unique equilibrium of the mean ﬁeld game with a major agent:

t , Nt, ¯φt)(cid:48). The following differential equation characterizes

B(t)−1 A Ξt + ˙Ξt = −







t + St)

α0(t)−1(M0
α(t)−1 Mt
α(t)−1(Yt + St)







,

(11)

Risks 2020, 8, 133

where N is a F0-adapted process with N0 = 0 and M0, M, and Y are F0-martingales that satisfy:






T = a0NT + a0φ0

M0
MT = aφ0
YT = λ( ¯φT − XT)

T + (a + λ)NT

T + λ0(φ0

T − X0
T)

9 of 21

(12)

and







A =

0 −a0
−a −a
a0

0







a

0

a

,







B(t) =

α0(t)

0
0 α(t)

0

0







.

0
0 α(t)

Denoting, by Φ(t), the fundamental matrix solution of the equation B(t)−1 A Ξt + ˙Ξt = 0, the solution is given
in integral form by the following expression:

Ξt = Υt − Π

0,t(I + DΠ

0,T)−1(D(cid:101)Υ

0 − ΛX0) −

(cid:90) t

0

Πs,t(I + DΠs,T)−1(Dd(cid:101)Υs − ΛdXs).

(13)

where,

Υt := −Φ(t)

(cid:90) t

0

Φ(s)−1







α0(s)−1Ss
0
α(s)−1Ss







ds, Xs :=













X0
s

0

Xs

, D =







a0 + λ0
a

a0
0
a + λ 0

0

0 λ







,

Λ =













0

λ0
0 0

0

0

0 0 λ

, Πs,t := Φ(t) (cid:82) t

s

Φ(u)−1B(u)−1du and (cid:101)Υt = E[ΥT|Ft].

Remark 1. These results can be generalized to the setting of several major agents, interacting with the mean-ﬁeld
of the minor agents, provided that each major agent observes the individual forecasts of the other agents, but not
those of the minor agents. In this case, the constrained optimization problem of one major agent becomes a
constrained game between several major agents. Because the setting remains linear-quadratic, one will still be
able to obtain an explicit solution, at the price of more tedious computations.

Remark 2. If α0(t) = cα(t) for some constant c, the fundamental matrix solution is explicitly given by

Φ(t) = exp

(cid:90) t

(cid:18)

−

0

(cid:19)

B(s)−1 Ads

Proof. From Equation (8) in Proposition 1 and (10) in Proposition 2, we immediately deduce the
expression of the characterizing differential equation of the equilibrium (11).

Let Φ(t) be the fundamental matrix solution of the equation B(t)−1 A Ξt + ˙Ξt = 0, which is,
0 = C is given by Φ(t)C. By a variation of

for every C ∈ R3, the solution with initial condition Ξ
constants, we have that the solution of (11) is given by:

Ξt = −Φ(t)

(cid:90) t

0

Φ(s)−1







s + Ss)

α0(s)−1(M0
α(s)−1 Ms
α(s)−1(Ys + Ss)







ds.

10 of 21

Risks 2020, 8, 133

Letting:

Ms :=













M0
s
Ms

Ys

and (cid:98)Ξt = Ξt − Υt,

we obtain the simpliﬁed equation:

(cid:98)Ξt = −Φ(t)

(cid:90) t

0

Φ(s)−1B(s)−1Msds.

and, ﬁnally, using (12) and the martingale property, the martingale components satisfy:

Mt = −DΦ(T)

(cid:90) t

0

Φ(s)−1B(s)−1Msds − DΠt,TMt + D(cid:101)Υt − ΛXt,

From this, we deduce, on the one hand,

M0 = (I + DΠ

0,T)−1(D(cid:101)Υ

0 − ΛX0),

(I + DΠt,T)dMt = Dd(cid:101)Υt − ΛdXt,

and, on the other hand,

so that, ﬁnally:

(cid:90) t

Ξt = Υt +

dΠs,t · Ms = Υt − Π

0,tM0 −

0
0,t(I + DΠ
= Υt − Π

0,T)−1(D(cid:101)Υ

0
0 − ΛX0) −

(cid:90) t

Πs,tdMs
(cid:90) t

0

Πs,t(I + DΠs,T)−1(Dd(cid:101)Υs − ΛdXs).

Let us make some comments regarding how minor and major player strategies change when the
parameters of the model vary. First, when the major player has no price impact, a0 = 0, we recover the
homogeneous mean ﬁeld setting optimal strategy for the minor player from (10) and (12):

¯φt =

(cid:90) t

0

η(s, t)
α(s)

(Ys + Ss)ds,

where Y satisﬁes the equation:

(cid:40)

Yt + α(t) ˙¯φ∗
YT = −λ( ¯φ∗

t + St + a ¯φ∗
T − XT).

t = 0

Second, we explore the limiting behavior of the optimal strategies for the major agent and mean

ﬁeld in various limiting cases. In this corollary, we use the notation of Theorem 2.

Risks 2020, 8, 133

Corollary 1.

11 of 21

i.

Assume that the fundamental price process S is a martingale. Subsequently, the equilibrium mean ﬁeld
position of minor agents and the position of the major agent satisfy

Ξt = −Π

0,t(I + DΠ

0,T)−1







S0 − λ0X0
0
0
S0 − λX0







−

(cid:90) t

0

Πs,t(I + DΠs,T)−1d







Ss − λ0X0
s
0
Ss − λXs







.

ii.

In the limit of inﬁnite terminal penalty (when λ, λ0 → ∞), the equilibrium mean ﬁeld position of minor
agents and the position of the major agent satisfy,

Ξt → Υt − Π

0,tΠ−1

0,T((cid:101)Υ

0 − D∞X0) −

(cid:90) t

0

Πs,tΠ−1

s,T(d(cid:101)Υs − D∞dXs),

almost surely for all t ∈ [0, T], where

D∞ =







1

0

0

0

0

0







0

0

1

.

When the fundamental price process S is a martingale, in the limit of inﬁnite terminal penalty, the strategies
do not depend on the fundamental price and we have,

Ξt → Π

0,t Π−1
0,T













X0
0
0

X0

+

(cid:90) t

0

Πs,t Π−1

s,T d













X0
s
0

Xs

.

iii.

In the absence of terminal penalties (when λ = λ0 = 0), the equilibrium mean ﬁeld position of minor
agents and the position of the major agent satisfy,

Ξt = Υt − Π

0,t(I + D0

Π

0,T)−1D0 (cid:101)Υ

0 −

(cid:90) t

0

Πs,t(I + D0

Πs,T)−1D0d(cid:101)Υs.

(14)

Proof. The ﬁrst part is a simpliﬁcation of the proof of Theorem 2. Using the expressions of Yt and (cid:101)Yt in
Theorem 2 and the martingale property of St , we can rewrite:

Yt = −Π

0,tS0 −

(cid:90) t

0

Πs,tdSs,

(cid:101)Yt = −Π

0,TS0 −

(cid:90) t

0

Πs,TdSs.

Substituting these expressions in the Equation (13), we obtain the result.
For the second part, we can rewrite:

Ξt = Υt − Π

0,t(I + DΠ

0,T)−1(D(cid:101)Υ

0 − ΛX0) −

(cid:90) t

= Υt − Π

0,t(D−1 + Π

0,T)−1((cid:101)Υ

0
0 − D−1ΛX0) −

0

Πs,t(I + DΠs,T)−1(Dd(cid:101)Υs − ΛdXs)
(cid:90) t

Πs,t(D−1 + Πs,T)−1(d(cid:101)Υs − D−1ΛdXs)

and when λ, λ0 −→ ∞, D−1 → 0 and D−1Λ → D∞. The third part follows by direct substitution of
λ = λ0 = 0 into the general formula.

Interestingly, when the players do not have a terminal penalty (λ = λ0 = 0), the equilibrium
positions of the agents in Equation (14) still contain forward looking terms, which were absent in the

Risks 2020, 8, 133

12 of 21

case of the mean ﬁeld game with identical players (see Equation (5) with λ = 0). The presence of these
terms is due to the strategic interaction of the major player with the mean ﬁeld of small agents.

In the limit of zero trading costs, the gain of the major player remains bounded in expectation;
however, contrary to the case of identical players, the optimal strategy of the major agent cannot be
uniquely determined from the optimization problem. Indeed, while assuming that the trading cost for
minor agents is zero, the equilibrium price (computed from Equation (12) in Féron et al. (2020) with
N → ∞) is given by

Pt = St + a0φ0

t + a ¯φt =

λ
a + λ

(aXt + E[ST|Ft] + a0

E[φ0

T|Ft]).

Substituting this expression into the optimization problem for the major player, we need to

minimize the following functional:

E

(cid:90) T

(cid:20) λ
a + λ
(cid:20) λ
a + λ

0

= E

t (aXt + E[ST|Ft] + a0
˙φ0

E[φ0

T|Ft])dt +

λ0
2

(aφ0

T XT + φ0

TST + a0(φ0

T)2) +

λ0
2

(φ0

T − X0

T)2

,

(cid:21)

(φ0

T)2

T − X0
(cid:21)

where the equality follows, in particular, from the martingale property of XT. Because the expression
to be minimized only depends on the terminal value φ0
T of the major agent’s position, any strategy
with the optimal terminal value will satisfy the condition of optimality: the Stackelberg equilibrium
will not be unique in this case.

To ﬁnish this section, we provide the explicit form of the strategy of the minor agents.

Corollary 2 (Minor agent strategy). Under Assumption 2, the optimal generic minor agent position φ∗ is
given by:

φ∗
t =

(cid:90) t

0

(cid:101)∆s,t

λd ˇXs
1 + λ(cid:101)∆s,T

+ (cid:101)∆

0,t

λ ˇX0
1 + λ(cid:101)∆

0,T

+ ¯φ∗
t ,

where ¯φ∗ is the optimal aggregate position of the minor agents, as given by Theorem 2.

Proof. Let ˇφ∗
and Y in Proposition 1, it follows that ˇY is an F-martingale and it satisﬁes

t , ˇXt = Xt − Xt and ˇYt := Yt − Yt. Subsequently, from the explicit form of Y

t = φ∗

t − ¯φ∗

ˇYT = −λ( ˇφ∗

T − ˇXT),

ˇYt = α(t) ˙ˇφ∗
t .

Subsequently,

ˇφ∗
t =

(cid:90) t

0

ˇYs
α(s)

ds,

(15)

and by the martingale property,

Yt = −λE[ ˇφ∗

T − ˇXT|Ft] = −λ

(cid:90) t

0

ˇYs
α(s)

ds − λ ˇYt

(cid:90) T

t

ds
α(s)

+ λ ˇXt.

Solving this linear equation for ˇY and then substituting into (15), we obtain the result.

4. Approximate Nash Equilibrium in the N-Player Stackelberg Game

In this section, we derive the (cid:101)-Nash approximation for the Stackelberg game. In the present
leader-follower setting, we allow the minor agents to change their strategies when the major agent
deviates from the optimal one.

Risks 2020, 8, 133

13 of 21

Because we would like to study the rate of convergence as N → ∞, we assume that there is
a major player and an inﬁnity of minor players replacing the generic agent. Their demand forecasts
t, i = 0, . . . , ∞, and t ∈ [0, T]. The private demand forecasts of all agents
are, respectively, given by Xi
are deﬁned on the same probability space. Therefore, we impose the following assumption.

Assumption 3.

•
•
•
•

•

The process S is square integrable and adapted to the ﬁltration F0.
The demand forecast X0 of the major agent is a square integrable F0-martingale.
The processes (Xi)∞
i=1 are square integrable F-martingales.
There exists a square intergrable F-martingale X, such that for all i ≥ 1, and all t ∈ [0, T], almost surely,
E[Xi
The processes ( ˇXi)∞
F-martingales, such that the expectation E[( ˇXi

t − Xt for t ∈ [0, T], are orthogonal square integrable

i=1 that are deﬁned by ˇXi

t ] = Xt.

t = Xi

T)2] does not depend on i.

t|F 0

The strategy ( ˙φi) of agent i = 1, . . . , ∞ is said to be admissible if it is F-adapted and square
integrable; the strategy ( ˙φ0) of the major agent is admissible if it is F0-adapted and square integrable.
For a ﬁxed N ≥ 1, we denote:

PN(φ0
PMF(φ0

N
t , ..., φN
t + a0φ0
t ) = St + aφ
t
t , ¯φt) = St + a ¯φt + a0φ0
t ,

where ¯φN
N-player game, the objective functions for the major agent:

t = 1
N

i=1 φi

∑N

t is the average position of the minor agents. Additionally, we deﬁne in the

( ˙φ0

t )2 + ˙φ0

t PN(φ0

t , . . . , φN
t )

(cid:27)

dt +

λ0
2

(φ0

T − X0

T)2

(cid:21)

,

(16)

J N,0(φ0, φ−0) := −E

(cid:20)(cid:90) T

0

(cid:26) α0(t)
2

and for the minor agents i = 1, . . . , N:

J N,i(φi, φ−i) := −E

(cid:20)(cid:90) T

0

(cid:26) α(t)
2

( ˙φi

t)2 + ˙φi

tPN(φ0

t , . . . , φN
t )

(cid:27)

dt +

λ
2

(φi

T − Xi

T)2

(cid:21)

,

as well as the objective function for the minor agents i = 1, . . . , N, in the mean ﬁeld setting:

J MF(φi, ¯φ, φ0) := −E

(cid:20)(cid:90) T

0

(cid:26) α(t)
2

( ˙φi

t)2 + ˙φi

tPMF(φ0

t , ¯φt)

(cid:27)

dt +

λ
2

(φi

T − Xi

T)2

(cid:21)

.

We next provide a deﬁnition of the (cid:101)-Nash equilibrium in the present Stackelberg setting.
As mentioned above, the deviations of the major and minor agents must be treated differently:
when the major agent deviates, we allow the minor agents to adjust their strategies to respond
optimally to the new strategy of the major agent. We say that the minor agent strategies φ1, . . . , φN are
an optimal response to the major agent strategy φ0 if, for every i = 1, . . . , N and for every admissible
minor agent strategy ˜φi,

J N,i( ˜φi, φ−i) ≤ J N,i(φi, φ−i).

Deﬁnition 3 (Stackelberg ε-Nash equilibrium). We say that (φi∗
the N-player game if these strategies are admissible and the following holds.

t )t∈[0,T],0≤i≤N is an (cid:101)-Nash equilibrium for

i. Deviation of a minor player:

for any other admissible strategy φi for the minor player i, i = 1, . . . , N,

J N,i(φi, φ−i∗) − ε ≤ J N,i(φi∗, φ−i∗).

(17)

(18)

Risks 2020, 8, 133

14 of 21

ii. Deviation of the major player:

for any other set of admissible strategies (φi), i = 0, . . . , N, such that

φ1, . . . , φN are optimal responses of minor players to the major player strategy φ0, we have,

J N,0(φ0, φ−0) − ε ≤ J N,0(φ0∗, φ−0∗).

Our deﬁnition of ε-Nash equilibrium is different from the one presented in Carmona and Zhu
(2016): while the latter paper assumes that the major player deviates from her strategy unilaterally
(see Deﬁnition 4.2 in the cited paper), we allow the minor players to respond to the deviation of the
major player, in agreement with the leader-follower nature of the game. In addition, in Carmona and
Zhu (2016), an a priori bound on the Lp-norm of the new strategy of the major agent is required to
establish Theorem 4.1 in the cited paper, whereas no such bound is needed in our setting.

Proposition 3. Assume that the strategies of the N minor agents are given by

φi∗
t =

(cid:90) t

0

(cid:101)∆s,t

λd ˇXi
s
1 + λ(cid:101)∆s,T

+ (cid:101)∆

0,t

λ ˇXi
0
1 + λ(cid:101)∆

0,T

+ φ

∗
t ,

where φ
is the third component of the mean ﬁeld equilibrium deﬁned in Theorem 2. Assume that the strategy of
the major agent is also given by Theorem 2. Let Assumption 3 hold true. Then there exists a constant C < ∞,
which does not depend on N, such that these strategies form an ε-Nash equilibrium of the N-player game with
ε = C

∗

N1/2 .

Remark 3. The ε-Nash equilibrium that is described in Proposition 3 approximates the N-player equilibrium in
the complete information setting (where every player observes the others’ actions), but its implementation for
each agent only requires the knowledge of the common information F0 as well as the agent’s individual forecast.

Proof. We need to show the conditions i. and ii. of Deﬁnition 3. Condition i. is shown in the same
way as in the case of homogeneous players (see proof of Proposition 2 in Féron et al. 2020). Therefore,
we focus on condition ii. Assume that all of the agents change their strategies to new ones φ0, . . . , φN,
such that φ1, . . . , φN are optimal responses to φ0. Let ¯φ be the optimal "mean ﬁeld" response to the
major agent strategy φ0.

Step 1.

E (cid:104)(cid:82) T

(cid:105)

We ﬁrst suppose that there exists a ﬁnite constant A > 0, independent of N, such that
0 ( ˙φ0
By Proposition 1 in Féron et al. (2020), for some constants c and C, which do not depend on N,

t )2dt

< A.

and may change from line-to-line,

(cid:20)(cid:90) T

E

0

( ¯φt − ¯φN

t )2dt

(cid:21)

≤

E

C
N2

(cid:20)(cid:90) T

0

(Ss + a0φ0

s )2ds

(cid:21)

+

c
N

,

and by our assumption,

(Ss + a0φ0

s )2ds

(cid:21)

(cid:20)(cid:90) T

E

0
(cid:20)(cid:90) T

= E

(cid:21)

S2
s ds

+ 2a0E

(cid:20)(cid:90) T

0

S2
s ds

(cid:21) 1
2

E

(cid:20)(cid:90) T

0

(φ0

s )2ds

(cid:21) 1
2

+ E

(cid:20)(cid:90) T

0

(cid:21)

(a0φ0

s )2ds

< C(1 + A).

0

Risks 2020, 8, 133

15 of 21

Thus, while using Cauchy–Schwartz inequality,

J N,0(φ0, φ−0) − J N,0(φ0∗, φ−0∗)
= J N,0(φ0, φ−0) − J MF(φ0, ¯φ) + J MF(φ0, ¯φ) − J MF(φ0∗, ¯φ∗) + J MF(φ0∗
≤ J N,0(φ0, φ−0) − J MF(φ0, ¯φ0) + J MF(φ0∗
(cid:21) 1
2

, ¯φ∗) − J N,0(φ0∗, φ−0∗)
(cid:21) 1
(cid:20)(cid:90) T
2

(cid:20)(cid:90) T

(cid:20)(cid:90) T

(cid:21) 1
2

(cid:40)

( ˙φ0

t )2dt

E

( ¯φt − ¯φN

t )2dt

+ E

( ˙φ0∗

t )2dt

≤ a

E

0

0

0

, ¯φ∗) − J N,0(φ0∗, φ−0∗)

(cid:20)(cid:90) T

E

(cid:41)

(cid:21) 1
2

( ¯φ∗

t − ¯φN∗
t

)2dt

0
(cid:17)
N− 1

2

(cid:16)

= O

Step 2.

Let there exist a sufﬁciently large constant A, independent of N, such that

(cid:20)(cid:90) T

(cid:16)

E

0

(cid:17)2

(cid:21)

dt

˙φ0
t

> A

Letting ¯α0 = min0≤t≤T α0(t), and ¯α = min0≤t≤T α(t), we have, by deﬁnition,

J N,0(φ0, φ−0) ≤ −E

(cid:20)(cid:90) T

0

¯α0
2

( ˙φ0

t )2 + ˙φ0

t (St + a ¯φN

t + a0φ0

t )dt +

(cid:21)

λ0
2

(φ0

T − XT)2

On the other hand, because φi for i = 1, . . . , N are optimal responses to φ0, we get that

(cid:20)(cid:90) T

E

0

(cid:26) α(t)
2

( ˙φi

t)2 + ˙φi

t(St + a ¯φN

t + a0φ0
t )

(cid:27)

dt +

λ
2

(φi

T − Xi

T)2

(cid:21)

≤

λ
2

E[(Xi

T)2] ≤ C,

where C < ∞ is deﬁned by C := maxi
dividing by N and using Jensen’s inequality, we obtain

E[(Xi

λ
2

T)2]. Summing up the above inequality over i = 1, . . . , N,

(cid:20)(cid:90) T

E

0

(cid:26) ¯α
2

( ˙¯φN

t )2 + ˙¯φN

t (St + a ¯φN

t + a0φ0
t )

(cid:27)

dt +

λ
2

( ¯φN

T − X

N
T )2

(cid:21)

≤ C.

Multiplying this inequality by a
a0

we ﬁnally obtain

, adding it to the ﬁrst one, and using integration by parts,

J N,0(φ0, φ−0) ≤ C − E

(cid:34) (cid:90) T

0

(cid:26) ¯α0
2

( ˙φ0

t )2 +

a ¯α
2a0

( ˙¯φN

t )2 +

St
a0

(a0 ˙φ0

t + a ˙¯φN
t )

(cid:27)

dt

+

1
2a0

(a ¯φN

T + a0φ0

T)2 +

λ0
2

(φ0

T − XT)2 +

aλ
2a0

( ¯φN

T − X

N
T )2

≤ C − E

− E

(cid:20)(cid:90) T

0

≤ C − E

(cid:20)(cid:90) T

0

¯α0
2

( ˙φ0

t )2dt

(cid:20)(cid:90) T

(cid:21)

+ E

S2
t dt

(cid:21) 1
2

E

(cid:20)(cid:90) T

( ˙φ0

t )2dt

a ¯α
2a0
(cid:20)(cid:90) T

0

( ˙¯φN

t )2dt

(cid:21)

+

E

a
a0

(cid:21)

+ E

( ˙φ0

t )2dt

¯α0
2

0
(cid:20)(cid:90) T

0
(cid:20)(cid:90) T

0

0
(cid:20)(cid:90) T

0
(cid:20)(cid:90) T

(cid:21) 1
2

E

S2
t dt

(cid:21) 1
2

E

S2
t dt

( ˙¯φN

t )2dt

(cid:35)

(cid:21) 1
2

(cid:21) 1
2

( ˙φ0

t )2dt

(cid:21) 1
2

+

E

a
¯αa0

(cid:20)(cid:90) T

0

(cid:21)

S2
t dt

0

Thus, if

(cid:20)(cid:90) T

E

0

( ˙φ0

t )2dt

(cid:21)

> A,

Risks 2020, 8, 133

16 of 21

for A sufﬁciently large (but not depending on N), then, from the above estimate, it follows that

J N,0(φ0, φ−0) ≤ J N,0(φ0∗, φ−0∗),

as well.

5. Numerical Illustration

In this section, our objective is to illustrate the theoretical results that are presented in Sections 3
and 4 with numerical simulations. We analyze the role of the major producer in the market and its
impact on price characteristics, such as volatility and price-forecast correlation, and compare this
situation to the homogeneous agent setting studied in Féron et al. (2020). Some comparisons with
the empirical market characteristics are also performed, but we refer the reader to Féron et al. (2020)
and other papers cited therein for a more detailed description of intraday electricity markets and
their empirical features. Here, we will consider production forecasts instead of demand forecasts
because the empirical analyses in Féron et al. (2020) are led on actual wind infeed forecasts, as is
the case in the rest of the paper. Throughout, we consider that the production forecasts are the the
differences between actual production forecasts and the agents’ positions in the market at time 0.
Therefore, the initial values Xi

0, i = 0, . . . , N will be set to 0.

5.1. Model Speciﬁcation

We now deﬁne the dynamics for the fundamental price and the production forecasts used in
the simulations and specify the parameter values. With the objective being to illustrate the model,
the majority of the parameters are not precisely estimated, but they are given ad hoc plausible values.

The evolution of the fundamental price is described, as follows:

where σs is a constant and (Wt)t∈[0,T] is Brownian motion. We also assume that the liquidity functions
α(.) and α0(.) have a speciﬁc form, given by

dSt = σSdWt

(19)

α(t) = α × (T − t) + β,
α0(t) = α0 × (T − t) + β0,

∀t ∈ [0, T]

∀t ∈ [0, T]

(20)

(21)

where α, β, α0, and β0 are strictly positive constants. Thus, the liquidity functions are decreasing with
time. This assumption relies on the fact that the market becomes more liquid as we get closer to the
delivery time and it is less costly to trade when the market is liquid.

To simulate production forecasts, we assume the following dynamics:

d ¯Xt = ¯σd ¯Bt
t = σ0dB0
d ˇX0
t ,
t = σXdBi
d ˇXi
t,

i ∈ {1, . . . , N}

(22)

(23)

(24)

where ¯σ, σ0, and σX are constants and ( ¯Bt)t∈[0,T], (Bi
motions, also independent from (Wt)t∈[0,T].

t)t∈[0,T], i ∈ {0, . . . , N} are independent Brownian

In this illustration, we choose the same parameters for the dynamics of the common and individual
production forecasts, as well as the forecast of the major agent. The common volatility is calibrated
to wind energy forecasts in Germany over January 2015 during the last quotation hour, by using the
classical volatility estimator

¯σ = σ0 = σX = ˆσ =

√

∆t
n(cid:48) − 1

n(cid:48)
∑
i=1

Y2
i

(25)

Risks 2020, 8, 133

17 of 21

with ∆t being the time step between two observations, Yi = Xti − Xti−1 as the increment between
two successive observations, and n(cid:48) depicting the total number of observed increments. Because the
forecasts are updated every 15 min, there are three daily variations during the last hour of forecasts
from the 3 January to the 31 January. Thus, for each delivery hour, we dispose of n(cid:48) = 87 increments in
order to estimate the volatility.

Table 1 speciﬁes the model parameters.

Table 1. Parameters of the model.

Parameter

S0
σS

X0

¯σ

ˇXi
0
σX, σ0

N

Value
40 e/MWh
10 e/MWh.h1/2

0 MWh

73 MWh/h1/2

0 MWh

73 MWh/h1/2

100

Parameter

a

λ

λ0

α

α0

β

β0

Value
1 e/MWh2
100 e/MWh2
100 e/MWh2
0.3 e/h·MW2
0.3 e/h·MW2
0.1 e/MW2
0.1 e/MW2

5.2. Equilibrium Price and Market Impact

In Figure 1, we plot the major agent production forecast and common production forecast
(respectively, the orange and blue solid lines) together with the equilibrium position of the major agent
and the aggregate position of the minor agents given by Theorem 2 and Proposition 2 (respectively,
the orange and blue dashed lines). For comparison, we also plot the aggregate position in the identical
agent case (dotted green line). All of the trajectories have been computed with the same production
forecasts, the same fundamental price, initial values, volatilities, and parameters, as speciﬁed in Table 1,
except for the price impact coefﬁcients of major and minor player, which differ according to model
speciﬁcation. In the Stackelberg game, we chose a0 = a = 0.5 e/MWh2 and, in the homogeneous case,
we kept a = 1 e/MWh2.

Figure 1. Demand forecasts and agents’ positions in the Stackelberg game.

We observe that the strategy in the setting of identical agents and the strategy of the minor player
in the Stackelberg setting converge to the same terminal value due to the terminal penalty. However,
in the Stackelberg case, the minor agent position tends to follow the one of the major player during the
ﬁrst part of the trading period. In the case of identical agents, the ﬂuctuations are not as strong, since,

Risks 2020, 8, 133

18 of 21

contrary to the case when a major agent is present, the minor agents have no incentive to modify their
trajectory to follow the leader. During the second half of the trading period, the minor agent position
deviates further away from the one of the major agent in order to target the same terminal position
as the mean ﬁeld in the case of identical agents. We can argue that the strategy of the minor agent
becomes more sensitive to the terminal constraint as we get closer to the delivery time: the weight of
the terminal constraint in the strategy increases due to the decrease of the instantaneous trading cost.

5.3. Volatility and Price-Forecast Correlation

In this paragraph, we illustrate with simulations the effect of the presence of the major agent on
the price characteristics, such as the volatility and the correlation between the price and renewable
infeed forecasts. The volatility was estimated from simulated price trajectories using a kernel-based
non parametric estimator of the instantaneous volatility:

ˆσ2
t =

i=1 Kh(ti−1 − t)∆ ˜P2
∑n
i=1 Kh(ti−1 − t)(ti − ti−1)

ti−1

∑n

,

(26)

where K(.) is the Epanechnikov kernel: K(x) = 3
h was taken equal to 0.08 h (≈5 min).

4 (1 − x2)1

[−1,1](x) and Kh(x) = 1

h K( x

h ). The parameter

For a ﬁxed scenario of production forecasts for the minor and major players, as drawn in Figure 1,
we estimated the volatility of the simulated market price for different values of the weights a0 and
a assigned, respectively, to the major player and the mean ﬁeld of minor players in the price impact
function. We studied three different combinations of weights in order to illustrate the impact of the
minor players and the major player in the game: a0 = a = 0.5 e/MWh2, the impact of the major player
and the minor players is the same; a0 = 0.9, a = 0.1 e/MWh2, the major player has a lot more impact
than the minor players, and ﬁnally a0 = 0 e/MWh2, a = 1 e/MWh2, equivalent to a market without
a major player. These weights can be seen as the respective market shares that are held by the major
agent and the minor players.

Figure 2, left graph, shows the estimated volatility trajectories for the three different cases of
market shares of the major agent averaged over 1000 simulations. We note that the volatility of the
market price depends on the strength of impact of the major player: the greater a0, the higher the
volatility. A possible explanation for this phenomenon is that stronger competition in the market
(when the major agent is absent or has a small market share) reduces proﬁt opportunities in the market
and the agents, therefore, trade less actively.

For comparison, we also plot, in Figure 2, right graph, the volatility estimated from empirical
intraday electricity price data using the same estimator (26). This graph is taken from Féron et al. (2020).
We see that the phenomenon of increasing volatility at the approach of the delivery date, which is
clearly visible in the actual electricity markets, is well reproduced by our model.

An important

stylized feature of

observed empirically
in Kiesel and Paraschiv (2017) and Féron et al. (2020), is the correlation between the price and
renewable production forecasts. In Figure 3, we plotted the correlation between the increments of the
market price and the increments of the renewable production forecast of the major agent as a function
of time, in the market impact setting a0 = a = 0.5 e/MWh2; as well as the correlation between the
price increments and increments of the total aggregate forecast of both the major and minor players.

intraday market prices,

Risks 2020, 8, 133

19 of 21

Figure 2.
(Left) volatility of simulated prices for different market shares of the major agent.
(Right) volatility for different delivery hours, estimated empirically from EPEX spot intraday market
data of January 2017 for the Germany delivery zone.

The correlation is computed over 15-min. increments while using the following estimator:

ˆρt =

(cid:113)

∑Nsim
k=1
(∆Yk

t − ∆Yt)(∆Pk
(∆Yk
t − ∆Yt)2 ∑Nsim
k=1

t − ∆Pt)
(∆Pk

∑Nsim
k=1

t − ∆Pt)2

,

with Nsim the number of simulations (we considered Nsim = 50,000) and where ∆Yk
t+dt − PMF,k
PMF,k
are the increments of, respectively, the forecast process and market price.

t

t and ∆Pk

t =

Figure 3. Correlation between the price increments and the major player renewable production increments
vs. the correlation between the price increments and the total renewable production increments.

For the sake of clarity, we only draw the Monte Carlo conﬁdence interval for the case of the
correlation between the major player production and the price considered in Figure 3. A similar
conﬁdence interval was obtained for the case of total production correlation. In Figure 3, we observe
that the correlation between the production forecast increments of the major agent and price is lower
in absolute value than the correlation between the total production forecast increments and the price.
However, the gap between the correlations diminishes as we approach the delivery time.

6. Conclusions

In this paper, we applied the theory of linear quadratic mean-ﬁeld games with a major player to
the analysis of intraday electricity markets. The linear quadratic setting, while allowing for obtaining
explicit formulas for the equilibrium price and optimal strategies of the agents, requires one to impose
a number of quite stringent assumptions on the price dynamics, such as linear market impact and
quadratic hedging cost. While these assumptions have been used in a number of papers on optimal

Risks 2020, 8, 133

20 of 21

trading and order execution in ﬁnancial markets, their validity in electricity markets remains to be
studied. Contrary to equity and bond markets, the literature on market impact and microstructure
of electricity markets is in the nascent state and we hope that our paper will motivate more in-depth
analysis of this topic, and more detailed studies of order book data of electricity markets. Another
important aspect of our study is the theoretical demonstration of the correlation between the renewable
production forecasts and market prices. As the renewable penetration and the participation of
renewable producers in intraday market increases, these correlations will become more important and
they may erode the proﬁts of the renewable producers, impeding investment ﬂows into this important
domain. Therefore, one may need to develop alternative market structures facilitating the participation
of renewable producers.

Author Contributions: The authors contributed equally to the paper. All authors have read and agreed to the
published version of the manuscript.

Funding:
ANR-19-CE05-0042) and from the FIME Research Initiative.

The authors gratefully acknowledge ﬁnancial support

from the ANR (project EcoREES

Conﬂicts of Interest: The authors declare no conﬂict of interest.

References

Aïd, René, Andrea Cosso, and Huyên Pham. 2020.

Equilibrium price in intraday electricity markets.

arXiv arXiv:2010.09285.

Aïd, René, Pierre Gruet, and Huyên Pham. 2016. An optimal trading problem in intraday electricity markets.

Mathematics and Financial Economics 10: 49–85. [CrossRef]

Alasseur, Clémence, Imen Ben Taher, and Anis Matoussi. 2020. An extended mean ﬁeld game for storage in smart

grids. Journal of Optimization Theory and Applications 18: 644–70. [CrossRef]

Bensoussan, Alain, Michael Chau, and Phillip Yam. 2016. Mean ﬁeld games with a dominating player.

Applied Mathematics & Optimization 74: 91–128.

Bensoussan, Alain, and Sheung Chi Phillip Yam. 2019. Mean ﬁeld approach to stochastic control with partial

information. arXiv arXiv:1909.10287v3.

Bouchard, Bruno, Masaaki Fukasawa, Martin Herdegen, and Johannes Muhle-Karbe. 2018. Equilibrium returns

with transaction costs. Finance and Stochastics 22: 569–601. [CrossRef]

Cardaliaguet, Pierre, Marco Cirant, and Alessio Porretta. 2020. Remarks on Nash equilibria in mean ﬁeld game
models with a major player. Proceedings of the American Mathematical Society 148: 4241–55. [CrossRef]

Carmona, René, and François Delarue. 2018.

Probabilistic Theory of Mean Field Games with Applications I.

Berlin/Heidelberg: Springer.

Carmona, Rene, and Xiuneng Zhu. 2016. A probabilistic approach to mean ﬁeld games with major and minor

players. The Annals of Applied Probability 26: 1535–80. [CrossRef]

Casgrain, Philippe, and Sebastian Jaimungal. 2020. Mean-ﬁeld games with differing beliefs for algorithmic

trading. Mathematical Finance 30: 995–1034. [CrossRef]

Donier, Jonathan, Julius Bonart, Iacopo Mastromatteo, and Jean-Philippe Bouchaud. 2015. A fully consistent,

minimal model for non-linear market impact. Quantitative Finance 15: 1109–21. [CrossRef]
2020.

Evangelista, David, and Yuri Thamsten.

Finite population games of optimal execution.

arXiv arXiv:2004.00790.

Féron, Olivier, Peter Tankov, and Laura Tinsi. 2020. Price formation and optimal trading in intraday electricity

markets. arXiv arXiv:2009.04786.

Fu, Guanxing, and Ulrich Horst. 2020. Mean-ﬁeld leader-follower games with terminal state constraint.

SIAM Journal on Control and Optimization 58: 2078–113. [CrossRef]

Fujii, Masaaki, and Akihiko Takahashi. 2020. A mean ﬁeld game approach to equilibrium pricing with market

clearing condition. CARF Working Paper CARF-F-473. arXiv arXiv:2003.03035

Huang, Minyi. 2010. Large-population LQG games involving a major player: The Nash certainty equivalence

principle. SIAM Journal on Control and Optimization 48: 3318–53. [CrossRef]

Risks 2020, 8, 133

21 of 21

Huang, Minyi, Roland P. Malhamé, and Peter E. Caines. 2006. Large population stochastic dynamic games:
Closed-loop McKean-Vlasov systems and the nash certainty equivalence principle. Communications in
Information & Systems 6: 221–52.

Kiesel, Rüdiger, and Florentina Paraschiv. 2017. Econometric analysis of 15-minute intraday electricity prices.

Energy Economics 64: 77–90. [CrossRef]

Lacker, Daniel. 2020. On the convergence of closed-loop Nash equilibria to the mean ﬁeld game limit. Annals of

Applied Probability 30: 1693–761. [CrossRef]

Lasry, Jean-Michel, and Pierre-Louis Lions. 2007. Mean ﬁeld games. Japanese Journal of Mathematics 2: 229–60.

[CrossRef]

Lasry, Jean-Michel, and Pierre-Louis Lions. 2018. Mean-ﬁeld games with a major player. Comptes Rendus

Mathematique 356: 886–90. [CrossRef]

Nourian, Mojtaba, and Peter E. Caines. 2013. (cid:101)-Nash mean ﬁeld game theory for nonlinear stochastic dynamical

systems with major and minor agents. SIAM Journal on Control and Optimization 51: 3302–31. [CrossRef]

Shrivats, Arvind, Dena Firoozi, and Sebastian Jaimungal.

A mean-ﬁeld game approach to
equilibrium pricing, optimal generation, and trading in solar renewable energy certiﬁcate (srec) markets.
arXiv arXiv:2003.04938.

2020.

Tan, Zongjun, and Peter Tankov. 2018. Optimal trading policies for wind energy producer. SIAM Journal on

Financial Mathematics 9: 315–46. [CrossRef]

Publisher’s Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional
afﬁliations.

c(cid:13) 2020 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access
article distributed under the terms and conditions of the Creative Commons Attribution
(CC BY) license (http://creativecommons.org/licenses/by/4.0/).

