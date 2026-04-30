Contents lists available at ScienceDirect

Energy Strategy Reviews

journal homepage: http://www.elsevier.com/locate/esr

The flow based market coupling arrangement in Europe: Implications
for traders

☆

Tarjei Kristiansen

SINTEF Energy Research, Sem Sælands Vei 11, 7034, Trondheim, Norway

A R T I C L E  I N F O

A B S T R A C T

Index Terms:
Flow based market coupling
Congestion management
Continental European power market
Power system economics

A new method for congestion management, flow based market coupling (FBMC), launched on May 21, 2015 in
the Central Western European (CWE) region. Prior to this, no similar congestion method has been implemented
elsewhere.  FBMC  models  the  electrical  network,  considering  cross-border  exchanges  including  security  con-
straints.  The  flows  span  all  available  parallel  paths  as  governed  by  the  laws  of  physics.  The  objective  is  to
optimize  market  flows  and  social  welfare.  FBMC  allocates  cross-border  flows  considering  power  transfer  dis-
tribution factors (PTDFs) which describe the sensitivity of a change in import/export at a particular country. The
PTDF matrix and the remaining available margin (RAM) determine the feasible transmission region at any given
point  in  time.  On  a  daily  basis,  the  Capacity  Auctioning  Service  Company  (CASC)  gives  information  about
maximum bilateral exchanges, minimum and maximum net positions and PTDFs for the day-ahead market. This
daily  tool  serves  as  a framework  for  analyzing  potential congestion  in  the CWE  region  and price  coupling of
markets in individual hours. We explain how traders can apply the CASC tool to analyze potential congestion and
identify trade opportunities. We discuss some approaches to analyze the FBMC beyond the day-ahead market.

1. Introduction

This  paper  gives  an  overview  and  analysis  of  flow  based  market
coupling (FBMC), a new method for managing congestion in the Central
Western European (CWE) region We analyze the results of the parallel
runs from 2013 to 2015 including the operational runs from its inception
on May 21, 2015 to March 31, 2016. During the parallel runs, flow based
parameters were computed in parallel with available transmission ca-
pacities (ATCs) and used to run market coupling simulations, based on
the  same  order  books  of  the  power  exchanges.  On  a  daily  basis,  the
Capacity Auctioning Service Company (CASC) gives information about
maximum  bilateral  exchanges,  minimum  and  maximum  net  positions
and  PTDFs  for  the  day-ahead  market.  This  online  tool  serves  as  a
framework  for  analyzing  potential  congestion  in  the  CWE  region  and
price coupling of markets in individual hours. Although FBMC has added
more complexity to electricity market analyses and trading, it provides
previously  unavailable  data  to  analyze  transmission  congestion  and
price differentials. Beyond the day-ahead market, FBMC implies highly
inter-related flows and integration of the entire CWE region.

The structure of the paper is as follows. Section 2 describes the his-
tory  of  market  coupling  in  Europe.  Section  3  briefly  reviews  the

literature  on  FBMC.  Section  4  provides  a  mathematical  overview  of
FBMC.  Section  5  analyzes  the  results  of  the  FBMC  parallel  runs  from
2013 to 2015 and compares the prices to the ATC method. Section 6
outlines some analytical frameworks for FBMC. Section 7 analyzes the
results  from  the  operational  FBMC  from  May  21,  2015  to  March  31,
2016. Section 8 discusses the implications and explains how traders can
apply the CASC to analyze potential congestion and identify trade op-
portunities. Section 9 concludes.

2. History of market coupling

Initially, cross-border trading among the Central Western European
(Germany,  France,  the  Netherlands  and  Belgium,  or  CWE)  electricity
markets involved auctioning cross-border capacity to the market sepa-
rately and independently from the electricity trading market place [1].
Thus, it occurred that flows could go from high to low price areas if the
market participants’  price  expectation  was  incorrect. After  November
22,  2006,  when  the  tri-lateral  market  coupling  (TLC)  among  France,
Belgium and the Netherlands was implemented [1,2], implicit capacity
auctioning  was  undertaken  by  only  trading  energy  for  the  day-ahead
market. The arrangement can best be described as a single centralized

☆

The views in this paper are not necessarily those of SINTEF Energy Research.
E-mail address: tarjei.kristiansen@sintef.no.

https://doi.org/10.1016/j.esr.2019.100444
Received 25 January 2017; Received in revised form 16 October 2019; Accepted 5 December 2019

