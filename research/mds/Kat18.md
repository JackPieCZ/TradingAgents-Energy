The value of forecasts: Quantifying the economic gains of accurate quarter-hourly
electricity price forecasts
ChristopherKatha,*,1,FlorianZielb
aRWESupply&TradingGmbH,Altenessenerstr.27,45141Essen
bUniversityofDuisburg-Essen,HouseofEnergyMarketsandFinance
Abstract
We propose a multivariate elastic net regression forecast model for German quarter-hourly electricity spot markets. While the
literature is diverse on day-ahead prediction approaches, both the intraday continuous and intraday call-auction prices have not
been studied intensively with a clear focus on predictive power. Besides electricity price forecasting, we check for the impact
of early day-ahead (DA) EXAA prices on intraday forecasts. Another novelty of this paper is the complementary discussion of
economicbenefits. Apreciseestimationisworthlessifitcannotbeutilized. Weelaboratepossibletradingdecisionsbasedupon
our forecasting scheme and analyze their monetary effects. We find that even simple electricity trading strategies can lead to
substantialeconomicimpactifcombinedwithadecentforecastingtechnique.
Keywords: forecasting,portfolioanalysis,elasticnetregression,Markowitzportfolio,quarter-hourlyspotprices,electricityprice
forecast
1. Introduction this paper, Germany has three independent exchanges that al-
low trading on an early day-ahead basis up to half an hour
Germanyisanoutstandingexampleofmassiverenewableinte- before physical delivery. The opportunity to enter QH trades
grationwithintheEuropeanenergymarket.Politicallyinduced, startedinDecember2011withthefirst15-minutecontractsin
renewablegenerationcapacitieswereexpandedandtheirmar- continuousintradaymarketsandwasconsequentlyexpandedin
ketingsubsidized.ThisnotonlyaffectedtheGermanday-ahead SeptemberandDecember2014byEXAAquarter-hourlyday-
bid-stack but also caused exchanges and market participants ahead products and the EPEX intraday call auction. A more
likewisetosetthefocusonquarter-hourly(QH)considerations thoroughdiscussionoftheGermanspotmarketisprovidedby
fortheiroptimizationproceduresduetotheincreasingresidual Viehmann(2017).
volumes after hourly day-ahead bidding. For more informa- Unfortunately, academic attention is only recently focused
tion on the described renewables impact, the interested reader onlowertimeintervals. Discussionsofquarter-hourlyGerman
might refer to Hirth (2013); Paraschiv et al. (2014); Ketterer spot markets are rare. A good starting point is provided by
(2014); Würzburg et al. (2013). As a result of this ongoing Kiesel & Paraschiv (2017) who discuss the econometric char-
trend,marketplaceshaveadaptedtheirproductssothattheGer- acteristics of quarter-hourly EPEX intraday (ID) time series
manmarketfeaturesanotheruniquecharacteristic. Whileother and provide an analytical model approach. Märkle-Huß et al.
countriessuchastheNetherlandsorBelgiumdonotofferany (2018)evaluatemarketimpactsoftheintroductionof15-minute
possibility to trade QH products at the time of the writing of contracts and report price reductions in correlated hourly spot
markets. However,thecurrentliteraturelacksadecentdiscus-
∗Correspondingauthor sion of forecasting QH prices. Quarter-hourly trading appears
Emailaddresses:christopher.kath@rwe.com(ChristopherKatha,*,),
florian.ziel@uni-due.de(FlorianZielb) tobecrucial,butthereisnoparticularforecastingmodelavail-
1The findings, interpretations and conclusions expressed hereinafter are able. This statement equally counts for QH auctions as well
thoseoftheauthoranddonotnecessarilyreflecttheviewsofRWESupply
&TradingGmbH.
PreprintsubmittedtoEnergyEconomics(acceptedforpublicationinEnergyEconomics:06Oct2018) November22,2018
8102
voN
12
]TS.nif-q[
1v40680.1181:viXra

2
ascontinuousintradaytrading. Weaimtofillthisgapbypro- sult, EXAA volumes might only be transferred with explicitly
viding precise price estimations for both of these markets. To sold cross-border capacities or are implicitly regarded by ex-
achievethis,wewillconsiderthemostcurrentinputfactorsin change auctions. One feature only available with EXAA is
Germanspottradingtogetherwiththestatusquoinforecasting post-trading. The exchange platform allows for a second bid-
techniques. dingroundwithknownpricestomarketasurplusoneitherthe
Another aspect that must not be ignored in this context is buy or sell side. EXAA trading only occurs on non-holiday
theeconomiceffectofanestimationscheme.
Ontheonehand, weekdays. All weekend or holiday prices are determined in
many forecasting models exist, at least for hourly day-ahead advance on the last weekday before the holiday or weekend.
applications (see Weron (2014) for a broader discussion), on Therefore, we already have a QH indication for delivery date
the other hand, the majority of these limit their scope to the Sunday on Friday, for instance. The next and
evaluationofaccuracybutneglecttheaspectofeconomicben- presumablymost
efits. Eventhemostaccuratepredictionhasnopracticalvalue importanttrading
|     |     |     |     |     |     |     |     |     |     |     | Exchange |     | tradedvolume[TWh] |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ----------------- | --- |
ifdoneinamarketoratapointintimewherenopossibilityof opportunityispro-
|     |     |     |     |     |     |     |     |     |     |     |     |     | 2015 | 2016 2017 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --------- |
autilizationexists. Therefore,oursecondcontributionshallbe videdbytheGer-
|     |     |     |     |     |     |     |     |     |     |     | EPEXDAauction |     | 264 | 235 233 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | ------- |
aquantificationofattainablegainsthroughpreciseforecastsin man EPEX day- EXAADAauction 8.2 8.0 5.4
| QHspotmarkets. |     |     |     |     |     |     |     | ahead (DA) | auc- |     | EPEXQHauction |     | 3.9 | 4.6 5.2 |
| -------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | --- | ------------- | --- | --- | ------- |
The rest of this paper is divided into the following sub- tion. A single EPEXQHID 3.9 3.6 4.9
sections: Section2introducesavailableGermanQHspotmar- biddingroundwith
|     |     |     |     |     |     |     |     |     |     | Table | 1: Yearly | volumes | of hourly | and quarter- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --------- | ------- | --------- | ------------ |
ketsandhighlightstheirpeculiarities,followedbysection3dis- results available
hourlyGermanspotexchanges.Allintradayfigures
cussing the connected forecast methodology. This comprises at12:42ammarks only entail data on Germany, while the day-ahead
auctionincludesAustriaandLuxembourg.
themodelinputparameters,necessarydatatransformationsand theprimarilytraded
theoverallestimationalgorithm. Section4addressesthefore- marketquotationintheday-aheadmarket. Atthetimeofwrit-
castperformanceinourempiricalstudyandtheassociatedeco- ing,theterm’EPEXday-ahead’correctlyspecifiestheGerman
nomiceffectsofourpricepredictionsfollowedbyaconclusion
|     |     |     |     |     |     |     |     | hourlyday-aheadexchange. |     |     | Still,theotherexchanges,EXAA |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | ---------------------------- | --- | --- | --- |
andashortoutlookonfurtherexpansionsinsection5. and Nord Pool Spot, are expanding their activities to the Ger-
|     |     |     |     |     |     |     |     | man day-ahead | market.   |     | It is planned |       | to unbundle | the pricing |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | --- | ------------- | ----- | ----------- | ----------- |
|     |     |     |     |     |     |     |     | algorithm     | from EPEX |     | such that     | three | independent | exchanges   |
2. Quarter-hourlytradinganditsrelevanceinGermany
offeraccesstothepricethatishereinafterreferredtoas’EPEX
|     |     |     |     |     |     |     |     | day-ahead’. | We  | stick to | that notation |     | to be in | line with other |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------- | ------------- | --- | -------- | --------------- |
offers
Germany a wide variety of possible trading venues for literatureandduetothefactthatthesechangesareplannedbut
marketparticipants.Othercountriesusuallyexhibitaday-ahead havenotbeenimplementedyet.
spotexchangeandcontinuousintradaytradingplatforms.These Duetorisingrenewablesinfeedandthenecessitytobalance
are also to be found for the four German grid areas, but be- quarter-hourly deviations, EPEX launched a second auction
| sides them, | there   | are     | two other | auctions, | as       | depicted | in Fig- |                   |     |             |     |       |          |                 |
| ----------- | ------- | ------- | --------- | --------- | -------- | -------- | ------- | ----------------- | --- | ----------- | --- | ----- | -------- | --------------- |
|             |         |         |           |           |          |          |         | for quarter-hours |     | in December |     | 2014. | Strictly | chronologically |
| ure 1. Spot | trading | ideally | starts    | with      | the EXAA | (Energy  | Ex-     |                   |     |             |     |       |          |                 |
speakingittakesplaceday-ahead,neverthelessitisreferredto
| change | Austria) | at 10:12am |     | for final | bid submission. |     | Only 8 |     |     |     |     |     |     |     |
| ------ | -------- | ---------- | --- | --------- | --------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
asanintradaycallauctionbecausetheday-aheadmarketwin-
minuteslater,theEXAApublishesthefirstday-aheadexchange
|     |     |     |     |     |     |     |     | dow ends | at d-1, | 14:30pm | for | grid operators, |     | as depicted by |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ------- | --- | --------------- | --- | -------------- |
traded quotation for the German delivery area. Although an thewhitelinesinFigure1. Whileallpriormarketplacesallow
Austrian exchange, EXAA results can easily be delivered into enteringasingleroundofbidsdeterminingthepricelevelina
Germanmarketareas.However,wemustacknowledgethatthis closed-formauction,ourlasttradingopportunity,theEPEXin-
situation could be of temporary character with ongoing talks tradaymarket,isacontinuousonethatistradableupto30min-
about splitting the German-Austrian bidding zone.2 As a re- utesbeforedelivery. ThisleadtimewaschangedperJuly2015
| 2As per | June 2018, | when | this paper | was finalized, |     | implementation | of a |     |     |     |     |     |     |     |
| ------- | ---------- | ---- | ---------- | -------------- | --- | -------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
Austriansplitareuncertainandignoredinthefollowing.
| marketsplithadnotbeenachieved. |     |     |     | Therefore,possibleeffectsofaGerman- |     |     |     |     |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

3
|     |     |     |     | D − 1 |     |     |     | Intraday |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | -------- | --- | --- |
Trading until 30 min
|     | 10:12 | 10:20 | 12:00 | 12:42 | 15:00 | 15:15 | 16:00 |     | Delivery |     |
| --- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | --- | -------- | --- |
before Delivery
Continuous
|     | EXAA DA  | EXAA  | EPEX DA  | EPEX DA  | EPEX QH | EPEX QH |     |     | Balancing  |     |
| --- | -------- | ----- | -------- | -------- | ------- | ------- | --- | --- | ---------- | --- |
close results  close results close results QH intraday  energy
market
Assumed forecast
time 14:30
Figure1: Spottradingtimelineanditsconnectedtradingvenues. Allmentioneddeadlinesareassumingusualcircumstanceswithnodelayedresults,technical
problemsandamarketclearingpricedeterminedinthefirstrunoftheunderlyingalgorithm. Pleasenotethattheintradayleadtimeof30minutesappliesfor
cross-gridtradesandlocaltradeswithinthesamegridareaarealloweduntil5minutesbeforedelivery.
from45to30minutes. Wewillconsiderthevolumeweighted 3. Forecastmethodology
| average | price | (VWAP) | of all transactions | for the specific | de- |     |     |     |     |     |
| ------- | ----- | ------ | ------------------- | ---------------- | --- | --- | --- | --- | --- | --- |
liveryquarter-hoursincecontinuoustradingactivitiesarediffi-
|                          |     |     |                                  |     |     | 3.1. Datatransformationandinputparameters |     |     |     |     |
| ------------------------ | --- | --- | -------------------------------- | --- | --- | ----------------------------------------- | --- | --- | --- | --- |
| culttoquantifyotherwise. |     |     | Lastbutnotleast,allopenpositions |     |     |                                           |     |     |     |     |
willbesettledbythegridoperatorsinthecourseofbalancing The price plots reveal price spikes and the occurrence of neg-
tariff
energy at the grid area independent imbalance (reBAP). ative prices. This is not a general problem but would usually
Since it is strictly forbidden by regulators to enter imbalance require either an explicit modeling of spikes by means of a
positions intentionally, this market is not a trading alternative price spike component, a spike-robust model or a transforma-
andisjustmentionedforthesakeofcomparability. tiontostabilizethevarianceofthetimeseries(Uniejewskietal.
Table 1 hints at the relevance of the different exchanges. (2018)).Wehavedecidedonthelatteraswedonotwanttogive
Theallocationofvolumespointstowardstheimmenseimpor- upthefeatureselectionabilitiesofourmodelsdiscussedlater.
| tanceofthehourlyEPEXDAauction. |     |     |     | ItoutrunstheQHtrad- |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
Oncetransformed,onecanuseawidersetofalgorithmswith-
| ing | venues | by far. This | phenomenon | might be explained | by  |                                    |     |     |                       |     |
| --- | ------ | ------------ | ---------- | ------------------ | --- | ---------------------------------- | --- | --- | --------------------- | --- |
|     |        |              |            |                    |     | outtakinggreatercareofpricespikes. |     |     | Wefirstlytransformand |     |
their purposes. As a result of missing liquidity, market play- theninversethedatasuchthattheoutputofourmodelsstillap-
ers are more likely trading residual positions in QH markets. pearsinarealisticformat. Thetransformationmainlysupports
The majority, i.e., the hourly demand and generation will be thealgorithmsbyprovidingamorestablevariancebutdoesnot
bid in the day-ahead exchange for which reason QH liquid- changeanycrucialinformation.
ity only accounts for 2% of the DA liquidity. Unfortunately, Ausualwaytotransformpriceseriesisthelogarithm.While
EXAAvolumesarereportedinanaggregatedformwithoutany a simple logarithmic transformation works in many different
separation into hourly or quarter-hourly amounts. Hence, the scenarios, our time series with negative values necessitates a
mentionedtradingvolumesonlyallowforaroughevaluationof
|             |     |         |                 |               |         | transformation   | method     | that can handle | negative | values. We         |
| ----------- | --- | ------- | --------------- | ------------- | ------- | ---------------- | ---------- | --------------- | -------- | ------------------ |
| importance. |     | The low | volumes suggest | that the EPEX | markets |                  |            |                 |          |                    |
|             |     |         |                 |               |         | stick to current | literature | findings to     | identify | the best transfor- |
aremoremomentouswhenGermanspottradingisconcerned. mation for our needs. In a large empirical study, Uniejewski
Whenever liquidity is limited, this could elicit high volatility et al. (2018) report superior RMSE-related performance for a
and price spikes. To detect such occurrences, we have plotted newlyproposedtransformationcalled’mlog’,whichweutilize
the price series in Figure 2. Both the QH auction and the on- for this paper. The authors especially propose the transforma-
going QH intraday trading can be highly volatile with prices tionforthespikesensitivemeasureRMSE(root-mean-square-
under0€/MWhorabove100€/MWh. While,ingeneral,both error)3whichmakessensetoapplytohighlyvolatiletimeseries
timeseriesappeartofollowsimilartrends,theintradayequiv- suchasourintradayone.Themlogtransformationshowedcon-
| alentseemstofeaturemorespikes. |     |     |     | However,thiseffectisnot |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
stantresultsacrossallmarkets,whichiswhywedecidedtouse
| predominant. |     | Theoverallpicturereflectstworesemblantprice |     |     |     |     |     |     |     |     |
| ------------ | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
quotations. 3Pleaserefertosection4.1forthemathematicalformulationofRMSE.

| 3.1 Datatransformationandinputparameters |     |     |     |     |     |     | 4   |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Training
]hWM/RUE[ ecirP 051
| a)EPEX QH call auction | Forecast |     |     |     |     |     |     |
| ---------------------- | -------- | --- | --- | --- | --- | --- | --- |
0
| 0   | 08.10.2015 - 06.10.2016 |     | 07.10.2016 - 31.05.2018 |     |     |     |     |
| --- | ----------------------- | --- | ----------------------- | --- | --- | --- | --- |
2
| 051 | Training |     |         out-of-sample |     |     |     |     |
| --- | -------- | --- | --------------------- | --- | --- | --- | --- |
]hWM/RUE[ ecirP 05
Forecast
0
0 0
1
05−
05
| 0   | 2016 | 2017 |     |     | 2018 |     |     |
| --- | ---- | ---- | --- | --- | ---- | --- | --- |
05−
Delivery date [08.10.2015−31.05.2018]
|     | 2016 | 2017 |     |     | 2018 |     |     |
| --- | ---- | ---- | --- | --- | ---- | --- | --- |
Delivery date [08.10.2015−31.05.2018]
bb)) EEPPEEXX  IIDD  ccoonnttiinnuuoouuss  QQHH  VVWWAAPP
0
0
| 2                   | 08.10.2015 - 06.10.2016 |     | 07.10.2016 - 31.05.2018 |     |     |     |     |
| ------------------- | ----------------------- | --- | ----------------------- | --- | --- | --- | --- |
| ]hWM/RUE[ ecirP 051 |                         |     |         out-of-sample   |     |     |     |     |
b) EPEX ID continuous QH VWAP
0
0
| 1                      | 08.10.2015 - 06.10.2016 |     | 07.10.2016 - 31.05.2018 |     |     |     |     |
| ---------------------- | ----------------------- | --- | ----------------------- | --- | --- | --- | --- |
| ]hWM/RUE[ ecirP 051 05 |                         |     |         out-of-sample   |     |     |     |     |
0
05−
05
| 0   | 2016 | 2017 |     |     | 2018 |     |     |
| --- | ---- | ---- | --- | --- | ---- | --- | --- |
05−
Delivery date [08.10.2015−31.05.2018]
|     | 2016 | 2017 |     |     | 2018 |     |     |
| --- | ---- | ---- | --- | --- | ---- | --- | --- |
Figure2:PriceplotoftheEPEXintradayQHauctionandEPEXintradaycontinuouspriceregimeseparatedintotrainingandforecastsections.Thebluepartition
markstheinitialtrainingandparameterizationperiodthatisconsequentlyshiftedwitheachiterationoftherollingestimation.Theredlinedepictstheout-of-sample
Delivery date [08.10.2015−31.05.2018]
datathatourpredictionmodelstrytoforecast.
itforourtimeseriesandmarkets. Beforeitsactualprocessing, plicate hour as well as a missing value. We follow Weron
thedatarequiresnormalization. Hence,theoriginaltimeseries (2007)andaveragetheduplicativehour. Itsomittedequivalent
x isadjustedto z = 1 (x −median) inwhichMAD iscalculatedusingmultipleimputationsaspresentedinBuuren
| qh,t | qh,t MAD qh,t |     |     |     |     |     |     |
| ---- | ------------- | --- | --- | --- | --- | --- | --- |
describes the median absolute deviation (MAD). Both MAD &Groothuis-Oudshoorn(2011)sothateverydayintheempir-
andmedianarecalculatedfor x overtheentireperiod. We ical test consists of 96 QHs. We also apply this approach to
qh,t
purposely introduce a neutral time series notation x since allothergapsinthetimeseries. Apartfromthat,nomorepre-
qh,t
thetransformationprocedureisnotonlyexecutedonpricesbut processing is carried out. We neglect all outlier effects in our
onalsootherexternalfactorslikeloadorwind. Oncethedata estimation scenario and leave extreme values untouched. Our
isnormalized, itstransformation y qh,t isgivenby(takenfrom empirical sample ranges from 08.10.2015 to 31.05.2018. In-
structionsonhowtoobtainthedifferentdataseriesareprovided
Uniejewskietal.(2018))
|     |     | inTable2. | Asolelyautoregressiveapproachisnotdesirableas |     |     |     |     |
| --- | --- | --------- | --------------------------------------------- | --- | --- | --- | --- |
(cid:20) (cid:21)
(cid:12) (cid:12) 1
y = sgn(z ) log( (cid:12)z (cid:12) + )+log(c) , (1) manypaperssuggesttheinfluencethatexternalfactorshave.
| qh,t | qh,t qh,t c |     |     |     |     |     |     |
| ---- | ----------- | --- | --- | --- | --- | --- | --- |
Weaimtokeepthemodelsimpleandeasilyreproducible
anditsinversefunction andonlyconsiderthemostcommonpubliclyavailableexternal
parameterslikethequarter-hourlyENTSO-Eloadforecast(e.g.
(cid:20) 1 (cid:21)
= |zqh,t |−log(c)−
z qh,t sgn(y qh,t ) e , (2) usedinKiesel&Paraschiv(2017))orwindpowerreportedby
c
|     |     | the | EEX transparency | platform | (see | Pape et | al. (2016); Aïd |
| --- | --- | --- | ---------------- | -------- | ---- | ------- | --------------- |
with c = 1 . ThisparameterwaslikewiseusedbyUniejewski
3 et al. (2016); Garnier & Madlener (2015) for models that in-
etal.(2018)andyieldedgoodresultsacrossseveralmarkets.
|     |     | clude | wind | infeed). The two | input factors | are | fundamentally |
| --- | --- | ----- | ---- | ---------------- | ------------- | --- | ------------- |
Thetimeseriesisaquarter-hourlyonewhichrendersaslight effects.
|                          |                                | driven | and might  | feature ramping   |       | For        | instance, morn- |
| ------------------------ | ------------------------------ | ------ | ---------- | ----------------- | ----- | ---------- | --------------- |
| transformationnecessary. | Daylightsavingtimecausesonedu- |        |            |                   |       |            |                 |
|                          |                                | ing    | times when | industrial shifts | begin | and people | are waking      |

3.1 Datatransformationandinputparameters 5
TSO Forecast
PV Production in MW
14000
Solar-enriched Predictions
12000 Non-Solar Non-Solar
10000 Prediction Model Prediction
8000
6000
4000
2000
0
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
Delivery Hour
Figure3:Averagedphotovoltaics(PV)productionforecastforGermanybasedonthepubliclyavailableTSOPVforecast.Pleasenotethatwehaveconsideredour
entiretimeseriesfrom01.10.2015to31.05.2018andaveragedacrossall24deliveryhoursinordertoanalyzeanydayandnighteffects.
upcause thegrid loadtoquickly increase, whereasits levelis decisiontoaddPVproductiondatatoallQHpredictionmodels
more likely to be stable around noon. We embrace these ef- from quarter-hours 29 to 76 and ignore PV entirely in case of
fectsforwindpowerproductionandloadbyregardingnotonly allotherquarter-hours.Wealsowanttocapturerampingeffects
theloadorwindinfeedforecastforaspecifichourbutalsothe asinwindandloadforecastsandconsidertheofficialTSOPV
forecast from one hour previous. Strong differences between infeedforecastfortherelevanthourtogetherwithitsequivalent
the two values might indicate ramping effects and can contain prediction one period before. Hence, our prediction approach
valuable information for our prediction model. Connected to accountsforramp-upsorramp-downsinPVproduction.
these inputs is the concern over hourly data. Some prices and Figure 1 is not strictly limited to quarter-hourly markets,
thewinddataarepresentinhourlyformatsonly.Theyaretrans- butif wedo so, three tradingopportunities remain: theEPEX
formedrathermodestlybyassumingthehourlyvaluesforevery QH auction, continuous intraday trading and the EXAA auc-
quarter-hour without any further processing. Since we do not tion which publishes results at 10:20am a day ahead. There-
knowanythingaboutthequarter-hourlyallocations,thisseems fore, the first quarter-hourly price information is delivered by
to be the most unbiased way to capture these effects. As for EXAA prices. Its information might be incorporated into a
wind, one might also find quarter-hourly forecasts by profes- forecastingschemefortheEPEXmarkets(seeZiel(2017)for
sionalproviders. WehavedeliberatelychosenthehourlyTSO this thought). Volume analysis has shown the importance of
data to ensure high reproducibility, but need to concede that EPEX hourly auction prices. Around noon, these prices mark
designatedvendordataincreasesforecastaccuracysinceitpro- thebenchmarkforanyspottradingactivities. Theyprovidean
videsmoreaccurateQHweatherdata. essential price indication for day-ahead trading. Possible im-
Speakingofweatherdata,onemustnotforgettheothercru- pactsonthismarketareexpectedtohaveapartialinfluenceon
cial component of the German fuel mix: Photovoltaics (PV) theintradaymarketaswell.
generation. A clear sign of its importance is that even the ex- Allexternaldeterminantsandtheirdatasourcesaresumma-
changeitselfmentionsPVinfeedasoneofthemajorreasonsfor rizedinTable2. Thecalculationsaremadeseparatelyforevery
the introduction of the QH auction in 2013 (see EPEX (2013) quarter-hour of the day. Such a method shrinks the size of all
for the press release). Märkle-Huß et al. (2018) support this matricesinthecalculationby96andreducesthecomputational
assessmentofimportancebystatingthatQHtradingismostly effortimmensely.Ontheotherhand,quarter-hourlyinterdepen-
driven by PV ramp-ups or -downs, i.e., times when PV pro- denciesevokedbyrampingcostsorsimilarloadeventsarelost.
duction quickly increases or decreases. However, a forecaster Traditionalthermalpowerplantshaveboundarieslikestart-up
needstobecarefulwithPVdata. Duringthenight,thetimese- times. Thesemightcauseonequarter-hourtobeprofoundlyaf-
riesfeaturesaconstantzeroduetonoproductionwhichmight fected by the preceding one. A principal component analysis
cause problems with prediction models. Figure 3 illustrates (PCA)acknowledgestheseeffectsin
how this effect is allocated over an entire day. The averaged
PV production only starts to remarkably differ from zero in a y h,t−1 (cid:118)Λ l,t F l,t , (3)
timeframebetweenhours8and19. Wehavemadetheexpert

| 3.1 Datatransformationandinputparameters |     |     |     |     |     |     |     |     |     | 6   |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Unit/granularity
| Determinant |     |     |     | Description |     |     | Datasource |     | Transformation |     |
| ----------- | --- | --- | --- | ----------- | --- | --- | ---------- | --- | -------------- | --- |
EPEXday-ahead EUR/MWh, MarketclearingpriceoftheEPEXday-ahead EuropeanPowerExchange mlog,hourly
auctionprice hourly auction,physicaldeliveryintoGermanorAustrian (EPEX), valueforallQHs
|     |     |     |     | gridpossible |     | https://www.epexspot.com/en/ |     |     |     |     |
| --- | --- | --- | --- | ------------ | --- | ---------------------------- | --- | --- | --- | --- |
EPEXintraday EUR/MWh, MarketclearingpriceoftheEPEXintradayauction, EuropeanPowerExchange mlog
auctionprice quarter-hourly physicaldeliveryintoGermangrid (EPEX),
https://www.epexspot.com/en/
EUR/MWh,
EPEXintraday Volumeweightedaverageofalltransactionsfor EuropeanPowerExchange mlog
VWAP quarter-hourly specificQH,physicaldeliveryintoGermangrid (EPEX),
https://www.epexspot.com/en/
EUR/MWh,
EXAA MarketclearingpriceoftheEXAAday-ahead EnergyExchangeAustria(EXAA), mlog
day-ahead quarter-hourly auction,physicaldeliveryintoGermanandAustrian http://www.exaa.at/en
| auctionprice |     |     |     | gridpossible |     |     |     |     |     |     |
| ------------ | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
ENTSO-E MW, Verticalsystemloadforbiddingzone EuropeanNetworkofTransmission mlog
loadforecast quarter-hourly Germany/Austria,publishedaround10:00d-1 SystemOperators(ENTSO-E),
https://transparency.entsoe.eu/
TSOPVforecast MW,hourly PhotovoltaicsinfeedforecastforGermanypublished EuropeanEnergyExchange(EEX), mlog,hourly
bytransmissionsystemoperators(TSO)at8:00d-1 https://www.eex-transparency.com/ valueforallQHs
TSOwind MW,hourly WindinfeedforecastforGermanypublishedby EuropeanEnergyExchange(EEX), mlog,hourly
forecast transmissionsystemoperators(TSO)at8:00d-1 https://www.eex-transparency.com/ valueforallQHs
Table2:Overviewofappliedexplanatoryvariables,theircharacteristicsandhowtoobtainthemforthesakeofreproducibility.
where Λ are the load factors and F the principal compo- tolocateasimilarloadday4 fromwhichtoextractprices. The
|     | l,t |     | l,t |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
nents of all 96 prices of today’s EXAA results, today’s EPEX identified price will serve as another input feature. We aim to
day-aheadresultandyesterday’slaggedpricesofthemarketto extractavectoroutofourfeaturematrixthatbestapproximates
| bepredicted. | Thecomponentsshallcomprisealldailypricein- |     |     |     |            |              |              |        |                     |     |
| ------------ | ------------------------------------------ | --- | --- | --- | ---------- | ------------ | ------------ | ------ | ------------------- | --- |
|              |                                            |     |     |     | the day to | be predicted | with regards | to its | Euclidean distance. |     |
formationandaredeterminedusingall96quarter-hours.Please
Inotherwords,theEuclideandistancebetweenthecurrentday
=
notethat l 1,...,96 because96quarter-hoursyield96com- andallhistoricalloadobservationsismeasured, andthemini-
ponents.WerunthePCAovertheEXAAandEPEXday-ahead mumisdetermined. Oncefound,thepricesofthemostsimilar
pricessincetheyarealreadyavailablearound10:21and12:42 loadscenarioarepluggedintothemodelassumingthattheyin-
the day ahead and might give a good indication of the most heritcrucialinformationaboutupcomingpricedevelopments.
currentpriceinterdependencies. IncaseofEPEXintradaycon- Regardingtiming,wedonotuseanyupdatedforecastdata,
tinuousforecasts,weaddaPCAonEPEXQHpricesbasedon i.e.,intradaypredictionsaremadeatthesamepointintimethat
the same argument and data availability. In addition, a forth the QH auction prices are being estimated even though their
PCAonlaggedpricestriestocaptureintradaydependenciesin
|                           |     |                           |     |     | computation | is not     | restricted to  | fixed auction     | times. This | is  |
| ------------------------- | --- | ------------------------- | --- | --- | ----------- | ---------- | -------------- | ----------------- | ----------- | --- |
| themarketsweaimtopredict. |     | AswithconventionalPCA,the |     |     |             |            |                |                   |             |     |
|                           |     |                           |     |     | essential   | because we | want to derive | a coinstantaneous | trading     |     |
firstfewfactorscomprisesufficientinformationtobeincluded.
decisionfromthepredictions,i.e.,enterpositionsinbothmar-
Inourcase,threecomponentsareutilized. ketsatthesametime. However,itleadstoasituationinwhich
WhiletheENTSO-Eloadforecastitselfisalreadyexpected we use the most current data only for the QH auction. It is a
to contain a good portion of price information, its connected trade-offforthesakeofpubliclyavailabledataandsimultane-
historical time series could deliver additional hints. Suppose ousapplicationsofbothforecaststocaptureeconomicbenefits.
thataspecificloadprofiledeterminestheshapeofquarter-hourly
| demand. | If we can identify | days with | a similar load | curve, |                                                                |     |     |     |     |        |
| ------- | ------------------ | --------- | -------------- | ------ | -------------------------------------------------------------- | --- | --- | --- | --- | ------ |
|         |                    |           |                |        | 4Foracorrectparameteridentification,theactualprocessistwofold. |     |     |     |     | First, |
theirobservablepricesprovidevaluableinputforourforecasts. thecalculusiscarriedoutforhistoricaldatatoretrievepastsamedaypricesfor
|     |     |     |     |     | modeltuning. | Inasecondphase,thedeterminationisdoneford+1tohavea |     |     |     |     |
| --- | --- | --- | --- | --- | ------------ | -------------------------------------------------- | --- | --- | --- | --- |
Thisideawasusedinacomparablepre-filteringset-upbyMa-
validinputparameterforaliveforecastofprices.
ciejowskaetal.(2016),oneofthewinningteamsinapricefore-
castingchallenge.Wewilllikewiseexploitthisthoughtandaim

3.2 Predictionmodel 7
3.2. Predictionmodel +β y +ε ,
(cid:32)q(cid:32)(cid:32)(cid:32)h(cid:32)(cid:32),(cid:32)3(cid:32)(cid:32)(cid:32)0(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)sim(cid:32)(cid:32)i(cid:32)l(cid:32)(cid:32)i(cid:32)a(cid:32)(cid:32)r(cid:32)(cid:32),(cid:32)q(cid:32)(cid:32)h(cid:32)(cid:32),t qh,t
(cid:124) (cid:123)(cid:122) (cid:125)
similarloadday
The aim is to predict both the EPEX quarter-hourly intraday
auction and the intraday continuous market price of the next with y beingthemlogpricesoftheidenticalquarter-hour
qh,t−k
day. Anequivalentmodelisutilizedforbothmarketswhichis one, two and seven days ago and y , y its equiv-
EXAA,qh DA,qh
why the following notations have a general character and are alent lags for the EXAA and EPEX day-ahead market. Obvi-
not restricted to one of the exchanges. Our deliberations start ously, the AR-term changes with the market to be predicted.
with a plain benchmark model, denoted as Naive in the The terms y and y refer to yesterday’s minimum
EXAA min,t−1 max,t−1
restofthispaper. Whilstinothermarketregimesthebestnaive andmaximummlogpriceandaresupposedtoreflectthenon-
guessisprovidedbyyesterday’sprice, theGermanmarketof- linear interdependency between the daily price regimes, while
fers an idiosyncrasy in the form of the EXAA auction and its φ ,...,φ arethewind,PVandloadforecastsforthere-
1,qh,t 6,qh,t
firstindicationforlaterauctionsandcontinuoustradingtofol- spectivedeliverydayanditslaggedvalues.Weusetheprevious
low. We exploit the EXAA results and expect them to be the hours’ lagged values to capture ramp-up effects of our funda-
bestestimatorfortheothermarketssuchthat yˆ =y . mental variables. The notation y describes prices of
qh,t EXAA,qh,t similar,qh,t
This model shall serve as an accuracy baseline for the other theminimumEuclideandistanceloadscenarioasmentionedin
forecastapproaches. theprevioussub-chapter,i.e.,pricesofadaythatfeatureasim-
Linear concepts tend to show convincing results in energy ilarloadprofilewithregardstotheEuclideandistancebetween
forecasting(seeMaciejowska&Nowotarski(2016)foranex- thecurrentloadforecastandallhistoricalones.
ample), which is why this paper sets the technical focus on Theterm D isadummyvariable(i.e.,takingavalueof1
k
them. Ofcoursewecouldhaveusedotherpredictors,likenon- incaseofoccurrence)tocapturetheintra-weektermstructure
linearones,buthavedecidedtothoroughlyintroducetheover- with m = 1,6,7 for Monday, Saturday and Sunday. Weekly
allmodelarchitectureinsteadofapplyingawidersetofmodels. seasonalityisacrucialfactorforspotelectricitypriceslikethe
Formoreinformationonothercommonforecastingapproaches onespresent(seealsoWeron&Misiorek(2008)foranexam-
andtheiraccuracyonemightrefertoGürtler&Paulsen(2018). ple on three weekly dummies). Saturday and Sunday differ
Withreferencetothedescribedinputfactors,weintroducetwo fromtherestoftheweekduetotheirweekendcharacteristics,
general regression approaches that serve as a basis for all up- with less traders being active and lower load and energy pro-
coming models. Our first input set, denoted by the prefix Ex- ductionlevels.Ourmarketsmightbetradedday-ahead,soeven
pert_,takesexpertdecisionsonweeklydummiesandlagsand Mondaycoulddifferfromtypicalweekdaysduetothefactthat
is described in the following simplified form exemplarily for quantities were traded on a Sunday. The argument certainly
y =EPEXquarter-hourlyauctionquotation holds true for the day-ahead traded QH auction and intraday
qh,t
continuous markets are at least partially traded one day in ad-
(cid:88)
y qh,t =β qh,0 + β (cid:32)q(cid:32)(cid:32)(cid:32)h(cid:32)(cid:32),(cid:32)i(cid:32) y q(cid:32)h(cid:32)(cid:32),(cid:32)(cid:32)t(cid:32)−(cid:32)(cid:32)j +β (cid:32)q(cid:32)(cid:32)(cid:32)h(cid:32)(cid:32),(cid:32)4(cid:32) φ 1(cid:32)(cid:32)(cid:32),(cid:32)q(cid:32)(cid:32)h(cid:32)(cid:32),t (4) vance. We therefore apply the set-up on both markets. The
j∈{1,2,7}(cid:124) (cid:123)(cid:122) (cid:125) (cid:124) (cid:123)(cid:122) (cid:125)
i=(1,...,3) AR-terms EEXwind notation PCA EXAA,l definesthe l−th principalcomponentof
+β φ +1 (qh)(β φ +β φ ) the EXAA QH prices. Besides EXAA, we include PCA’s for
(cid:32)q(cid:32)(cid:32)(cid:32)h(cid:32)(cid:32),(cid:32)5(cid:32)(cid:32)(cid:32)(cid:32) 2,(cid:32)q(cid:32)(cid:32)(cid:32)h(cid:32)(cid:32)−(cid:32)(cid:32)(cid:32)1(cid:32)(cid:32),t (29,...,76) (cid:32)(cid:32)(cid:32)(cid:32)q(cid:32)(cid:32)h(cid:32)(cid:32),(cid:32)6 (cid:32)3(cid:32)(cid:32)(cid:32),(cid:32)q(cid:32)(cid:32)h(cid:32)(cid:32),t (cid:32)q(cid:32)(cid:32)(cid:32)h(cid:32)(cid:32),(cid:32)7(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)4,q(cid:32)(cid:32)h(cid:32)(cid:32)(cid:32)−(cid:32)(cid:32)(cid:32)1(cid:32)(cid:32),(cid:32)t(cid:32)
(cid:124) (cid:123)(cid:122) (cid:125) (cid:124) (cid:123)(cid:122) (cid:125) (cid:124) (cid:123)(cid:122) (cid:125) EPEX QH and EPEX day-ahead prices. The error term ε
EEXwindlag EEXPV EEXPVlag h,t
(cid:88) (cid:88) is assumed to be independent and identically distributed (iid)
+ β (cid:32)q(cid:32)(cid:32)(cid:32)h(cid:32)(cid:32),(cid:32)(cid:32)7(cid:32)(cid:32)+(cid:32)(cid:32)(cid:32)i(cid:32)(cid:32) y D(cid:32)A(cid:32)(cid:32)(cid:32),(cid:32)q(cid:32)(cid:32)(cid:32)h(cid:32)(cid:32),(cid:32)t(cid:32)(cid:32)−(cid:32)(cid:32)k + β (cid:32)q(cid:32)(cid:32)(cid:32)h(cid:32)(cid:32),(cid:32)1(cid:32)(cid:32)(cid:32)1(cid:32)(cid:32)+(cid:32)(cid:32)(cid:32)i(cid:32)(cid:32) y (cid:32)(cid:32)EX(cid:32)A(cid:32)(cid:32)(cid:32)(cid:32)A(cid:32)(cid:32)(cid:32),(cid:32)(cid:32)q(cid:32)(cid:32)h(cid:32)(cid:32),(cid:32)(cid:32)t(cid:32)−(cid:32)(cid:32)k
k∈{0,1,2,7}(cid:124) (cid:123)(cid:122) (cid:125) k∈{0,1,2,7}(cid:124) (cid:123)(cid:122) (cid:125) with ε
h,t
∼ N(0,σ2
qh
). In case of EPEX intraday continuous
i=(1,...,4) EPEXDAlags i=(1,...,4) EXAAQHlags
prices we slightly expand Eq. (4) by adding its relevant auto-
+β y +β y +β φ +β φ
(cid:32)q(cid:32)(cid:32)(cid:32)h(cid:32)(cid:32),(cid:32)1(cid:32)(cid:32)(cid:32)6(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)m(cid:32)(cid:32)(cid:32)i(cid:32)(cid:32)n(cid:32)(cid:32),(cid:32)t(cid:32)(cid:32)−(cid:32)(cid:32)(cid:32)1(cid:32)(cid:32)(cid:32) (cid:32)(cid:32)(cid:32)(cid:32)(cid:32)q(cid:32)(cid:32)h(cid:32)(cid:32),(cid:32)(cid:32)1(cid:32)(cid:32)7(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)m(cid:32)(cid:32)(cid:32)(cid:32)a(cid:32)(cid:32)x(cid:32)(cid:32),(cid:32)t(cid:32)(cid:32)−(cid:32)(cid:32)1 (cid:32)q(cid:32)(cid:32)(cid:32)h(cid:32)(cid:32),(cid:32)1(cid:32)(cid:32)8 (cid:32)5(cid:32)(cid:32)(cid:32),(cid:32)q(cid:32)(cid:32)h(cid:32)(cid:32),t (cid:32)q(cid:32)(cid:32)(cid:32)h(cid:32)(cid:32),(cid:32)1(cid:32)(cid:32)(cid:32)9(cid:32)(cid:32) 6(cid:32),(cid:32)q(cid:32)(cid:32)(cid:32)h(cid:32)(cid:32)−(cid:32)(cid:32)(cid:32)1(cid:32)(cid:32),t regressivelags, thecurrentEPEXQHauctionpriceaswellas
(cid:124) (cid:123)(cid:122) (cid:125) (cid:124) (cid:123)(cid:122) (cid:125) (cid:124) (cid:123)(cid:122) (cid:125)
non-lineareffects ENTSOload ENTSOloadlag a PCA on the intraday continuous prices. They are available
(cid:88) (cid:88)
+ β (cid:32)q(cid:32)(cid:32)(cid:32)h(cid:32)(cid:32),(cid:32)(cid:32)1(cid:32)(cid:32)9(cid:32)(cid:32)+(cid:32)(cid:32)(cid:32)i(cid:32)(cid:32) P (cid:32)(cid:32) C (cid:32) A (cid:32)(cid:32)(cid:32)(cid:32)(cid:32)E(cid:32)(cid:32)(cid:32)X(cid:32)(cid:32)(cid:32)(cid:32)A(cid:32)(cid:32)(cid:32)A(cid:32)(cid:32)(cid:32),l + β (cid:32)q(cid:32)(cid:32)(cid:32)h(cid:32)(cid:32),(cid:32)2(cid:32)(cid:32)(cid:32)2(cid:32)(cid:32)+(cid:32)(cid:32)(cid:32)i(cid:32)(cid:32) P (cid:32)(cid:32)(cid:32)(cid:32) C (cid:32) A (cid:32)(cid:32)(cid:32)E(cid:32)(cid:32)(cid:32)P(cid:32)(cid:32)(cid:32)E(cid:32)(cid:32)X(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)D(cid:32)(cid:32)(cid:32)A(cid:32)(cid:32)(cid:32),l before the continuous trading window starts so it makes sense
l=(1,...,3) (cid:124) (cid:123)(cid:122) (cid:125) l=(1,...,3) (cid:124) (cid:123)(cid:122) (cid:125)
i=(1,...,3) dailyPCAfactors i=(1,...,3) dailyPCAfactors to exploit them for forecasting models. Please note that our
(cid:88) (cid:88)
+ β (cid:32)q(cid:32)(cid:32)(cid:32)h(cid:32)(cid:32),(cid:32)2(cid:32)(cid:32)(cid:32)5(cid:32)(cid:32)+(cid:32)(cid:32)(cid:32)i(cid:32)(cid:32) P (cid:32)(cid:32)(cid:32)(cid:32) C (cid:32) A (cid:32)(cid:32)(cid:32)E(cid:32)(cid:32)(cid:32)P(cid:32)(cid:32)E(cid:32)(cid:32)(cid:32)X(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)Q(cid:32)(cid:32)(cid:32)H(cid:32)(cid:32)(cid:32),l + β (cid:32)q(cid:32)(cid:32)(cid:32)h(cid:32)(cid:32),(cid:32)2(cid:32)9+(cid:32)i(cid:32)(cid:32) D (cid:32)(cid:32)(cid:32)(cid:32)(cid:32)m modelinEq. (4)isamultivariateonemeaningthatwehavean
l=(1,...,3) (cid:124) (cid:123)(cid:122) (cid:125) m={1,6,7}(cid:124) (cid:123)(cid:122) (cid:125) independentestimationperquarter-houror,inotherwords,96
i=(1,...,3) dailyPCAfactors i=(1,...,3)dailydummies

3.2 Predictionmodel 8
autarkicmodels. regressionform
Usingexpertdecisionsinevitablymeanssubjectivityandleaves
p
(cid:88)
roomforcriticism. WeincludeasecondinputsetcalledFull_ y = β x +ε . (5)
qh,t qh,t,j qh,t,j qh,t
thatovercomesallconcernsoverpossiblebias.Insteadofweek- j=1
days for Monday, Saturday and Sunday the full model imple-
The OLS optimization aims to minimize the residual sum of
ments dummies for every day of the week (such that m =
squares(RSS).Theelasticnetestimatorexpandsthisapproach
1,...,7) in equation (4). It also includes all 7 lags for every
byaddingalinearpenaltyfactor λ ≥0 in
qh
quarter-hourly price compared to the expert model only using
 
lag1,2and7. LastlythefullmodelreplacesallPCA’swith96
p
an
ri
d
ce
-
s
in
pe
c
r
as
q
e
ua
o
r
f
te
t
r
h
-
e
ho
in
u
t
r
r
f
a
o
d
r
a
E
y
X
co
A
n
A
ti
,
n
E
u
P
ou
E
s
X
p
Q
ri
H
ce
,
s
E
t
P
o
E
b
X
e
d
p
a
re
y
d
-a
ic
h
t
e
e
a
d
d
- βˆ EN =argmin

RSS +λ qh

 1− 2 α(cid:88)
p
β2 qh,j +α (cid:88)
p
(cid:12) (cid:12)β qh,j (cid:12) (cid:12)



,
forEPEXintraday. Thisexpansioncausesthemodelstructure
β qh 
(cid:124)
(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)
j
(cid:32)
=
(cid:32)(cid:32)(cid:32)
1
(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)
(cid:123)(cid:122)
(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)
j
(cid:32)
=
(cid:32)(cid:32)(cid:32)
1
(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)
(cid:125)

PenaltyTerm
to be much more complex than before. The full model fea-
(6)
tures254predictorsincaseofQHauctionpredictionsandover
T p
300forintradaycontinuousforecasts.Suchanexpansivemodel (cid:88) (cid:88)
whereRSS= (y − β x )2.
qh,t qh,j qh,t,j
might serve as a sensitivity check. If our expert decisions are
t=1 j=1
correct,thanthemodelsshallresultinsimilaraccuracy.
Incaseof λ = 0 weobtainthesameresultsasfortheOLS-
The β parametersinEq. (4)aredeterminedbythe qh
qh,1,...,30
basedLMmodel. Theotherextremecase λ →∞ causesall
well-known ordinary least squares (OLS) optimization in our qh
variablestobeshrunkentozero,i.e.,removedfromthemodel
firstmodel,leadingtotheestimatorcalledLMhereinafter.One
or tending to zero depending on the weighting between lasso
of the key points of this paper is an evaluation of the ideas in
and ridge regression. The allocation between ridge and lasso
Ziel et al. (2015) and Ziel (2017). Does the EXAA price add
is described by the parameter α∈[0,1]. We follow the find-
accuracygainsinQHmarkets? Weintroduceasecondmodel,
LM withoneslightdifferencetoEq. (4). Allparameters ings of an empirical study in Uniejewski et al. (2016) and set
EXAA,
α = 0.5 assubjectiveexpertdecision,thatisjustifiedbygood
remainunchangedforthepredictionofbothintradayandauc-
predictiveperformancereportedintheliterature.Theoptimiza-
tionmarkets,butweaddtheEXAAquarter-hourlyauctionre-
tionitselfmightbeseenasatrade-offbetweenminimizingthe
sultsasanotherexplanatoryvariable. Thesourcesabovefound
RSS and simplifying the model structure. Besides, an elastic
evidenceforaccuracygainsonceEXAApriceswereincluded,
netisaformofvariableselectionduetoitsabilitytocancelout
whichiswhyweexpectthemtoenhanceourmodelsinasimi-
entireinputfactors. Aregularizationmethodsuchastheelas-
larfashion.
tic net urgently necessitates normalization and standardization
Another concern indirectly arises from Eq. (4). We use a
to yield valid results. The penalty term works by both scale
large set of input factors where many features are assumed to
and magnitude of the variables while we desire a sparse solu-
becorrelated.WeapplyaPCAbutincludeaselectionoflagged
tion based solely on the individual magnitude. However, the
valueswhichareagaininputsforthePCA.Hence,highcorre-
topic of standardization is of no concern in our context since
lationinourpredictorsneedstobetakenintoaccounttogether
the mlog transformation explicitly regards this aspect. Please
withthefactthattoomanyvariablescouldcauseoverfitting. A
notethatincaseofstandardizationthereisnonecessityforan
secondlinearpredictionmodel,denotedasEN,shallovercome
interceptanymorewhichiswhythereisnoneinEq. (4).
thislimitation. IntroducedinZou&Hastie(2005),elasticnets
Equation (6) leaves an optimization problem to be solved.
(EN) balance between linear and quadratic penalty factors or
WecomputeasolutionusingR’sglmnetpackagebyFriedman
betweenlassoandridgeregression. Itsgreatadvantageisthat
et al. (2010). The optimization computation requires a mea-
it combines aspects out of the latter two algorithms, such that
suretobeminimized,andinourcasethatisthemeansquared
elastic nets can automatically remove unneeded variables en-
error(MSE).Basedonauser-specifiednumberof1,000differ-
tirelyfromthemodelwhilealsobeingmorerobusttocorrela-
entstepsfor λ ,glmnetautomaticallycreatesanexponential
tion than the lasso. We simplify the model in Eq. (4) to the qh

9
| grid starting | from | λ = | 0.001 | to a data-derived |     | maximum | per |     |     |     |     |     |     |     |     |
| ------------- | ---- | --- | ----- | ----------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
eachquarter-houranddeterminesthebestvaluebasedona10- EPEX QH auction EPEX ID continuous
|                       |     |                                    |     |     |     |     |     | Model        | RMSE |      | MAE |     | RMSE  | MAE |      |
| --------------------- | --- | ---------------------------------- | --- | --- | --- | --- | --- | ------------ | ---- | ---- | --- | --- | ----- | --- | ---- |
| foldcross-validation. |     | Despitebeingmoretimeintensivethana |     |     |     |     |     |              |      |      |     |     |       |     |      |
|                       |     |                                    |     |     |     |     |     | Expert_Naive |      | 7.85 |     | 4.9 | 12.81 |     | 8.64 |
EXAA
simple optimization, our cross-validation set-up provides gen- Expert_LM 7.09 4.26 12.11 7.88
|             |      |         |        |          |     |           |          | Expert_EN |     | 6.31 |     | 3.76 | 11.58 |     | 7.55 |
| ----------- | ---- | ------- | ------ | -------- | --- | --------- | -------- | --------- | --- | ---- | --- | ---- | ----- | --- | ---- |
| eralization | with | regards | to the | selected | λ . | Just like | the pre- |           |     |      |     |      |       |     |      |
qh
|     |     |     |     |     |     |     |     | Expert_LM | EXAA | 6.91 |     | 4.17 | 12.19 |     | 7.95 |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---- | ---- | --- | ---- | ----- | --- | ---- |
vious OLS model, a second predictor EN EXAA comprises the Expert_EN 6.12 3.65 11.58 7.55
EXAA
|     |     |     |     |     |     |     |     | Full_LM |     | 10.28 |     | 7.04 |     | 215 | 13.41 |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ----- | --- | ---- | --- | --- | ----- |
quarter-hourlyEXAAquotationsofthedeliverydate.
|     |     |     |     |     |     |     |     | Full_EN |      |       | 5.9 | 3.62  |           | 11.6     | 7.53 |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---- | ----- | --- | ----- | --------- | -------- | ---- |
|     |     |     |     |     |     |     |     | Full_LM | EXAA | 16.16 |     | 11.06 | over 1000 | over 100 |      |
|     |     |     |     |     |     |     |     | Full_EN |      | 6.02  |     | 3.67  | 11.61     |          | 7.54 |
EXAA
4. Back-testresults
|     |     |     |     |     |     |     |     | Table3: Errormeasuresroot-mean-square-error(RMSE)andmean-absolute- |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
4.1. Pointforecastperformance error(MAE)forappliedforecastmodels.
Beforeturningtheattentiontoeconomicgainsstemmingfrom thatseparatedtheLMandthenaivemodelforbothRMSEand
accurateforecasts,thepredictiveperformanceofourmodelsin MAE.Givenourrangeofauctiondata,advancedlinearmodel-
questionrequiresdiscussion. Rollingestimationsassurerealis- ingseemstoaddacrucialportionofperformance.Interestingly,
tic simulation results. Hence, every model is iteratively fitted ourchoiceofexpertdecisionwasnotentirelycorrectsincethe
and predicts on new data, while afterward the entire data ma- full models feature lower MAE and RMSE values. However,
|                 |     |                      |     |      |       |          |     | thisisnotthecasewithLMmodels. |     |     |     | Asexpected,theycannot |     |     |     |
| --------------- | --- | -------------------- | --- | ---- | ----- | -------- | --- | ----------------------------- | --- | --- | --- | --------------------- | --- | --- | --- |
| trix is shifted |     | by 96 quarter-hours. |     | This | modus | operandi | en- |                               |     |     |     |                       |     |     |     |
handlethemassivesetofinputsandfeaturethehighestRMSE
| sures that | all predictions |     | are | made on | out-of-sample |     | data and |     |     |     |     |     |     |     |     |
| ---------- | --------------- | --- | --- | ------- | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
andMAEresultswhenenrichedwithallinputs.
| reflectsrealisticbehaviorinpracticalapplications. |     |     |     |     |     | Wetrainour |     |     |     |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Atthesametime,theEXAAasamodelinputleavestheim-
| model with | nearly | one | year of | data so | that | a period | spanning |     |     |     |     |     |     |     |     |
| ---------- | ------ | --- | ------- | ------- | ---- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
from 08.10.2015 to 06.10.2016 is utilized for the initial train- pressionofminorimportance.EXAA-enrichedENmodelsout-
ing. From 07.10.2016 to 31.05.2017 all values are predicted performtheirrivalsbyaround3%fortheQHauctionifwecon-
sidertheRMSE.Still,thiseffecthasbeenexpectedtobehigher
inanout-of-samplemannersuchthatwehave57,714individ-
ually estimated quarter-hours to be evaluated in all upcoming andisonlylimitedtotheelasticnetthatcanhandlenumerous
tests. Giventhisvastamountofdata,webelievethetestresults inputfactors.ThecommonOLS-basedLMmodelratherseems
tobesound. to suffer from more inputs. The EXAA provides a quarter-
|              |        |              |                         |                |     |                |       | hourly quotation | for         | the same | delivery | date      | but    | only slightly |      |
| ------------ | ------ | ------------ | ----------------------- | -------------- | --- | -------------- | ----- | ---------------- | ----------- | -------- | -------- | --------- | ------ | ------------- | ---- |
| We report    |        | two commonly |                         | used measures, |     | the root-mean- |       |                  |             |          |          |           |        |               |      |
|              |        |              |                         |                |     |                |       | improves         | the models. | This     | could    | either be | caused | by the        | time |
| square-error | (RMSE) |              | and mean-absolute-error |                |     | (MAE),         | given |                  |             |          |          |           |        |               |      |
lagfromresultpublicationat10amtoEPEXbiddingat3pmor
by
(cid:118)
|     |     | (cid:117) |     |     |     |     |     | different |     |     |     |     |     |     |     |
| --- | --- | --------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
1 T 96 the intraday characteristics respectively. Indeed, one
|     | RMSE= | (cid:117) |      | (cid:88)(cid:88) |          |          |     |                                                   |     |     |     |     |     |     |     |
| --- | ----- | --------- | ---- | ---------------- | -------- | -------- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |       | (cid:116) |      | (y               | qh,t −yˆ | qh,t )2, | (7) |                                                   |     |     |     |     |     |     |     |
|     |       |           | 96 T |                  |          |          |     | mightarguethat5ormorehourscouldleadtonewwindfore- |     |     |     |     |     |     |     |
t=1 qh=1
|     |     |     |     |     |     |     |     | casts and | changed QH | bids. | Another | thought | is  | connected | to  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | ----- | ------- | ------- | --- | --------- | --- |
|     |     |     | T   | 96  |     |     |     |           |            |       |         |         |     |           |     |
1 (cid:88)(cid:88) (cid:12) (cid:12) t h e h o u rl y da y -a he ad a u c t io n . P re s um a b ly , m a rk e t p a rt i c ip a n ts
|         | MAE=      |     |        | ( (cid:12)y | −yˆ  | (cid:12)), | (8)      |                  |                |                |        |            |             |              |           |
| ------- | --------- | --- | ------ | ----------- | ---- | ---------- | -------- | ---------------- | -------------- | -------------- | ------ | ---------- | ----------- | ------------ | --------- |
|         |           | 96  | T      | qh,t        | qh,t |            |          |                  |                |                |        |            |             |              |           |
|         |           |     |        |             |      |            |          | w a it f o r     | t he m o st im | po r t a n t   | G e rm | a n sp o t | a u ct io n | u n t il t h | e y a c - |
|         |           |     | t=1    | qh=1        |      |            |          |                  |                |                |        |            |             |              |           |
|         |           |     |        |             |      |            |          | tively trade-out | their          | quarter-hourly |        | shapes.    | Thus,       | the          | EXAA      |
| where T | describes | the | number | of days,    | y    | the        | observed |                  |                |                |        |            |             |              |           |
qh,t
auctioncouldbecharacterizedbydifferentmarketplayersand
| prices and | yˆ  | its predicted |     | counterpart. | All | results | are re- |     |     |     |     |     |     |     |     |
| ---------- | --- | ------------- | --- | ------------ | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
qh,t
|                 |     |                                         |     |     |     |     |     | changing | bidding behavior. |     | However, | these | thoughts | require |     |
| --------------- | --- | --------------------------------------- | --- | --- | --- | --- | --- | -------- | ----------------- | --- | -------- | ----- | -------- | ------- | --- |
| portedinTable3. |     | Theysuggestthatthequarter-hourlyauction |     |     |     |     |     |          |                   |     |          |       |          |         |     |
quantitativebackinginfurtherresearch.
| indeed benefits |     | from forecasts |     | based | on external | factors | since |     |                 |      |     |      |            |          |     |
| --------------- | --- | -------------- | --- | ----- | ----------- | ------- | ----- | --- | --------------- | ---- | --- | ---- | ---------- | -------- | --- |
|                 |     |                |     |       |             |         |       | The | picture changes | with | the | EPEX | continuous | intraday |     |
thedifferencebetweenthebenchmarkmodelandthebestper-
|     |     |     |     |     |     |     |     | market. | The performance |     | is almost | two | times worse | than | QH  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------------- | --- | --------- | --- | ----------- | ---- | --- |
formingENestimatorismorethan20%intheRMSEcase.The
auctionresultsincaseofENpredictions.BothMAEandRMSE
| LM model         | is  | better than | the     | naive benchmark, |          | and      | the elas- |                  |        |     |          |              |     |     |         |
| ---------------- | --- | ----------- | ------- | ---------------- | -------- | -------- | --------- | ---------------- | ------ | --- | -------- | ------------ | --- | --- | ------- |
|                  |     |             |         |                  |          |          |           | are considerably | higher | for | intraday | estimations. |     | An  | initial |
| tic net approach |     | tops        | that by | roughly          | the same | accuracy | gain      |                  |        |     |          |              |     |     |         |

4.1 Pointforecastperformance 10
16 6
14
5
12
4
10
8 3
6 2
4
1
2
0 0
1 5 9 13 17 21 25 29 33 37 41 45 49 53 57 61 65 69 73 77 81 85 89 93 97
eulav
hq_EAM
/ hq_ESMR
hq_EAM
/
hq_ESMR
egnar
ledom
16 6
14
5
12
4
10
8 3
6
2
4
1
2
0 0
1 5 9 13 17 21 25 29 33 37 41 45 49 53 57 61 65 69 73 77 81 85 89 93
Delivery Quarter-hour
Range MAE_qh Range RMSE_qh best RMSE_qh model best MAE_qh model
eulav
hq_EAM
/ hq_ESMR
hq_EAM
/ hq_ESMR
egnar
ledom
a) EPEX QHauction
b) EPEX intraday continuous
Figure4: Quarter-hourlymodelfitmetricsMAE_qhandRMSE_qhandrangeofMAE_qhandRMSE_qhbetweenbestandworstmodel. Theplotislimitedto
thebestperformingmodelpermarket,incaseoftheQHauctionthatisFull_ENandfortheintradaycontinuousmarketitisExpert_EN.Pleasenotethatwehave
excludedFull_LMandFull_LMEXAAfromtheplotduetoitsunreasonablyhigherrormetrics.
guess might be that this observation is associated with even Figure 4 provides a graphical representation of the model
more substantial intra-model deviations. However, the results fit. Please note that we change eq. (7) and (8) to a quarter-
suggest a different outcome. The linear models only slightly hourly representation by adding the identically named suffix.
increasetheperformanceincomparisonwiththeusageofplain Itshowsthequarter-hourlytermstructureofthebestperform-
EXAApricesasapredictionmodelinput. Whereaselasticnet ing MAE_qh and RMSE_qh model as well as the range be-
outperforms the OLS-based predictor in QH auctions, its per- tween the best and worst performing model. It appears that
formancegainisonlymarginalintheintradayregime. Ourem- each hour’s last quarter-hour is harder to estimate with higher
piricaltestsuggeststhesameresultsforthequestionofEXAA RMSE_qhandMAE_qhresults. Thisresultsinacharacteristic
influencesonperformance.Anaccuracyincreaseofaround1% zig-zag pattern in both markets. Besides, the transition phase
does not support the argument of strong EXAA implications fromoff-peaktopeakbetweenhour7and8andhour20to21
in continuous intraday markets. The market itself features an isacommontimeofhigheruncertainty. Additionalplantsare
entirelydifferentpricingregimewhichtendstoeitherbemore rampeduptocovertradeablepeakprofiledemands. Theseef-
complicated in prediction or influenced by other parameters. fectsareobservableinhighererrormeasuresinFigure4. The
Besidesthat,thetimingaspectalsomatters. Allintradayfore- overallQHauction’serrorrangeisconstantbesidesthelastQH
casts exploit the same fundamental data that was used for the andoff-peak/peakchangesbuttheintradaycontinuousplotre-
QHauction. Updatedwindorloaddatacouldboostaccuracy. vealshighermodeldeviationsfortheentirepeaktime. Sothis
In terms of input factors our expert models are comparable to marketappearstobemoredifficulttopredictinpeakhours.
thefullmodelswithoneexception;whilethelinearmodelwas A more advanced test measure is delivered by Diebold &
alreadystrugglingforQHauctiondata,theintradaycontinuous Mariano(1995)intheeponymousDiebold-Mariano(DM)test
trading proves it to be unsuitable for large numbers of regres- statistics. Ithasproventobeaprofoundmeasurewithenergy
sors. Itserrormeasuresclearlyindicateamodelissueandun- pricingapplicationsinNowotarskietal.(2014)andBordignon
reasonablepointforecasts. et al. (2013) and aims at investigating the outperformance of

