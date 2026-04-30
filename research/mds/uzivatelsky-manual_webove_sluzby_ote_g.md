Uživatelská příručka
informačního systému

Uživatelský manuál
pro externí uživatele veřejného webu OTE
– webové služby

Tento  dokument  a jeho  obsah je  důvěrný.  Dokument  nesmí  být reprodukován  celý  ani  částečně, ani
ukazován  třetím  stranám  nebo  používán  k jiným účelům, než pro jaké byl  poskytnut, bez předchozího
písemného schválení společností OTE, a.s.

2025 OTE, a.s.

Revize dne:
29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

1

Datum

Popis změny

 4.8.2010

 Popis změn po redesign webových služeb

 7.9.2010

 Verze k OTE připomínkám

 29.9.2010

Finalizace připomínek

 2.12.2010

Aktualizace pro CR78

 8.5.2012

 Aktualizace pro CR160

 3.8.2016

 Aktualizace pro CR391

 9.9.2021

Aktualizace pro CR137

26.6.2023

Odstranění služeb týkajících se ukončených trhů

27.5.2024

Aktualizace služeb 15/ 60-minutové kontrakty a IDA

27.8.2024

Popis požadavku se zadání hodiny či periody

29.4.2025

Celková změna formátování dokumentu.
Rozšíření služeb pro DT 15min:
•
•
•

Nové služby: GetDamPricePeriodE, GetDamAllPeriodE, GetDamFlowsPeriodE
Úprava služby: GetDamIndexE
Omezené služby: GetDamPriceE, GetDamAllE

2025 OTE, a.s.

Revize dne:
11.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

2

Obsah

1.1
1.2
1.3

1  Webové služby ............................................................................................................................................. 3
Zpětná kompatibilita ............................................................................................................................ 3
WSDL ................................................................................................................................................... 3
Jednotlivé služby a formáty .................................................................................................................. 4
1.3.1.  Webové služby pro kmenová data ................................................................................................... 5
1.3.2.  Webové služby pro Denní trh .......................................................................................................... 7
1.3.3.  Webové služby pro Vnitrodenní aukce ......................................................................................... 19
1.3.4.  Webové služby pro Vnitrodenní trh s elektřinou........................................................................... 29
1.3.5.  Webové služby pro Odchylky – elektřina ..................................................................................... 32
1.3.6.  Webové služby pro Vnitrodenní trh s plynem ............................................................................... 38
1.3.7.  Webové služby pro Odchylky – plyn ............................................................................................ 39
Omezení vrácených hodnot při specifikování hodiny či periody ........................................................ 40
Služby se zadáním hodiny ............................................................................................................. 40
Služby se zadáním periody ............................................................................................................ 41

1.4.1
1.4.2

1.4

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

3

1  Webové služby

Webové  služby  umožňují  automatický  přístup  k některým datům  prezentovaným  na  veřejném  webu
OTE,  a.s.  Tato  technologie  je  značně  rozšířená  a  má  implementaci  v moderních  programovacích
jazycích. Pro jejich využívání je nutno mít program, který přijatá data zpracuje, uloží, případně přímo
zobrazí uživateli.

Současná  implementace  využívá  Python  aplikační  server  Zope  se  SOAP  knihovnou  SOAPpy  verze
0.11.6 se serverovým rozšířením SOAPSupport verze 0.7.2.

1.1

Zpětná kompatibilita

Služby  na  stávajícím  veřejném  webu  prošly  výrazným  redesignem  ve  sjednocení  polí  a  dalšími
změnami.  Zpětná  kompatibilita  s původním  řešením  klienta  (OTE  Win  klient  verze  1.1.2.0  a  OTE
WWW služby verze 1.1.2.0) již není podporována.

1.2

WSDL

Služba je dostupná na adrese http://www.ote-cr.cz/services/PublicDataService. WSDL je možno získat
na
http://www.ote-
požadavkem,
cr.cz/services/PublicDataService/wsdl

adrese  HTTP  GET

adrese

stejné

nebo

na

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

4

1.3

Jednotlivé služby a formáty

Všechny služby ve výstupním parametru vrací data v podobě XML dokumentu včetně jeho definice
(XSD).

Seznam webových služeb (je rozlišována velikost písmen):

•  Kmenová data

-  GetRutList

•  Denní trh

-  GetDamIndexE

Data do dne dodávky 30.9.2025:

-  GetDamPriceE

-  GetDamAllE

Data ode dne dodávky 1.10.2025 (Go-live 15 minut):

-  GetDamPricePeriodE

-  GetDamAllPeriodE

-  GetDamFlowsPeriodE

•  Vnitrodenní aukce

Data ode dne dodávky 14.6.2024 (Go-live IDA):

-  GetIDAIndexE

-  GetIDAPricePeriodE

-  GetIDAAllPeriodE

Data pouze pro dny dodávky od 14.6.2024 do 30.6.2024

-  GetIDAPriceE

-  GetIDAAllE

•  Vnitrodenní trh – elektřina

-  GetImPricePeriodE

-  GetImPriceE (služba poskytuje data pouze do dne dodávky 30.6.2024)

•  Odchylky – elektřina

-  GetImbalanceSettlementPeriodE

-  GetImbalanceSettlementE (služba poskytuje pouze data do dne dodávky 30.6.2024).

•  Vnitrodenní trh – plyn

-  GetImPriceG

•  Odchylky – plyn

-  GetImbalanceNCBALSettlementG

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

5

1.3.1.  Webové služby pro kmenová data

1.3.1.1.  GetRutList

Vrací seznam všech registrovaných účastníků trhu.

Služba je volána bez vstupních parametrů.

Výstupem je struktura s následujícími elementy:

-

Id – jednoznačný identifikátor účastníka (RÚT) v systému IS OTE

-  Ean – European article number, 13 číselný kód účastníka

-  Eic – jednoznačný identifikátor RUT prostřednictvím EIC

-  VatNo – IČ

-  Company – Název firmy

-  RegistrationDate – datum registrace (založení RÚT v systému)

-  SubjectSettlementDateElectricityFrom – datum počátku platnosti subjektu zúčtování – elektřina

-  SubjectSettlementDateEletricityTo – datum konce platnosti subjektu zúčtování – elektřina

-  SubjectSettlementDateGasFrom – datum počátku platnosti subjektu zúčtování – plyn

-  SubjectSettlementDateGasTo – datum konce platnosti subjektu zúčtování – plyn

-  DamElectricityValidityFrom – datum počátku platnosti přístupu na DT – elektřina

-  DamElectricityValidityTo – datum konce platnosti přístupu na DT – elektřina

-  DamGasValidityFrom – datum počátku platnosti přístupu na DT – plyn

-  DamGasValidityTo – datum konce platnosti přístupu na DT – plyn

-  DistributorElectricityFrom – datum počátku platnosti licence distributora – elektřina

-  DistributorElectricityTo – datum konce platnosti licence distributora – elektřina

-  DistributorGasFrom – datum počátku platnosti licence distributora – plyn

-  DistributorGasTo – datum konce platnosti licence distributora – plyn

Příklad vstupního požadavku:

<?xml version="1.0" encoding="utf-8" ?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:pub="http://www.ote-
cr.cz/schema/service/public">
   <soapenv:Header/>
   <soapenv:Body>
      <pub:GetRutList/>
   </soapenv:Body>
</soapenv:Envelope>

Příklad odpovědi:

<?xml version="1.0" encoding="UTF-8" ?>
<SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-
ENV="http://schemas.xmlsoap.org/soap/envelope/">
   <SOAP-ENV:Body>
      <GetRutListResponse xmlns="http://www.ote-cr.cz/schema/service/public">
         <Result>
            <Rut>
               <Id>3</Id>
               <Ean>8591824000304</Ean>
               <VatNo>70894451</VatNo>
               <Company>3</Company>

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

6

               <RegistrationDate>2002-04-11</RegistrationDate>
               <DamElectricityValidityFrom>2002-04-12</DamElectricityValidityFrom>
               <DamElectricityValidityTo>5000-01-01</DamElectricityValidityTo>
            </Rut>
            <Rut>
               <Id>5</Id>
               <Ean>8591824000502</Ean>
               <VatNo>46900896</VatNo>
               <Company>5</Company>
               <RegistrationDate>2004-04-02</RegistrationDate>
            </Rut>
            <Rut>
               <Id>6</Id>
               <Ean>8591824000601</Ean>
               <VatNo>00020699</VatNo>
               <Company>6</Company>
               <RegistrationDate>2004-06-30</RegistrationDate>
            </Rut>
            <Rut>
               <Id>20</Id>
               <Ean>8591824001905</Ean>
               <Eic>24X-OT-SK------V</Eic>
               <VatNo>35829141</VatNo>
               <Company>20</Company>
               <RegistrationDate>2009-08-20</RegistrationDate>
            </Rut>
            <Rut>
               <Id>21</Id>
               <Ean>8591824002100</Ean>
               <Eic>10XSK-SEPS-GRIDB</Eic>
               <VatNo>35829141</VatNo>
               <Company>21</Company>
               <RegistrationDate>2009-08-20</RegistrationDate>
            </Rut>
            <Rut>
               <Id>98</Id>
               <Ean>8591824009802</Ean>
               <VatNo>27865444</VatNo>
               <Company>98</Company>
               <RegistrationDate>2007-05-15</RegistrationDate>
               <DamElectricityValidityFrom>2009-03-31</DamElectricityValidityFrom>
               <DamElectricityValidityTo>5000-01-01</DamElectricityValidityTo>
            </Rut>
            <Rut>
               <Id>99</Id>
               <Ean>8591824009901</Ean>
               <VatNo>49546392</VatNo>
               <Company>99</Company>
               <RegistrationDate>2003-06-13</RegistrationDate>
            </Rut>
            <Rut>
               <Id>101</Id>
               <Ean>8591824010105</Ean>
               <VatNo>25702556</VatNo>
               <Company>101</Company>
               <RegistrationDate>2001-12-10</RegistrationDate>
            </Rut>
            <Rut>
               <Id>283</Id>
               <Ean>8591824028308</Ean>
               <Eic>27XG-CENTROPOL-P</Eic>
               <VatNo>25458302</VatNo>
               <Company>283</Company>
               <RegistrationDate>2003-04-14</RegistrationDate>
               <SubjectSettlementDateElectricityFrom>2007-10-31</SubjectSettlementDateElectricityFrom>
               <SubjectSettlementDateElectricityTo>2013-03-01</SubjectSettlementDateElectricityTo>
               <DamElectricityValidityFrom>2007-10-31</DamElectricityValidityFrom>
               <DamElectricityValidityTo>2013-03-01</DamElectricityValidityTo>
            </Rut>
         </Result>
      </GetRutListResponse>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

7

1.3.2.  Webové služby pro Denní trh

1.3.2.1.  GetDamIndexE

Služba poskytuje indexy denního trhu DT, platný ČNB kurz a sesouhlasené množství v daném pásmu a
za požadované období.

Struktura dotazu GetDamIndexE:

Element

Hodnota

Poznámka

Povinná
Nepovinná

/

StartDate

Datum

Počáteční den dodávky období, za které jsou požadovaná
data.

Povinná

Formát YYYY-MM-DD.

EndDate

Datum

Koncový den dodávky období, za které jsou požadovaná
data.

Povinná

Formát YYYY-MM-DD.

Struktura odpovědi GetDamIndexEResponse:

Element

Hodnota

Poznámka

Date

EurRate

Datum

Den dodávky. Formát YYYY-MM-DD.

Desetinné číslo

Kurz ČNB pro daný den dodávky

BaseLoad

Desetinné číslo

PeakLoad

Desetinné číslo

Hodnota s přesností na 3 desetinná místa.

Index obchodování v rámci pásma BASE LOAD
[EUR/MWh].

Hodnota s přesností na 2 desetinná místa.

Index obchodování v rámci pásma PEAK LOAD
[EUR/MWh]

Hodnota s přesností na 2 desetinná místa.

Povinná
Nepovinná

/

Povinná

Povinná

Nepovinná

Nepovinná

OffpeakLoad

Desetinné číslo

Index obchodování v rámci pásma OFFPEAK LOAD
[EUR/MWh].

Nepovinná

Hodnota s přesností na 2 desetinná místa.

BaseLoadVolume

Desetinné číslo

Celkové sesouhlasené množství v oblasti CZ v BASE
LOAD pásmu period daného dne dodávky v MWh.

Nepovinná

Hodnota s přesností na 3 desetinná místa.

PeakLoadVolume

Desetinné číslo

Celkové sesouhlasené množství v oblasti CZ v PEAK
LOAD pásmu period daného dne dodávky v MWh.

Nepovinná

Hodnota s přesností na 3 desetinná místa.

OffpeakLoadVolume  Desetinné číslo

Celkové sesouhlasené množství v oblasti CZ v OFFPEAK
LOAD pásmu period daného dne dodávky v MWh.

Nepovinná

Hodnota s přesností na 3 desetinná místa.

EmergencyState

Celé kladné číslo

Příznak stavu nouze.

Nepovinná

•

Hodnota:1 – Byl vyhlášen stav nouze.

