# GitHub Pagesis avaldamine

## Etapi 5 kehtiv täiendus

Etapi 5 jaoks kasuta AVALDAMINE_LOPLIK.md juhist ja tarne/Finantsvaade_avalik_demo.zip-i. Actions kasutab paki_etapp5.py-d ning avaldab ainult dist-kausta. Ära laadi avalikku veebikausta varasema etapi tervik-ZIP-i ega kandideerimismaterjale.

## Valmis projekti tee

1. Loo GitHubis repositoorium. Paki projekti ZIP lahti ja lisa **kausta sisu** repositooriumi juurkausta. Kasuta Giti, GitHub Desktopi või VS Code'i; suure projekti üleslaadimiseks on need mugavamad kui veebilehe faililisaja.
2. Kontrolli, et juurkaustas on requirements.txt, kood/, veeb/, dist/ ja .github/workflows/pages.yml. Punktiga algav .github kaust peab samuti kaasa minema.
3. Ava repositooriumi Settings → Pages. Vali Source: **GitHub Actions**.
4. Tee push main harusse või käivita Actions alt „Avalda finantsvaade“ käsitsi.
5. Workflow paigaldab Pythoni sõltuvused, ehitab dist/, käivitab testid, pakib allalaaditava projekti ja avaldab dist/ sisu.
6. Ava workflow deployment-väljundis näidatud URL. Kontrolli ülevaadet ning impordi näidis-CSV. Veeb kasutab suhtelisi failiteid, et töötada ka repositooriumi alamteel.

GitHubi repositooriumit selles töös ei loodud ega sinna sisse logitud. Pakett on avaldamiseks ette valmistatud; Sitesi avaldamine on eraldi majutusvõimalus. GitHubi töövoo kaugkäivitust ei väideta testituks.

## Lihtne alternatiiv ilma Actionsita

Käivita kõik ehitus- ja testikäsud lokaalselt. Kopeeri dist/ sisu repositooriumi docs/ kausta, vali Settings → Pages → Deploy from a branch → main → /docs. Kopeeri ka .nojekyll. Ära vali kogemata terve projekti juurkausta, kus avaleht ei asu.

## Andmete uuendamine

Veeb kuvab kaasasolevat kontrollitud andmeväljavõtet. Uue ametliku XLSX-faili puhul täienda allikaregistrit, kontrolli kaardistust ja võrdlusmetoodikat, seejärel käivita ehitus ning testid. Ainult lehe uuesti avaldamine ei hangi uusi algandmeid.

Kaasasolev workflow ei ole ajastatud ja ei kutsu kolmandaid API-sid. Automaatne uute allikate hankimine vajab eraldi kontrollitud ülesannet. GitHub Pages serveerib faile; Python töötab ehituse ajal ja kasutaja brauseris. Seansi SQLite ei ole serveri püsisalvestus.

Pyodide runtime on failidena kaasas. Avalik leht ei tohi sisaldada päris arveid, autentimisvõtmeid ega mitteavalikke finantsandmeid. GitHubi avaldamisel on dist/ failid külastajale allalaaditavad.
