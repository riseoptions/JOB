# Kolmanda etapi tulemused

06.11.2026; valmis ainult etapp 3 ja selleks vajalikud väikesed täiendused.

## Teostatud

- Säilitatud etappide 1 ja 2 toimiv loogika, lisatud Pydanticu tüübileping ja ANDMEKUJU kontroll.
- Lisatud ametlik augusti seadusepildi XLSX, kontrollsummad, ühiku- ja päritoluinfo.
- Eelarveanalüüs, kuukulud, aastavõrdlus, sünteetiline toetusearvestus ja automaataruandlus.
- Polarsi andmetöötlus, pandas võrdlustee; samad senditäpsed tulemused.
- Uus eraldi analüüsi SQLite, neli CSV-d, JSON, MD ja kolme lehega Exceli aruanne.
- 15 uut testi; koos varasematega 37/37 läbis.
- Arhitektuur, tarkvara- ja projektispetsifikatsioon, juhendid, 30-minutiline õppetund ning Colabi käivitusfail.

## Pärisandmete põhinäitajad

| Näitaja | Tulemus |
|---|---:|
| HTM valitsemisala algne aastaeelarve | 1 176 947 117 € |
| Augusti väljavõtte ajakohane aastaeelarve | 1 207 523 833 € |
| Jaanuar–august täitmine, seadusepildi kulud | 772 600 007 € |
| Kasutamise määr | 63,98% |
| Jaanuar–september kulud+investeeringud amortisatsioonita | 886 184 288,61 € |
| Muutus võrreldes 2025 sama perioodiga | +69 413 669,57 €; +8,50% |

Kaks viimast rida kuuluvad teise mõõdikuga vaatesse. Neid ei kasutata augusti eelarve kasutamise määra lugejana. Kasutamata aastaeelarve ei ole perioodi sääst; kinnitatud kuupõhine plaan puudub.

## Väike tehniline mõõtmine

Kontrollitud jooksu mediaan, 99 sisendrida ja 9 valitud kuud:

- Polars 1.287 ms.
- pandas 1.711 ms.

Seitse kordust pärast soojendust; sisaldab CSV lugemist, filtreerimist, sortimist ja kontrolle. Tulemus sõltub vahemälust/keskkonnast ega tõenda üldist kiiruseelist. Täpsed kordused ja keskkond: `valjund/etapp3/kontrollitud_naidis/tulemus.json`.

## Tõendid ja piirid

Allika URL, failiräsi ja hankimisaeg on `andmed/allikaregister.json`. Rea/veeru vastendus on eelarve.csv ja aastavordlus.csv. Summad kontrolliti vastu koondridu, algseadust, YTD ning SQL-i. Testilogid kaasas. Ametlike andmete hilisemaid muudatusi automaatselt alla ei laadita; aruandes kasutatakse kontrollitud väljavõtteid.

Toetuste näited on SUNTEETILINE. Ei ole täielikku toetusmeetme õiguslikku mudelit ega maksete täitmist. Rakendus töötab lokaalselt; päris autentimist, API serverit ja AI-komponente ei ole. Etapid 4/5 on alustamata.

## Ametlikud finantsandmete allikad

- [2026 riigieelarve ja täitmise failid](https://www.fin.ee/riigi-rahandus-ja-maksud/riigieelarve-ja-eelarvestrateegia/2026-riigieelarve).
- [Täitmise avalikustamise metoodika](https://www.fin.ee/riigi-rahandus-ja-maksud/riigieelarve-ja-eelarvestrateegia/tegevuspohise-eelarvestamise-kasiraamat/eelarve-taitmise-ulevaade): ajakohane eelarve sisaldab muudatusi; avaldatud esialgsed andmed võivad muutuda. Kontrollitud 06.11.2026.