EnergyStrategyReviews27(2020)100444Availableonline17December20192211-467X/©2019TheAuthor(s).PublishedbyElsevierLtd.ThisisanopenaccessarticleundertheCCBY-NC-NDlicense(http://creativecommons.org/licenses/by-nc-nd/4.0/).T. Kristiansen

price  coupling  system  that  calculated  market  prices  and  trading  vol-
umes, based on available cross-border capacity and the order books of
the  power  exchanges.  The  objective  was  to  maximize  social  welfare
subject to ATC. The ATC, which indicated the maximum capacity that
could be exchanged commercially across a border in a given direction,
only  considered  bilateral  transactions  and  above  already  committed
utilization.  Mathematically,  ATC  equals  the  total  transfer  capability
(TTC) less the transmission reliability margin (TRM) and less the sum of
existing long-term nominations. Thus, TSOs had to choose how to split
the capacity among the borders of France, Belgium and the Netherlands,
and  eventually  the  minimum  ATC  value  was  selected.  However,  the
feasible region was generally more restrictive than under FBMC because
the simplified modelling neglected many electrical characteristics.

On November 9, 2010 the day-ahead ATC market coupling for the
CWE  region  (Germany,  France,  the  Netherlands  and  Belgium)  was
implemented [1,3]. Basically, an extension of TLC, it included Germany
with similar price and flow calculations. Finally, on May 21, 2015, the
flow based market coupling (FBMC) was implemented for the CWE re-
gion.  FBMC  models  the  electrical  network,  considering  cross-border
exchanges including security constraints [2]. The flows span all avail-
able parallel paths as governed by the laws of physics. The objective is to
optimize market flows and social welfare.

3. Literature review

Bergh et al. [4], who describe the concepts and definitions utilized in
FBMC, observe that the methodology is complex and poorly understood.
Market  participants  rate  their  own  understanding  at  an  intermediate
level [5]. Aguado et al. [6] use FBMC to evaluate historical order books
and  conclude  that  the  transmission  capacity  made  available  is  larger
under  FBMC  than  ATC.  Waniek  et  al.  [7]  reach  similar  conclusions.
Marien et al. [8] demonstrate that FBMC’s parameters have substantial
impacts  on  market  outcomes.  Thus,  they  argue  for  transparency  and
monitoring of the FBMC calculation process. SINTEF Energy [9] perform
simulations using a flow-based model called Samnett to investigate the
possible advantages of FBMC compared to ATC; the results show that
Samnett has more efficient use of the grid and lower price differences
and provides a higher socio-economic surplus than the Samlast (ATC)
model.

4. Mathematical formulation of flow based market coupling

FBMC  uses  the  physical  transmission  constraints  of  the  electrical
network and allocates cross-border flows, considering the power trans-
fer distribution factors (PTDFs) which provides sensitivity information
about a change in import/export at a particular hub or country [10]. The
PTDF  matrix  and  remaining  available  margin  (RAM)  determine  the
feasibility region (or security domain) at any given point in time. The
maximum exchange values are generally greater than the ATC values
but cannot be allocated simultaneously.

With FBMC it is theoretically possible that power flows from a high
price area to a low price area if this increases social welfare, and the
flows obey the laws of physics. However, this is not possible because
FBMC’s current implementation (intuitive) enforces exporting from the
most inexpensive markets, albeit at the cost of lower social welfare.

FBMC’s important concepts are as follows [10]:

Generation shift key (GSK): Best estimate of how a country’s total
generation is distributed among the generators within the country or
area.
Power transfer distribution factor (PTDF): Specifies the incremental
flow of a 1 MW transaction between two hubs (for example A and B)
on a given critical branch (CB).
Critical  branch  (CB):  A  transmission network  element  (line,  trans-
former, or a normal or contingency operational situation) by cross-
border  trade  and  monitored  under  operation;  determination  of

each CB’s available physical capacity is based on the physical limit of
the line and considering necessary security margins.
Critical branches/critical outages (CBCOs): Tripping of a line, cable,
transformer, busbar, generating unit, significant load, or k elements;
also contingency cases (N-1, N-2) representing outages.
Remaining available margin (RAM): Maximum flow minus the flow
in the base case including long term capacities and minus the flow
reliability  margin;  RAM  specifies  the  free  margin  for  every  cross-
border.

Modelling  the  entire  grid,  including  contingency  scenarios,  would
amount  to  a  large  number  of  constraints  and  be  computationally
burdensome.  Thus,  modelling  limits  the  number  of  constraints  to  the
critical branches that are significantly affected by cross-border trade and
that potentially could become congested due to grid security reasons.
Congestion  in  FBMC  is  not  only  monitored  on  borders,  but  also  on
critical branches that are internal to countries.

4.1. Definitions

cb: the PTDF of zone z on a critical branch cb

cb 2 CB: one critical branch cb as a subset of all critical branches CB
z 2 CWE: zone z as a subset of all CWE zones
b 2 B: bidder b as a subset of all bidders B
PTDFz
nexz: the net import/export position of zone z
RAMcb: the allocated margin on critical branch cb
ðQz
b  in  MW  is
negative if it is a supply bid and positive if it is a demand bid. The
price Pz
xz
b: the accepted part of the bid b, between 0 and 1

Þ : the  bid  of  bidder  b  in  area  z.  The  quantity  Qz

b  is in €/MW

b;Pz
b

4.2. Objective function

Mathematically  the  objective  function  equals  three  components:

seller surplus, buyer surplus and congestion revenue defined as [10]:

(1)

X

X

max

x2CWE

b2B

Qz

bPz

bxz

b

Power exchanges provide order books. The decision variables are the
net positions in the CWE region (Germany, France, the Netherlands and
Belgium) and the accepted part of the bids.

4.3. Constraints

The sum of the net positions must equal zero. A positive net position

indicates exports and a negative indicates imports.

Mathematically, the balancing constraint ensuring that supply equals

demand bids is:
X

nexz ¼ 0;

z2CWE

where

nexz ¼ (cid:0)

X

b2B

Qz

bxz

b

The flow based constraints limit the CBCO’s flow [10].

X

PTDFz

cb⋅nexz � RAMcb

8cb 2 CB:

(2)

(3)

(4)

z2CWE

If the social welfare is maximized without any binding constraints,
the RAMs of the critical branches can support all market transactions. In
this case the prices are equal in all four zones.

Conversely, if a constraint is active (RAM is fully allocated), trans-
mission congestion occurs, and the price in each zone is related to the
magnitude of the PTDFs of the critical branch. The binding constraint

EnergyStrategyReviews27(2020)1004442T. Kristiansen

has  a  shadow  price  which  represents  the  increase  in  social  welfare
caused  by  making  1  MW  more  capacity  available  to  the  market.  The
country  price  differentials  are  proportionate  to  the  sensitivity  (i.e.
shadow price) it has on the constraint as well as the relative difference in
PTDFs [10]:

reported  in  Table  1;  losses  in  both  approaches  are  ignored.  The  key
features of ATC and FBMC are reported in Table 2.

For further information and background on FMBC, see ETSO [12], De

Jong et al. [13], Glachant [14] and Van der Berg et al. [4].

Pz (cid:0) Py
PTDFy (cid:0) PTDFz

¼ shadow price � 0;

5. Results from the parallel runs from 2013 to 2015

(5)

where  zones  z  and  y  are  a  subset  of  all  CWE  zones.  A  single  active
constraint  is  therefore  sufficient  to  create  four  different  prices  since
dispatch has to be adjusted to avoid overloading transmission lines. The
zonal  prices  will  then  be  calculated  on  that  adjusted  dispatch.  For  a
given constraint, the smaller the PTDF, the higher the price will be in
that zone [10]:

PTDFz > PTDFy→Py > Pz:

(6)

The equations reflect the physics of the electrical network and pri-
oritize  the  exchanges  using  the  least  transmission capacity.  Exchange
bids related to a hub with a smaller PTDF over a critical branch will have
priority even if their price is higher than a similar exchange bid related
to a hub with a higher PTDF over the same critical branch [10].

The price properties of FBMC are generalized as:

X

Pz (cid:0) Py ¼

ðPTDFy (cid:0) PTDFzÞμcb;

(7)

cb2CWE

where μcb is the shadow price of the critical branch. Eq. (7) states that the
price difference between two locations y and z is equal to the sum over
all congested branches of the PTDF difference for the locations multi-
plied by the shadow prices for the congested branches.

Note that PTDFA-PTDFB  represents the incremental flow of a 1 MW
transaction between hubs A and B on a given critical branch. The PTDF
value itself is meaningless. In fact, PTDFs are calculated using a slack
hub, and they represent the incremental flow on a given critical branch
of a 1 MW transaction between the hub the PTDF value refers to and the
slack hub.

In  the  ATC  method,  each  TSO  considered  historical  data  for  a
reference  day,  considering  loop  flows,  seasonal  impact  and  security
margin,  and  determined  a  net  transfer  capacity  (NTC)  value  for  each
direction on each border of its control area. NTCs can be viewed as the
maximum allowable commercial1 exchanges that put a critical network
element  to  its  maximum  physical  flow.  Neighbor  TSOs  coordinate
bilaterally to agree upon an NTC  value predominantly limited by the
lower NTC value. From the NTC values, ATC values can be determined
by subtracting long term nominations.

In the ATC method the following property holds:

where  μz->y  is  the  shadow  price  of  a  unidirectional  interconnector
transporting power from area z to y.

Thus, under FBMC the country price differentials in FBMC are pro-
portionate  to  the  electrical  characteristics  of  the  network  and  that
congestion on one border is sufficient to cause price differences in all
countries. Conversely, under ATC the country price difference between
two  countries  only  depends  on  the  shadow  price  on  the  border  con-
necting  those  countries.  Thus,  congestion  on  the  various  borders  is
independent.

2.4. Comparison

The  advantages  and  drawbacks  of  FBMC  and  ATC  approaches  are

1  Commercial  capacity  is  the  amount  of  trade  that  puts  a  critical  network
element to its maximum physical power flow. Physical capacity is the amount
of power that can flow over an unconstrained line.

Parallel runs of ATC vs FBMC conducted by the CASC from 2013 to
2015, show that social welfare and cross-border flows increased as more
capacity  was  made  available  to  the  market.  Likewise,  cross-border
country  price  differentials  decreased.  Germany’s  ability  to  exported
more  power  supported  its  domestic  prices,  whereas  Belgium  and  the
Netherlands imported more power which depressed their domestic pri-
ces.  France  experienced  a  small  price  decrease.  On  average,  German
prices  increased  by  1.35  €/MWh,  Belgian  prices  decreased  by  2.85
€/MWh,  Dutch  prices  decreased  by  2.17  €/MWh  and  French  prices
decreased slightly by 0.51 €/MWh. The results are reported in Table 3.
Likewise,  the  cross-border  spreads  calculated  from  2013  to  2015
show  that  prices  decreased  the  most  between  Germany  and  the
Netherlands (3.52 €/MWh), whereas they increased between France and
Belgium (2.33 €/MWh) and France and Germany (1.86 €/MWh), and
slightly  increased  slightly  (0.68  €/MWh)  between  Belgium  and  the
Netherlands. The results are reported in Table 4; the convention in the
table is “source” to “sink”.

Some price differentials mathematically increased but only because

the price differential for these borders “happened” to be negative.

6. Analytical methods for the flow based market coupling
method

In  this  section  we  discuss  two  analytical  frameworks  for  the  flow
based  market  coupling  method.  The  first  approach  utilizes  the  utility
tool published daily by CASC. The second approach utilizes historical
analysis of constraints.

6.1. The utility tool

Each day at 8.30 a.m. and 10.30 a.m. on the day before delivery,
CASC publishes market and operational information. The online tool’s
interface allows users to check for different simultaneous cross-border
trades.  The  tool  contains  ex  ante  information  about  the  relevant
PTDFs and RAMs including maximum bilateral exchanges and minimum

Table 1
Advantages and drawbacks of FBMC and ATC.

FBMC

ATC

Forecasts for longer term
transmission capacity are
available
“Easier” to understand and use

Higher social welfare as more
transmission capacity becomes
available
More efficient use of the electrical
network
Coordinated capacity calculation and
allocation mechanism
Obeys the laws of physics
Formulates transmission constraints
to reflect the network’s physical
limitations
Larger security domain, i.e., larger set
of trading opportunities

Cons  More complicated analyses of

congestion for the day-ahead market
More complicated price forecasting
for the day-ahead market
Trading longer term contracts is more
difficult since there is no forecast of
future transmission capacity

Lower social welfare as less
transmission capacity becomes
available
Uncoordinated capacity
calculation and allocation
mechanism
Ignores the laws of physics
Smaller security domain, i.e.,
smaller set of trading
opportunities

Pz (cid:0) Py ¼ μz→y (cid:0) μy→z;

(8)

Pros

EnergyStrategyReviews27(2020)1004443T. Kristiansen

Table 2
Summary of the key differences between FBMC and ATC [11].

Available
capacity
calculation

Verification
Long term
inclusion

Capacity

allocation

FBMC

ATC

Regional coordination among
TSOs
Set of critical branches with
associated available physical
capacity
24 time-stamps verified daily
Each considered critical
branch
Constraint for each considered
branch
Market based allocation via
bids and offers

Bilateral coordination
between TSOs
Commercial capacity (NTC)
values for each border
direction
2 time- stamps verified daily
Each direction on each
border
Constraint for each direction
on each border
Capacity predetermined

and maximum net positions. The main page or “Market view” is shown
in Fig. 1.

The most important spreadsheets in the Excel file are as follows [15]:

PTDFs_Early  Publication:  Ex  ante  PTDF  matrix  and  RAMs  for  pre-
solved critical branches for the next day excluding long term nomi-
nations for each single hour
PTDFs:  Ex  ante  PTDF  matrix  and  RAMs  for  pre-solved  critical
branches for the next day following long term nominations for each
single hour
Max net pos: Ex ante minimum and maximum net positions in each
CWE  country  for  the  following  day;  the  min/max  net  positions
depend  on  the net  positions of  the other hubs.  Thus, they are  not
simultaneously feasible.
Max  exchanges  (Maxbex):  Ex  ante  maximum  bilateral  exchanges
between each CWE country for the following day assuming that the
other net positions are null
Net  position:  Ex  post  CWE  net  positions  in  MW  computed  by  the
market  coupling  algorithm;  published  at  1  p.m.  the  day  before
delivery

Table 3
Results of the parallel runs ATC vs FBMC for 2013, 2014 and 2015.

ATC

FBMC

Delta

Germany
France
Belgium
Holland
Germany
France
Belgium
Holland
Germany
France
Belgium
Holland

Q1-13

43.77
54.15
56.34
54.54
46.03
51.09
54.07
55.06
2.26
(cid:0) 3.06
(cid:0) 2.27
0.52

Q2-13

32.65
33.56
45.84
52.10
33.72
34.69
40.97
47.90
1.07
1.13
(cid:0) 4.87
(cid:0) 4.20

Q3-13

38.26
36.73
38.27
48.49
38.81
36.86
37.33
46.52
0.55
0.13
(cid:0) 0.94
(cid:0) 1.97

Q4-13

37.69
48.10
47.54
52.10
39.81
46.54
46.27
48.76
2.12
(cid:0) 1.56
(cid:0) 1.27
(cid:0) 3.34

Table 4
Cross-border spreads of the parallel runs ATC vs FBMC for 2013, 2014 and 2015.

ATC

FBMC

Delta

BE-NL
DE-NL
BE-FR
FR-DE
BE-NL
DE-NL
BE-FR
FR-DE
BE-NL
DE-NL
BE-FR
FR-DE

Q1-13

(cid:0) 1.80
10.77
(cid:0) 2.19
(cid:0) 10.38
0.99
9.03
(cid:0) 2.98
(cid:0) 5.06
2.79
(cid:0) 1.74
(cid:0) 0.79
5.32

Q2-13

6.26
19.45
(cid:0) 12.28
(cid:0) 0.91
6.93
14.18
(cid:0) 6.28
(cid:0) 0.97
0.67
(cid:0) 5.27
6.00
(cid:0) 0.06

Q3-13

10.22
10.23
(cid:0) 1.54
1.53
9.19
7.71
(cid:0) 0.47
1.95
(cid:0) 1.03
(cid:0) 2.52
1.07
0.42

Q4-13

4.56
14.41
0.56
(cid:0) 10.41
2.49
8.95
0.27
(cid:0) 6.73
(cid:0) 2.07
(cid:0) 5.46
(cid:0) 0.29
3.68

Allocated capacities: Ex post allocated capacities computed from the
CWE net positions resulting from the bilateral exchange computation
(BEC) assuming the constraint is intuitive; published at 1 p.m. the
day before delivery
Price  spreads:  Ex  post  market  price  spread  in  €/MWh  for  the  two
directions; published at 1 p.m. the day before delivery
All CBCO fixed label: Information about the ex post CBCOs used for a
particular date with a fixed label; each row provides the features of
one CBCO per hour; published two days after the delivery date

“Market view,”  PTDFs, max net pos and max exchanges (Maxbex)
can be used prior to the clearing of the day-ahead market to identify
potentially  binding  constraints.  Historical  net  positions,  allocated  ca-
pacities, price spreads and CBXO fixed labels are retrieved by specifying
the date of interest.

An example of the first step in an ex ante analysis include:

In the volume (interactive) module in the “Market view” sheet, the
uses can specify hub to hub exchanges or hub positions and check for
the date and hour of interest. If the combinations are infeasible, cells
will  be  marked  “Constrained  Transmission  System”  in  red.  Thus,
traders can check the simultaneous execution of trading volumes in
CWE markets.
In the max volume (information) module in the “Market view” sheet,
the user can find the maximal trade volumes (MWh/h) which can be
physically transported between two hubs under the condition that no
other trade is executed between other hubs.
Are there any changes in maximum bilateral exchanges day on day or
similar weekday the previous week? Curtailments in maximum ex-
changes  can  lead  to  congestion  on  the  relevant  border  with  the
exporting hub exposed to lower prices and the importing region to
higher prices. Conversely, if maximum exchanges increase, it facili-
tates  higher  exports  with  higher  prices  in  the  exporting  hub  and
lower prices in the importing hub.

Q1-14

33.26
37.58
38.45
42.82
34.15
37.05
38.11
40.55
0.89
(cid:0) 0.53
(cid:0) 0.34
(cid:0) 2.27

Q1-14

4.37
9.56
(cid:0) 0.87
(cid:0) 4.32
2.44
6.40
(cid:0) 1.06
(cid:0) 2.90
(cid:0) 1.93
(cid:0) 3.16
(cid:0) 0.19
1.42

Q2-14

31.38
31.55
39.17
38.61
31.79
32.92
34.72
35.85
0.41
1.37
(cid:0) 4.45
(cid:0) 2.76

Q2-14

(cid:0) 0.56
7.23
(cid:0) 7.62
(cid:0) 0.17
1.13
4.06
(cid:0) 1.80
(cid:0) 1.13
1.69
(cid:0) 3.17
5.82
(cid:0) 0.96

Q3-14

31.49
28.40
39.02
38.65
32.28
29.65
34.13
36.44
0.79
1.25
(cid:0) 4.89
(cid:0) 2.21

Q3-14

(cid:0) 0.37
7.16
(cid:0) 10.62
3.09
2.31
4.16
(cid:0) 4.48
2.63
2.68
(cid:0) 3.00
6.14
(cid:0) 0.46

Q4-14

34.82
40.89
46.19
44.37
36.51
39.96
42.08
42.16
1.69
(cid:0) 0.93
(cid:0) 4.11
(cid:0) 2.21

Q4-14

(cid:0) 1.82
9.55
(cid:0) 5.30
(cid:0) 6.07
0.08
5.65
(cid:0) 2.12
(cid:0) 3.45
1.90
(cid:0) 3.90
3.18
2.62

Q1-15

32.11
44.92
46.69
43.01
34.47
42.50
44.19
41.95
2.36
(cid:0) 2.43
(cid:0) 2.50
(cid:0) 1.06

Q1-15

(cid:0) 3.68
10.90
(cid:0) 1.76
(cid:0) 12.81
(cid:0) 2.24
7.48
(cid:0) 1.69
(cid:0) 8.02
1.44
(cid:0) 3.42
0.07
4.79

average

35.05
39.54
44.17
46.08
36.40
39.03
41.32
43.91
1.35
(cid:0) 0.51
(cid:0) 2.85
(cid:0) 2.17

average

1.91
11.03
(cid:0) 4.62
(cid:0) 4.49
2.59
7.51
(cid:0) 2.29
(cid:0) 2.63
0.68
(cid:0) 3.52
2.33
1.86

EnergyStrategyReviews27(2020)1004444T. Kristiansen

Fig. 1. CASC’s utility tool.

Are there any changes on minimum and maximum net positions? A
higher  minimum  or  maximum  net  position  indicates  a  better  sup-
plied hub. Conversely, a lower maximum or minimum net position
indicates a more strained supply-demand balance.

After  obtaining  this  information,  the  second  step  is  to  reduce  the

number of potentially binding RAM constraints, considering:

Exporting country: Constraining critical branch with PTDF >0
Importing country: Constraining critical branch with PTDF <0
Low  RAM  value  indicates  a  higher  probability  of  congestion  and
price decoupling

Country net positions are the inputs in the RAM constraints. Thus,
the starting point is a view on the supply-demand balance in each CWE
country.  The  net  position,  defined  as  supply  minus  demand  for  each
country,  indicates  the  degree  of  tightness  in  the  relevant  country.  A
country with little tightness has surplus power for exports, i.e., a positive
net position and a country with a high degree of tightness has a deficit, i.
e., a negative net position. The net position for a country equals the sum
of  country  export  minus  imports  and  long-term  nominations  to/from
other  CWE  countries.  After  analyzing  the  supply-demand  balance  in
each CWE country, the number of potentially binding constraints can be
reduced.  Countries  with  deficits  should  consider  negative  PTDFs  and
countries with surplus should consider positive PTDFs. Constraints with
the highest RAM can be excluded since they are not likely to be binding.
The final step is to test the feasibility of various net positions if they
do not violate any transmission constraints. If there are no violations, it
is likely that prices will couple in those hours, whereas if constraints are
violated, prices will decouple in those hours. The recent net positions
give indications of the present tightness in the country.

Alternatively, a user can build a simulation tool with a social welfare
objective, given expectations about the hourly country prices and RAM
constraints  including  PTDFs.  Country  net  positions  are  the  decision
variables. This alternative tool allows the user to identify the binding
constraints, given country price expectations and determine the hours
when prices decouple.

6.2. Historical analysis of binding constraints

It  is  also  useful  to  track  the  history  of  active  constraints.  CASC
publishes active constraints two days after delivery. The numerical code
differentiating the various border/countries, is retrieved from the two
first  numbers  in  the  ID  of  the  relevant  constraint  [15]  as  shown  in
Table 5.

Each day at 1pm on the day before delivery, CASC publishes the net

positions. The active constraints can be identified by inserting the hourly
net positions for each country in eq. (4). If the left-hand side is greater
than or equal to the right-hand side, the constraint is active and binding,
i.e., the actual PTDF values for active constraints are identified. When
multiplied by the respective net positions, the congested hub and the
cause (import or export) of the congestion is identified.

However, two days ex post, the actual congested borders or locations
can  be  identified.  Some  constraints  may  span  over  several  days.  By
keeping  a  record of the  active  constraints, a  user can generate  useful
statistics about the most common cross-border congestion constraints.2

7. Flow based market coupling results from the operational runs

Average cross-border spreads from May 21, 2015 to March 31, 2016
are listed in Table 6. Compared to the full parallel run analysis period,
prices  decreased  for  the  Belgian-Dutch  border,  the  Belgian-French
border and the French-German border and increased for the German-
Dutch  border  prices.  The  most  congested  borders  were  the  French-
German  border  and  the  Belgian-Dutch  border.  The  price  duration
curves are illustrated in Fig. 2.

Monthly cross-border spreads for the same time period are listed in
Table 7. The largest spreads in the winter months were French-German

Table 5
Codes for borders/countries in the CWE region.

Code

Border/Country

11
12
13
14
15
16
17
18

BE
BE-NL
NL
NL-DE
DE
DE-FR
FR
FR-BE

2  It is useful to study locational marginal pricing markets in the United States
when  building  historical  transmission  congestion  databases.  This  analytics
framework could include the following [16]: 1) Transmission map highlighting
key transmission lines, interfaces, etc., 2) Identification of flow directions based
on historical prices, 3) Identification of historical bottlenecks, 4) Database of
real time and day-ahead prices, shadow prices, congestion, etc., 5) Digital map
or contour map showing different variables (prices, congestion, outages, etc.)
stored in database mentioned in 4., 6) Monitoring every market constraint and
explanation  (self-analysis;  media  coverage;  system  and  transmission  operator
reports).

