# RAAMATUPIDAMISE JA FINANTSANALÜÜSI TÖÖINTERVJUU TEST

**Richard Barkeri „Short Introduction to Accounting“ põhjal – praktilised juhtumid, vastused ja selgitused**

> **Eesmärk.** Kontrollida, kas kandidaat oskab majandustehinguid sisuliselt mõista, lugeda ja omavahel siduda finantsaruandeid, hinnata ettevõtte ja projekti väärtust, määrata aktsia põhjendatud väärtuse vahemikku ning märgata raamatupidamisvigu ja võimalikke pettuseriske.
>
> 
> **Alus:** Richard Barker, *Short Introduction to Accounting* (Cambridge University Press, 2011), peatükid 1–8. **Täiendused:** aktsia väärtuse hindamine, pettuseriski analüüs, andmekontroll SQL/Pythoniga ning AI kasutamine on tänapäevased tööalased laiendused, mitte raamatu eraldi peatükid.

[**Alusta testiga**](#1-testi-juhend) · [**Andmestik A**](#3-juhtum-a--ettevõte-kalev-tech-oü) · [**Andmestik B**](#4-juhtum-b--ettevõtte-ja-aktsia-hindamine)

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


**Kandidaadile:** salvesta vastused eraldi faili. Vastused ja hindamisjuhend on teises dokumendis.
