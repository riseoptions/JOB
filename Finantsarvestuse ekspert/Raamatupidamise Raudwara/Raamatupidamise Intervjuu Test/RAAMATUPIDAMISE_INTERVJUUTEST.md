# RAAMATUPIDAMISE JA FINANTSANALÜÜSI TÖÖINTERVJUU TEST

**Richard Barkeri „Short Introduction to Accounting“ põhjal – praktilised juhtumid, vastused ja selgitused**

> **Eesmärk.** Kontrollida, kas kandidaat oskab majandustehinguid sisuliselt mõista, lugeda ja omavahel siduda finantsaruandeid, hinnata ettevõtte ja projekti väärtust, määrata aktsia põhjendatud väärtuse vahemikku ning märgata raamatupidamisvigu ja võimalikke pettuseriske.
>
> 
> **Alus:** Richard Barker, *Short Introduction to Accounting* (Cambridge University Press, 2011), peatükid 1–8. **Täiendused:** aktsia väärtuse hindamine, pettuseriski analüüs, andmekontroll SQL/Pythoniga ning AI kasutamine on tänapäevased tööalased laiendused, mitte raamatu eraldi peatükid.

[**Alusta testiga**](#1-testi-juhend) · [**Andmestik A**](#3-juhtum-a--ettevõte-kalev-tech-oü) · [**Andmestik B**](#4-juhtum-b--ettevõtte-ja-aktsia-hindamine) · [**Vastused ja põhjendused**](#7-vastused-ja-selgitused) · [**Hindamisjuhend**](#8-hindamine-ja-tagasiside) · [**Intervjuu lisaküsimused**](#9-suuline-intervjuu)

---

## 1. Testi juhend

**Sihtrühm:** raamatupidaja, finantsanalüütik, finantskontroller, ärianalüütik, investeerimisanalüütik või nende ametite alustav kandidaat.

- **Ülesandeid:** 44 (sh arvutused, argumentatsioon, diagnostika, hindamine ning Python/SQL-i mõtlemine).
- **Punkte:** 140 (A: 16, B: 24, C: 24, D: 40, E: 24, F: 12).
- **Soovituslik aeg:** 210 min kirjalikult + 20–30 min suuline arutelu.
- **Abivahendid:** kalkulaator või Python, pliiats, tabelarvutus; esimesel läbimisel vastuseid ega AI-abi mitte kasutada.
- **Ümardamine:** summad ühe kümnendkohani tuhande euro täpsuses, suhtarvud 1–2 kümnendkohani, aktsia hind kahe kümnendkohani.
- **Kõik summad on illustratiivsed**, kui pole öeldud teisiti. Kasumimaks ja rahavoogude klassifikatsioon on lihtsustatud; neid ei tohi otse üle kanda Eesti maksudeklaratsioonidele.

**Vastamise standard:** iga arvutuse juures märgi ① valem, ② arvutus, ③ sisuline järeldus ning vajadusel ④ alternatiivne tõlgendus või täiendav kontroll. Ainult õige number ei anna täispunkte.

**Erinevus audiitorkontrollist:** punane lipp ei ole tõend pettusest. Oskus sõnastada kontrollitav hüpotees ja vajalike tõendite loend on olulisem kui sensatsiooniline süüdistus.

## 2. Kontseptsioonikaart – mida test katab?

| Raamatu teema | Peamised oskused | Testis |
|---|---|---|
| 1. Finantsaruanded | Bilanss, kasumiaruanne, rahavood | 1–4; 11–17 |
| 2. Finantsinfo vajadus | Tekkepõhisus, kasum vs raha, hinnangud | 5–6; 12; 18; 22 |
| 3. Tehingute registreerimine | Kahekordne kirjendamine, deebet ja kreedit | 7–10 |
| 4. Arvestuse alused | Aruannete sidusus, kandest aruandeni | 9–16 |
| 5. Kasvu tõlgendamine | Käibekapital, investeeringud, finantseerimine | 16; 18; 24 |
| 6. Väärtuse loomine | Varade tootlikkus, marginaalid, kapitalikulu | 17; 19; 23; 31 |
| 7. Risk | Tegevusvõimendus, laenuvõimendus, likviidsus | 13; 20–21; 32 |
| 8. Ettevõtte väärtus | Rahavoogude prognoos, DCF, diskonteerimine | 25–32 |
| **Tänapäevased lisateemad** | Aktsia hind, pettuserisk, forensiline analüüs, automatiseerimine | 29–44 |

---

## 3. Juhtum A – ettevõte Kalev Tech OÜ

**Taust:** ettevõte müüb ja paigaldab seadmeid. Ettevõttel on olnud käibekasv, kuid juhatus kurdab, et raha ei jätku. Summad on **tuhandetes eurodes (tuh €)**. Tähelepanu: maksukulu on väljamõeldud ja sobib ainult illustratiivseks finantsanalüüsiks, mitte Eesti ettevõtte tulumaksuarvestuse näidiseks.

### Kasumiaruanne, 2026

| Kirje | 2026 (tuh €) |
|---|---:|
| Müügitulu | 1 000 |
| Müüdud kaupade kulu | −650 |
| **Brutokasum** | **350** |
| Palgad ja muud rahalised tegevuskulud | −210 |
| Kulum ja amortisatsioon | −40 |
| **Ärikasum (EBIT)** | **100** |
| Intressikulu | −25 |
| Arvestuslik maksukulu | −25 |
| **Puhaskasum** | **50** |

**Täiendav võrdlusinfo:** 2025. aasta müügitulu oli 820 tuh €, müüdud kaupade kulu 530 tuh €. 2026. aastal maksti dividendideks 20 tuh €.

### Bilanss aasta lõpus

| Kirje | 31.12.2025 | 31.12.2026 |
|---|---:|---:|
| Raha | 70 | 45 |
| Ostjate nõuded | 100 | 160 |
| Varud | 80 | 115 |
| Materiaalne põhivara (jääkmaksumus) | 250 | 280 |
| **Varad kokku** | **500** | **600** |
| Võlad tarnijatele | 90 | 135 |
| Lühiajalised intressikandvad laenud | 40 | 65 |
| Pikaajalised intressikandvad laenud | 170 | 170 |
| **Kohustised kokku** | **300** | **370** |
| **Omakapital** | **200** | **230** |
| **Kohustised + omakapital** | **500** | **600** |

### Rahavoogude lisainfo

Aastal 2026 soetati põhivara 70 tuh € eest; põhivara ei müüdud, soetused tasuti rahas, kulum oli 40 tuh €. Laenukohustis suurenes kokku 25 tuh € võrra. Eeldame lihtsuse huvides, et muid bilansikirjeid, mitterahalisi muutusi ega rahavoogude klassifitseerimise erandeid ei ole. Kasuta kaudset meetodit.

## 4. Juhtum B – ettevõtte ja aktsia hindamine

**Ettevõte:** börsiettevõte Nord Analytics AS (väljamõeldud). Kõik hindamissummad on **tuhandetes eurodes**.

- Prognoositud **vabad rahavood kogu ettevõtte kapitaliomanikele** (FCFF): 1. aastal 120, 2. aastal 140, 3. aastal 160.
- Diskontomäär **WACC = 10%**.
- Pikaajaline prognoositud kasv pärast 3. aastat **g = 3%**.
- Hetke intressikandev võlg 400; raha ja raha ekvivalendid 70.
- Aktsiaid on 100 000 ehk **100 tuhat aktsiat**.
- Aktsia turuhind on **22,00 €**.
- Eeldame, et puuduvad eraldi vähemusosalused, eelisaktsiad, olulised kasutusrendikorrigeerimised, muud mitteoperatiivsed varad ja muud ettevõtte väärtusest omakapitali väärtuseni jõudmise korrigeerimised.

**Eraldi projekt:** tarkvaraarendus nõuab kohe 30 000 €; järgmise kolme aasta lõpus loodetakse saada vastavalt 12 000 €, 14 000 € ja 16 000 € puhast rahavoogu. Projekti kapitalikulu on 10%.

---

# 5. KÜSIMUSED – KANDIDAADILE

> **Ära liigu vastuste osasse enne iseseisvat lahendamist.** Küsimused ei eelda peast õpitud definitsioonide esitamist; iga vastus peab näitama mõistmist.

## A. Raamatupidamise mõistmine (1–8; 2 p igaüks = 16 p)

**1. Kolm finantsaruannet.** Selgita ühe lausega iga aruande eesmärk. Milline aruanne on „foto kindlal kuupäeval“ ja millised kirjeldavad perioodi? Miks ei piisa ainult kasumiaruandest?

**2. Bilansi invariant.** Ettevõte ostab pangalaenuga 80 000 € maksva seadme. Mis muutub bilansis esialgsel kajastamisel? Kas ettevõte saab tehingu hetkel 80 000 € rikkamaks?

**3. Tulu versus raha.** Ettevõte osutab detsembris teenuse 20 000 € eest ja klient maksab jaanuaris. Millise kuu tuludesse see üldjuhul kuulub? Millal raha tekib ja mis juhtub nõuetega?

**4. Kulum versus väljamakse.** Masin maksab 100 000 €, kestab viis aastat ja jääkväärtus on null. Selgita lineaarsel meetodil esimese aasta kulumit, ostuaasta rahavoogu ja esimese aasta kasumiaruande mõju. Eelda täisaasta kasutamist.

**5. Müügitulu ei ole kasum.** Pood müüb kauba 1 000 € eest, soetusmaksumus oli 700 € ja muud tegevuskulud on 250 €. Kas poe kasum on 1 000 €, 300 € või 50 €? Mida peaks veel teadma?

**6. Raamatupidamislik hinnang.** Kaks ettevõtet kasutavad ühesugust vara, kuid üks amortiseerib seda 3 ja teine 6 aastaga. Kuidas see võib mõjutada kasumi ja varade võrdlemist? Kas üks neist peab petma?

**7. Deebet ja kreedit.** Kas „deebet“ tähendab alati raha väljavoolu? Nimeta üks näide, milles deebet suurendab vara, ning üks näide, milles deebet suurendab kulu.

**8. Dividend versus kulu.** Ettevõte maksab omanikele 30 000 € dividendi. Kas see vähendab majandusaasta puhaskasumit? Milliseid bilansi- ja rahavoogude kirjeid see muudab?

## B. Aruannete koostamine ja sidumine (9–16; 3 p igaüks = 24 p)

Kasuta **juhtumit A**.

**9. Kanded.** Näita deebet/kreedit järgmistele tehingutele: a) ostjale arve 10 tuh € tehtud teenuse eest; b) sama arve laekumine; c) võetakse pangalaenu 25 tuh €; d) makstakse intressi 2 tuh €. Eelda, et teenuse otsene omahind puudub.

