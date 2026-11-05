# 06. Praktilised ülesanded koos lahendustega

**Reegel:** proovi vastus kõigepealt iseseisvalt ja alles siis loe lahendust. Kasuta näidetes fiktiivset „Haridusamet X-i“.

## Osa A – mõistmine

**1. Mis vahe on kulul ja maksel?**  
**Vastus:** kulu näitab aruandeperioodil tarbitud ressurssi, makse raha liikumist; kuupäevad võivad erineda.

**2. Miks peab teadma teenuse osutamise perioodi?**  
**Vastus:** tekkepõhises arvestuses määratakse kulu majandustehingu sisu ja perioodi järgi, mitte üksnes arve saabumise või makse kuupäeva alusel.

**3. Kas RTK teeb alati kõik arve menetluse sammud?**  
**Vastus:** ei. Ülesannete jaotus sõltub asutusega kokkulepitud toimemudelist.

**4. Kas arve sama number näitab tingimata pettust?**  
**Vastus:** ei. Kordumine on kontrollisignaal; võimalikud õigustatud põhjused on näiteks parandused, kordused andmeimpordis või vale tunnuste kombinatsioon.

**5. Millist küsimust küsid, kui kvartalikulu on eelarvest suurem?**  
**Vastus:** kas võrreldavad perioodid, eelarveversioon, liigitus ja arvestusalus on samad; seejärel otsin ajastuse, hinnamuutuse ja ühekordsete sündmuste mõju.

## Osa B – arvutused

**6. Arve alussumma on 1750 € ja kehtib 24% KM. Arvuta KM ja arve kokku.**

**Lahendus:** `1750 × 0,24 = 420 €`; kokku `2170 €`.

**7. Arve kogusumma on 2480 € (sisaldab 24% KM). Leia maksustatav väärtus ja KM.**

**Lahendus:** `2480 / 1,24 = 2000 €`; KM `480 €`.

**8. Perioodi eelarve on 80 000 €, perioodi täitmine 86 000 €. Arvuta täitmine ja hälve.**

**Lahendus:** täitmine `107,5%`; hälve `+6000 €` ehk `+7,5%`.

**9. Aasta eelarve on 120 000 €, 9 kuu täitmine 90 000 €. Kas võime järeldada, et aasta lõpuks on eelarve täpselt täidetud?**

**Lahendus:** ei. Lineaarne ekstrapolatsioon annaks `90 000 / 9 × 12 = 120 000 €`, kuid hooajalisus, lepingud ja eelarvemuudatused võivad tulemust muuta.

**10. Arve neto 1000 €, KM 240 €, kogusumma 1250 €. Kui suur on erinevus?**

**Lahendus:** oodatud 1240 €, tegelik 1250 €; erinevus 10 €. Tulemus on kontrolli hoiatus, mitte automaatne dokumenti parandav otsus.

## Osa C – finantsarvestuse otsused

**11. IT-teenus osutati 29.10, arve esitati 04.11, maksti 02.12. Mis kuu kulu see üldjuhul on?**

**Lahendus:** oktoober, kui teenus on sisuliselt selle kuu kulu ja muud tingimused seda ei muuda. Arve ja makse võivad olla hilisemad.

**12. Teenuse arve on 1240 € ning harjutuses eeldatakse, et kogu summa kuulub kulusse. Too kaks lihtsustatud kannet: arve ja tasumine.**

**Lahendus:** arve: deebet teenusekulu 1240 €, kreedit võlg tarnijale 1240 €. Makse: deebet võlg tarnijale 1240 €, kreedit raha 1240 €. Tegelik riigiarvestus võib nõuda täpsemaid kontosid, ajastust ja KM-eristusi.

**13. Arvel puudub kulukeskus. Kas summa sobivusest piisab kinnitamiseks?**

**Lahendus:** ei. Tuleb koguda puuduva liigituse ja pädeva kinnituse info vastavalt toimemudelile.

**14. Kahel arvel on sama tarnija ja sama arvenumber, kuid erinev summa. Mida teed?**

**Lahendus:** märgin võimaliku dubleeringu ja kontrollin algdokumente, parandusarvet, teenust ja menetluse ajalugu; automaatselt ei kustuta ega kinnita.

**15. Arve on 1240 €, aga eelarve täitmise aruandes suureneb näitaja 1000 €. Kas see on kindlasti viga?**

**Lahendus:** mitte tingimata. Võivad olla erinevad alused: käibemaksu käsitlus, eelarveklassifikaator, periood, kapitaliseerimine. Tuleb uurida aruande metoodikat ja kontosid.

## Osa D – Python / SQL

**16. Käivita `kood/arvete_kontroll.py`. Millised vealiigid leitakse?**

**Oodatav lahendus:** kontrolliraport sisaldab vähemalt summa mittevastavust, KM aritmeetika mittevastavust, võimalikku duplikaati, puuduva kulukeskuse ja vigase kuupäeva juhtumit.

**17. Lisa CSV-sse kaks sama tarnija ja arvenumbriga rida. Mis muutub?**

**Oodatav lahendus:** mõlemad read saavad duplikaadihoiatuse; kontroll ei tähenda, et mõlemad tuleb kustutada.

**18. Koosta SQL-päring, mis näitab kulukeskuse kaupa arvete arvu.**

```sql
SELECT kulukeskus, COUNT(*) AS arvete_arv
FROM arved
GROUP BY kulukeskus;
```

**19. Kuidas vältida Excelis käsitsi valemite kopeerimist?**

**Lahendus:** kirjuta arvutused Pythonis ühe funktsioonina, testi ja ekspordi tulemused `openpyxl` abil; samu reegleid kasutatakse iga uue andmestiku korral.

**20. Millised andmed on eelarve koondist puuduvad, kui tahame kontrollida üksikut ostuarvet?**

**Lahendus:** tehingu detailid, algdokument, tarnija, leping, kinnitused, raamatupidamiskanne, auditijälg. Avalik koondandmestik neid üldjuhul ei sisalda.

## Osa E – 90 sekundi lühietteaste

Selgita suuliselt järgmist:

> „Kuidas lahendaksin olukorra, kus asutuse IT-kulud on planeeritust suuremad?“

**Hea vastuse struktuur:** (1) kontrollin perioodi ja andmete võrreldavust; (2) teen kululiikide koondi; (3) uurin suurimad kõrvalekalded; (4) võrdlen lepingu ja teenuse ajastusega; (5) dokumenteerin põhjuslikud hüpoteesid, piirangud ja soovitatavad järgmised kontrollid.
