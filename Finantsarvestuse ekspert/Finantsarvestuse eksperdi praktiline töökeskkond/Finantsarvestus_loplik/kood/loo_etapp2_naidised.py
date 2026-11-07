"""Esimese etapi kuus arvet ja üksteist sihilikku vigast näidet."""
from pathlib import Path
from menetlus import ROOT,read_csv
from etapp1 import write_csv

def generate():
    base=read_csv(ROOT/'andmed/sunteetilised/naidisarved.csv')
    cases=[('VIGA-001',{'supplier_name':''},'PUUDUV_VALI'),
      ('VIGA-002',{'invoice_date':'2026-02-30'},'KUUPAEV'),
      ('VIGA-003',{'gross_cents':'124001'},'SUMMA'),
      ('VIGA-004',{'vat_cents':'23999','gross_cents':'123999'},'KM_SUMMA'),
      ('VIGA-005',{'account':'999999','cost_center':'PUUDUB'},'KONTO,KULUKESKUS'),
      ('VIGA-006',{'net_cents':'-100000'},'RAHA_TYYP'),
      ('VIGA-007',{'supplier_id':' demo-t002 ','invoice_number':' n-002 '},'DUPLIKAAT'),
      ('VIGA-008',{'invoice_date':'2026-12-01','due_date':'2026-12-15'},'TULEVIK'),
      ('VIGA-009',{'due_date':'2026-10-01'},'TAHTAEG'),
      ('VIGA-010',{'provenance':'TEGELIK'},'ANDMELIIK'),
      ('',{'invoice_number':'PUUDUV-ID'},'PUUDUV_VALI')]
    rows=list(base);expected=[]
    for i,(id,changes,codes) in enumerate(cases,1):
        row=dict(base[0]);row.update(invoice_id=id,supplier_id=f'DEMO-V{i:03}',invoice_number=f'V-{i:03}',note='Sihilik kontrollnäide; kõik tehingud fiktiivsed')
        row.update(changes);rows.append(row)
        expected.append(dict(input_id=id or '(puudub)',expected_error_codes=codes))
    write_csv(ROOT/'andmed/sunteetilised/etapp2_sisend.csv',rows)
    write_csv(ROOT/'andmed/sunteetilised/etapp2_oodatud_vead.csv',expected)
    return rows

if __name__=='__main__':print(f'Loodud {len(generate())} sisendrida.')