**10. Kasum ja omakapital.** Kontrolli bilansi põhivõrrandit 2026. aasta lõpus. Miks omakapital kasvas 30 tuh €, kui puhaskasum oli 50 tuh €? Milline kande-/rahastamissündmus seletab erinevust?

**11. Ärikasum ja EBITDA.** Arvuta juhtumi A brutokasumi marginaal, ärikasumi marginaal ja EBITDA. Miks EBITDA ei võrdu ettevõtte vaba rahavooga?

**12. Rahavoogude kaudne meetod.** Arvuta 2026. aasta äritegevuse rahavoog (CFO) puhaskasumist, kulumist ja käibekapitali muutustest. Selgita, miks kasum ja CFO on erinevad.

**13. Likviidsus.** Arvuta 2026. aasta current ratio ja quick ratio. Kas nendest kahest suhtarvust piisab, et kinnitada ettevõtte maksevõime?

**14. Kolm rahavoogu.** Arvuta investeerimistegevuse rahavoog (CFI), finantseerimistegevuse rahavoog (CFF), raha netomuutus ja lõppsaldo. Kontrolli, et rahavoogude aruanne ja bilanss klapivad.

**15. Tulemuse kvaliteet.** Müügitulu kasvas 2025 → 2026. Arvuta kasvuprotsent ja CFO/puhaskasumi suhe. Sõnasta **kaks** mõistlikku, kuid erinevat selgitust, miks kasvu ajal raha väheneb.

**16. Käibekapitali tsükkel.** Kasuta *lihtsustatud aastalõpu näitajaid* (mitte keskmisi): DSO = nõuded/müügitulu × 365; DIO = varud/müüdud kaupade kulu × 365; DPO = tarnijavõlad/müüdud kaupade kulu × 365; CCC = DSO + DIO − DPO. Arvuta CCC mõlemal aastal. Mida muutus tähendab? Selgita selle ligikaudse meetodi piiratust.

## C. Finantsaruannete sisuline tõlgendamine ja risk (17–24; 3 p igaüks = 24 p)

**17. Kasumlikkuse kvaliteet.** Ettevõtte müük kasvab 20%, kuid brutomarginaal langeb 40%-lt 28%-le. Too vähemalt kolm võimalikku majanduslikku põhjust ja kaks aruannetest/algandmetest kontrollitavat näitajat.

**18. Kasum kasvab, rahavood langevad.** Võrdle kaht olukorda: a) nõuded kasvavad, sest müüakse rohkem krediiti; b) nõuded kasvavad, sest klientide maksed viibivad. Kuidas neid eristad ja miks on see investorile oluline?

**19. Varade ja omakapitali tootlikkus.** Arvuta juhtumi A 2026 ROE keskmiselt omakapitalilt ja ROA keskmistelt varadelt (kasuta puhaskasumit). Miks võib väga suur ROE olla nii hea kui ka eksitav?

**20. Tegevusvõimendus.** Tehase püsikulud on 200 000 € aastas; müügihind 100 €/tk ja muutuvkulu 60 €/tk. Arvuta kasumiläve kogus; kasum 7 000 tk müügil; kasum 5 000 tk müügil. Mida järeldad riskist?

**21. Finantsvõimendus.** Kaks ettevõtet kasutavad 500 000 € väärtuses varasid ja teenivad enne intressi 50 000 € kasumit. X-l on 100 000 € laenu (5% intress); Y-l 400 000 € laenu (5% intress). Eelda maksudeta olukorda. Arvuta kummagi ROE ja selgita, mis juhtub, kui ärikasum langeb 15 000 euroni.

**22. Allahindlus.** Laoarvestuses on kaubapartii maksumus 30 000 €, kuid selle hinnanguline netorealiseerimisväärtus on 8 000 €. Mida tuleks üldjuhul aruandes teha? Kuidas muutuvad varad, kasum ja raha? Eelda, et varu on kajastatud soetusmaksumuses.

**23. Majanduslik kasum.** Ettevõttesse investeeritud kapital on 2 miljonit €, maksujärgne ärikasum (NOPAT) 240 000 € ja WACC 9%. Arvuta ROIC ning majanduslik kasum (EVA lihtsustatud kujul). Kas ettevõte loob väärtust, kui raamatupidamislik kasum on positiivne?

**24. Kasvu rahastamine.** Müügitulu tõuseb 30%, käibekapitalivajadus ja põhivarainvesteeringud kasvavad, kuid äritegevuse rahavoog on napp. Millised **neli** realistlikku rahastamis- või juhtimisvalikut on ettevõttel? Mis on iga valiku peamine risk või kompromiss?

## D. Investeering, ettevõtte ja aktsia fundamentaalne väärtus (25–32; 5 p igaüks = 40 p)

Kasuta **juhtumit B**, kui küsimuses pole teisiti öeldud.

**25. Projekti NPV.** Arvuta projekti 30 000 € alginvesteeringu ja kolme tulevase rahavoo nüüdisväärtus 10% määraga (NPV). Kas projekt tasub oodatud andmete alusel teostamist? Mida NPV mõõdab?

**26. IRR ja otsus.** Leia sama projekti sisemine tasuvusmäär (IRR) ligikaudu. Kasuta IRR-i ja NPV-d koos. Nimeta vähemalt kaks olukorda, kus IRR võib eksitada.

**27. FCFF tähendus.** Selgita FCFF-i ja FCFE vahet. Miks tuleb juhtumi B FCFF diskonteerida WACC-iga ning miks 3. aasta rahavoost ei piisa kogu ettevõtte hindamiseks? Too FCFF-i tüüpiline koostamisvalem EBIT-ist.

**28. Ettevõtte DCF-väärtus.** Arvuta Nord Analyticsi 1.–3. aasta FCFF-ide nüüdisväärtus, 3. aasta lõpu jätkuväärtus (terminal value) Gordoni mudeliga ja ettevõtte väärtus (EV). Näita valemeid ja põhjenda eeldust WACC > g.

