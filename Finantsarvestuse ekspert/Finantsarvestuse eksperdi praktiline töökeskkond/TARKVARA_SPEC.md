# Tarkvaraspetsifikatsioon · 0.4

## Ulatus

Etappide 1–3 toimiva loogika integreerimine eestikeelsesse veebirakendusse. Toetatud modernne brauser, HTTP(S), WebAssembly ja moodul-Worker. Testitud Chrome'is. Kohalikud Python-sõltuvused requirements.txt-s; brauseri Pyodide 314.0.7 / Python 3.14.2 / Pydantic 2.12.5 / openpyxl 3.1.5.

| ID | Nõue | Teostus |
|---|---|---|
| W01 | Põhinäitajad koos perioodiga | Ülevaade: aastaeelarve, 8 kuu täitmine, kasutamine, jääk; eraldi arvekontroll |
| W02 | Otsing, filter ja sort | ID/tarnija/arvenumber, vead/hoiatused/duplikaadid, bruto/ID/vigade arv |
| W03 | Vigade põhjused | Arve detail: kood, väli, selgitus, tõsidus |
| W04 | CSV/XLSX import | Sama adapter CPythonis ja brauseris, esimene tööleht, UTF-8 CSV semikooloniga |
| W05 | Kontrollmootor ja Pydantic | Ühine muutmata menetlus.py ja andmeleping.py |
| W06 | Metoodiliselt korrektne analüüs | Augusti eelarve; 9 kuu kulud; aastavõrdlus; eraldi sünteetiline toetus |
| W07 | Interaktiivne graafik | Kuu punkt hiire või klaviatuuriga; perioodi- ja asutusefilter |
| W08 | Eksport | Valitud read ja kogu seansi kontroll CSV/XLSX; valmis Exceli koond ja SQLite |
| W09 | Päritolu | source_id, allikalingid, periood, hankimisaeg ja väljavõtte loomisaeg |
| W10 | Õpe | Selgitused ja 4. mooduli viis harjutust lahendustega |
| W11 | Staatiline avaldamine | dist/, .nojekyll, GitHub Pagesi workflow ja juhend |

## Sisend ja tõrked

Kohustuslikud arveveerud pärinevad menetlus.REQUIRED loendist. Lisaveerud lubatud. Päised ei tohi dubleeruda, kõik read peavad sobima päisega. CSV-kodeering UTF-8 või UTF-8 BOM, eraldaja semikoolon. XLSX esimesel lehel on päis esimeses reas. Kuupäevad kas ISO-tekst või Exceli kuupäevalahter ilma kellaajata. Formuleid ei käivitata. Rahad sentides; bool, murdosa, negatiivne summa ja muud senise mootori rikkumised jäävad blokeerivaks.

Kogu sisendpartii import on atomaarne. Sama invoice_id ja sama sisu ei dubleeru; sama ID erinev sisu annab vea ja partii ei salvestu. Kasuta uue paranduse jaoks teist ID-d; varasema etapi CLI parandustöövoog säilib. Import ei kinnita arvet. Duplikaadikontroll arvutatakse pärast importi uuesti kõigile seansi dokumentidele.

Seansi piir on 500 dokumenti; lisanduvate ID-de kontroll võib piiri lähedal olla konservatiivne. Tühi valik ei anna petlikku tühja aruannet, vaid selge vea. Faili laadimise või Pythoni tõrke korral näidatakse põhjust ja uut käivitusvõimalust. 120 sekundi käivituspiir.

## Väljundileping

projekt.json: version, built_at, source_updated_at, sources, budget, monthly, yoy, grants, invoice_snapshot, invoice_seed, periods. Raha on täisarvulistes sentides; puuduv suhtarv null. Detailandmed ei tohi sisaldada päris arveid ega saladusi. Worker vahetab ID-ga JSON-sõnumeid (start, import, check, invoice_export, table_export). CSV/Excel fail edastatakse Base64-ga ainult Workerilt samale lehele.

Dünaamiline aruanne säilitab sendid ning kuupäeva/päritolu. Vormindatud etapi 3 koondaruanne kasutab eurokuva. Exceli valemi algusega tekstid neutraliseeritakse ekspordis; sisendit ei lisata DOM-i ilma HTML-põgenemiseta.

## Arvutused

Kõik etapi 3 valemid jäävad muutmata: kasutamine = 8 kuu täitmine / ajakohane aastaeelarve; jääk = eelarve − täitmine; aastamuutus võrdleb sama 9 kuu perioodi; toetus = min(ülempiir, ümardatud abikõlblik kulu × määr). Nullist nimetaja annab puuduva suhtarvu, mitte 0%.

## Mittenõuded

Ei ole tootmissüsteemi autentimist, serveri püsivat menetlust, SAP/RTIP ligipääsu, makseid, ML-mudelit, LLM-kõnesid, RAG-andmebaasi ega agenti. Need on eraldi tulevaste tööde otsused. Etapi 5 koondkontrolli ja kandideerimispaketti ei koostata.
