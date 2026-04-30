Contents lists available at ScienceDirect

Energy Policy

journal homepage: http://www.elsevier.com/locate/enpol

The way towards European electricity intraday auctions – Status quo and
future developments

Fabian Ocker a, b, *, Vincent Jaenisch b
a Brucknerstraße 27, 90429, Nuremberg, Germany
b Karlsruhe Institute of Technology, Kaiserstraße 12, 76131, Karlsruhe, Germany

A R T I C L E  I N F O

A B S T R A C T

Keywords:
Auctions
Electricity market
Intraday trading
Market design

This paper sheds light on the status quo of currently implemented electricity intraday auctions in Europe and
offers an outlook for future developments. First, we compare the two market mechanisms “continuous trading”
and  “auction”  and  identify  advantages  and  disadvantages.  Then,  we  investigate  the  currently  existing  six
intraday auctions in Europe. We compare crucial auction characteristics such as the number of auctions, tradable
market  period(s),  gate  opening  time  and  gate  closure  time,  and  find  a  wide  variety  in  auction  designs.  By
examining  relevant  European  regulation  and  recent  regulatory  decisions,  we  illustrate  that  future  European
intraday auctions can either be implemented as cross-border auctions or complementary regional auctions. We
find that complementary regional auctions of the borders Portugal-Spain, CCR Greece-Italy and CCR Italy-North
are already approved.

1. Introduction

In most European countries the current short-term electricity market
sequence consists of day-ahead and intraday markets, often referred to
as “spot markets” (e.g. Zweifel et al., 2017; EPEX SPOT SE, 2020a). Their
market designs differ in several aspects. For instance, day-ahead markets
are  coupled  across  most  of  Europe  since  several  years  (“Single
Day-ahead Coupling”; e.g. ENTSO-E, 2020), while intraday markets only
recently  underwent  changes  from  a  national  to  a  European  scope.
Furthermore,  there  is  a  difference  with  regard  to  price  formation:
day-ahead markets are commonly organized as auctions, i.e. aggrega-
tion  of  demand  and  supply,  whereas  intraday  markets  are  usually
implemented as continuous trading.1  The latter enables market parties
to  balance  supply  and  demand  changes  in  the  short-term  to  reduce
�
exposure to imbalance penalty (e.g. Chaves-
Avila and Fernandes, 2015;
Soysal  et  al.,  2017;  Ehrenmann  et  al.,  2019).  These  changes  occur
because contracted quantities in the day-ahead timeframe are based on
forecasts, which are prone to error: they depend on different parameters,
most  notably  on  the  intermittent  production  from  volatile  renewable
energy  sources  (henceforth  referred  to  as  “VRES”)  such  as  wind  and
solar power plants. Closer to real-time, forecasts are more accurate and

market  parties  can  adjust  positions  directly  on  a  bilateral  basis  by
continuous trading (Zweifel et al., 2017).

In the light of the growing production share by VRES across Europe,
this  both  national  and  bilateral  manner  of  intraday  trading  may  no
longer  be  sufficient.  Lanfranconi,  Lanza  and  Rossi  (2019)  argue  that
“economic arguments suggest that the current intraday market design at
European  level  (…)  would  benefit  from  improvements”.  Ehrenmann
et al. (2019) state that the very purpose of intraday markets needs to be
re-considered: they will no longer be only (national) adjustment markets
because the moment of exchange is moving closer to real-time. Conse-
quently, intraday trading should be revised and developed in such a way
that the integration of VRES in the system is facilitated by all available
means of market design (e.g. ACER/CEER, 2018). We pick up on these
arguments and discuss two options in more detail: firstly, the coupling of
existing intraday continuous markets in Europe, which enables market
parties to balance their positions also across borders. Secondly, and in
the focus of this paper, the implementation of auctions– on a national
and  European  level  –in  the  intraday  time  frame,  which  provides  an
alternative to bilateral, continuous trading.

The merger of continuous intraday markets to a coupled cross-border
European market was established in June 2018. It is known as the cross-
border  intraday (henceforth  referred  to as  “XBID”) system  (ENTSO-E,

* Corresponding author. Brucknerstraße 27, 90429, Nuremberg, Germany.

E-mail addresses: fabian.ocker@googlemail.com (F. Ocker), vincent.jaenisch@gmail.com (V. Jaenisch).

1  Lanfranconi et al. (2019) argue that the “choice of continuous trading as the European target model for intraday (…) comes from historical reasons” because it

was the applied mechanism in Northern and Central Europe at the time of market integration. Note that further differences are discussed in Section 3.

https://doi.org/10.1016/j.enpol.2020.111731
Received 4 February 2020; Received in revised form 16 May 2020; Accepted 3 July 2020

EnergyPolicy145(2020)111731Availableonline4August20200301-4215/©2020ElsevierLtd.Allrightsreserved.F. Ocker and V. Jaenisch

Abbreviations

ACER
CACM

Agency for the Cooperation of Energy Regulators
Regulation Guideline on Capacity Allocation and
Congestion Management
Capacity Calculation Region

CCR
CRIDA  Complementary Regional Intraday Auction
D
D-1
IDA
NRA
SIDC
TSO
XBID
VRES

Day of delivery
Day before delivery (day-ahead)
Intraday Auction
National Regulatory Authority
Single Intraday Coupling
Transmission System Operator
Cross-border Intraday Trading
Volatile Renewable Energy Sources

2018; Amprion, 2020). The XBID system initially involved 14 countries
and represents the IT implementation of the “single intraday coupling”
(henceforth  referred  to  as  “SIDC”)  for  continuous  trading,  which  was
recently  promoted  by  European  guidelines  and  network  codes  (Euro-
pean Commission, 2015, 2019).2 The XBID system unites the continuous
intraday  markets  and  complements  the  already  coupled  day-ahead
markets.  In  November  2019, the  XBID  system  was  enlarged  by  seven
countries: now the total number of coupled countries is 21 (SIDC, 2019;
HUPX,  2019).3  This  recent  enlargement  illustrates  that  continuous
intraday trading was until now in focus of European policy makers.

The  second  option,  the  introduction  of  auctions  in  the  intraday
timeframe, has caught far less attention of policy makers until now (e.g.
Bellenbaum et al., 2014; Lanfranconi et al., 2019). Only some European
countries  apply  intraday  auctions  (henceforth  referred  to  as  “IDAs”)
instead  of  or  as  a  complement  to  continuous  trading  such  as,  for
instance, Italy, Spain and Portugal do since the early 2000s (e.g. GME,
�
2003; Furi�o, 2011; Chaves-
Avila and Fernandes, 2015). Nonetheless, the
European guideline on capacity allocation and congestion management
(henceforth referred to as “CACM Regulation”) and recent decisions by
the  Agency  for  the  Cooperation  of  Energy  Regulators  (henceforth
referred to as “ACER”) present general framework conditions for future
European IDAs (European Commission, 2015; ACER, 2017, 2019a). The
overarching objective is to complement the SIDC for continuous trading
(ACER refers to this as “auction SIDC”).

