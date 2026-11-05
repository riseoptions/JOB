"""Vabatahtlik ML-labor: IsolationForest; mudel ei tuvasta pettust.

Paigaldus: python -m pip install scikit-learn
Enne käivita tuleviku_finantslabor.py. Treenib ainult sünteetiliste andmetega.
"""
import csv
from pathlib import Path
from statistics import median

BASE = Path(__file__).resolve().parents[1]
FILE = BASE / "andmed" / "tuleviku_naidisarved.csv"


def main():
    try:
        from sklearn.ensemble import IsolationForest
    except ImportError:
        print("Paigalda esmalt: python -m pip install scikit-learn")
        return
    if not FILE.exists():
        print("Käivita kõigepealt: python kood/tuleviku_finantslabor.py")
        return
    with FILE.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f, delimiter=";"))
    # Siin teadlikult ainult summa tunnus: algõppeks selge, tootmiseks ebapiisav.
    x = [[float(r["kokku"])] for r in rows]
    model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    tags = model.fit_predict(x)
    print("ÕPPEDEMO: ebatavalisena märgitud arved (ei tähenda vale arvet):")
    for row, tag in zip(rows, tags):
        if tag == -1:
            print(row["kirje_id"], row["arve_nr"], row["kokku"], "€")
    print("Tavaline arve mediaan:", round(median(v[0] for v in x), 2), "€")
    print("Ettevaatust: siin kasutati ainult üht tunnust ja sünteetilisi andmeid.")


if __name__ == "__main__":
    main()