EnergyStrategyReviews27(2020)1004445T. Kristiansen

border and the Belgium-Dutch border. The largest spread from August to
October was the Belgian-French border when the outage of several nu-
clear  plants  caused  a  tight  supply  situation  in  Belgium.  The  largest
spread in the summer months June to August was the German-Dutch
border  when  Dutch  prices  were  supported  by  the  same  tight  supply
situation  in  Belgium.  The  most  frequent  congestion  was  the  German-
Dutch and the Belgium-Dutch borders.

Net positions for the CWE countries are listed in Table 8. Germany
was a net exporter because it had vast amounts of renewables. Imports to
France were higher in the winter months. France exported more in the
summer months when demand was low. Belgium and the Netherlands
imported on average in all months.

8. Implications for traders

The introduction of FBMC has led to a change in trading patterns.
Moreover,  CASC  only  issues  the  utility  tool  twice  for  the  day-ahead
market. The only change observed between the 8.30 a.m. version and
the  10.30  a.m.  version  is  the  inclusion  of  long  term  nominations.
Without price driving information at 10.30 a.m., traders cannot antici-
pate  the  future  PTDFs,  maximum  bilateral  exchanges  and  minimum/
maximum net positions. Over time, it can be assumed that tech-savvy
traders will be hired or educated, so that FBMC will be well-understood.
For  the  day-ahead  market,  traders  may  utilize  information  about
maximum bilateral exchanges from the utility tool published ex ante. An
increase  in  maximum  bilateral  exchange  indicates  a  likelihood  of
decreased country price differential as the price in the exporting country
increases and the price in the importing country decreases. Conversely, a
decrease  in  maximum  bilateral  exchange  indicates  a  likelihood  of
increased country price differential as the price in the exporting country
decreases  and  the  price  in  the  importing  country  increases.  It  is  also
useful  to study the daily  or weekend to weekend change in the early
publication  PTDFs  from  the  utility  tool.  An  increase  in  the  PTDF  dif-
ferential indicates the likelihood of higher country price differentials,
whereas a decrease in the PTDF differential indicates the likelihood of
lower country price differentials.