Pozn.: Oddělovačem desetinných mís je tečka. V případě stavu nouze v rámci všech period daného dne dodávky
nejsou položky množství uvedené.

Příklad dotazu GetDamIndexE:

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:pub="http://www.ote-
cr.cz/schema/service/public">
   <soapenv:Header/>

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

8

   <soapenv:Body>
      <pub:GetDamIndexE>
         <pub:StartDate>2025-01-05</pub:StartDate>
         <pub:EndDate>2025-01-05</pub:EndDate>
      </pub:GetDamIndexE>
   </soapenv:Body>
</soapenv:Envelope>

Příklad odpovědi GetDamIndexEResponse:

<SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-
ENV="http://schemas.xmlsoap.org/soap/envelope/">
   <SOAP-ENV:Body>
      <GetDamIndexEResponse xmlns="http://www.ote-cr.cz/schema/service/public">
         <Result>
            <DamIndex>
               <Date>2025-01-05</Date>

   <EurRate>25.155</EurRate>

               <BaseLoad>112.78</BaseLoad>
               <PeakLoad>112.13</PeakLoad>
               <OffpeakLoad>113.43</OffpeakLoad>
               <BaseLoadVolume>84923.367</BaseLoadVolume>
               <PeakLoadVolume>41317.401</PeakLoadVolume>
               <OffpeakLoadVolume>43606.154</OffpeakLoadVolume>
            </DamIndex>
            <DamIndex>
               <Date>2025-01-06</Date>

   <EurRate>25.160</EurRate>

               <BaseLoad>114.48</BaseLoad>
               <PeakLoad>126.29</PeakLoad>
               <OffpeakLoad>102.67</OffpeakLoad>
               <BaseLoadVolume>81623.923</BaseLoadVolume>
               <PeakLoadVolume>40001.594</PeakLoadVolume>
               <OffpeakLoadVolume>41622.482</OffpeakLoadVolume>
               <EmergencyState>1</EmergencyState>
            </DamIndex>
            <DamIndex>
               <Date>2025-01-07</Date>

   <EurRate>25.155</EurRate>

               <EmergencyState>1</EmergencyState>
            </DamIndex>
         </Result>
      </GetDamIndexEResponse>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

1.3.2.2.  GetDamPriceE

Služba  poskytuje  výsledné  marginální  ceny  a  zobchodované  množství  na  DT  v 60min  rozlišení  za
požadované období.

Služba poskytuje data do dne dodávky 30.9.2025.

Struktura dotazu GetDamPriceE:

Element

Hodnota

Poznámka

Povinná
Nepovinná

/

StartDate

Datum

Počáteční den dodávky období, za které jsou požadovaná
data.

Povinná

Formát YYYY-MM-DD.

EndDate

Datum

Koncový den dodávky období, za které jsou požadovaná
data.

Povinná

StartHour

Celé kladné číslo

Formát YYYY-MM-DD.

Index počáteční hodinové periody rozsahu hodinových
period daného dne dodávky, za které jsou požadovaná
data. Může nabývat hodnot 1 až 25. (viz kap. 1.4.1 Služby
se zadáním hodiny).

Nepovinná

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

Element

Hodnota

Poznámka

EndHour

Celé kladné číslo

Index koncové hodinové periody rozsahu hodinových
period daného dne dodávky, za které jsou požadovaná
data. Může nabývat hodnot 1 až 25. (viz kap. 1.4.1 Služby
se zadáním hodiny).

9

Povinná
Nepovinná

/

Nepovinná

InEur

Boolean

Je-li nastaveno (true), vrací cenu v EUR, jinak v Kč. Cena
v Kč se přepočítává podle kurzu ČNB.

Nepovinná

Struktura odpovědi GetDamPriceEResponse:

Element

Hodnota

Poznámka

Date

Hour

Price

Datum

Den dodávky. Formát YYYY-MM-DD.

Celé kladné číslo

Index hodiny příslušného dne dodávky

Desetinné číslo

Marginální cena v [Kč/MWh] nebo v [EUR/MWh] v dané
hodině dodávky.

Hodnota s přesností na 2 desetinná místa.

Povinná
Nepovinná

/

Povinná

Povinná

Povinná

Volume

Desetinné číslo

Celkové zobchodované množství za ČR [MWh] v dané
hodině dodávky.

Povinná

Hodnota s přesností na 1 desetinné místo.

Emerg

Celé kladné číslo

Příznak stavu nouze.

Nepovinná

•

Hodnota:1 – Byl vyhlášen stav nouze.

Pozn.: Oddělovačem desetinných mís je tečka.

Příklad dotazu GetDamPriceE:

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:pub="http://www.ote-
cr.cz/schema/service/public">
   <soapenv:Header/>
   <soapenv:Body>
      <pub:GetDamPriceE>
         <pub:StartDate>2025-01-01</pub:StartDate>
         <pub:EndDate>2025-01-01</pub:EndDate>
         <!--Optional:-->
         <pub:StartHour>1</pub:StartHour>
         <!--Optional:-->
         <pub:EndHour>3</pub:EndHour>
         <!--Optional:-->
         <pub:InEur>true</pub:InEur>
      </pub:GetDamPriceE>
   </soapenv:Body>
</soapenv:Envelope>

Příklad odpovědi GetDamPriceEResponse:

<SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-
ENV="http://schemas.xmlsoap.org/soap/envelope/">
   <SOAP-ENV:Body>
      <GetDamPriceEResponse xmlns="http://www.ote-cr.cz/schema/service/public">
         <Result>
            <Item>
               <Date>2025-01-01</Date>
               <Hour>1</Hour>
               <Price>21.00</Price>
               <Volume>2935.0</Volume>
            </Item>
            <Item>
               <Date>2025-01-01</Date>
               <Hour>2</Hour>
               <Price>70.50</Price>

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

10

               <Volume>3465.7</Volume>
            </Item>
            <Item>
               <Date>2025-01-01</Date>
               <Hour>3</Hour>
               <Price>71.07</Price>
               <Volume>3521.0</Volume>
            </Item>
         </Result>
      </GetDamPriceEResponse>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

1.3.2.3.  GetDamPricePeriodE

Služba  poskytuje  marginální  ceny  a  zobchodované  množství  v rozlišení  15 min  nebo  60 min  podle
zvoleného parametru rozlišení a za požadované období a periody dodávky.

Služba poskytuje data ode dne dodávky 1.10.2025.

Struktura dotazu GetDamPricePeriodE:

Element

Hodnota

Poznámka

Povinná
Nepovinná

/

StartDate

Datum

Počáteční den dodávky období, za které jsou požadovaná
data.

Povinná

Formát YYYY-MM-DD.

EndDate

Datum

Koncový den dodávky období, za které jsou požadovaná
data.

Povinná

Formát YYYY-MM-DD.

PeriodResolution

Textový řetězec

Specifikace požadovaného rozlišení:

Povinná

•

•

PT15M – 15min rozlišení

PT60M – 60min rozlišení

StartPeriod

Celé kladné číslo

Počáteční index periody rozsahu period dodávky daného
rozlišení a v daném dni dodávky, za které jsou
požadovaná data. Může nabývat hodnot:

Nepovinná

•

•

1 až 100 v případě PeriodResolution= PT15M

1 až 25, v případě PeriodResolution= PT60M

Viz kap. 1.4 Omezení vrácených hodnot při specifikování
hodiny či periody.

EndPeriod

Celé kladné číslo

Index koncové periody rozsahu period dodávky daného
rozlišení v daném dni dodávky, za které jsou požadovaná
data. Může nabývat hodnot:

Nepovinná

•

•

1 až 100, v případě PeriodResolution = PT15M

1 až 25, v případě PeriodResolution = PT60M

Viz kap. 1.4 Omezení vrácených hodnot při specifikování
hodiny či periody.

Pozn.: Pokud rozsah dnů zadaného období je větší než 31 dnů, pak zpráva odpovědi bude obsahovat
data jen za 31 dnů počínaje dnem StartDate.

Struktura odpovědi GetDamPricePeriodEResponse:

Element

Hodnota

Poznámka

Povinná
Nepovinná

/

Date

Datum

Den dodávky. Formát YYYY-MM-DD.

Povinná

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

Element

Hodnota

Poznámka

PeriodResolution

Textový řetězec

PeriodIndex

PeriodInterval

Celé kladné číslo

Textový řetězec

Rozlišení periody dodávky, ve kterém jsou data
poskytována (odpovídá požadovanému rozlišení v
požadavku):

•

•

PT15M – 15min rozlišení

PT60M – 60min rozlišení

Index periody příslušného dne dodávky

Interval periody příslušného dne dodávky ve formátu:

•

•

HH24:MI-HH24:MI, v případě
PeriodResolution=PT15M

HH24-HH24, v případě PeriodResolu-
tion=PT60M

11

Povinná
Nepovinná

/

Povinná

Povinná

Povinná

Price

Desetinné číslo

Marginální cena [EUR/MWh] v dané periodě dodávky.

Nepovinná

Hodnota s přesností na 2 desetinná místa.

Položka se předává jen v případě 15min dat
(PeriodResolution=PT15M).

HourlyPrice

Desetinné číslo

60min cena [EUR/MWh] v dané periodě dodávky.

Nepovinná

Hodnota s přesností na 2 desetinná místa.

VolumeTotal

Desetinné číslo

Celkové sesouhlasené množství v CZ oblasti (MWh)
v dané periodě dodávky.

Nepovinná

Hodnota s přesností na 3 desetinná místa.

EmergencyState

Celé kladné číslo

Příznak stavu nouze.

Nepovinná

•

Hodnota:1 – Byl vyhlášen stav nouze.

Pozn.: Oddělovačem desetinných míst je tečka. V případě, že byl v dané periodě vyhlášen stav nouze, položky
ceny a množství nejsou v odpovědi zahrnuty.

Příklad dotazu GetDamPricePeriodE:

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:pub="http://www.ote-
cr.cz/schema/service/public">
   <soapenv:Header/>
   <soapenv:Body>
      <pub:GetDamPricePeriodE>
         <pub:StartDate>2025-01-05</pub:StartDate>
         <pub:EndDate>2025-01-05</pub:EndDate>
         <pub:PeriodResolution>PT15M</pub:PeriodResolution>
         <!--Optional:-->
         <pub:StartPeriod>1</pub:StartPeriod>
         <!--Optional:-->
         <pub:EndPeriod>3</pub:EndPeriod>
      </pub:GetDamPricePeriodE>
   </soapenv:Body>
</soapenv:Envelope>

Příklad odpovědi GetDamPricePeriodEResponse:

<SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-
ENV="http://schemas.xmlsoap.org/soap/envelope/">
   <SOAP-ENV:Body>
      <GetDamPricePeriodEResponse xmlns="http://www.ote-cr.cz/schema/service/public">
         <Result>
            <Item>
               <Date>2025-01-05</Date>
               <PeriodResolution>PT15M</PeriodResolution>
               <PeriodIndex>1</PeriodIndex>
               <PeriodInterval>00:00-00:15</PeriodInterval>
               <Price>113.39</Price>
               <HourlyPrice>112.73</HourlyPrice>

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

12

            </Item>
            <Item>
               <Date>2025-01-05</Date>
               <PeriodResolution>PT15M</PeriodResolution>
               <PeriodIndex>2</PeriodIndex>
               <PeriodInterval>00:15-00:30</PeriodInterval>
               <Price>111.55</Price>
               <HourlyPrice>112.73</HourlyPrice>
            </Item>
            <Item>
               <Date>2025-01-05</Date>
               <PeriodResolution>PT15M</PeriodResolution>
               <PeriodIndex>3</PeriodIndex>
               <PeriodInterval>00:30-00:45</PeriodInterval>
               <EmergencyState>1</EmergencyState>
            </Item>
         </Result>
      </GetDamPricePeriodEResponse>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

1.3.2.4.  GetDamAllE

Služba  poskytuje  výsledné  marginální  ceny  a  zobchodované  množství,  přeshraniční  tok  ČR/SR  a
realizované Importy, Exporty na DT v hodinovém rozlišení za požadované období.

Služba poskytuje data do dne dodávky 30.9.2025.

Struktura dotazu GetDamAllE:

Element

Hodnota

Poznámka

Povinná
Nepovinná

/

StartDate

Datum

Počáteční den dodávky období, za které jsou požadovaná
data.

Povinná

Formát YYYY-MM-DD.

EndDate

Datum

Koncový den dodávky období, za které jsou požadovaná
data.

Povinná

StartHour

Celé kladné číslo

EndHour

Celé kladné číslo

Formát YYYY-MM-DD.

Index počáteční hodinové periody rozsahu hodinových
period daného dne dodávky, za které jsou požadovaná
data. Může nabývat hodnot 1 až 25. (viz kap. 1.4.1 Služby
se zadáním hodiny).

Index koncové hodinové periody rozsahu hodinových
period daného dne dodávky, za které jsou požadovaná
data. Může nabývat hodnot 1 až 25. (viz kap. 1.4.1 Služby
se zadáním hodiny).

Nepovinná

Nepovinná

InEur

Boolean

Je-li nastaveno (true), vrací cenu v EUR, jinak v Kč. Cena
v Kč se přepočítává podle kurzu ČNB.