| 4.1 | Pointforecastperformance |     |     |     |     |     |                          |     |     |     |     |     |     |     | 11  |
| --- | ------------------------ | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
|     | DM test statistics       |     |     |     |     |     | a) Quarter-hourlyauction |     |     |     |     |     |     |     |     |
9
7
5
3
1
-1
-3
-5
|     | 1   | 8   | 15  |     | 22  | 29  | 36  | 43 50 | 57  | 64  | 71  |     | 78  | 85  | 92  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
b) Quarter-hourlyintraday market
9
7
5
3
1
-1
-3
-5
|     | 1   | 8   | 15  |     | 22  | 29  | 36  | 43 50 | 57  | 64  | 71  |     | 78  | 85  | 92  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
Quarter-hours
5% Significance Expert_EN Expert_LM Expert_ENEXAA Expert_LMEXAA
|     |     | Full_EN |     |     | Full_LM |     |     | Full_ENEXAA |     | Full_LMEXAA |     |     |     |     |     |
| --- | --- | ------- | --- | --- | ------- | --- | --- | ----------- | --- | ----------- | --- | --- | --- | --- | --- |
Figure5:Quarter-hourlyDiebold-MarianoteststatisticscarriedoutundertheabsolutelossfunctionandwithlossserieslaggedfourtimesdeterminedbyanAR(p)
process.
one model forecast over the other. The test input parameters to identify the most suitable lag order. In our case, an error
aregivenbythelossdifferentialseries Ωm1,m2 oftheabsolute series lagged four times appears to be statistically sound. The
qh,t
errorofmodels m ,m suchthat testitselfisperformedatthe5%significancelevelandreflects
|     |     | 1   | 2   |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
consistentoutperformanceagainstthenaivebenchmarkmodel.
|     |     | Ω m 1 , m2 =(cid:12) | (cid:12)ym 1 | −yˆm 1 | (cid:12) p (cid:12) (cid:12)ym 2 | −yˆm 2 (cid:12) p |     |     |     |     |     |     |     |     |     |
| --- | --- | -------------------- | ------------ | ------ | -------------------------------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:12) − (cid:12) . (9) Figure5providesagraphicalrepresentationoftheDMtest
|     |     | q h , t | qh ,t | qh ,t | qh  | ,t qh ,t |     |          |                                                    |     |     |     |     |     |     |
| --- | --- | ------- | ----- | ----- | --- | -------- | --- | -------- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |     |         |       |       |     |          |     | results. | Thehighertheteststatisticsforeveryquarter-hourare, |     |     |     |     |     |     |
p,thequadraticlossortheabso-
Dependingonthechoiceof
|                                     |         |          |           |     |            |     |              | the better | the    | model        | performs | in         | comparison | with     | the bench- |
| ----------------------------------- | ------- | -------- | --------- | --- | ---------- | --- | ------------ | ---------- | ------ | ------------ | -------- | ---------- | ---------- | -------- | ---------- |
| lute                                | loss is | applied. | Our tests | did | not reveal | any | considerable |            |        |              |          |            |            |          |            |
|                                     |         |          |           |     |            |     |              | mark       | model. | Furthermore, |          | all values | under      | or above | the dot-   |
| differenceinthetestresultsforeither |         |          |           |     | p=1        | p=2 |              |            |        |              |          |            |            |          |            |
|                                     |         |          |           |     |            | or  | whichis      |            |        |              |          |            |            |          |            |
tedgraylinedepictsignificantoverperfomanceorunderperfor-
| whywesticktotheformer. |     |     |     | Anessentialprerequisiteofthetest |     |     |     |                            |     |     |     |                           |     |     |     |
| ---------------------- | --- | --- | --- | -------------------------------- | --- | --- | --- | -------------------------- | --- | --- | --- | ------------------------- | --- | --- | --- |
|                        |     |     |     |                                  |     |     |     | manceoftherespectivemodel. |     |     |     | Bearingthisinmind,Figure5 |     |     |     |
isnon-covariancestationarityinerrorsasdiscussedinDiebold
|         |       |      |            |       |            |      |             | supportstheconclusiondrawnfromtheRMSEscores. |        |      |        |         |      |            | Nearly   |
| ------- | ----- | ---- | ---------- | ----- | ---------- | ---- | ----------- | -------------------------------------------- | ------ | ---- | ------ | ------- | ---- | ---------- | -------- |
| (2015). | Daily | test | statistics | might | contradict | this | postulation |                                              |        |      |        |         |      |            |          |
|         |       |      |            |       |            |      |             | all linear                                   | models | with | expert | choices | tend | to improve | forecast |
sinceallofthequarter-hoursaredrivenbythesamedailyfun-
|                                                   |         |          |        |                |           |             |             | accuracy | for     | the QH   | auction      | with      | the | EXAA-enriched | ones     |
| ------------------------------------------------- | ------- | -------- | ------ | -------------- | --------- | ----------- | ----------- | -------- | ------- | -------- | ------------ | --------- | --- | ------------- | -------- |
| damentaldriversasproposedbyNowotarskietal.(2016). |         |          |        |                |           |             |             | Our      |         |          |              |           |     |               |          |
|                                                   |         |          |        |                |           |             |             | better   | than    | non-EXAA | predictions, |           | and | EN estimates  | slightly |
| univariate                                        |         | approach | eludes | this           | matter by | its finer   | resolution. |          |         |          |              |           |     |               |          |
|                                                   |         |          |        |                |           |             |             | more     | precise | than     | its OLS      | opponent. |     | The LM models | show     |
| Another                                           | concern | arises   | from   | autoregressive |           | structures. |             | Since    |         |          |              |           |     |               |          |
significantlynegativeperformancecomparedtothebenchmark,
| we include |     | at least | three lags, | the | quarter-hours | and | their | con- |     |     |     |     |     |     |     |
| ---------- | --- | -------- | ----------- | --- | ------------- | --- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- |
whichagainhighlightstheirinabilitytodealwithlargeramounts
nected prices must be correlated. This issue is dealt with by suffer
|             |            |          |         |          |            |            |              | of regressors. |         | All                                  | models | seem       | to  | in the        | same period |
| ----------- | ---------- | -------- | ------- | -------- | ---------- | ---------- | ------------ | -------------- | ------- | ------------------------------------ | ------ | ---------- | --- | ------------- | ----------- |
| using       | lagged     | errors   | for Eq. | (9).     | We inspect | the        | partial      | auto-          |         |                                      |        |            |     |               |             |
|             |            |          |         |          |            |            |              | aroundQH36.    |         | WecanacknowledgethatEXAAslightlymat- |        |            |     |               |             |
| correlation |            | function | and fit | an AR(p) | process    | to         | the intraday |                |         |                                      |        |            |     |               |             |
|             |            |          |         |          |            |            |              | ters           | for the | QH auction                           | market | based      | on  | our empirical | study       |
| and         | QH auction | time     | series  | (see     | Ziel et    | al. (2015) | for the      | idea           |         |                                      |        |            |     |               |             |
|             |            |          |         |          |            |            |              | since          | DM      | statistics                           | are a  | bit higher | for | these models. | Still,      |
offittinganAR(p)processtotacklecorrelationintheDMtest)
|     |     |     |     |     |     |     |     | the effect | is  | very limited. |     | The differences |     | among | the contin- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------------- | --- | --------------- | --- | ----- | ----------- |

