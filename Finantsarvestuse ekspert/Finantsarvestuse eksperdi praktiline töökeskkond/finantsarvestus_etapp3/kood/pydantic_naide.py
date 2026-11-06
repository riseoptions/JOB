from pathlib import Path
from andmeleping import InvoiceInput, ValidationError
from menetlus import read_csv, issues_for
ROOT=Path(__file__).resolve().parents[1]
r=read_csv(ROOT/'andmed/sunteetilised/naidisarved.csv')[0]
m=InvoiceInput.model_validate(r)
print('Tüübitud netosumma:',m.net_cents,type(m.net_cents).__name__)
print('Teenuse kuupäev:',m.service_date)
print('Ärireeglite tulemus:',issues_for(r,'2026-11-05'))
try:InvoiceInput.model_validate(dict(r,net_cents=True))
except ValidationError as exc:print('Oodatud tüübiviga:',exc.errors()[0]['msg'])