Trading contracts beyond the day-ahead market is very complex in
FBMC.  For  example,  highly  inter-related  flows  require  studying  the
entire CWE region in depth. Chantelou [17] questions whether PTDFs
and RAM can be translated into simpler metrics to evaluate the level of
transmission constraints and represent the effects of FBMC in a funda-
mental  market  model.  FBMC’s  constraints  define  a  feasible  security
domain for flows within CWE [17]. This domain may be viewed as a
volume in the space of net positions by three of the four CWE countries.3
The domain is characterized by the CWE flow-based volume which in-
dicates the level of transmission congestion, i. e., the lower the volume,
the  more  constrained  the  system.  Additionally,  the  CWE  flow  based
import/export volume can help traders understand where FBMC’s con-
straints  are  most  binding  in  the  space  of  net  hub  positions.  For  each
country, the sum of export and import quadrant volumes equals the total
volume. It is possible to compare two domains by calculating the dis-
tance  between  them  as  specified  by  the  volume  of  space  which  is

Table 6
Cross-border spreads of FBMC from May 21, 2015 to March 31, 2016.

FBMC

Border

BE-NL
DE-NL
BE-FR
FR-DE

Average

Total number of congested hours

(cid:0) 3.85
5.25
(cid:0) 4.80
(cid:0) 4.30

