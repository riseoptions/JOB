# Tarkvaraspetsifikatsioon · 0.3

## Ulatus ja käitus

Etapid 1–3. Python 3.10+, sõltuvuste täpsed kontrollitud versioonid `requirements.txt`. Avalike failide töötlemine ja sünteetiliste dokumentide õppesimulatsioon. Etapid 4–5 on tegemata. Käivitus ei saada andmeid välisele teenusele.

## Funktsionaalsed nõuded

| ID | Nõue | Teostus / kontroll |
|---|---|---|
| F01 | Algandmed muutmata, kontrollsummaga | etapp1.build; read_budget |
| F02 | Senine arve- ja menetlusloogika säilib | 22 regressioonitesti |
| F03 | Väljade tüübid, ISO kuupäev ja täpsed sendid | InvoiceInput, ANDMEKUJU |
| F04 | Augusti ajakohane aastaeelarve versus 8 kuu täitmine | read_budget, asutuste summa, ristkontroll seadusega |
| F05 | Üheksa kuud ja eelmise aasta sama periood | aggregate_months, year_comparison; puuduv pole null |
| F06 | Sünteetiline toetus, perioodihälve ja ettemakse | Grant, grant_result |
| F07 | Polars/pandas tulemusvõrdsus | üks ja sama CSV/filter/sort; senditäpne võrdlus |
| F08 | SQLite, CSV, JSON, MD, vormindatud XLSX | etapp3_demo.run |
| F09 | Korduskäivitus ei kirjuta eelmist aruannet üle | mikrosekundiline UTC jooksukaust; olemasolev output lükatakse tagasi |

## Andmelepingud

InvoiceInput sisaldab seniseid kohustuslikke arvevälju, kuupäevi, kolme sentides summat, Decimal maksumäära, kulukeskust, kontot ja päritolu. `currency` vaikimisi EUR. Täisarvuline CSV tekst teisendatakse; bool, float raha, negatiivne raha ja ülemäärane summa lükatakse tagasi. Kuupäeval puudub ajatempel. Lisaväljad lubatud. Ärireeglid (KM määrad, neto+KM, tähtajad, duplikaadid jne) jäävad menetlusmootorisse: üksnes Pydanticu valideerimine ei tähenda arve heakskiitu.

Grant on rangelt määratletud väljadega sünteetiline toetuse sisend. Summad sentides 0…10^12, määr 0…1, abikõlblik summa ≤ tegelik kulu. Projekti ID seob aruande rea sisendiga. Kõigi kolme näite plaan ja tegelik kulu hõlmavad 2026 jaanuar–september perioodi.

## Valemid ja tähendus

- Ajakohase aastaeelarve muutus = ajakohane eelarve − algne eelarve.
- Kasutamata aastaeelarve = ajakohane eelarve − jaanuar–august täitmine.
- Kasutamise määr = jaanuar–august täitmine / ajakohane aastaeelarve.
- Aastamuutus = 2026 jaanuar–september − 2025 jaanuar–september; protsent võrreldes 2025-ga.
- Sünteetiline perioodihälve = tegelik kulu − sama perioodi plaan; positiivne tähendab plaani ületamist.
- Arvutuslik toetus = min(ülempiir, ROUND_HALF_UP(abikõlblikud sendid × määr)).
- Juurdemakse = max(toetus − ettemakse, 0); tagasinõue = max(ettemakse − toetus, 0).
- Nullist nimetaja annab None/SQL NULL/tühja Exceli lahtri, mitte 0%. Puuduv rahasumma peatab analüüsi.

## Tõrked ja piirangud

Muutunud kontrollsumma, lehe struktuur, vale ühik, kuude puudumine/dubleerumine või summade vastuolu peatab jooksu. Poolik jooksukaust võib jääda tõrke uurimiseks; valmis aruanne tekib alles pärast arvutuskontrolle. Uuendatud ametlik fail vajab uut allikaregistrit ja kaardistuse kontrolli, mitte vana SHA pimesi asendamist.

Aruanne kasutab fikseeritud 2026 kaardistust; universaalset suvaliste XLSX-failide importi ei lubata. Reaalne kuupõhine kinnitatud eelarveplaan puudub, seega tegelik sama perioodi plaanihälve on arvutatud ainult sünteetilises näites. Perioodiaruannetest ei järeldata põhjuslikkust ega maksete tegemist.
