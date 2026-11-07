# Õppemoodul 2: ostuarvest kontrollitud kirjendini

**25 minutit.** Eesmärk: oskad vea korral otsustada, kellelt infot küsida, kuidas dokument liigub ja kuidas tekib kirjend. Läbiv fiktiivne arve on DEMO-001: septembri IT-teenus 1000 € + 240 € käibemaks, arve 2. oktoobril, tähtaeg 16. oktoobril. Kontrollpäev on 5. november 2026.

## 1. Kontroll ei ole kinnitus · 4 minutit

**A. Lihtsalt.** Programm saab kontrollida summade kokkulangemist. Teenuse tegelikku osutamist peab kinnitama selle eest vastutav inimene.

**B. Miks finantseksperdile vaja?** Väldid olukorda, kus matemaatiliselt õige arve muutub põhjendamatu makse aluseks.

**C. Töös.** Analüütik kontrollib dokumenti ja küsib puuduva info. Sisukinnitaja kontrollib teenuse saamist. Eelarve eest vastutaja kinnitab kuluallika oma pädevuse piires. Täpne tegelik tööjaotus tuleb asutuse toimemudelist; meie rollid on simulatsioon.

**D. Näide.** Neto 1000, KM 240 ja bruto 1240 eurot on aritmeetiliselt kooskõlas. Kui vastuvõtuakt puudub, ei tõenda see veel, et teenus saadi.

**E. Python.** Käivita projekti `kood` kaustas:

```python
from menetlus import read_csv, issues_for, ROOT
arve = read_csv(ROOT / 'andmed/sunteetilised/naidisarved.csv')[0]
leiud = issues_for(arve, '2026-11-05')
print([(x['code'], x['severity']) for x in leiud])
# ULETAHTAJA ja PERIOOD on hoiatused. See ei ole kinnitus teenuse saamise kohta.
```

**F. Ülesanne.** Kas ilma summaveata arve võib automaatselt saada KINNITATUD oleku?

**G. Lahendus.** Ei. Demo kasutab ette kirjutatud õppeotsuseid, kuid põhifunktsioonid nõuavad eraldi ESITA, KOOSKOLASTA ja KINNITA toiminguid.

**H. Tüüpviga.** „Kõik automaatkontrollid läbisid, seega võib maksta.“ Kontrollid ei tõenda lepingu täitmist ega kinnitaja pädevust.

**I. Töövestlus.** Mida automatiseeriksid? Korduvad matemaatilised, struktuuri- ja dimensioonikontrollid; teenuse vastuvõttu ja erandotsust ei usaldaks pelgalt summakontrollile.

## 2. Viga, hoiatus ja duplikaadikahtlus · 5 minutit

**A. Lihtsalt.** Viga peatab edasiliikumise. Hoiatus nõuab tähelepanu ja põhjendust, sest see võib olla korrektne erijuht.

**B. Miks vaja?** Finantsekspert peab oskama tehnilise leiu sisuliseks tegevuseks tõlkida.

**C. Töös.** SUMMA tähendab matemaatilist vastuolu. PERIOOD võib olla tavaline olukord, kus teenus osutati septembris ja arve tuli oktoobris. ULETAHTAJA ei tõenda tasumata võlga, kui makseandmeid ei ole.

**D. Näide.** 1000 + 240 = 1240, mitte 1240,01. Ühe sendi erinevus on selles ühe reaga näites blokeeriv viga. Kahe tarnijakirje DEMO-T002/N-002 kordumine annab mõlemale dokumendile DUPLIKAAT leiu.

**E. Python.**

```python
from menetlus import issues_for
vigane = dict(arve, gross_cents='124001')
print([x['code'] for x in issues_for(vigane, '2026-11-05')])
# Muude hoiatuste kõrval peab olema SUMMA.
```

**F. Ülesanne.** `DEMO-T002 / N-002` ja ` demo-t002 / n-002 ` näevad erinevad välja. Kas neid tasub võrrelda?