**29. Aktsia fundamentaalne väärtus.** Teisenda EV omakapitali väärtuseks ja leia väärtus ühe aktsia kohta. Võrdle turuhinnaga 22 €. Kas aktsia on antud eeldustel odav või kallis? Arvuta erinevus turuhinnast protsentides ja selgita hindamisvea riski.

**30. Tundlikkus ja hindamisvahemik.** Arvuta ligikaudne õiglane aktsiahind kahel alternatiivsel juhul: a) WACC = 12% ja g = 2%; b) WACC = 9% ja g = 4%. Milline osa baasstsenaariumi EV-st tuleb jätkuväärtusest? Miks ei tohiks esitada ühte hinnangut vääramatu tõena?

**31. Suhtarvuline aktsia väärtuse hinnang.** Nord Analyticsi normaliseeritud EBITDA on 300 tuh € ja võrreldavate ettevõtete põhjendatud EV/EBITDA vahemik on 5–7. Leia EV ja aktsiahinna vahemik, kasutades juhtumi B netovõlga. Võrdle DCF-iga. Nimeta vähemalt kolm põhjust, miks võrdlusettevõtte kordajat ei tohi mehaaniliselt kopeerida.

**32. Investeerimisotsuse memo.** Koosta kuni 120-sõnaline otsus: kas ostaksid aktsiat 22 € hinnaga? Erista faktid, eeldused, riskid, katalüsaatorid ja ohutusvaru (*margin of safety*). Sõnasta, milliste täiendavate andmeteta ei saa teha vastutustundlikku järeldust.

## E. Vigade, manipulatsioonide ja võimalike pettuste tuvastamine (33–40; 3 p igaüks = 24 p)

> **Oluline:** ülesanded käsitlevad *riskisignaale*. Pettuse tuvastamiseks on vaja dokumente, tehingu sisu, kinnitusi, ajatempleid ja vajadusel sõltumatut uurimist. Ükski suhtarv ei tõenda kellegi süüd.

**33. Varajane tulu.** Ettevõte kajastab 30. detsembril 100 000 € müügitulu, kuigi kaup anti lepingu alusel kliendi kontrolli alla alles 3. jaanuaril. Kauba omahind on 60 000 €. Oletame, et vara õiguspärane üleandmine toimus tõesti jaanuaris ja muid asjaolusid pole. Kui palju on detsembri aruandes tulu, kasum enne makse ja nõuded üle hinnatud ning varud ala hinnatud?

**34. Kapitaliseeritud kulud.** Ettevõte hakkab jooksvaid reklaamikulusid kajastama „immateriaalse varana“. Mida see teeb lühiajaliselt kasumi, varade ja rahavoo näitajatega? Mis tõendeid küsid enne, kui väidad, et kajastamine on väär?

**35. Varude väärtus ja kasum.** Kaubavarud kasvavad 70%, kuid müügitulu kasvab ainult 5%; samal ajal ei kajastata aegunud kaupade allahindlusi. Paku kolm võimalikku seletust, kolm kontrolltoimingut ja üks näitaja, mille muutust otsida.

**36. Laekumata müügitulu.** Ettevõtte viimase kvartali müügitulu kasvab 40%, CFO on negatiivne ja ostjate nõuete üle 90 päeva viivises osa kahekordistub. Milliseid nelja erinevat hüpoteesi uurid? Milliseid allikaid võrdled?

**37. Tehing seotud osapoolega.** Aasta lõpus müüakse oluline kogus kaupa uuele kliendile, kelle tegelik kasusaaja on müüja omaniku lähisugulane. Miks on see kõrgendatud riskiga? Nimeta vähemalt neli kontrolli; kas sugulusside iseenesest tähendab pettust?

**38. Kulumipoliitika muutmine.** Masina soetusmaksumus on 100 000 €, jääkväärtus 0 ja algne kasulik eluiga 5 aastat. Juhatus muudab põhjendamatult eeldatava eluea 10 aastaks masina kasutuse alguses. Kui palju suureneb ühe aasta EBIT võrreldes 5-aastase elueaga? Miks kasumi ja CFO võrdlus on siin kasulik? Selgita, millal eluea muutmine võiks olla põhjendatud.

**39. Pank vs pearaamat.** Pearaamatu rahakonto näitab 120 000 €, pangaväljavõte 80 000 €. Nimeta viis võimalikku, üksteisest eristatavat selgitust või kontrollikohta. Millist lepitust teed? Kas erinevus iseenesest tõestab vargust?

**40. Pettuseriski prioriseerimine.** Ettevõttel on järgmised signaalid: CFO on kolmel aastal järjest negatiivne, puhaskasum kasvab, nõuded kasvavad müügist kiiremini, tegevjuhi boonus sõltub EBIT-ist ja audiitor vahetus. Milliseid kolme tõendusallikat kontrolliksid esimesena ja milline on sinu viisakas, neutraalne tööalane järeldus juhatusele?

## F. Kaasaegne töö: Python, SQL, andmekvaliteet ja AI (41–44; 3 p igaüks = 12 p)

**41. Automaatkontroll.** Sulle antakse päevik kannetega `(kanne_id, kuupäev, konto, deebet, kreedit, vastaspool)`. Kirjelda neli automaatset testi, millega avastad vead enne aruannete koostamist. Selgita, mis võib „tasakaalus“ andmestikus ikkagi valesti olla.

**42. SQL-i küsimus.** Kirjuta SQL-i põhimõtteline päring, mis leiab kanded, mille deebetite summa ei võrdu kreeditite summaga. Kasuta tabeleid `kanded(kanne_id, konto, deebet, kreedit)`. Mida see kontroll **ei** tõenda?

**43. AI kui analüütiku abiline.** Kirjelda töövoogu, kuidas annad LLM-ile kahe aasta finantsaruanded ning saad riskide ja väärtuse analüüsi. Kuidas väldid välja mõeldud arve, konfidentsiaalsusprobleeme ja ekslikku pettusesüüdistust?

**44. Vestluse lõpuküsimus.** Sulle näidatakse ettevõtet, mille müük ja raamatupidamislik kasum kasvavad, kuid aktsia hind langeb. Selgita vähemalt **viis** majanduslikult mõistlikku põhjust, miks see ei ole vastuolu.

---

# 6. VASTUSTE EELNE KONTROLL-LEHT

Enne vastusevõtme avamist vaata üle:

- [ ] Bilansid klapivad ja omakapitali muutus on seletatud.
- [ ] CFO + CFI + CFF võrdub raha muutusega.
- [ ] NPV ja DCF valemites on õiged ajad ja diskontomäärad.
- [ ] Ma ei ole segi ajanud EV-d ning omakapitali väärtust.
- [ ] Ma ei ole pidanud EBIT-i, EBITDA-d või puhaskasumit samaks mis rahavoog.
- [ ] Olen eristanud fakti, hinnangut, hüpoteesi ja pettuse tõendit.
- [ ] Olen andnud vähemalt ühe *kontrollitava* selgituse iga olulisema kõrvalekalde kohta.

---

# 7. VASTUSED JA SELGITUSED

## A. Raamatupidamise mõistmine

### 1. Kolm aruannet

**Vastus:** bilanss kirjeldab varasid, kohustisi ja omakapitali **kindlal kuupäeval**; kasumiaruanne kirjeldab tulu, kulu ja kasumit **perioodil**; rahavoogude aruanne näitab **perioodi tegelikke raha liikumisi** äri-, investeerimis- ja finantseerimistegevuses. Üksi kasumiaruanne ei näita likviidsust, võlakoormust, kapitalivajadust ega kasumi raha-laekumise kvaliteeti.

**Näide:** 100 000 € kasumiga ettevõte võib pankrotti sattuda, kui kliendid ei maksa arveid ja laen tähtaegub.

### 2. Bilansi invariant

**Vastus:** pärast laenuga rahastatud ostu on põhivara +80 000 €, laenukohustis +80 000 €; omakapital alguses **ei muutu**. Kui laen laekub enne ostu, suureneb esmalt raha ja võlg; ostul asendub raha seadmega. Varad = kohustised + omakapital. Ettevõte ei saanud kohe netovaraliselt 80 000 € rikkamaks.

