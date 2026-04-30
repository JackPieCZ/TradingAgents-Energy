Time Evolution of Hurst Exponent: Czech
Intraday Electricity Market Study
Juraj Čurpek *

Abstract:
In  this  paper  we  analyse  a  temporal  evolution  of  the  Hurst  exponent  estimated
on hourly  returns  of  intraday electricity  prices  in  the  Czech  Republic  in  2017  and
2018. Firstly we used the log-returns with adjustments due to negative values, and
secondly we employed the returns based on the area hyperbolic sine transformation.
We implemented a sliding window technique in order to estimate the Hurst exponent
using the Detrended Fluctuation Analysis method on subsamples with four distinct
window sizes. According to the stylised facts of electricity, the spot prices and their
corresponding  logarithmic  returns  should  be  mean-reverting.  Since  the  Czech
this
intraday  electricity  market  remains  mostly  unexplored,  we  examined
phenomenon  on  the  intraday  rather  than  on  the  spot  market.  Consequently,  our
analysis  showed  that  the  estimated  values  of  Hurst  exponent  indicate  a  mean-
reverting process for time scales greater than 24 hours and a weakly mean-reverting
process for the shorter time scales. There were a few exceptions, though, since our
calculations have revealed the presence of a nearly random or even weakly persistent
behaviour on the shorter time scales.
Key words:  Hurst exponent; Detrended Fluctuation Analysis; electricity markets;
intraday market.
JEL classification:  C13, G10.

1  Introduction
In  developed  countries,  electricity  trading  currently  takes  place  on  liberal  and
deregulated markets. Unlike other commodities, electricity is economically still not
viable to store since there is no efficient and financially sensible way of storing it,
even  though  electricity  can  actually  be  stored  in  batteries  or  through  the  use
of pumped hydro storage dams. Moreover, at every moment the aggregate supply
must meet the aggregate demand. Otherwise, shortages of electricity would occur
at some  places  or  the  electricity  grid  would  collapse.  Therefore,  the  price
of electricity  should  respect  the  transmission  grid  constraints  and  the  market
coupling in EU, which means the integration of two or more electricity markets from

*   Juraj Čurpek; University of Economics, Prague, Faculty of Finance and Accounting, Department
of  Banking  and  Insurance,  W.  Churchill  Sq.  4,  130  67  Prague  3,  Czech  Republic,
<xcurj07@vse.cz>.

  The  article  is  processed  as  an  output  of  a research  project  Vývojové  trendy na  finančních  trzích
registered by the Grant Agency of University of Economics, Prague under the registration number
F1/46/2019.

25

Čurpek, J.: Time Evolution of Hurst Exponent: Czech Intraday Electricity Market Study

different EU areas through the implicit cross-border allocation mechanism (Bergh
et al., 2016). Moreover, the so-called intermittent renewable energy sources, mostly
solar and wind generation units, have been recently widely used in many countries,
and these strongly depend on weather conditions. Together with an increase in the
capacity of the power grid, they have caused a higher volatility in the electricity load
and price (Hong et al, 2016).
The  presented  paper  focuses  on  the  Czech  wholesale  intraday  electricity  market
where electricity is traded between the producers and retailers or large consumers.
Although there is a plethora of studies that deal with the spot  (day-ahead) prices,
amount of research covering the topic of intraday electricity prices is rather scarce
and to this date none of it has dealt with the Hurst analysis of the intraday electricity
prices or their returns, concentrating rather on forecasting. For instance, the intraday
prices prediction was analysed by Monteiro et al. (2016) using artificial intelligence
on the Iberian electricity market. They deduced that variables with the largest impact
were the previous intraday prices and seasonal dummies. In the paper by Uniejewski
et  al.  (2019),  which  focused  on  the  forecasting  and  variable  selection  using  the
intraday  prices  transformed  using  the  area  (inverse)  hyperbolic  sine,  it  was
concluded that the most important regressors were the day-ahead price for the same
or nearby hour and the most recent intraday price. Regarding the Czech electricity
market, so far there is only a single relevant research by Béreš (2016), who analysed
the intraday market and its impact on the day-ahead counterpart with the conclusion
that the forecast errors of the renewable (mainly solar) generation and load affect
the  intraday  prices.  Furthermore,  the negative  intraday  prices  are  related  to  the
unexpected surplus of the renewable generation or the negative demand shock and
there is no connection with the negative day-ahead prices.
According to the stylised facts of electricity prices, the spot prices and also their
returns are mean-reverting. However, this feature has not been explored for intraday
prices or their respective returns, which is the goal of this paper. Application of the
Hurst  exponent  analysis,  which  quantifies  the  long-term  memory  in  time  series,
states  that  the  mean-reverting  process  should  have  a  certain  value  of  the  Hurst
exponent,  specifically  between  zero  and  0.5.  Thus,  we  can  estimate  the  time-
evolution of the Hurst exponent for intraday electricity returns, which could indicate
the potential presence of mean-reversion.
Relevant  empirical  studies  that  concentrated  solely  on  the  mean-reversion  of  the
spot electricity prices found a weak-mean reversion (Simonsen, 2003) on the Nord
Pool market. Meyer-Brandis et al. (2008) concluded that a daily spot electricity price
on  several  European  electricity  markets  is  a  sum  of  several  mean-reverting
processes with different speeds of mean reversion.
Regarding the empirical studies concerning the Hurst exponent of electricity prices,
it  was  shown  by  Kristoufek  et  al.  (2013)  that  hourly  prices  of  electricity  on the

