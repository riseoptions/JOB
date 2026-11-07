# Tehnoloogiate valik ja laienduskohad

| Tehnoloogia | Praegune kasutus | Piir ja alternatiiv |
|---|---|---|
| CPython + Polars | Avalike andmete ehitusaegne analüüs | Uus andmeväljavõte nõuab ehitust |
| pandas | Senine kuutulemuste võrdluskontroll | Ei kirjutata toimivat Polarsi teed ümber |
| Pydantic v2 | Sama InvoiceInput mõlemas keskkonnas | Skeem ei tõenda arve ärilist õigsust |
| SQLite | Kohalik audit / brauseri mäluseanss | Pole GitHub Pagesi serveri DB; püsiv server vajab eraldi teenust |
| openpyxl | XLSX import ja eksport | Ei käivita Exceli valemeid; lubatud on väärtuspõhine sisend |
| Pyodide | Pythoni arvekontroll brauseris | Esmane laadimine umbes 15 MB, nõuab WebAssemblyt |
| HTML/CSS/JS ja SVG | Interaktiivne UI ja ligipääsetav kuugraafik | JS ei dubleeri rahaarvutusi |
| GitHub Pages / Sites | Staatiliste failide majutus | Ei käita serveripoolset Pythonit ega taustaprotsessi |
| GitHub Actions | Testitud väljavõtte ehitus ja avaldamine pushi järel | Automaatne uute algallikate hankimine pole lisatud |

Polars on saadaval ka valitud Pyodide'i paketiloendis, kuid selle allalaadimist pole näidisarvete kontrolliks vaja. Pyodide ei ole siin üldise serveri asendus. Plotly asemel piisab väikesest SVG-joonisest: klaviatuuriga valitavad punktid, summa detail ja perioodifilter ilma lisasõltuvuseta.

## Täiendus olemasolevatele finantssüsteemidele

| Süsteem/tööprotsess | Sellise lahenduse võimalik lisaväärtus |
|---|---|
| E-arvete menetluskeskkond | Enne sisestamist failide kuju, summade ja võimalike duplikaatide kontroll |
| RTIP | Kinnitatud väljavõtte kvaliteedikontroll, perioodi- ja dimensioonivigade nähtavus |
| SAP / SAP BO | Ametliku väljavõtte põhjal täiendav analüüs ja korduv aruandlus; SAP jääb arvestuse allikaks |
| Toetuste infosüsteem | Nähtavad lepingupõhised kontrollid, ülempiiri ja ettemakse eristamine |

Need on integratsioonivõimalused, mitte teostatud ühendused ega väited konkreetse asutuse liideste kohta. Tootmises tuleb andmeleping, autentimine, rollid, kooskõlastusring, säilitamine ning audit täpsustada süsteemi omanikuga.

## Tulevane API ja AI

- **API:** brauseri adapteri sisendleping võib liikuda serveri teenusekihti. Arve kinnitamine vajab autoriseeritud kasutajat ja tehingut; idempotentsus ja sisuräsi säilivad.
- **ML:** Polars võib moodustada ajapõhise tunnustabeli; vältida tulevikuinfo leket ja hinnata mudelit eraldi testperioodil. Praegune 9 kuud ei õigusta keerulist prognoosimudelit.
- **LLM:** saab selgitada kontrollitud JSON-i, märkides perioodi ja allikad. Rahasummad võetakse Pythonist, mitte ei genereerita uuesti.
- **RAG:** indekseerida kinnitatud juhendeid koos versiooni ja viitega; arvutustabeli summad pärida deterministlikult SQL-ist.
- **Agent:** võib koostada kontrolliplaani või soovitada järgmist sammu; ei tee automaatseid arvekinnitusi ega makseid.

Praeguses paketis pole tasulist API-t, võtit, vektorandmebaasi ega AI-teenust.

Ametlikud tehnilised allikad (kontrollitud 06.11.2026): [GitHub Pagesi piirid](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site), [Pyodide paketid](https://pyodide.org/en/stable/usage/packages-in-pyodide.html), [Polars lazy](https://docs.pola.rs/user-guide/lazy/using/), [Pydantic valideerijad](https://docs.pydantic.dev/latest/concepts/validators/).