Economiceffectsofaccurateforecasts
| 4.2 |                |     |     |     |                                |     |     |     |     |     |     | 12  |
| --- | -------------- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|     | DA test value  |     |     |     | a) Directional accuracy test   |     |     |     |     |     |     |     |
0.7
| 0.65 |     |     |     |     |     | 50% Directional correctness |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- |
0.6
0.55
0.5
0.45
|     | 1 8                 | 15  | 22 29 | 36  | 43                               | 50  | 57  | 64 71 | 78  | 85  | 92  |     |
| --- | ------------------- | --- | ----- | --- | -------------------------------- | --- | --- | ----- | --- | --- | --- | --- |
|     | PT test statistics  |     |       |     | b) Pesaran and Timmermann test   |     |     |       |     |     |     |     |
6
|     | 4   |     |     |     |     | 5% Significance |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
2
0
-2
|     | 1 8 | 15  | 22 29 | 36  | 43  | 50  | 57  | 64 71 | 78  | 85  | 92  |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
Quarter-hour
Figure6: Directionalforecastevaluationsbasedona)DirectionalAccuracystatisticsandb)thePesaranandTimmermanntest. Theterm’directional’describes
whetherthesetofforecastsfortheEPEXQHauctionandIDcontinuousmarketiscapableofidentifyingthehighpriceandlowpricetradingvenue.
uousintradaymodelsarereasonablylow. VeryfewQHsshow ENandEN forouranalysisandintroduceadditionalport-
EXAA
tendenciesofstatisticalexcessperformance, andeveninthese folios, Base and Base . These will explicitly
|     |     |     |     |     |     |     | Sell_EXAA |     | Buy_EXAA |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | -------- | --- | --- | --- |
scenarios,itisdifficulttofavoraspecificmodel. Themajority includetheinformationprovidedbyEXAApricesjustasinthe
ofobservationsaretobefoundintherangebelow5%signifi- ENandLMforecastmodels.
cancemeaningneitherLM,ENorEXAAenrichmentleadsto Theaboveideanarrowsthedealdeterminationdowntoadi-
fewer errors compared to our benchmark. This outcome was rectionalforecastbasedonthehighandlowmarket. Therefore,
unanticipated but might again be due to the time lag between wewanttoelaboratethedirectionalaccuracyofourapproach.
estimationsandcontinuousintradaytradingactivities. The common measure (i.e., used in Moosa & Vaz (2015)) Di-
|     |     |     |     |     |     | rectional | Accuracy | (DAcc) | delivers the | first | hint of the | binary |
| --- | --- | --- | --- | --- | --- | --------- | -------- | ------ | ------------ | ----- | ----------- | ------ |
accuracyofourforecastsinadirectionalsettingandisdefined
4.2. Economiceffectsofaccurateforecasts
inalowmarket/highmarketapplicationas
4.2.1. Directionalforecastportfolioapproach
1(cid:88) n
DAcc=
|     |     |     |     |     |     |     |     |     | d   | ,   |     | (10) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
n qh,t
A single point forecast has limited value if considered sepa- i=1
| ratelywithoutatranslationintoatradingdecision. |     |     |     | Wewillin- |     |     |     |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
withtheconnectedhitseries
troducetwodifferentapproachesthatshallusetheforecastsas

