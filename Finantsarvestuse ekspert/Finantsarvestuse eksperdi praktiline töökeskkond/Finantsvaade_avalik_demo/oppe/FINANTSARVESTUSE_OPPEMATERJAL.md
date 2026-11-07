# Esimene õppemoodul: mida finantsandmed tegelikult tähendavad?

**Kestus: 25 minutit.** Eesmärk: oskad eristada kulu, makset ja eelarvet; seletada lihtsat kannet ning jälitada Pythoni tulemust algallikani. Matemaatikat ja programmeerimist sa juba tunned — keskendume arvestuse tähendusele.

Läbiv fiktiivne juhtum: asutus **Haridusamet X** tellib septembris IT-hooldust. Teenus osutatakse 30. septembril, arve saabub 2. oktoobril ning makstakse 16. oktoobril. Arvel on 1000 eurot + 24% käibemaks. Nimed ja tehing on välja mõeldud. Näidismäär vastab 2026. aasta standardmäärale; tehingu maksukäsitlus vajab päriselus eraldi hindamist. [EMTA 2026 maksumuudatused](https://www.emta.ee/uudised/maksumuudatused-2026).

## 1. Tekkepõhisus ja kassapõhisus · 4 minutit

**A. Lihtsalt.** Tekkepõhisus küsib, millal teenust kasutati ja kohustis tekkis. Kassapõhisus küsib, millal raha liikus.

**B. Miks vaja?** Muidu võib septembri kulu ekslikult oktoobrisse sattuda ja kuuaruanne muutuda maksetähtajast sõltuvaks.

**C. Töös.** Finantsekspert kontrollib teenuse perioodi, lepingut ja vastuvõtu kinnitust. Kui arve pole perioodi sulgemisel saabunud, hinnatakse vajadust kajastada viitvõlg. Täpne sulgemiskord tuleb asutuse sise-eeskirjast.

**D. Näide.** Eeldame, et sisendkäibemaksu mahaarvamise õigust ei ole. Teenuse ja sellega seotud käibemaksu kogukulu on 1240 eurot septembris; väljamakse 1240 eurot oktoobris. Käibemaksukulu võib avaliku sektori kontoplaani järgi olla eraldi kulureal.

**E. Python.**

```python
from datetime import date
teenuse_kuu = date(2026, 9, 30).strftime('%Y-%m')
makse_kuu = date(2026, 10, 16).strftime('%Y-%m')
print(teenuse_kuu, makse_kuu)  # 2026-09 2026-10
```

**F. Ülesanne.** Detsembri koristusteenus 620 eurot makstakse jaanuaris. Millises kuus on kulu ja millises makse?

**G. Lahendus.** Kulu detsembris, makse jaanuaris. Aastavahetusel on tasumata arve kohustis, kui see on nõuetekohaselt kajastatud.

**H. Tüüpviga.** „Arve saabumise või maksmise kuu määrab alati kulukuu.“ Ei määra.

**I. Töövestlus.** Kuidas leiad kuu lõpus puuduva arvega teenused? Küsin vastuvõetud teenuste infot, võrdlen lepingute ja perioodiga ning kooskõlastan arvestuskäsitluse RTK-ga.

## 2. Deebet, kreedit ja kohustis · 5 minutit

**A. Lihtsalt.** Igal kandel on vähemalt kaks poolt ja deebetite summa peab võrduma kreeditite summaga. Deebet ei tähenda alati suurenemist ega kreedit alati vähenemist: see sõltub kontoliigist.

**B. Miks vaja?** Kontrollid, kas arve, kulu ja hilisem makse on omavahel kooskõlas, ning oskad RTK-ga rääkida sama keelt.

**C. Töös.** Kulu ja vara suurenemine on üldjuhul deebetis; tulu ja kohustise suurenemine kreeditis. Tegelik kontonumber valitakse kehtiva kontoplaani ning tehingu sisu järgi. Siinsed kontonimed on õppenäited.

**D. Näide.** Meie eeldusel, et 240 eurot pole mahaarvatav:

| Sündmus | Deebet | Kreedit |
|---|---|---|
| Teenuse arve kajastamine | Teenusekulu 1000; käibemaksukulu 240 | Võlg tarnijale 1240 |
| Arve tasumine | Võlg tarnijale 1240 | Raha pangas 1240 |

Tasumine ei tekita teist 1240-eurost kulu. Kui sisendkäibemaks oleks õiguspäraselt mahaarvatav, oleks 240 eurot vastavas arvestuses nõue, mitte sama kulukäsitlus.

**E. Python.**

```python
deebet_sendid = [100000, 24000]
kreedit_sendid = [124000]
assert sum(deebet_sendid) == sum(kreedit_sendid)
```

**F. Ülesanne.** Kajastatud võlg on 1240 eurot ja makstakse 500 eurot. Kui suur on järelejäänud kohustis?

**G. Lahendus.** 740 eurot. Makse kanne: D võlg 500, K pank 500. Algne kulu ei muutu.

**H. Tüüpviga.** Tasakaalus kanne võib siiski olla vale konto, perioodi või asutuse all. Tasakaal on vajalik, kuid ebapiisav kontroll.

**I. Töövestlus.** Miks ei piisa kontrollist D = K? Sest see ei tõenda tehingu tegelikkust, õiguspärasust ega õiget liigitust.

## 3. Käibemaks ja täpne raha · 4 minutit

**A. Lihtsalt.** Arve neto + käibemaks = bruto. Maksumäär ja mahaarvamisõigus on eri küsimused.

**B. Miks vaja?** Õige matemaatika ei tõenda automaatselt õiget maksukäsitlust.

**C. Töös.** Kontrollid teenuse liiki, käibe tekkimise aega, tarnija arvet ning asutuse tegevusega seost. Standardmäär ei kehti kõigile tehingutele. Sünteetilised näited ei ole maksunõuanne konkreetsele asutusele.

**D. Näide.** 125,55 × 24% = 30,132 → ümardatult 30,13 eurot; kokku 155,68 eurot. Näidis kasutab ühe arverea ümardamist lähima sendini, täpselt poole korral üles. Mitmerealise arve kogusumma kontroll peab hiljem arvestama arve ümardusmeetodit.

**E. Python.**

```python
from decimal import Decimal, ROUND_HALF_UP
neto = Decimal('125.55')
km = (neto * Decimal('0.24')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
print(km, neto + km)  # 30.13 155.68
```

**F. Ülesanne.** Leia näidisarve 499,99 + 24% käibemaks ja bruto.

**G. Lahendus.** Käibemaks 120,00 ja bruto 619,99 eurot. Vahetulemus 119,9976 ümardatakse 120,00-ni.

**H. Tüüpviga.** `round(499.99 * 0.24, 2)` kasutamine universaalse arvestusreeglina. Binaarne float ja vaikimisi ümardamine võivad erineda kokkulepitud rahareeglist.

**I. Töövestlus.** Kuidas kontrolliksid arve summat? Rakendaksin dokumenteeritud ümardusreeglit Decimal-tüübiga ja eristaksin aritmeetilise vea maksukäsitluse küsimusest.

## 4. Eelarve, kulukeskus ja võrdlus · 5 minutit

**A. Lihtsalt.** Eelarve on plaan või lubatud maht. Kulu näitab toimunud majanduslikku tarbimist. Kulukeskus aitab määrata vastutaja, konto tehingu sisu ning rahastusallikas raha päritolu.

**B. Miks vaja?** Sama arve võib olla matemaatiliselt õige, kuid vale kulukeskuse või toetuse all.

**C. Töös.** Võrdlus eeldab sama perioodi, ulatust, arvestusalust ja eelarveversiooni. Toetuse kasutamist piiravad lisaks eelarvele lepingu tingimused ja abikõlblikkuse periood. Pelgalt raha laekumine ei tõenda tulu teenimist ega kulude abikõlblikkust.

**D. Näide.** Ainult fiktiivses võrreldavas juhtumis: üheksa kuu eelarve 10 000 eurot ja sama ulatuse kulu 8500 eurot. Täitmine 85%, jääk 1500 eurot. See ei ole meie pärisandmete tulemus.

**E. Python.**

```python
from decimal import Decimal
eelarve, kulu = Decimal('10000'), Decimal('8500')
taitmine = None if eelarve == 0 else kulu / eelarve * 100
print(taitmine, eelarve - kulu)  # 85.00 1500
```

**F. Ülesanne.** Kas septembrini kogunenud kulud ja investeeringud võib jagada algse aasta kulueelarvega ning nimetada tulemuse automaatselt eelarve täitmiseks?

**G. Lahendus.** Ei. Investeeringud, amortisatsioon, muudatused ja perioodiulatus vajavad ühtlustamist. Meie failis on üks näitaja algne kulueelarve, teine kulud ja investeeringud ilma amortisatsioonita. Programm seetõttu protsenti ei arvuta.

**H. Tüüpviga.** Riigieelarve algseaduse HTM-i valitsemisala ja ministeeriumi enda rida on erinevad. Samuti ei ole 75% aasta möödumine tõend, et kõik kulud peavad olema täpselt 75% eelarvest.

**I. Töövestlus.** Mida teeksid suure hälbe korral? Kontrolliksin andmete võrreldavust, ajastust, hooajalisust, lepinguid ja eelarve muudatusi enne põhjuste järeldamist.

## 5. Päritolu, auditijälg ja kontroll · 4 minutit

**A. Lihtsalt.** Auditijälg võimaldab liikuda tulemusest tagasi dokumendi ja tehtud muudatusteni. Saldoandmik on kontode ja nõutud dimensioonide järgi koondatud arvestusandmestik, mitte ostuarvete nimekiri.

**B. Miks vaja?** Teine inimene peab saama sinu arvutuse ja allika üle kontrollida.

**C. Töös.** Säilitatakse allikas, versioon, periood, sisestaja/muutja, muudatuse aeg ja põhjendus. Selles etapis on failide päritolu ning lahtriviited; kasutajate menetluslogi tuleb hiljem.

**D. Näide.** `TAIT2026-N137` viitab säilitatud Exceli N137-le. Seal on 886 184 288,61 eurot. CSV `amount_cents` väärtus on 88 618 428 861 senti. Üheksa kuu summa kattub selle näitajaga.

**E. Python.**

```python
import csv
from pathlib import Path
# Käivita projekti juurkaustas.
p = Path('andmed/toodeldud/htm_taitmine_2026.csv')
with p.open(encoding='utf-8-sig', newline='') as f:
    read = list(csv.DictReader(f, delimiter=';'))
rida = next(r for r in read if r['record_id'] == 'TAIT2026-N137')
assert int(rida['amount_cents']) == 88618428861
print(rida['sheet'], rida['cell'])
```

**F. Ülesanne.** Miks ei liideta täitmise CSV kõiki 99 rida?

**G. Lahendus.** Samas failis on kuud ja nende YTD-koond, 2025 võrdlusperiood, koond- ja alamread ning kattuv välistoetuste ristlõige. Liitmine tekitaks mitmekordse arvestuse.

**H. Tüüpviga.** Allika „–“ asendamine nulliga ilma selgituseta; tulevase kuu nulli pidamine kinnitatud nullkuluks.

**I. Töövestlus.** Kuidas tõendad, et lähtefail pole muutunud? SHA-256 kontrollsummaga. See tõendab failide samasust, mitte majandustehingute sisulist õigsust.

## Enesekontroll · 3 minutit

1. **Kas makse tekitab alati kulu?** Ei, näiteks tarnijavõla tasumine vähendab kohustist ja raha.
2. **Kas kulu võib tekkida enne makset?** Jah, näiteks tasumata teenusearve.
3. **Kas ettemakse on kohe kulu?** Üldjuhul tekib alguses ettemakse vara; kuluks kajastamine sõltub teenuse saamisest ja tingimustest.
4. **Kas kõik avaliku sektori ostud annavad sisendkäibemaksu mahaarvamise õiguse?** Ei; hinnatakse tehingu ja tegevuse tingimusi.
5. **Mille poolest erinevad konto ja kulukeskus?** Konto kirjeldab sisu, kulukeskus vastutust või organisatsioonilist jaotust.
6. **Kas koondrida lisatakse alamridade summale?** Ei, see tekitab topeltarvestuse.
7. **Mis eristab algset ja muudetud eelarvet?** Hilisemad kinnitatud muudatused, ülekanded ja muud kohaldatavad täiendused.
8. **Mida tähendab YTD?** Aasta algusest näidatud lõppkuupäevani kogunenud näitaja.
9. **Kas korrektne CSV tõendab arve kinnitamist?** Ei, kinnitus ja pädevus peavad olema ametlikus menetluses.
10. **Mis näitab sinu tehnilist tugevust siin?** Allikani jälgitav teisendus, korrektsed ühikud ja perioodid ning sisulised kontrolltestid.

## Sõnastik

| Mõiste | Tähendus |
|---|---|
| Vara | Ressurss, mille üle asutus omab kontrolli ja millest oodatakse kasu või teenusepotentsiaali |
| Kohustis | Minevikusündmusest tekkinud olemasolev kohustus |
| Nõue | Õigus saada teiselt poolelt raha või muu sooritus |
| Tulu | Arvestuslik majandusliku kasu suurenemine; ei võrdu alati laekumisega |
| Kulu | Arvestuslik majandusliku kasu vähenemine; ei võrdu alati maksega |
| E-arve | Struktureeritud masintöödeldav arve; PDF üksi ei ole sama |
| Finantsdimensioon | Tehingut täpsustav tunnus, nt projekt või rahastusallikas |
| Saldo | Konto jääk kindlal ajahetkel |
| Amortisatsioon | Vara soetusmaksumuse süstemaatiline kuluks jaotamine kasutusaja jooksul |
| Auditijälg | Tõendatav seos lähteinfo, muudatuste ja tulemuse vahel |

Ametlikuks süvenemiseks: [raamatupidamise seadus](https://www.riigiteataja.ee/et/akt/rps), [avaliku sektori finantsarvestuse ja -aruandluse juhend](https://www.riigiteataja.ee/akt/103012025007), [RTK arvestusteenus](https://www.rtk.ee/finantsarvestus-personaliteenus/arvestusteenused/finantsarvestus). Õigusakti kasutamisel vali kehtiv terviktekst; konkreetse asutuse kontod ja menetlus lähtuvad ka sise-eeskirjast.
