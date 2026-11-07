# Finantsarvestuse eksperdi kiirkursus

Matemaatika-, majandus- ja IT-taustaga õppijale. Umbes 6 tundi: teemad 2 h, praktilised ülesanded 2 h, küsimused 1 h, tööpäev ja demo 1 h. Eesmärk on põhjendada kontrolli ja küsida õige küsimus, mitte asendada asutuses sisseelamist. Näited on sünteetilised.

Ametlikud alused ja erandid: [finantsreeglite kontroll](FINANTSREEGLITE_KONTROLL.md).

## 1. Põhimõisted

Kulu kirjeldab perioodi ressursikasutust, makse raha liikumist. Kohustis on olemasolev kohustus; eelarve on plaan/piir. Deebet ja kreedit on kande pooled, mitte lihtsalt pluss ja miinus.

**Arvuline näide:** Oktoobri teenus 1000 ja näites mittemahearvatav KM 240: D kulu 1000 + D KM-kulu 240 = K tarnijavõlg 1240. Novembri makse vähendab võlga ja raha, uut teenusekulu ei teki.

**Tööolukord:** Kolleeg küsib, miks maksmata arve on oktoobri aruandes. Näita teenuse tõendit ja selgita tekkepõhisust.

## 2. Ostuarvete menetlemine

Kontrolli partnerit, tehingu sisu, vastuvõttu, lepingut, perioodi, summasid, maksukäsitlust ja eelarvet. Kontroll ei asenda volitatud inimese kinnitust.

**Arvuline näide:** 1000+240 ei võrdu 1240,01: erinevus 0,01. Ära paranda originaali vaikimisi, säilita parandusajalugu.

**Tööolukord:** Kordussaatmisel võrdle partnerit ja arvenumbrit ning eelmist olekut, mitte ainult faili nime.

## 3. RTK ja asutuse tööjaotus

Lähtu kliendi toimemudelist ja oma ametijuhendist. Avalik teenusekirjeldus ei ole HTM täpne kinnitusring.

**Arvuline näide:** 1240-eurosel arvel võib olla 0 arvutusviga, kuid puuduv teenuse vastuvõtt. Õppenäites jääb arve selgitust ootama.

**Tööolukord:** RTK-le küsimust koostades lisa dokumenditunnus, periood, summa ja konkreetne lahtine küsimus. Ära saada oletust kinnitatud faktina.

## 4. Eelarveanalüüs

Enne jagamist kontrolli perioodi, ulatust, mõõdikut, ühikut ja eelarveversiooni. Aasta kasutamine erineb perioodihälbest.

**Arvuline näide:** Aastaeelarve 10000, 8 kuu kulu 6000: 60% ja jääk 4000. Kui 8 kuu plaan oli 5500, on hälve +500 ehk +9,09%.

**Tööolukord:** 64% augustis pole iseenesest hea ega halb: vaja hooajalisust, perioodiplaani ja kohustusi.

## 5. Aruandlus ja klassifitseerimine

Bilanss kirjeldab seisu kuupäeval, tulemiaruanne perioodi tulusid-kulusid ja rahavoog raha liikumist. Konto on majanduslik liik, kulukeskus vastutuskoht.

**Arvuline näide:** Kokku 100 = tööjõud 60 + muu 40. Nende kõigi liitmine annab vale 200. Välisvahendite osa 30 ei ole lisakulu.

**Tööolukord:** Exceli ja SAP-i erinevuse puhul kontrolli enne kande otsimist filtreid, taset, perioodi ja maksukäsitlust. Investeering pole automaatselt tegevuskulu.

## 6. Andmekvaliteet

Kontrolli kuju, aritmeetikat, seoseid ja tähendust eraldi. Puuduv pole null; räsi pole tõend algallika sisulisest tõesusest.

**Arvuline näide:** Kuud 100, 120 ja puuduv ei anna kinnitatud kvartalikulu 220. Kui kolmas on teadaolev 0, on 220 õige.

**Tööolukord:** Uue faili puhul vaata allikakuupäeva, räsi, ridade arvu ja ühikut; säilita vana versioon.

## 7. Finantsarvutused

Raha hoitakse täisarvuna sentides; protsendi ümardus defineeritakse eraldi. Mitme rea ümardus ei pruugi võrduda koondneto ümardusega.

**Arvuline näide:** 50 senti ×13%=6,5 senti →7. Toetus: 10000×80%=8000, lagi 7000, ettemakse 6000 → juurde 1000.

**Tööolukord:** Ettemakse ei tõenda abikõlblikku kulu. Toetusotsus vajab tingimusi, mitte ainult korrutamist.

## 8. Python ja SQL

Python kordab kontrolli; SQL hoiab seoseid ja teeb päringuid. Inimene määrab, milliseid ridu on õige summeerida.