1808
4468
1083
601

3  The net position of the fourth country can be expressed as the sum of the

other three countries.

Fig. 2. Price duration curves from May 21, 2015 to March 31, 2016.

Table 7
Monthly cross-border spreads of FBMC from May 21, 2015 to March 31, 2016.

Month

May-15
Jun-15
Jul-15
Aug-15
Sep-15
Oct-15
Nov-15
Dec-15
Jan-16
Feb-16
Mar-16

BE-NL

1.14
(cid:0) 0.26
(cid:0) 0.47
(cid:0) 3.52
(cid:0) 12.84
(cid:0) 14.03
(cid:0) 4.64
(cid:0) 2.25
(cid:0) 1.04
(cid:0) 0.18
(cid:0) 0.99

DE-NL

5.11
8.68
7.14
7.29
7.80
2.08
6.07
5.95
2.54
3.20
1.86

BE-FR

(cid:0) 3.20
(cid:0) 6.90
(cid:0) 4.65
(cid:0) 10.27
(cid:0) 15.08
(cid:0) 10.49
(cid:0) 1.42
(cid:0) 0.81
0.99
0.14
(cid:0) 0.03

FR-DE

(cid:0) 0.77
(cid:0) 2.04
(cid:0) 2.96
(cid:0) 0.54
(cid:0) 5.56
(cid:0) 5.62
(cid:0) 9.29
(cid:0) 7.38
(cid:0) 4.57
(cid:0) 3.52
(cid:0) 2.81