The aim of this paper is to present the status quo of IDAs in Europe, to
address recent regulatory stipulations and to give an outlook for future
developments.  Our  approach  can  be  divided  in  three  parts.  First,  in
Section 3, the theoretical background is presented: we discuss the dif-
ferences  between  the  two  market  mechanisms  regarding  liquidity,
market  power  resilience,  information  efficiency,  static  allocation  effi-
ciency and the efficient usage of cross-zonal capacity, and advantages
and  disadvantages  are  concluded.  Second,  we  carry  out  an  empirical
analysis of existing IDAs in Europe in Section 4. We consider relevant
characteristics to compare the auctions, such as the number of auctions,
tradable market period(s), gate opening time and gate closure time, and
show that there exists a wide variety in currently implemented auction
designs.  Third,  we  illustrate  and  discuss  the  regulatory  framework
conditions for future European IDAs in Section 5. We present that future
European  IDAs can either be implemented  as cross-border  IDAs or as

complementary  regional  IDAs.  Furthermore,  we  refer  to  recent  appli-
cations of these stipulations in Southern European countries: the com-
plementary  regional  IDAs  at  the  borders  Portugal-Spain,  Greece-Italy
and Northern Italy are already approved.

The remainder of this paper is structured as follows: Section 2 pre-
sents related literature and background information, and Section 3 dis-
cusses the theoretical background. In Section 4, we present our analysis
of  the  currently  existing  European  IDAs,  and  Section  5  illustrates  the
regulatory conditions for future European IDAs. Section 6 concludes and
draws policy implications.

2. Background and literature review

This literature review focuses on IDAs and presents background in-
formation regarding the current state of discussion.4  Despite the only
occasional implementation of IDAs in Europe, there are many scientific
papers and documents around this topic.5

Regarding Southern European IDAs, being operational already for a
long  time,  Furi�o  (2011)  presents  an  econometrical  analysis  of  the
Spanish IDA from 2000 to 2010, focusing on prices and the evolution of
the registered electricity traded. It is shown that a growing interest in
intraday  trading  exists,  particularly  in  the  last-time-negotiated  hours.
�
Chaves-
Avila  and  Fernandes  (2015)  analyze  the  participation  of
renewable  generators  in  the  Spanish  intraday  market.  They  explore
different  market  rules  in  the  Spanish  market  that  incentive  market
parties to participate and find that the market design has contributed to
renewable generation balancing. Lanfranconi, Lanza and Rossi (2019)
present a recent analysis of IDAs across bidding zones in Italy and be-
tween  Italy  and  Slovenia.  By  providing  an  empirical  analysis,  they
suggest  to  re-consider  the  role  of  IDAs  because  they  allow  for  more
efficient use of cross-zonal capacity.

With respect to the German IDAs, being operational since the end of
2014,  Weber  (2010)  investigates  the  major  European  power  markets
France, Germany, Scandinavia, Spain and UK with a particular focus on
liquidity. One proposal for improving liquidity in the German market is
the introduction of IDAs. Neuhoff et al. (2016a) investigate the question
whether  adding  auctions  to  the  continuous  intraday  trading  is
improving  market  performance.  They  assess  this  by  referring  to  the
experience with the implementation of the German IDA, with a focus on
trading volumes,  prices  and  market  depth.  Ocker  and  Ehrhart  (2017)
link  the  declining  demand  for  balancing  power  in  Germany  to  the
introduction of the German IDA. Braun and Brunner (2018) study the
quarter-hourly IDA in the German market and find a distinctive zigzag
price formation, which they explain by two factors: “first, the solar re-
sidual that combines the trading of solar power ramps around midday as
well as the gradients of consumption and thermal power plant ramps
throughout the course of the day, and second, a characteristic two stage
market  design  with  higher  liquidity  for  the  hourly  than  for  the
quarter-hourly auction.”

Regarding theoretical analyses and market design questions, Henriot
(2012)  examines  the  benefits  for  wind  power  producers  to  trade  in
intraday markets. It is argued that in some cases it may be inefficient to
implement  IDAs:  market  participants  adjust  their  strategies  to  the
inflexible points of trading, which may lead to additional costs and lost
trading opportunities. Bellenbaum et al. (2014) discuss various options
to use and price intraday cross-zonal capacity in the context of the re-
quirements  of  the  European  target  model  and  the  network  codes.

2  The 14 countries are Austria, Belgium, Denmark, Estonia, Finland, France,
Germany,  Latvia,  Lithonia,  Norway,  Portugal,  Spain,  Sweden  and  the
Netherlands.

3  The  so-called  “second  wave  go-live”  in  XBID  includes  Bulgaria,  Croatia,
Czech  Republic,  Hungary,  Poland,  Romania  and  Slovenia.  A  “third  wave  go-
live” is planned at the end of 2020 with Italy and Greece (HUPX, 2019).

4  Literature  on  continuous  trading  can  be  found  in  Diamantopoulous  et  al.
(2012);  Hagemann  and  Weber  (2013);  Skajaa  et  al.  (2015);  Just  and  Weber
(2015); Scharff and Amelin (2016); Kiesel and Paraschiv (2017); Soysal et al.
(2017);  Martin  and  Otterson  (2018);  M€arkle-Huß  et  al.  (2018);  Maciejowska
et al. (2019) or Shinde and Amelin (2019).

5  Further literature can be found in Bellenbaum et al. (2014) or Lanfranconi

et al. (2019).

EnergyPolicy145(2020)1117312F. Ocker and V. Jaenisch

Neuhoff et al. (2015) discuss the use of IDAs within and between Eu-
ropean  member  states.  They  conclude  that  IDAs  could  present  “an
important step to enhance efficiency thus reducing cost of operation of
European power systems, to accommodate increasing shares of wind and
solar  energy,  and  to  enhance  security  of  system  operation.”  In  an
extensive study by IRENA (2017), continuous trading is contrasted with
IDAs in various aspects and a possible co-existent market design is dis-
cussed. Ehrenmann et al. (2019) argue that European IDAs will become
indispensable in the light of the rising share of electricity production by
VRES. They further argue that auction may foster the participation of
new and smaller market participants. It is recommended to introduce
several cross-zonal IDAs, such as an opening auction, an evening auction
and additional auctions in between.

3.3. Market power resilience

Mas-Colell, Whinston and Green (1995) define market power as “(…)
the ability to alter profitably prices away from competitive levels”. This
means that, in contrary to competitive markets, not all consumers and
producers act as price takers, i.e. the demand and supply are not infi-
nitely elastic at going market prices. Bellenbaum et al. (2014) argue that
continuous trading is of advantage for larger firms because they have a
“better return on information costs and thus creates barriers to entry”.
They conclude that all investigated continuous trading options are more
prone to market power than auction solutions. IRENA (2017) argues that
this advantage for auctions only holds as long as sufficient liquidity can
be guaranteed.

3. Theoretical background

3.4. Information efficiency

Any market-based solution shall reach the overarching political goal
of welfare maximization (e.g. European Commission, 2015, 2016, 2017,
2019). In literature, several criteria exist to evaluate this aim.6 We focus
on the most prominent ones: liquidity, market power resilience, infor-
mation  efficiency,  static  allocation  efficiency  and  efficient  usage  of
cross-zonal capacity. We conclude this section with an overview of ad-
vantages and disadvantages.

