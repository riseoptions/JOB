import unittest,sys,io,csv,json,base64
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'kood'))
from veeb_adapter import WebSession,parse_input,export_table,MAX_BYTES
from menetlus import read_csv
import openpyxl

class WebTests(unittest.TestCase):
 def setUp(self):
  self.row=read_csv(ROOT/'andmed/sunteetilised/naidisarved.csv')[0]
  self.s=WebSession([self.row],'2026-11-06')
 def tearDown(self):self.s.close()
 def csv(self,rows):
  f=io.StringIO();w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter=';');w.writeheader();w.writerows(rows);return f.getvalue().encode('utf-8-sig')
 def test_import_add_and_idempotent(self):
  r=dict(self.row,invoice_id='NEW',invoice_number='NEW')
  b=self.csv([r]);self.assertEqual(self.s.import_file(b,'csv')['checked'],2)
  self.assertEqual(self.s.import_file(b,'csv')['checked'],2)
 def test_import_duplicate_rechecks_both(self):
  snap=self.s.import_file(self.csv([dict(self.row,invoice_id='COPY')]),'csv')
  self.assertEqual(snap['duplicate_documents'],2)
  self.assertTrue(all(any(i['code']=='DUPLIKAAT' for i in r['issues']) for r in snap['invoices']))
 def test_conflicting_batch_atomic(self):
  rows=[dict(self.row,invoice_id='NEW'),dict(self.row,gross_cents='1')]
  with self.assertRaises(ValueError):self.s.import_file(self.csv(rows),'csv')
  self.assertEqual(self.s.snapshot()['checked'],1)
 def test_bad_headers_and_size(self):
  for text in ['a;b\n1;2','invoice_id;invoice_id\na;b','']:
   with self.assertRaises(ValueError):parse_input(text.encode())
  with self.assertRaises(ValueError):parse_input(b'x'*(MAX_BYTES+1))
 def test_xlsx_real_reader(self):
  w=openpyxl.Workbook();w.active.append(list(self.row));w.active.append(list(self.row.values()))
  b=io.BytesIO();w.save(b)
  self.assertEqual(parse_input(b.getvalue(),'xlsx'),[self.row])
 def test_invalid_provenance_is_blocked(self):
  snap=self.s.import_file(self.csv([dict(self.row,invoice_id='BAD',invoice_number='BAD',provenance='TEGELIK')]),'csv')
  r=next(r for r in snap['invoices'] if r['id']=='BAD')
  self.assertIn('ANDMELIIK',{i['code'] for i in r['issues']});self.assertEqual(r['data_kind'],'SUNTEETILINE_OPPESISEND')
 def test_pydantic_boundary_still_used(self):
  s=WebSession([dict(self.row,supplier_name=['not','text'])],'2026-11-06')
  self.assertIn('ANDMEKUJU',{i['code'] for i in s.snapshot()['invoices'][0]['issues']});s.close()
 def test_selected_export_and_numeric_precision(self):
  data=self.s.export(['DEMO-001'],'xlsx');w=openpyxl.load_workbook(io.BytesIO(data),data_only=False)
  self.assertEqual(w.active['A5'].value,'DEMO-001');self.assertEqual(w.active['C5'].value,'124000')
  self.assertEqual(w.active['E5'].value,'SUNTEETILINE_OPPESISEND')
 def test_csv_formula_injection_neutralized(self):
  b=export_table([dict(id='=1+1',money=100)],'csv')
  rows=list(csv.reader(io.StringIO(b.decode('utf-8-sig')),delimiter=';'))
  self.assertEqual(rows[1],["'=1+1",'100'])
 def test_xlsx_formula_injection_neutralized(self):
  b=export_table([dict(id='=1+1',money=100)],'xlsx')
  w=openpyxl.load_workbook(io.BytesIO(b),data_only=False)
  self.assertEqual(w.active['A5'].data_type,'s');self.assertEqual(w.active['B5'].value,100)
 def test_empty_or_unknown_selection_rejected(self):
  with self.assertRaises(ValueError):self.s.export([],'csv')
  with self.assertRaises(ValueError):self.s.export(['missing'],'csv')
 def test_built_financial_contract(self):
  d=json.loads((ROOT/'dist/data/projekt.json').read_text())
  self.assertEqual(d['budget'][0]['actual_cents'],77260000700)
  self.assertEqual(d['budget'][0]['budget_cents'],120752383300)
  self.assertEqual(sum(r['amount_cents'] for r in d['monthly']),88618428861)
  self.assertEqual(d['invoice_snapshot']['checked'],17)
  self.assertEqual(d['invoice_snapshot']['duplicate_documents'],2)
  self.assertTrue(all(g['provenance']=='SUNTEETILINE' for g in d['grants']))
  self.assertTrue(all(g['provenance']=='TULETATUD' for g in d['budget']))
 def test_worker_uses_identical_business_modules(self):
  for f in ['menetlus.py','andmeleping.py','veeb_adapter.py']:
   self.assertEqual((ROOT/'kood'/f).read_bytes(),(ROOT/'dist/python/kood'/f).read_bytes())

 def test_native_excel_dates(self):
  from datetime import datetime
  r=dict(self.row,invoice_date=datetime(2026,10,2))
  w=openpyxl.Workbook();w.active.append(list(r));w.active.append(list(r.values()))
  b=io.BytesIO();w.save(b)
  self.assertEqual(parse_input(b.getvalue(),'xlsx')[0]['invoice_date'],'2026-10-02')
