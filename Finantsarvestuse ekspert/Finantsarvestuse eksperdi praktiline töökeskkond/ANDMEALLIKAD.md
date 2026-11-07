# Andmeallikad ja kasutamise piirangud

Kontrollitud 5.11.2026. Algallikad on avalikud koondandmed, mitte üksikarved. Kaks XLSX-faili on päriselt alla laaditud ja pakis muutmata kujul. Täpsed ajad ning kontrollsummad on `andmed/allikaregister.json` failis.

## Kasutatud andmestikud

### RE2026

- Fail: `re2026_seadus.xlsx`.
- [Otseallikas](https://www.fin.ee/sites/default/files/documents/2025-12/2026.%20aasta%20riigieelarve%20seadus.xlsx).
- Allalaadimise aeg (UTC): `2026-11-05T17:03:07.103402+00:00`.
- Maht: 146794 baiti.
- SHA-256: `53779ac09966e779df08430e6c3fa2f2c4cbd831e6b0d3410c6d56b85131dce7`.

### TAIT2026

- Fail: `re2026_taitmine_september.xlsx`.
- [Otseallikas](https://www.fin.ee/sites/default/files/documents/2026-11/2026.%20aasta%20riigieelarve%20t%C3%A4itmine%20majandusliku%20sisu%20j%C3%A4rgi%20%28september%29.xlsx).
- Allalaadimise aeg (UTC): `2026-11-05T17:03:18.407437+00:00`.
- Maht: 224645 baiti.
- SHA-256: `678de30e7461527bd2f41b1f7435357b78fdb28988f7ebfc823ae518abd4a98c`.

| Tunnus | RE2026 | TAIT2026 |
|---|---|---|
| Sisu | Algse 2026 riigieelarve seaduse avaldatud tabel | 2026 täitmine majandusliku sisu järgi, september |
| Periood | Terve 2026 aasta | Jaanuar–september 2026 ja sama periood 2025 |
| Ühik | Tuhanded eurod | Eurod |
| Lehed | Seadusepilt; täpsustatud eelnõu | Eelarve täitmine üheksa kuud |
| Valitud osa | Esimese lehe HTM ploki read 101–117, D:E | Read 137–145, B:J ja N:O |
| Väljund | 34 kirjet | 99 kirjet |
| Suurim lõks | Kulud negatiivsed; kokku ja sh ei liideta | Koond, alamread ja rahastusallika ristlõige kattuvad |

Seaduse failis on ka leht nimega „täpsustatud eelnõu“ ja esimesel lehel ajalooline eelnõu veerupealkiri. Väljavõttes kasutatakse ametlikul veebilehel seadusena avaldatud faili **esimest lehte**, mitte teise lehe muutmisveerge. Päritolu ja pealkirjade erisus on säilitatud, mitte vaikimisi ümber nimetatud.

Täitmise faili vormindatud ala on 788 × 632 lahtrit, kuid mittetühjad väärtused ulatuvad reani 258 ja veeruni 16. Seetõttu pole 632 veergu 632 sisulist tunnust. Kõigi 211 valemilahtri salvestatud väärtused olid olemas. Neid ei arvutatud Excelis uuesti ümber.

## Veebiallikate kontroll

- [Rahandusministeeriumi 2026 eelarve](https://www.fin.ee/riigi-rahandus-ja-maksud/riigieelarve-ja-eelarvestrateegia/2026-riigieelarve) — Leht avanes; XLSX-lingid kontrollitud; kasutatud kaks faili. Täitmise lehel on septembri majandusliku sisu fail ja augusti seadusepildi fail.
- [RTK finantsarvestus](https://www.rtk.ee/finantsarvestus-personaliteenus/arvestusteenused/finantsarvestus) — Avanes; avalikud teenuseülesanded ja SAP/BO/RTIP/e-arvete viited.
- [RTIP](https://www.rtk.ee/riigitootaja-iseteenindusportaal) — Avanes; kinnitatud andmete automaatne liikumine SAP-i avalikult kirjeldatud.
- [HTM programmid](https://hm.ee/ministeerium-uudised-ja-kontakt/ministeerium/strateegilised-alusdokumendid-ja-programmid) — Avanes; programmid, tulemusaruanded ja eelarveviide Rahandusministeeriumile.
- [Eelarve täitmise metoodika](https://www.fin.ee/riigi-rahandus-ja-maksud/riigieelarve-ja-eelarvestrateegia/tegevuspohise-eelarvestamise-kasiraamat/eelarve-taitmise-ulevaade) — Aadress avanes käsiraamatu lehele; selle põhjal ei kinnitatud kahe valitud mõõdiku täielikku võrreldavust.
- [Riigiraha](https://www.riigiraha.fin.ee/) — Selle aadressi sisu ei olnud kontrollivahendiga loetav. API või eksport kontrollimata; ei kasutatud andmeallikana.
- [Avaandmed](https://avaandmed.eesti.ee/) — Suunas andmed.eesti.ee lehele; loetavat andmestikku ei saadud. API-t ei eeldatud.
- [RIK](https://www.rik.ee/) — Avanes ja suunas /et lehele. Käesolevas etapis registriandmeid ei laaditud.
- [Üldeeskiri](https://www.riigiteataja.ee/akt/103012025007) — Ametlik otsingutulemus näitas 06.01.2025 jõustunud tervikteksti kehtivana; otsese lehe sisu nõudis JavaScripti. Paragrahvide täielikku auditit ei tehtud.
- [EMTA](https://www.emta.ee/uudised/maksumuudatused-2026) — Avanes; 2026 standardne käibemaksumäär 24%.

## Kasutustingimused

Avalikud failid olid ligipääsetavad ilma autentimiseta. Andmestiku juures eraldi litsentsitähist ei tuvastatud; CC-litsentsi ei eeldata. Kaasas on allikaviited ja muutmata avalikud koondtabelid õppeotstarbel. Veebilehtede kujundust ega pikki tekste ei kopeerita. Koodi edasine litsentsivalik ei muuda ametlike lähtefailide kasutustingimusi. API automaatkasutuse ega piiramatu taaskasutuse õigust siin ei kinnitata.

## Andmetöötluse reeglid

1. Algandmeid ei muudeta. SHA-256 kaitseb märkamatute muudatuste eest.
2. Raha teisendatakse Decimaliga ja senditäpsusega; algne väärtus säilib CSV-s.
3. Algallika miinusmärki ei pöörata automaatselt positiivseks.
4. Tulevaste kuude K:M nullid ei ole kinnitatud tegelikud tulemused ja jäetakse välja.
5. Kriips ei tähenda vaikimisi nulli. Selle tähendus vajab allika metoodikat.
6. Üheksa kuu summa kontroll ei tõenda täielikku vastavust raamatupidamisregistrile.
7. Eelarve täitmise protsendiks on vaja sama ulatuse ja seisuga nimetajat. Algne kulueelarve ei sobi automaatselt kulude ja investeeringute nimetajaks.
8. Sünteetilisi arveid ei ühendata tegelike koondandmetega ega esitata nende detailidena.

Riigihangete tehinguandmete ja toetuste detailandmestiku import ei ole esimese etapi sõltuvus; need jäävad võimaliku hilisema laienduse uurimisvajaduseks.
