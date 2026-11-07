# Õppemoodul 4 · veebist kontrollitava finantsarvuni

**30 minutit:** 5 min ülevaade, 5 min andmete liikumine, 10 min import ja eksport, 10 min harjutused. Eesmärk: oskad rakendust kasutada ning põhjendada, miks veebis nähtav number on kontrollitav.

## Kuidas see töötab?

Veebileht on kasutajaliides. Python valmistab ametlike XLSX-failide põhjal ette eelarve ja kulude tabelid. Polars filtreerib tabelandmeid; pandas kontrollib sama kuutulemuse võrdsust. JSON kannab arvutatud summad lehele, kus JavaScript kuvab graafiku ja filtrid. Näiteks augusti kulude 772 600 007 € päritolu on ametliku faili E94 lahter; ühik tuhat EUR teisendatakse Pythoni abil sendiks.

Uue arve korral käivitub Python sinu brauseris Pyodide'i kaudu. Pydantic kontrollib tüüpe; varasem mootor kontrollib summasid, kuupäevi, kontot, kulukeskust ja duplikaate. SQLite hoiab dokumente ning kontrolli ajalugu ainult selle kaardi mälus. Fail ei lähe serverisse. Etapp 2 kinnitusring jääb kohalikus demokoodis alles; veebis on kontrollitöökoht.

## Miks Excel tekib automaatselt?

Python annab arvutustabeli openpyxl-ile, mis kirjutab XLSX-faili. Vormindatud finantskoond tuleb samast etapi 3 funktsioonist; jooksva arvevaliku kontrolliaruande genereerib brauseri Python. Väljund on hetkeseis. Kontrollimiseks võrdle vähemalt ühte rahasummat, ühe dokumendi veakoodi ja aruande ridade arvu. Ainult faili avanemisest ei piisa.

## Viis praktilist harjutust ja lahendused

### 1. Tuvasta võrreldavad näitajad

**Ülesanne:** leia eelarve kasutamine ja selgita, kas 64% tähendab kaheksa kuu säästu. Miks septembri kulujoonise summa erineb?

**Lahendus:** 772 600 007 / 1 207 523 833 ≈63,98%. Lugeja on 8 kuu täitmine, nimetaja terve aasta eelarve. Perioodiplaan puudub, seega säästu järeldada ei saa. Septembri vaade hõlmab 9 kuud ning kulusid ja investeeringuid ilma amortisatsioonita; koosseis erineb.

### 2. Leia duplikaat

**Ülesanne:** ava arvete vaade ja vali „Võimalikud duplikaadid“. Mitu dokumenti leitakse ning milline on põhjus?

**Lahendus:** algnäidises 2 dokumenti, DEMO-002 ja VIGA-007. Tarnija ID ning tühikute/suur-väiketähtede suhtes normaliseeritud arvenumber kattuvad. Viga on DUPLIKAAT. See on kontrollivajadus, mitte pettuse tõend.

### 3. Impordi summaveaga arve

**Ülesanne:** laadi impordiproov, impordi see ning otsi IMPORT-001. Neto 100000 senti, KM 24000 senti, bruto 124001 senti. Mida ootad?

**Lahendus:** SUMMA viga, sest 100000+24000=124000, mitte 124001. Dokumendid kasvavad 17-lt 18-le. Import säilitab vigase rea, et põhjust saaks uurida; ta ei kinnita arvet. Sama faili teine import ei lisa sama dokumenti uuesti.

### 4. Ekspordi kontrollitav valik

**Ülesanne:** eelarvevaates vali Keeleamet ja ekspordi CSV. Leia täitmine. Seejärel ekspordi arvete otsingust ainult IMPORT-001 Excelisse.

**Lahendus:** Keeleameti actual_cents=42991100 ehk 429 911 €. CSV sisaldab üht asutust. Arvearuandes võib olla mitu rida, sest ühel dokumendil on mitu leidu; kõik peavad viitama IMPORT-001-le. Protsent on suhtarv, raha sentides. Valikueksport ei tohi sisaldada teisi dokumente.

### 5. Kavanda kasulik API või AI-täiendus

**Ülesanne:** paku lahendus, mis selgitab juhile kontrollitud hälvet, kuid ei muuda summat ega kinnita arvet. Milliseid välju on vaja?

**Lahendus:** API annab source_id, perioodi, mõõdiku, eelarveversiooni, võrreldavad summad ja Pythoni arvutatud hälbe. LLM võib koostada tekstiselgituse; RAG lisab kinnitatud juhendi viite. Skeem valideerib väljundi kuju, numbrid kontrollitakse algse JSON-iga. Inimene hindab põhjuseid; mudel ei tee makset. ML-i jaoks kogutakse eraldi piisav ajalugu ja välditakse tulevikuinfo leket.

## Mida see võiks ministeeriumis parandada?

Korduvad tabelikontrollid muutuvad reprodutseeritavaks, vigade põhjused on nähtavad ning sama raport tekib igal jooksutamisel ühe metoodika järgi. Spetsialist saab keskenduda eranditele ja selgitustele. SAP, RTIP ja e-arvete menetlussüsteem jäävad ametlikeks allikateks ja töövoogudeks; õppeveeb näitab võimalikku täiendavat kontrolli- ja analüüsikihti, mitte nende väljavahetamist.

Õpetajale: palu õppijal enne arvutamist nimetada periood, ühik, päritolu ja koond/detail tase. Lase teadlikult vigane arve importida ning selgitada veakoodi. Edasi palu tõendada eksportfaili sisu. Etapi 5 terviklikku lõpukursust selles moodulis ei koostata.