Nepovinná

Struktura odpovědi GetDamAllEResponse:

Element

Hodnota

Poznámka

Date

Hour

Datum

Den dodávky. Formát YYYY-MM-DD.

Celé kladné číslo

Index hodiny příslušného dne dodávky

PriceCZ

Desetinné číslo

Marginální cena v [Kč/MWh] nebo v [EUR/MWh] v CZ
oblasti dodávky.

Hodnota s přesností na 2 desetinná místa.

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

Povinná
Nepovinná

/

Povinná

Povinná

Povinná

Element

Hodnota

Poznámka

VolumeCZ

Desetinné číslo

Celkové zobchodované množství za ČR [MWh] v dané
hodině dodávky.

Hodnota s přesností na 1 desetinné místo.

13

Povinná
Nepovinná

/

Povinná

FlowCZSK

Desetinné číslo

Výsledný tok [MWh] na propojení oblastí CZ-SK v dané
hodině dodávky.

Povinná

Hodnota s přesností na 1 desetinné místo.

FlowSKCR

Desetinné číslo

Výsledný tok [MWh] na propojení oblastí SK-CZ v dané
hodině dodávky.

Povinná

Hodnota s přesností na 1 desetinné místo.

ImportCZ

Desetinné číslo

Celková výše importu v CZ oblasti v MWh.

Povinná

Hodnota s přesností na 1 desetinné místo.

ExportCZ

Desetinné číslo

Celková výše exportu v CZ oblasti v MWh.

Povinná

Hodnota s přesností na 1 desetinné místo.

Emerg

Celé kladné číslo

Příznak stavu nouze.

Nepovinná

•

Hodnota:1 – Byl vyhlášen stav nouze.

Pozn.: Oddělovačem desetinných mís je tečka.

Příklad dotazu GetDamAllE:

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:pub="http://www.ote-
cr.cz/schema/service/public">
   <soapenv:Header/>
   <soapenv:Body>
      <pub:GetDamAllE>
         <pub:StartDate>2025-01-01</pub:StartDate>
         <pub:EndDate>2025-01-01</pub:EndDate>
         <!--Optional:-->
         <pub:StartHour>1</pub:StartHour>
         <!--Optional:-->
         <pub:EndHour>3</pub:EndHour>
         <!--Optional:-->
         <pub:InEur>true</pub:InEur>
      </pub:GetDamAllE>
   </soapenv:Body>
</soapenv:Envelope>

Příklad odpovědi GetDamAllEResponse:

<SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-
ENV="http://schemas.xmlsoap.org/soap/envelope/">
   <SOAP-ENV:Body>
      <GetDamAllEResponse xmlns="http://www.ote-cr.cz/schema/service/public">
         <Result>
            <Item>
               <Date>2025-01-01</Date>
               <Hour>1</Hour>
               <PriceCZ>21.00</PriceCZ>
               <VolumeCZ>2935.0</VolumeCZ>
               <FlowCZSK>627.7</FlowCZSK>
               <FlowSKCR>0.0</FlowSKCR>
               <ImportCZ>-1560.8</ImportCZ>
               <ExportCZ>2840.5</ExportCZ>
            </Item>
            <Item>
               <Date>2025-01-01</Date>
               <Hour>2</Hour>
               <PriceCZ>70.50</PriceCZ>
               <VolumeCZ>3465.7</VolumeCZ>
               <FlowCZSK>766.5</FlowCZSK>
               <FlowSKCR>0.0</FlowSKCR>

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

14

               <ImportCZ>-1663.8</ImportCZ>
               <ExportCZ>3310.8</ExportCZ>
            </Item>
            <Item>
               <Date>2025-01-01</Date>
               <Hour>3</Hour>
               <PriceCZ>71.07</PriceCZ>
               <VolumeCZ>3521.0</VolumeCZ>
               <FlowCZSK>745.6</FlowCZSK>
               <FlowSKCR>0.0</FlowSKCR>
               <ImportCZ>-1813.0</ImportCZ>
               <ExportCZ>3390.0</ExportCZ>
            </Item>
         </Result>
      </GetDamAllEResponse>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

1.3.2.5.  GetDamAllPeriodE

Služba poskytuje výsledné marginální ceny, zobchodované množství a realizované Importy, Exporty na
DT v rozlišení 15 min nebo 60 min podle zvoleného parametru rozlišení a za požadované období.

Služba poskytuje data ode dne dodávky 1.10.2025.

Struktura dotazu GetDamAllPeriodE:

Element

Hodnota

Poznámka

Povinná
Nepovinná

/

StartDate

Datum

Počáteční den dodávky období, za které jsou požadovaná
data.

Povinná

Formát YYYY-MM-DD.

EndDate

Datum

Koncový den dodávky období, za které jsou požadovaná
data.

Povinná

Formát YYYY-MM-DD.

PeriodResolution

Textový řetězec

Specifikace požadovaného rozlišení:

Povinná

•

•

PT15M – 15min rozlišení

PT60M – 60min rozlišení

StartPeriod

Celé kladné číslo

Počáteční index periody rozsahu period dodávky daného
rozlišení a v daném dni dodávky, za které jsou
požadovaná data. Může nabývat hodnot:

Nepovinná

•

•

1 až 100, v případě PeriodResolution= PT15M

1 až 25, v případě PeriodResolution= PT60M

Viz kap. 1.4 Omezení vrácených hodnot při specifikování
hodiny či periody.

EndPeriod

Celé kladné číslo

Index koncové periody rozsahu period dodávky daného
rozlišení v daném dni dodávky, za které jsou požadovaná
data. Může nabývat hodnot:

Nepovinná

•

•

1 až 100, v případě PeriodResolution= PT15M

1 až 25, v případě PeriodResolution= PT60M

Viz kap. 1.4 Omezení vrácených hodnot při specifikování
hodiny či periody.

Pozn.: Pokud rozsahu dnů zadaného období je větší než 31 dnů, pak zpráva odpovědi bude obsahovat
data jen za 31 dnů počínaje dnem StartDate.

Struktura odpovědi GetDamAllPeriodEResponse:

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

Element

Hodnota

Poznámka

Date

Datum

Den dodávky. Formát YYYY-MM-DD.

PeriodResolution

Textový řetězec

PeriodIndex

PeriodInterval

Celé kladné číslo

Textový řetězec

Rozlišení periody dodávky, ve kterém jsou data
poskytována (odpovídá požadovanému rozlišení v
požadavku):

•

•

PT15M – 15min rozlišení

PT60M – 60min rozlišení

Index periody příslušného dne dodávky

Interval periody příslušného dne dodávky ve formátu:

•

•

HH24:MI-HH24:MI, v případě
PeriodResolution=PT15M

HH24-HH24, v případě PeriodResolu-
tion=PT60M

15

Povinná
Nepovinná

/

Povinná

Povinná

Povinná

Povinná

Price

Desetinné číslo

Marginální cena [EUR/MWh] v dané periodě dodávky.

Nepovinná

Hodnota s přesností na 2 desetinná místa.

Položka se předává jen v případě 15min dat
(PeriodResolution=PT15M).

HourlyPrice

Desetinné číslo

60min cena [EUR/MWh] v dané periodě dodávky.

Nepovinná

Hodnota s přesností na 2 desetinná místa.

VolumeTotal

Desetinné číslo

Celkové sesouhlasené množství v CZ oblasti (MWh)
v dané periodě dodávky.

Nepovinná

Hodnota s přesností na 3 desetinná místa.

VolumeBuyQuarterly  Desetinné číslo

Sesouhlasené množství v CZ oblasti 15min nabídek na
nákup (MWh) v dané periodě dodávky.

Nepovinná

Hodnota s přesností na 3 desetinná místa.

VolumeSellQuarterly  Desetinné číslo

Sesouhlasené množství v CZ oblasti 15min nabídek na
prodej (MWh) v dané periodě dodávky.

Nepovinná

Hodnota s přesností na 3 desetinná místa..

VolumeBuyHourly

Desetinné číslo

Sesouhlasené množství v CZ oblasti 60min nabídek na
nákup (MWh) v dané periodě dodávky.

Nepovinná

Hodnota s přesností na 3 desetinná místa.

VolumeSellHourly

Desetinné číslo

Sesouhlasené množství v CZ oblasti 60min nabídek na
prodej (MWh) v dané periodě dodávky.

Nepovinná

Hodnota s přesností na 3 desetinná místa.

Import

Desetinné číslo

Celková výše importu v CZ oblasti v MWh v dané periodě
dodávky.

Povinná

Hodnota s přesností na 3 desetinná místa.

Export

Desetinné číslo

Celková výše exportu v CZ oblasti v MWh v dané periodě
dodávky.

Povinná

Hodnota s přesností na 3 desetinná místa.

EmergencyState

Celé kladné číslo

Příznak stavu nouze.

Nepovinná

•

Hodnota:1 – Byl vyhlášen stav nouze.

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

Pozn.: Oddělovačem desetinných mís je tečka. V případě, že byl v dané periodě vyhlášen stav nouze, položky
ceny a množství (vyjma exportu a import) nejsou v odpovědi zahrnuty.

16

Příklad dotazu GetDamPricePeriodE:

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:pub="http://www.ote-
cr.cz/schema/service/public">
   <soapenv:Header/>
   <soapenv:Body>
      <pub:GetDamAllPeriodE>
         <pub:StartDate>2025-01-05</pub:StartDate>
         <pub:EndDate>2025-01-05</pub:EndDate>
         <pub:PeriodResolution>PT15M</pub:PeriodResolution>
         <!--Optional:-->
         <pub:StartPeriod>1</pub:StartPeriod>
         <!--Optional:-->
         <pub:EndPeriod>3</pub:EndPeriod>
      </pub:GetDamAllPeriodE>
   </soapenv:Body>
</soapenv:Envelope>

Příklad odpovědi GetDamAllPeriodEResponse:

<SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-
ENV="http://schemas.xmlsoap.org/soap/envelope/">
   <SOAP-ENV:Body>
      <GetDamAllPeriodEResponse xmlns="http://www.ote-cr.cz/schema/service/public">
         <Result>
            <Item>
               <Date>2025-01-05</Date>
               <PeriodResolution>PT15M</PeriodResolution>
               <PeriodIndex>1</PeriodIndex>
               <PeriodInterval>00:00-00:15</PeriodInterval>
               <Price>113.39</Price>
               <HourlyPrice>112.73</HourlyPrice>
               <VolumeTotal>922.000</Volume>
               <VolumeBuyQuarterly>147.520</VolumeBuyQuarterly>
               <VolumeSellQuarterly>467.147</VolumeSellQuarterly>
               <VolumeBuyHourly>73.760</VolumeBuyHourly>
               <VolumeSellHourly>233.573</VolumeSellHourly>
               <Import>-180.825</Import>
               <Export>736.025</Export>
            </Item>
            <Item>
               <Date>2025-01-05</Date>
               <PeriodResolution>PT15M</PeriodResolution>
               <Period>2</Period>
               <PeriodInterval>00:15-00:30</PeriodInterval>
               <Price>111.55</Price>
               <HourlyPrice>112.73</HourlyPrice>
               <VolumeTotal>938.925</Volume>
               <VolumeBuyQuarterly>150.228</VolumeBuyQuarterly>
               <VolumeSellQuarterly>475.722</VolumeSellQuarterly>
               <VolumeBuyHourly>75.114</VolumeBuyHourly>
               <VolumeSellHourly>2373.861</VolumeSellHourly>
               <Import>-191.800</Import>
               <Export>773.125</Export>
            </Item>
            <Item>
               <Date>2025-01-05</Date>
               <PeriodResolution>PT15M</PeriodResolution>
               <Period>3</Period>
               <PeriodInterval>00:30-00:45</PeriodInterval>
               <Import>-90.123</Import>
               <Export>73.015</Export>
               <EmergencyState>1</EmergencyState>
            </Item>
         </Result>
      </GetDaAllPeriodEResponse>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

17

1.3.2.6.  GetDamFlowsPeriodE

Služba poskytuje výsledné přeshraniční toky v jednotkách MW za všechna propojení relevantní k CZ
oblasti a za požadované období.

Služba poskytuje data ode dne dodávky 1.10.2025.

Struktura dotazu GetDamFlowsPeriodE:

Element

Hodnota

Poznámka

Povinná
Nepovinná

/

StartDate

Datum

Počáteční den dodávky období, za které jsou požadovaná
data.

Povinná

Formát YYYY-MM-DD.

EndDate

Datum

Koncový den dodávky období, za které jsou požadovaná
data.

Povinná

Formát YYYY-MM-DD.

StartPeriod

Celé kladné číslo

Počáteční index periody rozsahu period dodávky daného
rozlišení a v daném dni dodávky, za které jsou
požadovaná data. Může nabývat hodnot:

Nepovinná

•

•

1 až 100, v případě dne dodávky s 15min
nejmenším rozlišením

1 až 25, v případě dne dodávky s 60min
nejmenším rozlišením

Viz kap. 1.4 Omezení vrácených hodnot při specifikování
hodiny či periody.

EndPeriod

Celé kladné číslo

Index koncové periody rozsahu period dodávky daného
rozlišení v daném dni dodávky, za které jsou požadovaná
data. Může nabývat hodnot:

