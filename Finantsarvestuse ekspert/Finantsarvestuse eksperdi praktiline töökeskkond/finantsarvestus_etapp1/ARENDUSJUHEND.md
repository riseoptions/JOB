# Arendusjuhend

Python 3.10+; tarnet testiti Python 3.12 ja openpyxl 3.1.5 abil.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
python -m pip install -r requirements.txt
python kood/etapp1.py
python kood/loo_naidisandmed.py
python -m unittest discover -s testid -v
```

`etapp1.py` teeb ainult esimese etapi väljavõtte ja andmeprofiili. Koodi sisendileping on seotud säilitatud failidega. `cents()` ei parsi suvalist rahateksti, vaid ootab Exceli arvulist väärtust. Sõne või tõeväärtuse korral katkestab teisenduse.

Algfailide hankimisel kasutati HTTPS-i ja brauseri User-Agent päist. Ilma päiseta andis allikas HTTP 403; päisega õnnestus mõlema faili allalaadimine. Tavaline käivitamine ei vaja internetti. `allikaregister.json` säilitab tegeliku allalaadimisaja UTC-s, faili suuruse ja SHA-256. Registri aeg on tehnilise keskkonna kellaaeg; koostamise kuupäev dokumentides on Eesti aja järgi 5.11.2026.

## Järgmiste etappide muutmisreeglid

- Algallika muutus → uus allikaversioon, uuendatud kaardistus ja testid.
- Tabeliveeru eemaldamine või tähenduse muutus → skeemiversiooni muutus ja migratsioon.
- Säilita stabiilsed identifikaatorid ja eraldi andmekihid.
- Ära nimeta FitekIN-i või SAP-i simulatsiooni pärisliideseks.
- Finantsreegel peab saama inimloetava kirjelduse, vea koodi ja sisulise testi.
- Hilisema Exceli ekspordi arvutused tehakse Pythonis; xlsx-failis olev kuvatav tulemus ei tohi sõltuda uuest valemiarvutusest.

SQL-faili võib kontrollida sqlite3-ga mälus. See ei impordi andmeid ega teosta 2. etapi menetlust.
