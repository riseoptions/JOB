"""Finantsarvestuse tulevikutehnoloogiate LABOR – AINULT sünteetilised andmed.

Käivitamine projekti juurkaustast:
    python kood/tuleviku_finantslabor.py

Koostab 50 fiktiivset arvet, teostab deterministlikud kontrollid ja
loob auditeeritava SQLite/CSV/JSON ning openpyxl olemasolul XLSX väljundi.
Mitte mingit ühendust SAP-i, RTIP-i ega päris maksekeskkonnaga.
"""
from __future__ import annotations

import csv
import hashlib
import json
import random
import sqlite3
from collections import Counter, defaultdict
from datetime import date, timedelta
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "andmed"
OUT = BASE / "valjund"
VERSION = "tuleviku_finantslabor-1.0"
BUDGET_EUR = {"IT": 25000, "KOOLITUS": 20000, "HALDUS": 25000}
FIELDS = ["kirje_id", "tarnija", "arve_nr", "arve_kp", "neto", "km", "kokku", "kulukeskus"]


def euro_to_cents(s: str) -> int:
    """Rahasummad sentides: vältida finantsarvutustes float'i."""
    try:
        x = Decimal(str(s).replace(",", "."))
        if not x.is_finite():
            raise ValueError("Rahasumma pole lõplik arv")
        return int((x * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    except (InvalidOperation, ValueError) as ex:
        raise ValueError(f"Vigane rahasumma: {s!r}") from ex


def eur(cents: int) -> str:
    return f"{Decimal(cents) / 100:.2f}"


def make_demo_rows(n: int = 50) -> list[dict[str, str]]:
    """Taasesitatavad fiktiivsed arved; mõned teadlikud erandid."""
    rng = random.Random(42)
    suppliers = {
        "IT": "Fiktiivne IT Partner OU",
        "KOOLITUS": "Fiktiivne Koolitaja OU",
        "HALDUS": "Fiktiivne Büroo OU",
    }
    rows = []
    for i in range(n):
        center = ["IT", "KOOLITUS", "HALDUS"][i % 3]
        neto = rng.randrange(18000, 155000)  # sendid
        km = int((Decimal(neto) * Decimal("0.24")).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
        rows.append({
            "kirje_id": f"K-{i+1:03d}",
            "tarnija": suppliers[center],
            "arve_nr": f"AR-{2026}-{i+1:04d}",
            "arve_kp": str(date(2026, 10, 1) + timedelta(days=i % 28)),
            "neto": eur(neto), "km": eur(km), "kokku": eur(neto + km),
            "kulukeskus": center,
        })
    if n >= 15:
        rows[4]["kokku"] = eur(euro_to_cents(rows[4]["kokku"]) + 1000)  # 10 € vahe
        rows[8]["arve_nr"] = rows[2]["arve_nr"]
        rows[8]["tarnija"] = rows[2]["tarnija"]  # sama tarnija ja number
        rows[12]["kulukeskus"] = ""  # puuduv info
        rows[14]["arve_kp"] = "2026-99-40"  # vigane kuupäev
    if n >= 20:
        rows[19]["neto"] = "25000.00"
        rows[19]["km"] = "6000.00"
        rows[19]["kokku"] = "31000.00"  # ebatavaline, kuid aritmeetiliselt korrektne
    return rows


def validate_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    """Reeglid leiavad KONTROLLIMIST vajavad juhud, mitte pettusi."""
    counts = Counter((r["tarnija"].strip().lower(), r["arve_nr"].strip().lower()) for r in rows)
    result = []
    for row in rows:
        issues = []
        if not row["tarnija"].strip() or not row["arve_nr"].strip():
            issues.append("KOHUSTUSLIK_VALI_PUUDUB")
        if not row["kulukeskus"].strip():
            issues.append("KULUKESKUS_PUUDUB")
        elif row["kulukeskus"] not in BUDGET_EUR:
            issues.append("TUNDMATU_KULUKESKUS")
        try:
            date.fromisoformat(row["arve_kp"])
        except ValueError:
            issues.append("VIGANE_KUUPAEV")
        try:
            net = euro_to_cents(row["neto"])
            vat = euro_to_cents(row["km"])
            gross = euro_to_cents(row["kokku"])
            if min(net, vat, gross) < 0:
                issues.append("NEGATIIVNE_SUMMA_KONTROLLI")
            if net + vat != gross:
                issues.append("SUMMA_EI_KLAPI")
            if net > 10_000 * 100:
                issues.append("EBATAVALISELT_SUUR_ARVE")
        except ValueError:
            issues.append("VIGANE_RAHASUMMA")
        if counts[(row["tarnija"].strip().lower(), row["arve_nr"].strip().lower())] > 1:
            issues.append("VOIMALIK_DUPLIKAAT")
        result.append({**row, "kontrollid": ",".join(issues),
                       "staatus": "VAJAB_ULEVAATUST" if issues else "ESIALGNE_OK"})
    return result


def build_report(rows: list[dict[str, str]]) -> dict:
    flags = Counter(code for r in rows for code in r["kontrollid"].split(",") if code)
    by_center = defaultdict(int)
    for r in rows:
        try:
            by_center[r["kulukeskus"]] += euro_to_cents(r["kokku"])
        except ValueError:
            continue
    # ÕPPENÄIDE: see on arvesummade koond, mitte ametlik eelarvetäitmine.
    return {
        "andmed": "AINULT SYNTEETILISED – EI OLE HTM/RTK ANDMED",
        "versioon": VERSION,
        "kirjeid": len(rows),
        "vajab_ulevaatust": sum(r["staatus"] == "VAJAB_ULEVAATUST" for r in rows),
        "reeglite_loendur": dict(sorted(flags.items())),
        "arve_summad_kulukeskuse_jargi_eur": {key or "PUUDUB": eur(value)
                                                     for key, value in sorted(by_center.items())},
        "marge": "SUM(kokku) on toorarvete koond; see ei ole ametlik raamatupidamis- ega eelarvetaitmine."
    }


def save_sqlite(rows: list[dict[str, str]], sha256: str) -> None:
    path = OUT / "tuleviku_andmed.sqlite"
    with sqlite3.connect(path) as con:
        con.execute("""CREATE TABLE IF NOT EXISTS demo_arved (
            kirje_id TEXT PRIMARY KEY, tarnija TEXT, arve_nr TEXT, arve_kp TEXT,
            neto_senti INTEGER, km_senti INTEGER, kokku_senti INTEGER,
            kulukeskus TEXT, staatus TEXT, kontrollid TEXT, source_sha256 TEXT
        )""")
        con.execute("""CREATE TABLE IF NOT EXISTS demo_import (
            source_sha256 TEXT PRIMARY KEY, versioon TEXT, kirjete_arv INTEGER
        )""")
        # Idempotentne demo: sama kirje_id ei tekita uut topeltrida.
        for r in rows:
            con.execute("""INSERT OR REPLACE INTO demo_arved VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
                        (r["kirje_id"], r["tarnija"], r["arve_nr"], r["arve_kp"],
                         euro_to_cents(r["neto"]), euro_to_cents(r["km"]),
                         euro_to_cents(r["kokku"]), r["kulukeskus"],
                         r["staatus"], r["kontrollid"], sha256))
        con.execute("INSERT OR REPLACE INTO demo_import VALUES (?,?,?)",
                    (sha256, VERSION, len(rows)))


def save_excel(rows: list[dict[str, str]], report: dict) -> bool:
    try:
        from openpyxl import Workbook
        from openpyxl.styles import Font, PatternFill
        from openpyxl.utils import get_column_letter
    except ImportError:
        return False
    wb = Workbook()
    ws = wb.active
    ws.title = "Kontrollid"
    columns = FIELDS + ["kontrollid", "staatus"]
    ws.append(columns)
    for r in rows:
        ws.append([r[c] for c in columns])
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions
    for cell in ws[1]:
        cell.font = Font(color="FFFFFF", bold=True)
        cell.fill = PatternFill("solid", fgColor="1F4E78")
    for col in ws.columns:
        max_len = max(len(str(cell.value or "")) for cell in col)
        ws.column_dimensions[get_column_letter(col[0].column)].width = min(max_len + 2, 60)
    overview = wb.create_sheet("Kokkuvote")
    overview.append(["NAIDISANDMED", "Ei ole ametlikud finantsandmed"])
    overview.append(["Kirjeid", report["kirjeid"]])
    overview.append(["Vajab ülevaatust", report["vajab_ulevaatust"]])
    overview.append(["Mõõdik", "Arv"])
    for key, val in report["reeglite_loendur"].items():
        overview.append([key, val])
    overview.column_dimensions["A"].width = 42
    overview.column_dimensions["B"].width = 56
    wb.save(OUT / "tuleviku_kontroll.xlsx")
    return True


def main() -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    source = DATA / "tuleviku_naidisarved.csv"
    rows = make_demo_rows()
    with source.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, delimiter=";")
        writer.writeheader()
        writer.writerows(rows)
    source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    checked = validate_rows(rows)
    report = build_report(checked)
    report["source_sha256"] = source_hash
    with (OUT / "tuleviku_kontrollid.csv").open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS + ["kontrollid", "staatus"], delimiter=";")
        writer.writeheader()
        writer.writerows(checked)
    (OUT / "tuleviku_kokkuvote.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    save_sqlite(checked, source_hash)
    xlsx_ok = save_excel(checked, report)
    print(f"Töödeldud sünteetilisi arveid: {len(rows)}")
    print(f"Käsitsi ülevaatust vajab: {report['vajab_ulevaatust']}")
    print(f"Kontrollide loendur: {report['reeglite_loendur']}")
    print(f"Tulemused: {OUT}")
    print("Exceli fail:", "loodud" if xlsx_ok else "openpyxl puudub (CSV ja JSON loodud)")


if __name__ == "__main__":
    main()
