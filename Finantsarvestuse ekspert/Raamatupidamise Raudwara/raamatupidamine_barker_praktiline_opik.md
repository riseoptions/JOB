# Raamatupidamine ja finantsaruannete analüüs AI ajastul

**Praktiline eestikeelne kiirõpik Richard Barkeri raamatu „Short Introduction to Accounting“ põhjal**  
Versioon: 7. november 2026 · Vorming: GitHub Markdown · Tase: algaja → iseseisev finantsandmete analüüs

> **Eesmärk.** Pärast materjali läbitöötamist oskad selgitada raamatupidamise põhimõtteid, lugeda bilanssi, kasumiaruannet ja rahavoogude aruannet, kontrollida kirjendeid, analüüsida ettevõtte tulemusi ning kasutada Pythonit, SQL-i ja AI-d oma töö kiirendamiseks. See on **õppe- ja analüüsijuhend**, mitte raamatupidaja kvalifikatsioon ega asendus konkreetse ettevõtte maksuarvestuse ja aruandluse kontrollile.

**Põhiallikas:** Richard Barker, *Short Introduction to Accounting*, Cambridge University Press, 2011, 8 peatükki. Peatükiviited osutavad raamatu trükitud lehekülgedele (PDF-is ligikaudu +10 lehekülge). **Barker**-märgistusega osad on raamatu kontseptsioonide ümberjutustus. **Tänapäevane täiendus** tähendab autori enda loodud näiteid, Eesti õigusraamistikku, tehnilisi töövõtteid ja uusi mõisteid, mida 2011. aasta raamat otseselt ei käsitle. Kõik tabelid, harjutused ja koodinäited on siin koostatud iseseisvalt, välja arvatud selgelt märgitud lühikesed viited Barkeri näidetele.

---

## Sisukord