**G. Lahendus.** Jah. Pärast tühikute ja tähesuuruse normaliseerimist on võti sama. Kahtlus tuleb uurida; see ei tõenda pettust. Kontroll ei kasuta ainsa võtmena arvenumbrit, sest eri tarnijatel võib olla sama number.

**H. Tüüpviga.** Sama arve faili uuesti importimise lugemine uueks arveks. Meil sama sisemine ID ja sisu uut rida ei tekita.

**I. Töövestlus.** Kuidas kontrollireeglit testiksid? Kasutaksin korrektset juhtu, ühe sendi viga, vigast andmetüüpi, duplikaadi variatsiooni ja olukorda, kus eri tarnijatel on sama arvenumber.

## 3. Parandus ja auditijälg · 5 minutit

**A. Lihtsalt.** Paranduse korral peab olema näha nii vana kui uus sisu ja muutmise põhjus.

**B. Miks vaja?** Hiljem peab saama selgitada, miks algne dokument ei sobinud ning mille alusel muutus tehti.

**C. Töös.** Meie näites saab SISEND või TAGASTATUD dokumendile luua uue ID-ga versiooni. Vana saab ASENDATUD oleku. Kinnitatud või kajastatud dokumenti ei parandata selle lihtsa mehhanismiga.

**D. Näide.** VIGA-003 bruto on 124001 senti. Parandus VIGA-003-R2 sisaldab algdokumendi järgi 124000 senti. Revision kasvab 1-lt 2-le ja vana JSON säilib.

**E. SQL.**

```sql
SELECT document_id, status, revision, supersedes_document_id
FROM input_document
ORDER BY document_id;
```

**F. Ülesanne.** Miks ei kirjuta me otse `UPDATE input_document SET raw_json=...`?

**G. Lahendus.** See kaotaks senise alginfo, tekitaks vastuolu kontrollsumma ja varasemate kinnitustega ning raskendaks põhjenduse jälgimist. Rakenduse parandusfunktsioon säilitab versioonide seose.

**H. Tüüpviga.** Trigeritega logi pidamine absoluutselt muutmiskindlaks. Lokaalse andmebaasi omanik saab skeemi muuta; see pole tootmiskeskkonna turvalahendus.

**I. Töövestlus.** Mida auditijälg sisaldaks? Dokument, versioon, tegija, aeg, toiming, vana/uus olek ja sisuline põhjus. Käesolevas etapis on need väljad olemas.

## 4. Simuleeritud RTK-vahetus ja kordused · 4 minutit

**A. Lihtsalt.** Edastatud dokument ja vastuvõetud dokument pole sama olek. Vastuvõtja peab teadma, millise konkreetse paketi ta sai.

**B. Miks vaja?** Võrgu- või kasutajavea tõttu võib sama päring korduda. Kordus ei tohi tekitada topeltkannet.

**C. Töös.** Meie programm loob kohaliku JSON-paketi ja salvestab selle räsi. Vastuvõtu simulatsioon kontrollib räsi ning salvestab viite SIM-SAP-DEMO-001. See ei ole SAP-i tegelik dokumendinumber.

**D. Näide.** Sama paketti võetakse vastu kaks korda: üks journal_entry, sama viide mõlemal vastusel. Kui paketis muutub bruto 124000 → 124001 senti, vastuvõtt blokeeritakse.

**E. SQL.**

```sql
SELECT invoice_id, COUNT(*) AS kannete_arv
FROM journal_entry
GROUP BY invoice_id;
```

**F. Ülesanne.** Kui JSON-faili kirjutamine ebaõnnestub, kuid eksport on andmebaasis olemas, kas peab uuesti arve looma?

**G. Lahendus.** Ei. Korduseksport annab sama salvestatud paketi. Uus arve või kanne oleks vale korduskäitumine.

**H. Tüüpviga.** Kohaliku SHA-256 kontrolli nimetamine e-allkirjaks. See tõendab siin paketi vastavust salvestatud koopiale, mitte saatja juriidilist identiteeti.

**I. Töövestlus.** Milliseid liidese teste kirjutaksid? Kordusvastuvõtt, muudetud sisu, tundmatu viide, vale olek ja katkestus poole kirjendi peal.