### 3. Tulu vs raha

**Vastus:** eeldusel, et teenus osutati ja teenuse eest on tekkinud sissenõutav nõue, tekib detsembris tulu 20 000 € ja ostjanõue 20 000 €. Jaanuaris suureneb raha 20 000 € ja nõue väheneb 20 000 €, uut müügitulu enam ei teki. Tekkepõhine arvestus eristab teenuse osutamise ja raha liikumise.

### 4. Kulum ja raha

**Vastus:** lineaarsel meetodil kulum = 100 000 / 5 = **20 000 €/a**. Masina rahas ostmisel on alguses investeerimistegevuse rahavoog −100 000 €. Esimese aasta kulum on kasumiaruande kulu 20 000 €, kuid sama aasta kulum ise ei ole uus väljamakse; põhivara jääkmaksumus pärast aastat 80 000 €. Vajadusel mõjutavad tulemust ajastamine, väärtuse langus ja maksureeglid.

### 5. Müügitulu vs kasum

**Vastus:** brutokasum 1 000 − 700 = **300 €**; ärikasum lihtsustatud juhul 300 − 250 = **50 €**. Puhaskasumiks nimetamiseks tuleb veel uurida intresse, makse, muid tulusid/kulusid ning seda, kas kõik kulud kuuluvad samasse perioodi.

### 6. Hinnangute mõju

**Vastus:** sama 60 000 € vara korral on aastane lineaarne kulum vastavalt 20 000 € ja 10 000 € (null-jääkväärtus, täisaasta). Lühem eluiga vähendab varasemate aastate kasumit ja bilansilist varaväärtust kiiremini. Erinevus võib tuleneda õigustatud kasutusintensiivsusest, tehnoloogiast või poliitikast; see ei tõenda iseenesest pettust. Võrdlemisel tuleb uurida lisasid ja arvestuspõhimõtteid.

### 7. Deebet/kreedit

**Vastus:** ei. Deebet on kirjendamise pool, mitte raha väljavoolu sünonüüm. Näiteks **deebet Raha 5 000 € / kreedit Müügitulu 5 000 €** suurendab vara (raha); **deebet Palgakulu 2 000 € / kreedit Võlg töötajale 2 000 €** suurendab kulu ja kohustist.

**Meelespea:** vara ja kulu kasvavad tavaliselt deebetis; kohustis, omakapital ja tulu kreeditis. Iga tervikliku kande deebet = kreedit.

### 8. Dividend

**Vastus:** dividendide jaotamine ei ole äritegevuse kulu ega vähenda perioodi puhaskasumit. Kui otsus ja väljamakse toimub korraga, vähenevad raha ja omakapital 30 000 €; kui esmalt tekib dividendikohustis, väheneb omakapital ja suureneb kohustis ning hilisemal maksmisel vähenevad raha ja kohustis. Rahavoogude aruandes on dividendi väljamakse üldjuhul finantseerimistegevuse rahavoog (klassifitseerimise detail sõltub kasutatavast raamistikust). Eesti maksukäsitlust tuleb eraldi hinnata.

## B. Aruannete koostamine ja sidumine

### 9. Kanded

| Tehing | Deebet | Kreedit |
|---|---|---|
| a) Osutatud teenus arvega 10 | Ostjate nõuded 10 | Müügitulu 10 |
| b) Arve laekub 10 | Raha 10 | Ostjate nõuded 10 |
| c) Pangalaen laekub 25 | Raha 25 | Laenukohustis 25 |
| d) Intress makstakse 2 | Intressikulu 2 | Raha 2 |

Kõigis kannetes on deebet = kreedit; **laenu saamine ei ole müügitulu** ja **nõude laekumine ei ole uus müügitulu**. Ühik: tuh €.

### 10. Bilanss ja omakapital

**2026:** varad 45+160+115+280 = **600**; kohustised 135+65+170 = **370**; omakapital **230**; 370+230 = 600. Omakapital: algsaldo 200 + puhaskasum 50 − dividend 20 = **230**. Kui muid omaniku tehinguid või koondkasumi komponente oleks, tuleks ka need arvesse võtta.

### 11. Marginaalid ja EBITDA

- Brutokasumi marginaal = 350/1 000 = **35%**.
- Ärikasumi marginaal = 100/1 000 = **10%**.
- EBITDA = EBIT + kulum ja amortisatsioon = 100+40 = **140 tuh €**.

**Tõlgendus:** EBITDA eirab vajalikke põhivarainvesteeringuid, käibekapitali muutust, intresse, makse ning muid tegelikke rahakulusid. Ettevõttel võib olla EBITDA 140 ja samal ajal negatiivne vaba rahavoog.

### 12. CFO kaudsel meetodil

```
Puhaskasum                                 +50
+ Kulum (mitterahaline kulu)               +40
− Ostjate nõuete kasv (160 − 100)         −60
− Varude kasv (115 − 80)                  −35
+ Tarnijavõlgade kasv (135 − 90)          +45
---------------------------------------------
Äritegevuse rahavoog (CFO)                 +40 tuh €
```

**Järeldus:** kasum 50 on suurem kui CFO 40. Kasumiaruanne näitab tekkepõhist tulemust, kuid nõuded ja varud sidusid kokku 95 tuh € ning tarnijad finantseerisid sellest 45 tuh €. Ühekordne aasta ei tõenda halba kasumi kvaliteeti; uurida tuleb korduvust ja maksetähtaegu.

### 13. Likviidsus

- Käibevara = 45+160+115 = **320**.
- Lühiajalised kohustised = 135+65 = **200**.
- Current ratio = 320/200 = **1,60**.
- Quick ratio = (45+160)/200 = **1,025 ≈ 1,03**.

Aruande põhjal näib lühiajaliste varade katvus olemas, kuid nõuded võivad osutuda aeglaselt laekuvaks, varud raskesti müüdavaks, laenud võivad sisaldada kovenante. Kontrolli nõuete vanuselist jaotust, lähikuude maksegraafikut, raha liikumist ja rahastuse jätkusuutlikkust.

### 14. Rahavood

```
CFO                                    +40
CFI: põhivara ost                     −70
CFF: laenu netokasv +25,
     dividendide väljamakse −20         +5
-----------------------------------------
Raha netomuutus                       −25
Algraha                                70
Lõppraha                               45
```

**Kontroll:** 40−70+5 = −25 ning 70−25 = **45**, mis võrdub bilansiga. Põhivara samuti klapib: 250+70−40 = **280**.

### 15. Kasvu ja rahakvaliteedi mõõdikud

- Müügitulu kasv = (1 000−820)/820 = **21,95%**.
- CFO/puhaskasum = 40/50 = **0,80**.

**Võimalik hea seletus:** ettevõte investeerib hoogsas kasvus rohkem varudesse ja pakub klientidele kokkulepitud pikemaid maksetähtaegu. **Võimalik halb seletus:** müügi laekumine halveneb, varud seisavad või lõpus on kajastatud müüki liiga vara. Kontrollimiseks võrdle DSO-d, nõuete vanuselist jaotust, järgneva perioodi laekumisi ning laovarude ringlust.

### 16. Rahakonversiooni tsükkel (CCC)

**2025:**

- DSO = 100/820 × 365 = **44,51 päeva**.
- DIO = 80/530 × 365 = **55,09 päeva**.
- DPO ≈ 90/530 × 365 = **61,98 päeva**.
- CCC ≈ **37,63 päeva**.

**2026:**

- DSO = 160/1 000 × 365 = **58,40 päeva**.
- DIO = 115/650 × 365 = **64,58 päeva**.
- DPO ≈ 135/650 × 365 = **75,81 päeva**.
- CCC ≈ **47,17 päeva**.

**Järeldus:** tsükkel pikenes umbes **9,54 päeva**. Ettevõte seob ühe müügi- ja tarnetsükli jooksul rohkem raha. DPO kasutas lihtsustatult COGS-i, kuigi korrektsem nimetaja on krediitostud; samuti võiks kasutada **keskmisi**, mitte aastalõpu saldosid, ning hooajalisust arvestada. Need suhtarvud on sõelumisvahend, mitte auditeeritud päevade arv.

## C. Finantsanalüüs ja risk

### 17. Brutokasumimarginaali halvenemine