3.1. Continuous trading and auction mechanism

In both mechanisms market parties submit ask and offer bids to the
auction  office,  which  are  published  in  a  central  order  book  (Zweifel
et  al.,  2017).  The  principle  of  continuous  trading  builds  upon  an
instantaneous  matching  of  suitable  bids  until  gate  closure,  while  the
auction principle aggregates, sorts and clears the entire market at once
after  gate  closure  (Henriot,  2012).7  For  auctions,  the  price  rule  can
either  be  uniform  pricing  (pay-as-cleared),  i.e.  all  awarded  market
parties pay/receive the same price, or pay-as-bid pricing, i.e. all awar-
ded parties pay/receive their individual bids. For continuous trading it is
limited to pay-as-bid pricing (Neuhoff et al., 2015). Note that there are
both  national  (Braun,  2018)  and  international  continuous  intraday
markets (e.g. the XBID system presented in the Introduction).

3.2. Liquidity

ACER/CEER (2018) define market liquidity as “a key indicator of a
well-functioning electricity market” that can be defined as “the feature
of the electricity market whereby a large number of market participants
are able to sell/buy products quickly, without significantly affecting the
product’s  price  and  without  incurring  significant  transaction  costs”.
Bellenbaum et al. (2014) state that a high liquidity is advantageous for
the overall efficiency because it means a high number of market par-
ticipants and high trading volumes. From a general viewpoint, IRENA
(2017) argues that auctions present the advantage of higher  liquidity
because  they  concentrate  transactions  since  the  last  trading  session.8
Lanfranconi et al. (2019) point to an analysis of intraday traded volumes
per product and per bidding zone for the largest European markets in
2017, which supports this reasoning: four of six bidding zone borders
with the highest intraday trading volumes implemented IDAs.

Bellenbaum et al. (2014) describe information efficiency as follows:
“[the]  arrival  of  new  information  is  instantaneously  translated  into
market adjustments”. This means that, for instance, a change in wind
forecast is immediately reflected into price signals. This is enabled by
continuous  trading  because  any  new  information  can  be  processed
directly into a new trade (IRENA, 2017). On the contrary, auctions are
conducted  only  at  certain  points  in  time:  information  can  only  be
translated into price signals with a delay that is given by the timespan
between  the  arrival  of  the  new  information  and  the  time  of  auction
clearing.9  Lanfranconi  et  al.  (2019)  summarize  it  as  follows:  “(…)  in
order to grant efficient allocation (…) auctions are in principle needed
each time a change in scarcity occurs.”

3.5. Static allocation efficiency

The auction principle entails bid aggregation in a specific order prior
to allocation. This ensures that the most suitable market participants are
selected  at  that  point  of  time:  the  bids  of  producers  are  sorted  in  an
increasing order, i.e. the producers with the lowest willingness to sell are
allocated  first,  and  the  bids  of  consumers  are  sorted  in  a  decreasing
order, i.e. the consumers with the highest willingness to pay are allo-
cated first (Ehrenmann et al., 2019).

Continuous trading does not aggregate bids prior to allocation but
follows  the  principle  of  “first-come,  first-served”  (IRENA, 2017).  This
feature  cannot  ensure  that  the  most  suitable  market  participants  are
matched  because  not  all  bid  information  are  available  at  the  time  of
allocation. For instance, this can lead to the situation that the consumer
with the highest willingness to pay is not allocated to the producer with
the lowest willingness to sell (instead to a producer with a sufficiently
low  willingness  to  sell)  because  of  different  bid  submission  times
(Henriot, 2012).

An  example  of  this  reasoning  is  depicted  in  Fig.  1,  inspired  by
Ehrenmann  et  al.  (2019).  The  graphs  illustrate  the  intraday  market
mechanism IDA on the left, and continuous trading on the right, where
the ordinate denotes the price and the abscissa denotes the quantity.10
The bids are given by the bars and they are the same in both graphs, i.e.
six ask bids (colored grey) and seven offer bids (colored white).11 In the
case of IDAs, the bids of producers are sorted in an increasing order and
bids of consumers in a decreasing order. The matching of these ordered
bids is carried out as long as the willingness to pay is greater than the
willingness  to  sell.  In  the  example  this  holds  for  the  first  three  bids
leading to an allocated quantity in the auction of qA and a uniform price

6  Comprehensive overviews are given in Bellenbaum et al. (2014), Neuhoff,

9  Note  that  the  information  efficiency  can  be  enlarged  by  the  frequency  of

Richstein and May (2016b), Lanfranconi et al. (2019).

7  Ehrenemann et al. (2019) refer to this difference as “competition on speed

rather than on costs”.

8  Note that it is acknowledged that a high number of auctions may negatively

affect the liquidity.

auctions, see for example IRENA (2017) or Lanfranconi et al. (2019).
10  Note that for continuous trading the abscissa can also be interpreted as a
timeline, representing the temporal order of bid submission.
11 For the sake of readability we assume the same quantity of all bids (hori-
zontal expansion).

EnergyPolicy145(2020)1117313F. Ocker and V. Jaenisch

Fig. 1. Allocation example for IDAs and continuous trading.

of pA (set by the highest rejected ask bid in our example). The resulting
welfare is the sum of the blue framed areas: the consumers’ surplus is the
sum of the areas below pA, and the producers’ surplus is the sum of the
areas above pA.

When applying continuous trading, the bids of consumers and pro-
ducers are not ordered prior to allocation but matched instantaneously
in the order of bid submission as long as the willingness to pay is greater
than the willingness to sell. In the example this leads to six allocations
with  a  total  quantity  of  qC.  Since  pay-as-bid  is  applied,  the  resulting
prices are different, ranging from pC,1 to pC,6.12 The resulting welfare is
the sum of the green framed areas, which, in this example, is smaller
than the welfare of the IDA. Please note that this example depicts an
extreme case because the trading principle of the XBID system is first-
come first-served, i.e. the highest ask bid and the lowest offer bid get
served first. Therefore, our example illustrates a rare case of bid sub-
mission timings in which the margins between ask and offer bids are
small. This means that higher welfare solutions for continuous trading
are possible.

3.6. Efficient usage of cross-zonal capacity

Lanfranconi et al. (2019) state: “the value of cross-zonal capacity can
change from day-ahead to real-time according to updated information
available  to  market  participants  and  their  willingness  to  pay.”  This
means that the scarcity of cross-zonal capacity is time-dependent. Im-
plicit  continuous  trading  is  unable  to  reflect  these  market  dynamics
efficiently because capacity is allocated for free as long as capacity is
available (IRENA, 2017).13  Consequently, the collection of congestion
rents, i.e. the cross-zonal price difference times the allocated volumes, is
not possible. In contrast, cross-zonal auctions correctly reflect network

12  Pay-as-bid pricing incentivizes consumers and producers to shade their bids
(i.e. consumers include a mark-down to their willingness to pay and producers
include a mark-up their willingness to sell) in order to generate a profit in the
case  of  allocation  (e.g.  Krishna,  2002).  In  the  example  this  is  considered  by
setting the resulting price in between the respective pair of willingness to pay
and willingness to sell. Further note that the strictly declining order of prices is
due to the example and cannot be assumed in general.
13  Implicit means that transport capacity and electricity is traded in one step.
This  is commonly referred  to as market coupling; for further information see
APG (2020).