**Arvuline näide:** 10000+2400 senti=12400 senti=124 eurot. Asutuste actual_cents summa analüüsibaasis on 77260000700.

**Tööolukord:** Igakuine sama raport sobib automatiseerimiseks. Salvesta filter ja oodatud kontrollsumma; ära kopeeri pimesi valemeid.

## 9. Automatiseerimine ja Excel

Automatiseeri korduv üheselt sõnastatud töö. Excel jääb kolleegile kasutatavaks üleandmisvormiks. Eksport ei tõenda ise õigsust.

**Arvuline näide:** 200 dokumendil 30 sekundit vähem tööd =100 min brutovõitu, millest lahuta hooldus ja erandite uurimine. See on oletus, mitte mõõdetud saavutus.

**Tööolukord:** Ava ekspordifail ja kontrolli rea arvu ning summat. actual_cents 42991100 tähendab 429911 eurot.

## 10. AI tulevik

ML võib järjestada anomaaliaid, LLM selgitada kontrollitud arve, RAG leida juhendiviiteid. Maksu- ja makseotsus jääb inimesele.

**Arvuline näide:** 100 hoiatusest 20 olulist tähendab leidude täpsust 20%. Tark mudel võib tekitada liiga palju lisatööd.

**Tööolukord:** Kui tekst väidab 15% kasvu, kuid Python annab 8,50%, kontrolli allikat ja paranda teksti. Ära lase mudelil puuduvaid põhjuseid välja mõelda.

## Käivitatavad näited

```python
from decimal import Decimal, ROUND_HALF_UP
vat = int((Decimal(50)*Decimal('0.13')).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
assert vat == 7
```

```python
import sqlite 3
c = sqlite 3.connect('dist/aruanded/analuus.sqlite')
assert c.execute("SELECT SUM(actual_cents) FROM budget_analysis WHERE level='asutus'").fetchone()[0] == 77260000700
c.close()
```

Detailsemad materjalid: [alused](FINANTSARVESTUSE_OPPEMATERJAL.md), [arvemenetlus](OPPEMOODUL_02.md), [analüüs](OPPEMOODUL_03.md), [veeb](OPPEMOODUL_04.md), [Pydantic/Polars](PYDANTIC_POLARS.md), [tööpäev](FINANTSARVESTUSE_EKSPERDI_TOOPAEV.md).

## 30 küsimust vastustega

1. **Kas kulu tekib maksmisel?** Mitte tingimata. Teenuse periood võib olla varasem; hilisem makse vähendab juba tekkinud võlga.

2. **Mis on ettemakse?** Raha antakse enne hüve saamist; kulu ja periood vajavad eraldi hinnangut.

3. **Kas D=K tõendab õigsust?** Ainult tasakaalu. Vale konto või periood võib olla samuti tasakaalus.

4. **Kas arve tõendab tarnet?** Tarne tegelikkust võib olla vaja eraldi vastuvõtu või lepinguga tõendada.

5. **Miks kontrollida partnerit?** Sama arvenumber võib eri tarnijatel olla õiguspärane; vale partner seob kohustise valesti.

6. **Kas duplikaat tähendab pettust?** Ei. Võimalik on kordussaatmine või parandatud versioon; uuri sisu ja ajalugu.

7. **Miks säilitada parandusajalugu?** Et oleks tuvastatav, mida, millal ja miks muudeti; originaali vaikne asendamine peidab jälje.

8. **Kas tähtaja ületamine tõendab võlga?** Makseinfo puudumisel mitte. Demos on ainult hoiatus.

9. **Kas 24% sobib igale arvele?** Ei. Liik, käibe aeg ja erandid määravad käsitluse; aritmeetika ei otsusta maksualust.

10. **Kas 0% ja maksuvaba on sama?** Ei. Õiguslik alus ja mahaarvamisõiguse tagajärjed võivad erineda.

11. **Kas bruto on alati kulu?** Ei. Vara, ettemakse või mahaarvatav KM võivad nõuda muud jaotust.

12. **Mida tähendab 64%?** Valitud täitmise suhe valitud eelarvesse; nimeta periood ja mõõdik.

13. **Kas jääk on sääst?** Mitte automaatselt: ees võib olla kohustusi ja perioodiplaan puududa.

14. **Mida teha null-eelarvega?** Näita eurodes vahet ja jäta protsent määramata, mitte 0%.

15. **Miks nimetada eelarveversioon?** Algne ja muudetud eelarve võivad anda eri tulemuse; võrdlus peab olema taasesitatav.

16. **Miks ei võrrelda 8 ja 9 kuud otse?** Perioodi erinevus ise tekitab muutuse; siin erineb lisaks mõõdik.

17. **Konto või kulukeskus?** Konto ütleb majandusliku liigi, kulukeskus vastutuskoha.

