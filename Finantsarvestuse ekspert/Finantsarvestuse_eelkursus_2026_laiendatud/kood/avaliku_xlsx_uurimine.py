"""Uuri kohaliku XLSX-i struktuuri, ilma oletamata tabeli päiseid.
Käivita: python kood/avaliku_xlsx_uurimine.py tee_failini.xlsx
"""
import sys
from pathlib import Path

import pandas as pd


def main():
    if len(sys.argv) != 2:
        print('Kasutus: python kood/avaliku_xlsx_uurimine.py "andmed.xlsx"')
        return 2
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"Faili ei leitud: {path}")
        return 2
    excel = pd.ExcelFile(path)
    print(f"Fail: {path.name}; lehti: {len(excel.sheet_names)}")
    for sheet in excel.sheet_names:
        frame = pd.read_excel(excel, sheet_name=sheet, header=None, nrows=8)
        print(f"\n=== Leht: {sheet!r} ===")
        print(frame.fillna("").to_string(index=False, header=False))
    print("\nMärkus: esmalt tuvasta õiged päiseread, ühikud ja aruande metoodika.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
