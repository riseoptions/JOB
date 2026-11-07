# Õppemoodul 3 · analüütiku 30 minutit

**Eesmärk:** oskad selgitada eelarve kasutamist, perioodihälvet, toetuse arvestust ning Pydanticu/Polarsi praktilist rolli. Läbiv olukord: fiktiivne finantsanalüütik koostab juhile HTM avalike koondandmete ülevaate ja kontrollib kolme väljamõeldud toetuse juhtumit.

Ajakava: 0–5 min demo ja Excel; 5–11 min eelarve; 11–17 min kulud ja toetus; 17–24 min Pydantic/Polars; 24–30 min harjutused ning vastuste kontroll. Pikemaks harjutamiseks jäta lahendused esialgu lugemata.

## 1. Eelarve kasutamine ja plaanihälve

**A. Mõiste.** Kasutamise määr näitab, kui palju võrdlusaluseks valitud eelarvest on kasutatud. Perioodihälve võrdleb sama perioodi tegelikku kulu ja plaani.

**B. Miks?** Juhile tuleb öelda, mida protsent mõõdab. Augusti täitmine jagatud terve aasta eelarvega ei näita, kas augusti lõpuks oli kulu plaanipärane.

**C. Töövoog.** Kontrolli ühikut → perioodi → asutuse ulatust → mõõdikut → eelarveversiooni → koond/detail taset → arvuta. Projekti augusti failis on eelarve ja täitmine sama rea eri veergudes.

**D. Arvuline näide.** Ajakohane aastaeelarve 1 207 523 833 €, kaheksa kuu täitmine 772 600 007 €. Kasutamine ≈63,98%, kasutamata aastaeelarve 434 923 826 €. Kui kaheksa kuu kinnitatud plaan puudub, jääb tegelik perioodihälve teadmata.

**E. Python.** `budget_metrics(117694711700, 120752383300, 77260000700)` annab sentides eelarve muutuse ja jäägi ning kasutamise suhtarvu.

**F. Ülesanne.** Fiktiivne septembri plaan 10 000 €, tegelik kulu 11 000 €. Leia hälve ja protsent. Kas 64% aastaeelarve kasutamine kaheksa kuuga tõendab säästu?

**G. Lahendus.** Hälve +1000 € ehk +10%; kulud ületavad sama perioodi plaani. 64% ei tõenda säästu: kulud võivad olla hooajalised ja aasta lõpus võib toimuda suurem väljamakse.

**H. Tüüpviga.** Võetakse 8/12 automaatselt „õigeks“ plaaniks. Lineaarne jaotus on eeldus, mitte kinnitatud kuueelarve.

**I. Töövestlus.** „Mida teete enne kahe Exceli tabeli ühendamist?“ Selgitan võrdlusaluse kontrolli ning keeldun eri ulatusega näitajatest petlikku protsenti tegemast.

## 2. Kulude võrdlus ja koondread

**A. Mõiste.** Sama perioodi aastavõrdlus mõõdab muutust; see ei ole eelarvehälve. Rahastuse ristlõige näitab sama kulu teise tunnuse järgi.

**B. Miks?** Kui liita koond, selle alamread ja välisvahendid kokku, loetakse osa kulusid mitu korda.

**C. Töövoog.** Vali jaanuar–september mõlemas aastas, sama ulatus ja mõõdik. Hoia koond eraldi. Kontrolli üheksa kuu summat allika YTD vastu.

**D. Arvuline näide.** 2025: 816 770 619,04 €. 2026: 886 184 288,61 €. Kasv 69 413 669,57 € ehk ligikaudu 8,50%. Mõõdik on kulud ja investeeringud ilma amortisatsioonita.

**E. Python.** `aggregate_months(path)` annab 9 rida; nende sentide summa on 88 618 428 861. `year_comparison(path)` välistab välisvahendite ristlõike.

**F. Ülesanne.** Miks ei või lisada kogu kulule 94 987 880,77 € välisvahendeid? Mida tähendab 0 € eelmine aasta protsendiarvutuses?

**G. Lahendus.** Välisvahendite rida kattub juba arvestatud kuludega. Nullist baasi korral kasvuprotsenti ei määrata; näita absoluutset muutust ja puuduvat suhtarvu.

**H. Tüüpviga.** Kulu kasvust järeldatakse automaatselt ebatõhusus. Põhjus võib olla mahu-, hinna-, ajastus- või klassifikatsioonimuutus; koondandmed üksi ei otsusta.

**I. Töövestlus.** „Kuidas väldite topeltarvestust?“ Kirjeldan ridade taset, lubatud summeerimist ning sõltumatut koondsummaga võrdlust.

## 3. Toetus ja ettemakse

**A. Mõiste.** Abikõlblik kulu on tingimustele vastav kulu. Toetus sõltub määrast ja ülempiirist. Ettemakse on rahavoog, mitte iseenesest kulu või lõplik toetus.

**B. Miks?** Tehtud kulude ja väljamakstud raha segiajamine võib anda põhjendamatu juurdemakse.

**C. Töövoog.** Kontrolli kuludokumente ja perioodi → määra abikõlblik summa → rakenda määra → kontrolli ülempiiri → lahuta ettemakse. Siin kasutatakse fiktiivseid tingimusi, mitte ühtegi konkreetset toetusmeedet.