Table 8
Monthly net positions for Germany, France, the Netherlands and Belgium from
May 21, 2015 to March 31, 2016.

Month

maj-15
jun-15
jul-15
aug-15
sep-15
okt-15
nov-15
dec-15
jan-16
feb-16
mar-16

DE

2627
2167
1027
1110
1696
1914
2722
3316
2630
3663
3096

FR

1401
1528
1974
2331
152
(cid:0) 223
(cid:0) 852
(cid:0) 1459
(cid:0) 1571
(cid:0) 1698
(cid:0) 1604

BE

(cid:0) 1258
(cid:0) 1633
(cid:0) 2013
(cid:0) 2127
(cid:0) 1628
(cid:0) 1667
(cid:0) 1339
(cid:0) 1326
(cid:0) 58
(cid:0) 601
(cid:0) 374

NL

(cid:0) 2771
(cid:0) 2062
(cid:0) 988
(cid:0) 1314
(cid:0) 220
(cid:0) 25
(cid:0) 531
(cid:0) 531
(cid:0) 1001
(cid:0) 1364
(cid:0) 1117

included in only one of the domains. Chantelou [17], who states that the
FBMC security domain is only one factor to consider when looking at
prices in the CWE region, defines a convergence metric as the sum of the
absolute price difference between a specific CWE country and the other
CWE countries. The metric only indicates the level of electrical network
constraints. FBMC’s domain volume explains convergence only partially
because of the effects of other market fundamentals.

