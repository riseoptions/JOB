# Finantsarvestuse ja kulude analüüsi töökeskkond

## Etapp 2 · finantsdokumentide menetlemine · versioon 0.2

Iseseisev eestikeelne õppeprojekt. Käesolev pakett jätkab esimese etapi arhitektuuri ja sisaldab nii esimese etapi faile kui ka teise etapi täiendusi. Etappe 3–5 pole teostatud.

**Valmis:** Pythoni arvekontroll, SQLite'i andmebaas, rollidega menetluse simulatsioon, paranduste ajalugu, kohalik RTK-JSON-i näidisvahetus, tasakaalus näidiskanne, SQL-päringud ja järgmine õppemoodul. See ei ole ametlik SAP-i ega RTK liides.

## Kiire käivitamine

Paki kogu ZIP lahti. Ava Thonnys `kood/etapp2_demo.py` ja vajuta F5. Kui openpyxl puudub, paigalda see Thonny paketihaldurist. Terminalis projekti juurkaustast:

```bash
python -m pip install -r requirements.txt
python kood/etapp2_demo.py
python -m unittest discover -s testid -v
```

Iga käivitus loob uue ajatempliga kausta `valjund/etapp2/` alla. Eelmist andmebaasi ei kirjutata üle. Kaasasolev kontrollitud näidisväljund on `valjund/etapp2/kontrollitud_naidis/`.

## Demo tulemus

17 sünteetilist sisendrida: esimese etapi 6 arvet ning 11 sihilikult vigast juhtu. Üks arve jõuab olekusse KAJASTATUD, üks TAGASTATUD ja 15 jäävad SISEND-olekusse. SISEND ei tähenda alati viga: demo ei menetle kõiki korras arveid automaatselt.

DEMO-001 näidiskanne: D teenusekulu 1000 €, D käibemaksukulu 240 €, K tarnijavõlg 1240 €. Teenuse kuupäev määrab näite arvestusperioodi. Sisendkäibemaksu mahaarvamist selles näites ei eeldata. Ühtegi makset ei tehta.

## Loe ja proovi

- [Teise etapi kasutusjuhend](KASUTUSJUHEND_ETAPP2.md): Thonny, käsurida ja DBeaver.
- [25-minutiline õppemoodul](OPPEMOODUL_02.md): tööolukorrad, arvutused, Python ja SQL.
- [Kontrollireeglid](KONTROLLIREEGLID.md): täpsed koodid, vead ja hoiatused.
- [Menetlus ja andmemudel](ETAPP2_TEHNILINE_SPEC.md): olekud, rollid, migratsioon ja piirid.
- [Tulemused ja testid](ETAPP2_TULEMUSED.md).
- [Esimese etapi õppemoodul](FINANTSARVESTUSE_OPPEMATERJAL.md) ja [esimese etapi tulemused](ETAPP1_TULEMUSED.md).

## Failid

| Asukoht | Otstarve |
|---|---|
| kood/menetlus.py | Teise etapi ärireeglid ja tehingud |
| kood/etapp2_demo.py | Korratav tervikdemo |
| kood/etapp2_cli.py | Sammhaaval käsitsi menetlemine |
| kood/loo_etapp2_naidised.py | Sihilikult vigaste näidiste generaator |
| kood/Etapp2_Colab.ipynb | Colabi käivitusjuhis |
| sql/001_skeem.sql | Säilitatud esimese etapi skeem |
| sql/002_menetlus.sql | Migratsioon versioonile 0.2 |
| sql/003_paringud.sql | Kuus praktilist päringut ja FK-kontroll |
| andmed/sunteetilised/etapp2_sisend.csv | 17 fiktiivset sisenddokumenti |
| valjund/etapp2/kontrollitud_naidis | SQLite, kontrollid, logi, JSON-vahetus ja kanded |

Esimese etapi avalikke andmeid ja algseid näidisarveid ei muudetud. Järgmine töö on alles kasutaja korralduse järel 3. etapi kulude analüüs ja aruandlus. Praegu ei ole veebilehte ega finantsanalüüsi koondaruannet.