Table 1
Evaluation of market mechanisms (see also Bellenbaum et al., 2014).

Continuous trading

Auction

Liquidity
Market power resilience
Information efficiency
Static allocation efficiency
Efficient usage of cross-zonal capacity

–
–
þþ
–
–

þþ
þ
–
þ
þþ

congestions because the bids are aggregated and cleared at one point in
time.  Lanfranconi,  Lanza  and  Rossi  (2019)  conclude  that  an  efficient
allocation  in  a  dynamic  context  can  be  guaranteed  best  by  a  high
number of cross-zonal IDAs.

3.7. Summary: advantages and disadvantages

The following table summarizes the advantages and disadvantages
associated with the two market mechanisms. The notation is inspired by
Bellenbaum et al. (2014) and as follows: “þ” (or “þþ”) denotes that the
criterion is (largely) met, “0”  expresses neutrality and “-”  (or “–”) de-
notes a (largely) negative impact.

Table 1 illustrates the essential and unique advantage of continuous
trading compared to the auction principle: information efficiency, i.e.
enabling market parties to correct their position(s) in the market as soon
as a change in their availability occurs. This possibility of instantaneous
correction is associated with lower costs for the market parties and for
the system, which in return is crucial for the efficiency of the market (e.
g. IRENA, 2017; ACER/CEER, 2018). In conjunction with the generally
viewed  purpose  of  the  intraday  market  until  now  (i.e.  serving  as  an
adjustment possibility), it is plausible why continuous trading is applied
in most intraday markets in Europe at present.

4. Status quo in Europe: Empirical analysis

In this section we present the currently existing six IDAs in Europe.
The structure of the analysis is presented in Table 2, while the market
areas,  their  acronyms  and  the  corresponding  geographical  scope  are

EnergyPolicy145(2020)1117314F. Ocker and V. Jaenisch

Table 2
Examined auction characteristics.

5. The way towards European IDAs

Number of auctions

It states how many auctions are carried out.

Tradable market

period(s)

Market time unit

Gate opening time

Gate closure time

Publication of

results

It states which market periods can be traded, e.g. the hours
between 00:00 until 24:00 of delivery day D.
It states the granularity of the tradable market period(s), e.
g. 15 min or 30 min.
It states the time when the order book opens (also referred
to as “opening of the order book”).
It states the time when the order book closes (also referred
to as “closing of the order book”).
It states when market results are published.

Admissible price

It states the price limits for bids.

interval

Bid price granularity

Bid quantity
granularity

Price rule

It states the granularity of bid prices, e.g. 0.1 Euro/MWh
(also referred to as “price increment”).
It states the granularity of bid quantities, e.g. 0.1 MWh
(also referred to as “volume increment”).
It states whether pay-as-bid pricing or uniform pricing is
applied.

Table 3
Overview  of  currently  existing  European  IDAs;  sources:  see  Table  A1  in  the
Annex.

Market area

Germany (DE)
Great Britain (GB)
Iberian Peninsula (IP)
Ireland (IR)
Italy (IT)
Switzerland (CH)

Geographical scope

Germany, Luxembourg
England, Scotland, Wales
Portugal, Spain
Northern Ireland, Irish Republic
Italya
Switzerland

a Note that since June 2016 two of the seven IDAs are extended to the Italian-
Slovenian border as part of a pilot project for implicit IDAs (e.g. Lanfranconi
et al., 2019).

listed in Table 3.

Note that in the Annex (Table A1) the auction characteristics of the
six market areas are presented in detail; we describe them briefly in the
following.14  Furthermore,  Fig.  2  depicts  information  regarding  the
timings  of  the  IDAs,  i.e.  for  each  auction  the  timespan  between  gate
opening and closure as well as the tradable market period(s).15

The number of auctions ranges from one (DE) to seven (IT). The gate
opening time varies between 45 days prior to delivery in DE to several
hours prior in IT and IP. The gate closure time ranges from 03:00 pm
day-ahead (e.g. DE or IT) to 05:00 pm on the delivery day in IR. The
tradable market period(s) relate to the number of auctions as well as the
gate closure times. For instance, in GB with two IDAs, there exist two
different tradable market periods: for the first IDA with a gate closure at
06:30 pm day-ahead it includes the hours 00:00 until 24:00, whereas for
the second IDA with a gate closure at 09:00 am it includes solely the
hours  12:00  until  24:00.  The  publication  of  results  is  close  to  gate
closure in all six market areas. The market time unit ranges from 60 min
in IP, IT and CH, 30 min in GB and IR to 15 min in DE. Regarding the
admissible price interval, DE has the highest limits with (cid:0) 3,000 Euro/
MWh to þ3,000 Euro/MWh, while in the market area IT it is þ0 Euro/
MWh  to  þ3,000  Euro/MWh.  The  bid  price  granularity  is  either  0.1
Euro/MWh (DE, GB and CH) or 0.01 Euro/MWh (IP and IR), and the bid
quantity granularity is 0.1 MWh in all five market areas for which in-
formation is available. Finally, all six market areas apply uniform pric-
ing as price rule.

There are two options for future European IDAs: cross-border IDAs
and complementary regional IDAs. The legal stipulations for these two
IDA types are presented in the following. Furthermore, we present IDAs
that were recently approved under this new regulation.

5.1. Cross-border IDAs

On  24.01.2019  ACER  published  its  decision  “establishing  a  single
methodology  for  pricing  intraday  cross-zonal  capacity”  required  by
Article 55 of the CACM Regulation (ACER, 2019a).16 The methodology
establishes  a  pricing  mechanism  for  cross-border  capacity  in  the
intraday  timeframe,  including  essential  market  design  parameters  for
cross-border implicit European IDAs. These auction characteristics are
presented in the following.

The methodology states that the pricing mechanism for cross-zonal
capacity in the intraday timeframe shall be based on IDAs. These im-
plicit auctions shall complement the already existing continuous SIDC. It
is stated that cross-zonal capacity shall not be allocated to an IDA and
continuous trading at the same time: trading for the continuous SIDC
must be suspended temporarily. In line with the continuous SIDC, the
TSOs responsible for a specific bidding zone border provide the available
cross-zonal capacity as an input for the IDAs.

It is decided that one IDA shall be established on 03:00 pm D-1 (for
all hours of the delivery day D), one IDA on 10:00 pm D-1 (for all hours
of the delivery day D), and one IDA on 10:00 am on the delivery day (for
the remaining hours of the delivery day D starting from 12:00 am). In
addition,  it  is  stipulated  that  the  price  rule  shall  be  uniform  pricing.
Regarding price thresholds, the methodology refers to an ACER decision
dated 14.11.2017 (ACER, 2017). In this decision and the corresponding
methodology “harmonized maximum and minimum clearing prices for
single intraday coupling” the maximum clearing price for SIDC is set to
þ9,999 EUR/MWh, and the minimum clearing price for SIDC is set to
(cid:0) 9,999 EUR/MWh. The auction characteristics market time unit, gate
opening  time,  publication  of  results,  bid  price  granularity  and  bid
quantity granularity are not specified.

