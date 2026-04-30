| IEEETRANSACTIONSONPOWERSYSTEMS,VOL.35,NO.3,MAY2020 |     |         |         |     |               |     |         |          |      |     |             |     |     | 2339 |
| -------------------------------------------------- | --- | ------- | ------- | --- | ------------- | --- | ------- | -------- | ---- | --- | ----------- | --- | --- | ---- |
| Adaptive                                           |     | Trading |         |     | in Continuous |     |         | Intraday |      |     | Electricity |     |     |      |
|                                                    |     |         | Markets |     | for           | a   | Storage |          | Unit |     |             |     |     |      |
GillesBertrand ,StudentMember,IEEE,andAnthonyPapavasiliou ,Member,IEEE
Abstract—Theincreasingintegrationofrenewableresourcesin Severalpapersanalyzetheoptimizationofbiddingstrategies
electricitymarketshasincreasedtheneedforproducerstocorrect in different electricity markets. In [4], the authors consider
theirtradingpositionclosetorealtimeinordertoavoidvolatile
|     |     |     |     |     |     |     | trading | in the | day-ahead | market | and | covering | their | position |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------ | --------- | ------ | --- | -------- | ----- | -------- |
real-timeprices.TheclosestoptiontodeliverytimeinEuropean
|     |     |     |     |     |     |     | in imbalance | for | a wind | power | producer. | This | work | has been |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------ | ----- | --------- | ---- | ---- | -------- |
marketsistotradeinthecontinuousintradaymarket.Thismarket
extendedin[5]inwhichtheauthorsalsoconsiderbiddinginthe
| is therefore | an attractive | trading | outlet | for | assets that target | at  |     |     |     |     |     |     |     |     |
| ------------ | ------------- | ------- | ------ | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
extracting value from their flexibility. Trading in this market is intradaymarket.In[6],theauthorsdevelopsatradingstrategy
challengingduetothemultistagenatureoftheproblem,itshigh forawindpowerproducerwhotradesintheday-aheadmarket,
uncertaintyandthefactthatdecisionsneedtobereachedrapidly,
|     |     |     |     |     |     |     | followed | by settlement |     | in the | real-time | market. |     | The authors |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- | ------ | --------- | ------- | --- | ----------- |
inordertolockinprofitabletrades.Wemodelthetradingproblem
|     |     |     |     |     |     |     | account | for the | impact | of the | dependence |     | between | the wind |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------ | ------ | ---------- | --- | ------- | -------- |
ofastorageunitintheMarkovDecisionProcessframework.We
productionerrorandthereal-timepriceonthetradingstrategy
presentanapproachbasedonpolicyfunctionapproximationfor
tacklingtheproblem.Weproviderelevantparametersfordefining ofthewindfarm.
our policy, and demonstrate the effectiveness of our approach A certain body of the literature focuses specifically on stor-
| by comparing | it       | to the rolling | intrinsic   | policy | on real historical    |     |            |             |           |            |         |          |             |        |
| ------------ | -------- | -------------- | ----------- | ------ | --------------------- | --- | ---------- | ----------- | --------- | ---------- | ------- | -------- | ----------- | ------ |
|              |          |                |             |        |                       |     | age units. | The         | operation | of         | storage | units in | the context | of a   |
| data. Our    | proposed | approach       | outperforms |        | the rolling intrinsic |     |            |             |           |            |         |          |             |        |
|              |          |                |             |        |                       |     | US-style   | centralized | unit      | commitment |         | has been | studied     | in the |
policy,whichiscommonlyemployedinpracticeforstorageunits,
literatureusingunitcommitmentmodelssuchasin[7]and[8].
byincreasingprofitabilityby17.8%onout-of-sampletestingfor
a storage with perfect round-trip efficiency and by 13.6% for a Nevertheless, these models are out of scope in an EU context,
storageunitwitharound-tripefficiencyof81%. whereresourceownersself-commitandself-scheduleindividual
|       |              |     |          |            |                 |     | resources | at the | nomination |     | stage which | follows |     | the clearing |
| ----- | ------------ | --- | -------- | ---------- | --------------- | --- | --------- | ------ | ---------- | --- | ----------- | ------- | --- | ------------ |
| Index | Terms—Markov |     | decision | processes, | policy function |     |           |        |            |     |             |         |     |              |
approximation, reinforcement learning, continuous intraday of the portfolio-based day-ahead market. In the EU context,
market. theauthors in[9]focus ontheinteractionoftradingstrategies
|           |     |                  |     |        |             |        | in the day-ahead |         | market    | and | the balancing |     | market,  | while the |
| --------- | --- | ---------------- | --- | ------ | ----------- | ------ | ---------------- | ------- | --------- | --- | ------------- | --- | -------- | --------- |
|           |     | I. INTRODUCTION  |     |        |             |        |                  |         |           |     |               |     |          |           |
|           |     |                  |     |        |             |        | interaction      | between | day-ahead |     | and intraday  |     | auctions | has been  |
| FOLLOWING |     |                  |     |        |             |        | analysedin[10].  |         |           |     |               |     |          |           |
|           |     | the introduction |     | of the | climate and | energy |                  |         |           |     |               |     |          |           |
packageinEurope[1],theintegrationofrenewableenergy Thestrategiesdevelopedforthesemarketscannotbeapplied
in Germany has increased from 18.2% in 2010 to 32.2% in directlytotheCIMduetothecontinuousformatofthismarket,
2016[2].Theserenewableresourcesincreasethevariabilityof whichdiffersfromtheday-aheadauctionortheintradayauction.
supply in the market, and consequently increase the need for Indeed, in auctions the producer has one chance to submit
|            |        |          |           |            |                |     | bids. Instead, | in  | the CIM, | the | producer | is  | afforded | a certain |
| ---------- | ------ | -------- | --------- | ---------- | -------------- | --- | -------------- | --- | -------- | --- | -------- | --- | -------- | --------- |
| correcting | system | dispatch | closer to | real time. | An interesting |     |                |     |          |     |          |     |          |           |
optionforsuchcorrectionsistotradeinthecontinuousintraday amountoftimeinordertoobservetheofferssubmittedbyother
market (CIM), which explains the recent increase of liquidity participants.Moreover,intheCIM,buyandsellpricesforthe
inthismarket.Specifically,tradedvolumesintheGermanCIM samedeliverytimemayevolveoverthehorizonoftrading.Due
have increased from 10 TWh in 2010 to 41 TWh in 2016 [3]. totheseparticularities,theCIMhasreceivedseparatetreatment
intheliterature.
| This market | is  | therefore | becoming | an interesting | option | for |     |     |     |     |     |     |     |     |
| ----------- | --- | --------- | -------- | -------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
fast-movingassets,suchasbatteriesorpumpedhydrostorage, The specific literature about the CIM can be classified into
toextractvaluefromtheirflexibility. thethreefollowingcategories.
|     |     |     |     |     |     |     | i) The | first | category | of  | papers | focuses | on modeling | the |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----- | -------- | --- | ------ | ------- | ----------- | --- |
Manuscript received May 20, 2019; revised October 9, 2019; accepted priceevolutionintheCIM.Thisincludes literaturethat
November16,2019.DateofpublicationDecember2,2019;dateofcurrent focusesontheexplanatoryvariablesfortheevolutionof
versionApril22,2020.ThisworkwassupportedinpartbytheENGIEChair
theprice[11],[12],andonthefactorsthatinfluencethe
onEnergyEconomicsandEnergyRiskManagement,byanElectrabelgrant
on“ModelingtheValueofFlexibilityatSub-HourlyOperatingTimeScales,” liquidityandthebid-askspread[13].In[14]theauthors
andinpartbytheBelgianNationalScienceFoundation(FSR-FNRS)through develop a Hawkes process for modeling the arrival of
aFRIAgrant.Paperno.TPWRS-00703-2019.(Correspondingauthor:Gilles
|     |     |     |     |     |     |     | orders. | A   | model | for the | simulation |     | of the | CIM based |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ----- | ------- | ---------- | --- | ------ | --------- |
Bertrand.)
TheauthorsarewiththeCORE,UCLouvain,LouvainlaNeuve1348,Belgium ondatafromtheEuropeanPowerExchangeisproposed
(e-mail:gilles.bertrand@uclouvain.be;anthony.papavasiliou@uclouvain.be).
in[3].
Colorversionsofoneormoreofthefiguresinthisarticleareavailableonline
|     |     |     |     |     |     |     | ii) Thesecondcategoryofpapersfocusesonoptimaltrading |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
athttp://ieeexplore.ieee.org.
|     |     |     |     |     |     |     | strategies, |     | and assumes |     | that the | intraday | prices | follow |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----------- | --- | -------- | -------- | ------ | ------ |
DigitalObjectIdentifier10.1109/TPWRS.2019.2957246
0885-8950©2019IEEE.Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.
Seehttps://www.ieee.org/publications/rights/index.htmlformoreinformation.
Authorized licensed use limited to: CZECH TECHNICAL UNIVERSITY. Downloaded on April 29,2026 at 09:07:50 UTC from IEEE Xplore.  Restrictions apply.

