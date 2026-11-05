> **Uuendus 0.2:** teine etapp on teostatud. Allolev tekst säilitab esimese etapi lähteolukorra. Kehtivad täiendused: [teise etapi spetsifikatsioon](ETAPP2_TEHNILINE_SPEC.md), [kasutusjuhend](KASUTUSJUHEND_ETAPP2.md) ja [tulemused](ETAPP2_TULEMUSED.md). Etapid 3–5 ootavad korraldust.

# Tarkvara spetsifikatsioon · 0.1

## Rakendatud esimese etapi nõuded

| ID | Nõue | Käitumine |
|---|---|---|
| F01 | Lugeda kaks XLSX-algfaili | openpyxl, data_only=True; valemite arvu kontroll eraldi |
| F02 | Tuvastada algfaili muutus | SHA-256 erinevus peatab töö |
| F03 | Kontrollida struktuuri | Oodatud pealkiri, leht, ühik ja periood; muutusel viga |
| F04 | Luua HTM-i väljavõtted | Seadus B:E, read 101–117; täitmine 137–145 |
| F05 | Normaliseerida raha | Decimal → täisarvulised eurosendid, ROUND_HALF_UP |
| F06 | Säilitada tühjade tähendus | Kriips/tühi ei muutu automaatselt nulliks |
| F07 | Eristada kuu ja YTD | B:J kuud, N ja O kumulatiivsed; K:M jäetakse välja |
| F08 | Kontrollida kuude summat | Jaanuar–september võrreldakse N-veeruga; tolerants 1 sent |
| F09 | Luua näidissisend | 6 fikseeritud arvet, provenance=SUNTEETILINE |
| F10 | Anda kontrollitav väljund | UTF-8 BOM, semikoolon-CSV ja JSON |

## Sisend ja väljund

Sisend: kaasasolevad ametlikud failid ja allikaregister. Väljund: `andmed/toodeldud/` neli faili. Skript kirjutab need uuesti, kuid algfaile ei muuda. Näidisarvete generaator kirjutab üle ainult oma näidisfaili.

See versioon on seotud just registreeritud allikaversioonidega. Uue Exceli pelgalt sama nime alla kopeerimine ei ole toetatud uuendusviis. Uuendamisel kontrollitakse struktuuri, tähendust ja testootusi ning lisatakse uus allikaversioon.

## Hiljem rakendatavad nõuded

| Moodul | Kavandatav käitumine | Etapp |
|---|---|---:|
| Arvekontroll | Puuduvad väljad, duplikaadikahtlus, summad, tähtajad, dimensioonid | 2 |
| Menetlus | Rollide otsused ja muutumatu sündmuslogi | 2 |
| Analüüs | Võrreldavad eelarveversioonid, hälbed, kulurühmad, toetused | 3 |
| Aruanded | Pythonis arvutatud CSV/XLSX ja juhtimiskokkuvõte | 3 |
| Veeb | Filtrid, graafikud, import ja eksport, andmeliigi tähis | 4 |
| Õpe | Täielik kursus, demonstratsioon ja töövestluse materjal | 5 |

## Mittefunktsionaalsed nõuded

Python 3.10 või uuem. Töötlemine peab töötama Windows 11/Thonny ja Colabi failikeskkonnas. Rahasummade kontrollis ei kasutata float-võrdlust. NumPy/pandas võivad hiljem aidata analüüsi, kuid tehingute kontroll jääb senti või Decimal-tüüpi. Brauserisse ega GitHubi ei lisata päris arveid ega isikuandmeid. Puudub automaatne maksmine või ametliku arve kinnitamine.

AI pole sõltuvus. Võimalik hilisem AI-kokkuvõte saab ainult kontrollitud koondandmed ning peab viitama allikale ja perioodile. Puuduvaid andmeid ei täideta AI oletustega.
