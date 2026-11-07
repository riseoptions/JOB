# Teise etapi kasutusjuhend

## 1. Demo Thonnys

Paki projekt lahti. Ava `kood/etapp2_demo.py` ja vajuta F5. Väljundi lõpus näed täpset kaustateed. Demo ise valib näidisrollid ning sooritab ette kirjutatud õppeotsused. Oma menetluse puhul kasuta allolevaid samme: import ja kontroll ei kinnita ühtegi arvet.

| Väljundfail | Mida vaadata |
|---|---|
| finantsarvestus.sqlite | Kõik sisendid, kontrolliajaloog, menetlus ja kanded |
| kontrollitulemused.csv | Iga dokumendi viimase kontrolli vead ja hoiatused |
| menetluslogi.csv | Kes, millal, miks ja millisesse olekusse liigutas |
| rtk_valjuv.json | Kohalik näidisedastus; võrgupäringut ei tehta |
| rtk_vastus.json | Demo vastuvõtutulemus |
| kanded.csv | Üks kanne kolme reaga, raha senditäpsusega |
| tulemus.json | Demo kontrollpäev ja loendused |

CSV kodeering on UTF-8 BOM, eraldaja semikoolon. Rahaväljad on **sendid**, mitte eurod. `kontrollitulemused.csv` puuduv dokument võib tähendada veatut kontrolli; tervet registrit vaata SQLite'ist. Vana kontrolliajaloog ei kordu selles CSV-s.

## 2. Sammhaaval terminalis

Käivita käsud projekti juurkaustas. Windowsis sobib Thonny „Open system shell“ või PowerShell. Kui `python` pole käsuna leitav, kasuta Windowsi `py` käsku.

```bash
python kood/etapp2_cli.py --db valjund/minu_demo.sqlite init
python kood/etapp2_cli.py --db valjund/minu_demo.sqlite import andmed/sunteetilised/etapp2_sisend.csv
python kood/etapp2_cli.py --db valjund/minu_demo.sqlite check ALL
python kood/etapp2_cli.py --db valjund/minu_demo.sqlite list
```

`check` kuvab leiud ja salvestab kontrolliajaloo; see ei tee olekuotsust. Muude toimingute blokeerimisel tagastab käsurida veakoodi 2.

```bash
python kood/etapp2_cli.py --db valjund/minu_demo.sqlite act DEMO-001 ESITA --actor analuutik --reason "Septembri teenus; tähtaja ja perioodi hoiatused on üle vaadatud"
python kood/etapp2_cli.py --db valjund/minu_demo.sqlite act DEMO-001 KOOSKOLASTA --actor sisukinnitaja --reason "IT-teenus on õppejuhtumis vastu võetud"
python kood/etapp2_cli.py --db valjund/minu_demo.sqlite act DEMO-001 KINNITA --actor eelarvejuht --reason "Õppejuhtumi kuluallikas ja teenuse periood kinnitatud"
python kood/etapp2_cli.py --db valjund/minu_demo.sqlite export DEMO-001 valjund/saadetis.json --reason "Kõik hoiatused on kinnitusringis läbi vaadatud"
python kood/etapp2_cli.py --db valjund/minu_demo.sqlite accept valjund/saadetis.json
```

Vaikimisi kontrollpäev on 2026-11-05. Teise kuupäeva jaoks lisa enne alamkäsku `--as-of 2026-11-10`. Ära vali kuupäeva eesmärgiga hoiatusi peita: see kirjeldab analüüsi tegelikku seisu. Demo korduskäivituse võrreldavuseks jäta vaikepäev alles.

## 3. Vigase dokumendi parandamine

SISEND või TAGASTATUD dokumenti saab parandada uue versioonina. Tee CSV, millel on samad päised ja täpselt üks parandatud rida. Anna sellele uus invoice_id, näiteks VIGA-003-R2; tarnija arvenumber võib säilida. Paranda tegelik vea põhjus.

```bash
python kood/etapp2_cli.py --db valjund/minu_demo.sqlite correct VIGA-003 minu_parandus.csv --reason "Brutosumma parandatud algdokumendi järgi"
python kood/etapp2_cli.py --db valjund/minu_demo.sqlite check VIGA-003-R2
```

Vana dokument saab ASENDATUD oleku, uus alustab SISEND-olekust ja peab läbima kinnitusringi. Vana sisu ning põhjendus jäävad alles. Parandus ei ole makstud arve tühistamise mehhanism.

## 4. SQL DBeaveris

Ava SQLite'i ühendus ja vali demo `finantsarvestus.sqlite`. Ava `sql/003_paringud.sql`. Käivita päringuid ükshaaval: sisendid, viimased vead, ühe dokumendi ajalugu, kande tasakaal ja edastused. Esimene SQL-fail on skeemi loomiseks; seda olemasolevas andmebaasis uuesti ei käivitata.

## 5. Colab

Laadi `kood/Etapp2_Colab.ipynb` Colabisse ja järgi lahtreid. Seal käivitub sama demo ja testikomplekt. Colabi kasutajaliidest pole siin eraldi testitud, kuid märkmiku tavapärased Python-käsud ning demo on kontrollitud kohalikus keskkonnas.

## Tõrkeolukorrad

- „Blokeerivad vead“: käivita `check ID`, paranda sisend uue versioonina.
- „Lubamatu olekuüleminek“: vaata `list`; kinnitusringi samme ei saa vahele jätta.
- „Sama ID all erinev sisu“: kordusimport ei ole redigeerimine; kasuta `correct`.
- „Edastuse kontrollsumma erineb“: taastamiseks ekspordi algne pakett uuesti. Ära muuda JSON-is summat.
- SQLite'i fail lukus: lõpeta teises rakenduses kirjutustehing ja proovi uuesti.

Võid uut demo korduvalt käivitada. Tööks kasutatava andmebaasi kustutamine pole vajalik.