2340 IEEETRANSACTIONSONPOWERSYSTEMS,VOL.35,NO.3,MAY2020
| a given         | parametric | model.       | Trading      |            | for a pumped |               | hydro   |     |     |     |
| --------------- | ---------- | ------------ | ------------ | ---------- | ------------ | ------------- | ------- | --- | --- | --- |
| storage         | facility   | is presented |              | in [15]    | and [16].    | The           | first   |     |     |     |
| paper discusses |            | the          | optimization |            | problem      | of pumped     |         |     |     |     |
| hydro storage   |            | trading,     | where        | it is      | assumed      | that          | traders |     |     |     |
| can access      | a forward  |              | curve.       | The second |              | paper         | studies |     |     |     |
| the problem     | of         | trading      | in the       | CIM        | and in       | the balancing |         |     |     |     |
market.Otherpapersdeveloptradingstrategiesforother
| types of | asset.        | In [17], | the | authors  | consider | trading      | in                                                                |     |     |     |
| -------- | ------------- | -------- | --- | -------- | -------- | ------------ | ----------------------------------------------------------------- | --- | --- | --- |
|          |               |          |     |          |          |              | Fig.1. ThesequenceofoperationsinatypicalcentralEuropeanshort-term |     |     |     |
| the CIM  | for balancing |          | the | forecast | error    | of renewable |                                                                   |     |     |     |
electricitymarket.
energy.Theauthorsassumethattheintradaypricefollows
| a geometric | Brownian |       | motion.      | A   | trading  | strategy | for |     |     |     |
| ----------- | -------- | ----- | ------------ | --- | -------- | -------- | --- | --- | --- | --- |
| a thermal   | power    | plant | is developed |     | in [18], | where    | it  |     |     |     |
policy.InsectionVI,wepresentatestcasewhichdemonstrates
| is assumed | that | the intraday |     | price | follows | an additive |     |     |     |     |
| ---------- | ---- | ------------ | --- | ----- | ------- | ----------- | --- | --- | --- | --- |
theeffectivenessofourapproachonGermanmarketdata,and
Brownianmotion.Thispriceisfurtherinfluencedbythe
|     |     |     |     |     |     |     | we analyze how | our proposed | policy fares | relative to rolling |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------------ | ------------ | ------------------- |
mostrecenttradesoftheproducer.
|     |     |     |     |     |     |     | intrinsic. Finally, | in section | VII we conclude | the paper and |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | ---------- | --------------- | ------------- |
iii) Thethirdstrandofliteraturefocusesondevelopingtrad-
proposedirectionsforfurtherresearch.
ingstrategies,withoutplacingassumptionsonthepara-
metricdistributionofthedata.In[19]theauthorspropose
aheuristictradingmethodforwindpowerproducers.The II. CONTINUOUSINTRADAYELECTRICITY
authors in [20] consider the problem of trading without MARKETSOPERATION
assets in the CIM in order to cover a position in the In this section, we describe the operation of a continuous
| imbalance | market. | The | authors | model | the | problem | as  |     |     |     |
| --------- | ------- | --- | ------- | ----- | --- | ------- | --- | --- | --- | --- |
intradaymarket.WebaseourdescriptionontheGermanmarket,
a one-stage MDP, and solve it using policy functions. whichisrepresentativeoftheoperationofelectricitymarketsin
RelatedtoMDP,twopapershavemodelledtheproblem
CentralEurope.
oftradingforastorageunitintheCIMusingMDP[21],
[22].Thefirstonereliesonvaluefunctionapproximation.
A. Short-TermElectricityMarketDescription
Thesecondoneresortstopolicyfunctionapproximation
intheformofathresholdpolicyinordertosimplifythe In Fig. 1 we describe the timing of the different short-term
problem. electricity markets in a typical central European power ex-
Inthepresentpaper,weconsiderageneralizationoftheprob- change.WeuseindicativevaluesfortheGermanmarket.Short-
lemthatispresentedin[22],whereweadditionallyaccountfor term market trading commences with the day-ahead market at
round-trip efficiency losses of storage units. The contributions 12noon,thedaybeforeelectricitydelivery(D-1)[23].Subse-
ofthispaperarethefollowing:(i)Wecasttheintradaymarket quently, the intraday auction takes place at 3PM on D-1 [24].
tradingproblemforastorageunitintheMDPframework.(ii) Followingtheconclusionoftheintradayauction,thecontinuous
Weemploypolicyfunctionapproximationinordertoarriveata intradaymarket(whichisaseparateprocessfromtheintraday
computationallytractableproblemformulation.Moreprecisely, auction)commencesat3PMforhourlyproductsandat4PM
we use a threshold policy according to which we seek a sell for quarter-hourly products [3]. The CIM closes 30 minutes
threshold above which we accept to sell power, and a buy beforedelivery.Finally,theimbalanceisclearedattheimbalance
| thresholdbelowwhichweaccepttobuypower.(iii)Wepropose |     |     |     |     |     |     | price[25]. |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- |
a parametrization of the trading thresholds that accounts for In this paper, we consider trading only in the continuous
severaleffects,inordertoarriveatapolicythatoutperformsa intraday market. In the CIM, at any moment, the traders have
benchmarkpolicyreferredtoasrollingintrinsic.(iv)Weanalyse accesstoanorderbook.Thisorderbookisthelistofallavailable
theresultsathighertradingfrequencythantheoneconsidered bidsontheCIM.Atanymoment,atradercansubmitnewbids
in [22]: whereas in [22] the results are derived using hourly oraccept(partiallyorfully)existingbids.Thebidsavailableon
frequency,inthepresentpublicationweconsiderafrequencyof themarkethave4characteristics:(i)adeliverytime,whichisthe
5 minutes for learning and 1 second for testing out of sample. momentatwhichthepowershouldbeinjectedtoorwithdrawn
Moreover, we demonstrate through experiments the important fromthegrid;(ii)thetypeofbid(sell/buy):asell(resp.buy)bid
role of frequency on the training and evaluation of trading correspondstoanofferfromacounter-partytosell(resp.buy)
power;(iii)thepriceofabid(in€/MWh);and(iv)thequantity
strategies.
SectionIIdescribestheoperationofthecontinuousintraday ofabid(inMWh).
market and how we simulate it. Section III explains how to Weareinterestedinthedevelopmentoftradingstrategiesfor
modelthetradingproblemfacedbyastorageunitintheMDP astorageassetowner.Astorageunitisanespeciallyinteresting
framework.InsectionIV,weintroducetheideaofathreshold assettoconsiderinthecontextofintradaytrading,sinceitoffers
policy, in order to arrive to a tractable problem for optimizing thepossibilitytoprocurepowerfromrelativelycheapsellbids,
over policies. We also recall the REINFORCE algorithm for store the power, and sell it back to subsequent buy bids that
optimizing the policy function parameters. Section V presents place a greater valuation on the procured power. We consider
the factors that we propose in order to adapt the threshold thefollowingsimplificationsinthesequel:
Authorized licensed use limited to: CZECH TECHNICAL UNIVERSITY. Downloaded on April 29,2026 at 09:07:50 UTC from IEEE Xplore.  Restrictions apply.

BERTRANDANDPAPAVASILIOU:ADAPTIVETRADINGINCONTINUOUSINTRADAYELECTRICITYMARKETSFORASTORAGEUNIT 2341
1) Thetradingstrategiesthatwedeveloparebalanced.This inlinewiththestateoftheartonthetopicofintradaytrad-
impliesthat,attheclosingtimeofthecontinuousintraday ing in electricity markets [15], [19]. Moreover, we have
market,thepositionofthestorageunitshouldbefeasible. assessedthevalidityofthisassumption intheelectronic
| WethusadheretoGermanregulation[25],whichrequires |     |     |     |     |     |     | supplement.2 |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
thattheproducercanonlybeinimbalanceifthisimbal-
anceiscausedbyanunpredictableevent1 (forecasterror, B. MarketSimulation
| outages). | Practically, |     | this implies | that | if we | do not have |          |     |          |               |     |              |          |
| --------- | ------------ | --- | ------------ | ---- | ----- | ----------- | -------- | --- | -------- | ------------- | --- | ------------ | -------- |
|           |              |     |              |      |       |             | In order | to  | simulate | the evolution |     | of the order | book, we |
anyenergystoredinourreservoir,wecannotsellpower
consider4typesofevents:
andcoveritintheimbalancemarket.
1) Open:theappearanceofatrade
2) Weonlyacceptbidsthatarealreadypresentinthemarket,
2) Cancel:thedisappearanceofatrade
| as opposed | to  | also placing | bids | in  | the market. | Adding |     |     |     |     |     |     |     |
| ---------- | --- | ------------ | ---- | --- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- |
3) Acceptance:theacceptanceofacertainquantityofabid
theoptionofplacingbidswouldcomplexifyourMarkov
|     |     |     |     |     |     |     | 4) Trading: |     | the moment | when | we  | decide which | bids we |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---------- | ---- | --- | ------------ | ------- |
DecisionProcessin2ways:(i)Wewouldhavetoaddto
accept.
| our state | all the | bids | that we | have placed | on  | the market |     |     |     |     |     |     |     |
| --------- | ------- | ---- | ------- | ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Thesimulationofthemarketcannowbedescribedasfollows.
atprevioustimesteps.(ii)Wewouldneedtoextendour
Atthebeginningofthesimulation,werankalltheevents,which
actionspaceinordertodecideonsuppressingthebidsthat
|     |     |     |     |     |     |     | areincludedinthesetEvent,chronologically. |     |     |     |     | Wetheniterate |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | ------------- | --- |
wehaveplacedatprevioustimesteps.
|     |     |     |     |     |     |     | on this set: | for | each new | event | j, we classify | it in | one of the |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | ----- | -------------- | ----- | ---------- |
3) Inpractice,CIMbidsarecategorizedintomorecomplex
|     |     |     |     |     |     |     | 4 categories | and | we update | the | order book | as described | in the |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------- | --- | ---------- | ------------ | ------ |
products,referredtoascontinuousbids,all-or-nonebids,
followingprocedure.
| block bids, | iceberg |     | bids, and | so on | [3]. | For our case |     |     |     |     |     |     |     |
| ----------- | ------- | --- | --------- | ----- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- |
L=[]
| study, we      | assume | that          | all the | data       | that we | have access |     |     |     |     |     |     |     |
| -------------- | ------ | ------------- | ------- | ---------- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| to corresponds |        | to continuous |         | bids. This | implies | that we     |     |     |     |     |     |     |     |
forj ∈Event
| can accept | fractions |     | of bids. | There | are two | reasons for |     |     |     |     |     |     |     |
| ---------- | --------- | --- | -------- | ----- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
∈Open
| adoptingthissimplification:(i)Theinformationaboutthe |                   |        |          |        |        |               |     | ifj |         |     |     |     |     |
| ---------------------------------------------------- | ----------------- | ------ | -------- | ------ | ------ | ------------- | --- | --- | ------- | --- | --- | --- | --- |
| type of                                              | bids (continuous, |        | integer, | block) | is     | not disclosed |     |     |         |     |     |     |     |
|                                                      |                   |        |          |        |        |               |     |     | Addbidj | toL |     |     |     |
| in the German                                        |                   | market | data set | that   | we use | for our case  |     |     |         |     |     |     |     |
study.(ii)Practitionershaveindicatedtousthattheimpact elseifj ∈Close
| of this restriction |       | is minor, | because   |         | most of  | the bids are |     |     |            |       |     |     |     |
| ------------------- | ----- | --------- | --------- | ------- | -------- | ------------ | --- | --- | ---------- | ----- | --- | --- | --- |
|                     |       |           |           |         |          |              |     |     | Removebidj | fromL |     |     |     |
| continuous          | bids. | To        | a certain | extent, | the more | complex      |     |     |            |       |     |     |     |
products have been inherited from the products that are elseifj ∈Acceptance
| available | in the | day-ahead | market. |     | A major | reason for |     |     |     |     |     |     |     |
| --------- | ------ | --------- | ------- | --- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Reducepartiallyacceptedquantityfrombidj
theexistenceofthesecomplexproductsintheday-ahead
|     |     |     |     |     |     |     |     | elseifj | ∈Trading |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | --- | --- | --- | --- |
marketisinordertoprovidetheoptionforaproducerto
| account | for complex |     | unit commitment |     | constraints. | This |     |     |     |     |     |     |     |
| ------- | ----------- | --- | --------------- | --- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- |
Launchthetradingalgorithm
interestismorelimitedintheCIM,becausethecommit-
ment variables have to be decided several hours before RemovethebidsthatwehaveacceptedfromL
delivery,throughtheso-callednominationprocedure.
end
4) Weonlyconsiderhourlyproductsinourpaper,asopposed
| toalsoconsideringquarterlyproductsthatrefertodelivery |     |     |     |     |     |     | end |     |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
withinaspecific15-minuteinterval.
5) Weassumethatourproducerisrisk-neutral.Thereasonfor III. MODELLINGTHEINTRADAYTRADINGPROBLEMUSING
thisisthatthedailyaverageprofitobtainedforourstorage THEMDPFRAMEWORK
unitisaround6400€,whereastheprofitfortheworstday
|     |     |     |     |     |     |     | Having | defined | how | to simulate | the | market, we | can now |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------- | --- | ----------- | --- | ---------- | ------- |
isapproximately−500€.Typicalenergycompanieshave
analysethetradingproblem.Thedecisionproblemistodecide,
thefinancialabilitytoabsorbthispotentiallossforseveral
atdifferentmomentsoftheContinuousIntradayMarket,which
| days without | any | problem. | Therefore, |     | the | company can |     |     |     |     |     |     |     |
| ------------ | --- | -------- | ---------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
bidsshouldbeacceptedinordertomaximizethefutureexpected
onlyfocusonmaximizingitslong-termprofit,whichwill
|     |     |     |     |     |     |     | profit of | our storage | unit. | In the | rest of | the paper, | we refer to |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | ----- | ------ | ------- | ---------- | ----------- |
beobtainedbybeingriskneutralonadailybasis.
|              |       |     |              |     |     |               | a general | storage  | unit. | This storage | unit        | is characterized | by       |
| ------------ | ----- | --- | ------------ | --- | --- | ------------- | --------- | -------- | ----- | ------------ | ----------- | ---------------- | -------- |
| 6) We assume | that, | no  | matter which | bid | we  | accept in the |           |          |       |              |             |                  |          |
|              |       |     |              |     |     |               | a certain | charging | and   | discharging  | efficiency. | These            | settings |
market,wedonotinfluencethebidsthattheotheractors
createthebasisforrepresentingabattery,asimplifiedmodelofa
willplacelaterinthemarket.Thissimplificationhasbeen pumpedstoragehydrounit,orcertaintypesofdemandresponse.
adoptedinordertosimplifytheproblem,andiscompletely
Themaintrade-offforourdecisionproblemisthefollowing:Do
wewanttotradepoweratthecurrentpriceandlockintheprofit?
1NotethatUSmarketoperationsdifferinthisrespectduetocentraldispatch,
2The
whichallowsthesystemoperatortoactivelymanageresourcesinrealtimein electronic supplement is available at the following link:
ordertoincreasetradingsurplus,asopposedtorequiringthemtoremainin https://sites.google.com/site/gillesbertrandresearch/publications/app-
| balanceatallcosts. |     |     |     |     |     |     | transaction-2019 |     |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: CZECH TECHNICAL UNIVERSITY. Downloaded on April 29,2026 at 09:07:50 UTC from IEEE Xplore.  Restrictions apply.