Nepovinná

•

•

1 až 100, v případě dne dodávky s 15min
nejmenším rozlišením

1 až 25, v případě dne dodávky s 60min
nejmenším rozlišením

Viz kap. 1.4 Omezení vrácených hodnot při specifikování
hodiny či periody.

Pozn.: Pokud rozsahu dnů zadaného období je větší než 31 dnů, pak zpráva odpovědi bude obsahovat
data jen za 31 dnů počínaje dnem StartDate.

Struktura odpovědi GetDamFlowsPeriodEResponse:

Element

Hodnota

Poznámka

Date

Datum

Den dodávky. Formát YYYY-MM-DD.

PeriodResolution

Textový řetězec

Rozlišení periody dodávky, ve kterém jsou data
poskytována (odpovídá rozlišení CZ oblasti dodávky pro
daný den dodávky):

•

•

PT15M – 15min rozlišení

PT60M – 60min rozlišení

Povinná
Nepovinná

/

Povinná

Povinná

PeriodIndex

Celé kladné číslo

Index periody příslušného dne dodávky

Povinná

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

Element

Hodnota

Poznámka

18

Povinná
Nepovinná

/

PeriodInterval

Textový řetězec

Interval periody příslušného dne dodávky ve formátu:

Povinná

•

•

HH24:MI-HH24:MI, v případě
PeriodResolution=PT15M

HH24-HH24,
tion=PT60M

v případě

PeriodResolu-

FlowCZAT

Desetinné číslo

Hodnota výsledného toku na úrovni oblasti ve směru CZ ->
AT v dané periodě v MW.

Povinná

Hodnota s přesností na 1 desetinné místo.

FlowATCZ

Desetinné číslo

Hodnota výsledného toku na úrovni oblasti ve směru AT ->
CZ v dané periodě v MW.

Povinná

Hodnota s přesností na 1 desetinné místo.

FlowCZPL

Desetinné číslo

Hodnota výsledného toku na úrovni oblasti ve směru CZ ->
PL v dané periodě v MW.

Povinná

Hodnota s přesností na 1 desetinné místo.

FlowPLCZ

Desetinné číslo

Hodnota výsledného toku na úrovni oblasti ve směru PL ->
CZ v dané periodě v MW.

Povinná

Hodnota s přesností na 1 desetinné místo.

FlowCZSK

Desetinné číslo

Hodnota výsledného toku na úrovni oblasti ve směru CZ ->
SK v dané periodě v MW.

Povinná

Hodnota s přesností na 1 desetinné místo.

FlowSKCZ

Desetinné číslo

Hodnota výsledného toku na úrovni oblasti ve směru SK ->
CZ v dané periodě v MW.

Povinná

Hodnota s přesností na 1 desetinné místo.

FlowCZDE

Desetinné číslo

Hodnota výsledného toku na úrovni oblasti ve směru CZ ->
DE(Tennet) v dané periodě v MW.

Povinná

Hodnota s přesností na 1 desetinné místo.

FlowDECZ

Desetinné číslo

Hodnota  výsledného  toku  na  úrovni  oblasti  ve  směru
DE(Tennet) -> CZ v dané periodě v MW.

Povinná

Hodnota s přesností na 1 desetinné místo.

Pozn.: Oddělovačem desetinných mís je tečka.

Příklad dotazu GetDamFlowsPeriodE:

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:pub="http://www.ote-
cr.cz/schema/service/public">
   <soapenv:Header/>
   <soapenv:Body>
      <pub:GetDamFlowsPeriodE>
         <pub:StartDate>2025-01-05</pub:StartDate>
         <pub:EndDate>2025-01-05</pub:EndDate>
         <!--Optional:-->
         <pub:StartPeriod>1</pub:StartPeriod>
         <!--Optional:-->
         <pub:EndPeriod>1</pub:EndPeriod>
      </pub:GetDamFlowsPeriodE>
   </soapenv:Body>
</soapenv:Envelope>

Příklad odpovědi GetDamFlowsPeriodEResponse:

<SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-
ENV="http://schemas.xmlsoap.org/soap/envelope/">
   <SOAP-ENV:Body>
      <GetDamFlowsPeriodEResponse xmlns="http://www.ote-cr.cz/schema/service/public">
         <Result>
            <Item>
               <Date>2025-01-05</Date>

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

19

               <PeriodResolution>PT15M</PeriodResolution>
               <PeriodIndex>1</PeriodIndex>
               <PeriodInterval>00:00-00:15</PeriodInterval>
               <FlowCZAT>2060.5</FlowCZAT>
               <FlowATCZ>0.0</FlowATCZ>
               <FlowCZPL>0.0</FlowCZPL>
               <FlowPLCZ>511.0</FlowPLCZ>
               <FlowCZSK>518.6</FlowCZSK>
               <FlowSKCZ>0.0</FlowSKCZ>
               <FlowCZDE>0.0</FlowCZDE>
               <FlowDECZ>913.6</FlowDECZ>
            </Item>
         </Result>
      </GetDamFlowsPeriodEResponse>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

1.3.3.  Webové služby pro Vnitrodenní aukce

1.3.3.1.  GetIDAIndexE

Služba poskytuje indexy IDA v EUR a platný ČNB kurz pro požadované dny dodávky a aukci.

Služba poskytuje data ode dne dodávky 14.6.2024.

Struktura dotazu GetIDAIndexE:

Element

Hodnota

Poznámka

Povinná
Nepovinná

/

StartDate

Datum

Počáteční den dodávky období, za které jsou požadovaná
data.

Povinná

Formát YYYY-MM-DD.

EndDate

Datum

Koncový den dodávky období, za které jsou požadovaná
data.

Povinná

Formát YYYY-MM-DD.

Auction

IDA1, IDA2, IDA3

Typ IDA aukce

Povinná

Struktura odpovědi GetIDAIndexEResponse:

Element

Hodnota

Poznámka

Date

Auction

EurRate

Datum

Den dodávky. Formát YYYY-MM-DD.

IDA1, IDA2, IDA3

Typ IDA aukce

Desetinné číslo

Kurz ČNB pro daný den dodávky

BaseLoad

Desetinné číslo

PeakLoad

Desetinné číslo

Hodnota s přesností na 3 desetinná místa.

Index obchodování v rámci pásma BASE LOAD
[EUR/MWh].

Hodnota s přesností na 2 desetinná místa.

Index obchodování v rámci pásma PEAK LOAD
[EUR/MWh].

Peak index není definován pro IDA3.

Hodnota s přesností na 2 desetinná místa.

Povinná
Nepovinná

/

Povinná

Povinná

Povinná

Nepovinná

Nepovinná

OffpeakLoad

Desetinné číslo

Index obchodování v rámci pásma OFFPEAK LOAD
[EUR/MWh].

Nepovinná

2025 OTE, a.s.

Revize dne:
 29.4.2025

OffPeak index není definován pro IDA3.

Hodnota s přesností na 2 desetinná místa.

Název dokumentu:
Uživatelský manuál webové služby OTE

20

Povinná
Nepovinná

/

Nepovinná

Element

Hodnota

Poznámka

Emerg

Celé kladné číslo

Příznak stavu nouze.

•

Hodnota:1 – Byl vyhlášen stav nouze.

Pozn.: Oddělovačem desetinných mís je tečka.

Příklad dotazu GetIDAIndexEResponse:

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:pub="http://www.ote-
cr.cz/schema/service/public">
   <soapenv:Header/>
   <soapenv:Body>
      <pub:GetIDAIndexE>
         <pub:StartDate>2024-06-14</pub:StartDate>
         <pub:EndDate>2024-06-15</pub:EndDate>
         <pub:Auction>IDA1</pub:Auction>
      </pub:GetIDAIndexE>
   </soapenv:Body>
</soapenv:Envelope>

Příklad odpovědi GetIDAIndexEResponse:

<SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-
ENV="http://schemas.xmlsoap.org/soap/envelope/">
   <SOAP-ENV:Body>
      <GetIDAIndexEResponse xmlns="http://www.ote-cr.cz/schema/service/public">
         <Result>
            <IDAIndex>
               <Date>2024-06-14</Date>
               <Auction>IDA1</Auction>
               <EurRate>24.740</EurRate>
               <BaseLoad>0.00</BaseLoad>
               <PeakLoad>0.00</PeakLoad>
               <OffpeakLoad>0.00</OffpeakLoad>
            </IDAIndex>
            <IDAIndex>
               <Date>2024-06-15</Date>
               <Auction>IDA1</Auction>
               <EurRate>24.740</EurRate>
               <BaseLoad>6.15</BaseLoad>
               <PeakLoad>-20.55</PeakLoad>
               <OffpeakLoad>99.58</OffpeakLoad>
            </IDAIndex>
         </Result>
      </GetIDAIndexEResponse>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

1.3.3.2.  GetIDAPriceE

Služba poskytuje výsledné marginální ceny a zobchodované množství pro zvolené období a IDA aukci
v 60 min rozlišení.

Služba poskytuje data pro dny dodávky od 14.6.2024 do 30.6.2024.

Struktura dotazu GetIDAPriceE:

Element

Hodnota

Poznámka

Povinná
Nepovinná

/

StartDate

Datum

Počáteční den dodávky období, za které jsou požadovaná
data.

Povinná

Formát YYYY-MM-DD.

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

Element

Hodnota

Poznámka

21

Povinná
Nepovinná

/

EndDate

Datum

Koncový den dodávky období, za které jsou požadovaná
data.

Povinná

StartHour

Celé kladné číslo

EndHour

Celé kladné číslo

Formát YYYY-MM-DD.

Index počáteční hodinové periody rozsahu hodinových
period daného dne dodávky, za které jsou požadovaná
data. Může nabývat hodnot 1 až 25. (viz kap. 1.4.1 Služby
se zadáním hodiny).

Index koncové hodinové periody rozsahu hodinových
period daného dne dodávky, za které jsou požadovaná
data. Může nabývat hodnot 1 až 25. (viz kap. 1.4.1 Služby
se zadáním hodiny).

Auction

InEur

IDA1, IDA2, IDA3

Typ IDA aukce

Boolean

Je-li nastaveno (true), vrací cenu v EUR, jinak v Kč. Cena
v Kč se přepočítává podle kurzu ČNB.

Struktura odpovědi GetIDAPriceEResponse:

Element

Hodnota

Poznámka

Date

Auction

Hour

Price

Datum

Den dodávky. Formát YYYY-MM-DD.

IDA1, IDA2, IDA3

Typ IDA aukce

Celé kladné číslo

Index hodiny příslušného dne dodávky

Desetinné číslo

Marginální cena v [Kč/MWh] nebo v [EUR/MWh] v dané
hodině dodávky.

Hodnota s přesností na 2 desetinná místa.

Nepovinná

Nepovinná

Povinná

Nepovinná

Povinná
Nepovinná

/

Povinná

Povinná

Povinná

Povinná

Volume

Desetinné číslo

Celkové zobchodované množství za ČR [MWh] v dané
hodině dodávky.

Povinná

Hodnota s přesností na 1 desetinné místo (poskytovány 3
des. místa).

Emerg

Celé kladné číslo

Příznak stavu nouze.

Nepovinná

•

Hodnota:1 – Byl vyhlášen stav nouze.

Pozn.: Oddělovačem desetinných mís je tečka.

Příklad dotazu GetIDAPriceE:

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:pub="http://www.ote-
cr.cz/schema/service/public">
   <soapenv:Header/>
   <soapenv:Body>
      <pub:GetIDAPriceE>
         <pub:StartDate>2024-06-18</pub:StartDate>
         <pub:EndDate>2024-06-18</pub:EndDate>
         <!--Optional:-->
         <pub:StartHour>1</pub:StartHour>
         <!--Optional:-->
         <pub:EndHour>3</pub:EndHour>
         <pub:Auction>IDA1</pub:Auction>
         <!--Optional:-->
         <pub:InEur>true</pub:InEur>
      </pub:GetIDAPriceE>
   </soapenv:Body>
</soapenv:Envelope>

Příklad odpovědi GetIDAPriceEResponse:

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

22

<SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-
ENV="http://schemas.xmlsoap.org/soap/envelope/">
   <SOAP-ENV:Body>
      <GetIDAPriceEResponse xmlns="http://www.ote-cr.cz/schema/service/public">
         <Result>
            <Item>
               <Date>2024-06-18</Date>
               <Auction>IDA1</Auction>
               <Hour>1</Hour>
               <Price>99.18</Price>
               <Volume>0.000</Volume>
            </Item>
            <Item>
               <Date>2024-06-18</Date>
               <Auction>IDA1</Auction>
               <Hour>2</Hour>
               <Price>90.00</Price>
               <Volume>1.500</Volume>
            </Item>
            <Item>
               <Date>2024-06-18</Date>
               <Auction>IDA1</Auction>
               <Hour>3</Hour>
               <Price>90.00</Price>
               <Volume>0.300</Volume>
            </Item>
         </Result>
      </GetIDAPriceEResponse>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

1.3.3.3.  GetIDAPricePeriodE

