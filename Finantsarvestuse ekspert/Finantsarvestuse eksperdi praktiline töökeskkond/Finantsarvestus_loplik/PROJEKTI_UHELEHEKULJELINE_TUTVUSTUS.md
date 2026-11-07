# Finantsvaade – kontrollitava finantsanalüüsi õppeprojekt

**Portfoolionäide finantsarvestuse eksperdi ametikohale.** Sõltumatu demonstratsioon, mitte HTM-i ega RTK ametlik infosüsteem.

Projekt ühendab matemaatika-, majandus- ja IT-tausta avaliku sektori finantsarvestuse õppimisega. Eesmärk on näidata, kuidas märgata ostuarve andmeviga, võrrelda sobivaid finantsnäitajaid ja koostada korratav aruanne. Projekt valmis AI-abiga; valmisolekut tuleb hinnata ka selle järgi, kas oskan lahendust ise selgitada ja kontrollida.

**Probleem:** käsitsi failide liitmisel võivad tekkida topeltarvestus, vale periood, ühikuviga ja märkamata duplikaat. Lahendus seob kontrollireeglid, allikaviited ja CSV/Exceli aruanded. Leid suunab inimest uurima; süsteem ei kinnita arveid ega tee makseid.

**Näidatav tulemus:** eestikeelne eelarveülevaade, sünteetiliste arvete import ja veapõhjused, asutuse/perioodi filtrid, graafikud ja aruanded. Tehnoloogiad on Python, SQLite, Pydantic v2, Polars, pandas, openpyxl ja Pyodide. Avalikud koondandmed ja fiktiivsed arved on eristatud. Imporditud andmed jäävad brauseri ajutisse mällu.

**Seos ametiga:** projekt harjutab andmete kontrolli, eelarveanalüüsi, aruande tõlgendamist ja täpset probleemikirjeldust koostööks. Õpikohad olid kulu/makse eristamine, võrreldava nimetaja valik, puuduvad väärtused ja valideerimise piirid.

**Aus enesehinnang:** tugevuseks on IT- ja analüüsitaust. Praktiline finantsarvestuse kogemus on piiratud; projekt ei tõenda SAP-i või RTIP-i igapäevast töökogemust. Vajaksin asutuse sise-eeskirja, maksuerandite ja töövoogude juhendatud õppimist.

Tõendid: lähtekood, [testiraport](TESTIRAPORT_LOPLIK.md), allikaregister ja [neljaminutiline demo](DEMONSTRATSIOONI_KAVA.md). Veeb: https://finantsarvestus-risto.tonedcoot2.chatgpt.site