| 2342 |     |     | IEEETRANSACTIONSONPOWERSYSTEMS,VOL.35,NO.3,MAY2020 |     |     |     |     |     |     |
| ---- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
Orisitworthwaitingforapotentialfuturebidthepriceofwhich Notethattheround-tripefficiencyofastorageunitispartofthis
would be more advantageous, despite the risk that the current transitionfunction,whichwedonotmodelexplicitly.
favorablebidsmaydisappear?Ourdecisionproblemfallsunder
thescopeofmultistageoptimizationunderuncertainty,because
IV. POLICYFUNCTIONAPPROXIMATION
weneedtoarrivetodecisionsknowingthatrecourseactionscan
Weareinterestedinanoptimalpolicyfortrading.Apolicyisa
beadoptedinanuncertainfuture.Acommonwaytoapproach
functionwhichisadistributionoveractionsforeverystateofthe
thisclassofproblemsisbyusingtheMarkovDecisionProcess
MDP.ThepolicyshouldbeselectedamongasetofpoliciesΠ,
framework.InordertocharacterizeanMDP,weneedtomodel
suchthatwemaximizethefutureexpectedrewardinEq.(1)
thestatevariables,theactionvariables,therewardandthestate
| transitionfunction. |     |     |     |     | (cid:2)T |            |           |     |     |
| ------------------- | --- | --- | --- | --- | -------- | ---------- | --------- | --- | --- |
|                     |     |     |     |     | max      | E[Rt (St,A | π(St ))], |     | (1) |
| A. StateVariables   |     |     |     |     | π∈Π      |            |           |     |     |
t=1
Inordertoreachadecisionattimestept,werequire3ingre- where Aπ(St ) is the action taken if we are in state St and we
dientsinourstateSt:(i)Theoffersavailableinthecontinuous followthepolicyπ.
intradaymarketattimestept.Thisdataisavailableinthemarket In our case, we have infinite states, since the prices
order book. (ii) A variable vt−1,d,∀d∈D which indicates the for the different delivery times are continuous. Therefore,
capacitythatwouldbestoredinthestorageunitatdeliveryhour
|     |     |     | the problem | of  | finding | an optimal | policy | becomes | infinite- |
| --- | --- | --- | ----------- | --- | ------- | ---------- | ------ | ------- | --------- |
difwewereonlyexecutingthetradesdecidedattimestept−1
|     |     |     | dimensional | [26], | [27]. Thus, | the | problem | as expressed | in its |
| --- | --- | --- | ----------- | ----- | ----------- | --- | ------- | ------------ | ------ |
orearlier.Thisvaluecanbeeasilycomputedbasedontheresults initialformulationisintractable.
ofallthetradesthatwehaverealizedinthepast.(iii)Exogenous In order to obtain an approximate solution to the problem,
data that we anticipate should influence our decision. Some weresorttopolicyfunctionapproximation.Theideaofpolicy
| examplesoftheseexogenousparametersincludetheremaining |     |     |          |               |     |               |            | (a|s) |      |
| ----------------------------------------------------- | --- | --- | -------- | ------------- | --- | ------------- | ---------- | ----- | ---- |
|                                                       |     |     | function | approximation |     | is to express | the policy | πθ    | with |
timebeforemarketclosure,andthepriceoftheintradayauction. respecttoaparametervectorθ,andtooptimizeoverthisθ:
Thefulllistoftheseparameters,andthewayinwhichweuse
|     |     |     |     | πθ  | (a|s)=P[At | =a|St | =s;θ]. |     |     |
| --- | --- | --- | --- | --- | ---------- | ----- | ------ | --- | --- |
them,isdiscussedinSectionV.
Wethusrestrictthepolicydomain,whichimpliesthatwewill
B. ActionVariables
|     |     |     | obtain a | policy which | may | be sub-optimal, |     | which is | the cost |
| --- | --- | --- | -------- | ------------ | --- | --------------- | --- | -------- | -------- |
InordertomodelouractionAt,werequireoneactionvariable of restricting our search over θ. The remainder of this section
at,d for each delivery time d. This action indicates how much explainshowwecalibratetheweightsθonthebasisofrepeated
we wish to sell at time step t. In theory, this variable can be episodes of trading and how we implement a threshold policy
continuous.But,inordertoreducethesizeoftheactionspace, forourtradingproblem.
wewilldiscretizethisvariableinto2n+1potentialactions:
A. REINFORCEAlgorithm
at,d ∈{−qn,...,−q1,0,q1,···qn }
|           |     |     | In order            | to optimize |     | the parameter | vector | θ, we | use the |
| --------- | --- | --- | ------------------- | ----------- | --- | ------------- | ------ | ----- | ------- |
| C. Reward |     |     | REINFORCEalgorithm: |             |     |               |        |       |         |
(cid:2)
(cid:2) Initializeθ
ThetotalrewardobtainedfromtheCIMattimesteptisequal {s1,a1,r2,...,sT−1,aT−1,rT }∼
|     |     |     | for | each | episode |     |     |     |     |
| --- | --- | --- | --- | ---- | ------- | --- | --- | --- | --- |
tothesumoftherewardsobtainedforeverydeliveryhour:
πθ (a|s)
(cid:2)
fort=1:T-1do
| Rt (St,At | )=  | rev(at,d ), |     |     |       |           |          |     |     |
| --------- | --- | ----------- | --- | --- | ----- | --------- | -------- | --- | --- |
|           | d∈D |             |     |     | =θ+γt | ∇ θlog(πθ | (a|s))gt |     |     |
|           |     |             |     |     | θ     |           |          |     | (2) |
wheretherewardfordeliveryhourdattimesteptiscomputed
| astheintegralofthedemandcurvept,d |         | from0toat,d: |     | end |     |     |     |     |     |
| --------------------------------- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
|                                   | (cid:3) |              | end |     |     |     |     |     |     |
a
t,d
rev(at,d )= pt,d (z)dz. The REINFORCE algorithm adapts the parameter vector θ
|     | 0   |     | so as to | maximize | expected | rewards | from | a certain | policy, |
| --- | --- | --- | -------- | -------- | -------- | ------- | ---- | --------- | ------- |
basedonrepeatedepisodesofthedecisionprocess.Anepisode
D. StateTransitionFunction
|     |     |     | corresponds | to one | day of | trading. | The episode | commences | at  |
| --- | --- | --- | ----------- | ------ | ------ | -------- | ----------- | --------- | --- |
In the case of the intraday trading problem, we assume that thefirsttradingintervaloftheday.Givenastates1,weselectan
there exists a state transition function but that it is unknown actionbasedonourpolicyfunction,wecollectarewardr2,and
(since we do not place any assumptions on the evolution of wearriveatthestates2.Thisprocessisrepeateduntiltheendof
intradayprices).Thisprohibitsusfromusingmethodssuchas thetradingday.Whentheepisodeisfinished,weupdateθusing
policyiterationorvalueiteration.Nevertheless,Reinforcement Eq.(2),wheregtistheprofitfromtuntiltheendoftheepisode
Learning techniques are perfectly suitable for such a setting. T. It has been proven in [28] that the REINFORCE algorithm
Indeed,theideaofReinforcementLearningtechniquesistogain is effectively a stochastic gradient algorithm. It is therefore
knowledge about the environment by running episodes of the guaranteedtoconvergeunderstandardstochasticapproximation
task(inourcase,eachepisodecorrespondstoadayoftrading). conditionsfordecreasingstep-sizesγt.
Authorized licensed use limited to: CZECH TECHNICAL UNIVERSITY. Downloaded on April 29,2026 at 09:07:50 UTC from IEEE Xplore.  Restrictions apply.