Regarding implementation of cross-border IDAs, it is stated that the
methodology shall “be implemented by amending and complementing
the  relevant  requirements  and  methodologies  related  to  the  develop-
ment of the SIDC” (ACER, 2019a). Thus, it does not state an exact date in
the future. Table 4 summarizes these auction characteristics.

5.2. Complementary regional IDAs

Pursuant to Article 63 of the CACM Regulation, the relevant nomi-
nated electricity market operators (i.e. power exchanges such as EPEX or
NordPool)  and  TSOs  on  bidding  zone  borders  may  jointly  develop  a
methodology  proposal  for  the  design  and  implementation  of  comple-
mentary regional IDAs (henceforth referred to as “CRIDAs”) and submit
it to the concerned national regulatory authorities (henceforth referred
to as “NRAs”) for approval (European Commission, 2015). The proposals
had to be submitted no later than 18 months after the entry into force of
the CACM Regulation (dated 24.07.2015), i.e. until 24.01.2017. They
may be implemented within or between bidding zones in addition to the
continuous SIDC. As for cross-border IDAs, continuous trading within
and between the relevant bidding zones may be stopped for a limited
period of time in order to conduct the auctions. The respective NRAs can
approve  such  a  proposal  for  CRIDAs  if  certain  conditions  are  met,
amongst  others:  the  CRIDAs  may  not  have  an  adverse  impact  on  the
liquidity of the SIDC, they shall not introduce any undue discrimination

14  Given the extent of the table, we decided to include Table A1 in the Annex
and not in the main text. Note that for easier reading we use in the following
description the acronyms of the market areas.
15  Note that for the sake readability all gate opening times and gate closure
times were harmonized to the Continental European Time.

16  Note that it is not in the scope of this paper to discuss the proposed solution
(“hybrid model”). For further details please refer to Bellenbaum et al. (2014),
ENTSO-E, 2017, IRENA, 2017 or Lanfranconi et al. (2019).

EnergyPolicy145(2020)1117315F. Ocker and V. Jaenisch

Fig. 2. Graphical presentation of IDA timings.

Table 4
Auction characteristics for cross-border IDAs according to ACER (2017, 2019a).

Number of auctions

3

Table 5
Auction characteristics of CRIDAs in the CCR Greece-Italy and CCR Italy-North
(CRIDA Approval GR-IT, 2019; CRIDA Approval IT-North, 2019).

Tradable market period(s)

Market time unit
Gate opening time
Gate closure time

Publication of results
Admissible price thresholds
Bid price granularity
Bid quantity granularity
Price rule

00:00–24:00;
00:00–24:00;
12:00–24:00
to be specified
to be specified
03:00 pm (D-1);
10:00 pm (D-1);
10:00 am (D)
to be specified
(cid:0) 9,999 Euro/MWh/þ9,999 Euro/MWh
to be specified
to be specified
uniform pricing

between market participants from adjacent regions and the timetables
for CRIDAs shall be consistent with SIDC to enable market participants
to trade as close as possible to real-time. In order to ensure that these
conditions  are  met  also  with  proceedings  SIDC  developments,  the
respective NRAs shall review the compatibility of CRIDAs with the SIDC
at least every two years after implementation.17

5.3. Approved CRIDAs

According to ACER’s “monitoring report on the implementation of
the  CACM  Regulation  and  the  FCA  Regulation”,  three  proposals  for
CRIDAs were submitted and approved: one at the border of Portugal and
Spain (approved on 13.04.2018), one by the capacity calculation region
(henceforth  referred  to  as  “CCR”)  “Greece-Italy”  (approved  on
07.05.2019)  and  one  by  the  CCR  “Italy-North”  (approved  on
04.06.2019) (ACER,  2019b, 2020).18  The Portuguese-Spanish  CRIDAs
are run already since the go-live of the XBID system in 2018 (CRIDA
Approval ES-PT, 2018). We included their description in Section 4 by
referring  to  this  border  as  market  area  Iberian  Peninsula.  The

17  Note  that  the  methodology  for  pricing  intraday  cross-zonal  capacity  (as
presented  in  Section  5.1)  does  not  apply  for  CRIDAs  (European  Commission,
2015).
18  The  rationales  behind  the  CRIDA  implementations  at  these  borders  are
described  in  the  respective  proposals  and  approvals  (CRIDA  Approval  ES-PT,
2018; CRIDA Approval GR-IT, 2019; CRIDA Approval IT-North, 2019).

Number of auctions
Tradable market period(s)

Market time unit
Gate opening time

Gate closure time

Publication of results

Admissible price thresholds
Bid price granularity
Bid quantity granularity
Price rule

CCR Greece-Italy and CCR Italy-North

3
00:00–24:00;
00:00–24:00;
12:00–24:00
60 min.
01:00 pm (D-1);
03:30 pm (D-1);
10:30 pm (D-1)
03:00 pm (D-1);
10:00 pm (D-1);
10:00 am (D)
03:30 pm (D-1);
10:30 pm (D-1);
10:30 am (D)
(cid:0) 9,999 Euro/MWh/þ9,999 Euro/MWh
0.1 Euro/MWh
0.1 MWh
uniform pricing

characteristics  of  the  CRIDAs  for  the  CCR  Greece-Italy  and  CCR
Italy-North  are  identical,  see  Table  5  (CRIDA  Approval  GR-IT,  2019;
CRIDA  Approval  IT-North,  2019).19  In  contrast  to  the  implemented
CRIDAs in the market area Iberian Peninsula, they are already aligned
with the stipulations made by ACER regarding cross-border IDAs (see
sections 4 and 5.1 for comparison). The implementation is foreseen as
soon as both countries join the continuous SIDC end of 2020 (HUPX,
2019).

For Italy this would result in up to three different IDAs available for
trading: the existing IDAs (Section 4), CRIDAs with the implementation
of  the  continuous  SIDC  and  cross-border  IDAs  with  the  methodology
implementation  for  pricing  intraday  cross-zonal  capacity.  Regarding
such a variety, ACER (2019b) suggests in its Monitoring Report of the
CACM  Regulation  that  CRIDAs  should  gradually  be  replaced  by  the
methodology  for  pricing  intraday  cross-zonal  capacity:  “the  need  for
additional CRIDAs might not be substantiated anymore”. On the con-
trary, it could be beneficial if the concepts of CRIDAs and cross-border
IDAs  “are  merged  into  a  single  methodology  for  pricing  of  intraday
cross-zonal capacity, which should ideally be harmonized across the EU”

19  The  reason  for  this  is  that  initially  there  was  only  one  proposal  for  both
CCRs  submitted  to  the  relevant  NRAs.  In  the  course  of  the  approval  process,
they had to be split up and submitted separately (ACER, 2020).

EnergyPolicy145(2020)1117316F. Ocker and V. Jaenisch