**Võimalikud põhjused:** (1) müügihinnad langevad tugeva konkurentsi tõttu; (2) materjalide/energia hinnad tõusevad; (3) müügimiks nihkub madala marginaaliga toodetele; (4) allahindlused ja kaubatagastused; (5) tootmiskadude/varude mahakandmiste kasv; (6) müügitulu/omahinna arvestuspõhimõtete muudatus.

**Kontrollid:** brutomarginaal toodete ja klientide lõikes, keskmine müügihind, ühiku soetus-/tootmiskulu, hinnakirjad, varude allahindlused ja aastate arvestuspõhimõtete võrreldavus. Pelk kasv ei tõesta kvaliteeti.

### 18. Nõuete kasv

**a)** Krediidimüük võib teadlikult toetada kasvu; kogulaekumised saabuvad hiljem, ent tähtajaks. **b)** Makseraskused tähendavad kasvavat viivitust, vaidlusi ja võimalikke allahindlusi.

**Eristus:** võrreldavad DSO/viivises nõuete osakaal, klientide kontsentratsioon, järgneva kuu tegelikud laekumised, kreeditarved ja mahakandmised, sõlmitud maksetingimused. Investorile on oluline, kas müügitulust sünnib lähitulevikus raha või tuleb kahjumit korrigeerida.

### 19. ROE ja ROA

Keskmine omakapital = (200+230)/2 = **215**; keskmised varad = (500+600)/2 = **550**.

- ROE = 50/215 = **23,26%**.
- ROA (puhaskasumipõhine, täpsusta definitsioon) = 50/550 = **9,09%**.

**Tõlgendus:** ROE võib olla kõrge tänu kasumlikkusele, kuid ka tänu kõrgele võlakoormusele või väikesele omakapitalile. Äritegevuse tootlust saab võrdluseks analüüsida ROIC-i või EBIT/varad suhtega. ROA definitsioonid varieeruvad, seega tuleb mõõdiku lugeja alati näidata.

### 20. Tegevusvõimendus

Ühiku jääktulu = 100−60 = **40 €**. Kasumilävi = 200 000/40 = **5 000 ühikut**. 

- 7 000 tk müügil EBIT = 7 000×40−200 000 = **80 000 €**.
- 5 000 tk müügil EBIT = **0 €**.

Müügi vähenemine 28,6% (7 000 → 5 000) viib kasumi 80 000-lt nulli: kõrged püsikulud võimendavad tulemuste kõikumist. Alla 5 000 tk tekib selle mudeli järgi kahjum. Lihtmudel eeldab muutumatut hinda, ühikukulu ja kulustruktuuri.

### 21. Finantsvõimendus

**Algselt** 50 000 € ärikasumi korral:

| | X | Y |
|---|---:|---:|
| Laen | 100 000 | 400 000 |
| Omakapital | 400 000 | 100 000 |
| Intress (5%) | 5 000 | 20 000 |
| Puhaskasum (maksudeta) | 45 000 | 30 000 |
| **ROE** | **11,25%** | **30%** |

**Halva stsenaariumi** 15 000 € EBIT korral: X kasum 10 000 → ROE **2,5%**; Y kahjum −5 000 → ROE **−5%**. Laenuvõimendus võimendab omakapitali tootluse mõlemas suunas. Y-l on lisaks refinantseerimis- ja kovenandirisk.

### 22. Varude allahindlus

Varu hinnanguline netorealiseerimisväärtus on 8 000 €, mistõttu tavapärase soetusmaksumuse ja netorealiseerimisväärtuse madalama väärtuse põhimõtte järgi tuleb kajastada allahindlus **22 000 €**. Varad vähenevad 22 000 €, jooksva perioodi kasum enne maksude mõju väheneb 22 000 €. Allahindlus ise **ei tekita kohe uut raha väljavoolu**; algne varuost võis olla makstud varem. Edasine maksukäsitlus sõltub raamistikust.

### 23. ROIC ja majanduslik kasum

ROIC = 240 000 / 2 000 000 = **12%**. Kapitalikulu = 2 000 000 × 9% = **180 000 €**. Lihtsustatud majanduslik kasum = 240 000−180 000 = **60 000 €**.

**Järeldus:** ROIC ületab WACC-i kolme protsendipunkti võrra → mudeli eeldustel luuakse väärtust. Positiivne raamatupidamislik kasum üksinda ei tõenda väärtuse loomist: näiteks 100 000 € NOPAT oleks selle kapitalimahu juures majanduslik kahjum 80 000 €. Praktikas tuleks kasutada õigesti mõõdetud keskmist investeeritud kapitali ja kohandatud NOPAT-it.

### 24. Kasvu rahastamine

| Võimalus | Kasu | Hind / risk |
|---|---|---|
| Kiirendada nõuete laekumist ja vähendada tarbetut varu | Vabastab käibekapitali | Liiga range krediidipoliitika võib müüki kahjustada |
| Investeerida etapiti / vähendada CAPEX-it | Vähendab vahetut rahavajadust | Võib pidurdada kasvu ja konkurentsivõimet |
| Kaasata omakapitali | Ei too automaatselt kohustuslikku intressi | Lahjendab olemasolevate omanike osalust |
| Võtta laenu / krediidilimiit | Säilitab omandistruktuuri | Intressi-, refinantseerimis- ja kovenandirisk |

Lisaks võib läbi rääkida tarnijate tähtaegu, kuid võlgade kasvatamine ei ole tasuta kapital. Hästi põhjendatud vastus seob valiku ettevõtte kapitalikulu ja rahavoo prognoosiga.

## D. Projekt, ettevõte ja aktsia väärtus

### 25. Projekti NPV

$$
NPV=-30\,000+\frac{12\,000}{1{,}10}+\frac{14\,000}{1{,}10^2}+\frac{16\,000}{1{,}10^3}
$$

**Arvutus:** PV1 10 909,09 €, PV2 11 570,25 €, PV3 12 021,04 €. Kokku 34 500,38 €. **NPV ≈ +4 500,38 €**. Projekt lisab ennustatud rahavoogude ja 10% nõutava tootluse korral väärtust. NPV on **tulevaste rahavoogude nüüdisväärtuse ja alginvesteeringu vahe**, mitte raamatupidamislik kasum ega garanteeritud tulu.

### 26. IRR

**IRR ≈ 17,93%** (määr, mille korral NPV=0). Kuna IRR 17,93% > kapitalikulu 10% ja NPV>0, tundub projekt antud eeldustel sobiv.

**IRR-i lõksud:** (1) eri suurusega projektidest võib väiksema NPV-ga projekt anda suurema IRR-i; (2) mitmekordse märgivahetusega rahavoo korral võib olla mitu IRR-i või pole ühtegi; (3) IRR ei asenda riskile vastava kapitalikulu ega rahavoogude realistlikkuse kontrolli; (4) projektide teineteist välistavate valikute korral eelista NPV-d.

### 27. FCFF, FCFE ja diskontomäär

- **FCFF (free cash flow to firm):** raha, mis on saadaval nii võla- kui ka omakapitali rahastajatele pärast tegevuskulusid, makse, käibekapitalivajadust ja investeeringuid.
- **FCFE (free cash flow to equity):** raha, mis jääb omanikele pärast laenuandjatega seotud rahavooge ja netolaenamist.
- Lihtsustatud valem: **FCFF = EBIT × (1−t) + kulum − CAPEX − Δoperatiivne käibekapital**. Maksumäär `t` on selle valemi jaoks kohandatud tegevustulemuse maksueeldus, mitte Eesti maksudeklaratsiooni universaalne valem.

FCFF-i diskonteeritakse **WACC-iga**, sest rahavood kuuluvad kogu kapitalile. FCFE diskonteeritakse omakapitali nõutava tootlusega. Kolme aasta lõpus ettevõte eeldatavasti jätkab tegutsemist, mistõttu lisatakse **jätkuväärtus**.

### 28. DCF: EV

**Märkus:** allpool on kõik arvud **tuh €**.

$$
PV(FCFF)=\frac{120}{1{,}10}+\frac{140}{1{,}10^2}+\frac{160}{1{,}10^3}
=345{,}004
$$

$$
TV_3=\frac{FCFF_4}{WACC-g}
=\frac{160\times1{,}03}{0{,}10-0{,}03}
=2354{,}286
$$

