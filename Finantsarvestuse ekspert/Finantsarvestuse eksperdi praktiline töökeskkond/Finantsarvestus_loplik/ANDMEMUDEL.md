# Andmemudel · 0.4

## Etapi 5 kehtiv täiendus

Skeemide muutmine ei olnud vajalik. Raha on täisarv sentides; veebivormis võidakse sendisumma transportida stringina. Float ei ole rahalise tõe allikas. Eelarvetabeli level eristab asutuse ja valdkonna koondeid: mõlema taseme liitmine topeltloendaks. provenance eristab sünteetilisi sisendeid. Export sisaldab kontrollpäeva ja päritolumärget. Brauseri andmebaas on mälus ja kaob lehe uuendamisel.

Senised SQL-skeemid 001–005 säilivad. Menetluse skeem on 0.2, reeglid 0.2.1, analüüsi skeem 0.3 ja veebiväljavõte 0.4.

| Objekt | Asukoht ja eluiga | Sisu |
|---|---|---|
| source_file / allikaregister | Failid ja kontrollitud projekti väljavõte | URL, fail, SHA-256, hankimisaeg, ühik ja periood |
| budget_analysis | Etapi 3 analüüsi SQLite, JSON budget | Koond/asutus, algeelarve, ajakohane eelarve, 8 kuu täitmine, lahtrid |
| monthly_actual | Analüüsi SQLite, JSON monthly | 9 koondkuud; kulud+investeeringud amortisatsioonita |
| grant_analysis | Analüüsi SQLite, JSON grants | Sünteetiline perioodiplaan, kulud, toetus, ettemakse |
| input_document | Brauseri :memory: SQLite | Algne JSON, sisuräsi, ID, olek SISEND, looja |
| check_run / validation_issue | Sama seansi SQLite | Iga kontrolli kuupäev, reeglivariant, vead/hoiatused |
| document_event | Sama seansi SQLite | Senise mootori impordi sündmuslogi |
| invoice_snapshot | JSON või jooksva seansi tulemus | Viimased vead, hoiatused, kontrollitud ja vigaste dokumentide arv |

Brauser ei loe sünteetiliste arvete summasid ministeeriumi avalikeks kuludeks. Seansi sisend dokumendil väitega provenance=TEGELIK ei muutu pärisandmeks: mootor annab ANDMELIIK vea ja UI märgistab seda näidissisendina.

Puuduv invoice_id saab senise mootori PUUDUV-<räsi> ID, et viga säiliks kontrollitavana. Sama ID erinev sisu ei kirjuta dokumenti üle. Koond ja detail on eelarvetabelis eraldi tasemed. Rahastusristlõige ei lisandu kulu kogusummale. Algallika rahamärk/ühik on teisendusel dokumenteeritud etapis 3.

Seansiandmed ei säili lehe uuendamisel. Importimis- ja kontrollikäikude püsiv tootmisajalugu nõuaks serveri andmebaasi; brauseri mälu seda ei asenda.