26

European Financial and Accounting Journal, 2019, vol.14, no. 3, pp. 25-44.

Czech  market  over  the  period  2009–2012  were  mean-reverting  with  the  scaling
exponent h ≈ 1.1, which corresponds to the Hurst exponent of H ≈ 0.1. In another
study (Weron, 2000), analysis of the logarithmic returns of average daily electricity
prices  on  the  California  Power  Exchange  (CalPX)  and  Swiss  Electricity  Price
(SWEP)  from  1998  to  2000  has  concluded  with  the  similar  results,  i.e.  that
logarithmic returns are mean-reverting. In  an extensive study of electricity prices
predictability in the Canadian provinces of Alberta and Ontario and the US Mid-C
market (Uritskaya et al., 2015) it was concluded that the original prices exhibited
strong mean-reverting behaviour as well, which is in accordance with the stylised
facts.
Since the number of studies on the Czech intraday market is limited and there are
no  actual  studies  concerning  the  Hurst  exponent  analysis  on  the  Czech  intraday
electricity market, the aim of this paper is to examine this matter and fill the gap.

2  Electricity Prices

2.1 Stylised facts of electricity prices
The unique features of electricity  cause its special price dynamics, in a literature
also  called  the  stylised  facts  (Girish  et  al.,  2013).  Note  that  some  of  these
characteristics are observable not only for the spot prices, but also for their returns.
The  most  visible  is  hourly,  daily,  weekly  and  annual  seasonality  caused  by  the
climate  changes  and  social  factors  that  influence  the  consumption.  Furthermore,
these seasonal patterns depend on the climate location, i.e. in the countries closer
to the equator the highest consumption is observed in the summer season due to air-
conditioning  and  in  the  countries  with  higher  latitudes,  the  highest  consumption
occurs in winter months due to heating.
Extreme volatility which tends to form clusters is visible as well. It is caused by non-
storability  of  electricity,  so  in  the  unexpected  change  of  consumption  there  are
almost no reserves that can be used immediately. Electricity prices are also well-
known to exhibit the so-called spikes, which are rapid changes in price that can be
both positive and negative with a slow reversion to the smaller/higher price. The
reasons are the demand or supply shocks, transmission constraints, etc.
Apart from that, spot electricity prices can under certain circumstances attain even
negative values and this phenomenon is not uncommon to observe in time series
data, e.g. as depicted on Figure 1. The reason is  that it is more profitable to sell
electricity for a negative price (in fact paying the buyer for electricity) than to shut
down the generators and then restart them again. Furthermore, as mentioned in the
introductory part, electricity prices are assumed to be mean-reverting. Hence, they
tend  to move  towards the  long-term price  level  over some time  that  corresponds
to the slowly changing marginal costs.

27

Čurpek, J.: Time Evolution of Hurst Exponent: Czech Intraday Electricity Market Study

