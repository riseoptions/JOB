> **Uuendus 0.2:** teine etapp on teostatud. Allolev tekst säilitab esimese etapi lähteolukorra. Kehtivad täiendused: [teise etapi spetsifikatsioon](ETAPP2_TEHNILINE_SPEC.md), [kasutusjuhend](KASUTUSJUHEND_ETAPP2.md) ja [tulemused](ETAPP2_TULEMUSED.md). Etapid 3–5 ootavad korraldust.

# Kasutusjuhend · esimene etapp

## Ilma Pythonita

Paki ZIP lahti. Loe README-d ja õppemoodulit. Ava algandmete XLSX-failid Excelis või LibreOffice'is. Ava CSV vajadusel menüüst **Andmed → Tekstist/CSV-st**, vali UTF-8 ja semikoolon. `line_id` ja muud koodid määra tekstiks. `amount_cents` on sentides: eurode saamiseks jaga 100-ga. Summadel säilib algallika märk.

## Thonny / Windows 11

1. Paki kogu projekt ühte kausta, mitte ära ava skripti otse ZIP-ist.
2. Thonny menüüst Tools → Manage packages paigalda `openpyxl` (paketis kasutatud versioon 3.1.5).
3. Ava `kood/etapp1.py` ja käivita F5. Tulemused tekivad alati projekti enda `andmed/toodeldud` kausta, sõltumata Thonny töökaustast.
4. Ava `kood/loo_naidisandmed.py`, käivita F5.
5. Kontrolltestide jaoks ava projekti kaustas terminal ja käivita `python -m unittest discover -s testid -v`.

## Colab

Ava `kood/Etapp1_Colab.ipynb` Colabis ja laadi üles projektipakett. Märkmik paigaldab openpyxl-i, pakib projekti lahti ning käivitab samad skriptid ja testid. Colabi kasutajaliidest selles töös eraldi läbi ei klõpsatud; samad Pythoni käsud on kohalikus keskkonnas testitud.

## Väljundite lugemine

- `htm_eelarve_2026.csv`: 17 seaduserida × 2 mõõdikut = 34 kirjet.
- `htm_taitmine_2026.csv`: 9 rida × (9 kuud + 2 YTD-perioodi) = 99 kirjet.
- `kooskolakontroll.csv`: iga lähterea kuude summa versus avaldatud üheksa kuu summa.
- `profiil.json`: lehed, ulatus, valemid, puuduva vahemälu arv ja võrdluspiirang.
- `naidisarved.csv`: 6 fiktiivset sisendarvet, mitte päris HTM-i dokumendid.

Ära liida kogu täitmise CSV-d: see liidaks kuud ja YTD ning koond- ja sh-read topelt. Vali üks mõõdik ja üks perioodiliik. Välistoetuste rida on rahastusallika ristlõige, mitte lisakulu teiste ridade kõrval.

## Veateated

`ModuleNotFoundError: openpyxl` → paigalda teek selle Pythoni jaoks, millega käivitad.

`Algfaili kontrollsumma erineb` → ära muuda lihtsalt registri kontrollsummat. Taasta paketi algfail või tee uue versiooni teadlik kaardistus.

`Struktuur on muutunud` → uus fail vajab lahtrite ja metoodika ülevaatust.

`PermissionError` → sulge avatud väljundfail Excelis ja käivita uuesti.

## GitHubi lisamine

Loo tühi hoidla ja laadi lahtipakitud projekti sisu üles. Kui brauseri failipiirang segab, kasuta GitHub Desktopi. Avaldamist, hoidla loomist ja GitHub Pagesi selles etapis ei tehtud.
