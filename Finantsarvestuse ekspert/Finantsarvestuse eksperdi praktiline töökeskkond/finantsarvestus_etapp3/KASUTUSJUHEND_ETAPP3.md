# Kolmanda etapi kasutusjuhend

## 1. Käivita ja vaata

Paki kõik failid ühte kausta. Thonny tööriistade paketihalduris paigalda `requirements.txt` versioonid (openpyxl, pydantic, polars, pandas). Ava `kood/etapp3_demo.py` ja vajuta F5. Alternatiiv on README käsurida. Kui pip ei leia paketiversiooni, kontrolli internetiühendust ja Python 3.10+ kasutamist; ära muuda versioone enne testide kordamist.

Konsool näitab uut väljundkausta. Esimese etapi teade „Täitmise protsenti ei arvutatud“ kehtib selle vanale eraldi väljavõttele; kolmas etapp arvutab sobitatud augusti failist kasutamise määra.

| Väljund | Kasutamine |
|---|---|
| Finantsanaluus.xlsx | Eelarve, Kulud, Toetused; summad eurodes, suhtarvud protsentides |
| aruanne.md | Lühike analüütiku ülevaade ja tõlgenduspiirid |
| eelarve.csv | Täpsed sendid, algne/ajakohane eelarve, täitmine, lahtrid |
| kuukulud.csv / aastavordlus.csv | Kuluvaate võrreldavad perioodid |
| toetused.csv | Fiktiivsete toetuste arvutused ja perioodihälbed |
| analuus.sqlite | Ava DBeaveris, käivita sql/005_analuusi_paringud.sql |
| tulemus.json | Põhinäitajad, teegiversioonid ja kohalik Polars/pandas mõõtmine |
| arve_skeem.json | Pydanticu loodud valideerimisskeem, mitte valmis HTTP-liides |

XLSX on aruande hetkeseis. Lahtrite käsitsi muutmine ei arvuta Pythonis tehtud tulemusi ümber. Täpsete sentide auditeerimiseks kasuta CSV-d või SQL-i. CSV eraldaja on semikoolon, kodeering UTF-8 BOM; protsentide veerud sisaldavad suhtarvu (0.64 = 64%).

## 2. Muuda sünteetilist näidet

Ava `andmed/sunteetilised/etapp3_toetused.json`. Muuda näiteks TOETUS-001 ettemakset 600000 → 850000 senti ja käivita uuesti. Toetus jääb 800000 senti; tagasinõue muutub 50000 sendiks. Eelmine aruanne jääb alles. Taasta algväärtus enne kaasasolevate oodatud tulemuste testimist.

Ametlikke XLSX-algfaile ära käsitsi muuda. Uue perioodi lisamisel kontrolli ühikut, lehte, pealkirju, mõõdikut, eelarveversiooni, perioodi, koond/detail taset ja päritolu. Praegune kaardistus on teadlikult fikseeritud ning peatub ootamatu sisendi korral.

## 3. Kontrolli

```bash
python -m unittest discover -s testid -v
python kood/pydantic_naide.py
python kood/etapp2_demo.py
```

Menetluse ja analüüsi andmebaasid on eraldi. Ära käivita SQL 004 menetluse andmebaasis. Pydanticu muudatus rakendub ka vana etapi 2 CLI kaudu tehtud uutele kontrollidele; olemasolevaid kontrolliajaloo kirjeid ei muudeta.
