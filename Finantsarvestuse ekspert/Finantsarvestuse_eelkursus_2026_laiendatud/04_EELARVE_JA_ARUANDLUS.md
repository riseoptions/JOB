# 04. Eelarve täitmise analüüs ja aruandlus

## Eelarve ei ole pangakonto

Eelarve annab teatud eesmärkidel ja tingimustel kavandatud rahalise raami. **Tekkepõhine kulu**, **tegelik makse** ja **eelarve täitmine** on erineva tähendusega mõisted. Analüüs on usaldusväärne ainult juhul, kui võrdled sama perioodi, asutust, liigitust ja arvestusalust.

## Miniandmestik (sünteetiline)

| Kululiik | Aasta eelarve | Perioodi eelarve | Perioodi täitmine |
|---|---:|---:|---:|
| IT-teenused | 60 000 € | 45 000 € | 48 000 € |
| Koolitused | 30 000 € | 22 500 € | 17 000 € |
| Lähetused | 20 000 € | 15 000 € | 12 000 € |
| **Kokku** | **110 000 €** | **82 500 €** | **77 000 €** |

**Oluline:** tabel on mõeldud arvutusoskuse harjutamiseks. Päris eelarve täitmise aruandes tuleb kontrollida veergude määratlusi ja liigitust.

## Arvutused

1. **Perioodi täitmine %** = `perioodi täitmine / perioodi eelarve × 100` (kui nimetaja on positiivne).
2. **Hälve eurodes** = `perioodi täitmine − perioodi eelarve`.
3. **Hälve %** = `hälve / perioodi eelarve × 100` (kui nimetaja on positiivne).
4. **Jääk** = `perioodi eelarve − perioodi täitmine` (vaid sobival võrreldaval alusel).

IT-teenuste näide:

- Täitmine = 48 000 / 45 000 × 100 = **106,67%**.
- Hälve = 48 000 − 45 000 = **+3000 €**.
- Mida see tähendab? Selle **harjutuse perioodieelarve** ületamine, kuid mitte veel automaatselt eelarvereegli rikkumine või aastaeelarve ületamine.

Kogusummas on täitmine 77 000 / 82 500 × 100 = **93,33%** ja hälve **−5500 €**.

## Ära tee neid tõlgendusvigu

- **Aasta eelarve vs 9 kuu täitmine** ilma planeeritud hooajalisust arvestamata võib eksitada.
- **Erinevad perioodid** (I–III kvartal vs aasta) ei ole otse võrreldavad.
- **Erinevad kululiigid** või ümberklassifitseerimised muudavad võrdluse sisutuks.
- **Negatiivsed kirjendid ja tagastused** võivad tulemit muuta.
- **Eelarve muudatused**: algne ja viimati kinnitatud eelarve võivad erineda.
- **Koondandmed** ei võimalda iseenesest tõestada konkreetse arve õigsust.

## Praktiline analüütiku töövoog

1. Pane kirja küsimus: „Mis põhjustab IT-teenuste perioodieelarve ületamise?“
2. Kontrolli allika avaldamise kuupäeva ja kas näitaja on tegelikult võrreldav.
3. Filtreeri sama kululiigi, asutuse ja perioodi kirjed.
4. Koosta Pythonis koond ja hälbed.
5. Võrdle lepingute, ajastuse ja ühekordsete kulude kontekstiga.
6. Kirjelda tulemus eelduste ja piirangutega: „Perioodihälve +3000 €, võimalik põhjus ...; kinnitamiseks vajame alusdokumente.“

## Pärisandmete leidmine

Rahandusministeeriumi [2026. aasta riigieelarve lehel](https://www.fin.ee/riigi-rahandus-ja-maksud/riigieelarve-ja-eelarvestrateegia/2026-riigieelarve) on kättesaadavad muu hulgas eelarve seaduse XLSX ning eelarve täitmise XLSX-failid. Seisuga 05.11.2026 oli seal olemas **2026. aasta septembri täitmine majandusliku sisu järgi**. Failide struktuuri tuleb enne analüüsi vaadata – ära eelda, et väljad vastavad meie näidistabelile.

**Harjutus:** laadi ametlik XLSX alla ja käivita `kood/avaliku_xlsx_uurimine.py`. Vaata lehtede nimesid ja veergude paigutust, seejärel esita 3 küsimust, millele andmed lubavad vastata, ja 2 küsimust, millele need ei luba vastata.

## Miks Python Exceli kõrval?

Python tagab sageli:

- korratava ja testitava arvutusloogika;
- automaatse suuremahulise andmepuhastuse;
- võrreldavate perioodide sidumise;
- sama aruande genereerimise ühtse reeglistiku järgi.

Excel on endiselt kasulik lõppkasutaja jaoks: kinnitatud tabelite vaatamine, otsused, manuaalne kontroll ja kontrollitava aruande edasiandmine.