aninputandtransformtheseintoaQHdeal. Buyingandsell- 1, if(yˆm1 >yˆm2)∧(ym1 >ym2)
|     |     |     |     |     |     |     | =   | qh,t | qh,t | qh,t | qh,t |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | ---- | ---- | --- |
ingareregardedindifferentportfoliostoreflectpossiblegains d qh,t (11)
|     |     |     |     |     |     |     |     | if(yˆm1 | <yˆm2)∧(ym1 |     | >ym2). |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | --- | ------ | --- |
0,
|         |                     |       |                    |     |         |     |     | qh,t | qh,t | qh,t | qh,t |     |
| ------- | ------------------- | ----- | ------------------ | --- | ------- | --- | --- | ---- | ---- | ---- | ---- | --- |
| for net | buyers and sellers. | Based | on these thoughts, | we  | firstly |     |     |      |      |      |      |     |
utilizebothpredictionsinasimplifiedbinaryscheme. Compa- Intuitively speaking, Eq. (11) assigns a value of 1 every time
niesneedtobuyorselltheirresidualquarter-hourlyspotprofile thehigherorlowermarketiscorrectlypredicted. Therepresen-
onspotexchangesandshalldosobasedonthesimpleruleof tation is kept general, but in our given case the model indices
buying in the cheaper market (low market) and selling in the m1, m2 denote either the EPEX QH auction or the QH in-
|      |                     |          |          |               |     | traday                                         | market. | Once we know | whether | the | prediction | of the |
| ---- | ------------------- | -------- | -------- | ------------- | --- | ---------------------------------------------- | ------- | ------------ | ------- | --- | ---------- | ------ |
| more | expensive one (high | market). | Hence, a | sell position | is  |                                                |         |              |         |     |            |        |
|      |                     |          |          |               |     | highermarketisrightorwrong,theDAccmeasureinEq. |         |              |         |     |            | (10)   |
enteredintothemarketwithhigherpredictedprices,denotedas
Base whiletheBase portfoliobuysinthelowerprojected reports the share of correct directional estimates. The second
| Sell, |     | Buy |     |     |     |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
market. Since the previous sub-chapter reflected an apparent frameworkisprovidedbyPesaran&Timmermann(1992)and
tendencytowardstheENpredictorsbeingthebest,weconsider supposesindependentdirectionsoftheobservedandpredicted

