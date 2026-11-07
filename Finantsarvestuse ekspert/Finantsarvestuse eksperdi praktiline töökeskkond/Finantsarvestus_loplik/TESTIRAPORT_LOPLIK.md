# Lõplik testiraport

Kontroll: 7.11.2026. Ulatus: õppeprojekti versioon 0.5; mitte sertifitseeritud turva- ega raamatupidamisaudit. Pärast tööfailide taastamist käivitati testid uuesti; varasemat edu ei kasutatud taastatud failide tõendina.

## Automaatsed kontrollid

`python -m unittest discover -s testid -v` → **71 testi edukad (51 varasemat + 20 etapi 5 testi)**. Toorlogi: [testitulemus](materjalid/testitulemus_etapp5.txt). JavaScripti süntaks: `node --check veeb/app.js` ja `node --check veeb/worker.js`.

| Valdkond | Kontroll ja oodatud tulemus | Tõend |
|---|---|---|
| CSV/XLSX | Korrektne import, vigane kodeering/arhiiv/kuupäev tagasi lükatud | test_etapp4.py, test_etapp5.py |
| Piirid | 500 dokumenti lubatud; 501, liigne laius ja lahtipakitav maht keelatud | test_etapp5.py |
| Ülekirjutamine | Olemasoleva ID kordus ei tarbi uut kohta; ebaõnnestunud lisamine ei muuda seanssi | test_etapp5.py |
| Valemid ja XML | XLSX valemid, DTD/ENTITY ning liigne arhiivimaht tagasi lükatud | test_etapp5.py |
| Väljund | Valemilaadne tekst, päis ja pealkiri neutraliseeritud; negatiivne arv jääb arvuks | test_etapp4.py, test_etapp5.py |
| Pydantic | Puuduvad kohustuslikud väljad ja sobimatud tüübid, sh bool raha asemel | test_etapp3.py, test_etapp5.py |
| Raha | Senditäpsus, poole sendi ümardus, liiga pikk summa; neto + KM = bruto | test_etapp2.py, test_etapp5.py |
| Analüüs | Polars/pandas/SQL tulemuste kooskõla, nullbaas ja ülekulu | test_etapp3.py, test_etapp5.py |
| Andmete päritolu | Avalikud koondandmed eraldi sünteetilistest arvetest/toetustest | test_etapp3.py, test_etapp4.py |
| Staatiline veeb | Kopeeritud Pythoni moodulite vastavus, nõutud failid | test_etapp4.py |

Testifailid asuvad `testid/`. Oodatud summasid kontrollitakse väärtuspõhiselt, mitte ainult erindi puudumise järgi. Regressioonitestid katavad ka SQLite'i tehingud, auditikirjed ja idempotentsuse.

## Brauserikontroll

Chrome'i päris brauseris, HTTP kaudu. Viimase taastatud versiooni kontrollid:

1. Avaleht: aastaeelarve 1 207,52 mln €, täitmine 772,6 mln €, kasutamine 64%, jääk 434,92 mln €. Need on täpsete lähtearvude kuvamisümardused.
2. Worker käivitus: Python 3.14.2, Pydantic 2.12.5 ja SQLite. Brauseri Pydantic erineb kohalikust lukustatud 2.13.4 versioonist; mõlemad on v2, töövoogu katsetati brauseris.
3. Puuduvate veergudega kleebitud CSV jättis 17 dokumenti alles ja näitas „Puuduvad veerud …” ilma Pythoni traceback'ita.
4. Näidisarve IMPORT-001 import: 17 → 18 dokumenti, 1240,01 €, üks blokeeriv summaviga. Otsing näitas 1/18 dokumenti.
5. Filtreeritud Excel laaditi brauserist alla ja loeti openpyxl-iga tagasi: kolm leiurida, kõik IMPORT-001; gross_cents=124001; SUMMA, PERIOOD ja ULETAHTAJA. Faili olemasolust üksi ei piisanud.
6. 390/768/1280 px iframe-paigutus: dokumendi clientWidth = scrollWidth vastavalt 375/753/1265; kogu leht ei ulatu raamist välja. Mobiili menüü ja tabelid võivad kerida oma konteineri sees. See ei ole päris telefoni test.

Varasemas sama etapi brauseriringis kontrolliti lisaks XLSX-faili importi, valemiga XLSX-i tagasilükkamist, Keeleameti filtrit ja Exceli 42991100/67988700 sendi väärtusi, septembri graafiku 86 428 785,64 € summat ning kahe duplikaadi filtrit. Need katsed ei asenda viimast automaattestide korduskäivitust; nende vanad ekraanipildid ei säilinud. Värsked pildid on `materjalid/kuvatommised/`.

## Kontrollimata või piiratud

- Safari, Firefox, füüsilised telefonid, ekraaniluger ja täielik WCAG audit.
- Pikaajaline koormus, pahatahtlike failide täielik fuzzimine ja sõltumatu turvatest.
- SAP/RTIP pärisliidesed, autentimine, tootmisandmete püsivus ja taastamine.
- Kõik käibemaksu erijuhud, kreeditarved ja asutuse sise-eeskirjade täielik vastavus.
- GitHub Actionsi päris käivitus kasutaja GitHubi kontol; töövoog valmistati ette. Sitesi juurutus õnnestus, kuid public-seadest hoolimata jäi kontovaba brauser sisselogimisvaatesse. See on kontrollitud ligipääsupiirang, mitte rakenduse funktsioonide edukas kaugtest.

Järeldus: sobib sünteetiliste arvete ja avalike koondandmetega õppeks ning demonstratsiooniks. Tootmiskasutuse valmidust see raport ei kinnita.
