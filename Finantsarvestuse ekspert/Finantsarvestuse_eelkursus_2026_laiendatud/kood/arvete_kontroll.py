"""Sünteetiliste näidisarvete kontroll: CSV -> Decimal -> SQLite + XLSX.

See ei sisalda maksualast otsustusloogikat ega ametlikku RTK töövoogu.
Käivita projekti suvalisest kataloogist: python kood/arvete_kontroll.py
"""
from __future__ import annotations

import csv
import sqlite3
from collections import Counter, defaultdict
from datetime import date
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "andmed" / "naidisarved.csv"
OUTPUT = ROOT / "valjund"
FIELDS = ["arve_nr", "tarnija", "arve_kp", "tahtaeg", "neto", "km_maar", "km", "kokku", "kulukeskus", "teenuse_periood"]
EURO = Decimal("0.01")


def raha(value: str | Decimal) -> Decimal:
    """Kasuta finantsandmetes kümnendarve, ümarda sentidesse."""
    try:
        return Decimal(str(value).strip()).quantize(EURO, rounding=ROUND_HALF_UP)
    except (InvalidOperation, ValueError) as exc:
        raise ValueError(f"Vigane rahasumma: {value!r}") from exc


def read_rows(path: Path = DATA) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")
        missing = set(FIELDS) - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Puuduvad väljad: {sorted(missing)}")
        return [{key: (value or "").strip() for key, value in row.items()} for row in reader]


def check_row(row: dict[str, str]) -> list[str]:
    errors: list[str] = []
    if not row.get("arve_nr") or not row.get("tarnija"):
        errors.append("TUNNUS_PUUDUB")
    if not row.get("kulukeskus"):
        errors.append("KULUKESKUS_PUUDUB")
    for field in ("arve_kp", "tahtaeg"):
        try:
            date.fromisoformat(row[field])
        except (KeyError, ValueError, TypeError):
            errors.append("VIGANE_KUUPAEV")
            break
    try:
        neto, km, total = (raha(row[key]) for key in ("neto", "km", "kokku"))
        if neto + km != total:
            errors.append("SUMMA_EI_KLAPI")
        rate = Decimal(row["km_maar"])
        if rate == 24 and raha(neto * rate / Decimal(100)) != km:
            errors.append("KM_EI_KLAPI")
    except (ValueError, KeyError, InvalidOperation):
        errors.append("SUMMA_VOI_KM_VIGANE")
    return errors


def validate(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    keys = Counter((r.get("tarnija", "").lower(), r.get("arve_nr", "").lower()) for r in rows)
    result: list[dict[str, str]] = []
    for row in rows:
        errors = check_row(row)
        key = (row.get("tarnija", "").lower(), row.get("arve_nr", "").lower())
        if key[0] and key[1] and keys[key] > 1:
            errors.append("VOIMALIK_DUPLIKAAT")
        result.append({**row, "vead": ", ".join(errors), "staatus": "KONTROLLI" if errors else "OK"})
    return result


def write_sqlite(rows: list[dict[str, str]], path: Path) -> None:
    with sqlite3.connect(path) as con:
        con.execute("DROP TABLE IF EXISTS arved")
        con.execute("""CREATE TABLE arved (
            id INTEGER PRIMARY KEY, arve_nr TEXT, tarnija TEXT, arve_kp TEXT,
            tahtaeg TEXT, neto TEXT, km_maar TEXT, km TEXT, kokku TEXT,
            kulukeskus TEXT, teenuse_periood TEXT, staatus TEXT, vead TEXT)""")
        columns = FIELDS + ["staatus", "vead"]
        marks = ", ".join(["?"] * len(columns))
        con.executemany(
            f"INSERT INTO arved ({', '.join(columns)}) VALUES ({marks})",
            [[r.get(col, "") for col in columns] for r in rows]
        )


def write_csv(rows: list[dict[str, str]], path: Path) -> None:
    columns = FIELDS + ["staatus", "vead"]
    with path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columns, delimiter=";")
        writer.writeheader()
        writer.writerows(rows)


def write_excel(rows: list[dict[str, str]], path: Path) -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Arvete kontroll"
    columns = FIELDS + ["staatus", "vead"]
    ws.append(columns)
    for row in rows:
        ws.append([row.get(c, "") for c in columns])
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions
    for cell in ws[1]:
        cell.font = Font(color="FFFFFF", bold=True)
        cell.fill = PatternFill("solid", fgColor="1B365D")
    for col, width in {"A": 16, "B": 23, "C": 14, "D": 14, "E": 14, "F": 13,
                       "G": 12, "H": 14, "I": 16, "J": 18, "K": 13, "L": 48}.items():
        ws.column_dimensions[col].width = width
    for i, row in enumerate(rows, start=2):
        if row["staatus"] == "KONTROLLI":
            ws.cell(i, 11).fill = PatternFill("solid", fgColor="FFF0C2")

    summary = wb.create_sheet("Kokkuvõte")
    summary.append(["Kulukeskus", "Arvete arv", "Kogusumma EUR (kontrollimata ridu sh)"])
    sums: dict[str, Decimal] = defaultdict(lambda: Decimal("0.00"))
    counts: Counter[str] = Counter()
    for row in rows:
        center = row["kulukeskus"] or "(puudub)"
        counts[center] += 1
        try:
            sums[center] += raha(row["kokku"])
        except ValueError:
            pass
    for center in sorted(counts):
        summary.append([center, counts[center], float(sums[center])])
    summary.append([])
    summary.append(["Tähelepanu: koond sisaldab ka vigaseid ja võimalikke kordusarveid."])
    summary.append(["See ei ole kinnitatud finantsaruanne. Kõik andmed on sünteetilised."])
    for cell in summary[1]:
        cell.font = Font(bold=True)
    summary.column_dimensions["A"].width = 25
    summary.column_dimensions["B"].width = 18
    summary.column_dimensions["C"].width = 50
    for row in summary.iter_rows(min_row=2, min_col=3, max_col=3):
        row[0].number_format = '#,##0.00 "€"'
    wb.save(path)


def main() -> None:
    OUTPUT.mkdir(exist_ok=True)
    records = validate(read_rows())
    write_sqlite(records, OUTPUT / "arved.sqlite")
    write_csv(records, OUTPUT / "kontroll_raport.csv")
    write_excel(records, OUTPUT / "arvete_kontroll.xlsx")
    flagged = sum(bool(row["vead"]) for row in records)
    print(f"Kontrollitud arveid: {len(records)}; kontrolli vajab: {flagged}")
    print("Tulemused:", OUTPUT)
    for row in records:
        if row["vead"]:
            print(f"  {row['arve_nr']} / {row['tarnija']}: {row['vead']}")


if __name__ == "__main__":
    main()