Economiceffectsofaccurateforecasts
| 4.2 |     |     |     |     |     |     |     |     |     |     |     |     |     | 13  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
realizationsunderthenullhypothesis,i.e.,thatestimateddirec- price movements leading to a return given by r =
traditional,qh,t
tionsdonotaddextraknowledge.Bothmetricswillbereported (y /y )−1. This notation makes sense for storable as-
|     |     |     |     |     |     |     |     | qh,t qh,t−1 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
quarter-hourlytogainadditionalinsightsintothetimestructure sets or long-term power contracts but does not apply to a spot
accuracyofthepredictions. marketexample. Long-termcontracts,likefutures,areusually
Figure6summarizesthefindingsinacombinedway. The settleddailyinamarginingprocesssuchthatonlythepricedif-
upperplotshowsthatusingtheindividualforecaststoestimate ference is paid or received. The same holds true for a stock
the cheaper or more expensive exchange leads to more than position. In spot markets, the daily position will most likely
bedifferentduetochangingoff-takeorpowerplantgeneration.
| 50% correctness |     | in most | cases. | In general, |     | this is a | promis- |     |     |     |     |     |     |     |
| --------------- | --- | ------- | ------ | ----------- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- |
Hence,theresultingcash-flowisdifferent.
ing finding since once we have a higher correctness rate than Aconsecutivetwo-
50%,thereisapossibilitytoobserveeconomicbenefits. How- daylongpositionof50MWwillnotjustbesettledattheprice
ever,thispostulationonlyholdstrueifthelossesofanincorrect delta between day one and day two (as done with futures and
predictionandthegainsofacorrectoneareequallydistributed daily margining), but a market participant has to pay 50 MW
suchthatthecostofmakingawrongpredictionisnearlyequal times the market price. Therefore, we will regard the price it-
tothebenefitofbeingcorrect. Ontheotherhand,weseeade- selfasthereturnleadingtoournotation r = y . Another
|     |     |     |     |     |     |     |     |     |     |     |     | qh,t | qh,t |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --- |
differenceisgivenbythedifferentiationintobuyandsellport-
| cline in | directional | accuracy |     | in the peak | QHs | ranging | roughly |     |     |     |     |     |     |     |
| -------- | ----------- | -------- | --- | ----------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
from quarter-hour 36 to 70. Our estimations seem to be more folios. Once we value a high return (or in our notation a high
off-peak
accurate in regimes given the dataset. This message clearing price) as desirable and optimize with regards to that,
is supported by the second metrics depicted in the lower part we will identify a sell portfolio because a market player obvi-
of Figure 6. The Pesaran and Timmermann (PT) test statis- ouslydemandshighpricesandhighreturns. Thebuyportfolio
tics exhibit an off-peak/peak pattern. The actual test score is is the inverse of the particular optimization result and yields
contradictory to the measure mentioned before. The majority lowerreturnsorlowerpricesfornetbuyersinthemarket.
of quarter-hours do not pass the test, meaning that we found Themean-variancetheoryincorporatesexpectedreturnsand
evidencethatthecorrectdirectionanditspredictedequivalent varianceintoanoptimizationframework.Individualassetsnum-
|     |     |     |     |     |     |     |     | i   | = 1,...,n |     |     |     | w   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
are less independent than desired. This outcome was unfore- bered by are weighted by a factor i,qh,t to com-
seen considering the results of the Directional Accuracy test. pose a portfolio of assets. In our concrete case, the portfolio
To conclude, the tests suggest a promising rate of correctness is restricted to two assets or the choice between the QH intra-
butdonotallowustorejectthenullhypothesisofautonomous day auction and continuous intraday trading. Unlike financial
directional errors. The forecast quality might be biased. Still, applications,wedonotincludeanyrisk-freebenchmarkassets.
we have to acknowledge that we only want to investigate the UsingourpricesassingletimeseriesreturnsintheMarkowitz
economicvalueofourpointforecastsandhavetranslatedthem senseleadstoaportfolioreturnin
| intoabinaryframework. |     |     | So, | theycouldbedistortedsincethe |     |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2
| basisisnotadesignateddirectionalestimation. |     |     |     |     |     |     |     |     |                |     | (cid:88) |        |     |      |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | ------ | --- | ---- |
|                                             |     |     |     |     |     |     |     |     | r              | =   | w        | y ,    |     | (12) |
|                                             |     |     |     |     |     |     |     |     | portfolio,qh,t |     | i,qh,t   | i,qh,t |     |      |
i=1
4.2.2. Mean-varianceportfolioselection where y i,qh,t aretherealizedvaluesforeithertheQHauctionor
|     |     |     |     |     |     |     |     | theintradaymarketand |     | w   | aretheconnectedweights. |     |     | Yet, |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ----------------------- | --- | --- | ---- |
i,qh,t
| A different                 | portfolio | composition |                                | technique | is  | given by | mean- |               |          |          |          |            |        |     |
| --------------------------- | --------- | ----------- | ------------------------------ | --------- | --- | -------- | ----- | ------------- | -------- | -------- | -------- | ---------- | ------ | --- |
|                             |           |             |                                |           |     |          |       | Eq. (12) only | provides | insights | into the | historical | return | and |
| varianceportfolioselection. |           |             | InitiallyintroducedinMarkowitz |           |     |          |       |               |          |          |          |            |        |     |
doesnotcompriseanyfuture-orientedquantification.Markowitz
(1952), itsclassicalscopecoversfinancialmarketsandthese-
|     |     |     |     |     |     |     |     | optimizationsrequireexpectedreturnsdenotedas |     |     |     |     | E(r | )   |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |
portfolio,qh,t
lectionofstocksunderexpectedreturnandvariance. However, whichinevitablynecessitatesexpectedsingle i-threturns,i.e.,
there are a few energy market applications of mean-variance E(r ) = E(y ) = µ . Instead of the traditional mean
|     |     |     |     |     |     |     |     | i,qh,t | i,qh,t | i,qh,t |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | ------ | --- | --- | --- | --- |
concepts available (the interested reader might refer to a re- formulation, we want to approximate the expected return by
cent review of this topic in Calvo-Silvosa et al. (2017)). To ∼yˆ
|             |     |            |     |              |     |               |     | meansofourforecastssothat |     |     | µ i,qh,t | i,qh,t . Pruningthenota- |     |     |
| ----------- | --- | ---------- | --- | ------------ | --- | ------------- | --- | ------------------------- | --- | --- | -------- | ------------------------ | --- | --- |
| apply such, | the | definition | of  | return needs | to  | be clarified. | Fi- |                           |     |     |          |                          |     |     |
tiontojustasingleweightingfactorandtakingintoconsidera-
nancialmarketsassumeafixedassetpositionwithpaymentsof

