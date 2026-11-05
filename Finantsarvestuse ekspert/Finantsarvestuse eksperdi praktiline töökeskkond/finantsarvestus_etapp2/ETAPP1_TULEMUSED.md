# Esimese etapi tulemused

Koostatud 5.11.2026. Algne lähteülesanne on `materjalid/ALGNE_LAHTEULESANNE.txt`.

## Valmis

- Kaks ametlikku Exceli algfaili ja allikaregister koos failiräsidega.
- Taaskäivitatav Pythoni väljavõte ja andmeprofiil.
- HTM-i algse eelarve 34 kirjet ning täitmise 99 kirjet.
- Üheksa lähterea kuusummade kooskõlakontroll.
- Kuus fiktiivset arvet koos deterministliku generaatoriga.
- Projekti- ja tarkvaraspetsifikatsioon, arhitektuur, andmemudel, SQL-kavand, kasutus- ja arendusjuhend.
- 25-minutiline õppemoodul: viis teemat A–I ülesehituses, viis ülesannet lahendustega, kümme kontrollküsimust ja sõnastik.

## Esimene sisuline kontroll

| Allika lahter | Näitaja | Väärtus |
|---|---|---:|
| Seaduse esimene leht D108 | HTM-i valitsemisala algne aastane kulueelarve | −1 176 947 117,00 EUR |
| Seaduse esimene leht D109 | HTM-i enda algne kulueelarve | −753 956 428,00 EUR |
| Täitmise leht N137 | HTM-i valitsemisala kulud ja investeeringud, v.a amortisatsioon; 9 kuud 2026 | 886 184 288,61 EUR |
| Täitmise leht N138 | Sama ploki tööjõukulud; 9 kuud 2026 | 192 474 964,76 EUR |

Asutuste eelarveridade D109:D117 summa võrdub koondreaga D108. Täitmise kõigi valitud ridade B:J summa võrdub N-veeruga; tegelik erinevus on kõigil üheksal real **0 senti**. See kinnitab väljavõtte aritmeetilist kooskõla, mitte kogu riigieelarve auditeeritust.

Täitmise failis „Haridus-ja Teadusministeerium“ asub valitsemisalade plokis. Seda ei samastata üksnes ministeeriumi enda D109 eelarvega. Kulude ja investeeringute mõõdikut ei võrrelda automaatselt algse kulueelarvega. Seetõttu eelarve täitmise protsenti ei väljastata.

## Teadaolevad piirid

- Väljavõte katab valitud HTM-i ploki, mitte kogu töövihikut.
- Septembri täitmine ei ole novembri hetkeseis ega terve aasta tulemus.
- Eelarvemuudatusi ja ülekandeid ei ole algse eelarvega ühendatud.
- Tegelikku HTM-i kinnitusringi, SAP-i liidest ega asutuse kontoplaani pole rakendatud.
- Exceli olemasolevaid valemivahemälusid loeti; Microsoft Exceli ümberarvutamist ei testitud.
- Thonny ja Colabi kasutajaliidest ei testitud, käsud töötasid kohalikus Pythonis.
- Andmeallikate eraldi taaskasutuslitsents jäi tuvastamata.

## Järgmine etapp

Alles järgmise korralduse järel: näidisarvete kontrollireeglid, vigased testjuhtumid, SQLite'i andmete import, menetluse simulatsioon ja järgmine õppemoodul. Etappe 2–5 selle tarnega ei alustatud.