to avoid “the risk of too fragmented intraday markets in terms of tim-
ings, design and geography” (ACER, 2019b). In fact, the CRIDA meth-
odologies of CCR Greece-Italy and Italy-North exclude the possibility of
having three  different types of  IDAs at the  same time:  as soon  as the
methodology for pricing intraday cross-zonal capacity is implemented,
the  CRIDAs  shall  be  replaced  by  cross-border  IDAs  (CRIDA  Approval
GR-IT, 2019; CRIDA Approval IT-North, 2019). Against the background
that the CRIDAs of the CCRs Greece-Italy and Italy-North are already in
line with the stipulations for cross-border IDAs, no major problems in
the transition should arise.

6. Conclusions and policy implications

In  the  last  section we  summarize  the  results,  discuss  policy  impli-

cations and point to future fields of research.

6.1. Summary of results

This paper examined the status quo of intraday auctions in Europe
and presented an outlook for future European intraday auctions. This
paper  analyzed  existing  national  intraday  auctions,  the  future  pan-
European cross-border intraday auctions and planned (or partly imple-
mented) complementary regional intraday auctions. We compared the
two market mechanisms continuous trading and auction and discussed
major  advantages  and  disadvantages.  We  presented  the  existing  six
European intraday auctions and compared crucial auction characteris-
tics.  A  wide  variety  in  auction  designs  was  found.  We  outlined  two
recent decisions by the Agency for the Cooperation of Energy Regulators
that provide the framework conditions for future cross-border intraday
auctions  as  well  as  the  relevant  Article  of  the  Guideline  on  Capacity
Allocation  and  Congestion  Management  for  the  implementation  com-
plementary  regional  intraday  auctions.  Furthermore,  it  was  discussed
that  the  complementary  regional  intraday  auctions  of  the  border
Portugal-Spain  and  the  capacity  calculations  regions  Greece-Italy and
Italy-North are already approved.

6.2. Policy implications

It  remains  open  whether  the  five  intraday  auctions  described  in
Section  4  and  the  complementary  regional  intraday  auctions  in  the
market area Iberian Peninsula persist. For the former, no proposals to
implement  them  as  complementary  regional  intraday  auctions  were
submitted to the relevant national regulatory authorities. Furthermore,
and this also holds for the latter, several auction characteristics are not
in  accordance  with  the  Agency  for  the  Cooperation  of  Energy

Regulators’  legal stipulations for cross-border intraday auctions. Most
notably, this includes the number of auctions and the associated trad-
able market period(s), gate opening and gate closure times (see Fig. 2).
Assuming  that  the  existing  intraday  auctions  persist,  the  smallest
adjustment  effort  should  arise  for  the  market  area  Ireland  with  three
intraday auctions because mostly timings need to be changed. For the
other  existing  intraday  auctions,  the  implementation  of  cross-border
intraday  auctions  will  require  adaptations.  In  particular,  it  poses  the
question  if  and  how  to  harmonize  these  auctions  with  respect  to
economical (e.g. market fragmentation), legal (e.g. future harmonized
European legislation as indicated by the Agency for the Cooperation of
Energy Regulators) and political (e.g. Great Britain leaving the European
Union)  developments.  For  the  market  area  Germany,  for  instance,  it
needs to be clarified whether the current national intraday auctions is
still needed when three cross-border intraday auctions are introduced,
while  for  the  market  area  Iberian  Peninsula  a  decision  is  required
whether only the three cross-border intraday auctions are sufficient or if
the  sum  of  six  intraday  auctions  should  persist  in  the  future  (i.e.
retaining three complementary regional intraday auctions).

6.3. Directions for further research

Future  research  should  investigate  the  co-existence  of  multiple
intraday auction concepts (on a per country basis, bidding-zone border
basis or capacity calculation region basis) more thoroughly. Our paper
only set the starting point for such an examination by illustrating the
status quo and the legal stipulations. The focus could be placed on effects
regarding market liquidity (e.g. in continuous intraday trading, intraday
auctions,  complementary  regional  intraday  auctions,  cross-border
intraday  auctions  and  balancing  energy  market),  bidding  strategies
across  different  trading  options  and  implications  regarding  the
remaining time for continuous trading.

CRediT authorship contribution statement

Fabian Ocker: Conceptualization, Methodology, Investigation, Re-
sources, Writing - original draft, Writing - review & editing, Visualiza-
tion,  Supervision,  Project  administration.  Vincent  Jaenisch:
Methodology, Investigation, Visualization.

Declaration of competing interest

The authors declare that they have no known competing financial
interests or personal relationships that could have appeared to influence
the work reported in this paper.

Annex.

Table A.1
Comparison  of  auction  characteristics  in  the  six  market  areas;  sources:  Germany:  EPEX  SPOT  SE  (2019,  2020b);  Great  Britain:  SEMOpx  (2017,  2020);  Iberian
�
Peninsula: Chaves-
Avila and Fernandes (2015) and OMIE (2018); Ireland: SEMOpx (2017, 2020); Italy: Oggioni and Lanfranconi (2015) and GME (2003, 2017, 2020);
Switzerland: EPEX SPOT SE (2019).

Germany

Great Britain

Iberian Peninsula

Ireland

1

2

6

3

Number of
auctions

Tradable market

00:00–24:00

period(s)

00:00–24:00;
12:00–24:00

00:00–24:00;
12:00–24:00;
18:00–24:00

21:00 (D-1) -
24:00 (D);
00:00–24:00;
04:00–24:00;
07:00–24:00;
11:00–24:00;
15:00–24:00

Switzerland

2

00:00–24:00;
16:00–24:00

Italy

7

00:00–24:00;
00:00–24:00;
04:00–24:00;
08:00–24:00;
12:00–24:00;
16:00–24:00;
20:00–24:00

(continued on next page)

EnergyPolicy145(2020)1117317F. Ocker and V. Jaenisch

Table A.1 (continued )

Germany

Great Britain

Iberian Peninsula

Ireland

1

2

6

3

Italy

7

Switzerland

2

Number of
auctions

Market time unit

15 min.

30 min.

60 min.

30 min.

60 min.

60 min.

Gate opening time

45 days prior to delivery

14 days prior to delivery

Gate closure time

03:00 pm (D-1)

06:30 pm (D-1);
09:00 am (D)

Publication of

03:10 pm (D-1)

results

09:10 pm (D-1);
09:40 am (D)

05:00 pm (D-1);
09:00 pm (D-1);
01:00 am (D);
04:00 am (D);
08:00 am (D);
12:00 am (D)

06:40 pm (D-1);
09:40 pm (D-1);
01:40 am (D);
04:40 am (D);
08:40 am (D);
12:40 am (D)

06:45 pm (D-1);
09:45 pm (D-1);
01:45 am (D);
04:45 am (D);
08:45 am (D);
12:45 am (D)

19 days prior to delivery

06:30 pm (D-1);
09:00 am (D);
05:00 pm (D)

07:10 pm (D-1);
09:40 am (D);
03:15 pm (D)

00:55 pm (D-1);
00:55 pm (D-1);
05:30 pm (D-1);
05:30 pm (D-1);
05:30 pm (D-1);
05:30 pm (D-1);
05:30 pm (D-1)