Služba poskytuje výsledné marginální ceny a zobchodované množství pro zvolené období a IDA aukci
v 15/60 min rozlišení (dle rozlišení periody pro daný den dodávky).

Služba poskytuje data ode dne dodávky 14.6.2024.

Struktura dotazu GetIDAPricePeriodE:

Element

Hodnota

Poznámka

Povinná
Nepovinná

/

StartDate

Datum

Počáteční den dodávky období, za které jsou požadovaná
data.

Povinná

Formát YYYY-MM-DD.

EndDate

Datum

Koncový den dodávky období, za které jsou požadovaná
data.

Povinná

StartPeriod

Celé kladné číslo

EndPeriod

Celé kladné číslo

Formát YYYY-MM-DD.

Počáteční index periody rozsahu period dodávky daného
rozlišení a v daném dni dodávky, za které jsou
požadovaná data. Může nabývat hodnot:

Nepovinná

•

•

1 až 25, v případě dne dodávky s hodinovým
rozlišením periody

1 až 100, v případě dne dodávky
s čtvrthodinovým rozlišením periody

Viz kap. 1.4 Omezení vrácených hodnot při specifikování
hodiny či periody.

Index koncové periody rozsahu period dodávky daného
rozlišení v daném dni dodávky, za které jsou požadovaná
data. Může nabývat hodnot:

Nepovinná

•

1 až 25, v případě dne dodávky s hodinovým
rozlišením periody

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

Element

Hodnota

Poznámka

•

1 až 100, v případě dne dodávky
s čtvrthodinovým rozlišením periody

Viz kap. 1.4 Omezení vrácených hodnot při specifikování
hodiny či periody.

Auction

InEur

IDA1, IDA2, IDA3

Typ IDA aukce

Boolean

Je-li nastaveno (true), vrací cenu v EUR, jinak v Kč. Cena
v Kč se přepočítává podle kurzu ČNB.

Struktura odpovědi GetIDAPricePeriodEResponse:

Element

Hodnota

Poznámka

Date

Datum

Den dodávky. Formát YYYY-MM-DD.

PeriodResolution

Textový řetězec

Rozlišení periody dodávky, ve kterém jsou data
poskytována:

•

•

PT15M – 15min rozlišení

PT60M – 60min rozlišení

23

Povinná
Nepovinná

/

Povinná

Nepovinná

Povinná
Nepovinná

/

Povinná

Povinná

PeriodIndex

Celé kladné číslo

Index periody příslušného dne dodávky. Může nabývat
hodnot:

Povinná

•

•

1 až 100, v případě PeriodResolution = PT15M

1 až 25, v případě PeriodResolution= PT60M

PeriodInterval

Textový řetězec

Interval periody příslušného dne dodávky ve formátu:

Povinná

•

•

HH24:MI-HH24:MI, v případě PeriodResolution
= PT15M

HH24-HH24, v případě PeriodResolution =
PT60M

Auction

Price

IDA1, IDA2, IDA3

Typ IDA aukce

Desetinné číslo

Marginální cena v [Kč/MWh] nebo v [EUR/MWh] v dané
periodě dodávky.

Hodnota s přesností na 2 desetinná místa.

Povinná

Povinná

Volume

Desetinné číslo

Celkové zobchodované množství za ČR [MWh] v dané
periodě dodávky.

Povinná

Hodnota s přesností na 1 desetinné místo.

Emerg

Celé kladné číslo

Příznak stavu nouze.

Nepovinná

•

Hodnota:1 – Byl vyhlášen stav nouze.

Pozn.: Oddělovačem desetinných míst je tečka.

Příklad dotazu GetIDAPricePeriodE:

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:pub="http://www.ote-
cr.cz/schema/service/public">
   <soapenv:Header/>
   <soapenv:Body>
      <pub:GetIDAPricePeriodE>
         <pub:StartDate>2024-07-02</pub:StartDate>
         <pub:EndDate>2024-07-02</pub:EndDate>
         <!--Optional:-->
         <pub:StartPeriod>1</pub:StartPeriod>
         <!--Optional:-->
         <pub:EndPeriod>3</pub:EndPeriod>
         <pub:Auction>IDA1</pub:Auction>

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

24

         <!--Optional:-->
         <pub:InEur>true</pub:InEur>
      </pub:GetIDAPricePeriodE>
   </soapenv:Body>
</soapenv:Envelope>

Příklad odpovědi GetIDAPricePeriodEResponse:

<SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-
ENV="http://schemas.xmlsoap.org/soap/envelope/">
   <SOAP-ENV:Body>
      <GetIDAPricePeriodEResponse xmlns="http://www.ote-cr.cz/schema/service/public">
         <Result>
            <Item>
               <Date>2024-07-02</Date>
               <PeriodResolution>PT15M</PeriodResolution>
               <PeriodIndex>1</PeriodIndex>
               <PeriodInterval>00:00-00:15</PeriodInterval>
               <Auction>IDA1</Auction>
               <Price>115.56</Price>
               <Volume>2.6</Volume>
            </Item>
            <Item>
               <Date>2024-07-02</Date>
               <PeriodResolution>PT15M</PeriodResolution>
               <PeriodIndex>2</PeriodIndex>
               <PeriodInterval>00:15-00:30</PeriodInterval>
               <Auction>IDA1</Auction>
               <Price>40.00</Price>
               <Volume>1.9</Volume>
            </Item>
            <Item>
               <Date>2024-07-02</Date>
               <PeriodResolution>PT15M</PeriodResolution>
               <PeriodIndex>3</PeriodIndex>
               <PeriodInterval>00:30-00:45</PeriodInterval>
               <Auction>IDA1</Auction>
               <Price>41.00</Price>
               <Volume>2.2</Volume>
            </Item>
         </Result>
      </GetIDAPricePeriodEResponse>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

1.3.3.4.  GetIDAAllE

Služba poskytuje výsledné marginální ceny a zobchodované množství a realizované Importy, Exporty
včetně Salda pro zvolené období a IDA aukci v 60 min rozlišení.

Služba poskytuje data pro dny dodávky od 14.6.2024 do 30.6.2024.

Vstupní parametry:

Struktura dotazu GetIDAAllE:

Element

Hodnota

Poznámka

Povinná
Nepovinná

/

StartDate

Datum

Počáteční den dodávky období, za které jsou požadovaná
data.

Povinná

Formát YYYY-MM-DD.

EndDate

Datum

Koncový den dodávky období, za které jsou požadovaná
data.

Povinná

Formát YYYY-MM-DD.

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

Element

Hodnota

Poznámka

StartHour

Celé kladné číslo

EndHour

Celé kladné číslo

Index počáteční hodinové periody rozsahu hodinových
period daného dne dodávky, za které jsou požadovaná
data. Může nabývat hodnot 1 až 25. (viz kap. 1.4.1 Služby
se zadáním hodiny).

Index koncové hodinové periody rozsahu hodinových
period daného dne dodávky, za které jsou požadovaná
data. Může nabývat hodnot 1 až 25. (viz kap. 1.4.1 Služby
se zadáním hodiny).

Auction

InEur

IDA1, IDA2, IDA3

Typ IDA aukce

Boolean

Je-li nastaveno (true), vrací cenu v EUR, jinak v Kč. Cena
v Kč se přepočítává podle kurzu ČNB.

Struktura odpovědi GetIDAAllEResponse:

Element

Hodnota

Poznámka

Date

Hour

Datum

Den dodávky. Formát YYYY-MM-DD.

Celé kladné číslo

Index hodiny příslušného dne dodávky

PriceCZ

Desetinné číslo

Marginální cena v [Kč/MWh] nebo v [EUR/MWh] v CZ
oblasti dodávky.

Hodnota s přesností na 2 desetinná místa.

25

Povinná
Nepovinná

/

Nepovinná

Nepovinná

Povinná

Nepovinná

Povinná
Nepovinná

/

Povinná

Povinná

Povinná

VolumeCZ

Desetinné číslo

Celkové zobchodované množství za ČR [MWh] v dané
hodině dodávky.

Povinná

Hodnota s přesností na 1 desetinné místo.

ImportCZ

Desetinné číslo

Celková výše importu v CZ oblasti v MW.

Povinná

Hodnota s přesností na 1 desetinné místo.

ExportCZ

Desetinné číslo

Celková výše exportu v CZ oblasti v MW.

Povinná

Hodnota s přesností na 1 desetinné místo.

SaldoCZ

Desetinné číslo

Celková výše salda v CZ oblasti v MW.

Povinná

Hodnota s přesností na 1 desetinné místo.

Emerg

Celé kladné číslo

Příznak stavu nouze.

Nepovinná

•

Hodnota:1 – Byl vyhlášen stav nouze.

Pozn.: Oddělovačem desetinných mís je tečka.

Příklad dotazu GetIDAAllE:

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:pub="http://www.ote-
cr.cz/schema/service/public">
   <soapenv:Header/>
   <soapenv:Body>
      <pub:GetIDAAllE>
         <pub:StartDate>2024-06-25</pub:StartDate>
         <pub:EndDate>2024-06-25</pub:EndDate>
         <!--Optional:-->
         <pub:StartHour>1</pub:StartHour>
         <!--Optional:-->
         <pub:EndHour>3</pub:EndHour>
         <pub:Auction>IDA1</pub:Auction>
         <!--Optional:-->
         <pub:InEur>true</pub:InEur>

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

26

      </pub:GetIDAAllE>
   </soapenv:Body>
</soapenv:Envelope>

Příklad odpovědi GetIDAAllEResponse:

<SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-
ENV="http://schemas.xmlsoap.org/soap/envelope/">
   <SOAP-ENV:Body>
      <GetIDAAllEResponse xmlns="http://www.ote-cr.cz/schema/service/public">
         <Result>
            <Item>
               <Date>2024-06-25</Date>
               <Hour>1</Hour>
               <PriceCZ>90.80</PriceCZ>
               <VolumeCZ>50.0</VolumeCZ>
               <ImportCZ>0.0</ImportCZ>
               <ExportCZ>49.9</ExportCZ>
               <SaldoCZ>49.9</SaldoCZ>
            </Item>
            <Item>
               <Date>2024-06-25</Date>
               <Hour>2</Hour>
               <PriceCZ>88.75</PriceCZ>
               <VolumeCZ>100.1</VolumeCZ>
               <ImportCZ>0.0</ImportCZ>
               <ExportCZ>100.1</ExportCZ>
               <SaldoCZ>100.1</SaldoCZ>
            </Item>
            <Item>
               <Date>2024-06-25</Date>
               <Hour>3</Hour>
               <PriceCZ>84.80</PriceCZ>
               <VolumeCZ>15.0</VolumeCZ>
               <ImportCZ>-15.0</ImportCZ>
               <ExportCZ>0.0</ExportCZ>
               <SaldoCZ>-15.0</SaldoCZ>
            </Item>
         </Result>
      </GetIDAAllEResponse>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

1.3.3.5.  GetIDAAllPeriodE

Služba poskytuje výsledné marginální ceny a zobchodované množství a realizované Importy, Exporty
včetně Salda pro zvolené období a IDA aukci v 15/60 min rozlišení (dle rozlišení dodávky).

Služba poskytuje data ode dne dodávky 14.6.2024.

Struktura dotazu GetIDAAllPeriodE:

Element

Hodnota

Poznámka

Povinná
Nepovinná

/

StartDate

Datum

Počáteční den dodávky období, za které jsou požadovaná
data.

Povinná

Formát YYYY-MM-DD.

EndDate

Datum

Koncový den dodávky období, za které jsou požadovaná
data.

Povinná

StartPeriod

Celé kladné číslo

Formát YYYY-MM-DD.

Počáteční index periody rozsahu period dodávky daného
rozlišení a v daném dni dodávky, za které jsou
požadovaná data. Může nabývat hodnot:

Nepovinná

•

1 až 25, v případě dne dodávky s hodinovým
rozlišením periody

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

Element

Hodnota

Poznámka

1 až 100, v případě dne dodávky s čtvrthodinovým
rozlišením periody Viz kap. 1.4 Omezení vrácených hodnot
při specifikování hodiny či periody.

27

Povinná
Nepovinná

/

EndPeriod

Celé kladné číslo

Index koncové periody rozsahu period dodávky daného
rozlišení v daném dni dodávky, za které jsou požadovaná
data. Může nabývat hodnot:

Nepovinná

•

•

1 až 25, v případě dne dodávky s hodinovým
rozlišením periody

1 až 100, v případě dne dodávky
s čtvrthodinovým rozlišením periody

Viz kap. 1.4 Omezení vrácených hodnot při specifikování
hodiny či periody.

Auction

InEur

IDA1, IDA2, IDA3

Typ IDA aukce

Boolean

Je-li nastaveno (true), vrací cenu v EUR, jinak v Kč. Cena
v Kč se přepočítává podle kurzu ČNB.

Struktura odpovědi GetIDAPricePeriodEResponse:

Element

Hodnota

Poznámka

Date

Datum

Den dodávky. Formát YYYY-MM-DD.

PeriodResolution

Textový řetězec

Rozlišení periody dodávky, ve kterém jsou data
poskytována:

•

•

PT15M – 15min rozlišení

PT60M – 60min rozlišení

Povinná

Nepovinná

Povinná
Nepovinná

