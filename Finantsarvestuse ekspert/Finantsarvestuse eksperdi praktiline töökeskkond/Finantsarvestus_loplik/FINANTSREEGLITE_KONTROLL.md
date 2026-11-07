# Finantsarvestuse sisuline kontroll

Ametlike allikate kontroll 06.11.2026, dokumendi taastamine 07.11.2026. Tegemist on õppeprojekti ülevaatusega, mitte audiitori arvamusega.

## Ametlik alus ja piirid

| Allikas | Kontrollitud põhimõte | Mõju projektile |
|---|---|---|
| [RM riigi raamatupidamine](https://www.fin.ee/riigi-rahandus-ja-maksud/riigi-raamatupidamine) | Riigi arvestus on tekkepõhine | Kulu ja makse aeg eristatakse |
| [RPS](https://www.riigiteataja.ee/et/akt/rps), [RM algdokumendi selgitus](https://fin.ee/finantspoliitika-valissuhted/arvestusvaldkond/raamatupidamise-algdokumendid-arved-e-arved) | Tehing peab olema dokumenteeritud ja arusaadav; asutus vajab sise-eeskirja | CSV kuju ei ole täielik õiguslik kontroll |
| [Avaliku sektori finantsarvestuse ja -aruandluse juhend](https://www.riigiteataja.ee/akt/103012025007) | Otsinguindeks näitas 06.01.2025 jõustunud teksti hetkel kehtivana | DEMO-kontod ei ole tegelik kontoplaan |
| [Juhendi 2022 tervikteksti §15](https://www.riigiteataja.ee/akt/109122022029) | Dokumendi sisu, periood, eelarve, vastaspool ning vastutuste lahusus | Ajalooline tekst toetab raamistikku, ei tõenda üksinda praegust nõuet |
| [EMTA määrad](https://www.emta.ee/ariklient/maksud-ja-tasumine/kaibemaks/kaibemaksumaarad-ja-maksuvaba-kaive/uldine-kaibemaksumaar) ja [üleminekunäited](https://www.emta.ee/ariklient/maksud-ja-tasumine/kaibemaks) | Standardmäär 24% alates 01.07.2025; määr sõltub käibe ajast ja käsitlusest | Lubatud näidismäärade loend ei otsusta maksualust |
| [RTK teenus](https://www.rtk.ee/finantsarvestus-personaliteenus/arvestusteenused/finantsarvestus) | Jagatud teenus ja kliendipõhine toimemudel; SAP ning toetavad süsteemid | Demo rollid ei tõenda HTM tegelikku kinnitusringi |

Riigi Teataja otseste lehtede ja PDF-aadressi täisteksti lugemist takistas JavaScripti nõue. Ei kinnitata kõigi paragrahvide sõnasõnalist ajakohasust. Enne päriskasutust tuleb kontrollida kehtivat tervikteksti, HTM sise-eeskirja ja toimemudelit; viimaseid ei olnud sisendina. RM eelarvemetoodika varasem süvalink suunas üldlehele ega tõenda kahe mõõdiku võrreldavust.

## 18 kontrollitavat juhtumit

Väikeste summadega näited on sünteetilised. Automaatkontrollid asuvad testid/test_etapp2.py, test_etapp3.py ja test_etapp5.py. Tõlgendusjuhtumeid ei esitata automaattestidena.

| ID | Sisend | Oodatud tulemus ja põhjendus | Kontroll |
|---|---|---|---|
| F01 | Teenus 31.10, arve 02.11, makse 16.11 | Kulu teenuse perioodis; makse eraldi. PERIOOD on hoiatus | test_period_warning; makset ei modelleerita |
| F02 | Neto 1000, KM 240, bruto 1240 | Summad klapivad | Etapi 2 tervikvoog |
| F03 | Sama, bruto 1240,01 | SUMMA: 0,01 vastuolu | Impordiproov, etapi 2 test |
| F04 | Neto 0,50; 13% | 0,065 → 0,07; bruto 0,57 | test_half_cent |
| F05 | Sama tarnija, „X” ja „ x ”; eri ID-d | Mõlemale DUPLIKAAT, mitte pettuseotsus | Etapi 2 duplikaaditest |
| F06 | Eri tarnijad, sama arvenumber | Ei ole sama duplikaadivõti | test_other_supplier |
| F07 | Eelarve 10000, täitmine 6000 | 60%, jääk 4000; mitte automaatselt sääst | budget_metrics ja tõlgendus |
| F08 | Eelarve 0, kulu 100 | Protsent puudub; jääk −100 | test_zero_overspend |
| F09 | Eelarve 100, kulu 120 | 120%, jääk −20 | test_zero_overspend |
| F10 | Puuduv rahaväärtus | Katkestus, mitte null | test_missing_bool |
| F11 | 2026-02-29 | KUUPAEV: pole liigaasta | test_bad_date_missing |
| F12 | 1000+240, näites KM pole mahaarvatav | D kulu 1000+D KM-kulu 240=K võlg 1240 | accept_transfer, tasakaalutest |
| F13 | Abikõlblik 3000, 80%, ettemakse 3000 | Teenitud 2400, näitlik tagasinõue 600 | Etapi 3 toetusetest |
| F14 | Abikõlblik 10000, 80%, lagi 7000 | Toetus min(8000,7000)=7000 | grant_result, käsitsi valemikontroll |
| F15 | Augusti sama mõõdiku koondid | 772600007 / 1207523833 ×100 ≈63,98% | test_built_financial_contract |
| F16 | Septembri kulud+investeeringud 886184288,61 | Ei jagata automaatselt augusti kulueelarvega | Vaadete metoodiline lahusus |
| F17 | 2025 tehingu 22% kreeditarve | Võib olla õige, kuid demo ei toeta 22%/negatiivset summat | Teadlik ulatuspiir |
| F18 | Tähtaeg möödas, makseinfo puudub | ULETAHTAJA hoiatus, mitte tõend tasumata arvest | Olemasolev kuupäevatest |

Raha hoitakse sentides, ümardus on Decimal ROUND_HALF_UP. Arvemudel on ühe rea ja ühe määraga. Nullmäär ja maksuvabastus, sisendkäibemaks, segakasutus, pöördmaksustamine, kreeditarved ning ajaloolised määrad vajavad eraldi käsitlust. Mittemahearvatava KM näidiskanne ei tähenda, et avaliku sektori KM oleks alati kulu. Tasakaalus kanne ei tõenda õiget kontot ega tegelikku tarnet.

Koondridu ja detaile ei liideta. Kasutamata aastaeelarve ei ole perioodi sääst. Sünteetilised arved ei ole avaliku HTM koondi detailid. Kontrollsumma tõendab failiversiooni, mitte kogu riigiarvestuse õigsust.
