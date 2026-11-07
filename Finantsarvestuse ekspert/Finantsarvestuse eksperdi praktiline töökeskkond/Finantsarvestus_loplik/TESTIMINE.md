# Testimine · etapp 4

## Etapi 5 kehtiv täiendus

Lõppversiooni kehtiv kokkuvõte on TESTIRAPORT_LOPLIK.md ja toorlogi materjalid/testitulemus_etapp5.txt: 71 edukat testi, sh 20 uut piirjuhtumit. Varasemate etappide testiarvud allpool on ajaloolised. Füüsilisi telefone, Safari/Firefoxi, päris SAP/RTIP liideseid ja tootmiskoormust pole kontrollitud.

Kontrollitud 06.11.2026. Kohalik Python 3.12; brauseris Chrome, Pyodide 314.0.7, Python 3.14.2, Pydantic 2.12.5. Senise keskkonna sõltuvus Polars taastati requirements.txt järgi enne eeltöö lõpetamist.

## Automaattestid

**51/51 Python-testi läbis:** 37 senist ning 14 veebiadapteri testi. Logid materjalid/etapp4_eelkontroll.txt ja materjalid/testitulemus_etapp4.txt.

| Katvus | Oodatud tulemus |
|---|---|
| CSV import, kordusimport | Uus ID lisandub ühe korra |
| Duplikaat | Sama tarnija/arvenumber annab vea mõlemale dokumendile |
| Konfliktne partii | Sama ID erinev sisu katkestab kogu partii; uus rida ei jää sisse |
| Päis, failipiir | Puuduv/dubleeruv päis ja üle 2 MB sisend lükatakse tagasi |
| XLSX import | Esimese lehe väärtused ja päris Exceli kuupäevad loetakse õigesti |
| Pydantic | Loend tarnija nimena annab ANDMEKUJU |
| Päritolu | TEGELIK-tekstiga näidisarve saab ANDMELIIK vea |
| Eksport | Õige dokumendi ID, bruto sendid ja sünteetiline päritolu |
| Valemitekst | CSV/XLSX valemina tõlgendatav tekst neutraliseeritakse |
| Valik | Tühi või tundmatu ID ei tekita eksitavat aruannet |
| Veebi finantsandmed | Eelarve 120752383300 ja täitmine 77260000700 senti; 9 kuu summa 88618428861 senti |
| Ühine äriloogika | Veebile kopeeritud 3 Python-moodulit on algfailidega baiditäpselt samad |

Senised testid kontrollivad lisaks ümardamist, puuduvat raha, Polars/pandas võrdsust, analüüsi koondsummasid, toetuse ülempiiri, SQL-vaateid, rolle, auditit ja tehingute tagasipööramist.

## Tegelikud brauserikontrollid

- Avaleht näitas 1207,52 mln € eelarvet, 772,6 mln € kulusid, 64% kasutamist ning 17 sünteetilist dokumenti.
- Duplikaadifilter näitas 2 / 17 dokumenti; detailis DUPLIKAAT ja põhjendus.
- Pyodide käivitus tuvastatavate Python/Pydantic versioonidega.
- Brauseris kleebiti uus BRAUSER-001 netoga 100000, KM-ga 24000 ja brutoga 124001 senti. Tulemus 18 dokumenti, SUMMA viga ning tähtaja/perioodi hoiatused.
- Valitud dokumendi XLSX laaditi brauserist alla ja loeti Pythonis tagasi: ainult BRAUSER-001, bruto 124001, SUMMA ning õige päritolu.
- Tegelik XLSX-fail imporditi failivalija kaudu. Uus XLSX-001 jõudis 19 dokumendiga seanssi; 1240 € arvel olid ainult eeldatud hoiatused.
- Keeleameti filter näitas 679887 € eelarvet ja 429911 € täitmist. Brauserist genereeritud CSV loeti tagasi: üks Keeleameti rida, actual_cents=42991100.
- Septembri filter näitas 86428785,64 €. Toetuste vaates olid 2000 € juurdemakse, 600 € tagasinõue ja 50 € ülempiir.
- Ülevaade vaadati visuaalselt üle. Fondi varuvariant säilib ja tabelid on kitsal ekraanil keritavad; eraldi mobiilseadmes testi ei tehtud.

Valikuline korduv Playwrighti test on `testid/browser.spec.mjs`; juhis ARENDUSJUHEND.md-s. Selle eraldi runnerit ei käivitatud selles keskkonnas. Eeltoodud brauseritoimingud tehti Chrome'i UI kaudu ja tulemusi kontrolliti, mitte ei loetud edu pelgast veateate puudumisest.

## Avaldamise kontroll

Valmis dist/ töötas staatilises HTTP-eelvaates, ilma Python-serveri API-ta. Sitesi avaldamise tulemus kontrollitakse avaldamisteenuse vastusest. GitHub Pagesi kaug-workflow ei käivitatud: repositooriumit ei ühendatud; ette on valmistatud workflow ja juhend. Etapi 5 täielikku lõppauditit see etapi 4 kontroll ei asenda.