2.2. Electricity prices formation
Formation of the spot  (day-ahead) electricity prices is well-known and can serve
as the  starting  point  into  the  analysis  of  the  formation  of  intraday  prices
of electricity.  In  general,  from  the  economic  theory  the  spot  electricity  price
is established  in  the  intersection  of  the  demand  and  supply  curves.  The  demand
is highly inelastic at the given time and the supply curve (also called the merit order
curve)  represents  the  marginal  costs  of  power  generation  using  different  power
sources.  Thus,  electricity  price  represents  the  marginal  cost  of  the  last  (with
the largest  marginal  cost)  power  generating  unit  that  wishes  to  participate  in  the
electricity trading auction, so the spot electricity prices reflect several fundamental
factors, which have an impact on the supply and demand for electricity. The most
important  factor  is  the  weather  conditions  that  influence  the  supply  side  via
renewables  and  the  consumption  (demand)  via  air-conditioning,  heating,  etc.
Another important demand-side factor is represented by the human-based business
cycles such as peak-hours during the working day, weekends and holidays that cause
the  apparent  seasonality.  The  supply-side  factors  consist  of  the  finance-like
variables such as the cost of building a power plant, its maintenance, operational
costs and costs of the fuel used in non-renewable electricity plants, i.e. coal, natural
gas, nuclear fuel  prices,  etc.  Moreover, the  spot  electricity  prices  also reflect  the
impact of regulations such as Carbon Emission Allowance, which has an impact on
the thermal power plant generation.
Prior  to  the  analysis  of  the  factors  that  influence  the  intraday  electricity  prices,
we take a look at the intraday market mechanics in Czechia. In general, the intraday
market  organised  by  OTE  complements  the  day-ahead  market  for  trading
throughout a day in the case of unpredicted events such as unexpected consumption,
weather conditions, etc. The day-ahead market closes at 11 a.m. on the day before
any  physical  delivery  takes  place,  and  before  2:30  p.m.  on  the  Day  1  the  spot
electricity prices are set for every hour of the Day 2 based on the expected demand
(both  domestic  and  exported/imported)  for  electricity  and  the  forecasted  load.
In addition, the spot prices must take into account the cross-border flow between
the countries, since the Czech, Slovak, Hungarian and Romanian day-ahead markets
are interconnected.
The  Czech  intraday  market  opens  daily  at  3  p.m.  and  closes  separately  for  each
hourly period 60 minutes before the physical delivery. Since the intraday market
participants have knowledge of the day-ahead price for the given hour, the intraday
price  for  the  exact  hour  should  also  reflect  the  improved  forecast  about  the
renewable  production  as  a  result  of  the  updated  weather  forecast,  updated
knowledge of the demand, information about the power plants outages and updated
electricity flow between countries as a result of the market coupling. Furthermore,
it works the other way around; the intraday prices have impact on  the day-ahead

28

European Financial and Accounting Journal, 2019, vol.14, no. 3, pp. 25-44.

price on the next day. In a study on the differences between intraday and day-ahead
electricity prices in the Danish power market, Karanﬁl et al. (2017) concluded that
a difference between intraday and day-ahead prices is primary caused by the wind
and conventional generation forecast errors and the intraday prices are negatively
inﬂuenced  by  the  forecast  error  of  wind  power  generation.  In addition,  an
unexpected  increase  in  the  combined  heat  and  power  generation  leads  to  higher
intraday prices and wider gap between intraday and day-ahead prices.

3  Hurst Exponent and Time Series Predictability
To conduct our research, we used a common measure of time series predictability
the Hurst exponent, introduced by H. E. Hurst to study the long-term water levels
in  Aswan  water  reservoir  (Hurst,  1951).  It  quantifies  the  long-term  memory  and
relates  to  the  autocorrelation  of  time  series.  Its  estimation  was  originally  based
on the  so-called  Rescaled  Range  approach  which  assumes  time  series  to  be
stationary,  which  might  not  be  the case  of  most  of the  real  financial  time  series.
Thus,  we  used  another  well-known  estimator  of  the  Hurst  exponent  called  the
Detrended  Fluctuation  Analysis  (described  below),  which  is  capable  of  handling
both stationary and non-stationary (both in mean and variance) time series.
The Hurst exponent can take any value in the range from zero to one. Anti-persistent
or  mean-reverting  time  series  have  the  Hurst  exponent  less  than  0.5.  The Hurst
exponent for persistent time series is larger than 0.5 and the uncorrelated random
time series have the Hurst exponent around 0.5.
This paper focuses on a common estimation algorithm which is called the Detrended
Fluctuation  Analysis  (DFA)  introduced  by  C.  K.  Peng  (Peng  et  al.,  1994)  while
studying the long-range correlations in DNA sequences. DFA is based on dividing
the  time  series  with  N  observations  into  k  non-overlapping  subsamples/windows
with equal size t. Subsequently, within each subsample we ﬁnd a local trend yt(k),
which  is  a  polynomial  ﬁt  of  some  order.  The  linear  fit  is  sometimes  denoted  as
DFA(1),  quadratic  fit  as  DFA(2),  etc.  The  integrated  time  series  y(k)  is  in  turn
detrended  by  subtracting  the  local  trend  in  each  subsample,  and  eventually  we
calculate the Fluctuation function for the specific time scale, defined as follows:

𝐹(𝑡) = √

1
𝑁

𝑁
2
∑(𝑦(𝑘) − 𝑦𝑡(𝑘))
𝑘=1

(1)

This calculation is repeated over all time scales to quantify the relationship between
the scaling or fluctuation function F(t) and the time-scale t visible as the slope of the
line between logF(t) and log(t), which corresponds to the scaling exponent h as the
estimate of the Hurst exponent if the time series is stationary. It is exponent because

29

Čurpek, J.: Time Evolution of Hurst Exponent: Czech Intraday Electricity Market Study

the relationship between F(t) and the time scale t (C is some constant) can be also
written as:

 𝐹(𝑡) = 𝐶𝑡ℎ

(2)

The scaling exponent is larger than one for non-stationary time series and relates
to the classical Hurst exponent simply as:

