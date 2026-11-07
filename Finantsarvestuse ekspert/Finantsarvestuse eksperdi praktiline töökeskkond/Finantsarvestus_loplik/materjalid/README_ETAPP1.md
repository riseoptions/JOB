# Finantsarvestuse ja kulude analüüsi töökeskkond

## Etapp 1 · analüüs ja ettevalmistus · 5.11.2026

Eesti avaliku sektori näitel koostatud iseseisev õppe- ja demonstratsiooniprojekt. See ei ole HTM-i ega RTK ametlik infosüsteem. Versioon 0.1.

**Valmis:** kaks muutmata ametlikku XLSX-algfaili, nende profiil, HTM-i andmete kontrollitavad CSV-väljavõtted, kuude ja kumulatiivse summa kooskõlakontroll, kuus sünteetilist arvet, projekti alusdokumendid ning 25-minutiline õppemoodul.

**Etapid 2–5 ei ole alustatud.** Arvete kontrollimootor, menetlusring, automaatne finantsanalüüs, Exceli aruandlus ja veebirakendus ei kuulu sellesse versiooni.

## Alusta siit

1. Loe [etapi tulemust](../ETAPP1_TULEMUSED.md) ja [tööprotsesse](../TOOPROTSESSID.md).
2. Läbi [25-minutiline õppemoodul](../FINANTSARVESTUSE_OPPEMATERJAL.md).
3. Käivita programm [kasutusjuhendi](../KASUTUSJUHEND.md) järgi.
4. Uuri [andmemudelit](../ANDMEMUDEL.md), [arhitektuuri](../ARHITEKTUUR.md) ja [allikaid](../ANDMEALLIKAD.md).

```bash
python -m pip install -r requirements.txt
python kood/etapp1.py
python kood/loo_naidisandmed.py
python -m unittest discover -s testid -v
```

Käsud käivita lahtipakitud projekti juurkaustas. Internetti on vaja teekide paigaldamiseks, kuid kaasasolevate algfailide töötlemiseks mitte. CSV-väljundid on juba kaasas.

## Kaustad

| Kaust | Sisu |
|---|---|
| andmed/algandmed | Muutmata ametlikud XLSX-failid |
| andmed/toodeldud | Tuletatud CSV-väljavõtted, andmeprofiil ja kontrolltulemused |
| andmed/sunteetilised | Üksnes fiktiivsed näidisarved |
| kood | Esimese etapi käivitatavad programmid ja Colabi märkmik |
| sql | Esialgne tabeliskeem, mitte valmis rakenduse andmebaas |
| testid | Esimese etapi automaatkontrollid |
| materjalid | Algne lähteülesanne ja jätkamise seis |

## Mida andmed ütlevad?

Algse 2026. aasta seaduse HTM-i valitsemisala kulurida on −1 176 947,117 tuhat eurot. Täitmise faili HTM-i valitsemisala **kulude ja investeeringute, v.a amortisatsioon** üheksa kuu näitaja on 886 184 288,61 eurot. Need on erineva ulatusega mõõdikud. Programm ei jaga neid omavahel ega nimeta saadud suhet eelarve täitmiseks.

Täpsed lähtekohad: seaduse esimese lehe D108 ja täitmise lehe N137. Vaata [tulemusi ja piiranguid](../ETAPP1_TULEMUSED.md).

## Seos varasema tööga

Kontrollitud varasema `Finantsarvestuse_eelkursus_2026.zip` README kirjeldab eraldi 6–8 tunni eelkursust ja mini-laborit. See ei ole käesoleva viieetapilise projekti esimese etapi lähtekood. Pakette ei ühendatud ega varasemaid faile muudetud. Käesolev struktuur on edasiste etappide ühine alus.

[Projekti spetsifikatsioon](../PROJEKTI_SPEC.md) · [Tarkvara spetsifikatsioon](../TARKVARA_SPEC.md) · [Arendus](../ARENDUSJUHEND.md) · [Testimine](../TESTIMINE.md)