$$
PV(TV)=\frac{2354{,}286}{1{,}10^3}=1768{,}810
$$

**EV = 345,004 + 1768,810 = 2 113,813 tuh €** ehk umbes **2,114 miljonit €**.

Gordoni kasvumudelis peab `WACC > g`; vastasel juhul ei ole see kasvava igavese rahavoo lihtne valem antud eeldustel majanduslikult mõistlik. Samuti peab pikaajaline kasv olema põhjendatud ettevõtte elutsükli ja majanduse kasvuvõimalustega.

### 29. Aktsia väärtus

Netovõlg = 400−70 = **330 tuh €**.

- Omakapitali väärtus = EV − netovõlg = 2 113,813−330 = **1 783,813 tuh €**.
- Aktsia väärtus = 1 783,813 tuh € / 100 tuhat aktsiat = **17,84 €/aktsia**.
- Erinevus turuhinnast = (17,838−22)/22 = **−18,92%**.

**Järeldus:** antud DCF-eeldustel on 22 € turuhind mudeli väärtusest umbes 19% kõrgem. See ei tõesta, et hind *kindlasti* langeb: turg võib eeldada kiiremat kasvu, madalamat riskipreemiat või suuremat lõppväärtust. Samuti võivad DCF-i eeldused ise olla valed.

### 30. DCF-tundlikkus

| Stsenaarium | WACC | g | EV (tuh €) | Aktsia mudelihind |
|---|---:|---:|---:|---:|
| Konservatiivne | 12% | 2% | 1 494,260 | **11,64 €** |
| Baas | 10% | 3% | 2 113,813 | **17,84 €** |
| Optimistlik | 9% | 4% | 2 921,303 | **25,91 €** |

Baasstsenaariumi diskonteeritud jätkuväärtuse osakaal = 1 768,810/2 113,813 = **83,68%**.

**Järeldus:** mudel on eriti tundlik pikaajalise kasvumäära ja kapitalikulu vastu; 83,7% hinnangust sõltub ajast, mida 3-aastane prognoos otse ei kata. Seepärast peaks analüütik kirjeldama vähemalt kolme stsenaariumi ja hindama, millised eeldused on usutavad.

### 31. Võrdluskordaja EV/EBITDA

EBITDA = 300 tuh €; põhjendatud kordajavahemik 5–7:

| EV/EBITDA | EV (tuh €) | Omakapital = EV−330 | Ühe aktsia väärtus |
|---|---:|---:|---:|
| 5× | 1 500 | 1 170 | **11,70 €** |
| 6× | 1 800 | 1 470 | **14,70 €** |
| 7× | 2 100 | 1 770 | **17,70 €** |

Vahemik on **11,70–17,70 €/aktsia**. See kattub peaaegu DCF-i baasväärtusega 17,84 € ülemises otsas, kuid meetodite tulemuste sarnasus ei tõesta täpsust. Kordajad sõltuvad kasvust, marginaalist, võlast, CAPEX-i vajadusest, arvestuspõhimõtetest, riskist, majandustsüklist ja võrdlusgrupi kvaliteedist. EBITDA ei ole rahavoog.

### 32. Lühike investeerimismemo (näidisvastus)

> Nord Analyticsi 22 € turuhind ületab baas-DCF väärtust 17,84 € umbes 19%. Konservatiivne stsenaarium annab 11,64 €, optimistlik 25,91 €. Kuna ligikaudu 84% ettevõtte hinnangulisest väärtusest pärineb jätkuväärtusest, sõltub tulemus väga tugevalt pikaajalisest kasvust ja kapitalikulust. EV/EBITDA võrdlus annab 11,70–17,70 €. Praeguse info põhjal ma 22 € eest uut positsiooni ei avaks: soovin ohutusvaru. Kontrolliksin tegelikke rahavooge, klientide püsimist, CAPEX-i, võlatingimusi, aktsiate lahjendust ja kasvu usutavust. Investeeringut võiks ümber hinnata, kui ettevõte tõestab püsivalt tugevamat rahavoogu või hind langeb põhjendatud väärtusvahemikku.

**Hindamise alus:** mitte „osta/ära osta“ sõna, vaid põhjuslik arutlus, risk ja eelduste kontroll.

## E. Võimalike vigade ja pettuseriskide tuvastamine

### 33. Enneaegne müügitulu

Kui lepingu sisulised tingimused näitavad ühemõtteliselt, et kontroll läks kliendile üle jaanuaris, tuleks detsembrist välja jätta:

- Müügitulu **100 000 €** (ülehinnatud).
- Nõuded **100 000 €** (ülehinnatud, eeldusel et arve/kajastamine lõi nõude).
- Müüdud kaupade kulu **60 000 €** (ülehinnatud; vajab ümberkannet varudesse).
- Varud **60 000 €** (alahinnatud).
- Kasum enne makse **40 000 €** (ülehinnatud).

**Kontroll:** leping ja tarneklauslid, saatedokument, üleandmisakt, lao väljastus, transpordikinnitus, kliendi kinnitus, arve kuupäev, kreeditarved ja järgmise perioodi kanded. Ainult arve kuupäev ei määra tulu tunnustamise õigust.

### 34. Reklaamikulu kapitaliseerimine

Tavaliste jooksva perioodi reklaamikulude põhjendamatu varana kajastamine **suurendab lühiajaliselt varasid ja kasumit**, kuid ei paranda raha, mis reklaamile tegelikult kulus; küll võib rahavoogude aruandes muutuda väljamakse *klassifikatsioon*, kui viga mõjutab selle esitusviisi. Kontrolli kuludokumentide olemust, tulevaste kasude eristatavust, vara määratlust, kontrolli vara üle, arvestusstandardi tingimusi ja juhatuse hinnanguid. Ära eelda, et kogu immateriaalse vara kajastamine on vale: näiteks teatud arenduskulud võivad konkreetsel raamistikul ja tingimustel kapitaliseeruda.

### 35. Varude 70% kasv

**Võimalused:** nõudluse hooajalisus või laovaru teadlik kasvatamine; müügi nõrgenemine ja aegunud varud; liiga kõrge soetusmaksumus/valesti kapitaliseeritud kulud; mittetäielik kulu kajastamine.

**Kontrollid:** füüsiline inventuur, varude vanuseline analüüs ja müügijärgne hind, laoliikumiste võrdlus arvetega, aegunud kaupade allahindlused. **Näitajad:** DIO ja varude käibekordaja; bruto- ja laovaruallahindluse marginaal.

### 36. Müük +40%, CFO negatiivne, viivised kasvavad

**Neli hüpoteesi:** (1) legitiimne krediidimüügi kasv; (2) klientide makseprobleem ja nõuete allahindluse vajadus; (3) liiga varane või fiktiivne müügitulu; (4) hooajalisus, erandlik kliendileping või aeglane projektide vastuvõtmine.

**Tõendid:** müügilepingud ja arved, lähetused/üleandmisaktid, panga tegelikud laekumised järgmistes kuudes, nõuete vanus, kreeditarved, klientide välised kinnitused. Otsi ajaliselt järjestatud lepingu → täitmise → arve → raha ahelat.

### 37. Seotud osapoole müük

**Risk:** tehing ei pruugi olla turutingimustel; tulu, ostjapoolne maksevõime või kauba tegelik liikumine võib vajada eraldi tõendamist.

**Kontrollid:** (1) tegeliku kasusaaja ja seotud osapoole avalikustamise kontroll; (2) tehingu hinnavõrdlus turutingimustega; (3) leping, saatedokumendid ja üleandmisakt; (4) sõltumatud laekumiskinnitused; (5) tagastus- ja tagasiostuklauslid; (6) kinnitused seotud osapoolega tehtud tehingute aruandluses. **Sugulusside ei võrdu pettus**; kontrolli seose täpne sisu ja dokumenteeritud majanduslik põhjendus.

### 38. Kasuliku eluea pikendamine

- Viie aasta kulum: 100 000/5 = **20 000 €** aastas.
- Kümne aasta kulum: 100 000/10 = **10 000 €** aastas.
- EBIT on uue hinnanguga esimesel aastal **10 000 € suurem** (muude asjaolude võrdsusel).

