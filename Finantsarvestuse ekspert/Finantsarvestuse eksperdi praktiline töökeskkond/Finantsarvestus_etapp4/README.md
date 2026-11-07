# Finantsvaade · finantsarvestuse töökeskkond

**Versioon 0.4: etapid 1–4.** Eestikeelne interaktiivne veebirakendus, Pythoni analüüs, ostuarvete kontroll, SQL, CSV/XLSX aruanded ja õppematerjal. Etappi 5 ei ole alustatud.

## Kiire algus

Valmis veeb on `dist/` kaustas. Selle avamiseks ei pea analüüsisõltuvusi paigaldama:

```bash
python -m http.server 8000 --directory dist
```

Ava http://localhost:8000. Ära ava index.html-i topeltklõpsuga: file:// ei toeta vajalikke mooduleid, fetch-päringuid ja Workerit. Brauser peab toetama WebAssemblyt ja moodul-Workerit. Arvete vaate esmakordne avamine laadib umbes 15 MB Pythoni käituskeskkonna faile samalt veebilehelt.

## Ehita ja testi

```bash
python -m pip install -r requirements.txt
python kood/ehita_veeb.py
python -m unittest discover -s testid -v
python kood/paki_etapp4.py
```

Thonnys käivita ehita_veeb.py F5-ga; veebilehe jaoks kasuta seejärel terminalis HTTP-serverit. Esimese kolme etapi skriptid töötavad seniste käskudega. Avalike andmete analüüsi teevad Python ja Polars; veeb kuvab nende tulemusi. Brauseri arvete import kasutab **samu** menetlus.py ja andmeleping.py faile, mitte ümberkirjutatud JavaScripti reegleid.

## Põhiosad

- **Ülevaade:** aastaeelarve, kaheksa kuu täitmine ja kasutamata eelarve; eraldi üheksa kuu kuluvaade ning sünteetiliste arvete seis.
- **Ostuarved:** otsing, sortimine, veafilter, duplikaadid, põhjused, CSV/XLSX import ja kontrolliaruande eksport.
- **Analüüs:** asutuse filter, kuuperiood, sama perioodi aastavõrdlus, sünteetilised toetused ja valikueksport.
- **Aruandlus:** Pythoni vormindatud Excel, CSV, analüüsi SQLite ja projekti ZIP.
- **Õppekeskkond:** selgitused ning Markdown-õppemoodulid koos lahendustega.

Alusta [veebijuhendist](VEEBIRAKENDUSE_JUHEND.md). Avaldamine: [GitHub Pages](GITHUB_PAGES_AVALDAMINE.md). Õppimine: [moodul 4](OPPEMOODUL_04.md). Tehniline alus: [arhitektuur](ARHITEKTUUR.md), [spetsifikatsioon](TARKVARA_SPEC.md), [testimine](TESTIMINE.md).

## Andmed ja piirid

HTM koondandmed on Rahandusministeeriumi avalikest failidest tuletatud. Arved ja toetuse näited on fiktiivsed. Arvefaili sisu ei saadeta serverisse. Brauseri SQLite on ainult jooksva kaardi mälus: lehe uuendamine taastab algnäidise. Ekspordi oma kontrollitulemus enne sulgemist.

GitHub Pages ei käita serveripoolset Pythonit, SQLite'i ega taustaprotsessi. Pyodide käitab Pythonit külastaja brauseris; avaliku analüüsi uue väljavõtte teeb ehitusskript. LLM-e, RAG-i, agente ja maksete tegemist pole lisatud. Täielik lõppkontroll, koondkursus ja kandideerimispakett jäävad etappi 5.
