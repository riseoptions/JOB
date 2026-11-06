# Testimine · etapp 3

Kontrollitud 06.11.2026 Linuxis Python 3.12.14-ga. Sõltuvused: openpyxl 3.1.5, Pydantic 2.13.4, Polars 1.44.2, pandas 2.2.3.

```bash
python -m unittest discover -s testid -v
```

**Tulemus: 37/37 testi läbis.** Enne muudatusi läbisid kõik 22 testi; pärast muudatusi läbivad need koos 15 uue testiga. Täpne logi: `materjalid/testitulemus_etapp3.txt`.

| Kontroll | Tõend |
|---|---|
| Etapp 1, 5 testi | Allika räsi, ümardamine, puuduvad väärtused, summad, sünteetiliste andmete korratavus |
| Etapp 2, 17 testi | Rollid, duplikaadid, veakoodid, korduskindlus, parandused, audit, kande tasakaal ja rollback |
| Etapp 3, 15 testi | Tüübitud CSV, lisaväljad, bool/float keeld, kuupäevad, vana reegli säilitamine, eelarve koondsummad, null/puuduv väärtus, Polars/pandas võrdsus, puuduvad/duplikaatkuud, aastavõrdlus, toetuse piir/ümardus/tagasinõue, SQL, perioodipiir, muudetud sisendi XLSX |

Täiendavalt käivitati mõlemad demod ning Pydanticu praktiline näide. Etapi 2 tulemus säilis: 17 dokumenti, 15 SISEND, 1 TAGASTATUD, 1 KAJASTATUD, üks tasakaalus kanne, 0 FK viga, integrity=ok. Etapi 3 väljundid loodi ja SQL koond võrreldi Pythoni tulemusega.

Exceli kolm lehte (Eelarve, Kulud, Toetused) renderdati ning vaadati visuaalselt üle. Väljundväärtuste kontrollis eelarve põhinäitajad klappisid; Exceli veaväärtusi ei leitud. XLSX ei sisalda arvutusvalemeid: tulemused arvutab Python. Muudetud toetuse määra/ettemakse test kinnitas aruande uuenemist uuel genereerimisel. Exceli töölauarakenduses ja Thonny/Colabi kasutajaliideses käsitsi ei testitud; Colabi koodirakud läbivad süntaksikontrolli.

Jõudlusmõõtmine on demonstratsioon, mitte läbimise kriteerium. Numbriline tulemuste võrdsus on kohustuslik; millisekunditele lävendit ei kehtestata.