BERTRANDANDPAPAVASILIOU:ADAPTIVETRADINGINCONTINUOUSINTRADAYELECTRICITYMARKETSFORASTORAGEUNIT 2343
B. ThresholdPolicy
| We         | focus       | on a policy | which         | is       | parametrized | by       | buy and     |     |     |     |     |
| ---------- | ----------- | ----------- | ------------- | -------- | ------------ | -------- | ----------- | --- | --- | --- | --- |
| sell price | thresholds. |             | The threshold |          | policy       | that we  | investigate |     |     |     |     |
| in this    | paper       | accepts     | sell bids     | if their | price        | is below | a buy       |     |     |     |     |
| threshold, | and         | accepts     | buy           | bids if  | their price  | is above | a sell      |     |     |     |     |
threshold.Ourfocusonthresholdpoliciesisjustifiedbyseveral
| factors: | (i) Optimal | inter-temporal |     | arbitrage |     | in a deterministic |     |     |     |     |     |
| -------- | ----------- | -------------- | --- | --------- | --- | ------------------ | --- | --- | --- | --- | --- |
settingisachievedbyathresholdpolicy,asprovedin[22].This
resulthasbeenextendedtoathree-stagestochasticprogramin
theelectronicsupplementofthispaper.(ii)Thresholdpolicies
| have also | been | proven | to be | optimal | in a number | of  | papers in |     |     |     |     |
| --------- | ---- | ------ | ----- | ------- | ----------- | --- | --------- | --- | --- | --- | --- |
theliteratureregardingspecificinstancesofstochasticoptimal
controlproblemswithuncertainprices[29]–[31].(iii)Theidea
| of using | a threshold | policy | in  | order | to trade | for a storage | unit |     |     |     |     |
| -------- | ----------- | ------ | --- | ----- | -------- | ------------- | ---- | --- | --- | --- | --- |
hasalreadybeenproposedinothersettings[32].
| We  | apply | a stochastic | threshold |     | policy, | in order | to ensure |     |     |     |     |
| --- | ----- | ------------ | --------- | --- | ------- | -------- | --------- | --- | --- | --- | --- |
sufficientexplorationtotakeplaceduringthelearningstageof Fig.2. Thresholdpolicyforthehydroproblemifweconsiderfourpossible
actions:sell0,10,20or30MWh.Thebellcurveindicatestheprobabilitydensity
thealgorithm.Concretely,weproposedrawingthesellandbuy
functionofthesellthreshold.Thetwolightgreysegmentsandthetwodarkgrey
| thresholds | from | a Gaussian |     | distribution. | Therefore, |     | we define |     |     |     |     |
| ---------- | ---- | ---------- | --- | ------------- | ---------- | --- | --------- | --- | --- | --- | --- |
segmentsofthebellcurveindicatetheprobabilityofeachofthefouractions.
our policy parameter, θ, as θ =(μX,σX,μY,σY ),where the Thesolidblackdecreasingfunctioncorrespondstothebuybidsthatareavailable
intheorderbook.
| buy threshold                                |     | for delivery | hour | d,     | Xd, is drawn | according | to        |     |     |     |     |
| -------------------------------------------- | --- | ------------ | ---- | ------ | ------------ | --------- | --------- | --- | --- | --- | --- |
| anormaldistributionwithparameters3(μX,exp(σX |     |              |      |        |              |           | )),andthe |     |     |     |     |
| sell threshold                               |     | for delivery | hour | d, Yd, | is drawn     | according | to a      |     |     |     |     |
whereΦ(·;μ,σ)indicatesthecumulativedistributionfunction
| normal | distribution | with | parameters |     | (μY,exp(σY | )). | We draw |     |     |     |     |
| ------ | ------------ | ---- | ---------- | --- | ---------- | --- | ------- | --- | --- | --- | --- |
one independent threshold per delivery hour d, therefore an ofthenormaldistributionwithmeanμandstandarddeviation
σ.InordertoapplytheREINFORCE4algorithm,wealsoneed
actionatdeliverytimed1isindependentoftheactionatdelivery
time d2. By independence, the distribution of actions over all tocomputethepolicyderivativesforthedifferentactions.These
derivativescanbecomputedanalyticallyasillustratedbelowfor
futuredeliveryhourscanbeexpressesas:
(cid:4)
thederivativeoftheprobabilityoftheactionSell10MWhwith
|     |     | πθ  | (a|s)= | π   | d(a|s) |     |              |     |     |     |     |
| --- | --- | --- | ------ | --- | ------ | --- | ------------ | --- | --- | --- | --- |
|     |     |     |        |     | θ      |     | respecttoμY: |     |     |     |     |
d∈D
|     |     |     |     |     |     |     |     | ∂π d(10|s) | ∂Φ(p(5);μY,exp(σY |     | ))  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------------- | --- | --- |
In order to illustrate how the stochastic threshold is imple- θ =
| mented,weconsidertheexampleofFig.2.atdeliveryhourd. |     |     |     |     |     |     |     | ∂μY |     | ∂μY |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(i)Thesolidblackdecreasingfunction(solidline)corresponds ∂Φ(p(15);μY,exp(σY ))
−
tothebuybidsthatareavailableintheorderbookfordelivery
∂μY
| hour d.      | This          | data is available |     | in the | order book | at the   | time we    |     |                     |     |     |
| ------------ | ------------- | ----------------- | --- | ------ | ---------- | -------- | ---------- | --- | ------------------- | --- | --- |
|              |               |                   |     |        |            |          |            |     | = −φ(p(5);μY,exp(σY |     | ))  |
| are deciding |               | on whether        | or  | not to | accept a   | bid. The | demand     |     |                     |     |     |
| curve        | is associated | with              | the | lower  | x-axis.    | (ii) The | bell curve |     |                     |     |     |
|              |               |                   |     |        |            |          |            |     | +φ(p(15);μY,exp(σY  |     | ))  |
representstheprobabilitydensityfunctionofthethreshold.This
curvecanbecomputedbasedonthecurrentvectorparameterθ. whereφ(·;μ,σ)denotestheprobabilitydensityfunctionofthe
| The bell | curve | is associated |     | with the | upper | x-axis. | With these |     |     |     |     |
| -------- | ----- | ------------- | --- | -------- | ----- | ------- | ---------- | --- | --- | --- | --- |
normaldistributionwithmeanμandstandarddeviationσ.
twoelements,weillustratehowweusethethresholdpolicyin
ordertoarriveatdecisions.Consider,forinstance,theactionSell
V. FACTORSDRIVINGTHEOPTIMALTHRESHOLD
10MWh:ifthesellthresholdthatwedrawisbetweentheprice
Intheprevioussection,wehavedevelopedabasicthreshold
associatedtoasellquantityof15MWhandthepriceassociated
toasellquantityof5MWh,wesell10MWh.Theprobabilityof policyfortradingintheCIM.Thissimplethresholdpolicydoes
thisactioncorrespondstothelightgreysurfaceπd(10|s).This not achieve satisfactory performance in practice, because it is
θ
probabilitycanalsobecomputedmathematically,asillustrated not sufficient to maintain the same threshold for every time
below: step of every day. This suggests that the threshold should be
furtherdependentoncertainfactorsthatarepertinenttowardsan
d(10|s)(cid:2)Pr(at,d
| π   |     | =10) |     |     |     |     |                                                        |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- |
| θ   |     |      |     |     |     |     | adaptivetradingstrategy.Inthissection,weproposeanumber |     |     |     |     |
=Pr(p(15)≤Yd ≤p(5)) of such factors and explain the reason for which we consider
them.Then,weexplainhowtheREINFORCEalgorithmcanbe
|     | =Pr(Yd | ≤p(5))−Pr(Yd |     |     | ≤p(15)) |     |     |     |     |     |     |
| --- | ------ | ------------ | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
adaptedinordertoincorporatethesefactors.
|             | =Φ(p(5);μY,exp(σY |          |     | ))−Φ(p(15);μY,exp(σY |     |     | ))  |     |     |     |     |
| ----------- | ----------------- | -------- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
| 3Weuseexp(σ |                   | )andnotσ |     |                      |     |     |     |     |     |     |     |
X X directlyinordertoensurethatthestandard 4Wepresentanexampleofallthecomputationsneededinordertorealize
deviationremainspositive. oneiterationoftheREINFORCEalgorithmintheelectronicsupplement.
Authorized licensed use limited to: CZECH TECHNICAL UNIVERSITY. Downloaded on April 29,2026 at 09:07:50 UTC from IEEE Xplore.  Restrictions apply.

| 2344 |     |     |     |     |     |     |     | IEEETRANSACTIONSONPOWERSYSTEMS,VOL.35,NO.3,MAY2020 |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Fig.3. Thedeliverytimeofanorderimpactsitsthreshold:buyingpowerat Fig.5. Continuousintradaymarketpricefortwodifferentdays.Thecurves
30€/MWhisnotworthwhileinhour6,butitisworthwhileinhour17.
correspondtodifferentaveragevalues,thereforedifferentthresholdsneedtobe
appliedforaneffectivethresholdstrategy.
|     |     |     |     |     |     |     |     |                                           |         | μk  |     | μk. |               |     |          |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | ------- | --- | --- | --- | ------------- | --- | -------- |
|     |     |     |     |     |     |     |     | are thus                                  | denoted | as  | and | In  | the remainder |     | of this  |
|     |     |     |     |     |     |     |     |                                           |         |     | X   | Y   |               |     |          |
|     |     |     |     |     |     |     |     | section,wewillexpressthesethresholdmeans5 |         |     |     |     |               | μk  | andμk as |
|     |     |     |     |     |     |     |     |                                           |         |     |     |     |               | X   | Y        |
(αs,αb,αs,
|     |     |     |     |     |     |     |     | a function | of  | 10 parameters, |     | which we | denote | as  | 1 1 2 |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------------- | --- | -------- | ------ | --- | ----- |
αb,αs,αb,αs,αb,αs,αb).
|     |     |     |     |     |     |     |     |     |     |     |     | We will | then | show | how the |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---- | ---- | ------- |
|     |     |     |     |     |     |     |     | 2 3 | 3 4 | 4 5 | 5   |         |      |      |         |
REINFORCEalgorithmcanbeusedinordertolearnthevalues
oftheparametervectorα.
Fig.4. Buyregime(left),andsellregime(right)basedontheintradayauction B. IntradayAuctionCurve
price.
|     |     |     |     |     |     |     |     | Our motivation |     | for | using | the intraday | auction |     | curve as a |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | ----- | ------------ | ------- | --- | ---------- |
featurefordeterminingthresholdsisillustratedinFig.5,where
A. DeliveryTime wepresenttheCIMpricefortwodifferenttradingdays.From
thisgraphitisclearthatitisnotpossibletosetasinglethreshold
| The need | for     | using       | different | thresholds   | depending |            | of the |             |            |               |     |            |         |     |             |
| -------- | ------- | ----------- | --------- | ------------ | --------- | ---------- | ------ | ----------- | ---------- | ------------- | --- | ---------- | ------- | --- | ----------- |
|          |         |             |           |              |           |            |        | which would | perform    | well          | for | both days, | because |     | the average |
| delivery | hour is | illustrated | in        | Fig. 3. This | graph     | represents | the    |             |            |               |     |            |         |     |             |
|          |         |             |           |              |           |            |        | level of    | the curves | is different. |     | In order   | to set  | an  | appropriate |
CIMprice(whichwedefineasthecenterofthebid-askspread)
baselevelforthethresholds,weusetheintradayauctionprice.
forthe24differentdeliveryhours.Thecrossrepresentstheprice
|           |        |        |           |       |         |        |          | The idea   | is that | the price | of  | previous    | markets | can  | provide an  |
| --------- | ------ | ------ | --------- | ----- | ------- | ------ | -------- | ---------- | ------- | --------- | --- | ----------- | ------- | ---- | ----------- |
| of buying | energy | at the | 6th hour, | while | the dot | is the | price of |            |         |           |     |             |         |      |             |
|           |        |        |           |       |         |        |          | indication | about   | the state | of  | the market, | and     | thus | support the |
17th
| buying energy | at  | the | hour. | These | two | prices | are equal, |     |     |     |     |     |     |     |     |
| ------------- | --- | --- | ----- | ----- | --- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
forecastofthepriceforsubsequentmarket-clearingstages.This
| however | the buying | decision |     | should | be different. | Indeed, | the |     |     |     |     |     |     |     |     |
| ------- | ---------- | -------- | --- | ------ | ------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
observationhasbeeninspiredby:(i)reference[33],wherethe
pricecorrespondingtothecrossisnotinteresting,becausethe
authorsfindastrongcorrelationbetweentheday-aheadmarket
sameamountofpowercouldhavebeenprocuredandstoredat
|     |     |     |     |     |     |     |     | and the | balancing | market; | and | (ii) reference |     | [9], | where the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ------- | --- | -------------- | --- | ---- | --------- |
thereservoiratalowerpriceathour4.Onthecontrary,theprice
authorsusetheday-aheadpriceinordertoforecasttheimbalance
| corresponding | to  | the dot | is interesting, |     | because | it corresponds |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ------- | --------------- | --- | ------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
price.
toalocalminimumprice.Thus,inhour17wecanbuypower,
|     |     |     |     |     |     |     |     | Motivated | by  | this observation, |     | we  | propose | an adaptation | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ----------------- | --- | --- | ------- | ------------- | --- |
inordertosellthatpowerbackatalaterdeliverytime.
thethresholdsasfollows:
Havingarguedthatitisnecessarytoemploydifferentthresh-
|     |     |     |     |     |     |     |     |     |     | k   |     | s(p |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
oldsfordifferentdeliverytimes,ourideaistodefineregimesfor μ ←p min,k +α max,k −p min,k )
|                                                       |           |      |        |     |           |     |             |     |     | X     |     | 1     |       |     |     |
| ----------------------------------------------------- | --------- | ---- | ------ | --- | --------- | --- | ----------- | --- | --- | ----- | --- | ----- | ----- | --- | --- |
| which the                                             | threshold | mean | should | be  | the same. | We  | will define |     |     |       |     |       |       |     |     |
|                                                       |           |      |        |     |           |     |             |     |     | k ←p  | −α  | b(p   | −p    | )   |     |
|                                                       |           |      |        |     |           |     |             |     | μ   | max,k |     | max,k | min,k |     |     |
| theseregimesbasedontheintradayauctionpricecurve,which |           |      |        |     |           |     |             |     |     | Y     |     | 1     |       |     |     |
conveys a significant amount of information about the CIM min,kistheminimumofthekthbuyregimeoftheintraday
wherep
price. auctioncurve,p max,k isthemaximumofthekth sellregimeof
| Wepresentanexampleoftheseregimesbasedontheintraday |     |     |     |     |     |     |     |                              |     |     |     | s/b                       |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | ------------------------- | --- | --- | --- |
|                                                    |     |     |     |     |     |     |     | theintradayauctioncurve,andα |     |     |     | 1 aretheweightsthatwillbe |     |     |     |
auctionpricecurve,foroneprecisedayofourdataset,inFig.4.
optimizedusingtheREINFORCEalgorithm.
| These graphs | illustrate |       | that   | the buy threshold |           | switches | at the |          |                 |      |                 |       |         |        |              |
| ------------ | ---------- | ----- | ------ | ----------------- | --------- | -------- | ------ | -------- | --------------- | ---- | --------------- | ----- | ------- | ------ | ------------ |
|              |            |       |        |                   |           |          |        | The idea | behind          | this | parametrization |       | is      | that p | min,k (resp. |
| maximum      | of the     | price | curve, | since             | any power | that     | we buy |          |                 |      |                 |       |         |        |              |
|              |            |       |        |                   |           |          |        | p max,k) | is a reasonable |      | starting        | point | for the | buy    | (resp. sell) |
between two maxima can be sold at the second maximum. threshold because it is the best price that could have been
Similarly,thesellthresholdswitchesattheminimumoftheprice
|     |     |     |     |     |     |     |     | obtained | in the | intraday | auction | for regime |     | k. Then, | with the |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | -------- | ------- | ---------- | --- | -------- | -------- |
curve,becauseanypowerthatwesellbetweentwominimacan
parameterαs(resp.αb)weallowtheREINFORCEalgorithmto
1 1
beboughtatthefirstminimum.
Theintroductionofregimesimpactstheparametervectorθ.
5Incontrasttothemean,wedonotmakethestandarddeviationdependent
Since we introduce different thresholds for the different onexogenousparameters.Thisisduetothefactthatthestandarddeviationis
regimes, μX and μY are now indexed by the regime k, and onlyusedinordertoensuresufficientexplorationinthelearningphase.
Authorized licensed use limited to: CZECH TECHNICAL UNIVERSITY. Downloaded on April 29,2026 at 09:07:50 UTC from IEEE Xplore.  Restrictions apply.