Modelling FBMC’s market fundamentals in the medium/long term
will require anticipating FBMC’s constraints beyond the day-ahead [17],
and developing a fundamental model of the entire CWE region and the
possible flows that can be limited by FBMC’s constraints.

It may be possible to apply constraints from a similar day in the past
to  model  the  future,  after  formally  defining  “similar”  from  the
perspective of FBMC perspective. Chantelou [17] suggests consumption,
solar generation and wind generation in France, Netherlands, Belgium
and Germany, and wind generation in the four German TSO zones as
variables.

EnergyStrategyReviews27(2020)1004446T. Kristiansen

9. Conclusions

This paper discussed the mathematical formulation and parameters
of the flow based market coupling method (FBMC) implemented on May
21, 2015 in the CWE region. Initially, a cross-border trade in the CWE
region involved separate auctions of energy and transmission capacity.
However,  if  the  market  participants’  price  expectation  was  incorrect,
flows could move from a high price area to a low price area. To address
the problem, implicit auctioning, where energy only was traded in the
day-ahead  market,  considering  the  electrical  characteristics  of  the
network was implemented. FBMC uses the electrical network’s physical
transmission  constraints  and  allocates  cross-border  flows,  considering
the  PTDFs,  which  provides  sensitivity  information  about  a  change  in
import/export at any particular hub or country. The country price dif-
ferentials in FBMC are proportionate to the network’s electrical char-
acteristics,  and  congestion  on  one  border  is  sufficient  to  cause  price
differentials in all countries. The merits of FBMC have included higher
social welfare, efficiency, coordinated capacity calculations, electrical
representation of the network and a larger set of trading opportunities.
Parallel  run  results  and  operational  results  from  the  flow  based
market  coupling  between  2013  and  2015  were  analyzed.  Among  the
findings,  cross-border  country  price  differentials  decreased  as  exports
and  imports  rose  because  of  increased  cross-border  capacity.  German
prices  increased,  whereas  Dutch  and  Belgium  prices  decreased.  The
result was lower German-Dutch price spreads but higher French-Belgian
and  French-German  price  differentials.  The  most  frequent  congestion
was  the  German-Dutch  and  the  Belgium-Dutch  borders.  However,
French-Belgium congestion gradually decreased as the supply situation
improved.