## 5. Arvestuskanne ja tehingu terviklikkus · 5 minutit

**A. Lihtsalt.** Kirjend peab olema tasakaalus ning salvestuma tervikuna.

**B. Miks vaja?** Poolik kanne rikub arvestuse; tasakaalus kanne vales perioodis võib samuti anda vale aruande.

**C. Töös.** Selles õppenäites ei arvata sisendkäibemaksu maha. Teenuse kuupäev 30.09.2026 läheb kande kuupäevaks. Päris süsteemis tuleb kontrollida ka perioodi avatust ning kontoplaani.

**D. Näide.**

| Näidiskonto | Deebet | Kreedit |
|---|---:|---:|
| DEMO_KULU | 1000 € | 0 € |
| DEMO_KM_KULU | 240 € | 0 € |
| DEMO_TARNIJA | 0 € | 1240 € |
| Kokku | 1240 € | 1240 € |

Need on fiktiivsed kontotähised. Arve tasumine oleks hilisem eraldi kanne D tarnijavõlg / K pank. Käesolev etapp makset ei tee.

**E. SQL.**

```sql
SELECT entry_id,
       SUM(debit_cents) AS deebet,
       SUM(credit_cents) AS kreedit,
       SUM(debit_cents-credit_cents) AS vahe
FROM journal_line
GROUP BY entry_id;
```

**F. Ülesanne.** Kui kolmanda kanderea salvestamine nurjub, mitu rida võib jääda alles?

**G. Lahendus.** Selle tehingu puhul null. SQLite'i rollback eemaldab nii päise kui juba lisatud read. Dokument jääb EDASTATUD-olekusse ja vastuvõttu võib pärast vea lahendamist uuesti proovida.

**H. Tüüpviga.** D = K pidamine piisavaks sisuliseks kontrolliks. Õige konto, periood, teenuse tegelikkus ja pädev kinnitus on samuti vajalikud.

**I. Töövestlus.** Kuidas kasutad oma testimiskogemust? Tekitan teadlikult vea kanderidade salvestamisel ja kontrollin, et ei jääks poolikut kannet, valet olekut ega teist kannet korduskatsel.

## 2-minutiline enesekontroll

1. **Kas kontrolli käivitamine kinnitab arve?** Ei.
2. **Kas puuduv ID kaotab sisendrea?** Ei; jääb tehnilise ID-ga toorkirje ja viga.
3. **Miks tarnija nimi pole hea duplikaadivõti?** Nimi võib muutuda või olla eri kirjapildiga; näites kasutatakse tarnija ID-d.
4. **Kas üle tähtaja arve on kindlasti tasumata?** Ei, makseinfo puudub.
5. **Miks üks arve jääb pärast tagastamist alles?** Vaja on säilitada ajalugu.
6. **Mis vahe on dokumentide ID-l ja tarnija arvenumbril?** Esimene määrab kohaliku kirje/versiooni, teine tarnija äridokumendi numbri.
7. **Mis on idempotentne vastuvõtt?** Sama paketi kordamine ei lisa teist kannet.
8. **Kas näidisrollid on kasutajate autentimine?** Ei.
9. **Kas demo eelarvejuhi kinnitus arvutab päris eelarvejäägi?** Ei; see on simuleeritud inimese otsus.
10. **Mis on järgmise etapi töö?** Võrreldavate pärisandmete kulude analüüs ja aruandlus, alles uue korralduse järel.

Lisaharjutus: käivita demo, ava DBeaveris andmebaas, leia DEMO-001 ajalugu ja kanna kuupäev ning selgita 60 sekundiga, miks novembris tehtud simulatsiooni kanne puudutab septembri teenust.

Allikate raamistik on [ANDMEALLIKAD.md](ANDMEALLIKAD.md) ja [RTK avalik teenusekirjeldus](https://www.rtk.ee/finantsarvestus-personaliteenus/arvestusteenused/finantsarvestus). Menetluse konkreetsed olekud, DEMO-kontod ja JSON on selle õppeprojekti kavand, mitte asutuste ametlik konfiguratsioon.
