# Power trading transition from algo finance

##### [**Undermind**](https://undermind.ai)

---

**Research Goal:** Find academic literature that helps a trader transition from traditional stock-exchange algorithmic trading into electricity trading, with primary emphasis on practical adaptation for short-term algorithmic trading and execution. The search should compare financial algorithmic trading with electrical energy trading in terms of market structure, liquidity, price formation, volatility drivers, and the role of physical constraints. It should cover the technical and mathematical adjustments needed when moving models into electricity markets, including negative prices, grid constraints, and distinct trading horizons such as day-ahead and intraday markets, while also covering the broader trading stack around short-term trading, including forecasting, dispatch-related constraints, portfolio and risk management, and settlement. Include literature on the data and infrastructure needed for electricity trading beyond traditional financial market feeds, such as meteorological forecasts, generation outages, grid load and system information, and other power-system variables relevant to trading. Also include research relevant to regulatory and compliance frameworks in Europe, especially REMIT and exchange or market-rule contexts relevant to EEX, OTE, and a trader based in Prague, but treat this as an important subfocus rather than the sole scope. Prioritize mostly recent market-practice and post-energy-crisis literature while also including foundational older electricity-market papers needed to understand the field. The goal is to synthesize verified, actionable recommendations, common pitfalls, and effective adaptations in models, execution, and risk management for entering power and energy markets from a financial algorithmic trading background.

*Found 185 papers · April 29, 2026 · Estimated coverage of relevant papers: 72%*

## Summary of Results

Electricity short-term trading is a sequential physical market in which updated renewable/load forecasts, grid constraints, and imbalance settlement co-determine prices, so the main adaptation from equity-style algo trading is from pure order-flow/execution thinking toward forecast-driven position management across day-ahead, intraday, and balancing layers \[1\], \[2\], \[3\], \[4\].

#### What matters most operationally

- **Intraday alpha is fundamentally forecast alpha**: wind/solar updates, outages, load, and merit-order slope dominate short-horizon repricing \[2\], \[5\], \[6\], \[7\].
- **Execution still matters, but in a thinner book**: liquidity is sparse, regime-dependent, and improves near gate closure; market impact often dominates nominal arbitrage opportunity \[3\], \[8\], \[9\], \[10\].
- **Price dynamics differ from finance benchmarks**: mean reversion, adjacent-product dependence, spike regimes, and negative prices are structural rather than pathological \[5\], \[11\], \[12\].

#### Trading-stack adjustments

- **Model inputs expand beyond market data**: ENTSO-E transparency data, TSO forecasts, outages, cross-border capacity, and weather nowcasts become core features \[2\], \[13\], \[14\].
- **Risk shifts from mark-to-market alone to joint price-volume-imbalance exposure**; balancing markets are extreme, and probabilistic forecasts are often more useful than point forecasts \[15\], \[16\], \[17\].
- **Physical constraints enter optimization directly**: ramping, dispatch delays, storage constraints, and transmission coupling change both valuation and execution logic \[18\], \[19\], \[20\], \[21\].

#### European context

- The literature is heavily **German/EPEX-centric**; European transfer is plausible via XBID/SIDC and flow-based coupling work \[22\], \[23\], but **Czech/PXE/Prague-specific academic coverage is thin**, with mostly exchange/credit-angle evidence \[24\], \[25\].
- **REMIT is a distinct compliance layer**, not a copy of financial MAR/MiFID practice, and now tightens further under REMIT II \[26\], \[27\].

## Paper Catalog (185 papers)