**D. Arvuline näide.** Kulu 11 000 €, abikõlblik 10 000 €, määr 80%, ülempiir 9000 €, ettemakse 6000 €. Toetus min(8000, 9000)=8000 €; juurdemakse 2000 €.

**E. Python.** `grant_result({...})` kasutab Pydanticu mudelit ja Decimal ümardamist. 1 sent × 50% = 0,5 senti ümardatakse HALF_UP reegliga 1 sendiks.

**F. Ülesanne.** Abikõlblik kulu 3000 €, määr 80%, ülempiir 3000 €, ettemakse 3000 €. Arvuta tulemus. Teises näites on abikõlblik kulu 100 €, määr 80%, ülempiir 50 €.

**G. Lahendus.** Esimene toetus 2400 €, arvutuslik tagasinõue 600 €. Teine toetus 50 €, sest ülempiir piirab 80 € arvutust. Makset ega tagasinõude otsust programm ise ei tee.

**H. Tüüpviga.** Ülempiiri rakendatakse enne toetuse määra või kogu tegelik kulu kuulutatakse automaatselt abikõlblikuks.

**I. Töövestlus.** „Milliseid tõendeid küsiksite?“ Kuludokument, periood, abikõlblikkuse alus, lepingutingimus, määr, ülempiir, ettemakse ja kinnitused.

## 4. Pydantic ja Polars analüütiku töös

**A. Mõiste.** Pydantic valideerib ühe kirje lepingu. Polars töötleb veergudena paljusid kirjeid. SQLite hoiab tehinguid ja pandas pakub tuttavat võrdluslahendust.

**B. Miks?** Korrektse kujuga andmed võimaldavad arvutusi automatiseerida. Tabelitööriist üksi ei otsusta, kas arve tohib kinnitada.

**C. Töövoog.** Säilita toorsisend → senised ärireeglid → tüübitud kontroll → menetlus. Analüüsis vali võrreldavad read → arvuta → kontrolli summasid → väljasta aruanne.

**D. Näide.** CSV `'100000'` teisendub 100000 sendiks. `True` ei tohi muutuda 1 sendiks. Senine arvebruto 124000 senti jääb samaks.

**E. Python.** Käivita `python kood/pydantic_naide.py`. Võrdle `aggregate_months(path, 'polars')` ja `aggregate_months(path, 'pandas')`. Praktikanäited on failis PYDANTIC_POLARS.md.

**F. Ülesanne.** Muuda näites net_cents väärtuseks True ja selgita viga. Lisa arvele veerg `projekti_markus`. Kas lisaveerg peab vana CSV kasutuse katkestama?

**G. Lahendus.** True on bool ning teadlik senditeisendaja keeldub sellest. Lisaveerg säilib `extra='allow'` abil; see ei muutu automaatselt kontrollitud äriväljaks.

**H. Tüüpviga.** „Pydantic läbis, järelikult LLM-i genereeritud arve on tõene.“ Skeem tõendab kuju, mitte väite tõele vastavust ega alusdokumendi olemasolu.

**I. Töövestlus.** „Miks kaks tabeliteeki?“ Polars on uus analüüsitee; pandas on väike kontroll- ja õppimisvõrdlus. Olemasolevat menetlusmootorit ei kirjutata ümber.

## Kontrollküsimused vastustega

1. Mis on eelarve kasutamise nimetaja? Selles aruandes augusti seisuga ajakohane terve aasta eelarve.
2. Kas kasutamata eelarve võrdub säästuga? Ei; puudu on sama perioodi plaan ja põhjused.
3. Miks august ja september eraldi? Erinev periood ja näitaja koosseis.
4. Kas koond ja detail summeeritakse koos? Ei.
5. Mida tähendab None protsendiveerus? Suhtarv on määramata, näiteks nullist nimetaja korral.
6. Kas ettemakse on automaatselt kulu? Ei.
7. Kus raha täpsus säilib? int/Int64/SQLite sentides; määrad ja ümardus Decimal abil.
8. Kas Pydantic teeb duplikaadipäringu? Ei, selle teeb menetlusmootor.
9. Miks lazy päring? Võimaldab päringu kui terviku optimeerimist; collect käivitab selle.
10. Kas ühe väikese faili ajastus tõestab Polarsi paremust? Ei; töökoormus ja keskkond määravad tulemuse.

## Sõnastik ja tööpäeva lõpp

**YTD** – aasta algusest aruandekuuni. **Plaanihälve** – tegelik miinus võrreldav plaan. **Abikõlblik kulu** – tingimustele vastav kulu. **Provenance/päritolu** – kust näitaja pärineb. **Skeem** – väljade, tüüpide ja piirangute leping. **Lazy** – päringu kirjeldamine enne täitmist.

Analüütiku lühike üleandmine: „Augustiks kasutati 64,0% ajakohasest aastaeelarvest. Septembri teistsugusel kuluvaatel on sama perioodi aastakasv 8,5%. Enne hälbe põhjuste hindamist vajan perioodiplaani. Toetusnäites vajab teine projekt 600 € tagasinõude alusandmete kontrolli.“

Õpetajale: palu õppijal esmalt nimetada protsendi lugeja ja nimetaja ning alles siis arvutada. Hinda kolme asja: võrreldavus, senditäpsus ja järelduse piirid. Täielik lõpukursus ja kandideerimispakett jäävad viiendasse etappi.
