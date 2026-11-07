# Teise etapi tulemused · 5.11.2026

Teostati ainult finantsdokumentide menetlemise etapp. Esimese etapi pärisandmed ja tulemused on kumulatiivses pakis säilinud. Kulude analüüsi, Exceli juhtimisaruandeid ega veebilehte ei loodud.

## Kontrollitud demonstratsioon

- 17 fiktiivset sisenddokumenti, millest 11 sisaldavad tahtlikult vigu.
- DEMO-002 saab lisaks duplikaadivea, sest VIGA-007 jäljendab sama tarnija arvenumbrit.
- Üks dokument KAJASTATUD, üks TAGASTATUD ja 15 SISEND.
- Üks tasakaalus kanne, 3 kanderida, D = K = 124 000 senti.
- SQLite `integrity_check`: ok; `foreign_key_check`: 0 viga.
- Muudetud JSON-pakett ei saa kannet. Kordusvastuvõtt ei tekita topeltkannet.
- Parandusdokumendi uus versioon säilitab vana toorinfo ja seose.

Kaasas on päriselt käivitatud demo andmebaas, kontrollileiud, menetluslogi ja kohalikud edastusfailid.

## Testimine

Kõik **22 automaattesti** läbisid: 5 esimese etapi regressioonitesti ja 17 teise etapi testi. Logi: `materjalid/testitulemus_etapp2.txt`.

Teise etapi katvus: puuduvad väljad; vigased kuupäevad; summad ja ümardamine; negatiivne või kümnendmurruline sentide arv; NaN/Infinity ning keelatud määr; tundmatu konto/kulukeskus; tulevik ja tähtajad; sünteetilise päritolu nõue; kordusimport; impordipartii rollback; puuduva ID säilitamine; duplikaadi mõlema poole leidmine; rollid ja olekud; tervikvoog; kordusvastuvõtt; JSON-i rikkumine; hiljem lisatud duplikaat; tagastamine; logi muutmise/kustutamise keeld; parandusversioon; katkestatud kande rollback; korduseksport; skeemi taasavamine.

Need on näidisreeglite ja lokaalse tarkvara testid. Need ei tõenda HTM-i pärisprotsesside ega SAP-i liidese toimimist. Konkreetne maksukäsitlus ja tegelikud kontod vajavad asutuse juhendeid.

## Järgmise etapi alus

Etapp 3 saab kasutada sama koodi, tuvastatud andmepiire ning säilitatud eelarvefaile. Enne täitmisprotsendi lisamist tuleb endiselt leida võrreldav eelarveversioon ja ulatus. Etapp 3 ootab kasutaja järgmist korraldust.

Täiendav lõppkontroll: üheksa käsureakäsku (loomisest näidiskandeni) läbisid, kõik 11 sihilikku vigast sisendrida andsid oodatud veakoodid. Colabi märkmike Python-süntaks ja Markdowni siselingid kontrolliti.
