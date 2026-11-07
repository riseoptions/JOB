# Lõppkontrolli plaan · 0.5

07.11.2026. Aluseks on etappide 1–4 kumulatiivne projekt.

1. Kontrolli mooduleid, SQL-skeeme, allikaregistrit ja varasemaid tulemusi; käivita regressioonid.
2. Võrdle finantsmõisteid ametlike allikatega, koosta oodatud tulemustega näited.
3. Paranda ainult leitud puudused: kordusimpordi mahupiir, XLSX mõõtmed ja valemid, väga pikk rahatekst, ekspordipäise valemikaitse, brauseri veateade.
4. Testi importi, eksporti, arvutusi, filtreid ja eri laiustega vaateid; erista tegelik kontroll oletusest.
5. Koosta terviklik õppematerjal ja aus kandideerimispakett.
6. Eralda avalik veeb isiklikest materjalidest, avalda ja paki kontrollsummadega tarne.

Arhitektuuri hinnang: CPython teeb avaliku analüüsi enne avaldamist; Pyodide kasutab brauseris sama arvemootorit. Pydanticu tüübipiir ja SQL-i tehingud säilivad. Polars/pandas võrdlus on juba olemas; uut raamistikku ega AI-teenust pole põhjendatud lisada.

Töökeskkonna puhastus eemaldas esimese viienda etapi tööversiooni enne püsisalvestust. Taastatud versioon kontrollitakse uuesti. Varasemad brauseritulemused on ajalooline tõend, mitte taastatud versiooni automaatne sertifitseerimine.