BERTRANDANDPAPAVASILIOU:ADAPTIVETRADINGINCONTINUOUSINTRADAYELECTRICITYMARKETSFORASTORAGEUNIT 2345
determinetowhatextentthethresholdshouldmovefromp min,k
(resp. p max,k) to p max,k (resp. p min,k), based on learning from
repeatedepisodes.InordertoapplytheREINFORCEalgorithm
for learning the parameter vector α, we need to compute the
derivativeofourpolicywithrespecttoα.Thederivativecanbe
computed using the chain rule, as we show in Eq. (3) for the
derivativeofαb,fordeliveryhourdinregimek.
1
∂πd(a|s) ∂πd(a|s)T ∂θ
θ = θ
∂αb ∂θ ∂αb
1 1
∂πd(a|s)
= ∂ θ μk (p min,k −p max,k ) (3)
Y
C. QuantityAlreadyTraded
The intuition for this adaptation is that, at any stage of the
trading process, if we have already bought a large quantity of
power and have not sold it yet, we wish to avoid the risk of
endingupwithunsoldpower.Notethatweassumethatthereis Fig.6. Illustrationoftheprobabilityreallocationthatreliesontheauxiliary
Gaussiandistribution,asdescribedinsectionV-E.
no residual value for leftover water in the reservoir at the end
of the horizon, which is consistent with the fact that we have
an interest in entering a new day with an empty reservoir and
fillingthereservoirupwithcheappowerthatisavailableduring where t is the current time step, T k b is the delivery time of the
thenighthours. maximumofthekth sellregime,andT k s isthedeliverytimeof
In order to capture this effect, we add a penalty in order to
theminimumofthekthbuyregime.
s/b
accept buying ata lower price and toaccept selling ata lower Weemploy4coefficientsinEqs.(4)and(5):(i)α 3 deter-
s/b
price: minesthestrengthofthiseffect;and(ii)α determineshow
4
smoothly the threshold adapts with respect to the gate closure
μ k X ←μ k X −α 2 s·v end s/b
time.Alargevalueforα woulddecreasetheselectivityvery
4
μ k ←μ k −α b ·v close to the delivery time. On the contrary, a small value for
Y Y 2 end
s/b
α woulddecreasetheselectivitymoresmoothlywithrespect
wherev isthevolumethatwewouldobtainatthelastdelivery 4
end totheremainingtime.
period with the trades that we have already engaged in. This
adjustmentofthethresholdsimpliesthat,movingforward,we
E. RelativeValueofObservableBids
become less selective about selling power and more selective
about buying power, until the reservoir eventually becomes Themotivationforthisfactoristoaccountforthecoupling
empty. amongthebidsofdifferentdeliveryhours,duetothefactthat
thebatterycanonlystoreafiniteamountofenergy.Concretely,
D. RemainingTimeBeforeMarketClosure we wish to avoid accepting a bid even though the order book
includesabidatanadjacentdeliveryperiodthatcanbetraded
Whenevertheproducerhasnotsoldalltheenergystoredin
forabetterprice.Inordertoaccountforthisinter-dependency,
its reservoir close to the maximum of a regime, the producer
wepenalizethebidsthatwouldnotbeacceptedbytherolling
should become less selective in the price it asks. This is due
intrinsicmethod.Therollingintrinsicpolicyisamyopicmethod
tothefactthattherearefewsubsequentopportunitiestotrade,
for trading in continuous markets. This method has already
andthecurrentlyobserved priceispossiblythebestpricethat
been used as a benchmark in the literature [21], [22], and was
the producer can secure for the trade. Similarly, whenever the
originallyproposedby[36]inthecontextoftradinggas.Theidea
producer has not bought up to the capacity of its reservoir as
of the method is to trade so as to maximize the instantaneous
it is approaching the minimum of a regime, it should become
reward at each time step [26]. In the context of our problem,
lessselectivewiththepricethatitasksforbuyingpower.This
the rolling intrinsic method will select the subset of trades
approach is inspired by the theory of the optimal stopping
which can be absorbed by the reservoir without exposing the
problem[34],[35].
unit to imbalances, and will do so by maximizing the profit
We capture this effect by varying the threshold means as
of the current time step. This myopic policy can be written
follows:
as an optimization problem at every time step of trade. The
μ k ←μ k +α s p max,k −p min,k exp(α s(t−T s)) (4) optimizationmodelisdevelopedintheelectronicsupplement.
X X 3 2 4 k
Concretely, the adjustment to our algorithm is illustrated in
μ k ←μ k −α b p max,k −p min,k exp(α b(t−T b)) (5) Fig. 6. The figure corresponds to the case in which rolling
Y Y 3 2 4 k intrinsicsells20MWhfordeliveryperiodd.Whenthisoccurs,
Authorized licensed use limited to: CZECH TECHNICAL UNIVERSITY. Downloaded on April 29,2026 at 09:07:50 UTC from IEEE Xplore. Restrictions apply.

