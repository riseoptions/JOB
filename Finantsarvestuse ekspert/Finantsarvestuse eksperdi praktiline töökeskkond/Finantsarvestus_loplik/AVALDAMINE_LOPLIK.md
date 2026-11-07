# Lõppversiooni avaldamine

Rakendus: https://finantsarvestus-risto.tonedcoot2.chatgpt.site

Etapi 4 juurdepääs oli omaniku kontoga piiratud. Etapi 5 ettevalmistus eemaldab avalikust dist-kaustast vana tervik-ZIP-i ja isikliku profiiliteksti. Publitseeritakse ainult avalikud koondandmed, sünteetilised arved ja üldised õppematerjalid. Täispakett ning kandideerimisdokumendid tuleb tööandjale anda eraldi. 7.11.2026 avaldamine õnnestus. Jagamise API kinnitas public (revisjon 2), kuid väljalogitud Chrome näitas ka pärast uuesti laadimist „Log in to access”. Seega kontovaba ligipääsu ei kinnitata. Ära eelda, et tööandja saab selle lingi kontota avada; kasuta allpool kirjeldatud Pagesi alternatiivi või ekraanipilte. Tõend: [ligipääsuvaade](materjalid/kuvatommised/ligipaas.png).

## GitHub Pagesi alternatiiv

1. Paki `tarne/Finantsvaade_avalik_demo.zip` lahti.
2. Loo enda GitHubis avalik hoidla (näiteks finantsvaade-demo). Lisa lahtipakitud failid hoidla juurkausta, säilitades alamkaustad ja `.nojekyll` faili. Ära lisa tervikpaketti ega isiklikke materjale.
3. Settings → Pages → Deploy from a branch → main → /(root) → Save.
4. Oota Pagesi juurutuse edu ja ava GitHubi kuvatud täpne URL väljalogitud brauseris. Kontrolli avalehte, importi ja Exceli allalaadimist.
5. Kui kasutad terviklikku lähtekoodi, vali Pagesi all GitHub Actions ning kasuta `.github/workflows/pages.yml`. See paigaldab sõltuvused, ehitab, testib ja avaldab ainult dist-kausta. Enne lähtekoodi avalikustamist eemalda isiklikud lähteülesanded/materjalid.

GitHub Pages ei käita serveripoolset Pythonit ega SQLite'i. Avalikud aruanded arvutab ehitusskript; import ja arvete kontroll toimuvad Pyodide'is brauseris. GitHubi ligipääsu selles töös ühendatud ei olnud, mistõttu päris GitHubi juurutust ei väideta.

## Kohalik ja esitlusvaru

`python -m http.server 8000 --directory dist`, seejärel http://localhost:8000. Kui hosti ühendus puudub, kasuta [ekraanipiltidega esitlust](ESITLUS_EKRAANIPILTIDEGA.md). Kohalik demo ei vaja internetist CDN-faile: käituskeskkond on kaasa pakitud. Hoia lähtekood ja ZIP kontrollsummad alles. Avaliku demo ZIP ei sisalda kandideerimispaketti.