|  | Year | Cit/yr | Title | Authors | Journal |
|---:|:--:|:--:|:---|:---|:---|
| 1 | 2020 | 1.4 | Optimal Order Execution in Intraday Markets: Minimizing Costs in Trade Trajectories ([link](https://www.semanticscholar.org/paper/70f8a2b69157f766e5d80026a801d795879d53d7)) | Christopher Kath and F. Ziel | arXiv: Trading and Market Microstructure |
| 2 | 2022 | 3.7 | Intraday power trading: toward an arms race in weather forecasting? ([link](https://doi.org/10.1007/s00291-022-00698-5)) | Thomas Kuppelwieser and D. Wozabal | OR Spectrum |
| 3 | 2021 | 5.2 | Optimal bidding in hourly and quarter-hourly electricity price auctions: Trading large volumes of power with market impact and transaction costs ([link](https://doi.org/10.1016/j.eneco.2022.105974)) | Michał Narajewski and F. Ziel | Energy Economics |
| 4 | 2018 | 2.3 | German Intraday Electricity Market Analysis and Modeling Based on the Limit Order Book ([link](https://doi.org/10.1109/EEM.2018.8469829)) | Henry Martin and Scott Otterson | 2018 15th International Conference on the European Energy Market (EEM) |
| 5 | 2021 |  | High-frequency Electricity Trading: Empirics, Fundamentals, and Stochastics ([link](https://doi.org/10.17185/DUEPUBLICO/74512)) | Marcel Kremer |  |
| 6 | 2021 | 5.9 | An econometric model for intraday electricity trading ([link](https://doi.org/10.1098/rsta.2019.0624)) | Marcel Kremer, Ruediger Kiesel, and Florentina Paraschiv | Philosophical Transactions of the Royal Society A |
| 7 | 2021 | 2.7 | Liquidity costs on intraday power markets: Continuous trading versus auctions ([link](https://doi.org/10.1016/J.ENPOL.2021.112299)) | Thomas Kuppelwieser and D. Wozabal | Energy Policy |
| 8 | 2020 | 6.7 | Price formation and optimal trading in intraday electricity markets ([link](https://doi.org/10.1007/s11579-021-00307-z)) | Olivier F’eron, P. Tankov, and L. Tinsi | Mathematics and Financial Economics |
| 9 | 2017 | 19 | Econometric Analysis of 15-Minute Intraday Electricity Prices ([link](https://doi.org/10.1016/J.ENECO.2017.03.002)) | Ruediger Kiesel and Florentina Paraschiv | Energy Economics |
| 10 | 2019 | 4.0 | Modeling Intraday Markets under the New Advances of the Cross-Border Intraday Project (XBID): Evidence from the German Intraday Market ([link](https://doi.org/10.3390/en12224339)) | Christopher Kath | Energies |
| 11 | 2015 | 5.3 | An optimal trading problem in intraday electricity markets ([link](https://doi.org/10.1007/s11579-015-0150-8)) | R. Aïd, P. Gruet, and H. Pham | Mathematics and Financial Economics |
| 12 | 2025 |  | Optimal execution in intraday energy markets under Hawkes processes with transient impact ([link](https://doi.org/10.1080/14697688.2025.2597415)) | Konstantinos Chatziandreou and Sven Karbach | Quantitative Finance |
| 13 | 2022 | 1.0 | An Empirical Analysis of the Bid-ask Spread in the Continuous Intraday Trading of the German Power Market ([link](https://doi.org/10.5547/01956574.43.3.cbal)) | Clara Balardy | The Energy Journal |
| 14 | 2022 | 4.1 | Simulation-based Forecasting for Intraday Power Markets: Modelling Fundamental Drivers for Location, Shape and Scale of the Price Distribution ([link](https://doi.org/10.5547/01956574.45.3.shir)) | Simon Hirsch and F. Ziel | The Energy Journal |
| 15 | 2020 | 9.5 | Ensemble Forecasting for Intraday Electricity Prices: Simulating Trajectories ([link](https://doi.org/10.1016/J.APENERGY.2020.115801)) | Michał Narajewski and F. Ziel | ArXiv |
| 16 | 2020 | 0.2 | REMIT: ten years and counting ([link](https://doi.org/10.1080/17521440.2020.1805870)) | L. Hiemstra | Law and Financial Markets Review |
| 17 | 2022 | 5.4 | Trading on short-term path forecasts of intraday electricity prices ([link](https://doi.org/10.1016/j.eneco.2022.106125)) | Tomasz Serafin, Grzegorz Marcjasz, and R. Weron | Energy Economics |
| 18 | 2024 | 6.1 | Bayesian Hierarchical Probabilistic Forecasting of Intraday Electricity Prices ([link](https://doi.org/10.1016/j.apenergy.2024.124975)) | Daniel Nickelsen and Gernot Müller | ArXiv |
| 19 | 2020 | 3.7 | Intraday renewable electricity trading: advanced modeling and numerical optimal control ([link](https://doi.org/10.1186/s13362-020-0071-x)) | S. Glas et al. | Journal of Mathematics in Industry |
| 20 | 2016 | 7.3 | Trading behaviour on the continuous intraday market Elbas ([link](https://doi.org/10.1016/J.ENPOL.2015.10.045)) | Richard Scharff and M. Amelin | Energy Policy |
| 21 | 2019 | 6.5 | Forecasting the Price Distribution of Continuous Intraday Electricity Trading ([link](https://doi.org/10.3390/en12224262)) | Tim Janke and Florian Steinke | Energies |
| 22 | 2022 | 8.1 | Probabilistic Forecasting of German Electricity Imbalance Prices ([link](https://doi.org/10.3390/en15144976)) | Michał Narajewski | Energies |
| 23 | 2023 | 4.2 | Multivariate simulation‐based forecasting for intraday power markets: Modeling cross‐product price effects ([link](https://doi.org/10.1002/asmb.2837)) | Simon Hirsch and F. Ziel | Applied Stochastic Models in Business and Industry |
| 24 | 2020 | 0.3 | Working Paper \#35 AN EMPIRICAL ANALYSIS OF THE BID-ASK SPREAD IN THE CONTINUOUS INTRADAY TRADING OF THE GERMAN POWER MARKET ([link](https://www.semanticscholar.org/paper/b16485f5260a39fd249817ee81a3dc5599dc32a4)) | Clara Balardy |  |
| 25 | 2018 | 13 | Econometric modelling and forecasting of intraday electricity prices ([link](https://doi.org/10.1016/j.jcomm.2019.100107)) | Michał Narajewski and F. Ziel | Journal of Commodity Markets |
| 26 | 2018 | 9.8 | The value of forecasts: Quantifying the economic gains of accurate quarter-hourly electricity price forecasts ([link](https://doi.org/10.1016/j.eneco.2018.10.005)) | Christopher Kath and F. Ziel | Energy Economics |
| 27 | 2018 | 16 | Understanding intraday electricity markets: Variable selection and very short-term price forecasting using LASSO ([link](https://doi.org/10.1016/J.IJFORECAST.2019.02.001)) | Bartosz Uniejewski, Grzegorz Marcjasz, and R. Weron | International Journal of Forecasting |
| 28 | 2025 | 2.4 | OrderFusion: Encoding Orderbook for End-to-End Probabilistic Intraday Electricity Price Forecasting ([link](https://www.semanticscholar.org/paper/251c73bde036b0c485a66844fbab2b3f90de0ffa)) | Runyao Yu et al. |  |
| 29 | 2022 | 3.3 | Predicting Electricity Imbalance Prices and Volumes: Capabilities and Opportunities ([link](https://doi.org/10.3390/en15103645)) | J. Browell and C. Gilbert | Energies |
| 30 | 2020 | 18 | Optimal bidding of a virtual power plant on the Spanish day-ahead and intraday market for electricity ([link](https://doi.org/10.1016/J.EJOR.2019.07.022)) | D. Wozabal and Gunther Rameseder | Eur. J. Oper. Res. |
| 31 | 2020 |  | Energy Trading and Its Multiplicity of Supervisors: Effectiveness of Fragmented Supervision and Information Sharing in View of Reporting Obligations for Energy Trading Companies ([link](https://doi.org/10.2139/ssrn.3715737)) | L. Hiemstra | Social Science Research Network |
| 32 | 2020 | 9.7 | Very-Short-Term Probabilistic Forecasting for a Risk-Aware Participation in the Single Price Imbalance Settlement ([link](https://doi.org/10.1109/TPWRS.2019.2940756)) | J. Bottieau, L. Hubert, Z. De Grève, F. Vallée, and J. Toubeau | IEEE Transactions on Power Systems |
| 33 | 2016 | 11 | Are fundamentals enough? Explaining price variations in the German day-ahead and intraday power market ([link](https://doi.org/10.1016/J.ENECO.2015.12.013)) | Christian Pape, S. Hagemann, and C. Weber | Energy Economics |
| 34 | 2024 | 1.3 | Simulating and analyzing a sparse order book: an application to intraday electricity markets ([link](https://doi.org/10.1080/14697688.2025.2568693)) | Philippe Bergault and Enzo Cogn’eville | Quantitative Finance |
| 35 | 2025 | 5.6 | Orderbook Feature Learning and Asymmetric Generalization in Intraday Electricity Markets ([link](https://www.semanticscholar.org/paper/7d143ebfcbdb406fd4e643ee4c89b4218f7a4420)) | Runyao Yu, Ruochen Wu, Yongsheng Han, and Jochen L. Cremer |  |
| 36 | 2021 | 1.8 | Intraday imbalance optimization: incentives and impact of strategic intraday bidding behavior ([link](https://doi.org/10.1007/s12667-021-00445-9)) | C. Koch | Energy Systems |
| 37 | 2017 | 1.0 | Optimal market maker pricing in the German intraday power market ([link](https://www.semanticscholar.org/paper/31ade0f4d8394d543349730896a4f9999eebd0f1)) | N. V. Luckner, Á. Cartea, S. Jaimungal, and R. Kiesel |  |
| 38 | 2020 | 7.4 | Beating the Naïve—Combining LASSO with Naïve Intraday Electricity Price Forecasts ([link](https://doi.org/10.3390/EN13071667)) | Grzegorz Marcjasz, Bartosz Uniejewski, and R. Weron | Energies |
| 39 | 2024 | 0.9 | Optimal intraday power trading for single-price balancing markets: An adaptive risk-averse strategy using mixture models ([link](https://doi.org/10.1016/j.apenergy.2025.125754)) | Robin Bruneel, Mathijs Schuurmans, and Panagiotis Patrinos | Applied Energy |
| 40 | 2021 |  | Optimal Trading of a Fixed Quantity of Power in an Illiquid Continuous Intraday Market ([link](https://doi.org/10.1109/PowerTech46648.2021.9494885)) | Gilles Bertrand and A. Papavasiliou | 2021 IEEE Madrid PowerTech |
| 41 | 2019 | 4.2 | The Impact of Renewable Energy Forecasts on Intraday Electricity Prices ([link](https://doi.org/10.5547/2160-5890.10.1.skul)) | S. Kulakov and F. Ziel | Economics of Energy & Environmental Policy |
| 42 | 2016 | 0.9 | Optimal Trading Policies for Wind Energy Producer ([link](https://doi.org/10.1137/16M1093069)) | Zongjun Tan and P. Tankov | SIAM J. Financial Math. |
| 43 | 2020 | 4.1 | The way towards European electricity intraday auctions – Status quo and future developments ([link](https://doi.org/10.1016/j.enpol.2020.111731)) | Fabian Ocker and Vincent Jaenisch | Energy Policy |
| 44 | 2020 | 2.1 | Intraday Electricity Pricing of Night Contracts ([link](https://doi.org/10.3390/en13174501)) | Marcel Kremer, R. Kiesel, and Florentina Paraschiv | Energies |
| 45 | 2021 | 2.5 | Volatility and Dispersion of Hourly Electricity Contracts on the German Continuous Intraday Market ([link](https://doi.org/10.3390/en14227531)) | Rainer Baule and M. Naumann | Energies |
| 46 | 2018 | 4.5 | A Trading-Based Evaluation of Density Forecasts in a Real-Time Electricity Market ([link](https://doi.org/10.3390/EN11102658)) | Derek W. Bunn, A. Gianfreda, and S. Kermer | Energies |
| 47 | 2020 | 5.9 | The flow based market coupling arrangement in Europe: Implications for traders ([link](https://doi.org/10.1016/j.esr.2019.100444)) | T. Kristiansen | Energy Strategy Reviews |
| 48 | 2019 | 0.8 | Optimal Cross-Border Electricity Trading ([link](https://doi.org/10.2139/ssrn.3506915)) | Á. Cartea, M. Flora, Tiziano Vargiolu, and Georgi Slavov | SIAM J. Financial Math. |
| 49 | 2023 | 1.5 | A common shock model for multidimensional electricity intraday price modelling with application to battery valuation ([link](https://doi.org/10.1080/14697688.2024.2395906)) | Thomas Deschatre and X. Warin | Quantitative Finance |
| 50 | 2019 | 6.2 | Integrated European intra-day electricity market: Rules, modeling and analysis ([link](https://doi.org/10.1016/J.APENERGY.2018.12.073)) | Hong Lam Le, V. Ilea, and C. Bovo | Applied Energy |
| 51 | 2018 | 27 | The ENTSO-E Transparency Platform – A review of Europe’s most ambitious electricity data platform ([link](https://doi.org/10.1016/J.APENERGY.2018.04.048)) | Lion Hirth, J. Mühlenpfordt, and Marisa Bulkeley | Applied Energy |
| 52 | 2023 | 1.0 | EU Energy derivatives markets: Structure and risks ([link](https://doi.org/10.53479/30051)) | A. bouveret, Davide Di Nello, Jordi Gutiérrez, and Martin Haferkorn | Revista de Estabilidad Financiera |
| 53 | 2019 | 12 | Day-Ahead vs. Intraday—Forecasting the Price Spread to Maximize Economic Benefits ([link](https://doi.org/10.3390/EN12040631)) | K. Maciejowska, W. Nitka, and Tomasz Weron | Energies |
| 54 | 2014 | 11 | Bidding in sequential electricity markets: The Nordic case ([link](https://doi.org/10.1016/j.ejor.2014.04.027)) | T. Boomsma, Nina Juul, and Stein-Erik Fleten | Eur. J. Oper. Res. |
| 55 | 2016 | 6.4 | Intraday Markets for Power: Discretizing the Continuous Trading? ([link](https://doi.org/10.2139/SSRN.2723902)) | K. Neuhoff, Nolan Ritter, Aymen Salah-Abou-El-Enien, and Philippe Vassilopoulos |  |
| 56 | 2024 |  | Algorithmic trading of real-time electricity with machine learning ([link](https://doi.org/10.1080/14697688.2024.2420609)) | Vighnesh Natarajan Ganesh and D. Bunn | Quantitative Finance |
| 57 | 2021 | 13 | Enhancing load, wind and solar generation for day-ahead forecasting of electricity prices ([link](https://doi.org/10.1016/J.ENECO.2021.105273)) | K. Maciejowska, W. Nitka, and Tomasz Weron | Energy Economics |
| 58 | 2011 | 8.6 | Balancing and Intraday Market Design: Options for Wind Integration ([link](https://doi.org/10.2139/SSRN.1945724)) | Frieder Borggrefe and K. Neuhoff |  |
| 59 | 2010 | 16 | Adequate intraday market design to enable the integration of wind energy into the European power systems ([link](https://doi.org/10.1016/J.ENPOL.2009.07.040)) | C. Weber | Energy Policy |
| 60 | 2020 | 6.7 | Adaptive Trading in Continuous Intraday Electricity Markets for a Storage Unit ([link](https://doi.org/10.1109/TPWRS.2019.2957246)) | Gilles Bertrand and A. Papavasiliou | IEEE Transactions on Power Systems |
| 61 | 2019 | 1.9 | Estimation and Simulation of the Transaction Arrival Process in Intraday Electricity Markets ([link](https://doi.org/10.3390/en12234518)) | Michał Narajewski and F. Ziel | Energies |
| 62 | 2015 | 2.3 | Flexible Short-Term Power Trading: Gathering Experience in EU Countries ([link](https://doi.org/10.2139/SSRN.2639088)) | K. Neuhoff et al. |  |
| 63 | 2015 | 0.1 | Wholesale energy market monitoring: ACER and the technical implementation of REMIT ([link](https://doi.org/10.1109/IYCE.2015.7180802)) | S. Papageorgiou | 2015 5th International Youth Conference on Energy (IYCE) |
| 64 | 2013 | 3.6 | Price Determinants in the German Intraday Market for Electricity: An Empirical Analysis ([link](https://doi.org/10.2139/SSRN.2352854)) | S. Hagemann |  |
| 65 | 2010 | 31 | Short-Term Trading for a Wind Power Producer ([link](https://doi.org/10.1109/PES.2010.5589379)) | J. Morales, A. Conejo, and J. Pérez-Ruiz | IEEE Transactions on Power Systems |
| 66 | 2019 | 20 | The impact of renewable energy forecast errors on imbalance volumes and electricity spot prices ([link](https://doi.org/10.1016/j.enpol.2019.06.035)) | S. Goodarzi, H. Perera, and Derek Bunn | Energy Policy |
| 67 | 2019 | 13 | Short-term electricity trading for system balancing: An empirical analysis of the role of intraday trading in balancing Germany’s electricity system ([link](https://doi.org/10.1016/J.RSER.2019.109275)) | C. Koch and Lion Hirth | Renewable and Sustainable Energy Reviews |
| 68 | 2023 | 4.4 | Market Manipulation in Stock and Power Markets: A Study of Indicator-Based Monitoring and Regulatory Challenges ([link](https://doi.org/10.3390/en16041894)) | Yu Hao, B. Vand, Benjamín Manrique Delgado, and Simone Baldi | Energies |
| 69 | 2015 | 1.3 | Trading Volumes in Intraday Markets - Theoretical Reference Model and Empirical Observations in Selected European Markets ([link](https://www.semanticscholar.org/paper/e65baae0912dd186c849ceb8f0c19f8c29392dc7)) | S. Hagemann and C. Weber |  |
| 70 | 2017 | 5.9 | Contract durations in the electricity market: Causal impact of 15 min trading on the EPEX spot market ([link](https://doi.org/10.1016/J.ENECO.2017.11.019)) | Joscha Märkle-Huss, S. Feuerriegel, S. Feuerriegel, and Dirk Neumann | Energy Economics |
| 71 | 2011 | 3.3 | Power Spot Price Models with negative Prices ([link](https://doi.org/10.21314/JEM.2011.079)) | S. Schneider | The Journal of Energy Markets |
| 72 | 2017 |  | STATISTICAL ARBITRAGE IN SINGLE PRICE BALANCING MARKETS ([link](https://www.semanticscholar.org/paper/59f33dd9cf5cfbb02cf782d7aa86354d62fc1070)) | S. Bunn |  |
| 73 | 2022 |  | Flexible Short-Term Electricity Certificates—An Analysis of Trading Strategies on the Continuous Intraday Market ([link](https://doi.org/10.3390/en15176344)) | Rainer Baule and M. Naumann | Energies |
| 74 | 2005 | 8.4 | The Nature of Power Spikes: A Regime-Switch Approach ([link](https://doi.org/10.2202/1558-3708.1361)) | Cyriel de Jong | Studies in Nonlinear Dynamics & Econometrics |
| 75 | 2017 | 4.6 | Modeling the impact of wind and solar power forecasting errors on intraday electricity prices ([link](https://doi.org/10.1109/EEM.2017.7981900)) | F. Ziel | 2017 14th International Conference on the European Energy Market (EEM) |
| 76 | 2022 | 0.5 | A Cross‐Border Market Model with Limited Transmission Capacities ([link](https://doi.org/10.1111/mafi.70009)) | Dörte Kreher and Cassandra Milbradt | Mathematical Finance |
| 77 | 2006 | 1.4 | Quantitative methods for electricity trading and risk management : advanced mathematical and statistical methods for energy finance ([link](https://doi.org/10.1057/9780230598348)) | Stefano Fiorenzani |  |
| 78 | 2018 | 1.0 | An Analysis of Threshold Policies for Trading in Continuous Intraday Electricity Markets ([link](https://doi.org/10.1109/EEM.2018.8469774)) | Gilles Bertrand and A. Papavasiliou | 2018 15th International Conference on the European Energy Market (EEM) |
| 79 | 2020 | 1.1 | The Economic Value of Wind Energy Nowcasting ([link](https://doi.org/10.3390/en13205266)) | Aurore Dupré, P. Drobinski, J. Badosa, C. Briard, and P. Tankov | Energies |
| 80 | 2019 | 0.7 | Passive Balancing through Intraday Trading ([link](https://doi.org/10.2139/ssrn.3399001)) | C. Koch and Philipp Maskos | SSRN Electronic Journal |
| 81 | 2024 | 6.5 | Frequent Auctions for Intraday Electricity Markets ([link](https://doi.org/10.5547/01956574.45.1.cgra)) | C. Graf, Thomas Kuppelwieser, and D. Wozabal | The Energy Journal |
| 82 | 2020 | 77 | Forecasting day-ahead electricity prices: A review of state-of-the-art algorithms, best practices and an open-access benchmark ([link](https://doi.org/10.1016/j.apenergy.2021.116983)) | J. Lago, Grzegorz Marcjasz, B. Schutter, and R. Weron | ArXiv |
| 83 | 2021 | 7.5 | The effects of wind power on electricity markets: A case study of the Swedish intraday market ([link](https://doi.org/10.1016/J.ENECO.2021.105159)) | Xiao Hu, J. Jaraitė, and A. Kažukauskas | Energy Economics |
| 84 | 2018 |  | Using published bid/ask curves to error dress spot electricity price forecasts ([link](https://www.semanticscholar.org/paper/4d82cb797991adb04e9b66cfaab372c57ad0c019)) | Gunnhildur H. Steinbakk, Alex Lenkoski, R. B. Huseby, Anders Løland, and Tor Arne Oigaard | arXiv: Statistical Finance |
| 85 | 2010 | 1.6 | A comparison of imbalance settlement designs and results of Germany and the Netherlands ([link](https://www.semanticscholar.org/paper/01e93c856651b251054cd5cb5639ac80d35081b5)) | R. V. D. Veen, A. Abbasy, and R. Hakvoort |  |
| 86 | 2020 | 2.4 | A market framework for grid balancing support through imbalances trading ([link](https://doi.org/10.1016/j.rser.2020.110467)) | J. Lago, K. Poplavskaya, G. Suryanarayana, and B. de Schutter | Renewable and Sustainable Energy Reviews |
| 87 | 2021 | 4.7 | A Reinforcement Learning Approach for the Continuous Electricity Market of Germany: Trading from the Perspective of a Wind Park Operator ([link](https://doi.org/10.1016/j.egyai.2022.100139)) | Malte Lehna, Bjorn Hoppmann, René Heinrich, and Christoph Scholz | ArXiv |
| 88 | 2019 | 1.3 | Reinforcement-Learning Based Threshold Policies for Continuous Intraday Electricity Market Trading ([link](https://doi.org/10.1109/PESGM40551.2019.8973602)) | Gilles Bertrand and A. Papavasiliou | 2019 IEEE Power & Energy Society General Meeting (PESGM) |
| 89 | 2017 | 4.1 | Joint price and volumetric risk in wind power trading: A copula approach ([link](https://doi.org/10.1016/J.ENECO.2016.11.023)) | Anca Pircalabu, Thomas Hvolby, Jesper Jung, and Esben Høg | Energy Economics |
| 90 | 2013 |  | Coping with the Clearing Obligation - From the Perspective of an Industrial Corporate with a Focus on Commodity Markets ([link](https://doi.org/10.2139/SSRN.2265792)) | F. Lehrbass |  |
| 91 | 2014 |  | Corporate Production and Hedging Decisions Under Dodd-Frank and EMIR ([link](https://doi.org/10.2139/SSRN.2491783)) | F. Lehrbass |  |
| 92 | 2013 | 2.2 | Transparency in Electricity Markets ([link](https://doi.org/10.5547/2160-5890.2.2.5)) | N. V. D. Fehr | Economics of Energy and Environmental Policy |
| 93 | 2020 | 1.4 | Modeling and Managing Joint Price and Volumetric Risk for Volatile Electricity Portfolios ([link](https://doi.org/10.3390/en13143578)) | Johanne Kaufmann, Philipp Artur Kienscherf, and W. Ketter | Energies |
| 94 | 2006 | 3.1 | A survey on risk management in electricity markets ([link](https://doi.org/10.1109/PES.2006.1709009)) | Min Liu, Felix F. Wu, and Y. Ni | 2006 IEEE Power Engineering Society General Meeting |
| 95 | 2025 |  | REMIT II: verscherpt toezicht op de groothandelsmarkt voor energie ([link](https://doi.org/10.5553/menm/138762362025028002007)) | L. Hiemstra | Markt en Mededinging |
| 96 | 2020 | 5.9 | Evolving Bidding Formats and Pricing Schemes in USA and Europe Day-Ahead Electricity Markets ([link](https://doi.org/10.3390/EN13195020)) | I. Herrero, Pablo Rodilla, and C. Batlle | Energies |
| 97 | 2014 | 124 | Electricity price forecasting: A review of the state-of-the-art with a look into the future ([link](https://doi.org/10.1016/J.IJFORECAST.2014.08.008)) | R. Weron | HSC Research Reports |
| 98 | 2025 |  | The Evolution of Probabilistic Price Forecasting Techniques: A Review of the Day-Ahead, Intra-Day, and Balancing Markets ([link](https://doi.org/10.48550/arXiv.2511.05523)) | Ciaran O’Connor, Mohamed Bahloul, Steven D. Prestwich, and Andrea Visentin | ArXiv |
| 99 | 2019 | 1.0 | Intraday Imbalance Optimization: Incentives and Impact of strategic Intraday Bidding in Germany ([link](https://doi.org/10.2139/ssrn.3495047)) | C. Koch | SSRN Electronic Journal |
| 100 | 2018 | 2.9 | The impact of intraday markets on the market value of flexibility — Decomposing effects on profile and the imbalance costs ([link](https://doi.org/10.1016/J.ENECO.2018.10.004)) | Christian Pape | Energy Economics |
| 101 | 2024 |  | Daily Episodic and Continuous Arbitrage Trading With Electric Batteries ([link](https://doi.org/10.1177/01956574241281143)) | Shujin Hou and Derek Bunn | The Energy Journal |
| 102 | 2009 | 0.3 | Transparency and confidentiality in competitive electricity markets ([link](https://www.semanticscholar.org/paper/36eeb14f2f36917139b7a95954f532e13a7bd9db)) | L. Hooper, Paul Twomey, and D. Newbery |  |
| 103 | 2007 | 1.5 | An Institutional Frame to Compare Alternative Market Designs in EU Electricity Balancing ([link](https://doi.org/10.17863/CAM.5153)) | J. Glachant and M. Saguan |  |
| 104 | 2006 | 8.7 | Using extreme value theory to measure value-at-risk for daily electricity spot prices ([link](https://doi.org/10.1016/J.IJFORECAST.2005.10.002)) | K. F. Chan and P. Gray | International Journal of Forecasting |
| 105 | 2018 | 3.7 | Impact of harmonised common balancing capacity procurement in selected Central European electricity balancing markets ([link](https://doi.org/10.1016/J.APENERGY.2018.03.120)) | B. Dallinger, H. Auer, and G. Lettner | Applied Energy |
| 106 | 2016 | 48 | Recent advances in electricity price forecasting: A review of probabilistic forecasting ([link](https://doi.org/10.1016/J.RSER.2017.05.234)) | J. Nowotarski and R. Weron | HSC Research Reports |
| 107 | 2007 | 11 | Spot and Derivative Pricing in the EEX Power Market ([link](https://doi.org/10.1016/J.JBANKFIN.2007.04.011)) | Michael Bierbrauer, C. Menn, S. Rachev, and S. Trück |  |
| 108 | 2014 | 3.7 | Market Design with Centralized Wind Power Management: Handling Low-predictability in Intraday Markets ([link](https://doi.org/10.5547/01956574.35.1.6)) | Arthur Henriot | The Energy Journal |
| 109 | 2024 | 3.2 | An Algorithm for Modelling Rolling Intrinsic Battery Trading on the Continuous Intraday Market ([link](https://doi.org/10.1145/3717413.3717428)) | Leo Semmelmann, Jannik Dresselhaus, Kim K. Miskiw, Jan Ludwig, and Christof Weinhardt | ACM SIGENERGY Energy Informatics Review |
| 110 | 2025 | 24 | A Review of Electricity Price Forecasting Models in the Day-Ahead, Intra-Day, and Balancing Markets ([link](https://doi.org/10.3390/en18123097)) | Ciaran O’Connor, Mohamed Bahloul, Steven D. Prestwich, and Andrea Visentin | Energies |
| 111 | 2010 | 6.6 | Portfolio Optimization for Power Plants: The Impact of Credit Risk Mitigation and Margining ([link](https://doi.org/10.2139/SSRN.1683508)) | J. Lang and R. Madlener |  |
| 112 | 2010 | 1.0 | Liquidity risks on power exchanges ([link](https://www.semanticscholar.org/paper/69116f34c762444539f705d272d4597388b03421)) | Gauthier de Maere d’Aertrycke and Y. Smeers |  |
| 113 | 2018 | 8.9 | The effect of wind and solar power forecasts on day-ahead and intraday electricity prices in Germany ([link](https://doi.org/10.1016/J.ENECO.2018.07.006)) | Marc Gürtler and Thomas Paulsen | Energy Economics |
| 114 | 2020 | 3.8 | Balancing Generation from Renewable Energy Sources: Profitability of an Energy Trader ([link](https://doi.org/10.3390/en13010205)) | Christopher Kath et al. | Energies |
| 115 | 2025 |  | The Regulation of Market Manipulation in the EU Energy Sector: Doctrinal Analysis of REMIT II’s Sanctioning Framework ([link](https://doi.org/10.3390/laws14050061)) | I. Berceanu, M. Cărăușan, and Alina Zorzoană | Laws |
| 116 | 2024 | 4.3 | Quantifying and modeling price volatility in the Dutch intraday electricity market ([link](https://doi.org/10.1016/j.egyr.2024.09.031)) | Dane Birkeland, T. Alskaif, Steven Duivenvoorden, Marvin Meeng, and J. Pennings | Energy Reports |
| 117 | 2015 | 0.2 | Credit Value Adjustment and Economic Motivation to Trade on PXE ([link](https://doi.org/10.18267/J.PEP.517)) | Igor Paholok |  |
| 118 | 2018 | 6.3 | Algorithmic Bidding for Virtual Trading in Electricity Markets ([link](https://doi.org/10.1109/TPWRS.2018.2862246)) | Sevi Baltaoglu, L. Tong, and Qing Zhao | IEEE Transactions on Power Systems |
| 119 | 2019 | 6.5 | Feature-Driven Improvement of Renewable Energy Forecasting and Trading ([link](https://doi.org/10.1109/TPWRS.2020.2975246)) | Miguel Angel Muñoz, J. Morales, and S. Pineda | IEEE Transactions on Power Systems |
| 120 | 2014 | 0.7 | The Integration of Renewables in Continuous Intraday Markets for Electricity ([link](https://doi.org/10.2139/SSRN.2405454)) | Alexander von Selasinsky |  |
| 121 | 2019 | 0.6 | Intraday Renewable Electricity Trading: Advanced Modeling and Optimal Control ([link](https://doi.org/10.1007/978-3-030-27550-1_59)) | S. Glas et al. | Progress in Industrial Mathematics at ECMI 2018 |
| 122 | 2022 | 19 | Ancillary services markets in europe: Evolution and regulatory trade-offs ([link](https://doi.org/10.1016/j.rser.2021.111850)) | G. Rancilio, A. Rossi, D. Falabretti, A. Galliani, and M. Merlo | Renewable and Sustainable Energy Reviews |
| 123 | 2022 | 5.3 | Integration of European Electricity Balancing Markets ([link](https://doi.org/10.3390/en15062240)) | C. Roumkos, P. Biskas, and I. Marneris | Energies |
| 124 | 2024 | 11 | Electricity Price Forecasting in the Irish Balancing Market ([link](https://doi.org/10.48550/arXiv.2402.06714)) | Ciaran O’Connor, Joseph Collins, Steven D. Prestwich, and Andrea Visentin | ArXiv |
| 125 | 2025 |  | A Review of Balancing Price Forecasting in the Context of Renewable-Rich Power Systems, Highlighting Profit-Aware and Spike-Resilient Approaches ([link](https://doi.org/10.3390/en18246460)) | Ali Dinler | Energies |
| 126 | 2011 | 1.9 | DESIGN AND INTEGRATI ON OF BALANCING MARKETS IN EUROPE ([link](https://www.semanticscholar.org/paper/57e535b42eaeaab9ccb38adc287e0a139f2ae17f)) | L. Vandezande |  |
| 127 | 2020 | 0.3 | Electricity Market Coupling in Europe: Status Quo and Future Challenges ([link](https://doi.org/10.1142/9789813278387_0005)) | Roland Füss, Steffen Mahringer, and Marcel Prokopczuk | Handbook of Energy Finance |
| 128 | 2024 | 0.5 | Agent based modeling for intraday electricity markets ([link](https://doi.org/10.1007/s12597-024-00805-w)) | A. Alberizzi, Paolo Di Barba, and F. Ziel | OPSEARCH |
| 129 | 2016 | 2.5 | Structural models for coupled electricity markets ([link](https://doi.org/10.2139/SSRN.2501352)) | Ruediger Kiesel and Michael Kusterman | Journal of Commodity Markets |
| 130 | 2019 | 0.7 | Trading wind power through physically settled options and short‐term electricity markets ([link](https://doi.org/10.1002/WE.2383)) | A. Papakonstantinou, Georgia Champeri, S. Delikaraoglou, and P. Pinson | Wind Energy |
| 131 | 2025 |  | Hierarchical Techniques to Forecast Joint Price-Volume Distributions of Intraday, Continuous Power Markets ([link](https://doi.org/10.1145/3679240.3734599)) | N. Thokala, Basheer Ahammad Ragimanu, V. Sarangan, and Mohan Raj Velayudhan Kumar | Proceedings of the 16th ACM International Conference on Future and Sustainable Energy Systems |
| 132 | 2020 | 5.3 | Factor models in the German electricity market: Stylized facts, seasonality, and calibration ([link](https://doi.org/10.1016/J.ENECO.2019.03.024)) | W. Hinderks and A. Wagner | Energy Economics |
| 133 | 2005 | 24 | Pricing in Electricity Markets: A Mean Reverting Jump Diffusion Model with Seasonality ([link](https://doi.org/10.1080/13504860500117503)) | Á. Cartea and Marcelo G. Figueroa | Applied Mathematical Finance |
| 134 | 2008 | 6.6 | MULTI-FACTOR JUMP-DIFFUSION MODELS OF ELECTRICITY PRICES ([link](https://doi.org/10.1142/S0219024908004907)) | T. Meyer‐Brandis and P. Tankov | International Journal of Theoretical and Applied Finance |
| 135 | 2009 | 5.7 | A two-factor model for the electricity forward market ([link](https://doi.org/10.1080/14697680802126530)) | R. Kiesel, G. Schindlmayr, and Reik H. Börger | Quantitative Finance |
| 136 | 2019 | 7.7 | A Literature Review of Intraday Electricity Markets and Prices ([link](https://doi.org/10.1109/PTC.2019.8810752)) | Priyanka Shinde and M. Amelin | 2019 IEEE Milan PowerTech |
| 137 | 2013 |  | Price dynamics in electricity spot markets ([link](https://www.semanticscholar.org/paper/568401bc327d69d30da2f2418975c802e688b427)) | Florentina Paraschiv and Michael Schürle |  |
| 138 | 2022 | 1.6 | Can the European intraday market be designed as a congestion management tool? ([link](https://doi.org/10.1016/j.eneco.2022.106171)) | Somayeh Rahimi Alangi, Endre Bjørndal, and Mette Bjørndal | Energy Economics |
| 139 | 2018 | 1.3 | Impact of Current Market Developments in Europe on Deterministic Grid Frequency Deviations and Frequency Restauration Reserve Demand ([link](https://doi.org/10.1109/EEM.2018.8469210)) | T. Weissbach, Simon Remppis, and Hendrik Lens | 2018 15th International Conference on the European Energy Market (EEM) |
| 140 | 2019 |  | Volatility and Dispersion of Hourly Electricity Contracts on the Epex Spot Continuous Intraday Market ([link](https://doi.org/10.2139/ssrn.3480527)) | Rainer Baule and M. Naumann | SSRN Electronic Journal |
| 141 | 2020 | 0.2 | Case studies analysis of REMIT regulation ([link](https://doi.org/10.1109/EEM49802.2020.9221989)) | A. Zani et al. | 2020 17th International Conference on the European Energy Market (EEM) |
| 142 | 2021 | 8.4 | Toward a fundamental understanding of flow-based market coupling for cross-border electricity trading ([link](https://doi.org/10.1016/J.ADAPEN.2021.100027)) | David Schönheit et al. |  |
| 143 | 2023 | 12 | The Role of Weather Predictions in Electricity Price Forecasting Beyond the Day-Ahead Horizon ([link](https://doi.org/10.1109/TPWRS.2022.3180119)) | Raffaele Sgarlato and F. Ziel | IEEE Transactions on Power Systems |
| 144 | 2013 | 4.6 | Measuring competitiveness of the EPEX spot market for electricity ([link](https://doi.org/10.1016/J.ENPOL.2013.07.052)) | C. Graf and D. Wozabal | Energy Policy |
| 145 | 2017 |  | Limited Liquidity, Market Asymmetry, and Stylized Facts of Asset Returns: An Example from Electricity Markets ([link](https://doi.org/10.2139/SSRN.2888944)) | Jakob Krause |  |
| 146 | 2015 | 1.2 | Electricity Spot and Derivatives Pricing When Markets are Interconnected ([link](https://doi.org/10.2139/SSRN.2378200)) | Roland Füss, Steffen Mahringer, and Marcel Prokopczuk |  |
| 147 | 2008 | 6.0 | Intra-day and regime-switching dynamics in electricity price formation ([link](https://doi.org/10.1016/J.ENECO.2008.02.004)) | Nektaria V. Karakatsani and D. Bunn | Energy Economics |
| 148 | 2002 | 2.2 | Power exchange spot market trading in Europe: theoretical considerations and empirical evidence ([link](https://www.semanticscholar.org/paper/0c6a9240e6b355b32ae8084f8255f5a02ce304cc)) | R. Madlener and M. Kaufmann |  |
| 149 | 2021 | 2.5 | Analyzing Trade in Continuous Intra-Day Electricity Market: An Agent-Based Modeling Approach ([link](https://doi.org/10.3390/en14133860)) | Priyanka Shinde, Ioannis Boukas, D. Radu, Miguel Manuel de Villena, and M. Amelin | Energies |
| 150 | 2017 | 3.8 | A new approach to electricity market clearing with uniform purchase price and curtailable block orders ([link](https://doi.org/10.1016/j.apenergy.2018.06.003)) | Iacopo Savelli, B. Cornélusse, Antonio Giannitrapani, S. Paoletti, and A. Vicino | Applied Energy |
| 151 | 2018 |  | Energy Market Surveillance in the EU and US: A Study of Market Designs, Regulations, and Detection Algorithms ([link](https://www.semanticscholar.org/paper/c2919cd586bc4638092fd4eba7d0c669810422e9)) | Van Stappen and Jonas Viktor |  |
| 152 | 2022 | 0.8 | Analysis of the intraday market: statistical analysis of German single intraday coupling ([link](https://doi.org/10.23919/AEIT56783.2022.9951806)) | A. Alberizzi, A. Zani, and Paolo Di Barba | 2022 AEIT International Annual Conference (AEIT) |
| 153 | 2016 | 0.3 | Optimal Trading Strategies in Intraday Power Markets ([link](https://doi.org/10.1057/9781137412973_8)) | Enrico Edoli, Stefano Fiorenzani, and Tiziano Vargiolu |  |
| 154 | 2019 |  | Can Intraday Market be Designed as a Congestion Management Tool? ([link](https://www.semanticscholar.org/paper/f1ae1d8e85c52e15733ccca2ee00da242a6382cf)) | Somayeh Rahimi Alangi, Mette Bjørndal, and Endre Bjørndal |  |
| 155 | 2003 | 2.0 | New models for integrated short-term forward electricity markets ([link](https://doi.org/10.1109/TPWRS.2003.810686)) | Shangyou Hao and Fulin Zhuang | IEEE Transactions on Power Systems |
| 156 | 2023 | 1.5 | Forecasting different dimensions of liquidity in the intraday electricity markets: A review ([link](https://doi.org/10.3934/energy.2023044)) | Sameer Thakare, N. Bokde, and A. E. Feijóo-Lorenzo | AIMS Energy |
| 157 | 2025 |  | Leveraging Asynchronous Cross-border Market Data for Improved Day-Ahead Electricity Price Forecasting in European Markets ([link](https://doi.org/10.48550/arXiv.2507.13250)) | Maria Margarida Mascarenhas, Jilles De Blauwe, M. Amelin, and H. Kazmi | ArXiv |
| 158 | 2021 | 4.6 | Electricity Price Forecasting in European Day Ahead Markets: A Greedy Consideration of Market Integration ([link](https://doi.org/10.1109/ACCESS.2021.3108629)) | Ties Van Der Heijden, Jesus Lago, P. Palensky, and E. Abraham | IEEE Access |
| 159 | 2009 | 0.4 | Lacking balancing market harmonisation in Europe: room for trader profits at the expense of economic efficiency? ([link](https://www.semanticscholar.org/paper/1f80eb20bcb393a0deb28edbe6950e81f5cb3c4c)) | L. Vandezande et al. |  |
| 160 | 2014 | 1.9 | Algorithmic properties of the all-European day-ahead electricity market ([link](https://doi.org/10.1109/EEM.2014.6861275)) | Á. Sleisz, P. Sőrés, and D. Raisz | 11th International Conference on the European Energy Market (EEM14) |
| 161 | 2019 | 0.4 | Enhancing load, wind and solar generation forecasts in day-ahead forecasting of spot and intraday electricity prices ([link](https://www.semanticscholar.org/paper/0ffeb98541e5dc42fb3aeede1bdb6b53911e5a85)) | K. Maciejowska, W. Nitka, and Tomasz Weron | HSC Research Reports |
| 162 | 2023 | 2.5 | A Multi-Agent Model for Cross-Border Trading in the Continuous Intraday Electricity Market ([link](https://doi.org/10.2139/ssrn.4350030)) | Priyanka Shinde, Giulia Gamberi, and M. Amelin | SSRN Electronic Journal |
| 163 | 2018 | 6.2 | Efficient Forecasting of Electricity Spot Prices with Expert and LASSO Models ([link](https://doi.org/10.3390/EN11082039)) | Bartosz Uniejewski and R. Weron | Energies |
| 164 | 2011 | 4.8 | Short-Term Congestion Forecasting in Wholesale Power Markets ([link](https://doi.org/10.1109/TPWRS.2011.2123118)) | Qun Zhou, Leigh Tesfatsion, and Chen-Ching Liu | IEEE Transactions on Power Systems |
| 165 | 2021 | 6.5 | Business cases of aggregated flexibilities in multiple electricity markets in a European market design ([link](https://doi.org/10.1016/J.ENCONMAN.2020.113783)) | D. Schwabeneder, Carlo Corinaldesi, G. Lettner, and H. Auer | Energy Conversion and Management |
| 166 | 2021 | 2.4 | Impact of Flow Based Market Coupling on the European Electricity Markets ([link](https://doi.org/10.1007/s00550-021-00520-w)) | R. Finck | Sustainability Management Forum \| NachhaltigkeitsManagementForum |
| 167 | 2019 | 2.6 | The future electricity intraday market design ([link](https://www.semanticscholar.org/paper/5022456d72ca6bde55fcaca6c3a04efff4c01c09)) | A. Ehrenmann et al. |  |
| 168 | 2023 | 2.8 | The economic impacts of integrating European balancing markets: The case of the newly installed aFRR energy market-coupling platform PICASSO ([link](https://doi.org/10.1016/j.eneco.2023.107124)) | Martijn Backer, D. Keles, and Emil Kraft | Energy Economics |
| 169 | 2019 | 3.3 | A Machine Learning Framework for Algorithmic Trading with Virtual Bids in Electricity Markets ([link](https://doi.org/10.1109/PESGM40551.2019.8973750)) | Wei Wang and N. Yu | 2019 IEEE Power & Energy Society General Meeting (PESGM) |
| 170 | 2009 | 0.8 | Algorithmic challenges and current problems in market coupling regimes ([link](https://doi.org/10.1002/ETEP.354)) | B. Tersteegen, C. Schröders, Sebastian Stein, and H. Haubrich | European Transactions on Electrical Power |
| 171 | 2015 | 0.1 | REMIT and the monitoring provisions of the EU energy markets ([link](https://doi.org/10.1109/EEM.2015.7216637)) | T. Medved, E. Lakić, I. Zlatar, and A. Gubina | 2015 12th International Conference on the European Energy Market (EEM) |
| 172 | 2018 | 0.1 | Optimal trading strategies for wind power producers in futures and short-term electricity markets ([link](https://www.semanticscholar.org/paper/6f840e053a81f6407a563092958a96dfa56c3dd4)) | A. Papakonstantinou, Georgia Champeri, S. Delikaraoglou, and P. Pinson |  |
| 173 | 2024 | 2.0 | Examining the drivers of the imbalance price: Insights from the balancing mechanism in the United Kingdom. ([link](https://doi.org/10.1016/j.jenvman.2024.123239)) | Huanhuan Chen, Jinke Li, Nigel O’Leary, and Jing Shao | Journal of environmental management |
| 174 | 2004 | 4.8 | Systematic Features of High-Frequency Volatility in Australian Electricity Markets: Intraday Patterns, Information Arrival and Calendar Effects ([link](https://doi.org/10.5547/ISSN0195-6574-EJ-Vol26-No4-2)) | H. Higgs and A. Worthington | The Energy Journal |
| 175 | 2007 | 6.0 | A structural model for electricity prices with spikes: Measurement of spike risk and optimal policies for hydropower plant operation ([link](https://doi.org/10.2139/SSRN.560603)) | Takashi Kanamura and Kazuhiko Ōhashi | Energy Economics |
| 176 | 2024 | 1.0 | Market Equilibria in Cross-Border Balancing Platforms ([link](https://doi.org/10.1109/TEMPR.2024.3360475)) | Jacques Cartuyvels, Gilles Bertrand, and A. Papavasiliou | IEEE Transactions on Energy Markets, Policy and Regulation |
| 177 | 2019 | 4.0 | Algorithm design for European electricity market clearing with joint allocation of energy and control reserves ([link](https://doi.org/10.1016/J.IJEPES.2019.04.006)) | D. Divényi, Beáta Polgári, Á. Sleisz, P. Sőrés, and D. Raisz | International Journal of Electrical Power & Energy Systems |
| 178 | 2021 | 1.3 | Investigating minimum income condition orders on European power exchanges: Controversial properties and enhancement proposals ([link](https://doi.org/10.1016/j.apenergy.2020.116070)) | D. Divényi, Beáta Polgári, Á. Sleisz, P. Sőrés, and D. Raisz | Applied Energy |
| 179 | 2005 | 0.5 | Monitoring and surveillance of wholesale electricity markets: roles, responsibilities and challenges ([link](https://doi.org/10.1109/PES.2005.1489475)) | Eddie Dehdashti | IEEE Power Engineering Society General Meeting, 2005 |
| 180 | 2008 | 0.1 | The European Electricity Market and Cross-Border Transmission ([link](https://doi.org/10.14311/985)) | M. Adamec, M. Indráková, and M. Karajica |  |
| 181 | 2023 | 1.2 | Analyzing the European Intraday Market: Statistical Insights and Strategies for Continuous Trading in Renewable Energy Systems ([link](https://doi.org/10.20508/ijrer.v13i4.14208.g8825)) |  | International Journal of Renewable Energy Research |
| 182 | 2023 |  | Electricity Markets with Complex Orders: A Review of Theory and Application ([link](https://doi.org/10.1109/EI259745.2023.10512502)) | Xinyi Ren, Runfan Zhang, and Yusong Yang | 2023 IEEE 7th Conference on Energy Internet and Energy System Integration (EI2) |
| 183 | 2021 | 0.2 | Electricity Market Liquidity and Price Spikes: Evidence from Hungary ([link](https://doi.org/10.3311/ppso.16857)) | Mátyás Bajai, Attila A. Vig, and Olivér Hortay | Periodica Polytechnica Social and Management Sciences |
| 184 | 2024 | 4.0 | Extrapolating the long-term seasonal component of electricity prices for forecasting in the day-ahead market ([link](https://doi.org/10.1016/j.jcomm.2024.100449)) | Katarzyna Chȩć, Bartosz Uniejewski, and R. Weron | Journal of Commodity Markets |
| 185 | 2017 | 0.1 | Impact of Czech intraday market on the electricity prices ([link](https://www.semanticscholar.org/paper/0ba2203341dd9d6a95cb0133f4ebe180e67b61b8)) | Samuel Béreš |  |

### Paper Details

1\. · 100% match · 2020 · 1.4 cit/yr\
**Optimal Order Execution in Intraday Markets: Minimizing Costs in Trade Trajectories** ([link](https://www.semanticscholar.org/paper/70f8a2b69157f766e5d80026a801d795879d53d7))\
Christopher Kath and F. Ziel\
*arXiv: Trading and Market Microstructure* · Sep 16, 2020 · 8 citations

> Optimal execution, i.e., the determination of the most cost-effective way to trade volumes in continuous trading sessions, has been a topic of interest in the equity trading world for years. Electricity intraday trading slowly follows this trend but is far from being well-researched. The underlying problem is a very complex one. Energy traders, producers, and electricity wholesale companies receive various position updates from customer businesses, renewable energy production, or plant outages and need to trade these positions in intraday markets. They have a variety of options when it comes to position sizing or timing. Is it better to trade all amounts at once? Should they split orders into smaller pieces? Taking the German continuous hourly intraday market as an example, this paper derives an appropriate model for electricity trading. We present our results from an out-of-sample study and differentiate between simple benchmark models and our more refined optimization approach that takes into account order book depth, time to delivery, and different trading regimes like XBID (Cross-Border Intraday Project) trading. Our paper is highly relevant as it contributes further insight into the academic discussion of algorithmic execution in continuous intraday markets and serves as an orientation for practitioners. Our initial results suggest that optimal execution strategies have a considerable monetary impact.

------------------------------------------------------------------------

2\. · 100% match · 2022 · 3.7 cit/yr\
**Intraday power trading: toward an arms race in weather forecasting?** ([link](https://doi.org/10.1007/s00291-022-00698-5))\
Thomas Kuppelwieser and D. Wozabal\
*OR Spectrum* · Nov 7, 2022 · 13 citations

> We propose the first speculative weather-based algorithmic trading strategy on a continuous intraday power market. The strategy uses neither production assets nor power demand and generates profits purely based on superior information about aggregate output of weather-dependent renewable production. We use an optimized parametric policy based on state-of-the-art intraday updates of renewable production forecasts and evaluate the resulting decisions out-of-sample for one year of trading based on detailed order book level data for the German market. Our strategies yield significant positive profits, which suggests that intraday power markets are not semi-strong efficient. Furthermore, sizable additional profits could be made using improved forecasts of renewable output, which implies that the quality of forecasts is an important factor for profitable trading strategies. This has the potential to trigger an arms race for more frequent and more accurate forecasts, which would likely lead to increased market efficiency, more reliable price signals, and more liquidity.

------------------------------------------------------------------------

3\. · 100% match · 2021 · 5.2 cit/yr\
**Optimal bidding in hourly and quarter-hourly electricity price auctions: Trading large volumes of power with market impact and transaction costs** ([link](https://doi.org/10.1016/j.eneco.2022.105974))\
Michał Narajewski and F. Ziel\
*Energy Economics* · Apr 29, 2021 · 26 citations

> This paper addresses the question of how much to bid to maximize the profit when trading in two electricity markets: the hourly Day-Ahead Auction and the quarter-hourly Intraday Auction. For optimal coordinated bidding many price scenarios are examined, the own non-linear market impact is estimated by considering empirical supply and demand curves, and a number of trading strategies is used. Additionally, we provide theoretical results for risk neutral agents. The application study is conducted using the German market data, but the presented methods can be easily utilized with other two consecutive auctions. This paper contributes to the existing literature by evaluating the costs of electricity trading, i.e. the price impact and the transaction costs. The empirical results for the German EPEX market show that it is far more profitable to minimize the price impact rather than maximize the arbitrage.

------------------------------------------------------------------------

4\. · 100% match · 2018 · 2.3 cit/yr\
**German Intraday Electricity Market Analysis and Modeling Based on the Limit Order Book** ([link](https://doi.org/10.1109/EEM.2018.8469829))\
Henry Martin and Scott Otterson\
*2018 15th International Conference on the European Energy Market (EEM)* · Jun 1, 2018 · 18 citations

> This paper presents a market model for the EPEX SPOT German continuous intraday market for electric power trading based on the limit order book (LOB). We use the EPEX SPOT M7 order book data, which contains all orders submitted to the German continuous intraday market, to simulate the historic course of the market. Thereby, we reconstruct the complete state of the LOB at every point in (trading) time. We validate our simulation by comparing the transactions that our simulation generated with the actual historical transactions available from a different data set. The LOB based market model can be used to include price volatility risk and illiquidity risk when simulating trading at the EPEX SPOT continuous intraday market. Furthermore, we present all preprocessing steps and decision rules necessary to correctly identify orders from the often ambiguous EPEX SPOT M7 order book data.

------------------------------------------------------------------------

5\. · 100% match · 2021\
**High-frequency Electricity Trading: Empirics, Fundamentals, and Stochastics** ([link](https://doi.org/10.17185/DUEPUBLICO/74512))\
Marcel Kremer\
Jul 2, 2021 · 0 citations

> In the wake of the continuous digital transformation and the rapid increase in the amount of available data, trading on financial markets takes place at ever higher frequencies. This development does not only concern classical financial markets but also the comparatively young electricity markets. Apart from the massive expansion of renewable energy sources, increasing demand-side flexibility and increasing storage capabilities, high-frequency trading is one of the major trends shaping the electricity markets of the future. This thesis explores high-frequency trading on two German electricity markets: the intraday electricity market and the electricity futures market. The first part of this thesis develops an econometric price model with fundamental impacts for intraday electricity markets of 15-minute contracts. We analyze a unique data set of high-frequency transaction data, fundamental supply and demand data, and intradaily updated forecasts of renewable power generation. Our empirical analysis shows that, on average, prices of 15-minute contracts exhibit a sawtooth-shaped and trading volumes a U-shaped hourly seasonality. Furthermore, market liquidity increases sharply within the last trading hour before gate closure. We calibrate our econometric model for morning, noon, evening, and night contracts and use a threshold regression technique to examine how 15-minute intraday trading depends on the slope of the merit order curve. Our estimation results reveal strong evidence of mean reversion in the price formation mechanism of 15-minute contracts. Additionally, prices of neighboring contracts exhibit strong explanatory power and a positive impact on prices of a given contract. These findings are independent of the time of day and thus generic features of the price formation process on the intraday market. In contrast, intraday auction prices have higher explanatory power for the pricing of night contracts than day contracts. We observe an asymmetric effect of renewable forecast changes on intraday prices depending on the slope of the merit order curve. In general, renewable forecasts have a higher explanatory power at noon and at night than in the morning and evening, but price information is the main driver of 15-minute intraday trading at all times of day. Overall, we show that the importance of influencing factors on the intraday electricity market has changed from fundamental towards trading-related factors. This novel finding illustrates that the intraday electricity market has become increasingly mature. The second part of this thesis conducts an empirical analysis of volatility and liquidity on electricity futures markets. We investigate high-frequency quote data of electricity month futures contracts, which are fundamental building blocks of power derivatives markets. We estimate volatility and liquidity by several measures from the scientific literature and particularly acknowledge that financial high-frequency data are not equally spaced in time. Empirical evidence suggests that volatility of electricity futures decreases as time approaches maturity, while coincidently liquidity increases. In contrast to previous research, we reveal a novel reciprocal relationship between volatility and liquidity on electricity markets. Established continuous-time stochastic models for electricity futures prices involve a growing volatility function in time and are thus not able to capture our empirical findings a priori. In Monte Carlo simulations, we demonstrate that increasing liquidity dominates the models’ volatility function and gives rise to a decreasing volatility evolution. Therefore, including liquidity is key to model the volatility of electricity futures. Overall, this thesis delivers a comprehensive picture of high-frequency trading mechanisms on electricity markets and thereby contributes to a better understanding of one of the most important trends in the electricity sector.

------------------------------------------------------------------------

6\. · 100% match · 2021 · 5.9 cit/yr\
**An econometric model for intraday electricity trading** ([link](https://doi.org/10.1098/rsta.2019.0624))\
Marcel Kremer, Ruediger Kiesel, and Florentina Paraschiv\
*Philosophical Transactions of the Royal Society A* · Jun 7, 2021 · 29 citations

> This paper develops an econometric price model with fundamental impacts for intraday electricity markets of 15-min contracts. A unique dataset of intradaily updated forecasts of renewable power generation is analysed. We use a threshold regression model to examine how 15-min intraday trading depends on the slope of the merit order curve. Our estimation results reveal strong evidence of mean reversion in the price formation mechanism of 15-min contracts. Additionally, prices of neighbouring contracts exhibit strong explanatory power and a positive impact on prices of a given contract. We observe an asymmetric effect of renewable forecast changes on intraday prices depending on the merit-order-curve slope. In general, renewable forecasts have a higher explanatory power at noon than in the morning and evening, but price information is the main driver of 15-min intraday trading. This article is part of the theme issue ‘The mathematics of energy systems’.

------------------------------------------------------------------------

7\. · 100% match · 2021 · 2.7 cit/yr\
**Liquidity costs on intraday power markets: Continuous trading versus auctions** ([link](https://doi.org/10.1016/J.ENPOL.2021.112299))\
Thomas Kuppelwieser and D. Wozabal\
*Energy Policy* · Jul 1, 2021 · 13 citations

> Abstract We analyze liquidity costs on continuous and auction-based intraday power markets using a cost-of-round-trip measure that works for both market designs. We use data from the Italian auction-based intraday market and the German continuous market and present descriptive statistics as well as multivariate regression models to analyze determinants of liquidity costs in both markets. To test for differences in liquidity due to market design, we employ a double machine learning technique controlling for several confounding variables. We show that weekly patterns, yearly seasonality, electricity demand, as well as the influence of temperatures significantly affect liquidity costs. Comparing liquidity costs in both market, we find that, overall, liquidity costs are lower on the Italian market. However, Italian costs increase towards later auctions, while the costs on the German continuous intraday market decrease and reach their low close to physical delivery, where costs are lower than on the last Italian market trading the corresponding products.

------------------------------------------------------------------------

8\. · 100% match · 2020 · 6.7 cit/yr\
**Price formation and optimal trading in intraday electricity markets** ([link](https://doi.org/10.1007/s11579-021-00307-z))\
Olivier F’eron, P. Tankov, and L. Tinsi\
*Mathematics and Financial Economics* · Sep 10, 2020 · 38 citations

> We develop a tractable equilibrium model for price formation in intraday electricity markets in the presence of intermittent renewable generation. Using stochastic control theory, we identify the optimal strategies of agents with market impact and exhibit the Nash equilibrium in closed form for a finite number of agents as well as in the asymptotic framework of mean field games. Our model reproduces the empirical features of intraday market prices, such as increasing price volatility at the approach of the delivery date and the correlation between price and renewable infeed forecasts, and relates these features with market characteristics like liquidity, number of agents, and imbalance penalty.

------------------------------------------------------------------------

9\. · 100% match · 2017 · 19 cit/yr\
**Econometric Analysis of 15-Minute Intraday Electricity Prices** ([link](https://doi.org/10.1016/J.ENECO.2017.03.002))\
Ruediger Kiesel and Florentina Paraschiv\
*Energy Economics* · May 1, 2017 · 169 citations

> The trading activity in the German intraday electricity market has increased significantly over the last years. This is partially due to an increasing share of renewable energy, wind and photovoltaic, which requires power generators to balance out the forecasting errors in their production. We investigate the bidding behavior in the intraday market by looking at both last prices and continuous bidding, in the context of a fundamental model. A unique data set of 15-minute intraday prices and intraday-updated forecasts of wind and photovoltaic has been employed and price bids are modelled by prior information on fundamentals. We show that intraday prices adjust asymmetrically to both forecasting errors in renewables and to the volume of trades dependent on the threshold variable demand quote, which reflects the expected demand covered by the planned traditional capacity in the day-ahead market. The location of the threshold can be used by market participants to adjust their bids accordingly, given the latest updates in the wind and photovoltaic forecasting errors and the forecasts of the control area balances.

------------------------------------------------------------------------

10\. · 100% match · 2019 · 4.0 cit/yr\
**Modeling Intraday Markets under the New Advances of the Cross-Border Intraday Project (XBID): Evidence from the German Intraday Market** ([link](https://doi.org/10.3390/en12224339))\
Christopher Kath\
*Energies* · Nov 14, 2019 · 26 citations

> The intraday cross-border project (XBID) allows intraday market participants to trade based on a shared order book independent of countries or local energy exchanges. This theoretically leads to an efficient allocation of cross-border capacities and ensures maximum market liquidity across European intraday markets. If this postulation holds, the technical implementation of XBID might mark a regime switch in any intraday price series. We present a regression-based model for intraday markets with a particular focus on the German European Power Exchange (EPEX) intraday market and evaluate if the introduction of XBID influence prices, volume or volatility. We analyze partial volume-weighted average prices and standard deviations as well as cross-border volumes at different trading times. We are able to falsify our initial hypothesis assuming a measurable influence of changes caused by XBID. Thus, this paper contributes to the ongoing discussion on appropriate modeling of intraday markets and demonstrates that XBID does not necessarily need to be included in any model.

------------------------------------------------------------------------

11\. · 100% match · 2015 · 5.3 cit/yr\
**An optimal trading problem in intraday electricity markets** ([link](https://doi.org/10.1007/s11579-015-0150-8))\
R. Aïd, P. Gruet, and H. Pham\
*Mathematics and Financial Economics* · Jan 19, 2015 · 60 citations

> We consider the problem of optimal trading for a power producer in the context of intraday electricity markets. The aim is to minimize the imbalance cost induced by the random residual demand in electricity, i.e. the consumption from the clients minus the production from renewable energy. For a simple linear price impact model and a quadratic criterion, we explicitly obtain approximate optimal strategies in the intraday market and thermal power generation, and exhibit some remarkable properties of the trading rate. Furthermore, we study the case when there are jumps on the demand forecast and on the intraday price, typically due to error in the prediction of wind power generation. Finally, we solve the problem when taking into account delay constraints in thermal power production.

------------------------------------------------------------------------

12\. · 100% match · 2025\
**Optimal execution in intraday energy markets under Hawkes processes with transient impact** ([link](https://doi.org/10.1080/14697688.2025.2597415))\
Konstantinos Chatziandreou and Sven Karbach\
*Quantitative Finance* · Apr 14, 2025 · 0 citations

> This paper investigates optimal execution strategies in intraday energy markets through a mutually exciting Hawkes process model. Calibrated to data from the German intraday electricity market, the model effectively captures key empirical features, including intra-session volatility, distinct intraday market activity patterns, and the Samuelson effect as gate closure approaches. By integrating a transient price impact model with a bivariate Hawkes process to model the market order flow, we derive an optimal trading trajectory for energy companies managing large volumes, accounting for the specific trading patterns of these markets. A back-testing analysis compares the proposed strategy against standard benchmarks such as Time-Weighted Average Price (TWAP) and Volume-Weighted Average Price (VWAP), demonstrating substantial cost reductions across various hourly trading products in intraday energy markets.

------------------------------------------------------------------------

13\. · 100% match · 2022 · 1.0 cit/yr\
**An Empirical Analysis of the Bid-ask Spread in the Continuous Intraday Trading of the German Power Market** ([link](https://doi.org/10.5547/01956574.43.3.cbal))\
Clara Balardy\
*The Energy Journal* · May 1, 2022 · 4 citations

------------------------------------------------------------------------

14\. · 100% match · 2022 · 4.1 cit/yr\
**Simulation-based Forecasting for Intraday Power Markets: Modelling Fundamental Drivers for Location, Shape and Scale of the Price Distribution** ([link](https://doi.org/10.5547/01956574.45.3.shir))\
Simon Hirsch and F. Ziel\
*The Energy Journal* · Nov 23, 2022 · 14 citations

> During the last years, European intraday power markets have gained importance for balancing forecast errors due to the rising volumes of intermittent renewable generation. However, compared to day-ahead markets, the drivers for the intraday price process are still sparsely researched. In this paper, we propose a modelling strategy for the location, shape and scale parameters of the return distribution in intraday markets, based on fundamental variables. We consider wind and solar forecasts and their intraday updates, outages, price information and a novel measure for the shape of the merit-order, derived from spot auction curves as explanatory variables. We validate our modelling by simulating price paths and compare the probabilistic forecasting performance of our model to benchmark models in a forecasting study for the German market. The approach yields significant improvements in the forecasting performance, especially in the tails of the distribution. At the same time, we are able to derive the contribution of the driving variables. We find that, apart from the first lag of the price changes, none of our fundamental variables have explanatory power for the expected value of the intraday returns. This implies weak-form market efficiency as renewable forecast changes and outage information seems to be priced in by the market. We find that the volatility is driven by the merit-order regime, the time to delivery and the closure of cross-border order books. The tail of the distribution is mainly influenced by past price differences and trading activity. Our approach is directly transferable to other continuous intraday markets in Europe.

------------------------------------------------------------------------

15\. · 100% match · 2020 · 9.5 cit/yr\
**Ensemble Forecasting for Intraday Electricity Prices: Simulating Trajectories** ([link](https://doi.org/10.1016/J.APENERGY.2020.115801))\
Michał Narajewski and F. Ziel\
*ArXiv* · May 4, 2020 · 57 citations

> Abstract Recent studies concerning the point electricity price forecasting have shown evidence that the hourly German Intraday Continuous Market is weak-form efficient. Therefore, we take a novel, advanced approach to the problem. A probabilistic forecasting of the hourly intraday electricity prices is performed by simulating trajectories in every trading window to receive a realistic ensemble to allow for more efficient intraday trading and redispatch. A generalized additive model is fitted to the price differences with the assumption that they follow a zero-inflated distribution, precisely a mixture of the Dirac and the Student’s t-distributions. Moreover, the mixing term is estimated using a high-dimensional logistic regression with lasso penalty. We model the expected value and volatility of the series using i.a. autoregressive and no-trade effects or load, wind and solar generation forecasts and accounting for the non-linearities in e.g. time to maturity. Both the in-sample characteristics and forecasting performance are analysed using a rolling window forecasting study. Multiple versions of the model are compared to several benchmark models and evaluated using probabilistic forecasting measures and significance tests. The study aims to forecast the price distribution in the German Intraday Continuous Market in the last 3 h of trading, but the approach allows for application to other continuous markets, especially in Europe. The results prove superiority of the mixture model over the benchmarks gaining the most from the modelling of the volatility. They also indicate that the introduction of XBID reduced the market volatility.

------------------------------------------------------------------------

16\. · 100% match · 2020 · 0.2 cit/yr\
**REMIT: ten years and counting** ([link](https://doi.org/10.1080/17521440.2020.1805870))\
L. Hiemstra\
*Law and Financial Markets Review* · Sep 21, 2020 · 1 citations

> Trading in energy derivatives is subjected to a fragmented regulatory framework which is largely designed for capital markets. Since 2011, a tailor made regime for the energy sector is in place; REMIT. Market participants need to find their way in this diverse set of obligations and prohibitions. This article describes the regulatory paradigm to which market participants need to adhere and the practical impact on trading in energy derivatives. Data reporting obligations, position limits and the prohibition on insider trading, market manipulation and the disclosure of inside information are discussed in more detail. The article concludes that REMIT fills in a regulatory gap, but its existence is not necessarily inevitable to capture energy derivative trading under a supervisory regime which is adapted to the specifics of energy markets.

------------------------------------------------------------------------

17\. · 100% match · 2022 · 5.4 cit/yr\
**Trading on short-term path forecasts of intraday electricity prices** ([link](https://doi.org/10.1016/j.eneco.2022.106125))\
Tomasz Serafin, Grzegorz Marcjasz, and R. Weron\
*Energy Economics* · Jun 1, 2022 · 21 citations

> We propose a novel electricity price forecasting model tailored to intraday markets with continuous trading. It is based on distributional deep neural networks with Johnson SU distributed outputs. To demonstrate its usefulness, we introduce a realistic trading strategy for the economic evaluation of ensemble forecasts. Our approach takes into account forecast errors in wind generation for four German TSOs and uses the intraday market to resolve imbalances remaining after day-ahead bidding. We argue that the economic evaluation is crucial and provide evidence that the better performing methods in terms of statistical error metrics do not necessarily lead to higher trading profits.

------------------------------------------------------------------------

18\. · 100% match · 2024 · 6.1 cit/yr\
**Bayesian Hierarchical Probabilistic Forecasting of Intraday Electricity Prices** ([link](https://doi.org/10.1016/j.apenergy.2024.124975))\
Daniel Nickelsen and Gernot Müller\
*ArXiv* · Mar 8, 2024 · 13 citations

> We address the need for forecasting methodologies that handle large uncertainties in electricity prices for continuous intraday markets by incorporating parameter uncertainty and using a broad set of covariables. This study presents the first Bayesian forecasting of electricity prices traded on the German intraday market. Endogenous and exogenous covariables are handled via Orthogonal Matching Pursuit (OMP) and regularising priors. The target variable is the IDFull price index, with forecasts given as posterior predictive distributions. Validation uses the highly volatile 2022 electricity prices, which have seldom been studied. As a benchmark, we use all intraday transactions at the time of forecast to compute a live IDFull value. According to market efficiency, it should not be possible to improve on this last-price benchmark. However, we observe significant improvements in point measures and probability scores, including an average reduction of $`5.9\,\%`$ in absolute errors and an average increase of $`1.7\,\%`$ in accuracy when forecasting whether the IDFull exceeds the day-ahead price. Finally, we challenge the use of LASSO in electricity price forecasting, showing that OMP results in superior performance, specifically an average reduction of $`22.7\,\%`$ in absolute error and $`20.2\,\%`$ in the continuous ranked probability score.

------------------------------------------------------------------------

19\. · 100% match · 2020 · 3.7 cit/yr\
**Intraday renewable electricity trading: advanced modeling and numerical optimal control** ([link](https://doi.org/10.1186/s13362-020-0071-x))\
S. Glas et al.\
*Journal of Mathematics in Industry* · Feb 4, 2020 · 23 citations

> As an extension of (Progress in industrial mathematics at ECMI 2018, pp. 469–475, 2019 ), this paper is concerned with a new mathematical model for intraday electricity trading involving both renewable and conventional generation. The model allows to incorporate market data e.g. for half-spread and immediate price impact. The optimal trading and generation strategy of an agent is derived as the viscosity solution of a second-order Hamilton–Jacobi–Bellman (HJB) equation for which no closed-form solution can be given. We construct a numerical approximation allowing us to use continuous input data. Numerical results for a portfolio consisting of three conventional units and wind power are provided.

------------------------------------------------------------------------

20\. · 100% match · 2016 · 7.3 cit/yr\
**Trading behaviour on the continuous intraday market Elbas** ([link](https://doi.org/10.1016/J.ENPOL.2015.10.045))\
Richard Scharff and M. Amelin\
*Energy Policy* · 75 citations

------------------------------------------------------------------------

21\. · 100% match · 2019 · 6.5 cit/yr\
**Forecasting the Price Distribution of Continuous Intraday Electricity Trading** ([link](https://doi.org/10.3390/en12224262))\
Tim Janke and Florian Steinke\
*Energies* · Nov 8, 2019 · 42 citations

> The forecasting literature on intraday electricity markets is scarce and restricted to the analysis of volume-weighted average prices. These only admit a highly aggregated representation of the market. Instead, we propose to forecast the entire volume-weighted price distribution. We approximate this distribution in a non-parametric way using a dense grid of quantiles. We conduct a forecasting study on data from the German intraday market and aim to forecast the quantiles for the last three hours before delivery. We compare the performance of several linear regression models and an ensemble of neural networks to several well designed naive benchmarks. The forecasts only improve marginally over the naive benchmarks for the central quantiles of the distribution which is in line with the latest empirical results in the literature. However, we are able to significantly outperform all benchmarks for the tails of the price distribution.

------------------------------------------------------------------------

22\. · 100% match · 2022 · 8.1 cit/yr\
**Probabilistic Forecasting of German Electricity Imbalance Prices** ([link](https://doi.org/10.3390/en15144976))\
Michał Narajewski\
*Energies* · May 23, 2022 · 32 citations

> The imbalance market is very volatile and often exhibits extreme price spikes. This makes it very hard to model; however, if predicted correctly, one could make significant gains by participating on the right side of the market. In this manuscript, we conduct a very short-term probabilistic forecasting of imbalance prices, contributing to the scarce literature in this novel subject. The forecasting is performed 30 min before the delivery, so that the trader might still choose the trading place. The distribution of the imbalance prices is modelled and forecasted using methods well-known in the electricity price forecasting literature: lasso with bootstrap, gamlss, and probabilistic neural networks. The methods are compared with a naive benchmark in a meaningful rolling window study. The results provide evidence of the efficiency between the intraday and balancing markets as the sophisticated methods do not substantially overperform the intraday continuous price index. On the other hand, they significantly improve the empirical coverage. Therefore, the traders should avoid participating in the balancing market, which is inline with the objective and current regulations of the market. The analysis was conducted on the German market; however, it could be easily applied to any other market of a similar structure.

------------------------------------------------------------------------

23\. · 100% match · 2023 · 4.2 cit/yr\
**Multivariate simulation‐based forecasting for intraday power markets: Modeling cross‐product price effects** ([link](https://doi.org/10.1002/asmb.2837))\
Simon Hirsch and F. Ziel\
*Applied Stochastic Models in Business and Industry* · Jun 23, 2023 · 12 citations

> Intraday electricity markets play an increasingly important role in balancing the intermittent generation of renewable energy resources, which creates a need for accurate probabilistic price forecasts. However, research to date has focused on univariate approaches, while in many European intraday electricity markets all delivery periods are traded in parallel. Thus, the dependency structure between different traded products and the corresponding cross‐product effects cannot be ignored. We aim to fill this gap in the literature by using copulas to model the high‐dimensional intraday price return vector. We model the marginal distribution as a zero‐inflated Johnson’s distribution with location, scale, and shape parameters that depend on market and fundamental data. The dependence structure is modeled using copulas, accounting for the particular market structure of the intraday electricity market, such as overlapping but independent trading sessions for different delivery days and allowing the dependence parameter to be time‐varying. We validate our approach in a simulation study for the German intraday electricity market and find that modeling the dependence structure improves the forecasting performance. Additionally, we shed light on the impact of the single intraday coupling on the trading activity and price distribution and interpret our results in light of the market efficiency hypothesis. The approach is directly applicable to other European electricity markets.

------------------------------------------------------------------------

24\. · 100% match · 2020 · 0.3 cit/yr\
**Working Paper \#35 AN EMPIRICAL ANALYSIS OF THE BID-ASK SPREAD IN THE CONTINUOUS INTRADAY TRADING OF THE GERMAN POWER MARKET** ([link](https://www.semanticscholar.org/paper/b16485f5260a39fd249817ee81a3dc5599dc32a4))\
Clara Balardy\
2 citations

> Liquidity is decisive for a well-functioning market. As most of the literature on the subject is based on financial markets, the extrapolation of its insights to the power market is fragile. This paper shows the specificities of the liquidity of the German power market. Using the bid-ask spread as a proxy, thanks to the detailed order book for the hourly contracts, I first describe the evolution of the liquidity over the trading session. The bid-ask spread has a ”L-shaped” pattern over it. Second, I identify the four main drivers of the liquidity using the bid-ask spread as a proxy: the risk, the adjustments’ need, the activity and the concentration of the market. I find that an increase of the volatility or the market concentration increases the bid-ask spread while an increase of the adjustments’ need or the market activity decreases it.

------------------------------------------------------------------------

25\. · 100% match · 2018 · 13 cit/yr\
**Econometric modelling and forecasting of intraday electricity prices** ([link](https://doi.org/10.1016/j.jcomm.2019.100107))\
Michał Narajewski and F. Ziel\
*Journal of Commodity Markets* · Dec 21, 2018 · 95 citations

> In the following paper we analyse the ID$`_3`$-Price on German Intraday Continuous Electricity Market using an econometric time series model. A multivariate approach is conducted for hourly and quarter-hourly products separately. We estimate the model using lasso and elastic net techniques and perform an out-of-sample very short-term forecasting study. The model’s performance is compared with benchmark models and is discussed in detail. Forecasting results provide new insights to the German Intraday Continuous Electricity Market regarding its efficiency and to the ID$`_3`$-Price behaviour. The supplementary materials are available online.

------------------------------------------------------------------------

26\. · 100% match · 2018 · 9.8 cit/yr\
**The value of forecasts: Quantifying the economic gains of accurate quarter-hourly electricity price forecasts** ([link](https://doi.org/10.1016/j.eneco.2018.10.005))\
Christopher Kath and F. Ziel\
*Energy Economics* · Oct 1, 2018 · 74 citations

> We propose a multivariate elastic net regression forecast model for German quarter-hourly electricity spot markets. While the literature is diverse on day-ahead prediction approaches, both the intraday continuous and intraday call-auction prices have not been studied intensively with a clear focus on predictive power. Besides electricity price forecasting, we check for the impact of early day-ahead (DA) EXAA prices on intraday forecasts. Another novelty of this paper is the complementary discussion of economic benefits. A precise estimation is worthless if it cannot be utilized. We elaborate possible trading decisions based upon our forecasting scheme and analyze their monetary effects. We find that even simple electricity trading strategies can lead to substantial economic impact if combined with a decent forecasting technique.

------------------------------------------------------------------------

27\. · 100% match · 2018 · 16 cit/yr\
**Understanding intraday electricity markets: Variable selection and very short-term price forecasting using LASSO** ([link](https://doi.org/10.1016/J.IJFORECAST.2019.02.001))\
Bartosz Uniejewski, Grzegorz Marcjasz, and R. Weron\
*International Journal of Forecasting* · Aug 31, 2018 · 120 citations

> Using a unique set of prices from the German EPEX market we take a closer look at the fine structure of intraday markets for electricity with its continuous trading for individual load periods up to 30 minutes before delivery. We apply the least absolute shrinkage and selection operator (LASSO) to gain statistically sound insights on variable selection and provide recommendations for very short-term electricity price forecasting.

------------------------------------------------------------------------

28\. · 100% match · 2025 · 2.4 cit/yr\
**OrderFusion: Encoding Orderbook for End-to-End Probabilistic Intraday Electricity Price Forecasting** ([link](https://www.semanticscholar.org/paper/251c73bde036b0c485a66844fbab2b3f90de0ffa))\
Runyao Yu et al.\
Feb 5, 2025 · 3 citations

> Probabilistic intraday electricity price forecasting is becoming increasingly important with the growth of renewable generation and the rise in demand-side engagement. Their uncertainties have increased the trading risks closer to delivery and the subsequent imbalance settlement costs. As a consequence, intraday trading has emerged to mitigate these risks. Unlike auction markets, intraday trading in many jurisdictions is characterized by the continuous posting of buy and sell orders on power exchange platforms. This dynamic orderbook microstructure of price formation presents special challenges for price forecasting. Conventional methods represent the orderbook via domain features aggregated from buy and sell trades, or by treating it as a multivariate time series, but such representations neglect the full buy-sell interaction structure of the orderbook. This research therefore develops a new order fusion methodology, which is an end-to-end and parameter-efficient probabilistic forecasting model that learns a full interaction-aware representation of the buy-sell dynamics. Furthermore, as quantile crossing is often a problem in probabilistic forecasting, this approach hierarchically estimates the quantiles with non-crossing constraints. Extensive experiments on the market price indices across high-liquidity (German) and low-liquidity (Austrian) markets demonstrate consistent improvements over conventional baselines, and ablation studies highlight the contributions of the main modeling components. The methodology is available at: https://runyao-yu.github.io/OrderFusion/.

------------------------------------------------------------------------

29\. · 100% match · 2022 · 3.3 cit/yr\
**Predicting Electricity Imbalance Prices and Volumes: Capabilities and Opportunities** ([link](https://doi.org/10.3390/en15103645))\
J. Browell and C. Gilbert\
*Energies* · May 16, 2022 · 13 citations

> Electricity imbalance pricing provides the ultimate incentive for generators and suppliers to contract with one another ahead of time and deliver against their obligations. As delivery time approaches, traders must judge whether to trade-out a position or settle it in the balancing market at the as-yet-unknown imbalance price. Forecasting the imbalance price (and related volumes) is therefore a necessity in short-term markets. However, this topic has received surprisingly little attention in the academic literature despite clear need by practitioners. Furthermore, the emergence of algorithmic trading demands automated forecasting and decision-making, with those best able to extract predictive information from available data gaining a competitive advantage. Here we present the case for developing imbalance price forecasting methods and provide motivating examples from the Great Britain’s balancing market, demonstrating forecast skill and value.

------------------------------------------------------------------------

30\. · 100% match · 2020 · 18 cit/yr\
**Optimal bidding of a virtual power plant on the Spanish day-ahead and intraday market for electricity** ([link](https://doi.org/10.1016/J.EJOR.2019.07.022))\
D. Wozabal and Gunther Rameseder\
*Eur. J. Oper. Res.* · Jan 1, 2020 · 116 citations

> Abstract We develop a multi-stage stochastic programming approach to optimize the bidding strategy of a virtual power plant (VPP) operating on the Spanish spot market for electricity. The VPP markets electricity produced in the wind parks it manages on the day-ahead market and on six staggered auction-based intraday markets. Uncertainty enters the problem via stochastic electricity prices as well as uncertain wind energy production. We set up the problem of bidding for one day of operation as a Markov decision process (MDP) that is solved using a variant of the stochastic dual dynamic programming algorithm. We conduct an extensive out-of-sample comparison demonstrating that the optimal policy obtained by the stochastic program clearly outperforms deterministic planning, a pure day-ahead strategy, a benchmark that only uses the day-ahead market and the first intraday market, as well as a proprietary stochastic programming approach developed in the industry. Furthermore, we study the effect of risk aversion as modeled by the nested Conditional Value-at-Risk as well as the impact of changes in various problem parameters.

------------------------------------------------------------------------

31\. · 100% match · 2020\
**Energy Trading and Its Multiplicity of Supervisors: Effectiveness of Fragmented Supervision and Information Sharing in View of Reporting Obligations for Energy Trading Companies** ([link](https://doi.org/10.2139/ssrn.3715737))\
L. Hiemstra\
*Social Science Research Network* · Jul 31, 2020 · 0 citations

> Energy companies trading in derivatives which have a value based on an energy product ( “Energy Trading”) are subjected to a fragmented regulatory framework. They are supervised by a multitude of authorities on a national and European level. These authorities cooperate horizontally (between EU agencies or between national regulatory authorities) or vertically – between EU agencies and NRA’s) and in a formal and informal way. They share information on Energy Trading to detect market abuse. This article aims to provide insight in the effectiveness of supervisory activities within the Energy Trading landscape. In doing so, the obligation for energy companies to report fundamental data on the derivatives they trade in, is used for illustrative purposes and explained in light of the European Market Infrastructure Regulation (‘EMIR’), the Markets in Financial Instruments Directive and Regulation (‘MiFID II and MiFIR’) and the regulation on wholesale energy market integrity and transparency (‘REMIT’). The article finishes with a conclusion which advocates the necessity of information sharing and professional secrecy in the current regulatory landscape and intends to contribute to a discussion on the effectiveness of information sharing within an international context.

------------------------------------------------------------------------

32\. · 100% match · 2020 · 9.7 cit/yr\
**Very-Short-Term Probabilistic Forecasting for a Risk-Aware Participation in the Single Price Imbalance Settlement** ([link](https://doi.org/10.1109/TPWRS.2019.2940756))\
J. Bottieau, L. Hubert, Z. De Grève, F. Vallée, and J. Toubeau\
*IEEE Transactions on Power Systems* · Mar 1, 2020 · 60 citations

> The single imbalance pricing is an emerging mechanism in European electricity markets where all positive and negative imbalances are settled at a unique price. This real-time scheme thereby stimulates market participants to deviate from their schedule to restore the power system balance. However, exploiting this market opportunity is very risky due to the extreme volatility of the real-time power system conditions. In order to address this issue, we implement a new tailored deep-learning model, named encoder-decoder, to generate improved probabilistic forecasts of the imbalance signal, by efficiently capturing its complex spatio-temporal dynamics. The predicted distributions are then used to quantify and optimize the risk associated with the real-time participation of market players, acting as price-makers, in the imbalance settlement. This leads to an integrated forecast-driven strategy, modeled as a robust bi-level optimization. Results show that our probabilistic forecaster achieves better performance than other state of the art tools, and that the subsequent risk-aware robust dispatch tool allows finding a tradeoff between conservative and risk-seeking policies, leading to improved economic benefits. Moreover, we show that the model is computationally efficient and can thus be incorporated in the very-short-term dispatch of market players with flexible resources.

------------------------------------------------------------------------

33\. · 100% match · 2016 · 11 cit/yr\
**Are fundamentals enough? Explaining price variations in the German day-ahead and intraday power market** ([link](https://doi.org/10.1016/J.ENECO.2015.12.013))\
Christian Pape, S. Hagemann, and C. Weber\
*Energy Economics* · Feb 1, 2016 · 117 citations

------------------------------------------------------------------------

34\. · 100% match · 2024 · 1.3 cit/yr\
**Simulating and analyzing a sparse order book: an application to intraday electricity markets** ([link](https://doi.org/10.1080/14697688.2025.2568693))\
Philippe Bergault and Enzo Cogn’eville\
*Quantitative Finance* · Oct 9, 2024 · 2 citations

> This paper presents a novel model for simulating and analyzing sparse limit order books (LOBs), with a specific application to the European intraday electricity market. In illiquid markets, characterized by significant gaps between order levels due to sparse trading volumes, traditional LOB models often fall short. Our approach utilizes an inhomogeneous Poisson process to accurately capture the sporadic nature of order arrivals and cancellations on both the bid and ask sides of the book. By applying this model to the intraday electricity market, we gain insights into the unique microstructural behaviors and challenges of this dynamic trading environment. The results offer valuable implications for market participants, enhancing their understanding of LOB dynamics in illiquid markets. This work contributes to the broader field of market microstructure by providing a robust framework adaptable to various illiquid market settings beyond electricity trading.

------------------------------------------------------------------------

35\. · 100% match · 2025 · 5.6 cit/yr\
**Orderbook Feature Learning and Asymmetric Generalization in Intraday Electricity Markets** ([link](https://www.semanticscholar.org/paper/7d143ebfcbdb406fd4e643ee4c89b4218f7a4420))\
Runyao Yu, Ruochen Wu, Yongsheng Han, and Jochen L. Cremer\
Oct 14, 2025 · 3 citations

> Accurate probabilistic forecasting of intraday electricity prices is critical for market participants to inform trading decisions. Existing studies rely on specific domain features, such as Volume-Weighted Average Price (VWAP) and the last price. However, the rich information in the orderbook remains underexplored. Furthermore, these approaches are often developed within a single country and product type, making it unclear whether the approaches are generalizable. In this paper, we extract 384 features from the orderbook and identify a set of powerful features via feature selection. Based on selected features, we present a comprehensive benchmark using classical statistical models, tree-based ensembles, and deep learning models across two countries (Germany and Austria) and two product types (60-min and 15-min). We further perform a systematic generalization study across countries and product types, from which we reveal an asymmetric generalization phenomenon: models trained on more liquid markets or products transfer well to less liquid ones, whereas the reverse transfer leads to substantial performance degradation.

------------------------------------------------------------------------

36\. · 100% match · 2021 · 1.8 cit/yr\
**Intraday imbalance optimization: incentives and impact of strategic intraday bidding behavior** ([link](https://doi.org/10.1007/s12667-021-00445-9))\
C. Koch\
*Energy Systems* · May 10, 2021 · 9 citations

> Intraday markets are crucial to balance supply and demand in the very short-term, up to delivery. They are often designed as continuous auctions with a pay-as-bid pricing mechanism. While several studies assess trading strategies to balance different types of portfolios, they normally do not consider the incentives of the imbalance prices for portfolio management. This paper analyzes a strategy of taking positions in the German intraday market based on expected imbalance prices and examines its impact on system stability. Using a logistic regression model, it is possible to accurately predict the direction of the overall system balance and to apply a profitable trading strategy. For a period from 01/07/2017 to 30/06/2019, the strategy outperforms a simple approach by EUR 47 000 per MW. However, this behavior would predominantly not have been system supportive due to biased imbalance price incentives. These are asymmetric price spreads and insufficiently low imbalance prices compared to intraday prices. An efficient intraday price constraint would partly solve the problem. The overall share of system supportive imbalance positions would raise by ten percentage points. In situations with high system wide imbalances, up to three-quarters of the positions would stabilize the system. These findings are important for regulation in Germany and other countries with a single imbalance pricing as they provide an indication for crucial points of the imbalance pricing rules to incite appropriate market behavior.

------------------------------------------------------------------------

37\. · 100% match · 2017 · 1.0 cit/yr\
**Optimal market maker pricing in the German intraday power market** ([link](https://www.semanticscholar.org/paper/31ade0f4d8394d543349730896a4f9999eebd0f1))\
N. V. Luckner, Á. Cartea, S. Jaimungal, and R. Kiesel\
9 citations

> Considering exchange-based trading of power supply contracts with delivery in Germany there exist both a futures and a spot market. The main German spot market is operated by EPEX SPOT SE and comprises trading of both power supply contracts with hourly and quarter hourly delivery. For contracts with hourly delivery the spot market comprises a day-ahead auction with submission deadline at 12.00 noon on the day before the delivery day and continuous trading which opens at 3.00 pm on the day before the delivery day and closes 30 minutes before delivery start. For contracts with quarter hourly delivery similar markets are in place. In the following, the markets involving continuous trading of power supply contracts with delivery in Germany are commonly referred to as the German intraday power market. They are mainly used in order to balance forecast errors which evolve after the submission deadlines for the day-ahead auctions, see e.g. Weber (2010). Participants in the German intraday power market have the choice between three types of orders, i.e. regular orders, iceberg orders and over-the-counter (OTC) orders. Iceberg orders are large-volume orders which are split into several orders with smaller volume and placed into the market sequentially. In case of OTC orders the trader needs to specify the receiving balancing group. OTC orders are not considered further in the following.

------------------------------------------------------------------------

38\. · 100% match · 2020 · 7.4 cit/yr\
**Beating the Naïve—Combining LASSO with Naïve Intraday Electricity Price Forecasts** ([link](https://doi.org/10.3390/EN13071667))\
Grzegorz Marcjasz, Bartosz Uniejewski, and R. Weron\
*Energies* · Apr 3, 2020 · 45 citations

> In the last three decades the vast majority of electricity price forecasting (EPF) research has concerned day-ahead markets. However, the rapid expansion of renewable generation—mostly wind and solar—have shifted the focus to intraday markets, which can be used to balance the deviations between positions taken in the day-ahead market and the actual demand and renewable generation. A recent EPF study claims that the German intraday, continuous-time market for hourly products is weak-form efficient, that is, that the best predictor for the so-called ID3-Price index is the most recent transaction price. Here, we undermine this claim and show that we can beat the naïve forecast by combining it with a prediction of a parameter-rich model estimated using the least absolute shrinkage and selection operator (LASSO). We further argue, that that if augmented with timely predictions of fundamental variables for the coming hours, the LASSO-estimated model itself can significantly outperform the naïve forecast.

------------------------------------------------------------------------

39\. · 100% match · 2024 · 0.9 cit/yr\
**Optimal intraday power trading for single-price balancing markets: An adaptive risk-averse strategy using mixture models** ([link](https://doi.org/10.1016/j.apenergy.2025.125754))\
Robin Bruneel, Mathijs Schuurmans, and Panagiotis Patrinos\
*Applied Energy* · Feb 2, 2024 · 2 citations

> Efficient markets are characterised by profit-driven participants continuously refining their positions towards the latest insights. Margins for profit generation are generally small, shaping a difficult landscape for automated trading strategies. This paper introduces a novel intraday power trading strategy tailored for single-price balancing markets. The strategy relies on a strategically devised mixture model to forecast future system imbalance prices and is formulated as a stochastic optimization problem with decision-dependent distributions to address two primary challenges: (i) the impact of trading positions on the system imbalance price and (ii) the uncertainty inherent in the model. The first challenge is tackled by adjusting the model to account for price changes after taking a position. For the second challenge, a coherent risk measure is added to the cost function to take additional uncertainties into account. This paper introduces a methodology to select the tuning parameter of this risk measure adaptively by continuously quantifying the performance of the strategy on a window of recently observed data. The strategy is validated with a simulation on the Belgian electricity market using real-time market data. The adaptive tuning approach leads to higher absolute profits, while also reducing the number of trades.

------------------------------------------------------------------------

40\. · 100% match · 2021\
**Optimal Trading of a Fixed Quantity of Power in an Illiquid Continuous Intraday Market** ([link](https://doi.org/10.1109/PowerTech46648.2021.9494885))\
Gilles Bertrand and A. Papavasiliou\
*2021 IEEE Madrid PowerTech* · Jun 28, 2021 · 0 citations

> The recent integration of renewable resources in electricity markets has increased the need for producers to correct their trading position close to real time in order to avoid volatile real-time prices. The last market to close before delivery is the Continuous Intraday Market. Therefore, this market is an interesting outlet for renewable units that aim at covering their forecast errors. As a starting point for tackling this problem, we characterize an optimal policy for trading a fixed quantity in a simplified market model. We use this analytical solution as a basis for developing an Approximate Dynamic Programming algorithm and an alternative Stochastic Dual Dynamic Programming that can trade under a more realistic set of assumptions.

------------------------------------------------------------------------

41\. · 100% match · 2019 · 4.2 cit/yr\
**The Impact of Renewable Energy Forecasts on Intraday Electricity Prices** ([link](https://doi.org/10.5547/2160-5890.10.1.skul))\
S. Kulakov and F. Ziel\
*Economics of Energy & Environmental Policy* · Mar 22, 2019 · 30 citations

> In this paper we study the impact of errors in wind and solar power forecasts on intraday electricity prices. We develop a novel econometric model which is based on day-ahead wholesale auction curves data and errors in wind and solar power forecasts. The model shifts day-ahead supply curves to calculate intraday prices. We apply our model to the German EPEX SPOT SE data. Our model outperforms both linear and non-linear benchmarks. Our study allows us to conclude that errors in renewable energy forecasts exert a non-linear impact on intraday prices. We demonstrate that additional wind and solar power capacities induce non-linear changes in the intraday price volatility. Finally, we comment on economical and policy implications of our findings.

------------------------------------------------------------------------

42\. · 100% match · 2016 · 0.9 cit/yr\
**Optimal Trading Policies for Wind Energy Producer** ([link](https://doi.org/10.1137/16M1093069))\
Zongjun Tan and P. Tankov\
*SIAM J. Financial Math.* · Sep 7, 2016 · 9 citations

> We study the optimal trading policies for a wind energy producer who aims to sell the future production in the open forward, spot, intraday and adjustment markets , and who has access to imperfect dynamically updated forecasts of the future production. We construct a stochastic model for the forecast evolution and determine the optimal trading policies which are updated dynamically as new forecast information becomes available. Our results allow to quantify the expected future gain of the wind producer and to determine the economic value of the forecasts.

------------------------------------------------------------------------

43\. · 100% match · 2020 · 4.1 cit/yr\
**The way towards European electricity intraday auctions – Status quo and future developments** ([link](https://doi.org/10.1016/j.enpol.2020.111731))\
Fabian Ocker and Vincent Jaenisch\
*Energy Policy* · Oct 1, 2020 · 23 citations

> Abstract This paper sheds light on the status quo of currently implemented electricity intraday auctions in Europe and offers an outlook for future developments. First, we compare the two market mechanisms “continuous trading” and “auction” and identify advantages and disadvantages. Then, we investigate the currently existing six intraday auctions in Europe. We compare crucial auction characteristics such as the number of auctions, tradable market period(s), gate opening time and gate closure time, and find a wide variety in auction designs. By examining relevant European regulation and recent regulatory decisions, we illustrate that future European intraday auctions can either be implemented as cross-border auctions or complementary regional auctions. We find that complementary regional auctions of the borders Portugal-Spain, CCR Greece-Italy and CCR Italy-North are already approved.

------------------------------------------------------------------------

44\. · 100% match · 2020 · 2.1 cit/yr\
**Intraday Electricity Pricing of Night Contracts** ([link](https://doi.org/10.3390/en13174501))\
Marcel Kremer, R. Kiesel, and Florentina Paraschiv\
*Energies* · Sep 1, 2020 · 12 citations

> This paper investigates the intraday electricity pricing of 15-min. contracts in night hours. We tailor a recently introduced econometric model with fundamental impacts, which is successful in describing the pricing of day contracts. Our estimation results show that the mean reversion and the positive price impact of neighboring contracts are generic features of the price formation process on the intraday market, independent of the time of day. Intraday auction prices have higher explanatory power for the pricing of night than day contracts, particularly, for the first and last 15-min. contract in a night hour. Intradaily updated forecasts of wind power infeed are the only significant fundamental factors for intraday electricity prices at night. Neither expected conventional capacities nor the slope of the merit order curve contribute to explaining price dynamics. Overall, we conclude that fundamentals lose in importance in night hours and the 15-min. intraday market is rather driven by price information.

------------------------------------------------------------------------

45\. · 100% match · 2021 · 2.5 cit/yr\
**Volatility and Dispersion of Hourly Electricity Contracts on the German Continuous Intraday Market** ([link](https://doi.org/10.3390/en14227531))\
Rainer Baule and M. Naumann\
*Energies* · Nov 11, 2021 · 11 citations

> Intraday electricity trading on the continuous intraday market of EPEX SPOT is particularly well suited for the rebalancing of energy production. We analyzed the volatility and dispersion of individual hourly contracts, taking into account the particularities of the market, due to which the standard volatility measure from financial time series cannot be applied. We used and analyzed five measures for price fluctuations, which turned out to be similarly well suited for electricity contracts, with small differences. We then identified fundamental drivers of price fluctuations: the relative share of wind in the overall mix increased dispersion. In addition, price dispersion was positively correlated with the traded volume as well as the absolute difference between the day-ahead auction price and the volume-weighted intraday price. We furthermore analyzed the timely structure of price fluctuations to identify forecast indicators for a contract’s peak trading hour before maturity, finding that trading-related variables are more important to forecast price fluctuations than fundamental factors. With lagged realizations and additional external drivers, forecast regressions reached an adjusted R2 of 0.479 for volatility and around 0.3 for the dispersion measures.

------------------------------------------------------------------------

46\. · 100% match · 2018 · 4.5 cit/yr\
**A Trading-Based Evaluation of Density Forecasts in a Real-Time Electricity Market** ([link](https://doi.org/10.3390/EN11102658))\
Derek W. Bunn, A. Gianfreda, and S. Kermer\
*Energies* · Oct 5, 2018 · 34 citations

> This paper applies a multi-factor, stochastic latent moment model to predicting the imbalance volumes in the Austrian zone of the German/Austrian electricity market. This provides a density forecast whose shape is determined by the flexible skew-t distribution, the first three moments of which are estimated as linear functions of lagged imbalance and forecast errors for load, wind and solar production. The evaluation of this density predictor is compared to an expected value obtained from OLS regression model, using the same regressors, through an out-of-sample backtest of a flexible generator seeking to optimize its imbalance positions on the intraday market. This research contributes to forecasting methodology and imbalance prediction, and most significantly it provides a case study in the evaluation of density forecasts through decision-making performance. The main finding is that the use of the density forecasts substantially increased trading profitability and reduced risk compared to the more conventional use of mean value regressions.

------------------------------------------------------------------------

47\. · 100% match · 2020 · 5.9 cit/yr\
**The flow based market coupling arrangement in Europe: Implications for traders** ([link](https://doi.org/10.1016/j.esr.2019.100444))\
T. Kristiansen\
*Energy Strategy Reviews* · 37 citations

> Abstract A new method for congestion management, flow based market coupling (FBMC), launched on May 21, 2015 in the Central Western European (CWE) region. Prior to this, no similar congestion method has been implemented elsewhere. FBMC models the electrical network, considering cross-border exchanges including security constraints. The flows span all available parallel paths as governed by the laws of physics. The objective is to optimize market flows and social welfare. FBMC allocates cross-border flows considering power transfer distribution factors (PTDFs) which describe the sensitivity of a change in import/export at a particular country. The PTDF matrix and the remaining available margin (RAM) determine the feasible transmission region at any given point in time. On a daily basis, the Capacity Auctioning Service Company (CASC) gives information about maximum bilateral exchanges, minimum and maximum net positions and PTDFs for the day-ahead market. This daily tool serves as a framework for analyzing potential congestion in the CWE region and price coupling of markets in individual hours. We explain how traders can apply the CASC tool to analyze potential congestion and identify trade opportunities. We discuss some approaches to analyze the FBMC beyond the day-ahead market.

------------------------------------------------------------------------

48\. · 100% match · 2019 · 0.8 cit/yr\
**Optimal Cross-Border Electricity Trading** ([link](https://doi.org/10.2139/ssrn.3506915))\
Á. Cartea, M. Flora, Tiziano Vargiolu, and Georgi Slavov\
*SIAM J. Financial Math.* · Dec 19, 2019 · 5 citations

> We show there exists a profitable cross-border trading strategy for an agent who trades electricity in the European electricity network. Data of the European markets are employed to show how electricity prices in all locations of the network are affected by the flow of power between any two locations that trade power between them. The optimal cross-border trading strategy is derived via the explicit solution of a non-trivial stochastic control problem in which prices at different locations are co-integrated and trading affects prices in all locations of the network.

------------------------------------------------------------------------

49\. · 100% match · 2023 · 1.5 cit/yr\
**A common shock model for multidimensional electricity intraday price modelling with application to battery valuation** ([link](https://doi.org/10.1080/14697688.2024.2395906))\
Thomas Deschatre and X. Warin\
*Quantitative Finance* · Jul 31, 2023 · 4 citations

> In this paper, we propose a multidimensional statistical model of intraday electricity prices at the scale of the trading session, which allows all products to be simulated simultaneously. This model, based on Poisson measures and inspired by the Common Shock Poisson Model, reproduces the Samuelson effect (intensity and volatility increases as time to maturity decreases). It also reproduces the price correlation structure, highlighted here in the data, which decreases as two maturities move apart. This model has only three parameters that can be estimated using a moment method that we propose here. We demonstrate the usefulness of the model on a case of storage valuation by dynamic programming over a trading session.

------------------------------------------------------------------------

50\. · 100% match · 2019 · 6.2 cit/yr\
**Integrated European intra-day electricity market: Rules, modeling and analysis** ([link](https://doi.org/10.1016/J.APENERGY.2018.12.073))\
Hong Lam Le, V. Ilea, and C. Bovo\
*Applied Energy* · Mar 15, 2019 · 44 citations

> Abstract Currently, the coupling of the European Electricity Markets has been fully achieved for the Day-Ahead Market. In the same time, a joint integrated Intra-Day Market based on the Continuous Trading mechanism is under implementation and it involves countries from West of Europe. However, some countries (e.g. Italy and Iberian countries) use the Discrete Auction mechanism and their integration implies the harmonization of the two trading mechanisms. A Hybrid Mechanism that represents the coordination of Continuous Trading and Discrete Auction has been discussed with two concrete proposals being made by Italy and Iberian countries. Thus, the aim of this paper is to propose an advanced algorithm which can simulate the clearing of the integrated European Intra-Day Market with any levels of coordination between Discrete Auction and Continuous Trading. The proposed model is formulated as a Mixed Integer Linear Problem and incorporates all market rules of both mechanisms. The algorithm is flexible enough to adapt to future changes. In addition, a case study that considers the current and near future market participants and covers an entire day of an Intra-Day Market is run by an iterative process to investigate the impact of the hybrid Intra-Day Market model on the Iberian countries and Italy according to their proposals. Moreover, the test cases represent realistic data in terms of number of variables and constraints, and in terms of complexity of the bids. The results of the paper show that, on one hand, the proposed market clearing model can be applied for different levels of Continuous Trading and Discrete Auction coordination and, on the other hand, the integration into the single European Intra-Day Market of Italy and Iberian countries can be beneficial for them. Therefore, the general conclusion is that the proposed market clearing model can be successfully used by the Power Exchanges currently integrated to solve the market or by the Power Exchanges not yet integrated to evaluate the impact of their future integration. On the other hand, the model can easily cope with any further changes in the market rules and represents a tool for future research, e.g. analysis of market participants behavior in future scenarios or evaluation of various financial instruments to manage the congestion of intra-border interconnectors.

*Showing top 50 of 185 papers. Full details available via CSV or BibTeX export.*