/

Povinná

Povinná

PeriodIndex

Celé kladné číslo

Index periody příslušného dne dodávky. Může nabývat
hodnot:

Povinná

•

•

1 až 100, v případě PeriodResolution = PT15M

1 až 25, v případě PeriodResolutio n= PT60M

PeriodInterval

Textový řetězec

Interval periody příslušného dne dodávky ve formátu:

Povinná

•

•

HH24:MI-HH24:MI, v případě PeriodResolution
= PT15M

HH24-HH24, v případě PeriodResolution =
PT60M

Auction

PriceCZ

IDA1, IDA2, IDA3

Typ IDA aukce

Desetinné číslo

Marginální cena v [Kč/MWh] nebo v [EUR/MWh] v CZ
oblasti dodávky.

Hodnota s přesností na 2 desetinná místa.

Povinná

Povinná

VolumeCZ

Desetinné číslo

Celkové zobchodované množství za ČR [MWh] v dané
hodině dodávky.

Povinná

Hodnota s přesností na 1 desetinné místo.

ImportCZ

Desetinné číslo

Celková výše importu v CZ oblasti v MWh.

Povinná

Hodnota s přesností na 1 desetinné místo.

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

Element

Hodnota

Poznámka

28

Povinná
Nepovinná

/

ExportCZ

Desetinné číslo

Celková výše exportu v CZ oblasti v MWh.

Povinná

Hodnota s přesností na 1 desetinné místo.

SaldoCZ

Desetinné číslo

Celková výše salda v CZ oblasti v MWh.

Hodnota s přesností na 1 desetinné místo.

Emerg

Celé kladné číslo

Příznak stavu nouze.

Nepovinná

•

Hodnota:1 – Byl vyhlášen stav nouze.

Pozn.: Oddělovačem desetinných mís je tečka.

Příklad dotazu GetIDAAllPeriodE:

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:pub="http://www.ote-
cr.cz/schema/service/public">
   <soapenv:Header/>
   <soapenv:Body>
      <pub:GetIDAAllPeriodE>
         <pub:StartDate>2024-07-02</pub:StartDate>
         <pub:EndDate>2024-07-02</pub:EndDate>
         <!--Optional:-->
         <pub:StartPeriod>1</pub:StartPeriod>
         <!--Optional:-->
         <pub:EndPeriod>3</pub:EndPeriod>
         <pub:Auction>IDA1</pub:Auction>
         <!--Optional:-->
         <pub:InEur>true</pub:InEur>
      </pub:GetIDAAllPeriodE>
   </soapenv:Body>
</soapenv:Envelope>

Příklad odpovědi GetIDAAllPeriodEResponse:

<SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-
ENV="http://schemas.xmlsoap.org/soap/envelope/">
   <SOAP-ENV:Body>
      <GetIDAAllPeriodEResponse xmlns="http://www.ote-cr.cz/schema/service/public">
         <Result>
            <Item>
               <Date>2024-07-02</Date>
               <PeriodResolution>PT15M</PeriodResolution>
               <PeriodIndex>1</PeriodIndex>
               <PeriodInterval>00:00-00:15</PeriodInterval>
               <Auction>IDA1</Auction>
               <PriceCZ>115.56</PriceCZ>
               <VolumeCZ>2.6</VolumeCZ>
               <ImportCZ>-0.5</ImportCZ>
               <ExportCZ>0.2</ExportCZ>
               <SaldoCZ>-0.3</SaldoCZ>
            </Item>
            <Item>
               <Date>2024-07-02</Date>
               <PeriodResolution>PT15M</PeriodResolution>
               <PeriodIndex>2</PeriodIndex>
               <PeriodInterval>00:15-00:30</PeriodInterval>
               <Auction>IDA1</Auction>
               <PriceCZ>40.00</PriceCZ>
               <VolumeCZ>1.9</VolumeCZ>
               <ImportCZ>0.0</ImportCZ>
               <ExportCZ>1.7</ExportCZ>
               <SaldoCZ>1.7</SaldoCZ>
            </Item>
            <Item>
               <Date>2024-07-02</Date>
               <PeriodResolution>PT15M</PeriodResolution>
               <PeriodIndex>3</PeriodIndex>
               <PeriodInterval>00:30-00:45</PeriodInterval>
               <Auction>IDA1</Auction>

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

29

               <PriceCZ>41.00</PriceCZ>
               <VolumeCZ>2.2</VolumeCZ>
               <ImportCZ>0.0</ImportCZ>
               <ExportCZ>1.7</ExportCZ>
               <SaldoCZ>1.7</SaldoCZ>
            </Item>
         </Result>
      </GetIDAAllPeriodEResponse>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

1.3.4.  Webové služby pro Vnitrodenní trh s elektřinou

1.3.4.1.  GetImPriceE

Služba poskytuje pro zvolené období dodávky zobchodované množství a vážený průměr cen na VDT
s elektřinou standardních hodinových kontraktů (v 60 min rozlišení dne dodávky).

Služba poskytuje data do dne dodávky 30.6.2024.

Struktura dotazu GetImPriceE:

Element

Hodnota

Poznámka

Povinná
Nepovinná

/

StartDate

Datum

Počáteční den dodávky období, za které jsou požadovaná
data.

Povinná

Formát YYYY-MM-DD.

EndDate

Datum

Koncový den dodávky období, za které jsou požadovaná
data.

Povinná

StartHour

Celé kladné číslo

EndHour

Celé kladné číslo

Formát YYYY-MM-DD.

Index počáteční hodinové periody rozsahu hodinových
period daného dne dodávky, za které jsou požadovaná
data. Může nabývat hodnot 1 až 25. (viz kap. 1.4.1 Služby
se zadáním hodiny).

Index koncové hodinové periody rozsahu hodinových
period daného dne dodávky, za které jsou požadovaná
data. Může nabývat hodnot 1 až 25. (viz kap. 1.4.1 Služby
se zadáním hodiny).

Nepovinná

Nepovinná

Struktura odpovědi GetImPriceEResponse:

Element

Hodnota

Poznámka

Date

Hour

Price

Datum

Den dodávky. Formát YYYY-MM-DD.

Celé kladné číslo

Index hodiny příslušného dne dodávky

Desetinné číslo

Vážený průměr cen na VDT v [EUR/MWh] v dané hodině
dodávky.

Hodnota s přesností na 2 desetinná místa.

Povinná
Nepovinná

/

Povinná

Povinná

Povinná

Volume

Desetinné číslo

Celkové zobchodované množství na VDT [MWh] v dané
hodině dodávky.

Povinná

Hodnota s přesností na 1 desetinné místo.

Emerg

Celé kladné číslo

Příznak stavu nouze.

Nepovinná

•

Hodnota:1 – Byl vyhlášen stav nouze.

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

30

Pozn.: Oddělovačem desetinných mís je tečka.

Příklad dotazu GetImPriceE:

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:pub="http://www.ote-
cr.cz/schema/service/public">
   <soapenv:Header/>
   <soapenv:Body>
      <pub:GetImPriceE>
         <pub:StartDate>2024-06-28</pub:StartDate>
         <pub:EndDate>2024-06-28</pub:EndDate>
         <!--Optional:-->
         <pub:StartHour>1</pub:StartHour>
         <!--Optional:-->
         <pub:EndHour>3</pub:EndHour>
      </pub:GetImPriceE>
   </soapenv:Body>
</soapenv:Envelope>

Příklad odpovědi GetImPriceEResponse:

<SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-
ENV="http://schemas.xmlsoap.org/soap/envelope/">
   <SOAP-ENV:Body>
      <GetImPriceEResponse xmlns="http://www.ote-cr.cz/schema/service/public">
         <Result>
            <Item>
               <Date>2024-06-28</Date>
               <Hour>1</Hour>
               <Price>101.79</Price>
               <Volume>481.8</Volume>
            </Item>
            <Item>
               <Date>2024-06-28</Date>
               <Hour>2</Hour>
               <Price>95.13</Price>
               <Volume>402.5</Volume>
            </Item>
            <Item>
               <Date>2024-06-28</Date>
               <Hour>3</Hour>
               <Price>97.30</Price>
               <Volume>272.5</Volume>
            </Item>
         </Result>
      </GetImPriceEResponse>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

1.3.4.2.  GetImPricePeriodE

Služba poskytuje pro zvolené období dodávky zobchodované množství a vážený průměr cen na VDT
s elektřinou standardních 15 min a 60 min kontraktů (v nejmenším rozlišení daného dne dodávky).

Struktura dotazu GetImPricePeriodE:

Element

Hodnota

Poznámka

Povinná
Nepovinná

/

StartDate

Datum

Počáteční den dodávky období, za které jsou požadovaná
data.

Povinná

Formát YYYY-MM-DD.

EndDate

Datum

Koncový den dodávky období, za které jsou požadovaná
data.

Povinná

StartPeriod

Celé kladné číslo

Formát YYYY-MM-DD.

Počáteční index periody rozsahu period dodávky daného
rozlišení a v daném dni dodávky, za které jsou
požadovaná data. Může nabývat hodnot:

Nepovinná

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

Element

Hodnota

Poznámka

•

•

1 až 25, v případě dne dodávky s 60min
nejmenším rozlišením

1 až 100, v případě dne dodávky s 15min
nejmenším rozlišením

Viz kap. 1.4 Omezení vrácených hodnot při specifikování
hodiny či periody.

31

Povinná
Nepovinná

/

EndPeriod

Celé kladné číslo

Index koncové periody rozsahu period dodávky daného
rozlišení v daném dni dodávky, za které jsou požadovaná
data. Může nabývat hodnot:

Nepovinná

•

•

1 až 25, v případě dne dodávky s 60min
nejmenším rozlišením

1 až 100, v případě dne dodávky s 15min
nejmenším rozlišením

Viz kap. 1.4 Omezení vrácených hodnot při specifikování
hodiny či periody.

Struktura odpovědi GetImPricePeriodEResponse:

Element

Hodnota

Poznámka

Date

Datum

Den dodávky. Formát YYYY-MM-DD.

PeriodResolution

Textový řetězec

Rozlišení periody dodávky, ve kterém jsou data
poskytována (odpovídá nejmenšímu rozlišení daného dne
dodávky):

•

•

PT15M – 15min rozlišení

PT60M – 60min rozlišení

Povinná
Nepovinná

/

Povinná

Povinná

PeriodIndex

Celé kladné číslo

Index periody příslušného dne dodávky. Může nabývat
hodnot:

Povinná

•

•

1 až 100, v případě PeriodResolution = PT15M

1 až 25, v případě PeriodResolution= PT60M

Price

Desetinné číslo

Vážený průměr cen na VDT v [EUR/MWh] v dané periodě
dodávky.

Povinná

Hodnota s přesností na 2 desetinná místa.

Volume

Desetinné číslo

Celkové zobchodované množství na VDT [MWh] v dané
periodě dodávky.

Povinná

Hodnota s přesností na 3 desetinná místa.

Emerg

Celé kladné číslo

Příznak stavu nouze.

Nepovinná

•

Hodnota:1 – Byl vyhlášen stav nouze.

Pozn.: Oddělovačem desetinných mís je tečka.

Příklad dotazu GetImPricePeriodE:

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:pub="http://www.ote-
cr.cz/schema/service/public">
   <soapenv:Header/>
   <soapenv:Body>
      <pub:GetImPricePeriodE>
         <pub:StartDate>2024-07-01</pub:StartDate>
         <pub:EndDate>2024-07-01</pub:EndDate>
         <!--Optional:-->
         <pub:StartPeriod>1</pub:StartPeriod>
         <!--Optional:-->

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

32

         <pub:EndPeriod>3</pub:EndPeriod>
      </pub:GetImPricePeriodE>
   </soapenv:Body>
</soapenv:Envelope>

Příklad odpovědi GetImPricePeriodEResponse:

<SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-
ENV="http://schemas.xmlsoap.org/soap/envelope/">
   <SOAP-ENV:Body>
      <GetImPricePeriodEResponse xmlns="http://www.ote-cr.cz/schema/service/public">
         <Result>
            <Item>
               <Date>2024-07-01</Date>
               <PeriodResolution>PT15M</PeriodResolution>
               <PeriodIndex>1</PeriodIndex>
               <Price>95.30</Price>
               <Volume>62.221</Volume>
            </Item>
            <Item>
               <Date>2024-07-01</Date>
               <PeriodResolution>PT15M</PeriodResolution>
               <PeriodIndex>2</PeriodIndex>
               <Price>94.56</Price>
               <Volume>86.621</Volume>
            </Item>
            <Item>
               <Date>2024-07-01</Date>
               <PeriodResolution>PT15M</PeriodResolution>
               <PeriodIndex>3</PeriodIndex>
               <Price>87.35</Price>
               <Volume>73.121</Volume>
            </Item>
         </Result>
      </GetImPricePeriodEResponse>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

1.3.5.  Webové služby pro Odchylky – elektřina

1.3.5.1.  GetImbalanceSettlementE

Služba poskytuje pro zvolené období dodávky a verzi zúčtování hodinové výsledky zúčtování odchylek
s elektřinou.

Služba poskytuje data do dne dodávky 30.6.2024.

