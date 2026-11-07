"""Raamatupidamise mini-labor (õppeotstarbel, mitte maksuarvestuseks).

Käivitamine: python raamatupidamise_demo.py
Väljund: paevik.csv, kontode_saldod.csv ja aruanne.txt.
Python 3 standardteek; puuduvad välised sõltuvused.
"""

from collections import defaultdict
from decimal import Decimal
from pathlib import Path
import csv

D = Decimal
OUTPUT = Path(__file__).resolve().parent

# Vara- ja kulukontode deebetsaldo on positiivne;
# kohustiste, tulu ja omakapitali kreeditsaldo on positiivne.
ACCOUNTS = {
    "Raha": "asset",
    "Nõuded ostjatele": "asset",
    "Varud": "asset",
    "Seadmed": "asset",
    "Akumuleeritud kulum": "contra_asset",
    "Võlad tarnijatele": "liability",
    "Pikaajaline laen": "liability",
    "Osakapital": "equity",
    "Müügitulu": "revenue",
    "Teenusetulu": "revenue",
    "Müüdud kaupade kulu": "expense",
    "Palgakulu": "expense",
    "Üürikulu": "expense",
    "Muud tegevuskulud": "expense",
    "Intressikulu": "expense",
    "Kulum": "expense",
}

# (kirje ID, deebetkonto, kreeditkonto, summa, rahavoo klass kui raha liigub)
JOURNAL = [
    (1, "Raha", "Osakapital", "20000", "finantseerimine"),
    (2, "Raha", "Pikaajaline laen", "15000", "finantseerimine"),
    (3, "Seadmed", "Raha", "12000", "investeerimine"),
    (4, "Varud", "Võlad tarnijatele", "10000", None),
    (5, "Nõuded ostjatele", "Müügitulu", "15000", None),
    (6, "Müüdud kaupade kulu", "Varud", "6000", None),
    (7, "Raha", "Nõuded ostjatele", "12000", "äritegevus"),
    (8, "Raha", "Teenusetulu", "20000", "äritegevus"),
    (9, "Palgakulu", "Raha", "12000", "äritegevus"),
    (10, "Üürikulu", "Raha", "4000", "äritegevus"),
    (11, "Muud tegevuskulud", "Raha", "2000", "äritegevus"),
    (12, "Võlad tarnijatele", "Raha", "7000", "äritegevus"),
    (13, "Intressikulu", "Raha", "600", "äritegevus"),
    (14, "Kulum", "Akumuleeritud kulum", "3000", None),
]


def eur(n):
    return f"{n:,.2f} €".replace(",", " ")


def build_reports():
    # Positiivne deebetmiinus-kreedit saldo, sobib T-kontode jälgimiseks.
    balances = defaultdict(lambda: D("0"))
    flows = defaultdict(lambda: D("0"))
    rows = []
    debits = credits = D("0")

    for entry_id, dr, cr, amount_text, cash_category in JOURNAL:
        assert dr in ACCOUNTS and cr in ACCOUNTS
        amount = D(amount_text)
        assert amount > 0
        balances[dr] += amount
        balances[cr] -= amount
        debits += amount
        credits += amount
        rows.append((entry_id, dr, cr, amount, cash_category or ""))
        if cash_category:
            cash_delta = (amount if dr == "Raha" else D("0")) - (
                amount if cr == "Raha" else D("0")
            )
            assert cash_delta != 0, "Rahavoo klass peab puudutama raha kontot"
            flows[cash_category] += cash_delta

    assert debits == credits
    assert sum(balances.values()) == 0, "Käibeandmik ei ole tasakaalus"

    revenue = -sum(v for a, v in balances.items() if ACCOUNTS[a] == "revenue")
    expenses = sum(v for a, v in balances.items() if ACCOUNTS[a] == "expense")
    profit = revenue - expenses
    assets = sum(v for a, v in balances.items() if ACCOUNTS[a] in ("asset", "contra_asset"))
    liabilities = -sum(v for a, v in balances.items() if ACCOUNTS[a] == "liability")
    contributed_capital = -sum(v for a, v in balances.items() if ACCOUNTS[a] == "equity")
    equity = contributed_capital + profit

    assert assets == liabilities + equity
    cash = balances["Raha"]
    assert cash == sum(flows.values())
    assert (cash, revenue, profit, assets, liabilities, equity) == tuple(map(D, [
        "29400", "35000", "7400", "45400", "18000", "27400"
    ]))
    assert (flows["äritegevus"], flows["investeerimine"], flows["finantseerimine"]) == tuple(map(D, [
        "6400", "-12000", "35000"
    ]))

    with (OUTPUT / "paevik.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "deebet", "kreedit", "summa_eur", "rahavoog"])
        for entry_id, dr, cr, amount, cat in rows:
            w.writerow([entry_id, dr, cr, str(amount), cat])

    with (OUTPUT / "kontode_saldod.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["konto", "liik", "deebet_miinus_kreedit"])
        for account in sorted(ACCOUNTS):
            w.writerow([account, ACCOUNTS[account], str(balances[account])])

    text = "\n".join([
        "NÄIDIS OÜ: FINANTSARUANNETE KONTROLL (ÕPPENÄIDE)",
        "=" * 57,
        f"Müügitulu:                    {eur(revenue)}",
        f"Kulud kokku:                  {eur(expenses)}",
        f"Puhaskasum:                   {eur(profit)}",
        "-" * 57,
        f"Varad kokku:                  {eur(assets)}",
        f"Kohustised:                   {eur(liabilities)}",
        f"Omakapital:                   {eur(equity)}",
        f"Bilansi vahe:                 {eur(assets - liabilities - equity)}",
        "-" * 57,
        f"Äritegevuse rahavood:         {eur(flows['äritegevus'])}",
        f"Investeerimise rahavood:      {eur(flows['investeerimine'])}",
        f"Finantseerimise rahavood:     {eur(flows['finantseerimine'])}",
        f"Raha perioodi lõpus:          {eur(cash)}",
        f"Rahavoogude kontrollivahe:    {eur(cash - sum(flows.values()))}",
        "KÕIK ARVULISED KONTROLLID LÄBITUD.",
    ])
    (OUTPUT / "aruanne.txt").write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    build_reports()