𝐻 = ℎ − 1

(3)

The Hurst exponent relates to the fractal  or Hausdorff  dimension for self-similar
time  series,  since  self-similar  dynamic  price  processes  are  characterised  by
a reflection of the local structure into the global structure (Mandelbrot, 1985):

𝐷 = 2 − 𝐻

(4)

It quantifies the roughness or smoothness of time series, so it is a local (short-term
memory) characteristic of time series as opposed to the Hurst exponent (Gneiting et
al., 2004).
The  application  of  the  Hurst  exponent  can  be  extended  to  study  the  multifractal
properties of time series using the Generalised Hurst exponent H(q), where q is the
moment  order  of  fluctuation  function.  Analogously,  the  so-called  Multi-Fractal
Detrended  Fluctuation  Analysis  method  (Kantelhardt,  2002)  has  been  developed
to estimate the values of the Hurst exponents for the given q. Then the scaling law
takes the following form:

𝐹(𝑞, 𝑡) = 𝐶𝑡ℎ(𝑞)

(5)

For monofractal time series the fluctuation function is independent of q, and in the
special case if q = 2, the generalised Hurst exponent is equal to the classical Hurst
exponent, which we deal with in this paper.

4  Data and Methodology
All calculations in this paper are based on the public data provided by the OTE, a.s.
–  the  Czech electricity  and  gas market  operator  on  its  webpage  (http://www.ote-
cr.cz/statistika/) in the form of annual reports with comprehensive information about
electricity trading. Nevertheless, for our purposes we used the average electricity
prices  on  intraday  trading  with  hourly  frequency  in  EUR/MWh.  To  assure
an adequate length of the dataset, our analysis was made on the data that spanned
from 1.1.2017 to 31.12.2018 which totals in 17,520 observations.
In our research, we were interested in quantifying the Hurst exponent of the returns
(increments) of actual prices after some variance-stabilising transformation as the
majority of the related papers does due to the fact that intraday prices exhibit high
volatility and spikes which impact not only the modelling (Uniejewski et al., 2017),

30

European Financial and Accounting Journal, 2019, vol.14, no. 3, pp. 25-44.

but  also  the  estimation  of  the  Hurst  exponent.  However,  calculation  of  the  log-
returns  from  electricity  prices  is  not  feasible  when  applied  on  negative  or  close
to zero  prices.  There  are  some  naïve  methods  of  how  to  tackle  these  obstacles,
for instance adding a constant to every observation, so it would be strictly positive
(Sewalt  et  al.,  2003)  or  dropping  the  negative  observations.  We tried,  at  first,
to calculate  the  adjusted  log-returns  of  the  intraday  electricity  prices  with  naïve
adjustment  for  the  negative  prices.  Since  the  log-returns  are  quantifiable  only
on series with positive prices, we replaced 192 negatives out of 17,519 observations
with  zeros  to  get  adjusted  log-returns.  Then  we  employed  a different  approach
to calculate  the  returns  using  the  area  (inverse)  hyperbolic  sine  transformation
as suggested  by  Schneider  (2012),  because  it  shares  some  similarities  with
a logarithm and allows for zero and negative values:

𝑥 = 𝑠𝑖𝑛ℎ−1 (

𝑝−𝜉
𝜆

)

(6)

where p is price, ξ is an offset and λ stands for scale. Due to simplicity, the offset is
equal to zero and the scale is equal to one. The asymptotic log behaviour for │p│→
+∞ can be described as follows:

𝑥 = 𝑠𝑖𝑛ℎ−1(𝑝) = 𝑙𝑛(𝑝 + √𝑝2 + 1) ≈ 𝑠𝑖𝑔𝑛(𝑝) 𝑙𝑛(2|𝑝|)

(7)

To calculate the Hurst exponent that varies with time, we decided to apply the so-
called rolling or sliding window approach, which means that the calculation  was
made on a subsample with a size Ns out of the total sample Nmax called the sliding
window.  On  each  window,  which  was  moved  by  defined  step  δs,  we  calculated
a static  Hurst  exponent  to  generate  a  sequence  of  Hurst  exponents  with  length
ranging from one when the subset coincides with the whole set to  Nmax –Ns +1 if
δs = 1. There is no strict consensus about how wide the rolling window should be.
Nevertheless, we based our selection of the sliding window size on Carbone et al.
(2004) who suggest that the minimum size of the subset should be  Nmin ≈ 2,000–
3,000 to achieve that the scaling law equation (2) holds.
Since  we  dealt  with  the  hourly  data,  we  experimentally  chose  the  step  to  be  24
hours/observations (one day) and the sliding window to have four distinct lengths:
2,190 hours (three months), 4,380 hours (six months), 6,570 hours (nine months)
and 8,760 hours (one year).
Consequently, the Hurst exponent sequences had a corresponding length, i.e. 638
days for three-month window, 547 days for six-month window, 456 days for nine-
month window and 365 days for a year-long window.

