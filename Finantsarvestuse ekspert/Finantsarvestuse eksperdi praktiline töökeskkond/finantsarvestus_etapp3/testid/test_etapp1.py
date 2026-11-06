import unittest, sys, tempfile, shutil, json
from pathlib import Path
from decimal import Decimal
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'kood'))
from etapp1 import cents,build
from loo_naidisandmed import generate

class Etapp1Tests(unittest.TestCase):
    def test_currency_and_rounding(self):
        self.assertEqual(cents(-1176947.117,1000),-117694711700)
        self.assertEqual(cents(Decimal('1.005')),101)
        self.assertEqual(cents(Decimal('-1.005')),-101)
    def test_missing_is_not_zero(self):
        self.assertIsNone(cents('-'))
        self.assertIsNone(cents(None))
        self.assertEqual(cents(0),0)
        with self.assertRaises(ValueError): cents('vigane')
    def test_real_source_reconciliation(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);shutil.copytree(ROOT/'andmed',p/'andmed')
            r=build(p)
            self.assertEqual(r['budget_records'],34)
            self.assertEqual(r['actual_records'],99)
            self.assertTrue(all(x['status']=='OK' for x in r['reconciliation']))
            self.assertEqual(r['reconciliation'][0]['stated_ytd_cents'],88618428861)
            self.assertFalse(r['comparison_allowed'])
    def test_changed_source_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);shutil.copytree(ROOT/'andmed',p/'andmed')
            f=p/'andmed/algandmed/re2026_seadus.xlsx'
            f.write_bytes(f.read_bytes()+b'changed')
            with self.assertRaises(ValueError):build(p)
    def test_synthetic_is_reproducible(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);a=generate(p);b=generate(p)
            self.assertEqual(a,b)
            self.assertEqual(len(a),6)
            self.assertTrue(all(x['net_cents']+x['vat_cents']==x['gross_cents'] for x in a))
            self.assertTrue(all(x['provenance']=='SUNTEETILINE' for x in a))
            self.assertEqual(a[0]['gross_cents'],124000)

if __name__=='__main__': unittest.main()
