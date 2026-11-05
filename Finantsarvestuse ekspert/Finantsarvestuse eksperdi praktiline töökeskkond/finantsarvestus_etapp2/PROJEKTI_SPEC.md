> **Uuendus 0.2:** teine etapp on teostatud. Allolev tekst säilitab esimese etapi lähteolukorra. Kehtivad täiendused: [teise etapi spetsifikatsioon](ETAPP2_TEHNILINE_SPEC.md), [kasutusjuhend](KASUTUSJUHEND_ETAPP2.md) ja [tulemused](ETAPP2_TULEMUSED.md). Etapid 3–5 ootavad korraldust.

# Projekti spetsifikatsioon · 0.1

## Eesmärk ja kasutaja

Risto valmistub HTM-i finantsarvestuse eksperdi tööks. Kandideerimise tähtaeg 15.11.2026 pärineb kasutaja lähteülesandest; töökuulutuse tähtaega siin sõltumatult ei kinnitatud. Projekti eesmärk on ühendada tema Python-, SQL- ja testimisoskus avaliku sektori finantsarvestuse praktilise mõistmisega.

Kasutajad: õppija, projektiga tutvuv tööandja ja hiljem avaliku demonstratsiooni kasutaja. Esimene versioon töötab lokaalselt. Andmed on avalikud koondandmed või selgelt fiktiivsed.

## Terviklik tööplaan

| Etapp | Tulemus | Seis |
|---|---|---|
| 1 | Allikad, andmete ettevalmistus, spetsifikatsioonid ja esimene õppetund | Käesolev tarne |
| 2 | Ostuarvete reeglid, SQL, menetluse simulatsioon | Ootab korraldust |
| 3 | Võrreldav eelarveanalüüs ja Exceli aruanded | Ootab korraldust |
| 4 | GitHub Pagesi veebiliides | Ootab korraldust |
| 5 | Terviku testid, õppematerjal ja kandideerimispakett | Ootab korraldust |

## Esimese etapi vastuvõtukriteeriumid

| ID | Kontrollitav tulemus | Tõend |
|---|---|---|
| E1-01 | Vähemalt kaks avalikku andmestikku hangitud | 2 XLSX-faili, allikaregister ja SHA-256 |
| E1-02 | Vähemalt üks pärisandmestik töödeldud | 34 eelarvekirjet ja 99 täitmiskirjet |
| E1-03 | Ühik, periood, päritolu ja lahter säilivad | Mõlema CSV veerud |
| E1-04 | Töötlemine korratav | etapp1.py ja testid |
| E1-05 | Protsessid ja rollid eristatud | TOOPROTSESSID.md |
| E1-06 | Esialgne mudel ja arhitektuur | ANDMEMUDEL.md, ARHITEKTUUR.md, SQL |
| E1-07 | Esimesed näidisandmed | 6 fiktiivset arvet ja generaator |
| E1-08 | 15–30 minuti õppetund koos lahendustega | 25-minutiline moodul |
| E1-09 | Järgmisi etappe ei teostata | Puuduvad menetlusmootor ja veebiliides |

## Piirid ja riskid

Andmeprofiil ja kooskõlakontroll on sisendi ettevalmistus, mitte 3. etapi finantsanalüüs. Mõlemad allikad sisaldavad hierarhilisi ja kattuvaid ridu. Eelarve summad on algse seaduse seisus, mitte septembriks muudetud eelarve. Tulevases analüüsis tuleb kooskõlastada asutuste ulatus, kontod, eelarve versioon ja investeeringute käsitlus.

SAP-i ligipääsu ega HTM-i sisemise kinnitusringi kirjeldust pole. Kõik sisemised tehnilised liidesed ja näidisrollide tegevused on kavand, mitte väide pärissüsteemi konfiguratsiooni kohta.

Täielik 30–50 küsimusega kursus ja vähemalt kümme ülesannet kuuluvad tervikprojekti lõpptulemusse. Esimene moodul sisaldab viit praktilist ülesannet ja kümmet kontrollküsimust.
