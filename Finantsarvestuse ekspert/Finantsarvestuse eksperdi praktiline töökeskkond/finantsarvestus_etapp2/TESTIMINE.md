> **Uuendus 0.2:** teine etapp on teostatud. Allolev tekst säilitab esimese etapi lähteolukorra. Kehtivad täiendused: [teise etapi spetsifikatsioon](ETAPP2_TEHNILINE_SPEC.md), [kasutusjuhend](KASUTUSJUHEND_ETAPP2.md) ja [tulemused](ETAPP2_TULEMUSED.md). Etapid 3–5 ootavad korraldust.

# Testimine · etapp 1

Kontrollitud 5.11.2026, Python 3.12, openpyxl 3.1.5.

```bash
python -m unittest discover -s testid -v
```

## Tegelikult käivitatud kontrollid

| Kontroll | Oodatav tulemus | Tulemus |
|---|---|---|
| Tuhat eurot → sendid; positiivne ja negatiivne poolsendi ümardus | Õige märk ja ROUND_HALF_UP | Läbis |
| Puuduv, kriips, null ja vigane tekst | Puuduv ei muutu nulliks; vigane tekst tekitab vea | Läbis |
| Pärisandmete väljavõte ja kooskõla | 34 + 99 kirjet; 9 lähterea kuu/YTD kooskõla; võrdlusprotsent keelatud | Läbis |
| Muudetud algfail | SHA-256 kontroll katkestab töö | Läbis |
| Näidisandmete korduv genereerimine | Sama 6 arvet; neto + KM = bruto; sünteetiline märgis | Läbis |

**5 automaattesti läbisid.** Täielik väljund: `materjalid/testitulemus.txt`. Testid töötavad ajutiste koopiatega ega muuda algfaile.

Täiendavalt käivitati SQL-skeem mälus: 10 tabelit loodi veatult. Eelarve asutuste detailridade D109:D117 summa võrreldi sõltumatult koondreaga D108: kattus. Colabi koodilahtrite Python-süntaks ja dokumentide kohalikud lingid kontrolliti.

Ei testitud: Microsoft Exceli ümberarvutus, Thonny/Colabi graafiline kasutus, SAP/RTIP ühendus ega veebiliides. Viimaseid ei ole selles etapis ehitatud. Algseid XLSX-faile ei vormindatud ümber ega muudetud.

Testid ei ole ametliku raamatupidamisregistri audit ega kinnitus tehingute õiguspärasuse kohta.