Struktura dotazu GetImbalanceSettlementE:

Element

Hodnota

Poznámka

Version

Celé číslo

Verze zúčtování:

Povinná
Nepovinná

/

Povinná

•

•

•

0 – Denní zúčtování odchylek

1 – Měsíční zúčtování odchylek

2 – Závěrečné měsíční zúčtování odchylek

StartDate

Datum

Počáteční den dodávky období, za které jsou požadovaná
data.

Povinná

Formát YYYY-MM-DD.

EndDate

Datum

Koncový den dodávky období, za které jsou požadovaná
data.

Povinná

Formát YYYY-MM-DD.

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

Element

Hodnota

Poznámka

StartHour

Celé kladné číslo

Index počáteční hodinové periody rozsahu hodinových
period daného dne dodávky, za které jsou požadovaná
data. Může nabývat hodnot 1 až 25. (viz kap. 1.4.1 Služby
se zadáním hodiny).

33

Povinná
Nepovinná

/

Nepovinná

EndHour

Celé kladné číslo

Index koncové hodinové periody rozsahu hodinových
period daného dne dodávky, za které jsou požadovaná
data. Může nabývat hodnot 1 až 25. (viz kap. 1.4.1 Služby
se zadáním hodiny).

Nepovinná

Struktura odpovědi GetImbalanceSettlementEResponse:

Element

Hodnota

Poznámka

Version

Celé číslo

Verze zúčtování:

•

•

•

0 – Denní zúčtování odchylek

1 – Měsíční zúčtování odchylek

2 – Závěrečné měsíční zúčtování odchylek

Date

Hour

Datum

Den dodávky. Formát YYYY-MM-DD.

Celé kladné číslo

Index hodiny příslušného dne dodávky.

SystemImbalance

Desetinné číslo

Systémová odchylka [MWh].

Hodnota s přesností na 3 desetinná místa.

Sum

Desetinné číslo

Součet absolutních odchylek [MWh].

Hodnota s přesností na 3 desetinná místa.

PositiveImbalance

Desetinné číslo

Kladné odchylky [MWh].

Hodnota s přesností na 3 desetinná místa.

NegativeImbalance

Desetinné číslo

Záporné odchylky [MWh].

Hodnota s přesností na 3 desetinná místa.

RoundedImbalance

Desetinné číslo

Zaokrouhlení odchylek [MWh].

Hodnota s přesností na 3 desetinná místa.

ReCost

Desetinné číslo

Náklady na RE [Kč].

Hodnota s přesností na 2 desetinná místa.

ImbalanceCost

Desetinné číslo

Náklady na odchylku [Kč].

Hodnota s přesností na 2 desetinná místa.

SettlImbalancePrice

Desetinné číslo

Zúčtovací cena odchylky [Kč/MWh].

Hodnota s přesností na 2 desetinná místa.

Povinná
/
Nepovinná

Povinná

Povinná

Povinná

Povinná

Povinná

Povinná

Povinná

Povinná

Povinná

Povinná

Povinná

SettlCounterImbalancePrice  Desetinné číslo

Zúčtovací cena protiodchylky [Kč/MWh].

Povinná

Hodnota s přesností na 2 desetinná místa.

Emerg

Celé kladné číslo

Příznak stavu nouze.

Nepovinná

•

Hodnota:1 – Byl vyhlášen stav nouze.

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

Element

Hodnota

Poznámka

PriceWARE

Desetinné číslo

Cena dle váženého průměru nákladů na RE [Kč/MWh].

Hodnota s přesností na 2 desetinná místa.

34

Povinná
/
Nepovinná

Nepovinná

PriceRE

Desetinné číslo

Cena dle dodané RE proti směru SO [Kč/MWh].

Nepovinná

Hodnota s přesností na 2 desetinná místa.

PriceWAIM

Desetinné číslo

Cena dle váženého průměru cen obchodů na VDT
[Kč/MWh].

Nepovinná

Hodnota s přesností na 2 desetinná místa.

PriceCurve

Desetinné číslo

Cena dle křivky (základní směrnice SO) [Kč/MWh].

Nepovinná

Hodnota s přesností na 2 desetinná místa.

Pozn.: Oddělovačem desetinných mís je tečka.

Příklad dotazu GetImbalanceSettlementE:

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:pub="http://www.ote-
cr.cz/schema/service/public">
   <soapenv:Header/>
   <soapenv:Body>
      <pub:GetImbalanceSettlementE>
         <pub:Version>0</pub:Version>
         <pub:StartDate>2024-06-30</pub:StartDate>
         <pub:EndDate>2024-07-30</pub:EndDate>
         <!--Optional:-->
         <pub:StartHour>1</pub:StartHour>
         <!--Optional:-->
         <pub:EndHour>2</pub:EndHour>
      </pub:GetImbalanceSettlementE>
   </soapenv:Body>
</soapenv:Envelope>

Příklad odpovědi GetImbalanceSettlementEResponse:

<SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-
ENV="http://schemas.xmlsoap.org/soap/envelope/">
   <SOAP-ENV:Body>
      <GetImbalanceSettlementEResponse xmlns="http://www.ote-cr.cz/schema/service/public">
         <Result>
            <Item>
               <Version>0</Version>
               <Date>2024-06-30</Date>
               <Hour>1</Hour>
               <SystemImbalance>-63.074</SystemImbalance>
               <Sum>168.196</Sum>
               <PositiveImbalance>52.561</PositiveImbalance>
               <NegativeImbalance>-115.635</NegativeImbalance>
               <RoundedImbalance>-0.121</RoundedImbalance>
               <ReCost>549396.010</ReCost>
               <ImbalanceCost>-860601.350</ImbalanceCost>
               <SettlImbalancePrice>10261.780</SettlImbalancePrice>
               <SettlCounterImbalancePrice>6202.690</SettlCounterImbalancePrice>
               <PriceWARE>7570.50</PriceWARE>
               <PriceRE>9914.88</PriceRE>
               <PriceWAIM>2029.12</PriceWAIM>
               <PriceCurve>10261.78</PriceCurve>
            </Item>
            <Item>
               <Version>0</Version>
               <Date>2024-06-30</Date>
               <Hour>2</Hour>
               <SystemImbalance>-98.892</SystemImbalance>
               <Sum>194.160</Sum>
               <PositiveImbalance>47.634</PositiveImbalance>
               <NegativeImbalance>-146.526</NegativeImbalance>
               <RoundedImbalance>-0.121</RoundedImbalance>

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

35

               <ReCost>262301.830</ReCost>
               <ImbalanceCost>-1009678.760</ImbalanceCost>
               <SettlImbalancePrice>7793.340</SettlImbalancePrice>
               <SettlCounterImbalancePrice>2776.340</SettlCounterImbalancePrice>
               <PriceWARE>2692.69</PriceWARE>
               <PriceRE>7249.44</PriceRE>
               <PriceWAIM>1725.96</PriceWAIM>
               <PriceCurve>7793.34</PriceCurve>
            </Item>
         </Result>
      </GetImbalanceSettlementEResponse>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

1.3.5.2.  GetImbalanceSettlementPeriodE

Služba  poskytuje  pro  zvolené  období  dodávky  a  verzi  zúčtování  výsledky  zúčtování  odchylek
s elektřinou v 15/60 minutových periodách (dle zúčtovací periody daného dne dodávky).

Struktura dotazu GetImbalanceSettlementPeriodE:

Element

Hodnota

Poznámka

Version

Celé číslo

Verze zúčtování:

Povinná
Nepovinná

/

Povinná

•

•

•

0 – Denní zúčtování odchylek

1 – Měsíční zúčtování odchylek

2 – Závěrečné měsíční zúčtování odchylek

StartDate

Datum

Počáteční den dodávky období, za které jsou požadovaná
data.

Povinná

Formát YYYY-MM-DD.

EndDate

Datum

Koncový den dodávky období, za které jsou požadovaná
data.

Povinná

Formát YYYY-MM-DD.

StartPeriod

Celé kladné číslo

Počáteční index periody rozsahu period dodávky daného
rozlišení a v daném dni dodávky, za které jsou
požadovaná data. Může nabývat hodnot:

Nepovinná

•

•

1 až 25, v případě dne dodávky s 60min
zúčtovací periodou

1 až 100, v případě dne dodávky s 15min
zúčtovací periodou

Viz kap. 1.4 Omezení vrácených hodnot při specifikování
hodiny či periody.

EndPeriod

Celé kladné číslo

Index koncové periody rozsahu period dodávky daného
rozlišení v daném dni dodávky, za které jsou požadovaná
data. Může nabývat hodnot:

Nepovinná

•

•

1 až 25, v případě dne dodávky s 60min
zúčtovací periodou

1 až 100, v případě dne dodávky s 15min
zúčtovací periodou

Viz kap. 1.4 Omezení vrácených hodnot při specifikování
hodiny či periody.

Struktura odpovědi GetImbalanceSettlementPeriodEResponse:

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

Element

Hodnota

Poznámka

Date

Datum

Den dodávky. Formát YYYY-MM-DD.

PeriodResolution

Textový řetězec

