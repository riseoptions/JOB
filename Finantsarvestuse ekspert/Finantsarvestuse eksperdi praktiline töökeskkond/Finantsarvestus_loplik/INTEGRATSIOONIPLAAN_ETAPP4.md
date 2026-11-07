# Eeltöö ja integratsioonihinnang

Kontrollitud etappide 1–3 arhitektuur, tarkvaraspetsifikatsioon, andmemudel, Python-moodulid, SQL 001–005, algallikad, aruanded ja testid. Esimesel kontrollil puudus uues käituskeskkonnas Polars; paigaldati olemasolev requirements.txt. Seejärel läbisid kõik **37 varasemat testi**. Logi: materjalid/etapp4_eelkontroll.txt.

Pydantic v2 on juba InvoiceInput-mudelis ja toetuse mudelis. Polars on etapi 3 filter/sort/aastavõrdluses; pandas kontrollib kuutulemuste võrdsust. SQL hoiab menetluse auditit ning eraldi analüüsiandmebaasi.

## Valitud lahendus

1. Säilita muutmata menetlus.py, andmeleping.py, analuus.py ning senised SQL-skeemid.
2. Lisa väike veeb_adapter.py: CSV/XLSX lugemine, seansi haldus, senise kontrolli kutsumine ja eksport.
3. ehita_veeb.py käivitab etapi 3 analüüsi ning avaldab JSON-väljavõtte ja aruanded dist-kausta.
4. Staatiline eestikeelne HTML/CSS/JS kuvab tulemusi, graafikut, filtreid ja õppeosa.
5. Moodul-Worker käivitab Pyodide'i ning sama Pythoni kontrolli kohalikus SQLite'is. Välditakse reeglite topeltteostust.
6. Testi CPythonis ja brauseris, paki täielik projekt ning avalda staatiliselt.

## Miks nii?

Kasutaja soovib tasuta staatilist majutust ja Pythonit põhiloogikaks. Serveri kasutuselevõtt ainult 17 sünteetilise arve jaoks lisaks haldust. Kogu Polarsi/pandas'e analüüsi brauserisse laadimine kasvataks esmast allalaadimist; valmis analüüs on koheselt nähtav. Pydanticu brauseriversioon 2.12.5 erineb kohalikust 2.13.4-st, mistõttu kontrolliti tegelikku importi ja valideerimist brauseris.

CDN-laadimise esmane katse ei õnnestunud testbrauseris. Seetõttu tarnitakse vajalik Pyodide 314.0.7 käituskeskkond, Pydantic ja openpyxl koos lehega. Polarsit brauserisse ei laadita; see ei tähenda väidet, et Polars seal üldse ei töötaks. Pyodide'i valitud versioon kasutab moodul-Workerit.
