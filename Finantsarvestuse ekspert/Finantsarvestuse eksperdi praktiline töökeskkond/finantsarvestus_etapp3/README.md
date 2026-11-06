# Finantsarvestuse ja kulude analüüsi töökeskkond

## Etapp 3 · versioon 0.3

Eestikeelne Python + SQL õppeprojekt. Pakett sisaldab **etappe 1–3**: avalike andmete kontrollitud väljavõte, ostuarvete menetluse simulatsioon ning finantsanalüüs ja Exceli aruandlus. Etappe 4 ja 5 ei ole alustatud. See ei ole HTM-i, RTK ega SAP-i ametlik infosüsteem.

### Käivitamine

Paki ZIP tervikuna lahti. Python 3.10 või uuem; kontrollitud Python 3.12-ga.

```bash
python -m pip install -r requirements.txt
python kood/etapp3_demo.py
python -m unittest discover -s testid -v
```

Thonny: paigalda requirements.txt-s nimetatud versioonid paketihalduriga, ava `kood/etapp3_demo.py`, vajuta F5. Internetti on vaja teekide paigaldamiseks; demo kasutab kaasasolevaid algfaile. Colabi juhis: `kood/Etapp3_Colab.ipynb`.

Iga käivitus loob uue kausta `valjund/etapp3/`. Ava sealt **Finantsanaluus.xlsx**, `aruanne.md` või `analuus.sqlite`. Kontrollitud valmisnäidis on `valjund/etapp3/kontrollitud_naidis/`. XLSX on Pythoni arvutuste hetkeseis; lähteandmete muutmise järel genereeri aruanne uuesti.

### Mida kolmas etapp teeb?

- Võrdleb augusti ametliku väljavõtte sama rea eelarvet ja täitmist, kontrollib asutuste summat ja algse seadusega vastavust.
- Arvutab septembri kuukulud ja eelmise aasta sama perioodi muutused eraldi arvestusalusel.
- Näitab sünteetiliste toetuste perioodihälvet, abikõlblikkust, ülempiiri, ettemakset, juurdemakset ja tagasinõuet.
- Lisab arvetele Pydantic v2 tüübid, säilitades senised ärireeglid, toor-JSON-i ja CSV-lisaveerud.
- Kasutab Polarsi uuteks väljavõteteks ning kontrollib kuutulemuse võrdsust pandas’ega.

### Õppimise järjekord

1. [Tehniline hinnang ja otsused](TEHNILINE_HINNANG_ETAPP3.md).
2. [Kolmanda etapi kasutusjuhend](KASUTUSJUHEND_ETAPP3.md).
3. [30-minutiline õppemoodul koos lahendustega](OPPEMOODUL_03.md).
4. [Pydantic, Polars ja edasine AI-integratsioon](PYDANTIC_POLARS.md).
5. [Arhitektuur](ARHITEKTUUR.md), [tarkvaraspetsifikatsioon](TARKVARA_SPEC.md), [testimine](TESTIMINE.md).

Varasemad demod töötavad samade käskudega: `python kood/etapp1.py` ja `python kood/etapp2_demo.py`. Menetluse SQLite skeem ja JSON-edastusleping jäävad versioonile 0.2; lisanduva tüübitesti reeglistiku versioon on 0.2.1. Analüüsiandmebaasil on oma versioon 0.3. Ühtne rakendus ja veebiliides jäävad järgmistesse etappidesse.