Rozlišení periody dodávky, ve kterém jsou data
poskytována (odpovídá zúčtovací periodě daného dne
dodávky

•

•

PT15M – 15min rozlišení

PT60M – 60min rozlišení

36

Povinná
/
Nepovinná

Povinná

Povinná

PeriodIndex

Celé kladné číslo

Index periody příslušného dne dodávky. Může nabývat
hodnot:

Povinná

•

•

1 až 100, v případě PeriodResolution =
PT15M

1 až 25, v případě PeriodResolutio n= PT60M

SystemImbalance

Desetinné číslo

Systémová odchylka [MWh].

Hodnota s přesností na 5 desetinných míst.

Sum

Desetinné číslo

Součet absolutních odchylek [MWh].

Hodnota s přesností na 5 desetinných míst.

PositiveImbalance

Desetinné číslo

Kladné odchylky [MWh].

Hodnota s přesností na 5 desetinných míst..

NegativeImbalance

Desetinné číslo

Záporné odchylky [MWh].

Hodnota s přesností na 5 desetinných míst.

RoundedImbalance

Desetinné číslo

Zaokrouhlení odchylek [MWh].

Hodnota s přesností na 5 desetinných míst.

ReCost

Desetinné číslo

Náklady na RE [Kč].

Hodnota s přesností na 2 desetinná místa.

ImbalanceCost

Desetinné číslo

Náklady na odchylku [Kč].

Hodnota s přesností na 2 desetinná místa.

SettlImbalancePrice

Desetinné číslo

Zúčtovací cena odchylky [Kč/MWh].

Hodnota s přesností na 2 desetinná místa.

Povinná

Povinná

Povinná

Povinná

Povinná

Povinná

Povinná

Povinná

SettlCounterImbalancePrice  Desetinné číslo

Zúčtovací cena protiodchylky [Kč/MWh].

Povinná

Hodnota s přesností na 2 desetinná místa.

Emerg

Celé kladné číslo

Příznak stavu nouze.

Nepovinná

•

Hodnota:1 – Byl vyhlášen stav nouze.

PriceWARE

Desetinné číslo

Cena dle váženého průměru nákladů na RE [Kč/MWh].

Nepovinná

Hodnota s přesností na 2 desetinná místa.

PriceRE

Desetinné číslo

Cena dle dodané RE proti směru SO [Kč/MWh].

Nepovinná

Hodnota s přesností na 2 desetinná místa.

PriceWAIM

Desetinné číslo

Cena dle váženého průměru cen obchodů na VDT
[Kč/MWh].

Nepovinná

Hodnota s přesností na 2 desetinná místa.

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

37

Povinná
/
Nepovinná

Nepovinná

Element

Hodnota

Poznámka

PriceCurve

Desetinné číslo

Cena dle křivky (základní směrnice SO) [Kč/MWh].

Hodnota s přesností na 2 desetinná místa.

Pozn.: Oddělovačem desetinných mís je tečka.

Příklad dotazu GetImbalanceSettlementPeriodE:

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:pub="http://www.ote-
cr.cz/schema/service/public">
   <soapenv:Header/>
   <soapenv:Body>
      <pub:GetImbalanceSettlementPeriodE>
         <pub:Version>0</pub:Version>
         <pub:StartDate>2024-08-08</pub:StartDate>
         <pub:EndDate>2024-08-08</pub:EndDate>
         <!--Optional:-->
         <pub:StartPeriod>1</pub:StartPeriod>
         <!--Optional:-->
         <pub:EndPeriod>2</pub:EndPeriod>
      </pub:GetImbalanceSettlementPeriodE>
   </soapenv:Body>
</soapenv:Envelope>

Příklad odpovědi GetImbalanceSettlementPeriodEResponse:

<SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-
ENV="http://schemas.xmlsoap.org/soap/envelope/">
   <SOAP-ENV:Body>
      <GetImbalanceSettlementPeriodEResponse xmlns="http://www.ote-cr.cz/schema/service/public">
         <Result>
            <Item>
               <Version>0</Version>
               <Date>2024-08-08</Date>
               <PeriodResolution>PT15M</PeriodResolution>
               <PeriodIndex>1</PeriodIndex>
               <SystemImbalance>-51.48865</SystemImbalance>
               <Sum>98.43749</Sum>
               <PositiveImbalance>23.47442</PositiveImbalance>
               <NegativeImbalance>-74.96307</NegativeImbalance>
               <RoundedImbalance>-0.00035</RoundedImbalance>
               <ReCost>1730404.910</ReCost>
               <ImbalanceCost>-1730404.800</ImbalanceCost>
               <SettlImbalancePrice>33607.500</SettlImbalancePrice>
               <SettlCounterImbalancePrice>33607.500</SettlCounterImbalancePrice>
               <PriceWARE>33607.50</PriceWARE>
               <PriceRE>38025.29</PriceRE>
               <PriceWAIM>2933.13</PriceWAIM>
               <PriceCurve>38308.47</PriceCurve>
            </Item>
            <Item>
               <Version>0</Version>
               <Date>2024-08-08</Date>
               <PeriodResolution>PT15M</PeriodResolution>
               <PeriodIndex>2</PeriodIndex>
               <SystemImbalance>6.60323</SystemImbalance>
               <Sum>27.78885</Sum>
               <PositiveImbalance>17.19604</PositiveImbalance>
               <NegativeImbalance>-10.59281</NegativeImbalance>
               <RoundedImbalance>-0.00023</RoundedImbalance>
               <ReCost>-14118.690</ReCost>
               <ImbalanceCost>17294.260</ImbalanceCost>
               <SettlImbalancePrice>2619.060</SettlImbalancePrice>
               <SettlCounterImbalancePrice>2619.060</SettlCounterImbalancePrice>
               <PriceWARE>2138.14</PriceWARE>
               <PriceRE>3224.45</PriceRE>
               <PriceWAIM>2619.06</PriceWAIM>
               <PriceCurve>3201.33</PriceCurve>
            </Item>
         </Result>
      </GetImbalanceSettlementPeriodEResponse>

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

38

   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

1.3.6.  Webové služby pro Vnitrodenní trh s plynem

1.3.6.1.  GetImPriceG

Služba poskytuje pro zvolené období dodávky zobchodované množství a vážený průměr cen na VDT
s plynem, včetně min/max ceny a indexu OTE.

Struktura dotazu GetImPriceG:

Element

Hodnota

Poznámka

Povinná
Nepovinná

/

StartDate

Datum

Počáteční den dodávky období, za které jsou požadovaná
data.

Povinná

Formát YYYY-MM-DD.

EndDate

Datum

Koncový den dodávky období, za které jsou požadovaná
data.

Povinná

Formát YYYY-MM-DD.

Struktura odpovědi GetImPriceEResponse:

Element

Hodnota

Poznámka

Povinná
Nepovinná

/

Date

Price

Datum

Plynárenský den dodávky. Formát YYYY-MM-DD.

Povinná

Desetinné číslo

Vážený průměr cen na VDT s plynem v [EUR/MWh].

Povinná

Hodnota s přesností na 2 desetinná místa.

Volume

Desetinné číslo

Celkové zobchodované množství na VDT s plynem [MWh].

Povinná

Hodnota s přesností na 1 desetinné místo.

MinPrice

Desetinné číslo

Minimální cena na VDT s plynem v [EUR/MWh].

Povinná

Hodnota s přesností na 2 desetinná místa.

MaxPrice

Desetinné číslo

Maximální cena na VDT s plynem v [EUR/MWh].

Povinná

Hodnota s přesností na 2 desetinná místa.

IndexOTE

Desetinné číslo

Index OTE na VDT s plynem v [EUR/MWh].

Povinná

Hodnota s přesností na 3 desetinná místa.

Příklad dotazu GetImPriceG:

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:pub="http://www.ote-
cr.cz/schema/service/public">
   <soapenv:Header/>
   <soapenv:Body>
      <pub:GetImPriceG>
         <pub:StartDate>2024-07-18</pub:StartDate>
         <pub:EndDate>2024-07-18</pub:EndDate>
      </pub:GetImPriceG>
   </soapenv:Body>
</soapenv:Envelope>

Příklad odpovědi GetImPriceGResponse:

<SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-
ENV="http://schemas.xmlsoap.org/soap/envelope/">
   <SOAP-ENV:Body>
      <GetImPriceGResponse xmlns="http://www.ote-cr.cz/schema/service/public">

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

39

         <Result>
            <Item>
               <Date>2024-07-18</Date>
               <Price>34.84</Price>
               <Volume>21003.5</Volume>
               <MinPrice>34.35</MinPrice>
               <MaxPrice>35.18</MaxPrice>
               <IndexOte>34.838</IndexOte>
            </Item>
         </Result>
      </GetImPriceGResponse>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

1.3.7.  Webové služby pro Odchylky – plyn

1.3.7.1.  GetImbalanceNCBALSettlementG

Vrací výsledky zúčtování odchylek NCBal za plyn a pro zadané období.

Vstupní parametry:

-  Version – specifikace verze (denní – 0, měsíční – 1, závěrečné měsíční – 2)

-  StartDate – datum od

-  EndDate – datum do

Výstupem je struktura s následujícími elementy:

-  Date – datum ve formátu dle doporučení W3C (http://www.w3.org/TR/2004/REC-xmlschema-

2-20041028/datatypes.html#date)

-  Version – specifikace verze (denní – 0, měsíční – 1, závěrečné měsíční - 2)

-  SystemImbalance – systémová odchylka [MWh]

-  PositiveImbalance – kladná odchylka [MWh]

-  NegativeImbalance – záporná odchylka [MWh]

-  TransferTsDs – Přetoky z PS do DS [MWh]

-  CnbRate – kurz ČNB [Kč/EUR]

-

IndexOTE [EUR/MWh]

-  PositiveImbalancePriceCZK (CZK/MWh) – Použitelná cena pro kladné vyrovnávací množství

(Kč/MWh)

-  NegativeImbalancePriceCZK (CZK/MWh) – Použitelná cena pro záporné vyrovnávací množství

(Kč/MWh)

-  PositiveImbalancePriceEUR (EUR/MWh) – Použitelná cena pro kladné vyrovnávací množství

(EUR/MWh)

-  NegativeImbalancePriceEUR (EUR/MWh) – Použitelná cena pro záporné vyrovnávací množství

(EUR/MWh)

-  MonthBalancingGasPrice (CZK) – Měsíční vyrovnávací cena plynu (CZK)

Příklad vstupního požadavku:

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:pub="http://www.ote-
cr.cz/schema/service/public">
   <soapenv:Header/>
   <soapenv:Body>

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

40

      <pub:GetImbalanceNCBALSettlementG>
         <pub:Version>0</pub:Version>
         <pub:StartDate>2016-07-01</pub:StartDate>
         <pub:EndDate>2016-07-01</pub:EndDate>
      </pub:GetImbalanceNCBALSettlementG>
   </soapenv:Body>
</soapenv:Envelope>

Příklad odpovědi:

<SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-
ENV="http://schemas.xmlsoap.org/soap/envelope/">
   <SOAP-ENV:Body>
      <GetImbalanceNCBALSettlementGResponse xmlns="http://www.ote-cr.cz/schema/service/public">
         <Result>
            <Item>
               <Date>2016-07-01</Date>
               <Version>0</Version>
               <SystemImbalance>-13932.541</SystemImbalance>
               <PositiveImbalance>3179.884</PositiveImbalance>
               <NegativeImbalance>-17112.762</NegativeImbalance>
               <TransferTsDs>0.0</TransferTsDs>
               <CnbRate>27.025</CnbRate>
               <IndexOTE>11.55</IndexOTE>
               <PositiveImbalancePriceCZK>305.896</PositiveImbalancePriceCZK>
               <NegativeImbalancePriceCZK>316.63</NegativeImbalancePriceCZK>
               <PositiveImbalancePriceEUR>11.319</PositiveImbalancePriceEUR>
               <NegativeImbalancePriceEUR>11.716</NegativeImbalancePriceEUR>
<MonthBalancingGasPrice>234.567</MonthBalancingGasPrice>             </Item>
         </Result>
      </GetImbalanceNCBALSettlementGResponse>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

1.4

Omezení vrácených hodnot při specifikování hodiny či periody

1.4.1  Služby se zadáním hodiny

Některé služby umožňují volitelně specifikovat dolní a horní hranici rozsahu hodin společně pro
všechny dny vrácené v odpovědi. V požadavku k tomu slouží elementy StartHour a EndHour, mohou
nabývat hodnot 1 až 25. Pokud položka StartHour není uvedena, odpovídá to stavu, kdy StartHour=1.
Pokud položka EndHour není uvedena nebo její hodnota je vyšší než počet hodinových period daného
dne dodávky, index koncové hodinové periody odpovídá poslední hodinové periodě daného dne
dodávky. Pokud tyto elementy nejsou v požadavku uvedeny, v odpovědi jsou obsaženy všechny
hodnoty ve všech hodinách daného dne. Jde tedy o ekvivalent požadavku obsahující StartHour s
hodnotou 1 a EndHour s hodnotou 25. Pokud v dané hodině neexistují žádné hodnoty, není tato hodina
obsažena v odpovědi. Cílem je tak umožnit vrácení hodnot pro danou hodinu či rozsah hodin. Pokud
EndHour < StartHour, pak výsledkem dotazu je prázdná množina.

Při přechodu času ze zimního na letní, jde tedy o den pouze se 23 hodinami, lze v požadavku uvést
EndHour s hodnotou 23, 24 i 25. Služba vždy vrátí pouze hodnoty pro 23 hodin. Naopak při přechodu
času z letního na zimní, jde tedy o den s 25 hodinami, je nutné v požadavku uvést EndHour s
hodnotou 25 nebo tento element v požadavku neuvádět vůbec, pokud je požadované vrácení všech
hodnot.

Příklad vstupního požadavku pro data 1. hodinu:

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:pub="http://www.ote-
cr.cz/schema/service/public">
   <soapenv:Header/>
   <soapenv:Body>
      <pub:GetDamPriceE>
         <pub:StartDate>2024-03-30</pub:StartDate>
         <pub:EndDate>2024-03-31</pub:EndDate>
         <pub:StartHour>1</pub:StartHour>

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

41

         <pub:EndHour>1</pub:EndHour>
      </pub:GetDamPriceE>
   </soapenv:Body>
</soapenv:Envelope>

Příklad odpovědi:

<SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-
ENV="http://schemas.xmlsoap.org/soap/envelope/">
   <SOAP-ENV:Body>
      <GetDamPriceEResponse xmlns="http://www.ote-cr.cz/schema/service/public">
         <Result>
            <Item>
               <Date>2024-03-30</Date>
               <Hour>1</Hour>
               <Price>1753.64</Price>
               <Volume>2210.6</Volume>
            </Item>
            <Item>
               <Date>2024-03-31</Date>
               <Hour>1</Hour>
               <Price>1660.77</Price>
               <Volume>2363.8</Volume>
            </Item>
         </Result>
      </GetDamPriceEResponse>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

1.4.2  Služby se zadáním periody

Jde o analogii služeb se zadáním hodin, kdy lze hodnoty v odpovědi omezit na požadovanou periodu či
rozsah period. Je k tomu u některých služeb určen volitelný element StartPeriod a EndPeriod nabývající
hodnot 1 až 96. V přechodu času na letní jde o rozsah 1 až 92 a na zimní pak o rozsah 1 až 100.

Příklad vstupního požadavku pro periodu 2 a 3:

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:pub="http://www.ote-
cr.cz/schema/service/public">
   <soapenv:Header/>
   <soapenv:Body>
      <pub:GetIDAPricePeriodE>
         <pub:StartDate>2024-07-01</pub:StartDate>
         <pub:EndDate>2024-07-01</pub:EndDate>
         <pub:StartPeriod>2</pub:StartPeriod>
         <pub:EndPeriod>3</pub:EndPeriod>
         <pub:Auction>IDA1</pub:Auction>
         <pub:InEur>True</pub:InEur>
      </pub:GetIDAPricePeriodE>
   </soapenv:Body>
</soapenv:Envelope>

Příklad odpovědi:

<SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-
ENV="http://schemas.xmlsoap.org/soap/envelope/">
   <SOAP-ENV:Body>
      <GetIDAPricePeriodEResponse xmlns="http://www.ote-cr.cz/schema/service/public">
         <Result>
            <Item>
               <Date>2024-07-01</Date>
               <PeriodResolution>PT15M</PeriodResolution>
               <PeriodIndex>2</PeriodIndex>
               <PeriodInterval>00:15-00:30</PeriodInterval>
               <Auction>IDA1</Auction>
               <Price>-114.56</Price>
               <Volume>0.8</Volume>
            </Item>
            <Item>
               <Date>2024-07-01</Date>
               <PeriodResolution>PT15M</PeriodResolution>
               <PeriodIndex>3</PeriodIndex>

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

42

               <PeriodInterval>00:30-00:45</PeriodInterval>
               <Auction>IDA1</Auction>
               <Price>41.00</Price>
               <Volume>1.6</Volume>
            </Item>
         </Result>
      </GetIDAPricePeriodEResponse>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

2025 OTE, a.s.

Revize dne:
 29.4.2025

Název dokumentu:
Uživatelský manuál webové služby OTE

