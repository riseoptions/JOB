# Veebirakenduse kasutusjuhend

## 1. Ava ülevaade

Ülal olevad neli näitajat kirjeldavad HTM valitsemisala **augusti** eelarve kasutamist. Joonisel on **jaanuar–september kulud ja investeeringud ilma amortisatsioonita**. Need on erinevad vaated. Graafiku punktile vajutades või klaviatuuriga fookustades ja Enteriga valides näed kuu täpset summat.

## 2. Kontrolli ostuarvet

1. Ava „Ostuarvete kontroll“. Esmane Python-laadimine võib võtta kuni kaks minutit; edasised kontrollid toimuvad samas Worker-seansis.
2. Kasuta otsingut või vali filter „Võimalikud duplikaadid“. Algnäidises on 17 dokumenti, kaks duplikaaditunnusega dokumenti.
3. Vajuta „Vaata“: näed koodi, välja ja vea põhjust. Tähtaja hoiatus ei tõenda tasumata arvet.
4. Laadi „impordiproov“, seejärel impordi sama CSV. Uuel real on invoice_id=IMPORT-001 ja sihilik bruto viga.
5. Impordi CSV/XLSX fail või kleebi CSV tekst vastavasse lahtrisse. Kasuta ainult fiktiivseid arveid.
6. Ekspordi valitud dokumendid CSV või Excelina. Ühel dokumendil võib olla mitu veateadet ja seetõttu mitu aruanderida.

Importimiseks kasuta algnäidise veerunimesid. Raha on sentides: 124000 tähendab 1240 eurot. XLSX esimesel lehel on päis esimeses reas. CSV UTF-8, semikooloniga. Lisaveerud on lubatud. Sama ID erineva sisuga ei asenda vana dokumenti; kasuta uut ID-d.

Kontrollpäeva muutmiseks vali kuupäev ja vajuta „Kontrolli uuesti“. Otsing ja sort töötavad ka eelnevalt arvutatud näidisel, kuid uus import ja dünaamiline eksport vajavad Pythonit.

**Seanss on ajutine.** Lehe uuendamine või „Taasta algne näidis“ eemaldab imporditud read brauseri mälust. Ekspordi tulemused enne. Midagi ei saadeta SAP-i, RTK-sse ega panka.

## 3. Analüüsi

- Eelarve kasutamise vaates vali asutus. Ainult augusti võrreldav eelarve/täitmise vaade on saadaval.
- Kuukulude vaates vali üks kuu või kõik üheksa kuud.
- Aastavõrdlus võrdleb 2025 ja 2026 jaanuar–septembrit.
- Toetuste vaade on sünteetiline: esimese projekti juurdemakse 2000 €, teise tagasinõue 600 €, kolmanda toetuse ülempiir 50 €.
- „Valiku CSV/Excel“ ekspordib kuvatava andmevaliku. CSV-s on rahad sentides ja protsendid suhtarvudena.

## 4. Aruanded ja allikad

Aruandluse alt saad kohe alla laadida etapi 3 vormindatud Exceli, eelarve CSV, kuluvõrdluse CSV ja SQLite'i. „Genereeri Excel“ loob vastava tabeli aruande Pythonis. Ostuarvete kontrolliaruanne kasutab sinu seansi viimast seisu. Allikate plokk näitab ametlikke faile ja hankimise aega; veebiväljavõtte loomisaeg on eraldi.

## 5. Kui midagi ei tööta

- Tühi andmevaade: ava leht HTTP(S) kaudu, mitte file:// aadressiga.
- Python ei käivitu: vaata konkreetset teadet, kontrolli ühendust ja vajuta „Käivita Python“. Moodul-Worker/WebAssembly peab olema lubatud.
- Päiseviga: võrdle näidisfailiga; ära tõlgi veerunimesid.
- Sama ID konflikt: lisa uus dokumendi ID; partii varasemad read ei salvestu osaliselt.
- Tühi eksport: muuda filtrit, et valida vähemalt üks rida.
- Import ei ole püsiv: see on teadlik brauseri seansi piirang. Tootmise püsisalvestus vajaks eraldi teenust.