31

Čurpek, J.: Time Evolution of Hurst Exponent: Czech Intraday Electricity Market Study

Fig. 1: Intraday prices, logarithmic and inverse hyperbolic sine returns

  Source: Own computation, data from OTE webpage

5  Results and Discussion
We estimated  the  Hurst  exponent  by  applying  DFA method  on  the  adjusted log-
returns and inverse hyperbolic sine returns of hourly intraday prices of electricity
using the statistical language R (RStudio ver. 1.1463, package nonlinearTseries ver.

32

European Financial and Accounting Journal, 2019, vol.14, no. 3, pp. 25-44.

0.2.5).  As  the  graphical  results,  we  present  plots  of  scaling  function  vs. scaling
window size applied on a full sample to check for the potential crossovers, and the
final plots of time evolution of the Hurst exponent estimated on the sliding windows
of different sizes. Note that the DFA method does not take into account the window
sizes below 10 due to its unreliability.

5.1 Adjusted log-returns
Applying the DFA method on the full sample of adjusted log-returns results in the
Figure 2 on next page which clearly indicates at least two crossovers – change in
the scaling exponents represented as the slope of the regression line. Therefore, we
have three different Hurst exponents for three different time scales. However, since
the fluctuation  function  estimations  above  the  second  crossover  are  evidently
biased,  we  considered  only  time  scales  up  to  the  second  crossover.  Thus,  we
calculated only two Hurst exponents.
Based on the graphical analysis and on the expert estimate, the position of the first
crossover  is  located  at  approx.  24  hours,  with  the  corresponding  Hurst  exponent
being  approx.  0.44,  which  indicates  a  weak  mean-reverting  process.  The  next
crossover  is  less  pronounced  than  the  first  one  and  located  at  the  time  scale
of approx.  240  hours  with the corresponding  Hurst  exponent  being  approx.  0.19,
which indicates a stronger mean-reversion process than on the shorter time scales.
This  clearly  shows  that  the  log-returns  of  intraday  electricity  prices  are  not  self-
affine since they behave differently on different time scales.
The  interpretation  follows  from  the  mechanics  of  the  intraday  market  described
in Section 2.2. The intraday prices and their respective log-returns separated by one
day  are  an  outcome  of  the  price  formation  process  based  on  unexpected  events,
imperfectly  forecasted  power  generation  of  renewables,  load,  and  thereby
consecutive  (or  the  same)  day-ahead  prices.  Since  the  day-ahead  prices  are  also
updated based on the previous intraday prices, for small time scales these updates
are relatively recent. These unexpected effects project themselves in more random-
like  behaviour  of the intraday  prices  and returns,  since  the  Hurst  exponent  close
to 0.5  indicates  the  uncorrelated  random  process.  On  the  higher  time  scales,  the
time-separation  between  the  intraday  prices  is  more  than  one  day  and  thus  their
values  are  based  on  the  aforementioned  forecasted  variables  for  different  days.
Consequently,  the  prices  and  their  returns  more  likely  tend  to  behave  according
to the stylised facts of the spot electricity prices, so they are mean-reverting.

33

Čurpek, J.: Time Evolution of Hurst Exponent: Czech Intraday Electricity Market Study

Fig. 2: Estimation of two Hurst exponents on different time scales

Source: Authorial computation
Due to the crossovers we estimated the time-varying Hurst exponents on two time
scales – 10–24 hours and 25–240 hours, applying four different window sizes and
a constant time step of 24 hours.
As depicted on Figures 3 and 4 on the next pages, in general, a wider sliding window
smooths the sequence of Hurst exponents compared to the narrower one regardless
of the time scale, and thereby it points out that the Hurst exponent stays quite stable
when calculated on the year-long sample. On the other hand, in case of the shorter
time scales, the sliding window with the width of 2,190 observations better captures
dynamics  of  the  estimated  Hurst  exponent  with  more  details.  Most  of  the  time
it indicated a weakly anti-persistent process, with a few exceptions when it revealed
approximately  random  or  even  slightly  persistent  process  for  53  out  of 639
observations with Hmax=0.56 for the centre of the sliding window corresponding to
the end of the year of 2017 and beginning of the 2018.
On the longer time scales, the estimated Hurst exponent indicates a mean-reverting
process for the whole time series and its dynamics is better visualised when using
the  narrower  sliding  window.  Moreover,  when  using  the  year-long  sample,  the
estimated Hurst exponent is roughly stable. The only sharp decline of the estimated
Hurst exponent level is approximately for the last 50 values.

34

European Financial and Accounting Journal, 2019, vol.14, no. 3, pp. 25-44.

Fig. 3: Hurst exponent – time scale of 10–24 hours

Source: Authorial computation

35