18. **Miks mitte liita koondit detailidega?** Koond juba sisaldab detaile; muidu loendatakse sama kulu kaks korda.

19. **Miks tühi pole 0?** Teadmata väärtuse nulliks muutmine võib alahinnata tulemust.

20. **Mida näitab räsi?** Faili baitide muutumist, mitte majandustehingu õigsust.

21. **Mida teeb Pydantic?** Kontrollib andmelepingut ja väljade tüüpe; ei tõenda tarnet ega maksukäsitlust.

22. **Miks sendid?** Täisarv vähendab ujukomavigu, kuid ümardusreegel on endiselt vajalik.

23. **Millal Polars?** Kui mõõdetud töökoormus ja hooldusvõime õigustavad seda; väike tabel ei nõua pandas’e asendamist.

24. **Milleks SQL-tehing?** Seotud muudatused kas jõustuvad või tühistatakse koos; poolik partii ei jää registrisse.

25. **Kas brauseri SQLite on server?** Ei. Praeguses demos on see ajutises mälus ja kaob värskendamisel.

26. **Kas Pages käitab serveri Pythonit?** Ei. Python töötab siin brauseris või enne avaldamist ehitamisel.

27. **Kas Exceli eksport on iseenesest ohutu?** Kasutajatekst võib muutuda valemiks. Eksport neutraliseerib valemimärgid; kontrolli ka ühikuid.

28. **Millal küsida RTK-lt?** Kui juhend või pädevus ei kata erandit; lisa faktid ja täpne küsimus.

29. **Mida lisab RAG?** Võimaluse toetuda konkreetsele juhendile ja redaktsioonile, kuid allikat tuleb siiski kontrollida.

30. **Mida projekt tõendab?** Praktilist analüüsi, testimist ja õppimist; mitte SAP-i töökogemust ega kutsepädevust.

## 10 ülesannet lahendustega

### Ü 1. Kulu ja makse

Teenus 800+KM 192,31.10; arve 02.11, makse 20.11.

**Lahendus:** Näite kulu 800+192 ja kohustis 992 teenuse perioodis; makse novembris vähendab võlga. PERIOOD hoiatus vajab selgitust.

### Ü 2. Üks sent

Impordi data/impordi_proov.csv: neto 100000, KM 24000, bruto 124001 senti.

**Lahendus:** SUMMA viga. Aritmeetiline bruto 124000; säilita algne sisend ja selgita parandus algallikaga.

### Ü 3. Duplikaat

ABC/INV  7 ja ABC/ inv 7 ; kolmas DEF/INV 7.

**Lahendus:** Esimesed kaks normaliseeruvad samaks partneri-numbripaariks; kolmas mitte. Kõik jäävad uuritavateks dokumentideks.

### Ü 4. Ümardus

50 senti ×13%; kas 6 või 7 senti?

**Lahendus:** 6,5 ümardub HALF_UP järgi 7-ks, bruto 57. Kuue sendiga KM_SUMMA.

### Ü 5. Eelarvehälve

Aasta 120000,8 kuu plaan 75000, kulu 78000.

**Lahendus:** Aasta kasutamine 65%, jääk 42000; perioodihälve+3000 ehk+4%. Mõisted on erinevad.

### Ü 6. Topeltarvestus

Kokku 150, personal 90, haldus 60, välisvahendid 40.

**Lahendus:** Õige kulu 150.90+60 selgitab koondit,40 on rahastusristlõige.

### Ü 7. Toetuse lagi

Kulu 11000, abikõlblik 10000,80%, lagi 7000, ettemakse 6000.

**Lahendus:** Teenitud 7000, juurde 1000, tagasi 0. Ülejäänud 1000 kulu pole näites abikõlblik.

### Ü 8. SQL ristkontroll

Summeeri budget_analysis actual_cents ainult level=asutus.

**Lahendus:** 77260000700 senti. Koondrea lisamine samasse SUM-i annaks kahekordse tulemuse.

### Ü 9. Eksport ja vigane Excel

Vali Keeleamet, ekspordi; proovi valemiga XLSX-i.

**Lahendus:** Üks asutuserida, actual_cents 42991100, budget_cents 67988700. Valemiga import lükatakse tagasi; varasem seanss säilib.

### Ü 10. AI väide

LLM:8,50% kasv tuli ainult palgatõusust ja kõik tähtajahoiatusega arved on tasumata.

**Lahendus:** Koond ei tõenda põhjust; makseinfo puudub. Esita arvutatud kasv faktina, põhjused ja makseolek uurimisküsimusena.

Hinda iga ülesannet 0–2: vale 0, õige arv ilma põhjenduseta 1, õige arv koos piiranguga 2. Siht 16/20. Kulu/makse, perioodihälbe, koondtaseme ja AI väite eksimused lahenda enne demonstratsiooni.
