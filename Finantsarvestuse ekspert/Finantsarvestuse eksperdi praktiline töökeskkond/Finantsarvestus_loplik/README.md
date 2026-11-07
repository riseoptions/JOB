# Finantsvaade – finantsarvestuse praktiline õppeprojekt

**Versioon 0.5 · etapid 1–5 · 7. november 2026.** Eestikeelne veebirakendus ühendab avalike finantsandmete analüüsi, sünteetiliste ostuarvete kontrolli, Pythonit ja SQL-i. Projekt on valminud AI abil; kandidaat peab suutma valitud arvutusi ja kontrollireegleid ise selgitada. See ei ole HTM-i ega RTK ametlik infosüsteem.

[Veebirakendus](https://finantsarvestus-risto.tonedcoot2.chatgpt.site) · [Projekti tutvustus](PROJEKTI_UHELEHEKULJELINE_TUTVUSTUS.md) · [4 minuti demonstratsioon](DEMONSTRATSIOONI_KAVA.md) · [Ekraanipiltidega varuesitlus](ESITLUS_EKRAANIPILTIDEGA.md)

**Ligipääs:** avaldatud Sitesi link küsis kontrollis endiselt ChatGPT sisselogimist. Kontovaba esitluse jaoks kasuta valmis Pagesi demo või ekraanipiltide paketti.

## Kiire käivitamine

Paki tervikpakett lahti ja ava terminal kaustas `finantsarvestus`:

```bash
python -m http.server 8000 --directory dist
```

Ava http://localhost:8000. Pythoni analüüsisõltuvusi pole valmis veebi serveerimiseks vaja. Ära ava index.html-i topeltklõpsuga: moodulid ja Worker vajavad HTTP-d. Esmakordne arvete vaade laadib samalt saidilt ligikaudu 15 MB Pyodide'i faile. Kasuta WebAssemblyt ja moodul-Workerit toetavat ajakohast brauserit.

## Ehita ja kontrolli

```bash
python -m pip install -r requirements.txt
python kood/ehita_veeb.py
python -m unittest discover -s testid -v
python kood/paki_etapp5.py
```

Soovitatav arenduskeskkond Python 3.12; Thonnys saab ehitusskripti käivitada F5-ga. Testid kinnitavad 71 kontrolljuhtu, sh 51 varasemat ja 20 uut. [Testiraport](TESTIRAPORT_LOPLIK.md) eristab automaatseid teste, brauserikatseid ja kontrollimata olukordi. Väljundid: `tarne/Finantsarvestus_loplik.zip`, `tarne/Finantsvaade_avalik_demo.zip`, kontrollsummad `tarne/SHA256.json`.

## Mida saab teha?

- Vaadata aastaeelarvet ja jaanuari–augusti täitmist; eraldi uurida jaanuari–septembri kulusid ja investeeringuid.
- Importida kuni 500 sünteetilist ostuarvet CSV/XLSX-failist, filtreerida, sortida ja selgitada kontrollileide.
- Leida võimalikke duplikaate; kontrollida kohustuslikke välju, kuupäevi ja summasid.
- Eksportida kontrolli- ja analüüsiaruandeid CSV/Excelina ning kasutada SQLite'i analüüsiandmebaasi.
- Läbida [kiirkursus](FINANTSARVESTUSE_EKSPERDI_KIIKURSUS.md) ja [tööpäeva simulatsioon](FINANTSARVESTUSE_EKSPERDI_TOOPAEV.md).

## Tehniline lahendus

Avaliku analüüsi teeb enne avaldamist Python koos Polarsiga; pandas on võrdlus- ja kontrolllahendus. JSON seob arvutused veebivaadetega. Brauseri Worker käitab Pyodide'i kaudu sama Pythoni ostuarvete mootorit ja Pydantic v2 andmelepingut. openpyxl loob Exceli väljundid. SQLite asub brauseriseansi mälus. Serveripoolset Pythonit ega andmebaasi GitHub Pagesis ei ole.

[Arhitektuur](ARHITEKTUUR.md) · [Spetsifikatsioon](TARKVARA_SPEC.md) · [Andmemudel](ANDMEMUDEL.md) · [Tehnoloogiline analüüs](TEHNOLOOGILINE_ANALUUS.md) · [Arendusjuhend](ARENDUSJUHEND.md)

## Andmed ja piirangud

HTM valitsemisala koondandmete allikad ja hankimiskuupäevad on [allikaregistris](ANDMEALLIKAD.md). Arved ja toetuste näited on sünteetilised. Eelarve täitmise andmed ja majandusliku sisu kuluvaade kasutavad eri perioode/aluseid: neid ei liideta ega võrrelda otse. Andmeid ei uuendata reaalajas.

Imporditud fail jääb brauserikaardi mällu; lehe uuendamisel lisatud arved kaovad. Ekspordi tulemus enne sulgemist. Ära kasuta päris isikuandmeid ega arveid. Rakendus ei kinnita makseid, maksukäsitlust ega raamatupidamiskannet. [Finantsreeglite kontroll](FINANTSREEGLITE_KONTROLL.md) sisaldab 18 põhjendatud juhtumit. [Riskid](RISKID_JA_PIIRANGUD.md) kirjeldab tootmiskasutuse eeldusi.

## Õppimine ja kandideerimine

[Kiirkursus: 30 küsimust ja 10 ülesannet](FINANTSARVESTUSE_EKSPERDI_KIIKURSUS.md) · [22 töövestluse küsimust](TOOVESTLUSE_ETTEVALMISTUS.md) · [Oskuste maatriks](OSKUSTE_MAATRIKS.md) · [Esitluspaketi register](KANDIDEERIMISE_ESITLUS.md)

[Veebijuhend](VEEBIRAKENDUSE_JUHEND.md) · [Avaldamine](AVALDAMINE_LOPLIK.md) · [GitHub Pages](GITHUB_PAGES_AVALDAMINE.md). Avalik demo sisaldab üldmaterjale; isiklik kandideerimispakett antakse eraldi. Ajaloolised ETAPP1–4 dokumendid kirjeldavad vastava etapi seisu; lõppversiooni puhul lähtu README-st ja [etapi 5 tulemustest](ETAPP5_TULEMUSED.md).