Čurpek, J.: Time Evolution of Hurst Exponent: Czech Intraday Electricity Market Study

Fig. 4: Hurst exponent – time scale of 25–240 hours

Source: Authorial computation

36

European Financial and Accounting Journal, 2019, vol.14, no. 3, pp. 25-44.

Tab. 1: Average Hurst exponent

Time scale/window
size

10–24 h

25–240h

2,190

0.4186

0.1913

4,380

0.4217

0.2018

Source: Authorial computation

6,570

0.4260

0.2059

8,760

0.4328

0.2077

5.2 Inverse hyperbolic sine returns
In case of inverse hyperbolic sine returns, the results are similar to those when using
the  adjusted  log-returns.  There  are  also  two  crossovers  after  applying  the  DFA
method on the full-size sample of time series, as illustrated on Figure 5. Thus, we
estimated  two  different  Hurst  exponents  on  two  different  time  scales.  The
crossovers were again determined graphically and by expert estimate.
The first crossover again corresponds to approx. 24 hours with the estimated Hurst
exponent  being  approx.  0.45,  which  indicates  a  weak  mean-reversion.  Next
crossover is more noticeable than in the previous case  (adjusted log-returns)  and
it is located at the time scale of approx. 240 hours. The respective estimated Hurst
exponent  at  these  time  scales  is  approx.  0.19  which  signifies  a  stronger  mean-
reversion  than  on  shorter  time  scales.  Since  estimated  values  of  the  fluctuation
function are evidently biased on the higher time scales, we omitted the calculation
of  the  Hurst  exponent  above  the  second  crossover  as  in  the  case  of  log-returns.
The interpretation of the different estimated Hurst exponents is the same as in the
case of adjusted log-returns.
Fig. 5: Estimation of two Hurst exponents on different time scales

Source: Authorial computation

37

Čurpek, J.: Time Evolution of Hurst Exponent: Czech Intraday Electricity Market Study

The  time-varying  Hurst  exponents  were  again  computed  using  four  different
window sizes. The results are summarised in Table 2 and on Figures 6, 7.
In  general,  the  results  are  analogous  to  the  previous  case  when  we  worked  with
adjusted log-returns. Thus, the wider sliding window generates smoother sequence
of estimated Hurst exponents compared to the narrower one, and the estimated Hurst
exponent  stays  stable  when  calculated  on  the  year-length  sample  for  short  time
scales. For longer time scales, however, even using the sliding window of yearly
length results in a sequence of estimated Hurst exponents that exhibits a level drop
near the end, as revealed on Figure 7.
Similarly,  in  case  of  the  short  time  scales,  the  sliding  window  with  the  width
of 2,190  observations  displays  the  estimated  Hurst  exponent  attaining  values
associated with mean-reverting behaviour. However, in some cases the estimated
Hurst exponent is even associated with almost random process or weakly persistent
behaviour with Hmax=0.55. As illustrated on Figure 6, these events occur for sliding
windows whose centre corresponds to the three different periods – approx. 06/2017,
the period ranging from 12/2017 to 01/2018 and 06/2018.
In addition, there is evident tendency of the estimated Hurst exponent rising almost
to the level of 0.5. The reason was explained in the previous section, i.e. the intraday
electricity  market  should  cover  the  unexpected  and  unforecasted  changes
in electricity demand and supply (generation) that was not reflected in the day-ahead
prices. In case of short time scales, updates of these changes are relatively “fresh”,
since also the day-ahead prices and their returns are based on intraday prices, which
reflect the changes of forecasted electricity variables. Thus, the imperfect forecast
of  the  renewable  generation  load  and  sudden  change  of  the  expected  demand
(together with market participants’ expectations) cause the intraday prices and their
returns to behave in a more random-like way.
On  the  Figure  7  we  noticed  that  on  the  longer  time  scales  the  estimated  Hurst
exponent  indicates  a  mean-reverting  process  for  the  whole  time  series  and  its
dynamics is better visualised when using the narrower sliding window.
Tab. 2: Average estimated Hurst exponent

Time scale/window

2,190

10–24 h

25–240h

0.4218

0.1854

Source: Authorial computation

4,380

0.4284

0.1995

6,570

0.4332

0.2006

8,760

0.4411

0.2001

38

European Financial and Accounting Journal, 2019, vol.14, no. 3, pp. 25-44.

Fig. 6: Hurst exponent – time scale of 10–24 hours

Source: Authorial computation

39

Čurpek, J.: Time Evolution of Hurst Exponent: Czech Intraday Electricity Market Study

Fig. 7: Hurst exponent – time scale of 25–240 hours

Source: Authorial computation

40

European Financial and Accounting Journal, 2019, vol.14, no. 3, pp. 25-44.