1. [Kiirstart: kümme põhimõtet](#1-kiirstart-kümme-põhimõtet)
2. [Raamatu kaheksa peatüki kaart](#2-raamatu-kaheksa-peatüki-kaart)
3. [Raamatupidamise mõttemudel](#3-raamatupidamise-mõttemudel)
4. [Bilanss, kasumiaruanne, rahavood ja omakapital](#4-bilanss-kasumiaruanne-rahavood-ja-omakapital)
5. [Kahekordne kirjendamine ja tekkepõhisus](#5-kahekordne-kirjendamine-ja-tekkepõhisus)
6. [Üks täielik ettevõttenäide algusest lõpuni](#6-üks-täielik-ettevõttenäide-algusest-lõpuni)
7. [Kõik olulised arvestuskontseptsioonid](#7-kõik-olulised-arvestuskontseptsioonid)
8. [Kuidas finantsaruandeid analüüsida](#8-kuidas-finantsaruandeid-analüüsida)
9. [Kasv, väärtus, riskid ja DCF](#9-kasv-väärtus-riskid-ja-dcf)
10. [Eesti raamatupidamine 2026. aastal](#10-eesti-raamatupidamine-2026-aastal)
11. [Kaasaegne töövoog: Excel, SQL, Python ja AI](#11-kaasaegne-töövoog-excel-sql-python-ja-ai)
12. [Seitsmepäevane õppeplaan ja oskuste test](#12-seitsmepäevane-õppeplaan-ja-oskuste-test)
13. [Mõistete sõnastik](#13-mõistete-sõnastik)
14. [Allikad ja edasine õppimine](#14-allikad-ja-edasine-õppimine)

---

## 1. Kiirstart: kümme põhimõtet

Kui saad aru järgmisest kümnest lausest ja oskad igaühe kohta ühe arvulise näite tuua, on raamatupidamise olulisim loogika omandatud.

1. **Bilanss kirjeldab seisu kuupäeval.** Mida ettevõte kontrollib (varad), mida ta võlgneb (kohustised) ja mis jääb omanikele (omakapital)?
2. **Kasumiaruanne kirjeldab tulemust perioodil.** Kui palju müüdi, millised kulud selle teenimiseks tekkisid ja kas ettevõte teenis kasumit?
3. **Rahavoogude aruanne kirjeldab raha tegelikku liikumist.** Kust tuli raha ja milleks see kasutati?
4. **Vara = kohustised + omakapital.** Iga korrektne kanne säilitab selle võrduse.
5. **Kasum ei võrdu rahaga.** Arve võib olla esitatud, kuigi klient pole maksnud; kulum vähendab kasumit ilma samal hetkel raha välja viimata.
6. **Tekkepõhisus seob tulu ja kulu õigesse perioodi**, mitte tingimata maksepäevaga.
7. **Ostuhetk ei ole alati kulude tekkimise hetk.** Tööpingi soetamine võib luua vara, mis kulub mitme aasta jooksul; ostetud kaup on kuni müügini varu.
8. **Suurem müügitulu ei tähenda tingimata paremat ettevõtet.** Vaata kasumimarginaale, klientide maksmist ja kapitalivajadust.
9. **Kasum ei tõesta väärtusloomet.** Kapitalil on alternatiivkulu. Kui ettevõte teenib investeeritud kapitalilt vähem kui selle kapitali nõutav tootlus, võib majanduslik väärtus hävida.
10. **Finantsaruanne on mudel, mitte täielik reaalsus.** Hinnangud, klassifitseerimisotsused, aruandlusreeglid ja väljajäänud väärtused mõjutavad pilti.

**Kõige lühem meelespea**:

```text
           BILANSS (seis)
     VARAD = KOHUSTISED + OMAKAPITAL
                  ↑
       KASUM muudab omakapitali
                  ↑
    KASUMIARUANNE (perioodi tulemus)
                  ↕
    RAHAVOOGUDE ARUANNE (raha muutus)
                  ↑
       Tekkepõhised korrigeerimised
```

> **Näide.** Ettevõte müüb detsembris 5 000 € eest teenust ja saab tasu jaanuaris. Detsembris suureneb **müügitulu** 5 000 € ja **nõue ostja vastu** 5 000 €. Detsembri raha ei muutu. Jaanuaris väheneb nõue 5 000 € ja suureneb raha 5 000 €, kuid uut müügitulu ei teki.

## 2. Raamatu kaheksa peatüki kaart

| Raamatu peatükk | Trükitud lk | Keskne küsimus | Mida pead oskama? |
|---|---:|---|---|
| 1. *A guided tour of the financial statements* | 13–26 | Mida kolm aruannet näitavad? | Leida müügitulu, kasum, varad, kohustised ja rahavood. |
| 2. *The need for financial information* | 27–46 | Miks ainult pangakonto ei piisa? | Eristada rahaliikumist, kasumit ja vara väärtust; mõista tekkepõhisust. |
| 3. *Keeping track of economic activity* | 47–64 | Kuidas tehingutest saavad aruanded? | Koostada deebet-kreedit-kandeid ja pearaamatut. |
| 4. *Summary of the foundations of accounting* | 65–84 | Kas suudan aruanded ise kokku panna? | Lahendada tervikliku kahe aasta kande- ja aruandlusülesande loogikat. |
| 5. *The accounts as a lens on growth* | 87–98 | Kuidas kasvu rahastatakse? | Eristada tegevusest teenitud, laenuga rahastatud ja varade müügist saadud kasvu. |
| 6. *Measuring value creation* | 99–110 | Kas ettevõte loob väärtust? | Mõista kapitali tootlust, käivet, marginaali ja majanduslikku kasumit. |
| 7. *Understanding risk* | 111–127 | Millal ettevõte on haavatav? | Arvutada tasuvuspunkti, tegevus- ja finantsvõimenduse mõju. |
| 8. *Building a corporate valuation model* | 128–141 | Kuidas hinnata tulevikku? | Siduda prognoosid, vaba rahavoog, diskonteerimine ja ettevõtte väärtus. |
| Lisa 1. Mõistete sõnastik | 142–152 | Kuidas finantskeelt lugeda? | Tunda põhitermineid nii eesti kui inglise keeles. |

**Barkeri keskne didaktiline mõte:** oluline ei ole üksnes aruanne *koostada*, vaid osata seda *kasutada* majandusotsuseks. Raamat rõhutab ka seda, et aruande väärtuse mõistmiseks peab teadma ettevõtte ärimudelit ja aruandluslike hinnangute piiranguid.

### Mõtlemise areng raamatus

```text
1. Mis aruandes on?
        ↓
2. Miks just nii mõõdetakse?
        ↓
3. Kuidas iga tehing kirjendatakse?
        ↓
4. Kuidas tekivad koondaruanded?
        ↓
5. Kuidas äri kasvab ja kust tuleb raha?
        ↓
6. Kas kapital teenib piisavalt?
        ↓
7. Milliste riskide korral kasum kaob?
        ↓
8. Mida võiks ettevõte väärt olla?
```

## 3. Raamatupidamise mõttemudel

### 3.1 Kolm tegevust: kajastamine, mõõtmine, esitamine

Barker (2. peatükk) jagab arvestusloogika kolmeks: **kajastamine (*recognition*)** — kas nähtus kuulub arvestusse; **mõõtmine (*measurement*)** — milline rahaline väärtus sellele omistada; **esitamine (*presentation*)** — kus ja millises vormis seda näidata.

Näide: ettevõte ostab 4 800 € eest töövahendi.

- **Kajastamine:** ettevõttel on kasutatav ja kontrollitav vara.
- **Mõõtmine:** algne arvestuslik soetusmaksumus on näites 4 800 € (eeldame, et lisakulusid ja käibemaksu erisusi pole).
- **Esitamine:** töövahend kajastub bilansi põhivaras; iga-aastane kulum kasumiaruandes.

Tähelepanu: „ettevõte kasutab midagi“ ei tähenda automaatselt, et see tuleb varana bilanssi panna. Tegelik käsitlus sõltub lepingust ja kohaldatavast standardist — näiteks rendiarvestusel on oma reeglid.

### 3.2 Raha, tulu, kulu, vara ja kohustis ei ole sünonüümid

| Olukord | Raha | Kasum | Bilansi muutus |
|---|---|---|---|
| Omanik investeerib 10 000 € | +10 000 | 0 | Raha +10 000, omakapital +10 000 |
| Pangast võetakse 5 000 € laenu | +5 000 | 0 | Raha +5 000, laen +5 000 |
| Müüakse teenus 2 000 € eest, tasumata | 0 | +2 000 enne seotud kulusid | Nõuded +2 000, omakapital +2 000 |
| Klient tasub varasema arve 2 000 € | +2 000 | 0 | Raha +2 000, nõuded −2 000 |
| Ostetakse põhivara 3 000 € eest | −3 000 | 0 soetamishetkel | Raha −3 000, põhivara +3 000 |
| Arvestatakse põhivara kulum 500 € | 0 | −500 | Vara netoväärtus −500, omakapital −500 |
| Makstakse juba arvestatud arve 700 € | −700 | 0 makse hetkel | Raha −700, võlg −700 |
| Omanikule makstakse dividend 1 000 € | −1 000 | 0 dividendist endast | Raha −1 000, omakapital −1 000 |

Viimase rea puhul võib tekkida **eraldi tulumaksukulu**. Eesti maksustamist selgitatakse 10. peatükis.

### 3.3 Kasum kui netovara muutus

Lihtsustatud olukorras, kui puuduvad omaniku sissemaksed ja väljamaksed:

```text
Kasum = Perioodi lõpu omakapital − Perioodi alguse omakapital
```

Üldisemalt:

```text
Kasum = Lõpu omakapital − Alguse omakapital
        − omanike sissemaksed + omanikele tehtud väljamaksed
        − muud otse omakapitali kajastatud muutused
```

Viimane täpsustus on oluline: **kõik omakapitali muutused ei käi läbi kasumiaruande** (näiteks omaniku investeering või teatud ümberhindlused).

---

## 4. Bilanss, kasumiaruanne, rahavood ja omakapital

### 4.1 Bilanss (*balance sheet / statement of financial position*)

**Küsimus:** milline on ettevõtte finantsseis konkreetsel kuupäeval?

```text
VARAD = KOHUSTISED + OMAKAPITAL
OMAKAPITAL = VARAD − KOHUSTISED
```

| Osa | Mida sisaldab? | Näited |
|---|---|---|
| Käibevara | Raha või tavapärases äritsüklis realiseeruvad varad | Raha, nõuded ostjatele, varud, ettemaksed |
| Põhivara | Pikemalt kasutatavad varad | Masinad, seadmed, tarkvara, kinnisvara |
| Lühiajalised kohustised | Lähiajal täitmisele kuuluvad võlad | Võlad tarnijatele, palgavõlad, maksuvõlad, laenude lühiajaline osa |
| Pikaajalised kohustised | Hilisemal ajal täitmisele kuuluvad kohustused | Pikaajaline laen, teatud rendikohustised |
| Omakapital | Omanike jääknõue netovarale | Osakapital, ülekurss, reservid, jaotamata kasum |

**Näide.** Varad 80 000 €; kohustised 55 000 €; omakapital 25 000 €. Kontroll: `80 000 = 55 000 + 25 000`.

**Oluline piirang:** bilansiline omakapital ei ole sama mis ettevõtte turuväärtus. Raamatupidamislik väärtus sõltub mõõtmisreeglitest, ajaloost ja hinnangutest; mitmed majanduslikult väärtuslikud tegurid (nt tugev kliendisuhe või töötajate oskused) ei pruugi bilansis eraldi varana kajastuda.

### 4.2 Kasumiaruanne (*income statement / profit and loss*)

**Küsimus:** mida ettevõte perioodil teenis ning mis see maksma läks?

| Rida | Summa, € | Selgitus |
|---|---:|---|
| Müügitulu | 100 000 | Kaupade ja teenuste teenitud tulu |
| Müüdud kaupade kulu | −40 000 | Müüdud toodete otsene maksumus |
| **Brutokasum** | **60 000** | Müügitulu miinus müügikulu |
| Palgad ja muud tegevuskulud | −35 000 | Äritegevuse ülalpidamine |
| Kulum | −5 000 | Põhivara kulumi perioodiline kulu |
| **Ärikasum (EBIT)** | **20 000** | Tegevuse tulemus enne intressi ja maksu |
| Intressikulu | −2 000 | Võõrkapitali hind |
| Kasum enne tulumaksu | 18 000 | Finantstulem pärast intressi |
| Tulumaksukulu (illustratiivne) | −3 000 | **Mitte Eesti tavapärane aastakasumi maksustamise skeem** |
| **Puhaskasum** | **15 000** | Aruandeperioodi lõpptulemus |

See on **õppemudel**, mitte Eesti ametlik kasumiaruande skeem. Eesti tegelikus aruandes kasutatakse kohaldatavat esitusviisi ja kontode liigitust. Näite maksukulurida ei tähenda, et Eesti äriühingu aastakasumile arvutataks automaatselt tulumaks.

**Võtmemarginaalid:**

```text
Brutomarginaal = Brutokasum / Müügitulu
Ärikasumi marginaal = Ärikasum / Müügitulu
Puhaskasumi marginaal = Puhaskasum / Müügitulu
```

Näites on brutomarginaal 60%, ärikasumi marginaal 20% ja puhaskasumi marginaal 15%.

> **Tähtis.** Kui ettevõte kasutab kulude esitamiseks teistsugust kasumiaruande skeemi (nt kulud liikide, mitte funktsioonide järgi), ei pruugi „müüdud kaupade kulu“ või „brutokasum“ samal kujul esineda. Võrdlemisel uuri lisasid ja arvestuspõhimõtteid.

### 4.3 Rahavoogude aruanne (*cash flow statement*)

**Küsimus:** miks ettevõtte raha muutus?

| Rahavoo liik | Tähendus | Näited |
|---|---|---|
| **Äritegevuse rahavood (CFO)** | Põhitegevusest tekkinud raha | Klientide laekumised, tasud tarnijatele ja töötajatele |
| **Investeerimistegevuse rahavood (CFI)** | Pikaajaliste varade ja investeeringute soetamine/müük | Masinate ost, vara müük |
| **Finantseerimistegevuse rahavood (CFF)** | Suhted kapitali andjatega | Laenude võtmine/tagasimakse, omanike investeering, dividendid |

```text
Raha muutus = CFO + CFI + CFF
Lõpuraha = Algusraha + Raha muutus
```

*Liigituse üksikasjad, näiteks intresside või dividendide rahavood, võivad standarditi erineda.*

**Näide:** CFO `+30 000`, CFI `−50 000`, CFF `+25 000` → raha muutus `+5 000`. See ei tähenda, et ettevõtte põhitegevus oleks tekitanud 5 000 € kasumit: rahavoog näitab raha päritolu ja kasutamist, mitte tekkepõhist tulusust.

**Otsene meetod:** loetleb klientidelt saadud ja tarnijatele/töötajatele makstud raha. **Kaudne meetod:** alustab kasumist ja korrigeerib seda mitterahaliste kulude ning käibekapitali muutustega.

### 4.4 Omakapitali muutuste aruanne (*statement of changes in equity*)

Barkeri põhiõpetus keskendub kolmele aruandele. **Tänapäevane täiendus:** paljudes täielikes aastaaruannetes on neljas põhiaruanne omakapitali muutuste aruanne.

```text
Alguse omakapital                  100 000
+ aruandeaasta kasum                20 000
+ omanike sissemaksed               10 000
− välja kuulutatud dividendid      −15 000
± muud omakapitalimuutused               0
-----------------------------------------
Lõpu omakapital                   115 000
```

**Kuidas seda lugeda?** Kui omakapital kasvas 15 000 €, aga omanikud panid sisse 10 000 €, ei saa kasvule üksnes ettevõtte kasumit põhjuseks tuua.

### 4.5 Aruannete lisad (*notes*)

Lisad ei ole kõrvalteema. Need selgitavad, **kuidas** näitajad kujunesid: arvestuspõhimõtted, põhivarade eluiga, nõuete allahindlused, võlakohustused, tagatised, eraldised, seotud osapooled, sündmused pärast bilansipäeva ning muud olulised asjaolud. Suurte numbrite taga võivad peituda olulised riskid.

**Aruannete lugemise järjekord (soovitus):** tegevusaruanne → kasumiaruanne → bilanss → rahavood → omakapital → lisad → eelmise aasta võrdlus → konkurentide võrdlus.

---

## 5. Kahekordne kirjendamine ja tekkepõhisus

### 5.1 Deebet ja kreedit ilma müstikata

**Deebet (D/Dr)** ja **kreedit (K/Cr)** on konto kaks poolt. Need **ei tähenda** alati „raha sisse“ ja „raha välja“ ega „hea“ ja „halb“.

| Kontoliik | Suureneb | Väheneb |
|---|---|---|
| Vara | **Deebet** | Kreedit |
| Kulu | **Deebet** | Kreedit |
| Kohustis | **Kreedit** | Deebet |
| Omakapital | **Kreedit** | Deebet |
| Tulu | **Kreedit** | Deebet |

**Kuldreegel:** iga majandustehingu deebetite summa = kreeditite summa.

Näited (kõik summad eurodes):

| Sündmus | Deebet | Kreedit |
|---|---|---|
| Omanik kannab firmasse 8 000 | Raha 8 000 | Osakapital 8 000 |
| Ostetakse kaup 1 200, tasumata | Varud 1 200 | Võlad tarnijatele 1 200 |
| Müüakse kaup 2 000, tasumata | Nõuded ostjatele 2 000 | Müügitulu 2 000 |
| Sama kauba soetusmaksumus oli 900 | Müüdud kaupade kulu 900 | Varud 900 |
| Klient maksab 2 000 | Raha 2 000 | Nõuded ostjatele 2 000 |
| Tasutakse tarnijale 1 200 | Võlad tarnijatele 1 200 | Raha 1 200 |

**Miks müügi kohta kaks kannet?** Üks kirjendab teenitud müügihinna; teine eemaldab laost müüdud kauba väärtuse ja kirjendab selle kuluks. Nii tekib brutokasum `2 000 − 900 = 1 100 €`.

### 5.2 Allikdokument → päevaraamat → pearaamat → aruanded

```text
Leping / arve / kassatšekk / palgaarvestus / pangaväljavõte
                            ↓
                    Algdokumendi kontroll
                            ↓
          Päevaraamatu (journal) deebet-kreedit-kanded
                            ↓
                Pearaamat (general ledger)
                            ↓
                Käibeandmik (trial balance)
                            ↓
    Perioodilõpu korrigeerimiskanded ja inventuur
                            ↓
    Kasumiaruanne + Bilanss + Rahavood + Lisad
                            ↓
                   Analüüs ja otsused
```

**Päevaraamat** sisaldab kronoloogilisi kandeid. **Pearaamat** koondab sama kontoga seotud kanded. **Käibeandmik** kontrollib, kas konto deebet- ja kreeditsaldod on tasakaalus. Tasakaal ei tõesta, et kõik kanded on sisuliselt õiged: vale konto või mõlema poole võrdselt vale summa võib tasakaalu alles jätta.

### 5.3 Tekkepõhine arvestus (*accrual accounting*)

**Näide A — müük arvega.** 20. detsembril väljastatakse tehtud töö eest arve 3 000 €. Maksetähtaeg on 20. jaanuar.

- Detsembris: D Nõuded 3 000 / K Müügitulu 3 000.
- Jaanuaris: D Raha 3 000 / K Nõuded 3 000.
- Mõju: detsembrikuu kasum võib suureneda, detsembri raha mitte.

**Näide B — detsembri elektriarve saabub jaanuaris.** Detsembris tarbiti elektrit 400 € väärtuses.

- Detsembris: D Elektrikulu 400 / K Viitvõlg 400.
- Jaanuaris arve/makse hetkel arveldub võlg, uut detsembri kulu ei teki.

**Näide C — ettemakstud üür.** Ettevõte maksab 1. oktoobril kuue kuu üüri kokku 6 000 €.

- Makse hetkel: D Ettemakstud kulud 6 000 / K Raha 6 000.
- Aasta lõpus kolme kuu kulu: D Üürikulu 3 000 / K Ettemakstud kulud 3 000.
- Aastalõpu bilansis ettemakse 3 000 €.

**Näide D — kliendi ettemaks.** Klient maksab 2 400 € teenuse eest, mida ei ole veel osutatud.

- D Raha 2 400 / K Saadud ettemaksed 2 400 (kohustis).
- Kui teenus osutatakse: D Saadud ettemaksed 2 400 / K Müügitulu 2 400.

### 5.4 Viis küsimust iga kande eel

1. Mis **majanduslikult toimus**, mitte pelgalt milline fail saabus?
2. Millise **perioodi** tulu, kulu või vara muutus see on?
3. Millised kaks või enam **kontot** muutuvad?
4. Kas deebet ja kreedit on **võrdsed**?
5. Millise **algdokumendiga** saab kande hiljem tõendada?


## 6. Üks täielik ettevõttenäide algusest lõpuni

**Tänapäevane, iseseisvalt koostatud harjutus.** Väikeettevõte **Näidis OÜ** müüb kaupu ja osutab teenust. Teeme esimese majandusaasta raamatupidamise nii, et kõik kolm aruannet on omavahel kooskõlas.

**Lihtsustused:** summad on eurodes; käibemaksu, kasumimaksu, palgamaksude, dividendide ja keerukamate arvestusreeglite mõju jäetakse selles *põhimehaanika* näites välja. Eraldi peatükis õpime Eesti käibemaksu ja tulumaksu mõju. Kõik omaniku ja laenu sissemaksed tehakse aasta alguses; laen on pikaajaline; seadme kulum on 3 000 € aastas.

### 6.1 Aasta tehingud

| Nr | Tehing | Eurot | Esmane mõju |
|---:|---|---:|---|
| 1 | Omanik investeerib raha | 20 000 | Raha ja omakapital kasvavad |
| 2 | Võetakse pikaajaline laen | 15 000 | Raha ja kohustised kasvavad |
| 3 | Ostetakse seade pangast tasudes | 12 000 | Raha asendub põhivaraga |
| 4 | Ostetakse kaup tarnijalt arvega | 10 000 | Varud ja tarnijavõlg kasvavad |
| 5 | Müüakse kaupa arvega | 15 000 | Müügitulu ja nõuded kasvavad |
| 6 | Müüdud kauba soetusmaksumus | 6 000 | Varud vähenevad, kulu kasvab |
| 7 | Laekub osa klientide arvetest | 12 000 | Raha kasvab, nõuded vähenevad |
| 8 | Teenitakse ja laekub teenusetulu | 20 000 | Raha ja tulu kasvavad |
| 9 | Makstakse palgakulu | 12 000 | Raha väheneb, kulu kasvab |
| 10 | Makstakse üüri | 4 000 | Raha väheneb, kulu kasvab |
| 11 | Makstakse muid tegevuskulusid | 2 000 | Raha väheneb, kulu kasvab |
| 12 | Tasutakse tarnijatele | 7 000 | Raha ja tarnijavõlg vähenevad |
| 13 | Makstakse intressi | 600 | Raha väheneb, finantskulu kasvab |
| 14 | Arvestatakse seadme aastakulum | 3 000 | Põhivara netoväärtus ja kasum vähenevad |

### 6.2 Päevaraamatu kanded

| Nr | Deebet | Kreedit | Summa |
|---:|---|---|---:|
| 1 | Raha | Osakapital | 20 000 |
| 2 | Raha | Pikaajaline laen | 15 000 |
| 3 | Seadmed | Raha | 12 000 |
| 4 | Varud | Võlad tarnijatele | 10 000 |
| 5 | Nõuded ostjatele | Müügitulu | 15 000 |
| 6 | Müüdud kaupade kulu | Varud | 6 000 |
| 7 | Raha | Nõuded ostjatele | 12 000 |
| 8 | Raha | Teenusetulu | 20 000 |
| 9 | Palgakulu | Raha | 12 000 |
| 10 | Üürikulu | Raha | 4 000 |
| 11 | Muud tegevuskulud | Raha | 2 000 |
| 12 | Võlad tarnijatele | Raha | 7 000 |
| 13 | Intressikulu | Raha | 600 |
| 14 | Kulum | Akumuleeritud kulum | 3 000 |

**Kontrollülesanne:** arvuta iga konto lõppsaldo, grupeerides samad kontod kokku. Raha lõpusaldo peab tulema **29 400 €**.

### 6.3 Kasumiaruanne — vastus

| Kasumiaruande rida | € | Arvutus |
|---|---:|---|
| Kaubamüügi tulu | 15 000 | Tehing 5 |
| Teenusetulu | 20 000 | Tehing 8 |
| **Müügitulu kokku** | **35 000** | 15 000 + 20 000 |
| Müüdud kaupade kulu | −6 000 | Tehing 6 |
| **Brutokasum** | **29 000** | 35 000 − 6 000 |
| Palgakulu | −12 000 | Tehing 9 |
| Üürikulu | −4 000 | Tehing 10 |
| Muud tegevuskulud | −2 000 | Tehing 11 |
| Kulum | −3 000 | Tehing 14 |
| **Ärikasum** | **8 000** | 29 000 − 21 000 |
| Intressikulu | −600 | Tehing 13 |
| **Puhaskasum (õppenäites)** | **7 400** | 8 000 − 600 |

**Tõlgendus.** 35 000 € tulust jäi pärast põhitegevuse kulusid alles 8 000 €. Laenuraha kasutamise kulu 600 € vähendas lõpptulemuse 7 400 euroni. See on kasum, mitte kontol olev raha.

### 6.4 Bilanss — vastus

| Varad | € | Kohustised ja omakapital | € |
|---|---:|---|---:|
| Raha | 29 400 | Võlad tarnijatele | 3 000 |
| Nõuded ostjatele | 3 000 | Pikaajaline laen | 15 000 |
| Varud | 4 000 | **Kohustised kokku** | **18 000** |
| Seadmed soetusmaksumuses | 12 000 | Osakapital | 20 000 |
| Akumuleeritud kulum | −3 000 | Aruandeaasta kasum | 7 400 |
| **Varad kokku** | **45 400** | **Omakapital kokku** | **27 400** |
| | | **Kohustised + omakapital** | **45 400** |

**Bilansikontroll:** `45 400 = 18 000 + 27 400`.

**Mis on äriliselt näha?** Ettevõttel on arvetega müüdud teenuseid/kaupu, mille eest pole veel 3 000 € tasutud. Tarnijatele võlgnetakse 3 000 €. Laen 15 000 € vajab tulevikus tagasimaksmist, ehkki tänavu on kontol 29 400 €.

### 6.5 Rahavoogude aruanne — otsene meetod

| Rida | € |
|---|---:|
| Raha klientidelt (kaup 12 000 + teenus 20 000) | 32 000 |
| Väljamaksed tarnijatele | −7 000 |
| Palgaväljamaksed | −12 000 |
| Üürimaksed | −4 000 |
| Muud tegevusmaksed | −2 000 |
| Intressimaksed (selles õppenäites CFO all) | −600 |
| **Äritegevuse rahavoog (CFO)** | **6 400** |
| Seadme ost (CFI) | −12 000 |
| Omaniku sissemakse (CFF) | +20 000 |
| Laenu saamine (CFF) | +15 000 |
| **Finantseerimise rahavoog (CFF)** | **35 000** |
| **Raha netomuutus** | **29 400** |
| Aasta alguse raha | 0 |
| **Aasta lõpu raha** | **29 400** |

**Kontroll:** `6 400 − 12 000 + 35 000 = 29 400`.

Ettevõtte **tegevus teenis rahaliselt 6 400 €**, kuid tema rahajääk on **29 400 €**, sest sinna kuuluvad ka omaniku sissemakse ja laenurahastamine. *Kõrge rahajääk ei tähenda tingimata tugevat isemajandamist.*

### 6.6 Rahavood — kaudne meetod ja kasumi sild

```text
Puhaskasum                                7 400
+ põhivara kulum (raha ei lahkunud)       3 000
− nõuete kasv (tulu pole laekunud)       −3 000
− varude kasv (varudesse seotud kapital) −4 000
+ tarnijavõlgade kasv (veel maksmata)    3 000
------------------------------------------------
Äritegevuse rahavoog                     6 400
```

**Meelespea:** kaudsel meetodil *lisatakse* mitterahaline kulum tagasi mitte sellepärast, et kulum oleks tulu, vaid seepärast, et see vähendas juba puhaskasumit ilma raha vähendamata.

### 6.7 Kolm kontrolli, mida raamatupidamistarkvara peaks automaatselt tegema

```text
1. Varad − Kohustised − Omakapital = 0
   45 400 − 18 000 − 27 400 = 0

2. Raha lõpus − Raha alguses = CFO + CFI + CFF
   29 400 − 0 = 6 400 − 12 000 + 35 000

3. Omakapital lõpus = Omakapital alguses + sissemaksed + kasum
   27 400 = 0 + 20 000 + 7 400
```

Need kolm võrdust moodustavad kasuliku **andmekvaliteedi testikomplekti**. Õiged võrdused on vajalikud, ent ei välista valesid klassifikatsioone, puuduvaid dokumente, topeltarveid ega pettusi.

---

## 7. Kõik olulised arvestuskontseptsioonid

### 7.1 Tekkepõhisus ja tulude-kulude perioodistamine

- **Tekkepõhisus:** tulu/kulu kajastatakse, kui majanduslik nähtus tekkis, mitte pelgalt siis, kui raha liikus.
- **Periodiseerimine:** 12 kuu kindlustusmakse jagatakse vastavatesse kuudesse; ühe kuu elektrikulu ei kuulu vale aasta kasumisse.
- **Tulude kajastamine (*revenue recognition*):** tulu kajastatakse siis ja ulatuses, mil kaup või teenus on nõuetekohaselt üle antud/osutatud; lepingu tingimused võivad asja keerukamaks teha.
- **Kulude vastavusse viimine tuludega (*matching*):** müüdud kauba soetusmaksumus seotakse selle müügiperioodiga; põhivara kulum jaotatakse selle kasuliku kasutuseale.
- **Olulisus (*materiality*):** väikeste summade puhul võib kasutatav arvestuspõhimõte olla lihtsustatud, kui see ei eksita aruande lugejat.
- **Järjepidevus ja võrreldavus:** sama mõõtmisviisi püütakse periooditi kasutada, või muudatus selgitatakse.
- **Jätkuvus (*going concern*):** arvestus lähtub eeldusest, et ettevõte jätkab tegevust; makseraskuste korral peab seda eeldust hindama.
- **Ettevaatlikkus (*prudence*):** hinnangutes ei tohi vara/tulusid põhjendamatult paisutada ega kohustisi/kulusid põhjendamatult vähendada.
- **Sisu ülimuslikkus vormi suhtes:** tehingu majanduslik sisu võib olla olulisem selle formaalsest nimetamisest.

### 7.2 Varud (*inventory*) ja müüdud kaupade kulu (*COGS*)

Ettevõte ostab 100 ühikut kaupa hinnaga 10 €/tk → varud 1 000 €. Müüb 60 ühikut → müüdud kauba kulu 600 €, allesjäänud varud 400 €. Kui müügihind on 18 €/tk, on müügitulu 1 080 € ja brutokasum 480 €.

**Oht:** kui ladudes on aegunud või müümatu kaup, võib varude bilansiline väärtus vajada allahindamist. Varude hindamisel kasutatakse kohaldatava standardi lubatud meetodeid (nt FIFO või kaalutud keskmine) ning vajadusel neto realiseerimisväärtuse piirangut.

### 7.3 Põhivara ja kulum (*PPE / depreciation*)

Seade maksab 12 000 € ja on kasutatav neli aastat, jääkväärtus eelduslikult 0 €.

```text
Aastane lineaarne kulum = (12 000 − 0) / 4 = 3 000 €
Lõpu bilansiline väärtus pärast 1. aastat = 12 000 − 3 000 = 9 000 €
```

**Kulum ei võrdu seadme turuhinna muutusega.** See on vara kulumi arvestuslik jaotus. Kui vara väärtus on erakorraliselt langenud, võib vajalik olla täiendav **allahindlus (*impairment*)**. Kui vara müüakse, võib tekkida kasum või kahjum sõltuvalt müügihinnast ja bilansilisest väärtusest.

### 7.4 Põhivara soetamine (*CAPEX*) või tegevuskulu (*OPEX*)?

- 12 000 € seadme ost: üldjuhul vara ning hilisem kulum.
- 400 € ühe kuu tarkvaratellimus: tavaliselt perioodikulu (või vajaduse korral ettemakse).
- 20 000 € tarkvaraarendus: **mitte automaatselt põhivara**; otsus sõltub arvestusstandardi nõuetest ning sellest, kas vara kriteeriumid ja usaldusväärne mõõtmine on täidetud.
- Koolitus ja reklaam: sageli jooksva perioodi kulu, mitte „vara“ üksnes võimaliku tulevase kasu tõttu.

### 7.5 Nõuded, laekumised ja krediidirisk

Müügiarve esitab ettevõttele nõude. Kui klient läheb makseraskustesse, ei pruugi nõue olla täielikult laekuv. Siis tuleb hinnata **nõuete allahindluse** vajadust.

**Näide:** 10 000 € nõudest on 2 000 € hinnanguliselt laekumatu. Vajaliku allahindluse korral väheneb nõuete netoväärtus 8 000 euroni ning perioodi kulu suureneb 2 000 € võrra (eeldusel, et varasem allahindlus puudus).

### 7.6 Võlad, viitvõlad, eraldised ja tingimuslikud kohustised

| Mõiste | Millal kasutatakse? | Näide |
|---|---|---|
| Võlg tarnijale (*accounts payable*) | Kaup/teenus on saadud, arve tasumata | Ostuarve 2 000 € |
| Viitvõlg (*accrued liability*) | Kulu kuulub perioodi, kuid veel arveldamata | Detsembri elektrikulu 300 € |
| Eraldis (*provision*) | Kohustis on olemas, kuid summas või ajastuses on ebakindlus | Tõenäoline kohtuvaidluse väljaminek |
| Tingimuslik kohustis (*contingent liability*) | Võimalik kohustus või täitmata kajastamistingimused | Ebatõenäoline nõue, mille kohta võib vaja olla lisa |

**Barkeri 4. peatüki oluline näide:** kohtuvaidlus ja hilisem selle äralangemine näitavad, et raamatupidamine kajastab ka *sündmusi ja hinnanguid*, mitte üksnes pangakandeid. Tegeliku eraldise kajastamisel on olulised kohaldatava standardi tingimused ning usaldusväärne hinnang.

### 7.7 Veel olulisi teemasid, mida praktikas ära tunda

| Mõiste | Lihtne selgitus | Mida aruandes vaadata? |
|---|---|---|
| Immateriaalne põhivara | Kontrollitav pikaajaline mittemateriaalne vara, kui kajastamistingimused täidetud | Tarkvara, õigused, amortisatsioon ja väärtuse langus |
| Firmaväärtus (*goodwill*) | Äriühenduses teatud tingimustel tekkiv soetusmaksumuse ülejääk | Bilansi väärtus, arvestuspõhimõtted ja võimalik allahindlus |
| Rendiarvestus | Rendi mõju varale, kulule ja kohustisele sõltub standardist ning rendiliigist | Rendikohustised, kulud ja lisad |
| Finantsinstrumendid | Raha, nõuded, laenud, võlakirjad jms lepingulised finantsvarad/-kohustised | Tähtaeg, intress, valuuta, riskid, väärtuse hindamine |
| Valuutakursivahed | Võõrvaluutas nõuete ja kohustiste ümberhindlus võib muuta kasumit | Finantstulud/-kulud, valuutapositsioonid |
| Seotud osapooled | Omanike, juhtide ja seotud ettevõtetega tehtud tehingud | Lisades laenud, nõuded, hinnastamine ja saldod |
| Konsolideerimine | Ema- ja tütarettevõtete aruannete koondamine ühtseks majandusüksuseks | Kontserni ja üksikettevõtte aruannete erinevus |
| Edasilükkunud maks (*deferred tax*) | Teatud maksurežiimides arvestus- ja maksubaasi ajutiste erinevuste tulevane maksuefekt | Maksulisa; ei teki igal ettevõttel samal viisil |
| Ebatavalised ja ühekordsed sündmused | Vara müügi kasum, erakorralised trahvid, ümberkorraldused | Jätkusuutliku põhikasumi eristamine |
| Järgnevad sündmused | Aruandekuupäeva järgne oluline info | Kas vajab aruande korrigeerimist või avalikustamist? |

**Praktiline reegel:** kui mõne tehingu kajastamises tekib kahtlus, ära otsusta üksnes „kontode nimetuste“ järgi. Kontrolli lepingu ja tehingu sisu ning seejärel standardit (Eestis RTJ või IFRS).

---

## 8. Kuidas finantsaruandeid analüüsida

Barkeri 1., 5. ja 6. peatükkide meetod: **ära loe ainult ühte numbrit; küsi, kust muutus tuli ja mida see tähendab.** Võrdle vähemalt kahte-kolme aastat ning võimalusel sama sektori ettevõtteid.

### 8.1 Esmalt tee vertikaal- ja horisontaalanalüüs

**Horisontaalanalüüs** — muutus ajas:

```text
Müügitulu kasv % = (Tänavune müügitulu / Mullune müügitulu − 1) × 100
```

Müük 2025: 200 000 €; 2026: 240 000 € → kasv 20%.

**Vertikaalanalüüs** — iga kasumiaruande rida protsendina müügitulust ja bilansi rida protsendina koguvaradest.

```text
Kui müügitulu = 240 000 ja palgakulu = 72 000,
siis palgakulu osakaal = 72 000 / 240 000 = 30%.
```

Müügitulu võib kasvada 20%, kuid kui palgakulu kasvab 40%, väheneb ettevõtte kuluefektiivsus — eeldusel, et muud tegurid jäävad samaks.

### 8.2 Peamiste suhtarvude tabel

| Mõõdik | Valem (lihtsustatud) | Küsimus, millele vastab |
|---|---|---|
| Müügitulu kasv | (Müük_t / Müük_t-1) − 1 | Kas tegevus laieneb? |
| Brutomarginaal | Brutokasum / Müügitulu | Kui palju jääb pärast otseseid müügikulusid? |
| Ärikasumi marginaal | EBIT / Müügitulu | Kui tasuv on põhitegevus? |
| Puhaskasumi marginaal | Puhaskasum / Müügitulu | Kui palju jääb lõpptulemuseks? |
| ROA | Puhaskasum / keskmised varad | Kui tõhusalt varad kasumit teenivad? |
| ROE | Puhaskasum / keskmine omakapital | Mis oli omanike arvestuslik tootlus? |
| ROIC / ROCE | Tegevustulemus / asjakohane keskmine investeeritud kapital | Kas kapital töötab tõhusalt? Täpne lugeja/nimetaja sõltub definitsioonist. |
| Vara käibekordaja | Müügitulu / keskmised varad | Kui suur müük saadakse ühe varaeuro kohta? |
| Lühiajalise maksevõime kordaja | Käibevara / lühiajalised kohustised | Kas lühiajalised varad katavad lühivõlgu? |
| Kiire maksevõime kordaja | (Raha + lühiajalised nõuded) / lühikohustised | Mida saab katta ilma varusid müümata? |
| Võla ja omakapitali suhe | Intressikandev võlg / omakapital | Kui palju kasutatakse laenukapitali? |
| Intresside kattekordaja | EBIT / intressikulu | Kui mugavalt ärikasum katab intressi? |
| DSO – nõuete päevad | Keskmised ostjanõuded / müügitulu × 365 | Kui kiiresti raha klientidelt laekub? |
| DIO – varude päevad | Keskmised varud / müüdud kaupade kulu × 365 | Kui kaua raha on varudesse seotud? |
| DPO – tarnijate päevad | Keskmised tarnijavõlad / asjakohased krediitostud × 365 | Kui kaua võtab tarnijale tasumine? |
| Raha konversioonitsükkel | DSO + DIO − DPO | Kui pikalt rahastab ettevõte äritsüklit? |
| CFO / puhaskasum | Tegevusrahavoog / puhaskasum | Kas kasum toetub rahalaekumistele? |
| CAPEX / kulum | Põhivara investeeringud / kulum | Kas varadesse investeeritakse kulumist enam? |

**Olulised piirangud:**

- Kasuta võimaluse korral **keskmist bilansisaldot**, mitte ainult aasta lõpu saldot. Kui ettevõte kasvas kiiresti, moonutab aasta lõpp suhet.
- ROIC, ROCE ja „net debt“ on levinud eri definitsioonides; võrdle ainult järjepidevalt arvutatud näitajaid.
- EBITDA on **EBIT enne kulumit ja amortisatsiooni**; see ei ole vaba rahavoog ega rahakonto jääk.
- Mõni ettevõte on hooajaline ja mõned sektorid (pangad, kindlustus) nõuavad teistsuguseid näitajaid.
- Suhtarvudele **ei ole universaalset ideaalväärtust**. Võrdle sektori, ärimudeli ja varasemate perioodidega.

### 8.3 DuPonti loogika: miks ROE muutub?

Lihtsustatud kolmekomponendiline seos:

```text
ROE = (Puhaskasum / Müügitulu)
    × (Müügitulu / keskmised varad)
    × (keskmised varad / keskmine omakapital)
```

See näitab kolme allikat:

1. **Kasumlikkus:** kui palju jääb igast müügieurost kasumiks?
2. **Efektiivsus:** mitu müügieurot loob üks varaeuro?
3. **Finantsvõimendus:** kui suurt vara hoitakse ühe omakapitali euro kohta?

**Näide:** 10% puhaskasumi marginaal × vara käibekordaja 1,5 × finantsvõimendustegur 2 = **30% ROE**. See võib olla hea, kuid 30% saavutamine suure laenuga tähendab ka suuremat riski.

### 8.4 Kvaliteetse kasumi kontroll

Kujutame ette kaht ettevõtet, kumbki näitab 100 000 € kasumit:

- **Ettevõte A:** CFO +120 000 €, nõuded stabiilsed, kliendid tasuvad õigel ajal.
- **Ettevõte B:** CFO −70 000 €, ostjanõuded kasvavad väga kiiresti, laekumine aeglustub.

Sama kasumi juures on B-l **suurem rahastamise ja nõuete laekumise risk**. See ei tõesta pettust — kiire kasv ja hooajalisus võivad anda sama mustri — kuid nõuab selgitust.

**Küsi alati:** kas kasum tekkis tavapärasest müügist või ühekordsest varatehingust; kas käibekapital neelab raha; kas kulusid kapitaliseeriti; kas nõudeid hinnati realistlikult; kas seotud osapoolte tehingud on olulised?

### 8.5 Kümme tüüpilist punast lippu

1. Müügitulu kasvab, kuid klientidelt laekunud raha ei kasva.
2. Nõuded suurenevad müügist oluliselt kiiremini.
3. Varude maht suureneb, aga läbimüük aeglustub.
4. Äritegevuse rahavoog on mitu perioodi negatiivne, kuigi kasum on positiivne.
5. Lühiajalised võlad kasvavad kiiremini kui kiiresti realiseeritavad varad.
6. Intressikulu kasvab ja kattekordaja halveneb.
7. Kasv sõltub pidevalt uutest laenudest või osakapitali sissemaksetest.
8. Kasum suureneb pärast arvestuspõhimõtte muutust, mitte ärimudeli paranemist.
9. Suur osa kasumist on seotud ühekordsete sündmustega.
10. Lisades on suured garantiid, kohtuvaidlused, seotud osapoolte laenud või tegevuse jätkuvuse kahtlused.

**Analüütiku kohustus:** punane lipp tähendab kontrollküsimust, mitte süüdistust.


## 9. Kasv, väärtus, riskid ja DCF

See osa võtab kokku **Barkeri raamatu II osa** — peatükid 5–8. Need on eriti väärtuslikud, kui tahad osata aruannetest teha **juhtimis- ja investeerimisotsuseid**, mitte ainult dokumente arvestusse sisestada.

### 9.1 Peatükk 5 — kuidas ettevõte kasvab?

Kasv võib tulla kolmest põhilisest allikast:

1. **Äritegevusest (sisemine rahastamine):** olemasolev ettevõte teenib raha, mis investeeritakse tagasi.
2. **Laenamisest või omanike uuest kapitalist (väline rahastamine):** raha saadakse väljastpoolt.
3. **Olemasoleva raha või varade vabastamisest:** kasutatakse kogunenud raha, müüakse vara või vähendatakse käibekapitali vajadust.

Barker võrdleb peatükis 5 **üheksat erinevat rahavoogude kombinatsiooni**, mille korral rahajääk on kokkuvõttes muutumatu, kuid äride olukorrad on väga erinevad. Näited:

| Ettevõte | CFO | CFI | CFF | Tõlgendus |
|---|---:|---:|---:|---|
| A | +100 | −100 | 0 | Ettevõte investeerib põhitegevuses teenitud raha. |
| B | −100 | 0 | +100 | Laenu või omanike raha kasutatakse jooksva tegevuse kahjumi katmiseks; potentsiaalselt ohtlik. |
| C | −100 | +100 | 0 | Müüakse varasid, et katta tegevuse rahapuudujääki; võib viidata ümberkorraldusele või probleemile. |
| D | 0 | −100 | +100 | Välist rahastust kasutatakse kasvuinvesteeringuks; tasuvus selgub hiljem. |
| E | +100 | 0 | −100 | Teenitud raha kasutatakse laenu tagasimakseks või omanikule väljamakseks. |

**Kõigil viiel rahajäägi muutus on 0** — aga üks võib kasvada, teine nõrgeneda ja kolmas muutuda finantsiliselt turvalisemaks.

**Barkeri teine mõte:** põhivara investeeringut tuleb võrrelda kulumiga. Kui CAPEX = 5 000 € ja kulum = 7 000 €, võib põhivara raamatupidamislik netoväärtus väheneda. See *ei tõesta üksinda* tootmisvõimsuse kahanemist, sest arvesse tuleb võtta hindu, vara kasutust ja tehnoloogilist arengut.

### 9.2 Käibekapital kui kasvamise peidetud hind

**Neto käibekapital** on sageli määratletud kui käibevara miinus lühiajalised kohustised. **Tegevuskäibekapital** on kitsam mõiste, näiteks:

```text
Tegevuskäibekapital ≈ Nõuded ostjate vastu + Varud − Võlad tarnijatele
```

**Näide:** ettevõtte müük kasvab. Nõuded suurenevad 20 000 €, varud 8 000 €, tarnijavõlg 5 000 €.

```text
Käibekapitali lisavajadus = 20 000 + 8 000 − 5 000 = 23 000 €
```

Kui muid tegureid ei ole, peab ettevõte rahastama **23 000 € rohkem** enne, kui sellest müügikasvust raha tagasi tuleb. Nii võib väga edukana näiv ettevõte sattuda likviidsusprobleemi.

### 9.3 Peatükk 6 — kasumlikkus, kapitali tootlus ja majanduslik kasum

**Kasum** näitab eurodes teenitud tulemust. **Kapitali tootlus** näitab, kui hästi kasutati selle kasumi teenimiseks vajalikku kapitali.

```text
Kapitali tootlus = Asjakohane kasum / Asjakohane investeeritud kapital
```

**Näide:** mõlemad ettevõtted teenivad 50 000 € kasumit.

| | A | B |
|---|---:|---:|
| Investeeritud kapital | 250 000 € | 1 000 000 € |
| Kasum | 50 000 € | 50 000 € |
| Lihtsustatud kapitali tootlus | **20%** | **5%** |

Sama suur kasum, väga erinev kapitaliefektiivsus.

Barker näitab, et kapitali tootlust saab parandada **marginaali** või **vara kasutamise efektiivsuse** kaudu:

```text
Kapitali tootlus ≈ (Tegevustulemus / Müügitulu)
                  × (Müügitulu / Investeeritud kapital)
```

**Majanduslik kasum (*economic profit*)** arvestab kapitali alternatiivkulu:

```text
Majanduslik kasum = Tegevustulemus pärast makse
                   − investeeritud kapital × kapitalikulu määr
```

Kui investeeritud kapital = 100 000 €, sobiv tegevustulemus pärast makse = 13 000 € ja kaalutud kapitalikulu = 10%, siis:

```text
Majanduslik kasum = 13 000 − 100 000 × 10% = +3 000 €
```

See on **positiivne väärtusloome**. Kui sama ettevõte teeniks vaid 7 000 €, oleks majanduslik kasum `−3 000 €`, kuigi raamatupidamislik kasum oleks positiivne.

> **Täpsustus.** Barkeri lihtsustatud näidetes võrreldakse vastava investori kapitali ja tema kasumit. Tänapäevases ettevõtte tervikväärtuse analüüsis kasutatakse tihti **NOPAT / investeeritud kapital** ning **WACC** (kaalutud keskmine kapitalikulu). Ära sega omakapitali tootlust (ROE) kogu kapitali kuluga (WACC) ilma vastavate näitajate definitsioone sobitamata.

### 9.4 Peatükk 7 — tegevusvõimendus ja tasuvuspunkt

**Muutuvkulu** suureneb või väheneb koos müügimahuga; **püsikulu** ei sõltu vaadeldaval lühiajalisel perioodil otseselt müügimahust.

```text
Müügihind ühiku kohta = 100 €
Muutuvkulu ühiku kohta = 60 €
Ühikuline kattepanus = 100 − 60 = 40 €
Püsikulud kuus = 4 000 €
Tasuvuspunkt = 4 000 / 40 = 100 ühikut
```

| Müügikogus | Käive | Muutuvkulu | Püsikulu | Ärikasum |
|---:|---:|---:|---:|---:|
| 75 tk | 7 500 € | −4 500 € | −4 000 € | **−1 000 €** |
| 100 tk | 10 000 € | −6 000 € | −4 000 € | **0 €** |
| 150 tk | 15 000 € | −9 000 € | −4 000 € | **2 000 €** |

**Tegevusvõimendus** tähendab, et kõrged püsikulud muudavad ärikasumi müügimahu suhtes tundlikuks. Barkeri 7. peatükk kasutab kulustruktuuri võrdlemiseks püsikulude osakaalu kogukuludes; analüütikas kasutatakse lisaks näiteks dünaamilist mõõdikut:

```text
Tegevusvõimenduse aste (DOL) = Kogu kattepanus / Ärikasum
```

Kui kattepanus on 6 000 € ja ärikasum 2 000 €, siis DOL = 3. See tähendab, et **antud tegevusmahu lähedal ja muutumatu kulu-/hinnastruktuuri korral** toob 1% müügi mahu muutus ligikaudu 3% ärikasumi muutuse. Tasuvuspunkti lähedal võib DOL olla äärmiselt suur või ebasobivalt tõlgendatav.

### 9.5 Finantsvõimendus (*financial leverage*)

Ettevõte ostab vara väärtusega 100 000 €. Põhitegevuse aastane EBIT on 12 000 €.

- **Ilma laenuta:** omakapital 100 000 €, intress 0 €, kasum enne makse 12 000 € → tootlus omakapitalile **12%**.
- **Laenuga:** omakapital 40 000 €, laen 60 000 €, intress 7% ehk 4 200 €, kasum enne makse 7 800 € → tootlus omakapitalile **19,5%**.

Kui EBIT langeb halbadel aegadel **4 000 euroni**, siis võlaga ettevõttes jääb enne makse tulemuseks `4 000 − 4 200 = −200 €`, mis on omakapitalile `−0,5%`. Laen **võimendab** nii häid kui halbu tulemusi.

**Erista kahte riski:** tegevusvõimendus sõltub püsikulude osakaalust ja nõudlusest; finantsvõimendus sõltub laenudest, intressist ja tagasimaksekohustusest.

### 9.6 Peatükk 8 — raha ajaväärtus, NPV, IRR ja DCF

**Raha ajaväärtus:** täna saadav 100 € on tavaliselt väärtuslikum kui sama 100 € mitme aasta pärast, sest raha saab vahepeal investeerida ning tulevik on riskantne.

```text
Tulevase summa nüüdisväärtus: PV = FV / (1 + r)^n

PV — nüüdisväärtus
FV — tulevane rahavoog
r  — sobiv diskontomäär perioodi kohta
n  — perioodide arv
```

**Näide:** aasta pärast saadav 110 € diskontomääraga 10% on täna väärt `110 / 1,10 = 100 €`.

**NPV (*net present value*)** on tulevaste rahavoogude nüüdisväärtuste summa miinus alginvesteering. Kui NPV > 0, loob projekt mudeli eelduste järgi väärtust.

**IRR (*internal rate of return*)** on diskontomäär, mille juures investeeringu NPV = 0. IRR-i võrdlemine kapitalikuluga on üks otsustamise viis; erakorraliste rahavoogude ja omavahel välistavate projektide puhul võib NPV olla usaldusväärsem.

**DCF (*discounted cash flow*)** hindab ettevõtet prognoositud vabade rahavoogude põhjal.

#### Täielik mini-DCF

Eeldame, et firma **vaba rahavoog ettevõttele (FCFF)** järgnevatel aastatel on 15 000, 18 000 ja 21 000 €. WACC = 10%; kasv pärast 3. aastat = 2% aastas. Eeldame matemaatiliselt `WACC > pikaajaline kasv`.

```text
FCFF (aasta 1) = 15 000 €
FCFF (aasta 2) = 18 000 €
FCFF (aasta 3) = 21 000 €
Diskontomäär = 10%
Terminalkasv = 2%
```

Terminalväärtus aasta 3 lõpus (Gordoni kasvumudel):

```text
TV_3 = FCFF_4 / (WACC − g)
     = 21 000 × 1,02 / (0,10 − 0,02)
     = 267 750 €
```

Nüüdisväärtused:

| Komponent | Nüüdisväärtus, € (ümardatud) |
|---|---:|
| Aasta 1 rahavoog | 13 636 |
| Aasta 2 rahavoog | 14 876 |
| Aasta 3 rahavoog | 15 778 |
| Terminalväärtus | 201 165 |
| **Ettevõtte tegevusvara hinnanguline väärtus (EV)** | **245 455** |

**Kui lähtud FCFF-ist ja WACC-ist**, saad üldjuhul ettevõtte väärtuse (*enterprise value*), millest omakapitali väärtuse leidmiseks tuleb teha põhjendatud korrigeerimised, nt:

```text
Omakapitali väärtus ≈ EV − netovõlg ± muud vajalikud korrigeerimised
```

**Kui kasutad omanikele jäävat vaba rahavoogu (FCFE)**, tuleb seda diskonteerida **omakapitali nõutava tootlusega**, mitte WACC-iga. **Neid kahte meetodit ei tohi segi ajada.**

**Vaba rahavoo lihtsustatud sild:**

```text
FCFF ≈ EBIT × (1 − asjakohane maksumäär)
       + kulum
       − CAPEX
       − tegevuskäibekapitali kasv
```

See valem on **üldine finantsanalüüsi mudel**, mitte Eesti kasumimaksu maksuarvestuse algoritm; kohalik maksumudel võib vajada eraldi prognoosi.

**DCF suur risk:** eeldused (kasv, marginaalid, investeeringud, kapitalikulu) võivad tulemust palju muuta. Eriti tundlik on terminalväärtus; ülal moodustab see üle 80% tulemusest. Seepärast arvuta vähemalt kolm stsenaariumi — pessimistlik, baas, optimistlik — ja kontrolli eelduste majanduslikku usutavust.

---

## 10. Eesti raamatupidamine 2026. aastal

**Tänapäevane täiendus, mitte Barkeri 2011. aasta raamatu osa.** Siin on olulised Eesti eripärad seisuga **7.11.2026**. Maksu- ja aruandlusreeglid võivad muutuda; tegelikus töös kontrolli alati ametlikku kehtivat redaktsiooni.

### 10.1 Eesti standardid ja aruandluskohustused

- Eesti ettevõte lähtub sobivast aruandlusraamistikust: **Eesti finantsaruandluse standard (EFS; RTJ juhendid)** või kohaldatavatel juhtudel **IFRS**.
- Raamatupidamise aluseks on **raamatupidamise seadus** ning selle täpsustused; igale majandustehingule peab olema jälgitav algdokument ja põhjendatud kirjend.
- Täismahus raamatupidamise aastaaruanne koosneb **bilansist, kasumiaruandest, rahavoogude aruandest, omakapitali muutuste aruandest ja lisadest**; majandusaasta aruanne sisaldab asjakohasel juhul ka tegevusaruannet.
- **Mikro- ja väikeettevõtja** võivad EFS-i kasutades esitada lühendatud aastaaruande, kus põhiaruanneteks on vähemalt bilanss ja kasumiaruanne ning lisad; tegevusaruande nõue sõltub ettevõtte kategooriast.
- Majandusaasta aruanne esitatakse üldjuhul **kuue kuu jooksul majandusaasta lõpust** e-äriregistri kaudu (kalendriaasta korral tavaliselt 30. juuni).
- Raamatupidamise algdokumente ja asjakohaseid raamatupidamisregistreid tuleb üldjuhul **säilitada seitse aastat** seaduses määratud tähtaja algusest.

**Ajakohane muutus:** 2026. aastal kinnitati EFS-i RTJ juhendite uued redaktsioonid, mida kohaldatakse **aruandeperioodidele, mis algavad 1. jaanuaril 2027 või hiljem**. Seega 2026. aasta aruande ja 2027. aasta aruande koostamisel tuleb jälgida kummale perioodile vastav juhend kehtib. 2026. aasta novembris on täiendav RTJ 17 aktsiapõhiste tasude juhend alles avalikul arutelul; ära eelda, et eelnõu on juba jõustunud.

### 10.2 Käibemaks: ära sega müügituluga

**Eesti üldine käibemaksumäär on alates 1. juulist 2025 24%**. Teatud kaupade ja teenuste puhul on erimäärad või maksuvabastus. Näite all eeldame, et ettevõte on KM-kohustuslane, tegemist on tavapärase 24% maksustatava käibega ja sisendkäibemaks on täielikult mahaarvatav.

**Müügiarve:** teenus 1 000 € + KM 240 € = kliendilt nõutav 1 240 €.

| Deebet | Kreedit | Summa |
|---|---|---:|
| Nõuded ostjatele | Müügitulu | 1 000 € |
| Nõuded ostjatele | Käibemaksukohustis | 240 € |

**Ostuarve:** äritegevuses kasutatav kaup 500 € + KM 120 € = tarnijale võlg 620 €.

| Deebet | Kreedit | Summa |
|---|---|---:|
| Varud või sobiv kulu | Võlad tarnijatele | 500 € |
| Sisendkäibemaksu nõue | Võlad tarnijatele | 120 € |

**Käibemaksu lihtsustatud netoarvutus:** müügilt arvestatud 240 € − lubatud sisendkäibemaks 120 € = **120 €** tasumisele. Tegelik käibemaksuarvestus sõltub maksustamise ajast, tehingu liigist, mahaarvamise õigusest, kreeditarvetest ja muudest tingimustest. See näide ei sobi automaatselt maksudeklaratsiooni koostamiseks.

**KMD** esitatakse käibemaksukohustuslasel üldjuhul iga kuu kohta **järgmise kuu 20. kuupäevaks**; vajaduse korral KMD INF lisaga. TSD on teine deklaratsioon, mida kasutatakse muu hulgas väljamaksete ja nendega seotud maksude deklareerimiseks.

### 10.3 Eesti äriühingu tulumaks — oluline erinevus raamatu lihtsustatud näitest

Barkeri kasumiaruandes on illustratsioon, kus kasumilt arvutatakse kohe maksumääraga tulumaks. **Eesti tavapärases äriühingu mudelis ei maksta tulumaksu lihtsalt sellepärast, et aasta kasum oli positiivne.** Ettevõtte tulumaksukohustus tekib üldjuhul kasumi jaotamisel (nt dividendid) ning teatud muudelt maksustatavatelt väljamaksetelt/kuludelt.

**2026. aastal on tavapärase jaotatud kasumi tulumaksumäär 22/78 netodividendilt.**

**Näide:** firma kuulutab välja / maksab netodividendi 780 € ja kohaldub 22/78 määr.

```text
Tulumaks = 780 × 22 / 78 = 220 €
Omanikule makstav netodividend = 780 €
Ettevõtte kogu rahaline väljaminek = 1 000 €
```

Raamatupidamises on dividend **omakapitali jaotus**, mitte tavapärane põhitegevuse kulu; dividendiga seotud tulumaks kajastatakse eraldi vastavalt kohaldatavale reeglile. Ajaline kajastamine, erandid ja varasemate maksustatud dividendide edasijaotamine võivad nõuda täpsustamist.

### 10.4 E-arved ja digitaalne auditijälg

**Struktureeritud e-arve ei ole lihtsalt e-postiga saadetud PDF.** E-arve sisaldab masinloetavaid arveandmeid, mida saab raamatupidamistarkvarasse importida ja kontrollida.

Eestis laienes 2025. aastal e-arvete „**ostja valib**“ põhimõte: raamatupidamiskohustuslane, kes on e-äriregistris e-arve vastuvõtjaks registreeritud, võib üldreeglina nõuda müüjalt e-arvet, kui osapooled ei ole teisiti kokku leppinud. Täpsed nõuded ja erandid vaata seadusest.

**Praktiline digitaalne kontrollahel:**

```text
E-arve / PDF / ostudokument
  → dokumendi ID ja allika salvestamine
  → tarnija / summa / KM / kuupäeva kontroll
  → kande ettepanek
  → inimese heakskiit (vajadusel)
  → pearaamatu kanne
  → pangamakse sobitamine
  → säilitamine ja auditijälg
```

### 10.5 Eesti tööülesanded, mida lisaks Barkeri raamatule õppida

Barker õpetab **arvestusmudeli loogikat**, kuid *ei ole Eesti raamatupidamis- ega maksukäsiraamat*. Tööalaseks valmisolekuks lisa eraldi järgmised oskused:

- ostu- ja müügiarvete korrektne vormistamine, kreeditarved, ettemaksed;
- käibemaksu-, palga- ja erisoodustuste arvestuse põhimõtted, deklaratsioonide kontroll;
- panga, kassa, klientide ja tarnijate saldode võrdlemine;
- põhivara register, kulumi plaan, inventuur ja varude arvestus;
- kuu- ning aastasulgemine, bilansikontode saldokinnitused;
- sise-eeskiri, dokumendihaldus, ligipääsuõigused, varukoopiad;
- aruande lisad, auditijälg ja e-äriregistrisse esitamine.

**Ametlikud viited:**

1. [Raamatupidamise seadus — Riigi Teataja](https://www.riigiteataja.ee/et/akt/rps)
2. [Raamatupidamise Toimkond ja RTJ juhendid — Rahandusministeerium](https://www.fin.ee/finantspoliitika-valissuhted/arvestusvaldkond/raamatupidamise-toimkond)
3. [Raamatupidamise põhinõuded — Eesti.ee](https://www.eesti.ee/et/artikkel/ettevotlus/raamatupidamine-ja-aruandlus/raamatupidamise-pohinouded)
4. [Majandusaasta aruanne — Eesti.ee](https://www.eesti.ee/et/artikkel/ettevotlus/raamatupidamine-ja-aruandlus/majandusaasta-aruanne)
5. [Algdokumendid ja e-arved — Rahandusministeerium](https://fin.ee/finantspoliitika-valissuhted/arvestusvaldkond/raamatupidamise-algdokumendid-arved-e-arved)
6. [Käibemaksumäärad — Maksu- ja Tolliamet](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/standard-vat-rate)
7. [Dividendide maksustamine — Maksu- ja Tolliamet](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/taxation-dividends)
8. [Käibedeklaratsiooni esitamine — Maksu- ja Tolliamet](https://emta.ee/ariklient/maksud-ja-tasumine/kaibemaks/kaibedeklaratsiooni-ja-aruannete-esitamine/millal-deklareeritakse)
9. [Aastaaruannete keskkond — Registrite ja Infosüsteemide Keskus](https://www.rik.ee/et/e-ariregister/majandusaasta-aruanne)


---

## 11. Kaasaegne töövoog: Excel, SQL, Python ja AI

**Tänapäevane täiendus.** Barkeri raamat annab mõttemudeli; tänapäevane finantsarvestus lisab masinloetavad algdokumendid, struktureeritud andmed, automaatkontrollid ja inimeste ülevaatuse. Ära automatiseeri protsessi, mille sisust sa aru ei saa.

### 11.1 Milline on tänapäevane finantsarvestuse tööpäev?

1. **Hankimine.** Võta vastu e-arved, ostu- ja müügiarved, pangaväljavõtted, lepingud, personalikulu andmed ning ERP-i väljavõtted.
2. **Tuvastamine.** Leia dokumendi kuupäev, majandustehingu sisu, summa, valuuta, maksukood, osapool, maksetähtaeg ja unikaalne ID.
3. **Kontroll.** Otsi dublette, puuduvaid välju, ebatavalisi summasid, vale käibemaksumäära või tundmatut partnerit.
4. **Klassifitseerimine.** Määra õige konto, kuluobjekt, projekt ja periood. Eristada tuleb põhivara, varu, kulu, ettemakse ja kohustist.
5. **Kirjendamine.** Koosta tasakaalus deebet-kreedit-kanne ja seo see algdokumendiga.
6. **Sobitamine.** Võrdle raamatupidamist panga, klientide, tarnijate, lao, maksu- ja põhivararegistriga.
7. **Sulgemine.** Kajasta kulum, viitvõlad, ettemaksed, ümberhindamised ja muud perioodilõpu korrigeerimised.
8. **Aruandlus.** Koosta kasumiaruanne, bilanss, rahavood, lisad, eelarve võrdlus ja juhtimisülevaade.
9. **Analüüs.** Selgita *miks* kasum ja raha erinevad, mis muutus eelmise perioodiga ning millised riskid kerkivad.
10. **Auditijälg.** Säilita andmeallikas, töötlemise versioon, kontrolli tulemus ja kinnituse andja.

### 11.2 Millist tehnoloogiat milleks kasutada?

| Tehnoloogia | Praktiline otstarve | Mida kindlasti kontrollida? |
|---|---|---|
| Excel / Google Sheets | Kiire analüüs, liigendtabel, võrdlus, eelarve | Valemivead, versioonid, käsitsi muudetud lahtrid |
| Python + pandas | Tuhandete kannete puhastamine, koondamine, suhtarvud | Andmetüübid, dubletid, ümardamine, vahekokkuvõtted |
| SQLite / PostgreSQL | Päevaraamat, dokumendid, kontoplaan, püsiv ajalugu | Unikaalsus, võtmed, transaktsioonid, ligipääs |
| Raamatupidamisprogramm / ERP | Päris arvestus, käibemaks, automaatkanded, aruanded | Seaded, integratsioonid, pädev kinnitamine |
| OCR / dokumendiparser | PDF-arvete väljade tuvastamine | OCR-i ebatäpsed summad ja kuupäevad |
| AI / LLM | Selgitused, anomaaliate põhjendused, juhtimisaruande mustand | Väljamõeldud faktid, allikakohasus, konfidentsiaalsus |
| Git + testid | Koodi versioonid ja kontrollitav töövoog | Testandmete privaatsus ja regressioonid |

**Minimaalne algaja tööriistakomplekt:** Excel (või CSV-vaatur), Python 3 Thonnys või Google Colabis ning SQLite. Veebirakendust, masinõpet või suurt andmeladu pole esmaseks väärtuslikuks tööks vaja.

### 11.3 Kaasnev jooksutatav Pythoni harjutus

Õppematerjaliga on kaasas fail **`raamatupidamise_demo.py`**. See töötleb jaotise 6 näidistehinguid ning annab välja kontrollitavad aruanded.

**Käivitamine Thonnys:** ava fail ja vajuta **Run (F5)**. Eraldi väliseid Pythoni pakette vaja ei ole. **Google Colabis:** laadi `.py` üles ja käivita `!python raamatupidamise_demo.py`.

Programm:

- kirjendab deebeti ja kreediti võrdsete summadena;
- arvutab kontode lõppsaldod;
- arvutab müügitulu, kulud ja kasumi;
- kontrollib bilansi tasakaalu;
- võrdleb otsest rahavoogude koondit lõpliku rahasaldoga;
- väljastab kaks faili: `paevik.csv` ja `kontode_saldod.csv`.

**Oodatavad kontrolltulemused:**

```text
Müügitulu:                 35 000 €
Puhaskasum:                 7 400 €
Raha lõppsaldo:            29 400 €
Varad kokku:               45 400 €
Kohustised:                18 000 €
Omakapital:                27 400 €
Bilansivahe:                    0 €
Rahavoogude kontrollivahe:      0 €
```

**Oluline piirang:** demo näitab põhimõtet, mitte täielikku Eesti raamatupidamissüsteemi. Selles ei ole käibemaksuarvestust, autentimist, korralikku auditeerimist, tehingute tühistamisprotsessi, tootmiskõlblikku andmebaasi ega standardipõhist täielikku aastaaruannet.

### 11.4 Üks lihtne SQL-analüüs

Kui sul on SQL-tabel `journal_lines` väljadega `document_id`, `account`, `side`, `amount`, saab iga dokumendi kirjendite tasakaalu kontrollida nii:

```sql
SELECT
    document_id,
    ROUND(SUM(CASE WHEN side = 'D' THEN amount ELSE -amount END), 2) AS vahe
FROM journal_lines
GROUP BY document_id
HAVING ABS(SUM(CASE WHEN side = 'D' THEN amount ELSE -amount END)) > 0.005;
```

**Tõlgendus:** korralikult tasakaalustatud kannete puhul tagastab päring **null rida**. Kui mõni dokument tekib tulemusse, peab selgitama, miks deebeti ja kreediti summad ei võrdu. See kontroll **ei avasta** näiteks õige summaga valel kontol olevat kannet; vaja on täiendavaid sisulisi reegleid.

Päristöö andmebaasis kasuta rahasummade salvestamiseks sobivat kümnendarvu tüüpi (`NUMERIC`/`DECIMAL`), mitte binaarset ujukoma tüüpi.

### 11.5 AI kasutamise kolm mõistlikku taset

**Tase 1 — selgitaja:** küsi finantsmõistete, kanderidade ja suhtarvude kohta. Võrdle vastust algandmetega.

**Tase 2 — kontrolliabiline:** lase AI-l kirjutada SQL- või Pythoni kontrollküsimusi; käivita need ise ja kontrolli tulemust deterministliku testiga.

**Tase 3 — aruande mustandi koostaja:** anna AI-le *anonümiseeritud* arvutatud KPI-de tabel ja palu selgitada trende, riskistsenaariume ning lisaküsimusi. Inimene kinnitab kõik järeldused.

**Kasulikud promptid:**

```text
Oled finantsaruannete analüütik. Analüüsi alljärgnevat bilanssi ja
kasumiaruannet. Kontrolli kõigepealt, kas varad = kohustised +
omakapital. Arvuta kasumi-, likviidsus- ja võimendussuhtarvud.
Selgita iga suhtarvu arvutust ja majanduslikku tähendust.
Eralda kindlad faktid hüpoteesidest. Ära oleta puuduvaid andmeid.
```

```text
Oled raamatupidamise kontrollija. Siin on anonümiseeritud päevaraamat
ja kontoplaan. Leia tasakaalust väljas kanded, dubleeruvad dokumendi-
numbrid, tavatud summad ja võimalikud valed perioodid.
Tagasta tabel: kontroll, kahtlane rida, põhjus, vajalik lisatõend.
Ära paku maksu- ega raamatupidamiskannet lõplikuks kinnitamiseks
ilma inimese kontrollita.
```

```text
Selgita juhatusele ühe lehekülje pikkuselt, miks ettevõtte puhaskasum
kasvas, kuid äritegevuse rahavoog vähenes. Kasuta ainult minu antud
numbrilisi andmeid; iga väite juurde lisa vastav arv ja valem.
Tee eraldi lõik riskide ja võimalike põhjuste kohta, mida aruanded
üksinda ei tõesta.
```

### 11.6 Esimene päriseluline analüüsiprojekt

Võta üks avalikult kättesaadav Eesti ettevõtte majandusaasta aruanne. Koosta CSV, kus iga rida vastab ühele näitajale ja aastale. Tee kolm aruannet kokkuvõtteks ühe A4 pikkune memokiri:

1. *Kas ettevõte teenib kasumit?* Müügitulu kasv, ärikasumi ja puhaskasumi marginaalid.
2. *Kas raha jätkub?* Raha, lühiajalised kohustised, laekumiste ja varude trendid.
3. *Kas kasv on kvaliteetne?* Tegevusrahavoog, investeeringud, võla muutus.
4. *Mis nõuab selgitust?* Kolm numbrit, mis on ebatavalised või mille muutus jäi põhjendamata.
5. *Mida teeksid edasi?* Millised lisad, kontoandmed või võrdlusperioodid on vajalikud?

Märgi memorandumisse, kas tegu on **fakti**, **arvutuse**, **hinnangu** või **kontrollimist vajava väitega**.

---

## 12. Seitsmepäevane õppeplaan ja oskuste test

Soovituslik õppemaht **7 päeva × 2–3 tundi**. Piisab esimeseks iseseisvaks aruandeanalüüsiks, kuid mitte reguleeritud või täieliku raamatupidamisteenuse osutamiseks ilma täiendava väljaõppe ja kontrollita.

| Päev | Teema | Tegevus ja kontrollitav tulemus |
|---|---|---|
| 1 | Kolm finantsaruannet | Selgita suuliselt 1 minuti jooksul, miks kasum ≠ raha |
| 2 | Bilanss ja tekkepõhisus | Tee 10 näidet: vara, kulu, kohustis või omakapital |
| 3 | Deebet ja kreedit | Koosta 15 tehingukannet, kontrolli tasakaalu |
| 4 | Täielik ettevõttenäide | Korda jaotise 6 aruanded ilma vastuseid vaatamata |
| 5 | Finantsanalüüs | Arvuta 10 peamist suhtarvu ja selgita nende piiranguid |
| 6 | Kasv, risk ja väärtus | Lahenda tasuvuspunkti, võimenduse ja DCF-i ülesanne |
| 7 | Python + Eesti praktika | Käivita demo, analüüsi aruannet ja kirjuta memo |

### 12.1 Teadmiste kiirtest

Püüa vastata ilma teksti vaatamata.

1. Millise kuupäeva või perioodi kohta käib bilanss? Aga kasumiaruanne?
2. Miks saab ettevõttel olla kasum 10 000 €, kuid pangas 0 €?
3. Mis vahe on müügitulul ja kliendi maksel?
4. Mis on bilansi põhiidentiteet?
5. Millal suureneb varakonto deebetis ja millal kohustis kreeditis?
6. Mille poolest erinevad ettemakstud üür ja üürikulu?
7. Mis on kaubamüügi brutokasum?
8. Milleks on vaja põhivara kulumit, kui raha selle arvestamisel ei välju?
9. Mis on äritegevuse, investeerimise ja finantseerimise rahavoogude vahe?
10. Miks võib kiire kasv põhjustada rahapuuduse?
11. Millal loob ettevõte majanduslikku väärtust: kas siis, kui kasum on positiivne, või siis, kui kapitali tootlus ületab kapitalikulu?
12. Kuidas suurendab suur püsikulude osakaal tegevusriski?
13. Miks võib väga suur võlakoormus muuta omakapitali tootluse kõikuvaks?
14. Millist diskontomäära kasutad FCFF-i korral ja millist FCFE puhul?
15. Miks ei tohi Eesti äriühingu kasumimaksu arvutada automaatselt Barkeri raamatu 30% näite järgi?

### 12.2 Arvulised ülesanded

**Ülesanne A — tekkepõhisus.** Ettevõte osutab detsembris teenust 4 000 € eest, saab detsembris 1 500 € ja jaanuaris ülejäänud 2 500 €. Kui suur on detsembri tulu, nõue aasta lõpus ja detsembri rahaline laekumine?

**Ülesanne B — kaubamüük.** Ettevõte ostis 40 ühikut 25 €/tk. Müüs 30 ühikut hinnaga 40 €/tk. Kui suur on müügitulu, müüdud kauba kulu, brutokasum ja lõppvaru?

**Ülesanne C — bilanss.** Varad on 80 000 €, kohustised 46 000 €. Kui suur on omakapital? Seejärel teenib ettevõte 6 000 € kasumit, kuid maksab omanikele 2 000 € dividendi (ignoreeri maksuarvestust). Kui suur on uus omakapital, kui muid muutusi ei ole?

**Ülesanne D — tasuvuspunkt.** Toote hind 50 €, muutuvkulu 30 €/tk, aastased püsikulud 20 000 €. Mitu ühikut on vaja müüa nullkasumi saavutamiseks? Kui suur on ärikasum 1 300 müüdud ühiku korral?

**Ülesanne E — tootlus ja väärtus.** Investeeritud kapital 100 000 €, ärikasum pärast arvestuslikku ettevõtte tulumaksu (NOPAT) 12 000 €, WACC 9%. Leia ROIC ja majanduslik kasum.

### 12.3 Vastused ja lühiselgitused

<details>
<summary><strong>Ava kiirtesti ja arvutusülesannete vastused</strong></summary>

**Teadmiste test:**

1. Bilanss: seis kindlal kuupäeval. Kasumiaruanne: tulemus perioodi jooksul.
2. Kasum sisaldab ka laekumata nõudeid ja mitterahalisi kuluarvestusi ning ettevõte võib raha kulutada investeeringuteks või võlgade tasumiseks.
3. Tulu tekib tehingu majandusliku sisu ja kajastamisreeglite järgi; makse muudab raha ja nõude saldot.
4. Varad = kohustised + omakapital.
5. Vara kasvab deebetis; kohustis kasvab kreeditis.
6. Ettemaks on tulevase perioodi vara, üürikulu on juba tarbitud perioodi kulu.
7. Müügitulu miinus müüdud kauba soetusmaksumus.
8. Kulum jaotab põhivara amortiseeritava maksumuse kasutusperioodidele; ei ole perioodi makse.
9. Põhitegevuse laekumised ja maksed / pikaajaliste varade soetamine-müük / kapitali kaasamine-tagastamine.
10. Kasv võib nõuda varusid ja krediteeritud müüki enne klientidelt raha laekumist.
11. Majanduslik väärtus luuakse, kui investeeritud kapitali tootlus ületab asjakohase kapitalikulu.
12. Müügi languse korral ei vähene püsikulud samas tempos, mistõttu kasum langeb järsult.
13. Intressid tuleb tasuda sõltumata tulemusest ja omanike kapitali osakaal on väiksem.
14. FCFF: WACC. FCFE: omakapitali nõutav tootlus.
15. Eesti maksusüsteemi põhiloogika ja maksuobjekt erinevad raamatu illustratsioonist.

**Arvutusülesanded:**

- **A:** detsembri tulu = **4 000 €**, nõue 31.12 = **2 500 €**, detsembri laekumine = **1 500 €**.
- **B:** müügitulu `30 × 40 = 1 200 €`; COGS `30 × 25 = 750 €`; brutokasum `450 €`; varu `10 × 25 = 250 €`.
- **C:** algomakapital `80 000 − 46 000 = 34 000 €`; lõppomakapital `34 000 + 6 000 − 2 000 = 38 000 €`.
- **D:** ühiku kattepanus `50 − 30 = 20 €`; tasuvuspunkt `20 000 / 20 = 1 000` ühikut. 1 300 ühiku korral ärikasum `1 300 × 20 − 20 000 = 6 000 €`.
- **E:** ROIC `12 000 / 100 000 = 12%`; majanduslik kasum `12 000 − (100 000 × 9%) = 3 000 €`.

</details>

**Töövalmiduse kontroll:** suudad õppematerjali eesmärgi praktiliselt täita, kui oskad 1) tehinguid kirjendada, 2) aruannete kooskõla testida, 3) iga olulise muutuse kohta majandusliku selgituse anda ning 4) näidata, milline algdokument või standard järeldust toetab. Maksuarvestuse ja pärisettevõtte aruandluse iseseisvaks tegemiseks on vaja täiendavaid erialaseid teadmisi.

---

## 13. Mõistete sõnastik

| Mõiste eesti keeles | Inglise keeles | Ühe lausega selgitus |
|---|---|---|
| Raamatupidamine | Accounting | Majandustehingute mõõtmine, kajastamine ja finantsinfo esitamine |
| Finantsarvestus | Financial accounting | Peamiselt välistele kasutajatele suunatud arvestus ja aruandlus |
| Juhtimisarvestus | Management accounting | Juhtimisotsuste toetamiseks loodud sisemine info |
| Majandustehing | Transaction | Sündmus, mis muudab ettevõtte finantsseisu või -tulemust |
| Algdokument | Source document | Tõend, mis aitab kirjendatud tehingu sisu ja toimumist kontrollida |
| Kontoplaan | Chart of accounts | Ettevõttes kasutatavate kontode süstematiseeritud loend |
| Päevaraamat | Journal | Kronoloogiline raamatupidamiskannete loend |
| Pearaamat | General ledger | Tehingute koondamine kontode kaupa |
| Käibeandmik | Trial balance | Konto saldode koond, mis võimaldab tasakaalu kontrolli |
| Deebet | Debit, Dr | Konto üks pool; varad ja kulud kasvavad tavaliselt siin |
| Kreedit | Credit, Cr | Konto teine pool; tulud ja kohustised kasvavad tavaliselt siin |
| Kahekordne kirjendamine | Double-entry bookkeeping | Igal kandel on võrdses summas deebet ja kreedit |
| Tekkepõhisus | Accrual accounting | Tulud ja kulud kajastatakse seotud perioodil, mitte lihtsalt maksepäeval |
| Kassapõhisus | Cash accounting | Tehingud kajastatakse raha liikumise põhjal |
| Bilanss | Balance sheet | Ettevõtte varade, kohustiste ja omakapitali seis kuupäeval |
| Kasumiaruanne | Income statement | Perioodi tulud, kulud ja kasum või kahjum |
| Rahavoogude aruanne | Cash flow statement | Raha ja raha ekvivalentide liikumise selgitus |
| Aruannete lisad | Notes to financial statements | Arvestuspõhimõtted, detailid, riskid ja selgitused |
| Vara | Asset | Kontrollitav majanduslik ressurss, millest eeldatakse kasu |
| Kohustis | Liability | Minevikusündmusest tulenev praegune kohustus, mis tuleb täita |
| Omakapital | Equity | Varade ja kohustiste vahe ehk omanike jääkosalus |
| Käibevara | Current assets | Vara, mis realiseerub tavapärases äritsüklis või lähiajal |
| Põhivara | Non-current assets / PPE | Pikaajaliseks kasutuseks soetatud vara |
| Nõuded ostjatele | Accounts receivable | Klientide tasumata arved ja muud nõuded |
| Võlad tarnijatele | Accounts payable | Tarnijate ees olevad maksekohustused |
| Varud | Inventories | Müügiks või tootmiseks hoitavad kaubad ja materjalid |
| Müügitulu | Revenue / sales | Perioodil teenitud kaupade ja teenuste müügitulu |
| Kulu | Expense | Perioodil kasumit vähendav majandusliku kasu vähenemine |
| Müüdud kaupade kulu | Cost of goods sold | Müüdud kaupade soetus- või tootmiskulu |
| Brutokasum | Gross profit | Müügitulu miinus müüdud kauba kulu |
| Ärikasum | Operating profit / EBIT | Põhitegevuse kasum enne intresse ja tavapärases mudelis maksu |
| Puhaskasum | Net profit / net income | Perioodi lõpptulemus pärast kajastatud kulusid ja makse |
| Kulum | Depreciation | Materiaalse põhivara amortiseeritava maksumuse jaotamine perioodidele |
| Amortisatsioon | Amortisation | Immateriaalse vara maksumuse perioodidele jaotamine |
| Allahindlus | Impairment / write-down | Vara bilansilise väärtuse vähendamine nõutava hinnangu alusel |
| CAPEX | Capital expenditure | Pikaajaliste varade omandamiseks või parendamiseks tehtud investeering |
| OPEX | Operating expenditure | Igapäevase tegevusega seotud kulutused; arvestuslik käsitlus võib erineda |
| Käibekapital | Working capital | Tavaliselt käibevara ja lühiajaliste kohustiste vahe |
| Tegevuskäibekapital | Operating working capital | Tegevusega seotud nõuete ja varude ning tegevuskohustiste netosumma |
| Likviidsus | Liquidity | Võime katta lähiajal tasumisele tulevaid kohustusi |
| Maksevõime | Solvency | Võime täita kohustusi pikema aja jooksul |
| Raha konversioonitsükkel | Cash conversion cycle | Aeg varude ja klientide rahaks muutumisest, arvestades tarnijatele maksmist |
| ROA | Return on assets | Kasumi ja varade suhtele tuginev tootlusnäitaja |
| ROE | Return on equity | Puhaskasum jagatud keskmise omakapitaliga |
| ROIC | Return on invested capital | Tegevustulemi maksujärgne tootlus investeeritud kapitalilt |
| WACC | Weighted average cost of capital | Võõr- ja omakapitali nõutava tootluse kaalutud keskmine |
| Majanduslik kasum | Economic profit | Kapitalikuluga korrigeeritud majanduslik tulemus |
| Tegevusvõimendus | Operating leverage | Püsikuludest tulenev kasumi tundlikkus müügimahu suhtes |
| Finantsvõimendus | Financial leverage | Laenukapitali kasutamisest tulenev omanike tootluse võimendumine |
| Kattepanus | Contribution margin | Müügitulu miinus muutuvkulud |
| Tasuvuspunkt | Break-even point | Müügimaht, kus tulud katavad kõik arvestatud kulud |
| Vaba rahavoog | Free cash flow | Raha, mis jääb pärast vajalikke investeeringuid ja käibekapitali muutust |
| FCFF | Free cash flow to the firm | Kapitali pakkujatele tervikuna kättesaadav modelleeritud vaba rahavoog |
| FCFE | Free cash flow to equity | Omakapitali omanikele kättesaadav modelleeritud vaba rahavoog |
| NPV | Net present value | Tulevaste rahavoogude nüüdisväärtuste summa miinus alginvesteering |
| DCF | Discounted cash flow | Väärtuse hindamine tulevaste rahavoogude diskonteerimise abil |
| EBITDA | Earnings before interest, taxes, depreciation and amortisation | Kasuminäitaja enne intresse, makse, kulumit ja amortisatsiooni |
| EFS | Estonian Financial Reporting Standard | Eesti finantsaruandluse standard |
| RTJ | Estonian Accounting Standards Board guidance | Raamatupidamise Toimkonna juhend |
| IFRS | International Financial Reporting Standards | Rahvusvahelised finantsaruandlusstandardid |
| E-arve | Structured electronic invoice | Masinloetavaid arveandmeid sisaldav elektrooniline arve |
| Auditijälg | Audit trail | Kontrollitav seos sündmusest algdokumendi ja aruandeni |

---

## 14. Allikad ja edasine õppimine

### 14.1 Põhiraamat

**Richard Barker (2011).** *Short Introduction to Accounting*. Cambridge University Press. Kasutatud kasutaja esitatud 172-leheküljelist PDF-i. Raamatu trükilehekülgedel olevate põhimõistete mõistmiseks on kõige olulisemad järgmised osad:

| Lugemisvajadus | Raamatu peatükk | Trükitud leheküljed |
|---|---|---|
| Tervikpilt kolmest aruandest | 1 | 13–26 |
| Miks kasum erineb rahast? | 2 | 27–46 |
| Deebet, kreedit, pearaamat | 3 | 47–64 |
| Terviklik näide mitme perioodiga | 4 | 65–84 |
| Kasvu mõju rahale ja bilansile | 5 | 87–98 |
| Kapitali tootlus ja väärtusloome | 6 | 99–110 |
| Tegevus- ja finantsrisk | 7 | 111–127 |
| Rahavoogude prognoos ja ettevõtte väärtus | 8 | 128–141 |
| Ingliskeelsete mõistete kordamine | Lisa 1 | 142–152 |

### 14.2 Ametlikud Eesti allikad

- [Raamatupidamise seadus — Riigi Teataja](https://www.riigiteataja.ee/et/akt/rps)
- [Raamatupidamise Toimkond ja ajakohased RTJ-d — Rahandusministeerium](https://www.fin.ee/finantspoliitika-valissuhted/arvestusvaldkond/raamatupidamise-toimkond)
- [Käibemaksu alused ja määrad — Maksu- ja Tolliamet](https://www.emta.ee/ariklient/maksud-ja-tasumine/kaibemaks)
- [Dividendide ja omakapitali väljamaksete maksustamine — Maksu- ja Tolliamet](https://emta.ee/ariklient/maksud-ja-tasumine/tulumaks-ja-sotsiaalmaks/dividendide-ja-omakapitali-valjamaksete)
- [Algdokumendid ja e-arved — Rahandusministeerium](https://www.fin.ee/finantspoliitika-valissuhted/arvestusvaldkond/raamatupidamise-algdokumendid-arved-e-arved)
- [Majandusaasta aruannete esitamine — RIK](https://www.rik.ee/et/e-ariregister/majandusaasta-aruanne)

### 14.3 Soovitatav jätkuprojekt: „Finantsaruannete analüütik“

Loo avalike aruannete peale isiklik tööriist, mille neli osa on:

1. **Andmesisend:** CSV või XLSX avalikust finantsaruandest.
2. **Automaatkontroll:** bilansi võrdsus, puuduolevad perioodid, ilmsed summavead.
3. **Analüüsimootor:** kasv, marginaalid, likviidsus, võla suhtarvud, rahavoogude sild.
4. **Juhtimisraport:** üks leht faktide, arvutuste, riskide ja kontrollimist vajavate hüpoteesidega.

Kõigepealt ehita see lihtsa Python + CSV lahendusena. Lisa SQL või veebileht alles siis, kui see parandab kontrollitavust või kasutusmugavust. Lisa AI viimases etapis, et saada mõistetavaid seletusi, mitte asendada deterministlikke arvutusi.

**Lõppjäreldus.** Raamatupidamise põhisamm ei ole kontonumbri meeldejätmine. See on oskus võtta üks majandussündmus, kirjendada see õigesse perioodi, selgitada selle mõju **kasumile**, **rahale** ja **bilansile**, kontrollida saadud numbreid ning nende põhjal teha põhjendatud otsus.
