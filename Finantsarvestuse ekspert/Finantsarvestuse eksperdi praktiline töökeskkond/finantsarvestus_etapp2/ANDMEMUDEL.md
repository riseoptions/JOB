> **Uuendus 0.2:** teine etapp on teostatud. Allolev tekst säilitab esimese etapi lähteolukorra. Kehtivad täiendused: [teise etapi spetsifikatsioon](ETAPP2_TEHNILINE_SPEC.md), [kasutusjuhend](KASUTUSJUHEND_ETAPP2.md) ja [tulemused](ETAPP2_TULEMUSED.md). Etapid 3–5 ootavad korraldust.

# Andmemudel · skeem 0.1

## Praegu olemasolevad failid

| Fail | Ühe rea tähendus | Võti |
|---|---|---|
| allikaregister.json | Üks ametlik allikafail konkreetsel allalaadimisel | source_id |
| htm_eelarve_2026.csv | Üks seaduserida ja üks mõõdik (kokku või sh piirmääraga) | record_id |
| htm_taitmine_2026.csv | Üks lähterida ühes kuu- või YTD-perioodis | record_id |
| kooskolakontroll.csv | Ühe lähterea üheksa kuu ja N-veeru võrdlus | source_row |
| naidisarved.csv | Üks fiktiivne ühe reaga arve | invoice_id |

### Päritolu

Algne XLSX = **TEGELIK** avalik allikas. CSV-väljavõte = **TULETATUD** pärisandmetest, mitte sünteetiline. Näidisarve = **SUNTEETILINE**. Väljavõtte töötlemine ei suurenda algandmete täpsust.

### Eelarve väljad

`record_id`, `source_id`, `sheet`, `cell` on jälgitavuse tekstiväljad. `line_id` on tekst, nt `9.10`, mitte kümnendmurd. `label` on allika nimetus. `metric` eristab eelarvet ja selle piirmääraga osa, mida ei tohi liita. `year` on täisarv. `period_start/end` on ISO-kuupäevad. `budget_version=algne_seadus`. `scope=HTM_valitsemisala` tähistab väljavõtte plokki, mitte iga alamrea võrdsust valitsemisala kogusummaga. `row_kind` eristab koond- ja detailridu. `raw_value/unit` säilitavad algväärtuse ning `amount_cents` on märgiga täisarv. `sign_policy` kinnitab allika märgi säilimise.

### Täitmise väljad

Lisaks päritolule: `measure=kulud_ja_investeeringud_va_amortisatsioon`; `row_kind=koond/sh_rida/ristloige`; `period_kind=kuu/YTD`. YTD tähendab perioodi algusest kogunenud summat. 2025. aasta võrdlusnäitaja tuleb O-veerust ja kannab 2025 kuupäevi, mitte 2026 kuupäevi. `missing_reason` eristab kriipsu. CSV-s tühi amount_cents tähendab puuduvat või tõlgendamata näitajat, mitte nulli.

### Sünteetilise arve väljad

Tekstilised `invoice_id`, `supplier_id`, `invoice_number`; ISO `invoice_date/service_date/due_date`; `net_cents/vat_cents/gross_cents` täisarvud; `vat_rate` kümnendmurru tekst, nt 0.24; `cost_center/account` ainult DEMO-koodid; `status=SISEND`. Tegelik registrikood, pangakonto ja isikunimi puuduvad.

## Kavandatud SQLite-tabelid

`sql/001_skeem.sql` on esialgne leping, mitte kogu rakendus. `source_file → budget_line` ja `source_file → actual_observation` kannavad andmepäritolu. Tulevased `invoice → invoice_line`, `invoice → workflow_event` ja `invoice → check_result` võimaldavad mitmerealisi arveid ning ajalugu. Pearaamatu `journal_entry → journal_line` eristub arvest, sest üks arve võib tekitada mitu kannet.

Rahaväljad: INTEGER sendid. Määrad: TEXT Decimal-kujul. Kuupäevad: TEXT ISO-kujul. Kohustuslikud identifikaatorid: NOT NULL. Välisvõtmed: SQLite-is tuleb aktiveerida PRAGMA foreign_keys=ON. Vigased impordiandmed jäävad tulevikus eraldi staging-kihti, et andmebaasi piirang ei kaotaks nende kontrollimise võimalust.

Täielik kontoplaan, eelarveversioonide vastendus, toetuse abikõlblikkus ja kinnitusringide õigused vajavad järgnevate etappide täpsustust. DEMO-kontosid ei kasutata ametlike koodidena.
