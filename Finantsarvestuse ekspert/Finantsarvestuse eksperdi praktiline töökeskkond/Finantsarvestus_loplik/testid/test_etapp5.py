import unittest,sys,io,csv,zipfile,re
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'kood'))
from veeb_adapter import *
from menetlus import read_csv,issues_for
from analuus import budget_metrics,aggregate_months
class FinalTests(unittest.TestCase):
 def setUp(self):self.row=read_csv(ROOT/'andmed/sunteetilised/naidisarved.csv')[0]
 def csv(self,rows):
  f=io.StringIO();w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter=';');w.writeheader();w.writerows(rows);return f.getvalue().encode()
 def xlsx(self,row):
  w=openpyxl.Workbook();w.active.append(list(row));w.active.append(list(row.values()));b=io.BytesIO();w.save(b);return b.getvalue()
 def issues(self,**kw):return {i['code'] for i in issues_for(dict(self.row,**kw),'2026-11-06')}
 def test_repeat_capacity(self):
  s=WebSession([self.row],'2026-11-06')
  try:
   with patch('veeb_adapter.MAX_ROWS',1):self.assertEqual(s.import_file(self.csv([self.row]),'csv')['checked'],1)
  finally:s.close()
 def test_capacity_atomic(self):
  s=WebSession([self.row],'2026-11-06')
  try:
   with patch('veeb_adapter.MAX_ROWS',1):
    with self.assertRaises(ValueError):s.import_file(self.csv([dict(self.row,invoice_id='NEW')]),'csv')
   self.assertEqual(s.snapshot()['checked'],1)
  finally:s.close()
 def test_500_rows(self):
  self.assertEqual(len(parse_input(self.csv([self.row]*500))),500)
  with self.assertRaises(ValueError):parse_input(self.csv([self.row]*501))
 def test_wide(self):
  with self.assertRaises(ValueError):parse_input((';'.join(str(i) for i in range(65))+'\n').encode())
 def test_dimensions(self):
  b=io.BytesIO()
  with zipfile.ZipFile(io.BytesIO(self.xlsx(self.row))) as src,zipfile.ZipFile(b,'w') as dst:
   for n in src.namelist():
    data=src.read(n)
    if n=='xl/worksheets/sheet1.xml':data=re.sub(rb'<dimension ref="[^"]+"',b'<dimension ref="A1:XFD1048576"',data)
    dst.writestr(n,data)
  with self.assertRaisesRegex(ValueError,'mõõtmete'):parse_input(b.getvalue(),'xlsx')
 def test_expansion(self):
  b=io.BytesIO()
  with zipfile.ZipFile(b,'w',zipfile.ZIP_DEFLATED) as z:z.writestr('xl/a.xml','x'*10_000_001)
  with self.assertRaisesRegex(ValueError,'suur'):parse_input(b.getvalue(),'xlsx')
 def test_xml_entity(self):
  b=io.BytesIO()
  with zipfile.ZipFile(b,'w') as z:z.writestr('xl/a.xml','<!DOCTYPE x [<!ENTITY y "z">]>')
  with self.assertRaisesRegex(ValueError,'XML'):parse_input(b.getvalue(),'xlsx')
 def test_bad_encoding(self):
  with self.assertRaises(ValueError):parse_input(b'\xff')
 def test_bad_xlsx(self):
  with self.assertRaisesRegex(ValueError,'Vigane'):parse_input(b'bad','xlsx')
 def test_formula(self):
  with self.assertRaisesRegex(ValueError,'valemid'):parse_input(self.xlsx(dict(self.row,description='=1+1')),'xlsx')
 def test_export_header_title(self):
  s=openpyxl.load_workbook(io.BytesIO(export_table([{'=1+1':'@a','money':-12}],'xlsx','=2+2'))).active
  for cell in ['A1','A4','A5']:self.assertEqual(s[cell].data_type,'s')
  self.assertEqual(s['B5'].value,-12)
 def test_huge_money(self):self.assertIn('SUMMA_PIIR',self.issues(net_cents='9'*5000))
 def test_bad_date_missing(self):
  self.assertIn('KUUPAEV',self.issues(service_date='2026-02-29'));self.assertIn('PUUDUV_VALI',self.issues(net_cents=''))
 def test_half_cent(self):
  self.assertNotIn('KM_SUMMA',self.issues(net_cents='50',vat_rate='0.13',vat_cents='7',gross_cents='57'))
  self.assertIn('KM_SUMMA',self.issues(net_cents='50',vat_rate='0.13',vat_cents='6',gross_cents='56'))
 def test_period_warning(self):
  r=issues_for(dict(self.row,invoice_date='2026-11-02',service_date='2026-10-31',due_date='2026-11-16'),'2026-11-06')
  self.assertEqual([(i['code'],i['severity']) for i in r],[('PERIOOD','HOIATUS')])
 def test_zero_overspend(self):
  self.assertIsNone(budget_metrics(0,0,100)['usage']);self.assertEqual(budget_metrics(100,100,120)['remaining_cents'],-20)
 def test_missing_bool(self):
  for args in [(100,None,1),(100,100,True)]:
   with self.assertRaises(ValueError):budget_metrics(*args)
 def test_engines(self):
  p=ROOT/'andmed/toodeldud/htm_taitmine_2026.csv';a=aggregate_months(p,'polars');self.assertEqual(a,aggregate_months(p,'pandas'));self.assertEqual(sum(r['amount_cents'] for r in a),88618428861)
 def test_sql(self):
  s=WebSession([dict(self.row,invoice_id="x'; DROP TABLE input_document; --")],'2026-11-06')
  try:
   self.assertEqual(s.snapshot()['checked'],1);self.assertEqual(s.c.execute('pragma integrity_check').fetchone()[0],'ok');self.assertEqual(s.c.execute('pragma foreign_key_check').fetchall(),[])
  finally:s.close()
 def test_other_supplier(self):
  s=WebSession([self.row,dict(self.row,invoice_id='OTHER',supplier_id='OTHER')],'2026-11-06')
  try:self.assertEqual(s.snapshot()['duplicate_documents'],0)
  finally:s.close()
