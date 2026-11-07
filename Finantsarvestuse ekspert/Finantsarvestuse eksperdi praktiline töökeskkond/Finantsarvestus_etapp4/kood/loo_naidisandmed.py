"""Fikseeritud sünteetiline sisend tulevasele 2. etapile. Ei menetle arveid."""
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from etapp1 import write_csv

ROOT=Path(__file__).resolve().parents[1]

def generate(root=ROOT):
    rows=[]
    cases=[('IT hooldus','1000.00','0.24','DEMO_IT'),('Kontoritarbed','125.55','0.24','DEMO_HALDUS'),
           ('Ruumide hooldus','750.00','0.24','DEMO_HALDUS'),('Raamatud','200.00','0.09','DEMO_OPE'),
           ('IT litsents','499.99','0.24','DEMO_IT'),('Tõlketeenus','360.00','0.24','DEMO_OPE')]
    for i,(label,net,rate,center) in enumerate(cases,1):
        vat=(Decimal(net)*Decimal(rate)).quantize(Decimal('.01'),rounding=ROUND_HALF_UP)
        day=date(2026,10,i+1)
        rows.append(dict(invoice_id=f'DEMO-{i:03}',supplier_id=f'DEMO-T{i:03}',
          supplier_name=f'Näidistarnija {i} (fiktiivne)',invoice_number=f'N-{i:03}',
          invoice_date=day.isoformat(),service_date='2026-09-30' if i==1 else day.isoformat(),
          due_date=(day+timedelta(days=14)).isoformat(),description=label,
          net_cents=int(Decimal(net)*100),vat_rate=rate,vat_cents=int(vat*100),
          gross_cents=int((Decimal(net)+vat)*100),cost_center=center,
          account='DEMO_KULU',status='SISEND',provenance='SUNTEETILINE',
          note='Õppenäide; ei tõenda maksukäsitluse sobivust tegelikule tehingule'))
    write_csv(root/'andmed/sunteetilised/naidisarved.csv',rows)
    return rows

if __name__=='__main__':
    print(f'Loodud {len(generate())} sünteetilist näidisarvet.')