03:00 pm (D-1);
04:30 pm (D-1);
11:45 pm (D-1)
03:45 am (D);
07:45 am (D);
11:15 am (D);
03:45 pm (D)

03:30 pm (D-1);
05:00 pm (D-1);
00:15 am (D);
04:15 am (D);
08:15 am (D);
11:45 am (D);
04:15 pm (D)

14 days prior to delivery

04:30 pm (D-1);
11:15 am (D)

04:45 pm (D-1);
11:30 am (D)

Admissible price

interval

(cid:0) 3,000 Euro/MWh/
þ3,000 Euro/MWh

(cid:0) 150 Euro/MWh/
þ1,500 Euro/MWh

n/a

(cid:0) 150 Euro/MWh/
þ1,500 Euro/MWh

þ0 Euro/MWh/
þ3,000 Euro/MWh

(cid:0) 500 Euro/MWh/
þ3,000 Euro/MWh

Bid price

granularity

Bid quantity
granularity

0.1 Euro/MWh

0.1 Euro/MWh

0.01 Euro/MWh

0.01 Euro/MWh

0.1 MWh

0.1 MWh

0.1 MWh

0.1 MWh

n/a

n/a

0.1 Euro/MWh

0.1 MWh

Price rule

uniform pricing

References

ACER – Agency for the Cooperation of Energy Regulators, 2017. Decision of the Agency
for the Cooperation of Energy Regulators of 14 November 2017 on the Nominated
Electricity Market Operators’ Proposal for Harmonized Maximum and Minimum
Clearing Prices for Single Intraday Coupling.

ACER – Agency for the Cooperation of Energy Regulators, 2019a. Decision No 01/2019

of the Agency for the Cooperation of Energy Regulators of 24 January 2019
Establishing a Single Methodology for Pricing Intraday Cross-Zonal Capacity.
ACER – Agency for the Cooperation of Energy Regulators, 2019b. Monitoring Report on

the Implementation of the CACM Regulation and the FCA Regulation as of
31.01.2019.

ACER – Agency for the Cooperation of Energy Regulators, 2020. Market coupling

development: development of methodologies related to market coupling. Available
via. https://acer.europa.eu/pt/Electricity/MARKET-CODES/CAPACITY-ALLOCATI
ON-AND-CONGESTION-MANAGEMENT/IMPLEMENTATION/Paginas/MARKE
T-COUPLING-DEVELOPMENT.aspx. last check on 26.01.2020.

ACER/CEER – Agency for the Cooperation of Energy Regulators & Council of European
Energy Regulators, 2018. Annual Report on the Results of Monitoring the Internal
Electricity and Natural Gas Markets in 2017 - Electricity Wholesale Markets. Volume,
October 2018.

Amprion, 2020. Cross-border intraday (XBID) project. Available via. https://www.

amprion.net/Energy-Market/Congestion-Management/Multi-Regional-Coupling-
(MRC)-and-Cross-Border-Intraday-(XBID)/Content-Page.html. last check on
26.01.2020.

APG – Austrian Power Grid, 2020. Allocation of cross border transport capacities.

Available via. https://www.apg.at/en/markt/strommarkt/Allokationen. last check
on 26.01.2020.

Bellenbaum, J., Bucksteeg, M., Kallabis, T., Pape, C., Weber, C., 2014. Intra-day cross-
zonal capacity pricing. Study on Behalf of OFGEM. University Duisburg-Essen.
Braun, S., 2018. Pumped Hydropower Storage Optimization and Trading Considering

Short-Term Electricity Markets. Phd project. https://doi.org/10.13140/
RG.2.2.15931.46881.

Braun, S., Brunner, C., 2018. Price sensitivity of hourly day-ahead and quarter-hourly
intraday auctions in Germany. Z. Energiewirtschaft 42, 257–270. https://doi.org/
10.1007/s12398-018-0228-0.

�
Avila, J.P., Fernandes, C., 2015. The Spanish intraday market design. A

Chaves-

successful solution to balance renewable generation? Renew. Energy 74, 422–432.
https://doi.org/10.1016/j.renene.2014.08.017.

CRIDA Approval ES-PT, 2018. Iberian NEMO and TSOs Proposal for the Spanish-

Portuguese Complementary Regional Intraday Auctions in Accordance with the

Article 63 of Commission Regulation (EU) 2015/1222 of 24 July 2015 Establishing a
Guideline on Capacity Allocation and Congestion Management.

CRIDA Approval GR-IT, 2019. Approval by the Greece-Italy Regulatory Authorities of the

Greece-Italy NEMO and TSO Proposal for Complementary Regional Intraday
Auctions.

CRIDA Approval IT-North, 2019. Approval by the Italy Regulatory Authorities of the
Italy North NEMO and TSO Proposal for Complementary Regional Intraday
Auctions.

Diamantopoulos, T.G., Symeonidis, A.L., Chrysopoulos, A.C., 2012. Designing robust

strategies for continuous trading in contemporary power markets. Agent-Mediated
Electronic Commerce. Designing Trading Strategies and Mechanisms for Electronic
Markets, pp. 30–44. https://doi.org/10.1007/978-3-642-40864-9_3.

Ehrenmann, A., Henneaux, P., Küpper, G., Bruce, J., Klasman, B., Schumacher, L., 2019.

The future electricity intraday market design. Available via. https://publications.
europa.eu/en/publication-detail/-/publication/f85fbc70-4f81-11e9-a8ed-01aa75e
d71a1. last check on 26.01.2020.

ENTSO-E – European Network of Transmission System Operators, 2017. All TSOs’

Proposal for the Single Methodology for Pricing Intraday Cross-Zonal Capacity in
Accordance with Article 55 of Commission Regulation (EU) 2015/1222 of 24 July
2015 Establishing a Guideline on Capacity Allocation and Congestion Managements.
ENTSO-E – European Network of Transmission System Operators, 2018. European cross-
border intraday (XBID) solution and 10 local implementation projects successful go-
live. Available via. https://www.entsoe.eu/news/2018/06/14/european-cross-bo
rder-intraday-xbid-solution-and-10-local-implementation-projects-successful-go-live
/. last check on 26.02.2020.

ENTSO-E – European Network of Transmission System Operators, 2020. Single day-
ahead coupling (SDAC). Available via. https://www.entsoe.eu/network_codes/
cacm/implementation/sadc/. last check on 04.04.2020.

EPEX SPOT SE, 2019. Operational rules. Available via. https://www.epexspot.
com/en/downloads#rules-fees-processes. last check on 31.01.2020.

EPEX SPOT SE, 2020a. Basics of the power market. Available via. https://www.epexspot.
com/en/basicspowermarket#day-ahead-and-intraday-the-backbone-of-the-europe
an-spot-market. last check on 26.01.2020.

EPEX SPOT SE, 2020b. Trading products. Available via. https://www.epexspot.
com/en/tradingproducts#intraday-trading. last check on 26.01.2020.

European Commission, 2015. Commission Regulation (EU) 2015/1222 of 24 July 2015
establishing a guideline on capacity allocation and congestion management. Offc. J.
Europ. Union.

European Commission, 2016. Commission Regulation (EU) 2016/1719 of 26 September
2016 establishing a guideline on forward capacity allocation. Offc. J. Europ. Union.

