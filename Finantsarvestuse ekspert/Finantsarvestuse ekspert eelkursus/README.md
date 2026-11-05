# Finantsarvestuse eksperdi eelkursus

**Praktiline eestikeelne ettevalmistus Haridus- ja Teadusministeeriumi finantsarvestuse eksperdi ametikohale**  
Versioon: 1.0 · Koostatud 5.11.2026 · Iseseisev õppe- ja näidisprojekt; ei ole HTM-i ega RTK ametlik materjal.

## Milleks see on?

Sul on matemaatika, majanduse, SQL-i, Pythoni ja infosüsteemide testimise taust. Selle kursuse eesmärk on täita **finantsarvestuse praktilise töö** lüngad, mitte õpetada Pythoni nullist.

**Läbiv olukord:** fiktiivne asutus „Haridusamet X“ saab IT-teenuse ostuarve; finantsekspert kontrollib arve ja kooskõlastuse, teeb koostööd keskse raamatupidamisteenusega, jälgib eelarvet ning vormistab aruande. Kõik näidisarved ja väljamõeldud eelarved on **sünteetilised**.

## Õpitee (6–8 tundi)

| Järjekord | Materjal | Aeg | Omandatav oskus |
|---|---|---:|---|
| 1 | [01 – Amet ja tööpäev](01_AMET_JA_TOOPAEV.md) | 35 min | Selgitad rolli ja osapooli |
| 2 | [02 – Raamatupidamise alused](02_FINANTSARVESTUSE_ALUSED.md) | 60 min | Eristad kulu, kohustist ja makset; teed lihtsa kande |
| 3 | [03 – Ostuarve teekond](03_OSTUARVE_TOOVOOG.md) | 50 min | Kontrollid arvet ja mõistad kooskõlastusringi |
| 4 | [04 – Eelarve ja aruandlus](04_EELARVE_JA_ARUANDLUS.md) | 55 min | Arvutad täitmise, hälbe ja oskad andmeid tõlgendada |
| 5 | [05 – Python, SQL ja Excel](05_PYTHON_SQL_EXCEL.md) | 75 min | Käivitad töötava mini-labori |
| 6 | [06 – Ülesanded ja lahendused](06_HARJUTUSED_JA_LAHENDUSED.md) | 90 min | Harjutad tööolukordi ja kontrollid vastuseid |
| 7 | [07 – Töövestlus](07_TOOVESTLUSE_ETTEVALMISTUS.md) | 30 min | Esitled oskusi ausalt ja konkreetselt |
| Lisad | [08 – Allikad ja jätk](08_ALLIKAD_JA_EDASINE_PLAAN.md) | 20 min | Leiad pärisandmed ning õiged juhendid |

### Esimene 90-minutiline õppeseanss

1. **20 min** – loe 01 ja selgita suuliselt ministeeriumi–RTK tööjaotust.
2. **25 min** – õpi 02 peatükist näide „1000 € + 24% käibemaks“.
3. **20 min** – loe 03 ja loetle ostuarve kontrollid.
4. **25 min** – täida 06 ülesanded 1–5 ja võrdle vastuseid.

## Failistruktuur

```text
finantsarvestuse_eelkursus/
├── README.md
├── 01_AMET_JA_TOOPAEV.md
├── 02_FINANTSARVESTUSE_ALUSED.md
├── 03_OSTUARVE_TOOVOOG.md
├── 04_EELARVE_JA_ARUANDLUS.md
├── 05_PYTHON_SQL_EXCEL.md
├── 06_HARJUTUSED_JA_LAHENDUSED.md
├── 07_TOOVESTLUSE_ETTEVALMISTUS.md
├── 08_ALLIKAD_JA_EDASINE_PLAAN.md
├── requirements.txt
├── andmed/naidisarved.csv
├── kood/arvete_kontroll.py
├── kood/avaliku_xlsx_uurimine.py
├── testid/test_arvete_kontroll.py
└── valjund/    (programm loob failid siia)
```

## Mini-labori käivitamine

Terminalis projekti juurkaustast:

```bash
python -m pip install -r requirements.txt
python kood/arvete_kontroll.py
python -m unittest discover -s testid -v
```

Programm loeb **sünteetilisi** arveid, tuvastab mitut liiki vigu, koostab SQLite-andmebaasi ja Exceli koondaruande. Tulemused salvestatakse kausta `valjund/`.

## Tähtsad piirid

- See ei ole SAP, RTIP-i ega e-arvete menetluskeskkonna tegelik liides.
- Näidisandmete kontrollireeglid ei asenda ametlikku raamatupidamisjuhendit, dokumentide nõudeid ega pädeva spetsialisti otsust.
- Käibemaksu arvutus ja sisendkäibemaksu mahaarvamise õigus on erinevad küsimused; näidetes ei eeldata automaatselt sisendkäibemaksu mahaarvamist.
- Avalikud riigieelarve koondandmed ei võrdu üksikarvete registriga.

## Põhilised ametlikud lähteallikad

- [RTK finantsarvestuse teenus](https://www.rtk.ee/finantsarvestus-personaliteenus/arvestusteenused/finantsarvestus)
- [Rahandusministeerium – riigi raamatupidamine](https://www.fin.ee/riigi-rahandus-ja-maksud/riigi-raamatupidamine)
- [2026. aasta riigieelarve ja selle täitmine](https://www.fin.ee/riigi-rahandus-ja-maksud/riigieelarve-ja-eelarvestrateegia/2026-riigieelarve)
- [Raamatupidamise seadus](https://www.riigiteataja.ee/et/akt/rps)
- [Avaliku sektori finantsarvestuse ja -aruandluse juhend](https://www.riigiteataja.ee/akt/103012025007)
- [EMTA – käibemaksumäärad](https://www.emta.ee/ariklient/maksud-ja-tasumine/kaibemaks/kaibemaksumaarad-ja-maksuvaba-kaive/uldine-kaibemaksumaar)