Kulumimuutus ise raha ei genereeri; seega paraneb EBIT ilma samaväärse muutuseta CFO-s. Kasuliku eluea hinnangu muutmine võib olla põhjendatud tegeliku kasutusaja, hoolduse või tehnoloogilise muutuse tõttu, kuid vajab dokumente ja korrektset edasiulatuvat arvestust. Küsimuse arvutus eeldab muutust **kasutuse alguses**; hilisem muutus arvutataks allesjäänud bilansilise väärtuse ja järelejäänud eluea alusel.

### 39. Panga ja pearaamatu erinevus

**Võimalikud põhjused:** (1) teel olevad laekumised; (2) välja kirjutatud, kuid esitamata maksed; (3) pangatasud/intressid kajastamata; (4) tehingud vale kuupäeva, konto või summaga; (5) topeltkanne, valuutakursi mõju, puuduolev makse või lubamatu väljamakse.

**Lepitus:** võrdle **sama kuupäeva** pankade saldosid, iga panga kontot eraldi, raha teel ja lahtisi makseid, tee väljavõte ↔ pearaamat üks-ühele sobitus, kontrolli autoriseerimisi ning paranda põhjendatud erinevused. **40 000 € lahknevus ei tõenda vargust**, vaid nõuab kiiret selgitamist.

### 40. Pettuseriski prioriteedid

**Esmased kolm allikat:** (1) nõuete vanus ja pärast aruandekuupäeva toimunud reaalsed laekumised; (2) suurte aasta lõpu müükide lepingud, saatedokumendid ning kreeditarved; (3) arvestuspõhimõtted, ebatavalised päevikukanded, juhtkonna põhjendused ja audiitori vahetumise dokumenteeritud taust.

**Neutraalne järeldus:** „Kasum ja rahalaekumised lahknevad süsteemselt, nõuded kasvavad müügist kiiremini ning juhtimistasustamises on tulususe stiimul. See suurendab olulise väärkajastamise riski ja õigustab sihitud lisakontrolle. Esitatud info ei võimalda teha järeldust tahtliku pettuse kohta.“

## F. Kaasaegsed töövahendid

### 41. Neli andmekontrolli

1. **Kande tasakaal:** iga `kanne_id` korral `SUM(deebet) = SUM(kreedit)` tolerantsiga nt 0,01 €.
2. **Perioodi ja duplikaatide kontroll:** puuduvad / korduvad ID-d, sama arvenumber + partner + summa + kuupäev, lubamatu kuupäev väljaspool perioodi.
3. **Kontoplaani ja loogika kontroll:** ainult lubatud kontod; erandlikud negatiivsed summad; ebatavaline tulu- või kassakonto kasutus.
4. **Lepitus:** raha konto ↔ pank, ostjate/tarnijate koondkontod ↔ alamaruanded, põhivara bilansiline muutus ↔ ostud/kulum/müük.

**Oluline:** ideaalselt tasakaalus fiktiivne müük võib läbida deebet/kreedit kontrolli. Seega kontrolli ka tehingu toimumist, õigusi, ajastust ja majanduslikku sisu.

### 42. SQL

```sql
SELECT
    kanne_id,
    ROUND(SUM(COALESCE(deebet, 0)), 2) AS deebet_kokku,
    ROUND(SUM(COALESCE(kreedit, 0)), 2) AS kreedit_kokku,
    ROUND(SUM(COALESCE(deebet, 0) - COALESCE(kreedit, 0)), 2) AS vahe
FROM kanded
GROUP BY kanne_id
HAVING ABS(ROUND(SUM(COALESCE(deebet, 0) - COALESCE(kreedit, 0)), 2)) > 0.01;
```

**Selgitus:** päring toob välja tasakaalust väljas olevad kanded. Rahaühiku ümardus ja tolerants sõltuvad andmetest ning DBMS-ist. `NULL`-ide automaatne käsitlemine nullina on siin ainult diagnostiline eeldus; tootmiskontrollis tuleks puuduvaid väärtusi eraldi lipustada. Tasakaal ei tõenda tehingu ehtsust, õiget perioodi, õiget kontot, tehingu täielikkust ega vastavust standardile.

### 43. AI töövoog

**Näidiskäik:** (1) kontrolli aruannete päritolu ja valmista masinloetav tabel; (2) arvuta Pythoni/SQL-iga valemid ja võrdle bilanssi; (3) anna LLM-ile *ainult vajaliku ulatusega*, vajadusel anonüümitud struktureeritud andmed koos definitsioonidega; (4) palu kirja panna kasv, marginaalid, CFO, likviidsus, võimalikud seletused, tõendamata hüpoteesid; (5) valideeri iga number sõltumatu arvutusega; (6) eralda riskihüpoteesid ja kinnitatud rikkumised; (7) lase inimesel otsus üle vaadata, salvesta auditijälg.

**Näidisprompt:**

> Analüüsi kahte finantsaastat. Arvuta müügikasv, marginaalid, CFO/puhaskasum, DSO/DIO/DPO ja netovõlg/EBITDA. Kasuta ainult antud arve, too iga järelduse juurde valem ja algandmed ning märgi puuduva info puhul „ei saa järeldada“. Erista kinnitatud faktid, võimalikud riskid ja kontrollimiseks vajalikud dokumendid. Ära esita pettusesüüdistust ilma tõenditeta.

**Andmekaitse:** ära laadi töötajate, klientide ega ärisaladusi sisaldavaid algandmeid teenusesse ilma lubatud keskkonna ja andmetöötlusaluseta.

### 44. Kasvav kasum, langev aktsiahind

Võimalikud põhjused (piisab viiest koos põhjendusega):

1. Turg ootas **veel kiiremat** kasvu: tulemused on head, aga alla ootuste.
2. Diskontomäärad/kapitalikulu kasvavad, vähendades tulevaste rahavoogude nüüdisväärtust.
3. Kasum ei muutu rahaks: CFO nõrk, nõuded või varud kasvavad.
4. Puhaskasum kasvas ühekordsest tulust, mitte püsivast ärikasumist.
5. Ettevõte vajab suurt CAPEX-it, mis vähendab tulevast vaba rahavoogu.
6. Konkurentsi, regulatsiooni või tehnoloogia tõttu halveneb pikaajaline prognoos.
7. Võlakoormus või refinantseerimisrisk kasvab.
8. Aktsia oli juba alguses üle hinnatud või turu riskisentiment halvenes.
9. Uute aktsiate emiteerimine võib kasumit aktsia kohta lahjendada.
10. Raamatupidamislik hinnang või kvaliteet muutus; tuleviku kasum on ebakindlam.

**Põhiseos:** turuhind peegeldab ootusi *tulevasele* riskiga korrigeeritud rahavoole, mitte üksnes möödunud perioodi puhaskasumit.

---

# 8. HINDAMINE JA TAGASISIDE

## Punktid

| Osa | Küsimused | Punkte |
|---|---:|---:|
| A – Põhimõtted | 1–8 | 16 |
| B – Aruanded ja seosed | 9–16 | 24 |
| C – Tõlgendamine ja risk | 17–24 | 24 |
| D – Väärtuse hindamine | 25–32 | 40 |
| E – Võimalikud pettused | 33–40 | 24 |
| F – Andmeanalüüs ja AI | 41–44 | 12 |
| **KOKKU** | **44** | **140** |

## Hindamisstandard

- **0 p:** puuduv vastus või sisuline arusaamatus.
- **Osapunktid:** arvutus on valemilt õige, kuid eksib ühikutes; või mõte on õige, kuid ilma sisulise tõlgenduseta.
- **Täispunktid:** korrektne tulemus koos põhjenduse, piirangute ja vajadusel kontrollitava alternatiivse seletusega.
- **Raskemates 5-punktistes küsimustes:** 2 p metoodika ja valemid, 2 p arvutused, 1 p asjakohane otsus/ebakindlus (intervjueerija võib alampunktid täpsustada).
- **Pettuseteemalistes 3-punktistes küsimustes:** 1 p riski kirjeldus, 1 p tõend / kontroll, 1 p põhjendatud neutraalne järeldus.

| Tulemus | Hinnang | Oskustase |
|---|---|---|
| 0–69 p (<50%) | Vajab põhioskuste kordamist | Alustaja |
| 70–97 p (50–69%) | Saab osaleda juhendatud arvestustöös | Juunior |
| 98–118 p (70–84%) | Analüüsib aruandeid iseseisvalt | Tugev spetsialist |
| 119–132 p (85–94%) | Oskab hinnata projekte, ettevõtet ja riske | Vanemanalüütiku valmidus |
| 133–140 p (95–100%) | Väga tugev tervikmõtlemine | Eksperdi lähedane testi tulemus |

