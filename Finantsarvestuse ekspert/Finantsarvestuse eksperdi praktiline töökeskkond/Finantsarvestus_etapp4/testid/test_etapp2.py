import unittest,sys,tempfile,json,sqlite3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'kood'))
from menetlus import *

class Etapp2Tests(unittest.TestCase):
    def setUp(self):
        self.c=connect(':memory:');initialize(self.c)
        self.r=read_csv(ROOT/'andmed/sunteetilised/naidisarved.csv')[0]
        import_rows(self.c,[self.r]);self.day='2026-11-05';self.reason='Teenuse ja tähtaja hoiatused on õppenäites läbi vaadatud'
    def tearDown(self):self.c.close()
    def ready(self):
        for action,actor in [('ESITA','analuutik'),('KOOSKOLASTA','sisukinnitaja'),('KINNITA','eelarvejuht')]:transition(self.c,'DEMO-001',action,actor,self.day,self.reason)
    def codes(self,**changes):return {i['code'] for i in issues_for(dict(self.r,**changes),self.day)}
    def test_missing_and_invalid_date(self):
        self.assertIn('PUUDUV_VALI',self.codes(supplier_name=''))
        self.assertIn('KUUPAEV',self.codes(invoice_date='2026-02-30'))
    def test_money_rounding_and_bad_types(self):
        self.assertIn('SUMMA',self.codes(gross_cents='124001'))
        self.assertIn('RAHA_TYYP',self.codes(net_cents='1.5'))
        self.assertIn('RAHA_TYYP',self.codes(net_cents='-1'))
        self.assertNotIn('KM_SUMMA',self.codes(net_cents='49999',vat_cents='12000',gross_cents='61999'))
        self.assertIn('KM_SUMMA',self.codes(vat_cents='23999'))
    def test_rate_and_dimensions(self):
        for x in ['NaN','Infinity','0.22','abc']:self.assertIn('KM_MAAR',self.codes(vat_rate=x))
        self.assertIn('KONTO',self.codes(account='X'))
        self.assertIn('KULUKESKUS',self.codes(cost_center='X'))
    def test_dates_and_provenance(self):
        self.assertIn('ULETAHTAJA',self.codes())
        self.assertNotIn('ULETAHTAJA',self.codes(due_date=self.day))
        self.assertIn('TAHTAEG',self.codes(due_date='2026-09-01'))
        self.assertIn('TULEVIK',self.codes(service_date='2027-01-01'))
        self.assertIn('ANDMELIIK',self.codes(provenance='TEGELIK'))
    def test_import_idempotent_and_atomic_conflict(self):
        self.assertEqual(import_rows(self.c,[self.r]),0)
        with self.assertRaises(ValueError):import_rows(self.c,[dict(self.r,invoice_id='NEW'),dict(self.r,gross_cents='9')])
        self.assertEqual(self.c.execute('SELECT count(*) FROM input_document').fetchone()[0],1)
    def test_missing_id_preserved_and_blocked(self):
        import_rows(self.c,[dict(self.r,invoice_id='')])
        id=self.c.execute("SELECT document_id FROM input_document WHERE document_id LIKE 'PUUDUV-%'").fetchone()[0]
        self.assertIn('PUUDUV_VALI',{x['code'] for x in validate(self.c,id,self.day)})
    def test_duplicate_both_sides(self):
        import_rows(self.c,[dict(self.r,invoice_id='COPY',supplier_id=' demo-t001 ',invoice_number=' n-001 ')])
        for id in ['DEMO-001','COPY']:self.assertIn('DUPLIKAAT',{x['code'] for x in validate(self.c,id,self.day)})
    def test_blocked_and_wrong_role(self):
        with self.assertRaises(ValueError):transition(self.c,'DEMO-001','KINNITA','eelarvejuht',self.day,self.reason)
        with self.assertRaises(ValueError):transition(self.c,'DEMO-001','ESITA','rtk_demo',self.day,self.reason)
        with self.assertRaises(ValueError):transition(self.c,'DEMO-001','ESITA','analuutik',self.day,'')
    def test_full_flow_balanced_and_idempotent_receipt(self):
        self.ready();p=export_transfer(self.c,'DEMO-001','analuutik',self.day,self.reason)
        a=accept_transfer(self.c,p,'rtk_demo',self.day);b=accept_transfer(self.c,p,'rtk_demo',self.day)
        self.assertEqual(a,b)
        self.assertEqual(document(self.c,'DEMO-001')['status'],'KAJASTATUD')
        self.assertEqual(self.c.execute('SELECT count(*) FROM journal_entry').fetchone()[0],1)
        self.assertEqual(self.c.execute('SELECT sum(debit_cents)-sum(credit_cents) FROM journal_line').fetchone()[0],0)
        self.assertEqual(self.c.execute('SELECT posting_date FROM journal_entry').fetchone()[0],'2026-09-30')
        self.assertEqual(self.c.execute('PRAGMA foreign_key_check').fetchall(),[])
    def test_payload_tampering_no_posting(self):
        self.ready();p=export_transfer(self.c,'DEMO-001','analuutik',self.day,self.reason)
        p['invoice']['gross_cents']='1'
        with self.assertRaises(ValueError):accept_transfer(self.c,p,'rtk_demo',self.day)
        self.assertEqual(self.c.execute('SELECT count(*) FROM journal_entry').fetchone()[0],0)
    def test_new_duplicate_blocks_previously_approved(self):
        self.ready();import_rows(self.c,[dict(self.r,invoice_id='COPY')])
        with self.assertRaises(ValueError):export_transfer(self.c,'DEMO-001','analuutik',self.day,self.reason)
        self.assertEqual(document(self.c,'DEMO-001')['status'],'KINNITATUD')
    def test_return_and_audit_immutable(self):
        transition(self.c,'DEMO-001','ESITA','analuutik',self.day,self.reason)
        transition(self.c,'DEMO-001','TAGASTA','sisukinnitaja',self.day,'Puudub teenuse vastuvõtu kinnitus')
        self.assertEqual(document(self.c,'DEMO-001')['status'],'TAGASTATUD')
        with self.assertRaises(sqlite3.IntegrityError):self.c.execute('DELETE FROM document_event')
        self.c.rollback()
        with self.assertRaises(sqlite3.IntegrityError):self.c.execute("UPDATE document_event SET reason='x'")
    def test_correction_preserves_source_and_removes_old_duplicate(self):
        old=document(self.c,'DEMO-001')['raw_json']
        new=dict(self.r,invoice_id='DEMO-001-R2',description='Parandatud teenuse kirjeldus')
        id=replace_document(self.c,'DEMO-001',new,'analuutik','Täpsustatud teenuse sisu vastuvõtuakti põhjal')
        self.assertEqual(document(self.c,'DEMO-001')['raw_json'],old)
        self.assertEqual(document(self.c,'DEMO-001')['status'],'ASENDATUD')
        self.assertEqual(document(self.c,id)['revision'],2)
        self.assertNotIn('DUPLIKAAT',{x['code'] for x in validate(self.c,id,self.day)})
        with self.assertRaises(ValueError):transition(self.c,'DEMO-001','ESITA','analuutik',self.day,self.reason)
    def test_posting_failure_rolls_back(self):
        self.ready();p=export_transfer(self.c,'DEMO-001','analuutik',self.day,self.reason)
        self.c.execute("CREATE TRIGGER fail_line BEFORE INSERT ON journal_line BEGIN SELECT RAISE(ABORT,'test'); END")
        with self.assertRaises(sqlite3.IntegrityError):accept_transfer(self.c,p,'rtk_demo',self.day)
        self.assertEqual(self.c.execute('SELECT count(*) FROM journal_entry').fetchone()[0],0)
        self.assertEqual(document(self.c,'DEMO-001')['status'],'EDASTATUD')
    def test_export_retry_returns_same_payload(self):
        self.ready();a=export_transfer(self.c,'DEMO-001','analuutik',self.day,self.reason)
        b=export_transfer(self.c,'DEMO-001','analuutik',self.day,self.reason)
        self.assertEqual(a,b)
        self.assertEqual(self.c.execute('SELECT count(*) FROM transfer').fetchone()[0],1)
    def test_entire_fixture_expected_errors(self):
        c=connect(':memory:');initialize(c)
        rows=read_csv(ROOT/'andmed/sunteetilised/etapp2_sisend.csv')
        import_rows(c,rows)
        for expected in read_csv(ROOT/'andmed/sunteetilised/etapp2_oodatud_vead.csv'):
            id=expected['input_id']
            if id=='(puudub)':id=c.execute("SELECT document_id FROM input_document WHERE document_id LIKE 'PUUDUV-%'").fetchone()[0]
            codes={x['code'] for x in validate(c,id,self.day) if x['severity']=='VIGA'}
            self.assertEqual(codes,set(expected['expected_error_codes'].split(',')),id)
        c.close()
    def test_schema_reopen(self):
        initialize(self.c)
        self.assertEqual(self.c.execute('SELECT version FROM schema_version').fetchone()[0],'0.2')

if __name__=='__main__':unittest.main()
