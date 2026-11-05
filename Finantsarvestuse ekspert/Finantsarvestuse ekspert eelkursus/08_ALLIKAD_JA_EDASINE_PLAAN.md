# 08. Ametlikud allikad, pärisandmed ja järg Workile

Kontrollimise kuupäev: **05.11.2026**. Viimaseid muudatusi vaata alati lähtesaidilt.

## Asutused ja tööprotsessid

1. **RTK – finantsarvestuse teenus**: https://www.rtk.ee/finantsarvestus-personaliteenus/arvestusteenused/finantsarvestus  
   Loe RTK tegevuste loend ja mõiste „toimemudel“. Küsi: millist infot peab ministeerium RTK-le andma?
2. **Rahandusministeerium – riigi raamatupidamine**: https://www.fin.ee/riigi-rahandus-ja-maksud/riigi-raamatupidamine  
   Loe, miks riigi raamatupidamine on tekkepõhine.
3. **RTK – tutvustus ja struktuur**: https://www.rtk.ee/asutus-uudised-kontakt/organisatsioonist/tutvustus-ja-struktuur  
   Tutvu SAP-i, e-arvete menetluskeskkonna ning RTIP-iga.

## Õigusaktid

4. **Raamatupidamise seadus (kehtiv tekst)**: https://www.riigiteataja.ee/et/akt/rps  
   Otsi algdokument, raamatupidamiskirjend, tekkepõhine arvestus, raamatupidamiskohustuslane.
5. **Avaliku sektori finantsarvestuse ja -aruandluse juhend**: https://www.riigiteataja.ee/akt/103012025007  
   Loe üldpõhimõtteid; jälgi ka võimalikke muudatusi.
6. **EMTA käibemaksumäärad**: https://www.emta.ee/ariklient/maksud-ja-tasumine/kaibemaks/kaibemaksumaarad-ja-maksuvaba-kaive/uldine-kaibemaksumaar  
   Standardmäär on alates 01.07.2025 24%; kõik tehingud ei pruugi sellesse kategooriasse kuuluda.

## Päris eelarveandmed

7. **Rahandusministeeriumi 2026. a riigieelarve leht**: https://www.fin.ee/riigi-rahandus-ja-maksud/riigieelarve-ja-eelarvestrateegia/2026-riigieelarve

   Lehel leiduvad XLSX-failid eelarve ja täitmise kohta. 05.11.2026 kontrollimisel oli näha *2026. aasta septembri majandusliku sisu järgi eelarve täitmise XLSX* ning eelarve seaduse XLSX.

### Andmestiku uurimise mall

| Küsimus | Mida kirja panna |
|---|---|
| Allika aadress | Konkreetne allalaadimisleht ja failinimi |
| Avaldamise/seisu aeg | Näiteks september 2026; avaldamise kuupäev eraldi |
| Arvestusmeetod | Mida tähendavad kulud ja täitmine? |
| Üksus | Euro, tuhat eurot, miljon eurot? |
| Tähendus | Kas read on asutused, valitsemisalad, kontod või tegevused? |
| Filtreeritavus | Kas saab välja võtta HTM-i valitsemisala? |
| Piirangud | Kas võimalik võrrelda eelneva aasta sama perioodiga? |

## Ettevalmistus Worki viieks etapiks

1. Kui oskad selgitada ostuarve ja eelarve põhimõisteid, on sul lihtsam **Worki 1. etapi** lähteandmeid ja spetsifikatsiooni hinnata.
2. Kui oled käivitanud CSV → Python → SQLite → XLSX näite, oskad hinnata **2. ja 3. etapi** koodi.
3. Kui mõistad, millised andmed on päris ja millised sünteetilised, saad hinnata **4. etapi** veebirakenduse usaldusväärsust.
4. **5. etapis** esitad vaid need oskused ja testitulemused, mida suudad ise põhjendada.

## Kontroll-loend enne Worki jätkamist

- [ ] Oskan seletada „kulu“, „kohustis“, „makse“, „eelarve“ ja „täitmine“.
- [ ] Oskan arvutada 24% KM-i ning eristada selle mahaarvamise küsimusest.
- [ ] Mõistan, miks arve saabumise kuupäev ei pruugi olla kulu periood.
- [ ] Oskan nimetada 5 ostuarve kontrolli.
- [ ] Oskan arvutada täitmise protsenti ja hälvet.
- [ ] Olen Pythonis genereerinud Exceli aruande.
- [ ] Olen SQLite'is käivitanud koondpäringu.
- [ ] Oskan oma projekti piiranguid ausalt tutvustada.