European Commission, 2017. Commission Regulation (EU) 2017/1485 establishing a
guideline on electricity transmission system operation. Offc. J. Europ. Union.

EnergyPolicy145(2020)1117318F. Ocker and V. Jaenisch

European Commission, 2019. Clean energy for all Europeans package completed: good
for consumers, good for growth and jobs, and good for the planet. Available via. http
s://ec.europa.eu/info/news/clean-energy-all-europeans-package-completed-good-
consumers-good-growth-and-jobs-and-good-planet-2019-may-22_en. last check on
26.01.2020.

Furi�o, D., 2011. A survey on the Spanish electricity intraday market. Estud. Econ. Apl. 29

(2), 1–19.

GME – Gestore Mercati Energetici, 2003. Integrated text of the electricity market rules.
Available via. https://www.mercatoelettrico.org/En/MenuBiblioteca/Documenti
/20081020NuovoTestoIntegratoEn.pdf. last check on 31.01.2020.

GME – Gestore Mercati Energetici, 2017. Technical rule no. 03 rev 7 MPE: timing of

activities for the sessions of the MGP, MI and MSD. Available via. https://www.me
rcatoelettrico.org/En/Mercati/MercatoElettrico/Normativa.aspx. last check on
31.01.2020.

GME – Gestore Mercati Energetici, 2020. Spot electricity market MPE. Available via. htt
ps://www.mercatoelettrico.org/En/Mercati/MercatoElettrico/MPE.aspx. last check
on 26.01.2020.

Hagemann, S., Weber, C., 2013. An empirical analysis of liquidity and its determinants in

the German intraday market for electricity. In: EWL Working Paper 17/13.

Henriot, A., 2012. Market Design with Wind: managing low predictability in intraday

markets. In: EUI RSCAS, 2012/63, Loyola de Palacio Programme on Energy Policy.
HUPX – Hungarian Power Exchange, 2019. XBID 2nd wave go-live date confirmed for
November 2019. Available via. https://hupx.hu/en/articles/xbid-2nd-wave-go-live
-date-confirmed-for-november-2019/41. last check on 26.01.2020.

IRENA – International Renewable Energy Agency, 2017. Adapting Market Design to High

Mas-Collel, A., Whinston, M.D., Green, J.R., 1995. Microeconomic Theory. Oxford

University Press.

Neuhoff, K., Batlle, C., Brunekreeft, G., Konstantinidis, C.V., Nabe, C., Oggioni, G.,
Rodilla, P., Schwenen, S., Siewierski, T., Strbac, G., 2015. Flexible Short- Term
Power Trading: Gathering Experience in EU Countries.

Neuhoff, K., Ritter, N., Salah-Abou-El-Enien, A., Vassilopoulos, P., 2016a. Intraday

markets for power: discretizing the continuous trading?. In: DIW Berlin Discussion
Paper No. 1544.

Neuhoff, K., Richstein, J., May, N., 2016b. Auctions for Intraday - trading Impacts on

efficient power markets and secure system operation. In: DIW Berlin Discussion
Paper No. 1494.

Ocker, F., Ehrhart, K.-M., 2017. The “German paradox” in the balancing power markets.

Renew. Sustain. Energy Rev. 67, 892–898. https://doi.org/10.1016/j.
rser.2016.09.040.

Oggioni, G., Lanfranconi, C., 2015. Empirics of Intraday and Real-Time Markets in

Europe: Italy. DIW, Berlin.

OMIE – Operador do Mercado Ib�erico de Energia, 2018. Day-ahead and Intraday
Electricity Market Operating Rules (Non-binding Translation of the Market
Operating Rules), 11.05.2018, Madrid.

Scharff, R., Amelin, M., 2016. Trading behaviour on the continuous intraday market
Elbas. Energy Pol. 88, 544–557. https://doi.org/10.1016/j.enpol.2015.10.045.
SEMOpx, 2017. SEMOpx operating procedures. DAM, IDA, IDC. Available via. http://lg.
sem-o.com/ISEM/General/SEMOpx%20Operating%20Procedures%20Draft.pdf. last
check on 26.01.2020.

SEMOpx, 2020. Intraday market auctions. Available via. https://www.semopx.com/ma

Shares of Variable Renewable Energy (Abu Dhabi).

rkets/intraday-market/. last check on 26.01.2020.

Just, S., Weber, C., 2015. The German market for system reserve capacity and balancing.

In: EWL Working Paper 06/15.

Kiesel, R., Paraschiv, F., 2017. Econometric analysis of 15-minute intraday electricity
prices. Energy Econ. 64, 77–90. https://doi.org/10.1016/j.eneco.2017.03.002.

Krishna, V., 2002. Auction Theory. Academic Press.
Lanfranconi, C., Lanza, S., Rossi, S., 2019. Intraday electricity market and efficient
congestion management: continuous trading vs. implicit auctions. In: Power
Conference on Energy Research and Policy. Haas School of Business – UC Berkeley.
Maciejowska, K., Nitka, W., Weron, T., 2019. Day-ahead vs. Intraday—forecasting the
price spread to maximize economic benefits. Energies. https://doi.org/10.3390/
en12040631, 12/631.

M€arkle-Huß, J., Feuerriegel, S., Neumann, D., 2018. Contract durations in the electricity
market: causal impact of 15 min trading on the EPEX SPOT market. Energy Econ. 69,
367–378. https://doi.org/10.1016/j.eneco.2017.11.019.

Martin, H., Otterson, S., 2018. German intraday electricity market analysis and modeling
based on the limit order book. In: Proceedings of the 15th International Conference
on the European Energy Market. https://doi.org/10.1109/EEM.2018.8469829.

Shinde, P., Amelin, M., 2019. A literature review of intraday electricity markets and
prices. IEEE Milan PowerTech. https://doi.org/10.1109/PTC.2019.8810752.
SIDC – Single Coupling Intraday Coupling, 2019. European Single Intraday Coupling

(SIDC) Parties confirm successful 2nd wave go- live. Available via. http://www.ne
mo-committee.eu/assets/files/sidc-press-release-successful-2nd-wave-go-live.pdf.
last check on 26.01.2020.

Skajaa, A., Edlund, K., Morales, J.M., 2015. Intraday trading of wind energy. IEEE Trans.
Power Syst. 30 (6), 3181–3189. https://doi.org/10.1109/TPWRS.2014.2377219.

Soysal, E.R., Olsen, O.J., Skytte, K., Sekamane, J.K., 2017. Intraday market

asymmetries—a Nordic example. In: Proceedings of the 14th International
Conference on the European Energy Market. https://doi.org/10.1109/
EEM.2017.7981920.

Weber, C., 2010. Adequate intraday market design to enable the integration of wind

energy into the European power systems. Energy Pol. 38 (7), 3155–3163. https://
doi.org/10.1016/j.enpol.2009.07.040.

Zweifel, P., Praktiknjo, A., Erdmann, G., 2017. Energy Economics–Theory and

Applications. Springer Publishing. https://doi.org/10.1007/978-3-662-53022-1.

EnergyPolicy145(2020)1117319