4.2 Economiceffectsofaccurateforecasts 14
Spread EPEX QH vs.
EPEX ID in EUR/MWh
2 Ø -Spreadof all quarter-hours:0.76EUR/MWh
0
1 11 21 31 41 51 61 71 81 91
-2
Delivery quarter-hour
Figure7: Quarter-hourlyspreadsofportfoliostrategyBaseSell_EXAA /BaseBuy_EXAA,i.e.,sellinthepredictedhighmarketandbuyinitslowerequivalent. The
marketsunderconsiderationarethecontinuousQHintradaymarketandtheEPEXQHintradaycallauction.
PortfolioID Description Price MinPrice MaxPrice Std.Dev Sharpe-
Ratio
soiloftropkramhcneB
NaiveEXAA EXAAQHtradingofresidualvolumes 34.95 -102.34 168.85 17.18 2.04
NaiveAUQH EPEXintradayQHauctiontradingofresuming 34.66 -134.82 290.65 19.15 1.81
position
NaiveIDQH EPEXintradayQHVWAPtradingofresidual 34.81 -241.83 329.81 20.27 1.72
position
NaivereBAP SettlementofresidualpositionatreBAPpricewith 34.74 -2558.42 24455.05 147.54 0.24
gridoperator
PerfectBuy Fullinformationbenchmarkportfolio,alwaysbuys 30.74 -241.83 166.42 19.40 1.58
inlowermarket
PerfectSell Fullinformationbenchmarkportfolio,alwayssellsin 38.73 -117.77 329.81 19.22 2.02
lowermarket
soiloftroptsaceroF
BaseBuy BuyinmarketwithlowestpredictedpriceusingEN 34.38 -173.94 329.81 19.83 1.74
BaseSell SellinmarketwithhighestpredictedpriceusingEN 35.09 -241.83 266.17 19.61 1.78
BaseBuy_EXAA Buyinmarketwithlowestpredictedpriceusing 34.36* -173.94 329.81 19.84 1.73
ENEXAA
BaseSell_EXAA Sellinmarketwithhighestpredictedpriceusing 35.11** -241.83 266.17 19.59 1.79
ENEXAA
MeanVarBuy Mean-varianceportfoliowithlowestreturn,i.e., 34.71 -178.50 245.99 19.09 1.83
lowestpricetopayusingEN
MeanVarSell Mean-varianceportfoliowithhighestreturn,i.e., 34.76 -173.89 213.02 18.62 1.87
highestpricetosellusingEN
MeanVarBuy_EXAA Mean-varianceportfoliowithlowestreturn,i.e., 34.72 -178.50 245.99 19.00 1.83
lowestpricetopayusingENEXAA
MeanVarSell_EXAA Mean-varianceportfoliowithhighestreturn,i.e., 34.76 -173.89 213.02 18.62 1.87
highestpricetosellusingENEXAA
Table4: Empiricaltestresultsofdifferentportfoliostrategiesinthecasestudyperiodfrom07.10.2017-31.05.2018. Thepricesarenotvolumeweightednor
adjustedinanywayandreflectthepriceonewouldbuyorsellatgiventheselectedportfoliostrategy.Naivepricesdenotethesimpleaverageoftherespectiveprice
series.Boththelowestbuyprice(*)andthehighestsellprice(**)aremarkedforconvenience.
tionthethoughtsonexpectedreturnyieldsamoresimpleform Thevarianceisdeterminedbyasimplifyingrelaxation. Instead
suchthat of complex estimation schemes, we will apply the empirical5
variance σ2 oftheindividualexchangereturnseriesandas-
i,qh,t
E(r )=yˆ +w (yˆ −yˆ ). (13)
portfolio,qh,t 1,qh,t 2,qh,t 2,qh,t 1,qh,t
5Pleasenotethatweapplythedescribedrollingestimationshiftstodeter-
minetheempiricalvariance. Hence,thefirstwindowtocalculatethevariance
rangesfrom08.10.2015until07.10.2016.Thistimespanisshiftedby96units
foreverysingledayandensuresauniqueempiricalvarianceforeverydayand
everyquarter-hour.

4.2 Economiceffectsofaccurateforecasts 15
sumeittobethebestestimatorinthecalculationoftheportfolio whereasitscounterpartMeanVar setsthefocusonnegative
Buy
returnin returns and lower prices for a net buyer. The same contentual
separation counts for the EXAA-enriched equivalents Mean-
σ2 portfolio,qh,t =(w2 1,qh,t σ2 1,qh,t )+(w2 2,qh,t σ2 2,qh,t )+2w 1,qh,t w 2,qh,t ρ 12,qh,t , Var Sell_EXAA andMeanVar Buy_EXAA respectively.
(14)
with ρ being the correlation of the returns. We simplify
12,qh,t
4.2.3. Economicportfolioassessment
Eq. (14)toeliminate w :
1,qh,t
Nowthatwehavedetermineddifferentportfoliostrategieswith
σ2 =σ2 +2w (ρ −σ2 ) (15)
portfolio,qh,t 1,qh,t 2,qh,t 12,qh,t 1,qh,t EXAAandnon-EXAAvariations,thelastfacettoassessisthe
+(w2 )(σ2 −2ρ +σ2 ).
2,qh,t 1,qh,t 12,qh,t 2,qh,t economic gain or loss resulting from our underlying forecasts
andportfoliostrategies. Forthesakeofsimplicity, weneglect
An important part of portfolio theory is the identification of
all kinds of fees and trading charges as well as the price im-
all efficient portfolios under non-zero weights and a sum of
pacts possible bids might have. Hence, we assume sufficient
weights equal to one. The latter postulation results in the as-
marketliquiditytoabsorbadditionaltradingvolumes. Lastbut
sumption of perfectly divisible asset portions. We follow this
not least, volume weighted average prices (VWAP) are only
traditional concept but must acknowledge that under real-life
an approximation for continuous market prices. Apparently, a
tradingcircumstancestheexchangepre-definedminimumtick
market participant does not have direct access to index quota-
sizes condition small adjustments to the optimization results
tions. Instead, regular trading activities could lead to average
due to the fact that they are not tradable. We are also not in-
dealpricesneartheVWAP.Sincetheintradaytradingactivities
terested in computing the entire set of efficient portfolios but
areuptoindividualcounterparts,withadetailedtimeseriesnot
want to find the one portfolio that exhibits the highest utility
being available, we apply the VWAP as a best guess. Based
forthemarketparticipant. Theutilityfunctionisdefinedasan
ontheseprices,wecarryoutasimpleportfoliosimulationand
optimizationproblemin(basicformtakenfromCalvo-Silvosa
check the average portfolio price a market participant would
etal.(2017))
payorreceivewhenfollowingtheportfoliostrategy. Theback-
1 test ranges from 07.10.2016 to 31.05.2018 and is summarized
U =argminE(r )− γσ2 (16)
qh,t w2,qh,t portfolio,qh,t 2 portfolio,qh,t in Table 4 together with a synopsis of all portfolio strategies.
s.t. w ∈[0,1], Weusetheoriginalpricestogetthemostrealisticresults. The
i,qh,t
only adaptation we apply is the clock-change adjustment de-
in which γ denotes a variable to specify the risk-aversion of scribedundersub-section3.1.Weacknowledgethatthiscauses
themarketparticipant. Wefollowtheenergyliteratureandset asmallbiasbutsinceitonlyaccountsfortwohoursofeachyear
γ = 2 which is regarded to be a slightly higher average risk weignoretheclock-changeinthetradingsimulation. Besides
appetite(Gökgöz&Atmaca(2012);Liu&Wu(2007)). Given theusualstandardmeasuresontimeseriesresolution,wereport
the high variance of the intraday series an adjustment towards acommonportfoliomanagementcriterioncalledSharpe-Ratio
less risk aversion appears to be suitable. Otherwise, the op- (adjustedfromCalvo-Silvosaetal.(2017))
timization will mostly select the QH auction market. At the
1 (cid:80)T (cid:80)96 (y )
same time, the slight changes to the original equations in Eq. S = 96T t=1 qh=1 strategy,qh,t , (17)
σ
(13) and Eq. (15) yield only one weighting parameter w strategy
2,qh,t
to be optimized. If we consider that possible solutions are re-
wherethenumeratordescribestheaveragerealizedpriceofthe
strictedtobeanythingbetweenzeroorone,itbecomesevident
respectiveportfoliostrategyoveralldaysandquarter-hoursand
that we implicitly meet the requirement (cid:80)2 w = 1. We
i=1 i,qh,t σ
strategy
the standard deviation of the realized prices of each
use R’s standard optimization command optim to find a so-
strategy. Thestrategyprices y areindividuallydeter-
strategy,qh,t
lution for Eq. (16). The optimization result yields two trad-
minedperstrategy,aspreviouslydescribed. IncaseofBase
Sell
ing indications; if we value positive returns as desired to sell
for instance, the strategy prices equal the market price of the
at high prices, the portfolio MeanVar is the important one
Sell higherpredictedexchange. Pleasebearinmindthatinitscon-

