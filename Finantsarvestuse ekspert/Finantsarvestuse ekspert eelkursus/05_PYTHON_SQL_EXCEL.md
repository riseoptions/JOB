# 05. Praktiline mini-labor: Python + SQL + Excel

## Eesmärk

Käivitad ühe programmi, mis:

1. loeb `CSV`-näidisarved;
2. kontrollib summasid, olulisi välju, kuupäevi ja võimalikke duplikaate;
3. salvestab andmed SQLite'i;
4. arvutab kulukeskuste koondi;
5. kirjutab aruande `XLSX`-faili.

**Kõik selles labori osas kasutatud arvekirjed on sünteetilised.**

## Paigaldamine (Windows, Thonny või VS Code)

1. Paki arhiiv lahti.
2. Ava terminal / käsurida kursuse kaustas.
3. Käivita:

```bash
python -m pip install -r requirements.txt
python kood/arvete_kontroll.py
python -m unittest discover -s testid -v
```

Valmivad failid:

```text
valjund/arvete_kontroll.xlsx
valjund/arved.sqlite
valjund/kontroll_raport.csv
```

Kui `python` käsk ei tööta, proovi Windowsis `py -3`.

## Milliseid automaatseid reegleid kontrollime?

| Reegel | Miks? | Veateade |
|---|---|---|
| Neto + KM = kokku | Aritmeetiline terviklus | `SUMMA_EI_KLAPI` |
| Sama tarnija ja arvenumber | Võimalik korduv menetlus | `VOIMALIK_DUPLIKAAT` |
| Tähtaeg ja kuupäev loetav | Andmete kvaliteet | `VIGANE_KUUPAEV` |
| Kulukeskus olemas | Analüüsi liigitus | `KULUKESKUS_PUUDUB` |
| KM aritmeetika 24%-ga tähistatud ridadel | Kontrolli illustratsioon | `KM_EI_KLAPI` |

Tegelikes arvete kontrollides on rohkem reegleid ning näiteks KM erisused nõuavad asjakohaseid andmeid ja professionaalset tõlgendust.

## SQL-päringud

Ava andmebaas näiteks DBeaveris või kasuta Pythonit.

**1. Kulude koond kulukeskuse järgi:**

```sql
SELECT kulukeskus,
       COUNT(*) AS arvete_arv,
       ROUND(SUM(CAST(kokku AS REAL)), 2) AS kokku_eur
FROM arved
GROUP BY kulukeskus
ORDER BY kokku_eur DESC;
```

**2. Võimalikud duplikaadid:**

```sql
SELECT tarnija, arve_nr, COUNT(*) AS kordusi
FROM arved
GROUP BY tarnija, arve_nr
HAVING COUNT(*) > 1;
```

**3. Kirjed, millel puudub kulukeskus:**

```sql
SELECT *
FROM arved
WHERE kulukeskus IS NULL OR TRIM(kulukeskus) = '';
```

**Täpsusmärkus:** `CAST(... AS REAL)` on siin näitlik SELECT-päringu mugavuslahendus; päris finantsarvutustes kasutatakse sendipõhiseid täisarve või kümnendarve, mitte binaarset ujukoma. Python-koodis kasutatakse `Decimal`-tüüpi.

## CSV ja Exceli erinevus

- `CSV`: lihtne teksttabel, ei hoia mitut lehte ega vormindust.
- `XLSX`: mitu lehte, vormindus ja kasutajale mugav väljund.
- `SQLite`: päringud ja kontrollitav struktureeritud kohalik andmekogu.
- `pandas`: puhastamine, ühendamine, grupeerimine, Exceli import.
- `openpyxl`: Exceli kirjutamine ja vormindamine.

Põhimõte: **Python arvutab → Excel kuvab**.

## Harjutus: ametlik XLSX (pärisandmete uurimine)

1. Mine Rahandusministeeriumi 2026. aasta eelarve lehele.
2. Laadi alla avalik XLSX (seaduse eelarve või täitmise tabel).
3. Käivita:

```bash
python kood/avaliku_xlsx_uurimine.py "C:\\Users\\Sina\\Downloads\\fail.xlsx"
```

4. Vaata, mitu lehte on ning millistes ridades algavad tegelikud andmed.
5. **Ära ühenda** näidisarveid päris koondandmetega faktidena – need kirjeldavad erinevat detailsust ja näidisarved on fiktiivsed.

## Mida võiks töövestlusel näidata?

„Tegin kontrollitava väikese toru: Python loeb arved, leiab anomaaliad, salvestab SQLite'i ning koostab Exceli aruande. Kontrollisin töökindlust automaattestidega. See on õppedemo, mitte ametliku arvesüsteemi asendus.“