| 2346 |     |     |     |     |     |     |     | IEEETRANSACTIONSONPOWERSYSTEMS,VOL.35,NO.3,MAY2020 |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- |
we wish to decrease the probability of selecting the action of TABLEI
selling 30 MWh, and reallocate it to the probability of selling PERCENTAGEOFOFFERSTHATAREOBSERVEDASAFUNCTIONOF
FREQUENCYOFACCESSINGTHEMARKETDATA
20MWh.Tothisend,weintroduceanauxiliaryGaussiandis-
| tributionwithameanofμk |     |         | +αb             | andwithastandarddeviation |        |        |      |     |     |     |     |     |     |
| ---------------------- | --- | ------- | --------------- | ------------------------- | ------ | ------ | ---- | --- | --- | --- | --- | --- | --- |
|                        |     |         | Y 5             |                           |        |        |      |     |     |     |     |     |     |
| exp(σY                 | ).  |         |                 |                           |        |        |      |     |     |     |     |     |     |
| of                     | We  | compute | the probability |                           | of the | action | Sell |     |     |     |     |     |     |
30MWhbyusingathresholddrawnfromtheauxiliaryGaussian
distribution,whichisindicatedwiththeblackbellcurveinthe
figure.ThisdecreasestheprobabilityoftheactionSell30MWh,
| relative to  | the probability |       | that would | have           | been | obtained       | from |     |     |     |     |     |     |
| ------------ | --------------- | ----- | ---------- | -------------- | ---- | -------------- | ---- | --- | --- | --- | --- | --- | --- |
| the original | bell            | curve | of Fig. 6. | The difference |      | in probability |      |     |     |     |     |     |     |
massistransferredtothelastactionthatisacceptedbyrolling
intrinsic(Sell20MWh),asillustratedinFig.6.Aswecansee
Thisadaptationiscoherentwiththeintuitionpresentedin
b,
in the figure, the higher the value of α 5 the less likely we are the example. Indeed, if we are canceling a position that
tochoosetheactionthatisnotselectedbyrollingintrinsic.The we have previously taken in the market, we can accept a
| computationoftheclosed-formexpressionforπ |     |     |     |     |     | d(a|s)andits |     |                  |       |                 |     |                     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | ------------ | --- | ---------------- | ----- | --------------- | --- | ------------------- | --- |
|                                           |     |     |     |     |     | θ            |     | less interesting | price | (i.e. accepting | a   | lower sell / higher |     |
derivativeispresentedindetailintheelectronicsupplement. buythreshold),becausetheperceivedefficiencyishigher
|     |     |     |     |     |     |     |     | (cid:2) than1. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
F. PreventingImbalances The mean of the auxiliary Gaussian represents the case
|       |         |        |               |     |          |            |     | in which | we are opening | a new | position. | Therefore, | the |
| ----- | ------- | ------ | ------------- | --- | -------- | ---------- | --- | -------- | -------------- | ----- | --------- | ---------- | --- |
| As we | explain | in the | introduction, | we  | are only | interested | in  |          |                |       |           |            |     |
developing trading strategies that do not result in imbalance, auxiliary Gaussian distribution mean will be equal to: (i)
μ
|     |     |     |     |     |     |     |     | η ·η | ·μX forthebuythreshold;and(ii) |     |     | Y forthe |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------------------------ | --- | --- | -------- | --- |
giventheamountofwaterthatiscurrentlystoredinthereservoir. in out η · η
|     |     |     |     |     |     |     |     |     |     |     |     | in out |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- |
Inordertoremoveactionsthatresultinimbalances,were-assign sell threshold. This is also coherent with the example,
|     |     |     |     |     |     |     |     | because | we are requesting | a more | selective | price | if we |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------------- | ------ | --------- | ----- | ----- |
theirprobabilitytotheclosestactionwhichdoesnotresultinan
|     |     |     |     |     |     |     |     | are opening | a new position | than | if we | are engaging | in a |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------------- | ---- | ----- | ------------ | ---- |
imbalance,usingthesameideaasinsectionV-E.Inthiscase,the
parameterαb isreplacedbyaconstantM whichissufficiently purelyfinancialtransaction,sincetheperceivedefficiency
5
islessgood.Notethatthisadaptationdoesnotaddanynew
largeinordertoensurethatanactionwhichwouldresultinan
| imbalanceisneverselected. |     |     |     |     |     |     |     | parametersinthelearningalgorithm. |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- |
VI. CASESTUDY
G. AdaptingWithRespecttoRound-TripEfficiency
In order to account for round-trip efficiency, we present an Inthissectionwepresentresultsfromtheimplementationof
theproposedpolicyontheGermancontinuousintradaymarket.
| example | that illustrates |     | the concept | of  | perceived | efficiency, |     |     |     |     |     |     |     |
| ------- | ---------------- | --- | ----------- | --- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
whichdistinguisheswhetherweareplanningtocoverabidfinan- The data for the German CIM has been procured from the
ciallyorphysically.Supposethatwehavetwodeliveryhours,a European Power Exchange (EPEX), and spans two years. For
thepurposeofthecasestudy,weplaceourselvesintheposition
| chargingefficiencyη |     | of0.9andadischargingefficiencyη |     |     |     |     | of  |     |     |     |     |     |     |
| ------------------- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                     |     | in                              |     |     |     |     | out |     |     |     |     |     |     |
0.9.Supposethatwehavealreadybought20MWhforthefirst ofastorageassetownerwhomanagesaunitwithamaximum
storagecapacityof200MWh.Weassumethat,onJuly19,the
deliveryhourattheprevioustimestep.Therefore,thequantity
thatwouldbestoredis18MWhforbothdeliverytimes.Ifwe owner adopts our strategy and has at its disposal market data
wanttosellpowerattheseconddeliverytime,wecanonlysell sincethebeginningoftheyear.6Therefore,weusethe200first
daysof2015astrainingset,andthelast165daysof2015and
16.2MWh,becausewehavetoapplythedischargeefficiency.
Wedefinetheperceivedefficiencyforthisorderas 16.2 =0.9. the366daysof2016asatestset.
18
| On the contrary, |     | if we | want to | sell at | the first | delivery | time, |     |     |     |     |     |     |
| ---------------- | --- | ----- | ------- | ------- | --------- | -------- | ----- | --- | --- | --- | --- | --- | --- |
wecansell20MWh,becausethisoperationwillsimplycancel A. LearningProcess
| the previous | purchase |     | of 20 MWh. | This | is a purely |     | financial |     |     |     |     |     |     |
| ------------ | -------- | --- | ---------- | ---- | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- |
Weaimatlearningtheoptimalthreshold,soastoapplyour
operation.Wethusdefinetheperceivedefficiencyforthisorder
thresholdpolicywithafrequencyof1second.Weconsider1sec-
as 20 =1.11.
| 18  |     |     |     |     |     |     | ondasasufficientlyhighfrequencyfortestingthealgorithmin |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
Inordertoaccountforthiseffectinthethresholdparametriza- thecontinuousintradaymarketbecause,asobservedinTableI,
tion,weusethesameideaasinsectionV-E.
| (cid:2) |           |     |                  |     |         |      | ifwetradeeverysecond,wewillobserve98.3%oftheoffers. |     |     |     |     |     |     |
| ------- | --------- | --- | ---------------- | --- | ------- | ---- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| We      | determine | a   | certain baseline |     | for the | mean | of the                                              |     |     |     |     |     |     |
Thismeansthatalmostalloftheoffersremaininthemarketfor
Gaussiandistributionofourbuyandsellthreshold,which atleastonesecond,beforebeingmatchedwithcompetingoffers
correspondstothecaseinwhichweareacceptingacertain
ontheplatform.
| quantity | that | serves | as a purely | financial | transaction. |     | We  |     |     |     |     |     |     |
| -------- | ---- | ------ | ----------- | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Inorderforthelearningstageofthealgorithmtobecompu-
thenadaptthethresholdsasfollows:
tationallytractable,wegraduallyrefinethelearningfrequency
1
|     |     |     | μ k ← | μ   | k   |     |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | X     |     | X   |     |     |     |     |     |     |     |     |
η out 6Notethatdatawhichextendstoofarbackintimemaynotbeasuseful,due
totherapidstructuralevolutionofthemarket(increaseinrenewableenergy
|     |     |     | μ k ←η | μ k  |     |     |                                          |     |     |     |     |     |     |
| --- | --- | --- | ------ | ---- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |     |     | Y      | in Y |     |     | integration,changesinmarketdesign,etc.). |     |     |     |     |     |     |
Authorized licensed use limited to: CZECH TECHNICAL UNIVERSITY. Downloaded on April 29,2026 at 09:07:50 UTC from IEEE Xplore.  Restrictions apply.

BERTRANDANDPAPAVASILIOU:ADAPTIVETRADINGINCONTINUOUSINTRADAYELECTRICITYMARKETSFORASTORAGEUNIT 2347
TABLEII
PROFITMEAN[€/DAY]
| Fig. | 7. Evolution | of  | profit | as a function | of  | iterations | of the | REINFORCE |     |     |     |     |     |
| ---- | ------------ | --- | ------ | ------------- | --- | ---------- | ------ | --------- | --- | --- | --- | --- | --- |
algorithm.
fromhourlystepsto15-minutestepsandultimatelyto5-minute
steps,7
|          | as  | indicated     | in  | Fig. 7. | In this | figure, | 1 iteration  | cor-  |     |     |     |     |     |
| -------- | --- | ------------- | --- | ------- | ------- | ------- | ------------ | ----- | --- | --- | --- | --- | --- |
| responds | to  | 4 repetitions |     | of the  | 200     | days    | of learning, | which |     |     |     |     |     |
amountsto800episodes.Theseepisodesareexecutedinparallel
onanHPCclusterusing8CPUsfor40hours8.
| A   | potential | issue | for | our learning |     | phase | is that | the REIN- |     |     |     |     |     |
| --- | --------- | ----- | --- | ------------ | --- | ----- | ------- | --------- | --- | --- | --- | --- | --- |
FORCEalgorithmisastochasticalgorithm.Therefore,different
runscanproducedifferentresults.Inordertotestthesensitivity
ofourresults,wehaveconductedanexperimentinwhichwerun
6differentrealizationsoftheREINFORCEalgorithmathourly
| frequency |              | and compare |      | the evolution |            | of the | alpha   | parameters |     |     |     |     |     |
| --------- | ------------ | ----------- | ---- | ------------- | ---------- | ------ | ------- | ---------- | --- | --- | --- | --- | --- |
| and       | the profit.  | We          | find | that the      | different  | runs   | exhibit | a very     |     |     |     |     |     |
| similar   | performance. |             | The  | complete      | experiment |        | is      | available  | in  |     |     |     |     |
theelectronicsupplementofthepaper.
Fig.8. Distributionofthedifferencebetweentheprofitofthethresholdpolicy
andtherollingintrinsicpolicy.
B. Out-Of-SampleTesting
Inthissection,wepresenttheresultsobtainedbyourthreshold
|        |     |               |     |       |      |            |     |           | presented | in [22]; (iii) | our threshold policy | also outperforms |     |
| ------ | --- | ------------- | --- | ----- | ---- | ---------- | --- | --------- | --------- | -------------- | -------------------- | ---------------- | --- |
| policy | on  | out-of-sample |     | data. | More | precisely, | we  | apply the | θ         |                |                      |                  |     |
parameter vector learned on the 200 first days of 2015 on the rollingintrinsicforanonperfectround-tripefficiency;(iv)the
resultsinandout-of-sampleareverysimilar;and(v)themost
remainderof2015andtotheentireyearof2016.Wecompare
importantparametersareα3α4andα5.Intheremainderofthis
| these | results | with | the | ones obtained |     | by the | rolling | intrinsic |     |     |     |     |     |
| ----- | ------- | ---- | --- | ------------- | --- | ------ | ------- | --------- | --- | --- | --- | --- | --- |
section,wewillanalysethesefiveobservationsinmoredetails.
| method, | which | is  | described | in  | section | V-E. | . We | present the |     |     |     |     |     |
| ------- | ----- | --- | --------- | --- | ------- | ---- | ---- | ----------- | --- | --- | --- | --- | --- |
a) SuperiorityoftheThresholdPolicyComparedtoRolling
resultsinTableII.(i)Column1representsthetradingfrequency.
|      |        |          |     |            |     |         |      |             | Intrinsic: | Byobservingrows4and5ofthetable,weobserve |     |     |     |
| ---- | ------ | -------- | --- | ---------- | --- | ------- | ---- | ----------- | ---------- | ---------------------------------------- | --- | --- | --- |
| (ii) | Column | 2 refers | to  | the method |     | that we | use: | “Threshold” |            |                                          |     |     |     |
thattheaverageprofitdifferenceamountsto17.8%.Moreover,
| refers | to the | method | developed |     | in this | paper, | ”Rolling” | refers |     |     |     |     |     |
| ------ | ------ | ------ | --------- | --- | ------- | ------ | --------- | ------ | --- | --- | --- | --- | --- |
theproposedthresholdpolicyachievesahigherprofitin77.4%
torollingintrinsic,”GM”isthepolicythathasbeendeveloped
|     |     |     |     |     |     |     |     |     | of the days. | In Fig. 8, | we present the daily | profit difference |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | -------------------- | ----------------- | --- |
in[22]and“Thresholdwithoutαi”isthepolicylearnedbythe
REINFORCEalgorithmifwefixαsandαbto0.(iii)Column3 betweenthethresholdandtherollingintrinsicpolicy.Thefigure
i i demonstratesthattheextraprofitisacumulativeeffectofmulti-
referstotheround-tripefficiencyoftheconsideredstorageunit.
pledaysofsuperiorperformance,asopposedtobeingtheresult
(iv)Column4referstothedatathatareusedforthetest.Itcan
ofafewisolateddaysinwhichthethresholdpolicyperformed
eitherbein-sample(the200firstdaysof2015)orout-of-sample
significantlybetter.
| (the | remainder | of  | 2015 | and 2016). | (v) | Column | 5   | contains the |         |                  |                    |                |     |
| ---- | --------- | --- | ---- | ---------- | --- | ------ | --- | ------------ | ------- | ---------------- | ------------------ | -------------- | --- |
|      |           |     |      |            |     |        |     |              | In Fig. | 9, we illustrate | one of the effects | that justifies | the |
averageprofit.Fromthistable,5mainobservationscanbemade:
|     |               |     |        |             |     |         |            |          | superior | profit of the | threshold policy. | This graph indicates |     |
| --- | ------------- | --- | ------ | ----------- | --- | ------- | ---------- | -------- | -------- | ------------- | ----------------- | -------------------- | --- |
| (i) | our threshold |     | policy | outperforms |     | rolling | intrinsic; | (ii) our |          |               |                   |                      |     |
whetherpowerhasbeentradedforthedifferentdeliverytimes
thresholdpolicyismoresuitedforhighfrequencythantheone
|     |     |     |     |     |     |     |     |     | and time | steps. An empty | dot indicates | that we have | bought |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | ------------- | ------------ | ------ |
power,whereasasoliddotindicatesthatwehavesoldpower.The
7Wedecidetoswitchtoahigherlearningfrequencywhentheprofitappears
leftgraphillustratesoneoftheweaknessesofrollingintrinsic:
tostabilize.Thisisduetothefactthatthereisnoreasontorunthealgorithm
|     |     |     |     |     |     |     |     |     | at each | time step where | there are empty | dots, there | are also |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------------- | --------------- | ----------- | -------- |
untilfullconvergenceforthehourlyfrequency,becauseitisnottheproblemwe
areinterestedin(theorderdataarrivesatmuchhigherfrequencythanhourly). soliddots.Thisimpliesthatthemethodonlyconsidersbuying
8We have performed an analysis on the computational scalability of our power if it can sell it directly (except if it can buy power at a
learningprocess.Themainmessageofthestudyisthattheruntimeincreases
linearlywithrespecttothetradingfrequency.Thecompletenumericalanalysis negativeprice).Thisisduetothefactthatthemethodmaximizes
hasbeenaddedintheelectronicsupplement. the profit of the current time step, and ignores future trading
Authorized licensed use limited to: CZECH TECHNICAL UNIVERSITY. Downloaded on April 29,2026 at 09:07:50 UTC from IEEE Xplore.  Restrictions apply.