Economiceffectsofaccurateforecasts
| 4.2 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 16  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ventionalformtheSharpe-Ratioappliestheaverageexcessre- and standard deviation do. Both the Markowitz portfolio and
turn,butsincewesettherisk-freeratetobeequaltozero,this the Sharpe-Ratio include a variance measure in their calculus.
stepisnotnecessary,andtherealizedportfoliopriceisidentical Therefore, itdoesnotcomeasasurprisethatthebestSharpe-
totheexcessreturn. Ratio results are provided by mean-variance portfolios. Still,
The naive portfolios only buy or sell in one market at the we would have expected at least a small portion of economic
simpleaverageofthetimeseriesandconsequentlyyieldlower benefit expressed in better spread levels. An explanation for
sell and higher buy prices. There is no buy or sell separa- the performance is the concern over correlation. Our choice
tion with the naive prices while the forecast approaches im- ofassetswaspredetermined,andwehavenotcheckedthecor-
ply a buy and sell market price. Consequently, our naive sin- relation between the time series, but in financial markets, the
gular market strategies yield no spread benefits. We likewise co-movementamongstockscontributestoalessbalancedport-
reportaperfectportfoliostrategyundertheassumptionofcom- folio composition. The picture might change with less corre-
plete market information. The results are highly unlikely to lation between assets. However, the empirical results do not
be achieved in a real-world scenario but represent the obtain- provide evidence for Markowitz approaches to perform better
ablegainsfromfullyaccurateforecasts. However,wewillnot regardinghigherspreadsbutconstructarisk-minimizingport-
discuss the perfect portfolio in depth but focus our attention folio. Therefore, we favor the simple base strategies that are
groundedonahigh/lowmarketscenarioandwillpurelyfocus
| on achieved | spreads | compared |     | to singular | market | activities | as  |     |     |     |     |     |     |     |     |
| ----------- | ------- | -------- | --- | ----------- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thesedepictcurrentmarketparticipantbehaviormorethanthe onsuchinthedetailedanalysis.
postulationforcompleteex-antemarketknowledge.Ingeneral, A simple t-test depicted in Table 5 is supposed to deliver
theforecastportfoliosperformwell. Ourresultspointtowards further evidence on the statistical soundness of the identified
anoutperformanceofhigh/lowmarketinteractionreferredtoas excess performance. The p-values propose significant differ-
Base andBase andtheirEXAA-enrichedequivalents. encesbetweenourforecast-aidedbaseportfoliopricesandthe
| Buy        |        | Sell         |     |      |             |     |         |           |            |          |             |        |              |        |         |
| ---------- | ------ | ------------ | --- | ---- | ----------- | --- | ------- | --------- | ---------- | -------- | ----------- | ------ | ------------ | ------ | ------- |
|            |        |              |     |      |             |     |         | intraday  | continuous | time     | series.     | The QH | auction      | result | is less |
| In detail, | market | participants | buy | 0.70 | - 0.74€/MWh |     | cheaper |           |            |          |             |        |              |        |         |
|            |        |              |     |      |             |     |         | clear and | shows      | signs of | correlation | with   | the non-EXAA |        | base    |
andsell0.74-0.78€/MWhhighercomparedtoanyotherofthe
|     |     |     |     |     |     |     |     | strategies. | The | result at | least partially |     | confirms | our | findings. |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --------- | --------------- | --- | -------- | --- | --------- |
individualmarkets. Interestingly,theadditionofEXAAprices buy/sell
|     |     |     |     |     |     |     |     | Forecast | applications | translated |     | into a simple |     |     | trading |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | ---------- | --- | ------------- | --- | --- | ------- |
yields higher spreads. While the EXAA-aided point forecasts different
|     |     |     |     |     |     |     |     | decision | result in |     | portfolio | price | means | compared | to  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | --- | --------- | ----- | ----- | -------- | --- |
becomeonlyabitmoreaccuratefortheQHauction,thedirec-
|                 |           |           |          |            |         |             |         | the underlying | individual |                | prices.       | There    | are tests   | available | for    |
| --------------- | --------- | --------- | -------- | ---------- | ------- | ----------- | ------- | -------------- | ---------- | -------------- | ------------- | -------- | ----------- | --------- | ------ |
| tional accuracy |           | tends to  | improve. | This       | finding | seems       | contra- |                |            |                |               |          |             |           |        |
|                 |           |           |          |            |         |             |         | the equality   | of         | Sharpe-Ratios. |               | They use | the         | portfolio | prices |
| dictory         | at first, | but might | be the   | case since | a       | directional | fore-   |                |            |                |               |          |             |           |        |
|                 |           |           |          |            |         |             |         | as inputs      | and check  | for            | statistically | sound    | differences |           | among  |
castdoesnotadvancefromaprecisepointpredictionbutsolely
|     |     |     |     |     |     |     |     | Sharpe-Ratios. |     | We apply | the classical |     | pairwise | test | of Ledoit |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | ------------- | --- | -------- | ---- | --------- |
fromcorrecthigh/lowmarketestimates.
&Wolf(2008)andanexpansionthatconsidersjointeffectsof
| The | Markowitz | approach | adds | a considerably |     | lower | por- |     |     |     |     |     |     |     |     |
| --- | --------- | -------- | ---- | -------------- | --- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
pricesinamultipleSharp-RatiotestinLeung&Wong(2008)
| tionofeconomicgains.                        |     | Itsportfoliostructureisatrade-offbe- |     |     |     |             |     |                                             |          |          |     |          |                 |            |         |
| ------------------------------------------- | --- | ------------------------------------ | --- | --- | --- | ----------- | --- | ------------------------------------------- | -------- | -------- | --- | -------- | --------------- | ---------- | ------- |
|                                             |     |                                      |     |     |     |             |     | andlaterfornon-iidcasesinWrightetal.(2014). |          |          |     |          |                 | Resultsare |         |
| tweentheauctionandcontinuousintradayprices. |     |                                      |     |     |     | Therealized |     |                                             |          |          |     |          |                 |            |         |
|                                             |     |                                      |     |     |     |             |     | reported                                    | in Table | 5. While | the | multiple | test statistics |            | clearly |
portfoliopricevariesbetweentheQHauctionanditscontinu-
pointtowardsindependentSharpe-Ratios,someofthepairwise
| ous equivalent. |     | A possible | explanation |     | might | be given | by the |                               |     |     |     |                            |     |     |     |
| --------------- | --- | ---------- | ----------- | --- | ----- | -------- | ------ | ----------------------------- | --- | --- | --- | -------------------------- | --- | --- | --- |
|                 |     |            |             |     |       |          |        | testfindingshavetoberejected. |     |     |     | However,thisdoesnotcontra- |     |     |     |
Markowitz inputs. The optimization has to split between the considerablediffer-
dictourgeneralstatementofindependent,
highlyvolatileintradaycontinuousmarketandthemoremod-
|                 |     |                                         |     |     |     |     |     | ences in | prices | when using | forecasts | since | most | of the | combi- |
| --------------- | --- | --------------------------------------- | --- | --- | --- | --- | --- | -------- | ------ | ---------- | --------- | ----- | ---- | ------ | ------ |
| erateQHauction. |     | Mostofthetime,thisresultsinasignificant |     |     |     |     |     |          |        |            |           |       |      |        |        |
nationsthatappeartobecorrelatedareusingaslightlychanged
| portion | of QH | auction prices | due | to risk | aversion | tendencies. |     |     |     |     |     |     |     |     |     |
| ------- | ----- | -------------- | --- | ------- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
setofinputsandmightindeedbenearlyequal.
| Hence,ifoneconsiderstheutilityfunctioninEq. |           |             |     |       |           | (16),amore |        |                                       |     |     |     |     |     |             |     |
| ------------------------------------------- | --------- | ----------- | --- | ----- | --------- | ---------- | ------ | ------------------------------------- | --- | --- | --- | --- | --- | ----------- | --- |
|                                             |           |             |     |       |           |            |        | Table4implieshomogeneityacrossallQHs. |     |     |     |     |     | Weaddition- |     |
| risk averse                                 | portfolio | is created. |     | While | the plain | prices     | do not |                                       |     |     |     |     |     |             |     |
allywanttoanalyzetimestructureeffectsontheeconomicout-
suggestlargerbenefitsfromfollowingMarkowitz-guidedtrad-
|     |     |     |     |     |     |     |     | come and | turn our | attention | to the | realized | spread | of  | the best |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --------- | ------ | -------- | ------ | --- | -------- |
ing in comparison with the base strategies, the Sharpe-Ratio /Base
|     |     |     |     |     |     |     |     | performing | Base | Sell | Buy strategy. | Based | on  | the forecasts, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ---- | ------------- | ----- | --- | -------------- | --- |

17
|     |     |     |     |     |     |     |     | 5. Conclusionandoutlook |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- |
p-values
|     |     | BaseBuy | BaseSell | BaseBuy_EXAA |     | BaseSell_EXAA |     |     |     |     |     |     |     |     |     |
| --- | --- | ------- | -------- | ------------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
<0.001
| NaiveAUQH |     | 0.016  | 0.017  |        | 0.005 |       |     |                                         |     |            |      |        |         |                |        |
| --------- | --- | ------ | ------ | ------ | ----- | ----- | --- | --------------------------------------- | --- | ---------- | ---- | ------ | ------- | -------------- | ------ |
|           |     |        |        |        |       |       |     | We contributed                          |     | to a blind | spot | in the | current | literature     | by an- |
| NaiveIDQH |     | <0.001 | <0.001 | <0.001 |       | 0.005 |     |                                         |     |            |      |        |         |                |        |
|           |     |        |        |        |       |       |     | alyzingquarter-hourlyGermanspotmarkets. |     |            |      |        |         | Thegeneralten- |        |
Table5: T-testforstatisticalsignificanceoflowerbuyandhighersellprices.
dencytowardsmorevolatilepowergridsnecessitatedtheintro-
| Thetwo-sidedtestpostulates |     |     | H0 : µ1 | −µ2 = | 0 andchecksforstatistically |     |     |     |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | ------- | ----- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sounddifferencesinportfolioprices. duction of a quarter-hourly intraday call auction and the pos-
|     |     |     |     |     |     |     |     | sibility | to trade | quarter-hours |     | in continuous |     | intraday | trading. |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ------------- | --- | ------------- | --- | -------- | -------- |
weobserveahigh/lowspread(thedeltabetweenhighandlow
Ourpaperprovidesthefirstdetaileddiscussiononhowtofore-
prices)of0.76€/MWhamongallQHs.
Figure7cascadesthis
|          |        |              |              |     |            |             |     | castthesemarketsex-ante. |                                               |     | Wehaveappliedmodernregression |     |     |     |     |
| -------- | ------ | ------------ | ------------ | --- | ---------- | ----------- | --- | ------------------------ | --------------------------------------------- | --- | ----------------------------- | --- | --- | --- | --- |
| singular | number | into a finer | granularity. |     | It depicts | limitations |     |                          |                                               |     |                               |     |     |     |     |
|          |        |              |              |     |            |             |     | techniques,              | namelytheelasticnetestimatorthatautomatically |     |                               |     |     |     |     |
forthepeak-loadrangingfromQHs32to75wherespreadsare
penalizesfeaturesthatdonotaddanyinsight,andcomparedthe
aroundzeroorevennegative.Thisfindingmatchestheoutcome
outcomewithclassicallinearregressionmodels.Oneofthepe-
ofourdirectionalforecastmetricsandsuggestsanoveralllower
culiaritiesofGermanspotmarketsistheexistenceofavariety
predictivepowerduringthemiddlequarter-hoursoftheday.On
|     |     |     |     |     |     |     |     | oftradingopportunities. |     |     | Inparticular, |     | theAustrianEXAAof- |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | ------------- | --- | ------------------ | --- | --- |
theotherhand,itssurroundingoff-peakequivalentsfeaturere-
fersafirstday-aheadindicationonquarter-hoursthatcanbede-
| markably      | high spreads. |                                      | Some | hours exhibit |     | price differences |     |                            |     |     |     |                            |     |     |     |
| ------------- | ------------- | ------------------------------------ | ---- | ------------- | --- | ----------------- | --- | -------------------------- | --- | --- | --- | -------------------------- | --- | --- | --- |
|               |               |                                      |      |               |     |                   |     | liveredintotheGermangrids. |     |     |     | Toaccountforthat,wehaveap- |     |     |     |
| around2€/MWh. |               | Evenundertheassumptionofnegativepeak |      |               |     |                   |     |                            |     |     |     |                            |     |     |     |
pliedtheEXAAasastandalonenaiveestimateaswellasanin-
70Cent/MWh
| spreads, | the overall | average | delta | of more | than |     |     |     |     |     |     |     |     |     |     |
| -------- | ----------- | ------- | ----- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
putforourmoreadvancedregressionmodels.Wefoundthatthe
allowsfortheconclusionofeconomicgainstobemadeinour
intradayauctioniseasiertopredictcomparedtoongoingtrad-
casestudy.
ing.OurEN-basedpredictionmethodprovideshighforecasting
| Overall, | we need   | to        | mention | that a     | very primitive |            | strategy |          |                 |               |      |            |           |         |          |
| -------- | --------- | --------- | ------- | ---------- | -------------- | ---------- | -------- | -------- | --------------- | ------------- | ---- | ---------- | --------- | ------- | -------- |
|          |           |           |         |            |                |            |          | accuracy | and outperforms |               | the  | considered | benchmark |         | models.  |
| based on | two point | forecasts |         | yields the | most           | attractive | eco-     |          |                 |               |      |            |           |         |          |
|          |           |           |         |            |                |            |          | When we  | add             | the available | EXAA | prices,    | the       | results | are even |
nomicbenefitsalbeittheteststatisticsbeforehaverevealedthe
|             |        |       |           |           |            |     |          | more convincing. |                 | This | assumption | was       | further  | confirmed | by            |
| ----------- | ------ | ----- | --------- | --------- | ---------- | --- | -------- | ---------------- | --------------- | ---- | ---------- | --------- | -------- | --------- | ------------- |
| limitations | of our | point | forecasts | to binary | prediction |     | applica- |                  |                 |      |            |           |          |           |               |
|             |        |       |           |           |            |     |          | the popular      | Diebold-Mariano |      |            | test that | revealed | a         | statistically |
tions.Themorecomplexmean-varianceoptimizationapproach
|                                          |     |     |     |     |     |                |     | sound outperformance |                |      | of all | models,          | but EXAA | ones          | and the |
| ---------------------------------------- | --- | --- | --- | --- | --- | -------------- | --- | -------------------- | -------------- | ---- | ------ | ---------------- | -------- | ------------- | ------- |
| couldnotentirelyliveuptotheexpectations. |     |     |     |     |     | Thestrategydid |     |                      |                |      |        |                  |          |               |         |
|                                          |     |     |     |     |     |                |     | EN one               | in particular, | over | the    | naive benchmark. |          | Surprisingly, |         |
notprovideanyspreadbenefits,onlyagoodSharpe-Ratioand
thisfindingdoesnotholdtrueforthecontinuousintradaymar-
| risk-averse | portfolio | structures.   |     | However,  | the    | Markowitz | op-  |                                                        |     |     |     |     |     |     |     |
| ----------- | --------- | ------------- | --- | --------- | ------ | --------- | ---- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|             |           |               |     |           |        |           |      | ket. Ourforecastmodelsrevealedonlyminorincreasesinper- |     |     |     |     |     |     |     |
| timization  | was the   | less volatile |     | portfolio | choice | with the  | low- |                                                        |     |     |     |     |     |     |     |
formanceandfewerquarter-hourswheretheDiebold-Mariano
| eststandarddeviations. |             |             | Despitethemissingspreadbenefit,its |          |            |           |          |                                              |         |        |         |      |                       |     |             |
| ---------------------- | ----------- | ----------- | ---------------------------------- | -------- | ---------- | --------- | -------- | -------------------------------------------- | ------- | ------ | ------- | ---- | --------------------- | --- | ----------- |
|                        |             |             |                                    |          |            |           |          | statistics                                   | suggest | better | results | than | the benchmark.        |     | EXAA        |
| price level            | was exactly | between     |                                    | the two  | individual | exchanges |          |                                              |         |        |         |      |                       |     |             |
|                        |             |             |                                    |          |            |           |          | pricesonlymatteredtoasmallextent.            |         |        |         |      | Anotherinterestingas- |     |             |
| and marks              | the best    | alternative |                                    | for risk | averse     | market    | partici- |                                              |         |        |         |      |                       |     |             |
|                        |             |             |                                    |          |            |           |          | pectoccurredintheconstructionofinputfactors. |         |        |         |      |                       |     | Weinitially |
pants.
expectedtheexpertchoicemodeltocompriseallrelevantfac-
Tobemoreconcreteonnumbers,weassumeanequallydis-
tors,buttheoutperformanceofthefullmodelgroupprovedus
tributed50MWQHspreadpositionbasedontheBase
|         |          |            |                                |     |     | Sell_EXAA |     | wrong. | Whenaddingeverypossibleinput,theOLS-basedLM |          |     |        |         |        |            |
| ------- | -------- | ---------- | ------------------------------ | --- | --- | --------- | --- | ------ | ------------------------------------------- | -------- | --- | ------ | ------- | ------ | ---------- |
| andBase | Buy_EXAA | forecasts. | Ifamarketparticipantfollowsour |     |     |           |     |        |                                             |          |     |        |         |        |            |
|         |          |            |                                |     |     |           |     | models | ran into                                    | problems | due | to the | massive | set of | regressors |
EXAAbasestrategyfrom07.10.2016to31.05.2018,savingsof
buttheelasticnetanditsfeatureselectionrevealedlowererror
€325,080forabuyeroradditionalrevenuesinthesamerange
metrics.
foraselleraretoberealizedundertheassumptionofnoextra
|     |     |     |     |     |     |     |     | If we | recap | the times | of  | trading | and forecasting, |     | a prob- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | --------- | --- | ------- | ---------------- | --- | ------- |
feesandaccesstoVWAPprices.
|     |     |     |     |     |     |     |     | lem arises.        | The        | QH auction                          |           | is estimated  | shortly | after     | the data   |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | ---------- | ----------------------------------- | --------- | ------------- | ------- | --------- | ---------- |
|     |     |     |     |     |     |     |     | has been           | published, | i.e.,                               | uses      | the most      | current | freely    | available  |
|     |     |     |     |     |     |     |     | inputs, whereas    |            | the last                            | hours     | of continuous |         | trading   | are deter- |
|     |     |     |     |     |     |     |     | mined24hourslater. |            | Thissituationcouldleadtonewinforma- |           |               |         |           |            |
|     |     |     |     |     |     |     |     | tion. However,     |            | we have                             | neglected | this          | last    | facet and | have si-   |