6  Conclusion
In  this  paper  we  applied  the  Hurst  exponent  analysis  on  the  Czech  intraday
electricity market, which still remains to be mostly unexplored. We employed the
Detrended  Fluctuation  Analysis  to  estimate  the  time-varying  Hurst  exponent
on hourly  log-returns  of  the  intraday  electricity  prices  adjusted  for  the  negative
values,  and  on  hourly  area  (inverse)  hyperbolic  sine  returns.  Due  to  presence
of the crossovers  in  the  scaling  function,  we  concluded  that  the  intraday  hourly
returns in our sample were not self-affine. Thus, on two different time scales divided
by the  crossover  that  corresponds  to  24  hours,  there  are  two  different  Hurst
exponents.  We  assume  that  this  is  due  to  the  intraday  market  price  formation
process,  i.e.  the  intraday  market  complements  the  day-ahead  market,  which
repetitively sets the prices (and load) on the daily basis for the whole next day. Thus,
on the time scales of less than 24 hours, the intraday prices and returns are based
on the unexpected supply and demand changes that were not forecasted by the day-
ahead market for the time interval between 12 and 36 hours in advance. Their time
distance to their consecutive day-ahead forecast is the same for the time scale of 24
hours  and  less  for  smaller time  scales.  Moreover,  the  day-ahead  prices  and  their
returns  are  also  based  on  the  previous  intraday  prices,  which  are  based  on the
updated forecast  of the supply and demand changes. This mutual updating to the
changes of fundamental factors that influence electricity prices causes the intraday
returns  on  smaller  time  scales  to  be  weakly  mean-reverting  or  behave  in  a near-
random way. However, the intraday prices and returns on the time scales above 24
hours are based on different, unexpected supply and demand changes from the day-
ahead market forecast, because they were made on more distant days. As a result,
on the larger time scales the intraday returns behave more like the day-ahead returns,
which are mean-reverting according to the stylised facts.
To  get  a  better  view  of  temporal  evolution  of  the  estimated  Hurst  exponent,
we applied the sliding windows of different sizes on the both types of returns. They
brought similar results as visualised by the plots, when the larger sliding windows
caused larger smoothing of the estimated Hurst exponent sequence. Thus, to detect
some dynamics in time we suggest not to use an excessively wide window, even
though  it  might  lead  to  more  precise  estimation  of  the  Hurst  exponent.  In  our
research, the sliding window with a size of three months was satisfactory.
Moreover,  we  have  come  to  the  conclusion  that  the  estimated  Hurst  exponent
on both types of returns indicates that, in general, the intraday electricity returns are
mean-reverting.  For  larger  time  scales  above  one  day,  the  average  value  of  the
estimated Hurst exponent was approximately 0.2 regardless of the type of returns
we used. This result is in agreement with the stylised facts of electricity prices (and
also returns), now extended to intraday electricity returns.

41

Čurpek, J.: Time Evolution of Hurst Exponent: Czech Intraday Electricity Market Study

However, as the time scales get shorter than one day, the estimated Hurst exponent
was associated with a weakly mean-reverting process, since the average value of the
Hurst  exponent  was  approximately  0.43.  Furthermore,  in  some  short  periods  the
estimated Hurst exponent was associated with a behaviour of the returns that is close
to randomness or even weak persistence. In addition, using the inverse hyperbolic
sine returns revealed that these nearly random or weakly persistent regimes occurred
in the summer of 2017 and 2018 and in the winter between 2017 and 2018. Thus,
these periods were separated by roughly 6 months. We believe these were caused
by the imperfect forecast of  mainly renewable generation load (dependent on the
weather)  and  a  sudden  change  of  the  expected  demand  together  with  the
expectations of the market participants, which substantially deviated from the real
(generated)  supply  and  demand.  Thus,  a  more  precise  forecast  of  the  power
production, especially  of the  renewable sources,  which  are  based  on the  weather
forecast, together with the expected demand would diminish the gap between the
intraday and day-ahead prices and their returns.
Further research into the behaviour of the Hurst exponent on the intraday electricity
market with data comprising several years may show if these periods of non-mean-
reverting or almost random behaviour can be detected on different markets and for
different periods.

References
Bergh, Van den, K., Boury, J., Delarue, E., 2016. The Flow-Based Market Coupling
in Central Western Europe: Concepts and definitions. The Electricity Journal, 29(1),
24-29, 2016. DOI: 10.1016/j.tej.2015.12.004.
Béreš, S., 2017. Impact of Czech intraday market on the electricity prices. Bachelor
thesis. Charles University. Faculty of Social Sciences Institute of Economic Studies.
Carbone,  A.;  Castelli,  G.;  Stanley,  H.E.,  2004.  Time-dependent  Hurst  exponent
in financial  time  series.  Physica  A:  Statistical  Mechanics  and  its  Application,
344:267–271. DOI: 10.1016/j.physa.2004.06.130.
Girish,  G.  P.,  Vijayalakshmi  S.,  2013.  Determinants  of  Electricity  Price
in Competitive Power Market. International Journal of Business and Management;
Vol. 8, No. 21. Canadian Center of Science. DOI: 10.5539/ijbm.v8n21p70.
Gneiting, T., Schlather, M., 2004. Stochastic models that separate fractal dimension
and
46:269.  DOI:
effect.
10.1137/S0036144501394387.
Hong, T., Fan, S., Pinson, P., Zareipour, H, Troccoli, A., Hyndman, R. J., 2016.
Probabilistic energy forecasting: Global Energy Forecasting Competition 2014 and
beyond.
914–938.  DOI:
International
10.1016/j.ijforecast.2016.02.001.

