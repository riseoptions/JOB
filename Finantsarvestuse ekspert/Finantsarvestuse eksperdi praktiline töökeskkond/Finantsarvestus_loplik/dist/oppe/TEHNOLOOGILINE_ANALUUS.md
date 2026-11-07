# Tehnoloogiline analüüs

| Valik | Praktiline kasu | Piir |
|---|---|---|
| Python | Üks testitav reeglistik; korratavad aruanded | Ühekordne väike tabel võib Excelis kiiremini valmida |
| SQL/SQLite | Seosed, tehingud, audit, ristkontroll | Brauseri mälu pole püsiv mitme kasutaja register |
| Pydantic v 2 | Tüübileping ja selged väljavead; True pole raha | Õige tüüp ei tõenda tehingut |
| Polars | Lazy valik ja Int 64 rahaveerud |99 real ei tõesta kiiruse vahe üldist paremust |
| pandas | Tuttav analüüs ja sõltumatu võrdlustee | Jälgi puuduvaid väärtusi ja ujukomat |
| Excel/openpyxl | Kolleegile kasutatav väljund ja vormistus | openpyxl ei arvuta valemeid ümber |
| Pyodide/Worker | Python brauseris, failid lokaalses seansis | Esmalaadimine ja mälu; pole SAP-i serveriliides |

Pydanticu [mudelid](https://pydantic.dev/docs/validation/2.5/concepts/models/) tagavad valideeritud tulemuse tüübid. Polarsi [optimeerija](https://docs.pola.rs/user-guide/lazy/optimizations/) võib veeruvalikut ja filtreid lugemisele lähemale viia. Valikut põhjendab esinduslik mõõtmine, mitte tehnoloogia nimi.

## Olemasolevate süsteemide täiendamine

SAP jääks põhiregistriks. RTIP ja e-arvete keskkond säilitaksid ametliku menetluse; tööriist toetaks eelkontrolli ja erandiaruannet. RTK [teenusekirjeldus](https://www.rtk.ee/finantsarvestus-personaliteenus/arvestusteenused/finantsarvestus) kinnitab süsteemide rolli, mitte konkreetset API-õigust. Demo ei ühendugi nendega.

## API laienduse kavand

Kasuta sama teenusekihti WebSession.import_file/snapshot/export. Tulevane POST /invoice-checks võiks tagastada ID, reeglistiku versiooni ja leiud; seda otspunkti pole rakendatud. Pärissisend vajab uut andmelepingut, mitte SUNTEETILINE kaitse eemaldamist. Lisa serveri autentimine, rollid, püsibaas ja audit. Väline sündmuse ID tagab idempotentsuse; tehniline vastuvõtt ja finantskinnitus on eri olekud. Saladusi brauserisse ei panda.

## Tulevikutehnoloogiad vajaduse järgi

| Võimalus | Eeltingimus | Mõõdik ja inimese otsus |
|---|---|---|
| ML anomaaliad | Lubatud ajalugu, märgendid, ajapõhine testjaotus | Leidude täpsus ja uurimisaeg; inimene hindab |
| LLM seletus | Kontrollitud arvud, definitsioonid, viited | Faktivead; inimene kinnitab teksti |
| RAG juhendiotsing | Lubatud juhendid, kehtivusaeg ja õigused | Õige redaktsioon ja allikatoetus; inimene tõlgendab erandit |
| Agent | Väikesed lubatud lugemistoimingud ja logi | Edukus/vead; muutus ja makse ei lähe autonoomselt läbi |

17 sünteetilist arvet ei ole pettusemudeli treeningandmestik. RAG viide ei garanteeri õigsust. Dokumendi käsulaadne tekst on andmed, mitte agendi volitus. Pärisarvete saatmine välisele mudelile eeldab asutuse lubatud lahendust.

## Ajasääst

Automatiseeri esmalt vorming, summade kooskõla, duplikaadikahtlus ja sama perioodi raport. Inimesele jäävad tarne tõendamine, maksukäsitlus, konto erandid ja maksmise lubamine. Näitlik 200 arvet ×1,5 min säästu=300 min; hooldus/valepositiivsed 90 min →neto 210 min. Need on oletused, mitte mõõdetud saavutus. Piloodis mõõda sama keerukusega partiide aega, veamäära ja hooldust. Järgmine kasulik samm oleks lubatud pärisekspordi kontroll, mitte kohe AI-agent.
