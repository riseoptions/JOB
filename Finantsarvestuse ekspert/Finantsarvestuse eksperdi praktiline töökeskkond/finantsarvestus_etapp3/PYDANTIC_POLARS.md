# Pydantic v2 ja Polars praktiliselt

## Pydanticu roll

Pydantic kirjeldab ühe dokumendi kuju. Praegu teisendas menetlusmootor tüüpe mitmes reeglis ise. Säilitasime need kasutajale tuttavad reeglid ja lisasime ühtse tüübitud piiri. Näiteks list kujul supplier_name oli varem tekstiks muutes näiliselt täidetud; nüüd annab see `ANDMEKUJU` vea.

```python
from andmeleping import InvoiceInput
from menetlus import read_csv, issues_for
from pathlib import Path
r = read_csv(Path('andmed/sunteetilised/naidisarved.csv'))[0]
m = InvoiceInput.model_validate(r)
print(m.net_cents, type(m.net_cents))  # 100000, int
print(m.service_date)                 # date objekt
print(m.model_dump(mode='json'))      # JSON-sobiv kuju
print(issues_for(r, '2026-11-05'))     # tähtaja ja perioodi hoiatused
```

Käivitatav näide: `python kood/pydantic_naide.py`. CSV teisendus on sihilik: `'100000'` lubatakse, `100000.0`, `True` ja `'1.5'` mitte. `Decimal` säilitab maksumäära täpsuse. Tehingu summasid arvutatakse täisarvulistes sentides. Väljadele ei rakendata pimedat üldist tüübisundi.

Mudeli valideerimine **ei kinnita arvet**: mudel ei tea duplikaatidest, kasutajarollist, lepingust ega maksumäära õiguslikust sobivusest. Nende jaoks jäävad ärireeglid ja inimese otsus. Toor-JSON säilib eraldi, seega mudeli kuupäevad/int-väärtused ei muuda olemasolevat sisuräsi.

Pydantic genereerib JSON Schema. CSV-le lubatud tekstteisendused ja mudeli väljunditüübid võivad erineda; API kavandamisel tuleb otsustada üks selge sisendleping. Tulevane API võiks vastu võtta sentides JSON-täisarve ja ISO kuupäevi, mitte Exceli kujundatud rahateksti.

## Polarsi roll ja pandas-võrdlus

```python
import polars as pl
q = (pl.scan_csv('andmed/toodeldud/htm_taitmine_2026.csv', separator=';',
                 schema_overrides={'amount_cents': pl.Int64})
     .filter((pl.col('period_kind') == 'kuu') & (pl.col('row_kind') == 'koond'))
     .select('period_start', 'amount_cents')
     .sort('period_start'))
print(q.collect())
```

Lazy päring kirjeldab töö enne käivitamist. Suuremate CSV/Parquet-andmete korral saab Polars optimeerida filtrite ja veergude lugemist. Antud projektis on vaid 99 lähterida ning põhjus Polars valida on õppimine ja selge töötlusloogika, mitte lubadus suurest kiirusvõidust.

```python
import pandas as pd
p = pd.read_csv('andmed/toodeldud/htm_taitmine_2026.csv', sep=';',
                dtype={'amount_cents': 'Int64'})
print(p.loc[(p.period_kind == 'kuu') & (p.row_kind == 'koond'),
            ['period_start','amount_cents']].sort_values('period_start'))
```

| Tehnoloogia | Sobiv roll siin | Mida ei asenda |
|---|---|---|
| Senine Python + Decimal | Käibemaks, reeglid, senditäpsus | Selget tüübitud sisendlepingut |
| Pydantic v2 | Dokumendi valideerimine ja skeem | Duplikaadipäringut, rolliõigust, kinnitust |
| pandas | Tuttav võrdluslahendus ja hilisem ML-liides | SQL tehinguid |
| Polars | Tüübitud veerud, lazy filter/sort; hiljem suured failid | XLSX vormindust ega iga rea ärilist õiguspärasust |
| SQLite | Püsivad tehingud/audit ja aruandepäringud | Pythoni täielikku valideerimist |
| openpyxl | Alg-XLSX lugemine ja Python-aruande vormindus | Polarsi arvutusmootorit |

Mõõtmine: mõlemad loevad sama CSV, valivad samad read/veerud ja sordivad. Tehakse soojendus + 7 mõõdetud jooksu. Võrdlus sisaldab lugemist ja kontrolle, mitte ainult tuumarvutust; järjekord on Polars, pandas ning OS vahemälu mõjutab tulemust. Mediaan ja keskkond on `tulemus.json`. Üks väike mõõtmine ei tõenda üldist paremust. Õigsust kontrollitakse ajast sõltumatu täpse tulemuste võrdlusega.

## Kuidas see toetab järgmisi tehnoloogiaid?

| Suund | Kasulik alus | Enne rakendamist vajalik |
|---|---|---|
| ML | Polars moodustab kuupõhised tunnused; vajadusel `to_numpy()` või eraldi pandas adapter | Piisav ajalugu, ajapõhine treening/testjaotus, tulevikuinfo lekke vältimine; 9 kuud ei õigusta keerulist mudelit |
| LLM | Pydantic kontrollib väljavõtte/selgituse struktuuri; rahasummad arvutab Python | Väite sidumine allikaga; korrektne JSON ei tõenda sisu tõesust; LLM ei kinnita arveid |
| RAG | source_id, lahter, periood ja versioon annavad viidatava päritolu | Tekstidokumentide tükeldus, ligipääsukontroll, otsingu kvaliteedi hindamine; arvutustabeli summad pärida SQL-ist |
| API | Pydanticu sisend/väljund ja JSON Schema; sama teenusloogika | Autentimine, autoriseerimine, idempotentsus, versioonimine ja logimine; CSV ning API lepingud eraldi kokku leppida |

Praegu ei ole lisatud mudelit, vektorandmebaasi, LLM päringuid, agente ega API serverit. Need on põhjendatud jätkuvõimalused pärast põhiandmete ja töövoogude ühendamist.

## Ametlikud tehnilised allikad

Kontrollitud 06.11.2026. Paigaldatud versioonid on requirements.txt-s; dokumentatsiooni latest võib ajas muutuda.

- [Pydanticu valideerijad](https://docs.pydantic.dev/latest/concepts/validators/)
- [Pydanticu range tüübikontroll](https://docs.pydantic.dev/latest/concepts/strict_mode/)
- [Pydantic JSON Schema](https://docs.pydantic.dev/latest/concepts/json_schema/)
- [Polars lazy kasutamine](https://docs.pola.rs/user-guide/lazy/using/)
- [Polars optimiseerimine](https://docs.pola.rs/user-guide/lazy/optimizations/)