2348 IEEETRANSACTIONSONPOWERSYSTEMS,VOL.35,NO.3,MAY2020
Fig.9. Bidacceptancepatternsfor1dayoftradingfortherollingintrinsic
Fig.11. Profitevolutionforonedayoftradingforthefullday(left)anda
(left)andthresholdmethod(right).
zoominontheendoftheday(right).
volume, which are not visible at the outset of the trading day.
These profits correspond to the small increase of the profit of
therollingintrinsicpolicy,followingthelargejump.Itisworth
notingthatthesesmallincreasesarealmostinsignificantwhen
tradingatanhourlytimestep,butbecomeveryimportantata
highertradingfrequency.
This analysis highlights that, when trading at a higher fre-
quency,werequireatradingstrategythatiseffectiveatcapturing
the value of both predictable large arbitrage opportunities and
Fig.10. Profitevolutionforonedayoftradingfortherollingintrinsicmethod
forvarioustradingfrequencies. less predictable small opportunities. In Fig. 11 we observe
thatthethresholdpolicyattainssimilarperformancetorolling
intrinsicintermsofcapturingsmallarbitrageopportunities.This
opportunitieswhichmayarrivebuthavenotyetbeenobserved. isrepresentedbytherightgraph,whereweobservethatthetwo
On the contrary, the threshold method procures power at the curves follow a similar pattern towards the end of the day. On
beginningofthehorizon,butmayturndownoffersforselling the contrary, the GM policy is not able to capture these small
power if the sales price is not sufficiently attractive. Thus, the arbitrage opportunities, which is clear from the fact that the
threshold method may wait in order to sell the power later, profitremainsconstantattheendoftheday.NotethattheGM
counting on the possibility that at a later moment there will policyparametrizationdoesnotincludeanyinformationabout
beoffersarrivinginthemarketwithahigherwillingnesstopay the prices available for the other delivery hours. The problem
thanthecurrentlyavailableoffers. is that, for these small arbitrage opportunities, a bid is not
b) ComparisonofOurThresholdPolicyandtheGMPolicy interesting only due to its price but also because if we accept
at High Frequency: We compare the influence of the trading italongwithabidwithanotherdeliverytime,wecandirectly
frequencyontheperformanceofthreedifferentmethods:(i)the secureapositiveprofitusingourstorageunit.
thresholdpolicypresentedinthepresentpaper;(ii)therolling Ontheotherhand,themaindifferencebetweenourthreshold
intrinsic policy; and (iii) the GM policy. Note that the GM policy and rolling intrinisc mainly rests on the fact that the
policy does not incorporate the parameters αs and αb in the threshold policy is better suited for trading for big arbitrage
5 5
parametrization of the threshold. From rows 1–6 of the table, opportunities.Thisisillustratedbythefactthatthelargejump
weobservethattheprofitincreaseswithrespecttothetrading of the threshold policy is higher than that of rolling intrinsic.
frequencyforallthemethods.Thisisexpected,sinceanincrease The rolling intrinsic policy buys and sells prematurely in the
in the trading frequency increases the number of offers that beginning of the day, whereas the threshold policy holds back
we observe and use for trading. However, this profit increase untilmorefavorabletradescanbelockedin.
is smaller for the GM policy. In order to interpret this result, c) Threshold Performance for a Non Perfect Roundtrip
Figs.10and11comparetheevolutionoffivedifferentpolicies: Efficiency: Inthissection,wepresenttheresultsforastorage
(i)rollingintrinsicwithanhourlytradingfrequency;(ii)rolling unitwithachargingefficiencyof0.9andadischargingefficiency
intrinsic with a trading frequency of 15 seconds; (iii) rolling of 0.9. Our aim is to verify that our threshold policy is also
intrinsicwithatradingfrequencyof1second;(iv)athreshold suitableforanassetwithanimperfectround-tripefficiency.The
policy with a trading frequency of 1 second; and (v) the GM results are presented in rows 7 and 8 of the table. As before,
policywithatradingfrequencyof1second. we compare the results obtained by our threshold policy with
InFig.10,weobservethattwofactorscontributetotheprofit. the ones obtained by rolling intrinsic on the same data. The
(i) The first factor is the profit that results from the signifi- proposedthresholdpolicyachievesahigherprofitin64.6%of
cant arbitrage possibilities of the storage unit. These arbitrage the days. The average profit difference amounts to 13.6%. In
opportunities can be anticipated. These profits correspond to Fig.12wepresentthedailyprofitdifference.Theseresultsare
the large jump of the rolling intrinsic method. (ii) The second relatively close to the ones obtained for a storage unit with a
factorcorrespondstotheprofitsthatresultfromtradesofsmaller perfect round-trip efficiency. The results thus suggest that our
Authorized licensed use limited to: CZECH TECHNICAL UNIVERSITY. Downloaded on April 29,2026 at 09:07:50 UTC from IEEE Xplore. Restrictions apply.

BERTRANDANDPAPAVASILIOU:ADAPTIVETRADINGINCONTINUOUSINTRADAYELECTRICITYMARKETSFORASTORAGEUNIT 2349
Fig.12. Distributionofthedifferencebetweentheprofitofthethresholdpolicy Fig.13. Distributionofthedifferencebetweentheprofitoftherollingintrinsic
|     |     |     |     |     |     |     |     | policyandtheprofitofthethresholdpolicywithoutparametersαs |     |     |     |     |     | /b  | andαs /b |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- |
andtherollingintrinsicpolicyinthecasewithround-tripefficiencylosses. .
|              |      |               |         |      |                 |            |        |         |               |      |                |                       |     | 3       | 4       |
| ------------ | ---- | ------------- | ------- | ---- | --------------- | ---------- | ------ | ------- | ------------- | ---- | -------------- | --------------------- | --- | ------- | ------- |
| policy is    | also | suitable      | for the | case | with round-trip | efficiency |        |         |               |      |                |                       |     |         |         |
|              |      |               |         |      |                 |            |        | αb.     | This implies  | that | the            | sell threshold        |     | will be | low and |
| losses.      |      |               |         |      |                 |            |        | 1       |               |      |                |                       |     |         |         |
|              |      |               |         |      |                 |            |        | the     | buy threshold |      | will be        | high. Simultaneously, |     |         | the al- |
| d) Stability |      | of the Method |         | with | Respect         | to Change  | in the |         |               |      |                |                       |     |         |         |
|              |      |               |         |      |                 |            |        |         |               |      |                |                       | αs  | αb      |         |
|              |      |               |         |      |                 |            |        | gorithm | increases     |      | the parameters |                       | and | to      | a very  |
Data: In rows 5 and 10 of the table, we compare the profit 5 5
highvalue.Theconsequenceofthisbehaviourwillbethat
| obtained | by rolling | intrinsic |     | in-sample | and | out-of-sample. | We  |     |     |     |     |     |     |     |     |
| -------- | ---------- | --------- | --- | --------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thepolicywillaimatacceptingeverypossiblebidthatis
observethattheprofitisslightlyhigherin-samplethanout-of-
alsoacceptedbyrollingintrinsic.Thisindicatesthatthis
sample.Thus,theperformanceunderin-sampledataisslightly
policyisattemptingtomimictherollingintrinsicpolicy.
| morefavourablethanunder |     |     | out-of-sampledata.Inrows4and |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Inordertoconfirmthisintuition,wepresentinFig.13the
9,weobservethatourthresholdpolicyalsoachievesaslightly
|     |     |     |     |     |     |     |     | profit | difference | between |     | the rolling | intrinsic | policy | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | ------- | --- | ----------- | --------- | ------ | --- |
higherprofitin-sample.Notethatthedifferencebetweenthetwo
methodsamountsto911€ in-sampleand966€ this policy. We observe that the values are concentrated
out-of-sample.
around0,whichconfirmsourintuitionthatthealgorithm
Thus,ourmethodisobservedtoachievearobustperformance
isattemptingtomimicrollingintrinsic.
againstout-of-sampledata.
| e) ImportanceoftheDifferentParameters: |     |     |     |     |     | Inordertotest |     |     |     |     |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theinfluenceofeachelementofthethresholdparametrization, VII. CONCLUSIONSANDPERSPECTIVES
| we have | launched | the | REINFORCE |     | algorithm | by cancelling |     |         |          |        |             |     |             |         |     |
| ------- | -------- | --- | --------- | --- | --------- | ------------- | --- | ------- | -------- | ------ | ----------- | --- | ----------- | ------- | --- |
|         |          |     |           |     |           |               |     | In this | paper we | tackle | the problem |     | of intraday | trading | for |
eachoftheparametersonebyone.Thenweapplythelearned
|     |     |     |     |     |     |     |     | storage units. | We  | model | the problem | using | Markov |     | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----- | ----------- | ----- | ------ | --- | -------- |
policyout-of-sample.Moreprecisely,wehaverealized3simu-
Processes.Wefocusonpoliciesthatareparametrizedonprice
| lations:(i)weoptimizethepolicywhilefixingαs |     |     |     |     |     | andαb |        |     |     |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
|                                             |     |     |     |     |     | 1     | 1 to0; |     |     |     |     |     |     |     |     |
(ii)weoptimizethepolicywhilefixingαsandαb thresholds,andweoptimizetheresultingpolicyfunctionsusing
to0;and(iii)
|                                             |     |     |     |     | 2   | 2   |         | theREINFORCEalgorithm.Weintroduceandjustifyacollec- |     |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| weoptimizethepolicywhilefixingαs,αb,αsandαb |     |     |     |     |     |     | to0.The |                                                     |     |     |     |     |     |     |     |
3 3 4 4 tionoffactorsthatcanbeusedforadaptingthetradingthreshold
reasonforfixingbothα3andα4togetheristhatcancellingone
|     |     |     |     |     |     |     |     | to system | conditions. | We  | compare | our | threshold | policy | to the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | ------- | --- | --------- | ------ | ------ |
willcanceltheotherautomatically.
|     |     |     |     |     |     |     |     | rolling intrinsic |     | method | on the | German | continuous |     | intraday |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------ | ------ | ------ | ---------- | --- | -------- |
αs
| We have | not     | considered     | the | case | in which       | we set | 5 and   |                                                        |     |     |     |     |     |     |     |
| ------- | ------- | -------------- | --- | ---- | -------------- | ------ | ------- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
| αb      |         |                |     |      |                |        |         | market.Wedemonstratethatthethresholdpolicyperformssig- |     |     |     |     |     |     |     |
| to 0,   | because | the importance |     | of   | this parameter | is     | already |                                                        |     |     |     |     |     |     |     |
5 nificantlybetterthanrollingintrinsic,andanalyzetheresultsin
discussedextensivelywhenanalysingtheGMpolicy.Theresults
ordertoexplaintheperformancedifference.Infuturework,we
| are presented |     | in the last | three | rows | of Table | II and | will be |     |     |     |     |     |     |     |     |
| ------------- | --- | ----------- | ----- | ---- | -------- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
areinterestedinimprovingthepolicyfunctionsbyaddingmore
analysedindetailintheremainderofthesection.
explanatoryvariablesofthepricethresholdssuchasrenewable
Withoutαsandαb:Weobservethattheprofitisslightly
1) 1 1 forecastsorgeneratoroutages.Wealsoaimatdevelopingtrading
|        |     |            | αs  | αb  |          |        |      |     |     |     |     |     |     |     |     |
| ------ | --- | ---------- | --- | --- | -------- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| better | if  | we include |     | and | compared | to the | case | in  |     |     |     |     |     |     |     |
1 1 strategies in the Continuous Intraday Market for renewable
whichwesetthemto0.Thissuggeststhattheseparameters
sourceswithuncertainreal-timeproduction.
help,buttheirimpactisnotdecisive.9
| 2) Without   |     | αs and | αb: | We observe                     |     | that the profit | with |     |     |                |     |     |     |     |     |
| ------------ | --- | ------ | --- | ------------------------------ | --- | --------------- | ---- | --- | --- | -------------- | --- | --- | --- | --- | --- |
|              |     | 2      | 2   |                                |     |                 |      |     |     |                |     |     |     |     |     |
| andwithoutαs |     | andαb  |     |                                |     |                 |      |     |     | ACKNOWLEDGMENT |     |     |     |     |     |
|              |     | 2      | 2   | isalmostidentical.Thissuggests |     |                 |      |     |     |                |     |     |     |     |     |
thatthisparametercouldbediscardedwithouthurtingthe TheauthorswouldliketothankG.deMaereandG.Erbsfor
profitabilityofthepolicy.
theirhelpfulcommentsduringthedevelopmentofthiswork.
|            |      | αs, αb, | αs      | αb:      |         |                  |          |     |     |     |     |     |     |     |     |
| ---------- | ---- | ------- | ------- | -------- | ------- | ---------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3) Without |      | 3 3     | 4 and   | 4        | In this | case, we observe |          | a   |     |     |     |     |     |     |     |
| big        | drop | in the  | profit, | compared | to      | the initial      | case. By |     |     |     |     |     |     |     |     |
REFERENCES
furtherinvestigatingtheobtainedparameters,weobserve
αs
that the algorithm converges to a high value of and [1] EU,Dec.2019. [Online].Available:https://ec.europa.eu/clima/policies/
1
strategies/2020_en
|     |     |     |     |     |     |     |     | [2] Eurostat, | Dec. | 2019. [Online]. | Available: |     | http://ec.europa.eu/eurostat/ |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---- | --------------- | ---------- | --- | ----------------------------- | --- | --- |
9Noticethatwehaverealizedthesameexperimentatafrequencyof1minute, statistics-explained/images/d/de/Table_3-Share_of_electricity_from_
andtheextraprofitwasmoresignificant(around0.83%). renewable_sources_in_gross_electricity_consumption_2004-2016.png
Authorized licensed use limited to: CZECH TECHNICAL UNIVERSITY. Downloaded on April 29,2026 at 09:07:50 UTC from IEEE Xplore.  Restrictions apply.

