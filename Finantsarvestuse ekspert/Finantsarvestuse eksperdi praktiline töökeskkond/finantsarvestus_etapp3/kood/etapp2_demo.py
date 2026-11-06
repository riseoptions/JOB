"""Käivita Thonnys F5 või terminalis. Iga käivitus loob eraldi demo kausta."""
import json
import sqlite3
from datetime import datetime,timezone
from pathlib import Path
from menetlus import *
from loo_etapp2_naidised import generate

def run_demo(output_parent=None):
    parent=Path(output_parent) if output_parent else ROOT/'valjund/etapp2'
    out=parent/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S_%fZ')
    out.mkdir(parents=True,exist_ok=False)
    c=connect(out/'finantsarvestus.sqlite');initialize(c)
    rows=generate();import_rows(c,rows)
    as_of='2026-11-05'
    for r in c.execute('SELECT document_id FROM input_document').fetchall():validate(c,r[0],as_of)
    id='DEMO-001'
    transition(c,id,'ESITA','analuutik',as_of,'Teenuse periood september; maksetähtaeg möödas, makseinfo vajab eraldi kontrolli')
    transition(c,id,'KOOSKOLASTA','sisukinnitaja',as_of,'Õppesimulatsioon: septembri IT-teenus on vastu võetud')
    transition(c,id,'KINNITA','eelarvejuht',as_of,'Õppesimulatsioon: kuluallikas kontrollitud; septembri periood kinnitatud')
    payload=export_transfer(c,id,'analuutik',as_of,'Õppesimulatsioon: hoiatused üle vaadatud, edastan näidiskande jaoks')
    (out/'rtk_valjuv.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')
    ref=accept_transfer(c,payload,'rtk_demo',as_of)
    (out/'rtk_vastus.json').write_text(json.dumps({'simulation':True,'transfer_id':payload['transfer_id'],'status':'KAJASTATUD','external_reference':ref},ensure_ascii=False,indent=2),encoding='utf-8')
    # Teine dokument näitab tagastamist, ilma parandatud andmete väljamõtlemiseta.
    transition(c,'DEMO-003','ESITA','analuutik',as_of,'Õppenäite tähtaja hoiatus on üle vaadatud')
    transition(c,'DEMO-003','TAGASTA','sisukinnitaja',as_of,'Õppesimulatsioon: teenuse vastuvõtu kinnitus vajab täiendamist')
    export_csv(c,out/'kontrollitulemused.csv',LATEST_ISSUES)
    export_csv(c,out/'menetluslogi.csv','SELECT * FROM document_event ORDER BY event_id')
    export_csv(c,out/'kanded.csv','SELECT e.entry_id,e.invoice_id,e.posting_date,l.account,l.debit_cents,l.credit_cents FROM journal_entry e JOIN journal_line l USING(entry_id) ORDER BY l.line_id')
    totals={s:c.execute('SELECT COUNT(*) FROM input_document WHERE status=?',(s,)).fetchone()[0] for s in ['SISEND','TAGASTATUD','KAJASTATUD']}
    result={'as_of':as_of,'documents':len(rows),'status_counts':totals,'journal_entries':c.execute('SELECT COUNT(*) FROM journal_entry').fetchone()[0],
            'foreign_key_errors':len(c.execute('PRAGMA foreign_key_check').fetchall()),'integrity':c.execute('PRAGMA integrity_check').fetchone()[0],
            'simulation':True,'payments_executed':False}
    (out/'tulemus.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    c.close();print(json.dumps(result,ensure_ascii=False,indent=2));print('Väljund:',out)
    return out

if __name__=='__main__':run_demo()
