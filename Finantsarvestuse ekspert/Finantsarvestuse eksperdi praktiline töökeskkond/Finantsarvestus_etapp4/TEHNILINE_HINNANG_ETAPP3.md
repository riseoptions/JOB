# Tehniline hinnang enne kolmanda etapi muudatusi

Kontrollitud 06.11.2026: etapi 2 Python, SQL-skeemid 001–003, arhitektuur, andmeallikad ja automaattestid. Kõik **22 senist testi läbisid** enne muudatusi. Menetluses on atomaarne import, korduskindlad edastused/vastuvõtud, rollide kontroll, muutmatu sündmuslogi ja tasakaalukanne. Täpsed sendid arvutatakse int/Decimal abil. Toorandmete säilitamine võimaldab vigast sisendit uurida.

| Koht | Hinnang | Rakendatud otsus |
|---|---|---|
| Ostuarve väljade kuju | Protseduuriline reeglistik on toimiv; tüübileping oli hajutatud | Pydantic `InvoiceInput` ja täiendav `ANDMEKUJU` kontroll |
| Ärireeglid, rollid, duplikaadid | Vajavad konteksti ja andmebaasi; Pydantic ei asenda neid | Säilitada `menetlus.py`; minimaalne lisakutse pärast seniseid kontrolle |
| SQLite | Sobib menetluse tehinguteks ja auditiks | Menetluse skeemi ei muudeta; uus eraldi aruandeandmebaas |
| Tabelanalüüs | 99 lähterida on liiga vähe üldise jõudluseelistuse järeldamiseks | Polars lazy väljavõte, pandas võrdlustee ja mõõdetud kohalik ajakulu |
| Excel | Kasutaja nõuab Python/openpyxl väljundit | Vormindatud automaatne hetkeseis, täpsed arvutused Pythonis |
| Eelarve vastendamine | Algseaduse kulud ja septembri kulud+investeeringud pole sama mõõdik | Lisatud ametlik augusti seadusepildi fail, sama rea C/D/E võrdlus |

Pydanticu kasutamine on põhjendatud ka väikeses projektis selgema skeemi ja integratsioonipiiri tõttu. Polarsi praegune väärtus on väljenduspõhine töötlus ja õpitav laiendustee; kogu varasema koodi ümberkirjutamine ei oleks põhjendatud.

## Teadaolevad piirid

Menetluse rollid on simulatsiooni tabelikirjed, mitte päris autentimine. Sündmuslogi trigereid saab andmebaasi omanik muuta. Üherealine arve ei kata krediitarveid, mitme maksumääraga arveid ega ettemaksete täielikku arvestust. Analüüs kasutab avaldatud esialgseid koondandmeid; see ei tõenda üksiktehingute õiguspärasust. Neid piire ei lahendata kolmanda etapi käigus.
