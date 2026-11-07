# Kontrollireeglid · 0.2.0

Kontrollid on õppesimulatsiooni reeglid, mitte ammendav loetelu õigusaktidest tulenevatest nõuetest. Kontrollpäev antakse parameetrina; demo kasutab 5.11.2026, et tulemus oleks taasesitatav.

| Kood | Tase | Käivitumise tingimus | Tegevus |
|---|---|---|---|
| PUUDUV_VALI | VIGA | Kohustuslik väli tühi või puudub | Täienda dokumenti |
| ANDMELIIK | VIGA | provenance pole SUNTEETILINE | Sellesse demonstratsiooni pärisandmeid ei sisestata |
| VALUUTA | VIGA | Valuuta erineb EUR-ist | Muud valuutad pole toetatud |
| KUUPAEV | VIGA | Kuupäev pole kehtiv AAAA-KK-PP | Kontrolli algdokumenti |
| TULEVIK | VIGA | Arve või teenuse kuupäev on kontrollpäevast hilisem | Tulevikuteenus/ettemakse vajab eraldi käsitlust |
| TAHTAEG | VIGA | Maksetähtaeg enne arve kuupäeva | Kontrolli kuupäevi |
| ULETAHTAJA | HOIATUS | Maksetähtaeg enne kontrollpäeva | Uuri makseinfot; ei tõenda tasumata arvet |
| PERIOOD | HOIATUS | Teenuse ja arve kalendrikuu erinevad | Kinnita õige arvestusperiood |
| RAHA_TYYP | VIGA | Rahaväli pole mittenegatiivne täisarv sentides | Paranda vorming; kreeditarved pole toetatud |
| SUMMA_PIIR | VIGA | Rahaväli ületab 10¹² senti | Demonstratsiooni tehniline piir |
| NULLARVE | VIGA | Neto on null | Nullarve pole selle mudeli ulatuses |
| KM_MAAR | VIGA | Määr pole 0, 0.09, 0.13 või 0.24, või pole lõplik arv | Kontrolli määra ja maksualust eraldi |
| SUMMA | VIGA | Neto + KM ≠ bruto | Paranda summade vastuolu |
| KM_SUMMA | VIGA | Ühe rea neto × määr, sendini ROUND_HALF_UP, ei võrdu KM-ga | Kontrolli ümardamist |
| KONTO | VIGA | Konto pole DEMO_KULU | Valida tuleb toetatud näidiskonto |
| KULUKESKUS | VIGA | Kulukeskus pole DEMO_IT, DEMO_HALDUS või DEMO_OPE | Täpsusta dimensioon |
| DUPLIKAAT | VIGA | Sama normaliseeritud tarnija ID ja arvenumber teisel aktiivsel dokumendil | Uuri algallikat või asenda vigane versioon |

Kohustuslikud väljad: invoice_id, supplier_id, supplier_name, invoice_number, invoice_date, service_date, due_date, description, net_cents, vat_rate, vat_cents, gross_cents, cost_center, account, provenance.

Duplikaadi normaliseerimine eemaldab äärmist ja korduvat tühikut ning ignoreerib tähesuurust. See on kahtluse reegel, mitte tõend pettusest. Mõlemad dokumendid saavad vea. Sama sisemise ID ja sama sisuga kordusimport ei tekita uut dokumenti. Sama ID muutunud sisu korral lükatakse kogu impordipartii tagasi. ASENDATUD vana versioon duplikaadikontrollis enam ei osale.

Puuduva invoice_id korral moodustub tehniline ID `PUUDUV-<räsi algus>`, kuid PUUDUV_VALI viga jääb alles. Vigane rida säilib JSON-kujul sisenditabelis.

Kõik VIGA-tasemega leiud peatavad edasiliikumise. Hoiatus ei peata iseenesest, kuid toiming nõuab sisulist põhjendust; vähemalt 10 märgi kontroll on tehniline miinimum, mitte tõend põhjenduse kvaliteedist. Edasi liikumisel tehakse kontroll uuesti. Nii võib hiljem lisatud duplikaat peatada ka varem kinnitatud arve edastamise.

Maksumäärade loend on näidisreegel, mitte maksukäsitluse automaatne otsus. See ei erista nullmäära ja maksuvabastuse õiguslikku alust, pöördmaksustamist ega osalist mahaarvamist. Määrade ametlik lähteviide: [EMTA 2026 maksumuudatused](https://www.emta.ee/uudised/maksumuudatused-2026), kontrollitud eelmises etapis 5.11.2026.


## Lisanduv tüübikontroll 0.2.1

`ANDMEKUJU` (VIGA): Pydanticu sisendleping ei sobi, näiteks tarnija nimi on loend. Rakendub pärast seniseid kontrolle ainult siis, kui need ei leidnud blokeerivat viga. Vana reeglistiku koodid säilivad; uued kontrollkäigud salvestavad rule_version=0.2.1.