2350 IEEETRANSACTIONSONPOWERSYSTEMS,VOL.35,NO.3,MAY2020
[3] H.MartinandS.Otterson,“Germanintradayelectricitymarketanalysis [24] EPEXSPOT,Dec.2019.[Online].Available:https://www.epexspot.com/
andmodelingbasedonthelimitorderbook,”inProc.15thInt.Conf.Eur. sites/default/files/download_center_files/Trading%20Brochure.pdf
EnergyMarket,Lodz,Poland,2018,pp.1–6. [25] TENNET, Dec. 2019. [Online]. Available: https://www.epexspot.com/
[4] J.MatevosyanandL.Soder,“Minimizationofimbalancecoststrading sites/default/files/download_center_files/Trading%20Brochure.pdf
windpowerontheshort-termpowermarket,”IEEETrans.PowerSyst., [26] W.PowellandS.Meisel,“Tutorialonstochasticoptimizationinenergy—
vol.21,no.3,pp.1396–1404,Aug.2006. partII:Anenergystorageillustration,”IEEETrans.PowerSyst.,vol.31,
[5] J.Chaves,R.Hakvoort,andA.Ramos,“Short-termstrategiesforDutch no.2,pp.1468–1475,Mar.2016.
windpowerproducerstoreduceimbalancecosts,”EnergyPolicy,vol.52, [27] R.SuttonandA.Barto,ReinforcementLearning:AnIntroduction.Cam-
pp.573–582,Jan.2013. bridge,MA,USA:MITPress,2018.
[6] D.Lee,H.Shin,andR.Baldick,“Bivariateprobabilisticwindpowerand [28] R.J.Williams,“Simplestatisticalgradient-followingalgorithmsforcon-
real-timepriceforecastingandtheirapplicationstowindpowerbidding nectionistreinforcementlearning,”Mach.Learn.,vol.8,no.3/4,pp.229–
strategydevelopment,”IEEETrans.PowerSyst.,vol.33,no.6,pp.6087– 256,May1992.
6097,Nov.2018. [29] W.Morris,“Someanalysisofpurchasingpolicy,”Manage.Sci.,vol.5,
[7] C.O’DwyerandD.Flynn,“Usingenergystoragetomanagehighnetload no.4,pp.443–452,Jul.1959.
variabilityatsub-hourlytime-scales,”IEEETrans.PowerSyst.,vol.30, [30] B.Kingsman,“Commoditypurchasing,”J.Oper.Res.Soc.,vol.20,no.1,
no.4,pp.2139–2148,Jul.2015. pp.59–79,Mar.1969.
[8] M.Khodayar,M.Shahidehpour,andL.Wu,“Enhancingthedispatcha- [31] K.Golabi,“Optimalinventorypolicieswhenorderingpricesarerandom,”
bilityofvariablewindgenerationbycoordinationwithpumped-storage OperationsRes.,vol.33,no.3,pp.575–588,1985.
hydrounitsinstochasticpowersystems,”IEEETrans.PowerSyst.,vol.28, [32] W.PowellandS.Meisel,“Tutorialonstochasticoptimizationinenergy-
no.3,pp.2808–2818,Aug.2013. partI:Modelingandpolicies,”IEEETrans.PowerSyst.vol.31,no.2,
[9] T.Boomsma,N.Juul,andS.Fleten,“Biddinginsequentialelectricity pp.1459–1467,Mar.2016.
markets:TheNordiccase,”Eur.J.Oper.Res.,vol.238,no.3,pp.797–809, [33] G.Klaboe,A.Eriksrund,andS.Fleten,“Benchmarkingtimeseriesbased
Nov.2014. forecastingmodelsforelectricitybalancingmarketprices,”EnergySyst.,
[10] S.Braun,“Hydropowerstorageoptimizationconsideringspotandintraday vol.6,no.1,pp.43–61,Mar.2015.
auctionmarket,”EnergyProcedia,vol.87,pp.36–44,Jan.2016. [34] D.Lindley,“Dynamicprogramminganddecisiontheory,”Appl.Statist.,
[11] R.KieselandF.Paraschiv,“Econometricanalysisof15-minuteintraday vol.10,no.1,pp.39–52,1961.
electricityprices,”EnergyEcon.,vol.64,pp.77–90,May2017. [35] J. Tsitsiklis and B. Van Roy, “Optimal stopping of markov processes:
[12] F.Ziel,“Modelingtheimpactofwindandsolarpowerforecastingerrors Hilbertspacetheory,approximationalgorithms,andanapplicationtopric-
onintradayelectricityprices,”inProc.14thInt.Conf.Eur.EnergyMarket, inghigh-dimensionalfinancialderivatives,”IEEETrans.Autom.Control,
Dresden,Germany,2017,pp.1–5. vol.44,no.10,pp.1–5,Oct.1999.
[13] C.Balardy,“Anempiricalanalysisofthebid-askspreadintheGerman [36] J. Gray and P. Khandelwal, “Realistic natural gas storage models II:
PowerContinuousMarket,”Workingpaper,2018. Tradingstrategies,”CommoditiesNow,pp.1–5,Sep.2004.
[14] R.Kiesel,“Modelingmarketorderarrivalsontheintradaypowermarket
fordeliveriesinGermanywithHawkesprocesseswithparametrickernels,”
inProc.EnergyFinanceChristmasWorkshop,2017,pp.1–45.
[15] S. Braun and R. Hoffmann, “Intraday optimization of pumped hydro GillesBertrand(S’16)receivedtheB.Sc.andM.Sc.
powerplantsinthegermanelectricitymarket,”EnergyProcedia,vol.87, degreesinmathematicalengineeringfromUCLou-
pp.45–52,Jan.2016. vain, Louvain-la-Neuve, Belgium. He is currently
[16] E.Engmark,H.Sandven,S.Fleten,andG.Klaboe,“Stochasticmultistage working toward the Ph.D. degree in applied math-
biddingoptimisationinanintradaymarketwithlimitedliquidity,”inProc. ematics with the Center for Operations Research
15thInt.Conf.Eur.EnergyMarket,Lodz,Poland2018,pp.1–5. andEconometricsofUCLouvain,Louvain-la-Neuve,
[17] E.GarnierandR.Madlener,“Balancingforecasterrorsincontinuous-trade Belgium.
intradaymarkets,”EnergySyst.,vol.6,no.3,pp.361–388,Sep.2015.
[18] R.Aid,P.Gruet,andH.Pham,“Anoptimaltradingprobleminintraday
electricity markets,” Math. Financial Econ., vol. 10, no. 1, pp. 49–85,
Jan.2016.
[19] A.Skajaa,K.Edlund,andJ.Morales,“Intradaytradingofwindenergy,”
IEEETrans.PowerSyst.,vol.30,no.6,pp.3181–3189,Nov.2015.
[20] G.BertrandandA.Papavasiliou,“Ananalysisofthresholdpoliciesfor
tradingincontinuousintradayelectricitymarkets,”inProc.15thInt.Conf. AnthonyPapavasiliou(M’06)receivedtheB.S.de-
Eur.EnergyMarket,Lodz,Poland,2018,pp.1–5. gree in electrical and computer engineering from
[21] I.Boukasetal.,“Intra-daybiddingstrategiesforstoragedevicesusing theNationalTechnicalUniversityofAthens,Athens,
deepreinforcementlearning,”inProc.15thInt.Conf.Eur.EnergyMarket, Greece,andthePh.D.degreefromtheUniversityof
Lodz,Poland,2018,pp.1–6. CaliforniaatBerkeley,Berkeley,CA,USA.Heholds
[22] G.BertrandandA.Papavasiliou,“Reinforcement-learningbasedthreshold theENGIEChairwithUCLouvain,Belgium.
policiesforcontinuousintradayelectricitymarkettrading,”inProc.IEEE
PESGen.Meeting,Atlanta,GA,USA,2019.
[23] EPEXSPOT,Dec.2019.[Online].Available:https://www.epexspot.com/
sites/default/files/download_center_files/Trading%20Brochure.pdf
Authorized licensed use limited to: CZECH TECHNICAL UNIVERSITY. Downloaded on April 29,2026 at 09:07:50 UTC from IEEE Xplore. Restrictions apply.