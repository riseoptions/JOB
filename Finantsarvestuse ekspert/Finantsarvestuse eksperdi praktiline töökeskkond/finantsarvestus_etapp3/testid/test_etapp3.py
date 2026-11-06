import unittest,sys,json,tempfile,csv,sqlite3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'kood'))
from analuus import *
from andmeleping import InvoiceInput,ValidationError
from menetlus import issues_for,read_csv

class Stage3Tests(unittest.TestCase):
    def setUp(self):self.invoice=read_csv(ROOT/'andmed/sunteetilised/naidisarved.csv')[0]
    def test_typed_csv_and_extra_preserved(self):
        m=InvoiceInput.model_validate(dict(self.invoice,extra_column='säilib'))
        self.assertEqual(m.net_cents,100000);self.assertEqual(m.extra_column,'säilib')
        self.assertEqual(m.service_date.isoformat(),'2026-09-30')
        self.assertEqual(self.invoice['net_cents'],'100000')
    def test_no_bool_float_or_negative_cents(self):
        for v in [True,100000.0,-1,'1.5','NaN',10**12+1]:
            with self.subTest(value=v),self.assertRaises(ValidationError):InvoiceInput.model_validate(dict(self.invoice,net_cents=v))
    def test_no_timestamp_date_coercion(self):
        for v in [12345,'2026-09-30T00:00:00','2026-02-30']:
            with self.assertRaises(ValidationError):InvoiceInput.model_validate(dict(self.invoice,service_date=v))
    def test_boundary_integrated_in_old_engine(self):
        self.assertIn('ANDMEKUJU',{r['code'] for r in issues_for(dict(self.invoice,supplier_name=['nimi']),'2026-11-05')})
    def test_original_error_not_replaced(self):
        codes={r['code'] for r in issues_for(dict(self.invoice,net_cents='1.5'),'2026-11-05')}
        self.assertIn('RAHA_TYYP',codes);self.assertNotIn('ANDMEKUJU',codes)
    def test_budget_reconciles_and_signs(self):
        r=read_budget();self.assertEqual(r[0]['actual_cents'],77260000700)
        self.assertEqual(r[0]['budget_cents'],120752383300)
        self.assertEqual(sum(x['actual_cents'] for x in r[1:]),r[0]['actual_cents'])
    def test_zero_and_missing_budget(self):
        self.assertIsNone(budget_metrics(0,0,100)['usage'])
        self.assertEqual(budget_metrics(0,0,100)['remaining_cents'],-100)
        with self.assertRaises(ValueError):budget_metrics(0,None,100)
    def test_polars_pandas_equivalence(self):
        p=ROOT/'andmed/toodeldud/htm_taitmine_2026.csv'
        self.assertEqual(aggregate_months(p),aggregate_months(p,'pandas'))
        self.assertEqual(sum(x['amount_cents'] for x in aggregate_months(p)),88618428861)
    def test_missing_duplicate_month_fails_both(self):
        rows=read_csv(ROOT/'andmed/toodeldud/htm_taitmine_2026.csv')
        for variant in [rows+[rows[0]], [dict(r,amount_cents='') if r==rows[0] else r for r in rows],rows[1:]]:
            with tempfile.TemporaryDirectory() as d:
                from etapp1 import write_csv
                p=Path(d)/'data.csv';write_csv(p,variant)
                for engine in ['polars','pandas']:
                    with self.assertRaises(ValueError):aggregate_months(p,engine)
    def test_year_comparison_no_crosscut(self):
        r=year_comparison(ROOT/'andmed/toodeldud/htm_taitmine_2026.csv')
        self.assertEqual(len(r),8);self.assertEqual(r[0]['previous_cents'],81677061904)
        self.assertEqual(sum(x['current_cents'] for x in r[1:]),r[0]['current_cents'])
    def test_grant_cap_recovery_zero_budget(self):
        rows=json.loads((ROOT/'andmed/sunteetilised/etapp3_toetused.json').read_text())
        r=[grant_result(x) for x in rows]
        self.assertEqual(r[0]['payable_cents'],200000);self.assertEqual(r[1]['recoverable_cents'],60000)
        self.assertEqual(r[2]['earned_cents'],5000);self.assertIsNone(r[2]['variance'])
    def test_grant_invalid_eligible_rate_rounding(self):
        r=dict(id='X',budget_cents=1,actual_cents=1,eligible_cents=1,ceiling_cents=1,advance_cents=0,rate='0.5')
        self.assertEqual(grant_result(r)['earned_cents'],1)
        for change in [dict(eligible_cents=2),dict(rate='NaN'),dict(rate='1.1'),dict(actual_cents=True)]:
            with self.assertRaises(ValidationError):grant_result(dict(r,**change))
    def test_sql_matches_python(self):
        b=read_budget();g=[grant_result(x) for x in json.loads((ROOT/'andmed/sunteetilised/etapp3_toetused.json').read_text())]
        c=save_sql(':memory:',b,aggregate_months(ROOT/'andmed/toodeldud/htm_taitmine_2026.csv'),g)
        self.assertEqual(c.execute("SELECT remaining_cents FROM budget_report WHERE level='koond'").fetchone()[0],b[0]['remaining_cents'])
        self.assertEqual(c.execute("SELECT recoverable_cents FROM grant_report WHERE id='TOETUS-002'").fetchone()[0],60000)
        with self.assertRaises(sqlite3.IntegrityError):c.execute("INSERT INTO monthly_actual VALUES('2026-01-01',1)")
        c.close()

    def test_wrong_comparison_period_rejected(self):
        rows=read_csv(ROOT/'andmed/toodeldud/htm_taitmine_2026.csv')
        for change in [dict(period_end='2026-08-31'),dict(measure='muu')]:
            variant=[dict(r,**change) if r['cell']=='N137' else r for r in rows]
            with tempfile.TemporaryDirectory() as d:
                from etapp1 import write_csv
                p=Path(d)/'data.csv';write_csv(p,variant)
                with self.assertRaises(ValueError):year_comparison(p)
    def test_workbook_and_report_use_changed_input(self):
        from etapp3_demo import workbook_report
        import openpyxl
        b=read_budget();path=ROOT/'andmed/toodeldud/htm_taitmine_2026.csv'
        rows=json.loads((ROOT/'andmed/sunteetilised/etapp3_toetused.json').read_text())
        rows[0]['advance_cents']=850000;rows[0]['rate']='0.75'
        g=[grant_result(x) for x in rows]
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'test.xlsx'
            workbook_report(p,b,aggregate_months(path),year_comparison(path),g,json.loads((ROOT/'andmed/allikaregister.json').read_text()))
            w=openpyxl.load_workbook(p,data_only=True)
            self.assertEqual(w['Toetused']['J6'].value,1000)
            self.assertIn('75%',w['Toetused']['A14'].value)
            self.assertIsNone(w['Toetused']['E8'].value)
            self.assertEqual(w['Eelarve']['D6'].value,772600007)
            w.close()