Bibliography 18
EXAA_QH EPEX_ID EPEX_QH EN_Sell EN_Buy EN_Sell EXAA EN_Buy EXAA MVC_Sell EXAA MVC_Buy EXAA MVC_Buy MVC_Sell
| EXAA_QH |     | X      |         |        |         |         |     |     |     |     |
| ------- | --- | ------ | ------- | ------ | ------- | ------- | --- | --- | --- | --- |
| EPEX_ID |     | <0.001 |         | X      |         |         |     |     |     |     |
| EPEX_QH |     | <0.001 | <0.001X |        |         |         |     |     |     |     |
| EN_Sell |     | <0.001 | <0.001  | 0.05X  |         |         |     |     |     |     |
| EN_Buy  |     | <0.001 | 0.08    | <0.001 | <0.001X |         |     |     |     |     |
| EN_Sell |     | <0.001 | <0.001  | <0.001 | <0.001  | <0.001X |     |     |     |     |
EXAA
EN_Buy
|          | EXAA | <0.001 | 0.13   | <0.001 | <0.001 | 0.47   | <0.001X |         |     |     |
| -------- | ---- | ------ | ------ | ------ | ------ | ------ | ------- | ------- | --- | --- |
| MVC_Sell |      | <0.001 | <0.001 | <0.001 | <0.001 | <0.001 | <0.001  | <0.001X |     |     |
EXAA
| MVC_Buy |     | <0.001 | <0.001 | 0.02 | <0.001 | <0.001 | 0.83 | <0.001 <0.001X |     |     |
| ------- | --- | ------ | ------ | ---- | ------ | ------ | ---- | -------------- | --- | --- |
EXAA
MVC_Buy <0.001 <0.001 0.02 <0.001 <0.001 0.84 <0.001 <0.001 0.21X
MVC_Sell <0.001 <0.001 <0.001 <0.001 <0.001 <0.001 <0.001 0.39 <0.001 <0.001X
Multiple Sharpe-Ratio test (all 11 price series jointly tested) p-value: <0.001
Table6: Testresultsreportedasp-valuesfortwoSharpe-Ratioequalitytests. ThenullhypothesisstatesthatSharpe-Ratiosareequalandcanberejectedwith
sufficientlylowp-values.Weapplytwodifferenttests,apairwisetestreportedinthetableandatestthatjointlyconsidersallSharpe-Ratios.
multaneouslypredictedbothmarketstoevaluatetheeconomic in EPEX day-ahead predictions. But does this hold true for
effects of our forecasts. Their standalone information might quarter-hourlymarketsaswell? Anotherpointofpossiblecrit-
help regulators or grid operators, but we deliberately focus on icism arises from the high/low portfolio. The individual fore-
amarketplayerapplicationandderiveportfoliostrategieswith castswerecombinedtoadirectionalestimation.Onecouldalso
both EXAA and non-EXAA-enriched estimations. We intro- discuss available directional forecast approaches and simplify
duced a straightforward “sell in the high and buy in the low theforecastingproblemtothebinaryonethatisutilizedinthe
market”ruleforthefirstsetofportfoliosandexpandedthesec- portfolioapplication.
| ondgroupbyaMarkowitzmean-varianceapproach. |     |     |     |     |     | Wewere |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
low/high
| able to | demonstrate | that | the | strategies |     | perform best, |     |     |     |     |
| ------- | ----------- | ---- | --- | ---------- | --- | ------------- | --- | --- | --- | --- |
Acknowledgments
| leading                    | to considerable |     | spreads                   | and attractive | benefits | for ei- |     |     |     |     |
| -------------------------- | --------------- | --- | ------------------------- | -------------- | -------- | ------- | --- | --- | --- | --- |
| theranetbuyeroranetseller. |                 |     | TheMarkowitzapproachesdid |                |          |         |     |     |     |     |
notshowanyeconomicimprovementsintheformoffavorable The valuable contributions of anonymous referees are grate-
spreads but delivered a maximum Sharpe-Ratio portfolio. So fullyacknowledged. Thisworkwaspartiallysupportedbythe
evenifmarketplayersseektofollowtraditionalmean-variance German Research Foundation (DFG, Germany) and the Na-
|     |     |     |     |     |     |     | tional | Science Center (NCN, | Poland) through | BEETHOVEN |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------------------- | --------------- | --------- |
strategiesunderthepreceptofrisk-aversion,aprecisequarter-
hourly forecast could deliver a suitable input for estimated re- projectIMMORTAL(InvestigatingMarketMicrostructureand
turns. shOrt-termpRiceforecasTinginintrA-dayeLectricitymarkets)
Atthesametime,wemustacknowledgethatthebasicsetup, grantno. 379008354(toFZ).
| despite      | its decent | gains,     | was a    | rather simple | one | and could     |     |     |     |     |
| ------------ | ---------- | ---------- | -------- | ------------- | --- | ------------- | --- | --- | --- | --- |
| be extended. |            | We assumed | a stable | net buy       | or  | sell position |     |     |     |     |
AppendixA.Supplementarydata
| inallQHs | andonlyroughly |              | consideredterm-structureeffects. |               |          |        |     |     |     |     |
| -------- | -------------- | ------------ | -------------------------------- | ------------- | -------- | ------ | --- | --- | --- | --- |
| A proper | analysis       | of weekends, |                                  | peak/off-peak | patterns | or the |     |     |     |     |
aforementioned trading and prediction time could yield bene- SupplementarydatatothisarticlecanbefoundonlineatDOI:
10.17632/2trdgv8wrp.3.
| ficial | insights.       | The same        | counts     | for the point           | predictions | it-      |     |     |     |     |
| ------ | --------------- | --------------- | ---------- | ----------------------- | ----------- | -------- | --- | --- | --- | --- |
| self.  | What if         | we continuously |            | forecast quarter-hourly |             | prices   |     |     |     |     |
| once   | new information | is              | published? | Or                      | how does    | accuracy |     |     |     |     |
Bibliography
| changeifweaddmoreaccuratevendordata? |     |     |     |     | Wehavejustfo- |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
cusedonlinearmodelsinourstudybutofcoursethereareother
non-linearpredictionmodelssuchasrandomforestsavailable. Aïd,R.,Gruet,P.,&Pham,H.(2016).Anoptimaltradingprobleminintraday
electricitymarkets.MathematicsandFinancialEconomics,10,49–85.
| For instance, |     | a study in | Ludwig | et al. (2015) | has | shown that |     |     |     |     |
| ------------- | --- | ---------- | ------ | ------------- | --- | ---------- | --- | --- | --- | --- |
Bordignon,S.,Bunn,D.W.,Lisi,F.,&Nan,F.(2013).Combiningday-ahead
lassoestimatorsprovidedcomparableresultstorandomforests
forecastsforbritishelectricityprices.EnergyEconomics,35,88–103.

Bibliography 19
Buuren,S.,&Groothuis-Oudshoorn,K.(2011).mice:Multivariateimputation Nowotarski,J.,Liu,B.,Weron,R.,&Hong,T.(2016).Improvingshortterm
bychainedequationsinR.Journalofstatisticalsoftware,45,1–67. loadforecastaccuracyviacombiningsisterforecasts.Energy,98,40–49.
Calvo-Silvosa,A.,Antelo,S.I.,Soares,I.etal.(2017).Energyplanningand Nowotarski,J.,Raviv,E.,Trück,S.,&Weron,R.(2014).Anempirical
modernportfoliotheory:Areview.RenewableandSustainableEnergy comparisonofalternativeschemesforcombiningelectricityspotprice
Reviews,77,636–651. forecasts.EnergyEconomics,46,395–412.
Diebold,F.X.(2015).Comparingpredictiveaccuracy,twentyyearslater:A Pape,C.,Hagemann,S.,&Weber,C.(2016).Arefundamentalsenough?
personalperspectiveontheuseandabuseofdiebold–marianotests. explainingpricevariationsinthegermanday-aheadandintradaypower
JournalofBusiness&EconomicStatistics,33,1–1. market.EnergyEconomics,54,376–387.
Diebold,F.X.,&Mariano,R.S.(1995).Comparingpredictiveaccuracy. Paraschiv,F.,Erni,D.,&Pietsch,R.(2014).Theimpactofrenewableenergies
JournalofBusiness&economicstatistics,13,253–263. oneexday-aheadelectricityprices.EnergyPolicy,73,196–210.
EPEX(2013).15-minuteintradaycallauction:3pm.thenewmeetingpoint Pesaran,M.H.,&Timmermann,A.(1992).Asimplenonparametrictestof
forthegermanmarket.URL:https://www.epexspot.com/document/ predictiveperformance.JournalofBusiness&EconomicStatistics,10,
29113/15-Minute%20Intraday%20Call%20Auction. 461–465.
Friedman,J.,Hastie,T.,&Tibshirani,R.(2010).Regularizationpathsfor Uniejewski,B.,Nowotarski,J.,&Weron,R.(2016).Automatedvariable
generalizedlinearmodelsviacoordinatedescent.Journalofstatistical selectionandshrinkageforday-aheadelectricitypriceforecasting.
software,33,1. Energies,9,621.
Garnier,E.,&Madlener,R.(2015).Balancingforecasterrorsin Uniejewski,B.,Weron,R.,&Ziel,F.(2018).Variancestabilizing
continuous-tradeintradaymarkets.EnergySystems,6,361–388. transformationsforelectricityspotpriceforecasting.IEEETransactionson
Gökgöz,F.,&Atmaca,M.E.(2012).Financialoptimizationintheturkish PowerSystems,33,2219–2229.
electricitymarket:Markowitz’smean-varianceapproach.Renewableand Viehmann,J.(2017).Stateofthegermanshort-termpowermarket.Zeitschrift
SustainableEnergyReviews,16,357–368. fürEnergiewirtschaft,41,1–17.
Gürtler,M.,&Paulsen,T.(2018).Forecastingperformanceoftimeseries Weron,R.(2007).Modelingandforecastingelectricityloadsandprices:A
modelsonelectricityspotmarkets:aquasi-meta-analysis.International statisticalapproachvolume403.JohnWiley&Sons.
JournalofEnergySectorManagement,12,103–129. Weron,R.(2014).Electricitypriceforecasting:Areviewofthe
Hirth,L.(2013).Themarketvalueofvariablerenewables:Theeffectofsolar state-of-the-artwithalookintothefuture.Internationaljournalof
windpowervariabilityontheirrelativeprice.Energyeconomics,38, forecasting,30,1030–1081.
218–236. Weron,R.,&Misiorek,A.(2008).Forecastingspotelectricityprices:A
Ketterer,J.C.(2014).Theimpactofwindpowergenerationontheelectricity comparisonofparametricandsemiparametrictimeseriesmodels.
priceingermany.EnergyEconomics,44,270–280. Internationaljournalofforecasting,24,744–763.
Kiesel,R.,&Paraschiv,F.(2017).Econometricanalysisof15-minuteintraday Wright,J.,Yam,S.,&PangYung,S.(2014).Atestfortheequalityof
electricityprices.EnergyEconomics,64,77–90. multiplesharperatios.JournalofRisk,16,3–21.
Ledoit,O.,&Wolf,M.(2008).Robustperformancehypothesistestingwith Würzburg,K.,Labandeira,X.,&Linares,P.(2013).Renewablegeneration
thesharperatio.JournalofEmpiricalFinance,15,850–859. andelectricityprices:Takingstockandnewevidenceforgermanyand
Leung,P.-L.,&Wong,W.-K.(2008).Ontestingtheequalityofthemultiple austria.EnergyEconomics,40,S159–S171.
sharperatios,withapplicationontheevaluationofishares.JournalofRisk, Ziel,F.(2017).Modelingtheimpactofwindandsolarpowerforecasting
10,15–30. errorsonintradayelectricityprices.InEuropeanEnergyMarket(EEM),
Liu,M.,&Wu,F.F.(2007).Portfoliooptimizationinelectricitymarkets. 201714thInternationalConferenceonthe(pp.1–5).IEEE.
ElectricPowersystemsresearch,77,1000–1009. Ziel,F.,Steinert,R.,&Husmann,S.(2015).Forecastingdayaheadelectricity
Ludwig,N.,Feuerriegel,S.,&Neumann,D.(2015).Puttingbigdataanalytics spotprices:Theimpactoftheexaatoothereuropeanelectricitymarkets.
towork:Featureselectionforforecastingelectricitypricesusingthelasso EnergyEconomics,51,430–444.
andrandomforests.JournalofDecisionSystems,24,19–36. Zou,H.,&Hastie,T.(2005).Regularizationandvariableselectionviathe
Maciejowska,K.,&Nowotarski,J.(2016).Ahybridmodelforgefcom2014 elasticnet.JournaloftheRoyalStatisticalSociety:SeriesB(Statistical
probabilisticelectricitypriceforecasting.InternationalJournalof Methodology),67,301–320.
Forecasting,32,1051–1056.
Maciejowska,K.,Nowotarski,J.,&Weron,R.(2016).Probabilistic
forecastingofelectricityspotpricesusingfactorquantileregression
averaging.InternationalJournalofForecasting,32,957–965.
Märkle-Huß,J.,Feuerriegel,S.,&Neumann,D.(2018).Contractdurationsin
theelectricitymarket:Causalimpactof15mintradingontheepexspot
market.EnergyEconomics,69,367–378.
Markowitz,H.(1952).Portfolioselection.Thejournaloffinance,7,77–91.
Moosa,I.,&Vaz,J.(2015).Directionalaccuracy,forecastingerrorandthe
profitabilityofcurrencytrading:model-basedevidence.Applied
Economics,47,6191–6199.