**Ettevaatus:** see on õppeotstarbeline intervjuusimulatsioon, mitte kutsetunnistus ega usaldusväärne hinnang inimese tegelikule ametikvalifikatsioonile. Vanemanalüütiku/eksperdi töö eeldab ka ajaliselt kestvat kogemust ja eetilist otsustusvõimet. Hästi põhjendatud alternatiivne vastus väärib punkte ka siis, kui ei järgi sõna-sõnalt näidisvastust.

## Kriitilised oskused: eraldi läbimiskriteerium

Isegi hea koondskoori puhul nõuab järelõpet, kui kandidaat:

- ei suuda siduda bilanssi, kasumit ja rahavooge (10–14);
- ajab segi ettevõtte väärtuse ja aktsionäride omakapitali väärtuse (28–29);
- ei oska eristada kasumit ja rahavoogu (12, 18, 27);
- peab kaudset riskisignaali automaatselt pettuse tõendiks (33–40);
- usaldab pimesi LLM-i arvutusi või laeb tundlikke andmeid sobimatusse keskkonda (43).

---

# 9. SUULINE INTERVJUU – 10 LÜHIKÜSIMUST

Küsimustele peaks olema võimalik vastata 1–2 minutiga. Näidisvastuse märksõnad on lisatud sulgudesse; intervjueerija võib need enne vestlust peita.

1. **Miks firma võib olla kasumlik ja siiski maksejõuetu?** (Tekkepõhisus, nõuete laekumine, lühiajalised kohustised, rahavood.)
2. **Miks suurenev EBITDA ei pruugi tähendada suuremat väärtust?** (CAPEX, käibekapital, risk, kapitalikulu.)
3. **Millal laen tõstab ROE-d, millal hävitab väärtust?** (ROIC vs laenu hind, allapoole mõju, risk.)
4. **Milline üks muudatus võib näidata korraga väiksemat kasumit ja väiksemat vara, ilma et raha liiguks?** (Kulum/vara allahindlus.)
5. **Miks aktsia „odav P/E“ ei pruugi olla hea ost?** (Kasumi ühekordsus, kvaliteet, langev kasv, võlg, tsükkel.)
6. **Mida otsiksid aruande lisadest esimesena?** (Arvestuspõhimõtted, võlakohustised, seotud osapooled, tingimuslikud kohustised, segmentide info.)
7. **Mis vahe on DCF-il ja EV/EBITDA võrdlusel?** (Tulevane rahavoog vs võrdlusettevõtete turuhinnad.)
8. **Kas negatiivne CFO on alati halb?** (Ei; võib olla ajutine kasvufaas, aga nõuab selgitust.)
9. **Mida teed, kui juhatus palub ebamugava näitaja „ilusamaks“ kirjutada?** (Faktid, alternatiivne korrektne esitus, dokumenteerimine, eskalatsioon.)
10. **Mis on esimene kontroll, kui finantsmudel annab ebaloogiliselt kõrge aktsiahinna?** (Ühikud, FCFF vs FCFE, WACC, g, jätkuväärtus, netovõlg, aktsiate arv.)

---

# 10. VALMIDUS TÖÖLE – PRAKTILINE TÖÖPROOV

**Tööproovi ülesanne (eraldi, 60–90 min).** Saa ettevõtte kaks aastaaruannet ja tehingute CSV (või kasuta anonüümitud näidisandmeid). Tee järgmised etapid:

1. Impordi CSV Pythonisse või SQL-i; kontrolli andmetüüpe, väärtuste puudumist, duplikaate ja deebet/kreedit tasakaalu.
2. Koosta vähemalt bilanss, kasumiaruanne ja kaudse rahavoogude aruande peamised seosed.
3. Arvuta kasv, marginaalid, current/quick ratio, DSO, netovõlg/EBITDA, ROE ning CFO/puhaskasumi suhe.
4. Kirjuta 8–10 lauseline **ettevõtte tervise diagnoos**: kaks tugevust, kolm riski ja kaks vajalikku lisadokumenti.
5. Hinda ettevõtet lihtsustatud FCFF-DCF-iga: esita WACC, kasv, jätkuväärtus, EV, netovõlg ja aktsia hind (kui börsiettevõte).
6. Kirjelda kolm kontrollitavat ebakõla või pettuseriski hüpoteesi ilma kedagi süüdistamata.
7. Lisa metoodika- ja eelduste nimekiri, et teine inimene saaks tulemust korrata.

**Parima kandidaadi tunnus:** ta oskab öelda mitte ainult „arv on X“, vaid ka „X tekib neist tehingutest; see tähendab tõenäoliselt Y-d; alternatiiv on Z; eristamiseks kontrollin dokumenti D“.

## Lühisõnastik

| Mõiste | Tähendus |
|---|---|
| Bilanss | Finantsseisund kuupäeval: varad = kohustised + omakapital |
| Kasumiaruanne | Perioodi tekkepõhised tulud, kulud ja tulemus |
| Rahavoogude aruanne | Raha liikumine äri-, investeerimis- ja finantseerimistegevuses |
| Tekkepõhisus | Tulud/kulud kajastatakse majandusliku tekkimise, mitte tingimata maksmise järgi |
| Debitoorne võlg / nõue | Kliendi kohustus ettevõttele maksta |
| Kreditoorne võlg | Ettevõtte kohustus tarnijale maksta |
| Kulum | Põhivara soetusmaksumuse süstemaatiline kuluna jaotamine |
| EBIT | Ärikasum enne intresse ja makse (määratlus sõltub esitlusest) |
| EBITDA | Ärikasum enne kulumit ja amortisatsiooni (mitte rahavoog) |
| CFO | Rahavoog äritegevusest |
| CAPEX | Põhivarainvesteeringute rahaline väljaminek |
| FCFF | Vaba rahavoog kogu ettevõtte rahastajatele |
| FCFE | Vaba rahavoog omanikele |
| WACC | Kapitali kaalutud keskmine hind |
| NPV | Rahavoogude diskonteeritud nüüdisväärtuste summa miinus alginvesteering |
| IRR | Diskontomäär, mille juures projekti NPV = 0 |
| EV | Ettevõtte põhitegevuse väärtus kõigile kapitaliandjatele, koos nõutavate korrigeerimistega |
| Equity value | Omakapitali väärtus pärast netovõla ja muude korrigeerimiste arvestamist |
| ROE | Omakapitali tootlus |
| ROIC | Investeeritud kapitali tootlus |
| DSO / DIO / DPO | Nõuete / varude / tarnijavõlgade ligikaudne käibevälde päevades |
| CCC | Raha konversioonitsükkel = DSO + DIO − DPO |
| Ohutusvaru | Vahe hinnangulise konservatiivse väärtuse ja turul makstava hinna vahel |
| Punane lipp | Riskisignaal, mis nõuab täiendavat kontrolli, mitte pettuse tõend |

## Lähteraamat ja ulatus

**Richard Barker.** *Short Introduction to Accounting*. Cambridge University Press, 2011. Peatükkide fookus originaalraamatus: 1) aruannete tutvustus (lk 13), 2) finantsinfo vajadus (lk 27), 3) majandustegevuse kirjendamine (lk 47), 4) aluste koondnäide (lk 65), 5) kasv (lk 87), 6) väärtuse loomine (lk 99), 7) risk (lk 111), 8) ettevõtte hindamismudel (lk 128). Leheküljed vastavad **raamatu trükitud lehekülgedele**, mitte PDF-i leheküljenumbritele.

**Õppeautori täiendused:** börsiaktsia FCFF-põhine väärtus, EV/EBITDA, ohutusvaru, pettuseriski analüüs, SQL/Python ja LLM-i tööprotsessid. Küsimused, numbrilised juhtumid ja vastused on loodud selle õppematerjali jaoks; need ei ole sõnasõnalised raamatu ülesanded. Raamatu 2011. aasta käsitlus ei asenda 2026. aasta raamatupidamisstandardeid, maksureegleid, auditeerimisstandardeid ega kutsealast õigusnõu.
