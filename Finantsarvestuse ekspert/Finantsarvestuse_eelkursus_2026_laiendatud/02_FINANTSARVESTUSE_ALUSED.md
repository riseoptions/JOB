# 02. Finantsarvestuse alused – nähtused, mitte ainult terminid

## 1. Viis asja, mida ei tohi segamini ajada

| Mõiste | Lihtne tähendus | Näide |
|---|---|---|
| **Eelarve** | Eelnevalt kavandatud ja kinnitatud rahaline raam | IT-teenuste aastane eelarve 60 000 € |
| **Kulu** | Tarbitud teenuse või ressursi väärtus arvestusperioodis | Oktoobri hooldusteenus 1000 € (+ võimalik mitte-mahaarvatav KM) |
| **Kohustis** | Asutuse tasumiskohustus tarnija ees | Kinnitatud, kuid maksmata arve 1240 € |
| **Makse** | Raha tegelik ülekandmine | Tarnijale kantakse 1240 € novembris |
| **Eelarve täitmine** | Mõõdik eelarve jälgimiseks; sõltub aruande metoodikast | Perioodi vastava liigi täitmine 45 000 € |

**Oluline:** riigi finantsarvestus on tekkepõhine, kuid riigieelarve ja selle täitmise aruannete liigitus ning mõõdikud nõuavad metoodika eraldi kontrolli. Ära eelda, et kõigi tabelite „kulu“ on sama näitaja.

Allikas: [Rahandusministeerium – riigi raamatupidamine](https://www.fin.ee/riigi-rahandus-ja-maksud/riigi-raamatupidamine).

## 2. Näide: teenus oktoobris, arve novembris, makse detsembris

- Teenus osutatakse **28.10**: majandussisu järgi on teenus üldjuhul oktoobri kulu.
- Arve saabub **03.11**: dokument tõendab summat ja tekitab menetlustoimingu; kohustis võis tekkida juba oktoobris.
- Makse toimub **05.12**: väheneb rahajääk ja kohustis, kuid uus detsembrikuu kulu sellest üksnes makse tõttu ei teki.

Tegelik kajastamise aeg ja kanne sõltuvad lepingu tingimustest, dokumentidest ning rakenduvast arvestusjuhendist.

## 3. Deebet ja kreedit – miks summa peab tasakaalus olema?

Iga lihtsa kahekordse raamatupidamiskande korral:

`deebet kokku = kreedit kokku`

Kui ostuarve on 1240 € ja **eeldame üksnes harjutuse jaoks**, et kogu käibemaks kuulub kulusse, siis:

| Konto tüüp | Deebet | Kreedit |
|---|---:|---:|
| IT-teenuse kulu | 1240 | 0 |
| Võlg tarnijale | 0 | 1240 |
| **Kokku** | **1240** | **1240** |

Kui makstakse arve:

| Konto tüüp | Deebet | Kreedit |
|---|---:|---:|
| Võlg tarnijale | 1240 | 0 |
| Raha pangas | 0 | 1240 |

Need on **õppeks lihtsustatud kontotüübid**, mitte riigi SAP-i ametlikud kontokoodid. Kui sisendkäibemaksu mahaarvamine on konkreetsel juhul lubatud, muutub kulukande ja maksuarvestuse jaotus.

## 4. Käibemaks (2026)

Eestis kehtib 1. juulist 2025 **24% standardmäär**; olemas on ka muud määrad ning maksuvabad olukorrad. Maksumäära määramisel on oluline käibe toimumise aeg ja tehingu liik.

Näidis, kui maksustatav väärtus on 1000 € ja kohaldub standardmäär:

```text
Käibemaks: 1000 × 0,24 = 240 €
Arve kokku: 1000 + 240 = 1240 €
Kui kogusumma on teada: 1240 / 1,24 = 1000 € (maksustatav väärtus)
```

**Ära järelda:** et asutus saab 240 € automaatselt tagasi küsida. Sisendkäibemaksu mahaarvamise õigus on eraldi õiguslik kontroll.

Allikas: [EMTA maksumäärad](https://www.emta.ee/ariklient/maksud-ja-tasumine/kaibemaks/kaibemaksumaarad-ja-maksuvaba-kaive/uldine-kaibemaksumaar).

## 5. Nõuded, kohustised, varad, kulud, tulud

- **Vara:** kontrollitav majanduslik ressurss (nt raha, nõue, põhivara).
- **Kohustis:** olemasolev kohustus (nt tasumata ostuarve).
- **Tulu:** aruandeperioodi majandusliku kasu või teenusepotentsiaali suurenemine arvestusreeglite mõttes.
- **Kulu:** aruandeperioodil tarbitud ressursi arvestuslik väärtus.
- **Investeering / põhivara:** teatud soetused ei muutu ostmisel kohe täies ulatuses perioodikuluks; arvestus sõltub vara iseloomust ja rakenduvatest kapitaliseerimisreeglitest.

## 6. Üks küsimus, mida alati küsida

**„Mis majandustehing tegelikult toimus ning millise aruande metoodika järgi seda mõõdame?“**

See on olulisem kui üksiku Exceli lahtri arvväärtus.

## Kiirtest

1. 1240 € arve saabub 3. novembril teenuse eest, mis osutati oktoobris. Millise kuu kulu see üldjuhul on?
2. Kas arve tasumine tekitab samast teenusest uue kulu?
3. Kui 1000 € maksustatavale väärtusele lisatakse 24% käibemaks, kui suur on arve?
4. Kas iga 1240-eurone arve tähendab 1240-eurost kulu?

**Vastused:** (1) oktoober, (2) ei, (3) 1240 €, (4) ei – sõltub nt sisendkäibemaksu käsitlusest ja vara/kulu klassifikatsioonist.
