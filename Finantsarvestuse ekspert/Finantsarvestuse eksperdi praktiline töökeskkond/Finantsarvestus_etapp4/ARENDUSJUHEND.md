# Arendusjuhend · 0.4

## Tööjärjekord

```bash
python -m pip install -r requirements.txt
python kood/ehita_veeb.py
python -m unittest discover -s testid -v
python kood/paki_etapp4.py
python -m http.server 8000 --directory dist
```

Muuda veebiliidest veeb/ kaustas, äriloogikat kood/ kaustas. Ehitusskript kopeerib vajalikud moodulid dist/python/ alla. Ära muuda neid koopiaid käsitsi. Ehitamine käivitab etapi 3 analüüsi ja kontrollib Polars/pandas tulemust. Uue allikafaili puhul tuleb üle kontrollida struktuur, ühik, periood, vastendus ja SHA, mitte üksnes fail asendada.

Brauseri käitus on fikseeritud: Pyodide 314.0.7, Pydantic 2.12.5 ja openpyxl 3.1.5. Kohalik Pydantic 2.13.4 jääb senise requirements.txt järgi. Brauseriversiooni uuendamisel korrata arve impordi, vigade, duplikaatide ning ekspordi teste. Kaasasolevad runtime failid on kolmanda osapoole sõltuvused, mitte projekti kirjutatud kood.

## Valikuline automaatne UI test

`testid/browser.spec.mjs` kasutab Playwright Testi. Kohalikus arenduskeskkonnas paigalda `npm install --save-dev @playwright/test` ja `npx playwright install chromium`. Käivita eelnevalt Python HTTP-server pordil 8000, seejärel `npx playwright test testid/browser.spec.mjs`. Testi baasaadress on keskkonnamuutujaga BASE_URL muudetav. Tarnimisel kontrolliti vastavaid põhitoiminguid lisaks päris Chrome'i brauseris; eraldi Playwright runnerit selles keskkonnas ei käivitatud.

## Serverita arhitektuuri piir

HTML/JS valib andmed ja kutsub Workerit. Uut finantsvalemit ära kirjuta JS-i: lisa see Pythoni moodulisse ja testi oodatud summaga. Töötava menetlusmootori kood on ühine. API või mitme kasutaja serveri lisamine on eraldi arhitektuuriotsus; Sites/GitHub Pages ei muutu selle tõttu Python-serveriks.