of  Forecasting

Review.

Journal

SIAM

2004;

hurst

32,

the

42

European Financial and Accounting Journal, 2019, vol.14, no. 3, pp. 25-44.

from:

Hurst,  H.  E.,  1951.  Long-Term  Storage  of  Reservoirs:  An  Experimental  Study.
Transactions of the American Society of Civil Engineers, 116, 770-799.
Kantelhardt, J., Zschiegner, S., Koscielny-Bunde, E., Bunde, A., Havlin, S., Stanley
E.,  2002.  Multifractal  Detrended  Fluctuation  Analysis  of  Nonstationary  Time
Series. Physica A: Statistical Mechanics and its Applications, 316(1-4):87–114.
Karanﬁl, F., Li, Y., 2017. The Role of Continuous Intraday Electricity Markets: The
Integration of Large-Share Wind Power Generation in Denmark. Energy Journal,
38(2).
Kristoufek,  L.,  Lunackova,  P.,  2013.  Long-term  Memory  in  Electricity  Prices:
Czech Market Evidence. Faculty of Social Sciences, Charles University in Prague,
Available
<journal.fsv.cuni.cz/storage/1282_407-24---kristoufek.pdf>.
[22 June 2018].
Mandelbrot, B., 1985. Self-affine fractals and fractal dimension. Physica Scripta.
1985;32:257-260. DOI: 10.1088/0031-8949/32/4/001.
Meyer-Brandis,  T.,  Tankov  P.,  2008.  Multifactor
jump-diffusion  models
of electricity prices. International Journal of Theoretical and Applied Finance, Vol.
11 (5) (2008), pp. 503-528. DOI: 10.1142/S0219024908004907.
Monteiro, C., Ramirez-Rosado, I., Fernandez-Jimenez, L., Conde, P., 2016. Short-
term  price  forecasting  models  based  on  artificial  neural  networks  for  intraday
sessions in the Iberian electricity market. Energies 9 (9).
Peng,  C.-K.,  Buldyrev,  S.V.,  Havlin,  S.,  Simons,  M.,  Stanley,  H.E.,  Goldberger,
A.L.,  1994.  Mosaic  Organization  of  DNA  nucleotides.  Physical  Review  E.
1994;49(2):1685. DOI: 10.1103/PhysRevE.49.1685.
Sewalt, M., De Jong, C., 2003. Negative Prices in Electricity Markets. Commodities
Now
<kyos.com/wp-
content/uploads/2016/10/Commodities-Now-Negative-prices-in-Electricity-
Markets.pdf>. [15 June 2019].
Schneider,  S.,  2011.  Power  spot  price  models  with  negative  prices.  The  Journal
of Energy Markets 4(4):77-102, December 2011, pp. 77–102.
Simonsen, I., 2003. Measuring anti-correlations in the Nordic electricity spot market
by  wavelets.  Physica  A:  Statistical Mechanics and its  Application,  322:597–606.
DOI: 10.1016/S0378-4371(02)01938-6.
Uniejeweski, B., Marcjasz, G., Weron, R., 2019. Understanding intraday electricity
markets:  Variable  selection  and  very  short-term  price  forecasting  using  LASSO.
International Journal of  Forecasting. DOI: 10.1016/j.ijforecast.2019.02.001.
Uniejewski, B., Weron, R., Ziel, F., 2017. Variance stabilizing transformations for
electricity spot price forecasting. IEEE Transactions on Power Systems, pp. (99):1-
1. DOI: 10.1109/TPWRS.2017.2734563.

74–77.  Available

2003),

from:

(June

pp.

43

Čurpek, J.: Time Evolution of Hurst Exponent: Czech Intraday Electricity Market Study

Uritskaya,  O.  Y.,  Uritsky,  V.  M.,  2015.  Predictability  of  price  movements
in deregulated  electricity  markets.  Available  from:    <arxiv.org/abs/1505.08117>.
[20 June 2019].
Weron,  R.,  Przybyłowicz, B.,  2000.  Hurst  analysis  of  electricity  price  dynamics.
Physica  A:  Statistical  Mechanics  and  its  Applications.  283.  462-468.  DOI:
10.1016/S0378-4371(00)00231-4

44