Two possible online tools for use by traders to take full advantage of
FBMC  were  suggested.  Both  tools  require  extensive  analytical  and
forecasting ability. CASC’s online utility tool is presently available only
for the day-ahead market, and trading contracts beyond the day-ahead
market  requires  studying  the  entire  CWE  region.  The  other  tool  in-
volves constructing, and updating, a model of real time and historical
data in spreadsheets and other electronic formats to help traders identify
trends and forecast potential congestion trouble spots.

In  conclusion,  the  flow  based  market  coupling  mechanism,  while
more demanding to use, leads to higher social welfare and cross-border
flows  than  the  simpler  ATC  model.  However,  if  transmission  system
operators continue to only publish forecasts of power transfer distribu-
tion  factors  for  the  day-ahead  market,  traders  will  find  it  difficult  to
forecast prices beyond this timeframe.

References

[1] EPEX spot. http://www.epexspot.com/en/market-coupling. (Accessed 15

September 2015).

[2] Belpex (now Epex SPOT Belgium), From Trilateral Market Coupling to CWE

Coupling, October 2008.

[3] TenneT, Market Integration - Coupling of the European Electricity Markets,

December 2010.

[4] K. Van den Bergh, J. Boury, E. Delarue, The flow-based market coupling in central
Western Europe: concepts and definitions, Electr. J. 29 (Issue 1) (2016) 24–29.
[5] ACM, Bundesnetzagentur, CRE, CREG, E-control and ILR. NRA Public Consultation

on Flow Based Market Coupling: Synthesis of Respondent Answers, 2014.

[6] M. Aguado, J. Bourgeois, J. Van Casteren, M. Ceratto, M. Jakel, B. Malfiet,

C. Mestdag, P. Noury, M. Pool, Flow-based Market Coupling in the Central Western
European Region: on the Eve of Implementation, CIGRE, 2012, pp. C5–C204.
[7] D. Waniek, C. Rehtanz, E. Handschin, Flow-based evaluation of congestions in the
electric power transmission system, in: 7th International Conference on the
European Energy Market, 2010, pp. 1–6.

[8] A. Marien, P. Luickx, A. Tirez, D. Woitrin, Importance of design parameters on

flow-based market coupling implementation, in: 10th International Conference on
the European Energy Market, 2013, pp. 1–8.

[9] A. Helseth, Flow-based vs ATC Market Coupling in the Nordic Power Market,

Method and Simulation Results, SINTEF Energy.

[10] ELIA, Implementation of Day-Ahead Flow-Based Market Coupling in the CWE

Region, 13. Mar, 2015.

[11] KU Leven Energy Institute, EI Fact sheet 205-02: cross-border electricity trading:
towards flow-based market coupling, KU Leuven. https://set.kuleuven.be
/ei/factsheet9/at_download/file. (Accessed 17 March 2016).

[12] ETSO, Flow-based Market Coupling, 2004.
[13] H.D.E. Jong, R. Hakvoort, M. Sharma, Effects of Flow-Based Market Coupling for

the CWE Region, 2007.

[14] J.M. Glachant, The Achievement of the EU Electricity Internal Market through

Market Coupling, 2010.

[15] CASC, Publication handbook, CWE market coupling, 17- Apr. 2015, http://utilit

ytool.jao.eu/CWEMC_PublicationHandbook_1.1.pdf. (Accessed 2 December 2016).

[16] J. Arce, Personal Communication, May 2015.
[17] D. Chantelou, Thomson reuters, what have 200 days of flow-based market coupling

taught us?, presentation, 2015. Dec, 2.

EnergyStrategyReviews27(2020)1004447