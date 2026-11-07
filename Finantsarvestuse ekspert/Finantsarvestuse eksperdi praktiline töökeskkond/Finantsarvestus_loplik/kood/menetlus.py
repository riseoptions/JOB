"""Etapi 2 lokaalne õppesimulatsioon. Ei ühendu RTK, SAP-i ega pangaga."""
import csv
import hashlib
import json
import re
import sqlite3
from datetime import date, datetime, timezone
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
RULE_VERSION='0.2.1'
from andmeleping import shape_issues
CENTERS={'DEMO_IT','DEMO_HALDUS','DEMO_OPE'}
ACCOUNTS={'DEMO_KULU'}
RATES={Decimal('0'),Decimal('0.09'),Decimal('0.13'),Decimal('0.24')}
REQUIRED=['invoice_id','supplier_id','supplier_name','invoice_number','invoice_date','service_date',
          'due_date','description','net_cents','vat_rate','vat_cents','gross_cents','cost_center','account','provenance']


def now(): return datetime.now(timezone.utc).isoformat()
def canonical(obj): return json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(',',':'))
def digest(text): return hashlib.sha256(text.encode('utf-8')).hexdigest()
def normalized(s): return ' '.join(str(s).split()).casefold()


def connect(path):
    c=sqlite3.connect(path)
    c.row_factory=sqlite3.Row
    c.execute('PRAGMA foreign_keys=ON')
    return c


def initialize(c):
    version=c.execute("SELECT name FROM sqlite_master WHERE name='schema_version'").fetchone()
    if not version: c.executescript((ROOT/'sql/001_skeem.sql').read_text(encoding='utf-8'))
    v=c.execute('SELECT version FROM schema_version').fetchone()[0]
    if v=='0.1':c.executescript((ROOT/'sql/002_menetlus.sql').read_text(encoding='utf-8'))
    elif v!='0.2':raise ValueError('Tundmatu skeemiversioon')


def authorize(c,actor,role):
    row=c.execute('SELECT role FROM actor WHERE actor_id=?',(actor,)).fetchone()
    if not row or row[0]!=role:raise ValueError('Selle toimingu jaoks puudub näidisrolli õigus')


def document(c,id):
    row=c.execute('SELECT * FROM input_document WHERE document_id=?',(id,)).fetchone()
    if not row:raise ValueError('Dokumenti ei leitud')
    return row


def log(c,id,actor,action,old,new,reason):
    c.execute('INSERT INTO document_event(document_id,actor_id,occurred_at,action,old_status,new_status,reason) VALUES(?,?,?,?,?,?,?)',
              (id,actor,now(),action,old,new,reason))


def import_rows(c,rows,actor='analuutik'):
    """Kogu partii atomaarne. Sama ID+sisu ei dubleeru; muutunud sisu lükatakse tagasi."""
    authorize(c,actor,'ANALUUTIK')
    added=0
    with c:
        for r in rows:
            raw=canonical(r);h=digest(raw)
            id=str(r.get('invoice_id','')).strip() or 'PUUDUV-'+h[:16]
            old=c.execute('SELECT content_hash FROM input_document WHERE document_id=?',(id,)).fetchone()
            if old:
                if old[0]!=h:raise ValueError(f'{id}: sama ID all erinev sisu; kasuta uut parandusdokumendi ID-d')
                continue
            c.execute('INSERT INTO input_document(document_id,raw_json,content_hash,creator_actor,imported_at) VALUES(?,?,?,?,?)',(id,raw,h,actor,now()))
            log(c,id,actor,'IMPORT','PUUDUB','SISEND','Sünteetiline CSV-sisend')
            added+=1
    return added


def read_csv(path):
    with Path(path).open(encoding='utf-8-sig',newline='') as f:
        return list(csv.DictReader(f,delimiter=';'))


def issues_for(r,as_of,duplicate=False):
    as_of=date.fromisoformat(as_of)
    issues=[]
    def add(code,field,msg,severity='VIGA'):issues.append(dict(code=code,field=field,message=msg,severity=severity))
    for field in REQUIRED:
        if not str(r.get(field,'') or '').strip():add('PUUDUV_VALI',field,'Kohustuslik väärtus puudub')
    if r.get('provenance')!='SUNTEETILINE':add('ANDMELIIK','provenance','Lubatud on ainult sünteetilised õppeandmed')
    if r.get('currency','EUR')!='EUR':add('VALUUTA','currency','See versioon toetab ainult EUR-i')
    dates={}
    for field in ['invoice_date','service_date','due_date']:
        text=str(r.get(field,''))
        if text:
            try:
                if not re.fullmatch(r'\d{4}-\d{2}-\d{2}',text):raise ValueError()
                dates[field]=date.fromisoformat(text)
            except ValueError:add('KUUPAEV',field,'Vajalik on kehtiv ISO-kuupäev AAAA-KK-PP')
    if 'invoice_date' in dates and dates['invoice_date']>as_of:add('TULEVIK','invoice_date','Arve kuupäev on kontrollpäevast hilisem')
    if 'service_date' in dates and dates['service_date']>as_of:add('TULEVIK','service_date','Tulevikuteenuse/ettemakse käsitlus ei ole selles versioonis toetatud')
    if all(k in dates for k in ['due_date','invoice_date']) and dates['due_date']<dates['invoice_date']:add('TAHTAEG','due_date','Maksetähtaeg on enne arve kuupäeva')
    if 'due_date' in dates and dates['due_date']<as_of:add('ULETAHTAJA','due_date','Tähtaeg möödas; see ei tõenda tasumata olekut','HOIATUS')
    if all(k in dates for k in ['invoice_date','service_date']) and dates['invoice_date'].strftime('%Y-%m')!=dates['service_date'].strftime('%Y-%m'):
        add('PERIOOD','service_date','Teenuse ja arve kuu erinevad; kinnita õige arvestusperiood','HOIATUS')
    money={}
    for field in ['net_cents','vat_cents','gross_cents']:
        value=str(r.get(field,''))
        if value:
            if not re.fullmatch(r'\d+',value):add('RAHA_TYYP',field,'Vajalik on mittenegatiivne täisarv sentides')
            elif len(value.lstrip('0'))>13 or int(value.lstrip('0') or '0')>10**12:add('SUMMA_PIIR',field,'Õppenäite piir on 10 miljardit eurot')
            else:money[field]=int(value.lstrip('0') or '0')
    if money.get('net_cents')==0:add('NULLARVE','net_cents','Nullarve ei kuulu selle õppesimulatsiooni ulatusse')
    try:
        rate=Decimal(str(r.get('vat_rate','')))
        if not rate.is_finite() or rate not in RATES:raise ValueError()
    except (ValueError,ArithmeticError):
        rate=None;add('KM_MAAR','vat_rate','Lubatud näidismäärad: 0, 0.09, 0.13, 0.24; see pole maksualuse kontroll')
    if len(money)==3 and money['net_cents']+money['vat_cents']!=money['gross_cents']:add('SUMMA','gross_cents','Neto + käibemaks ei võrdu brutoga')
    if rate is not None and all(k in money for k in ['net_cents','vat_cents']):
        expected=int((Decimal(money['net_cents'])*rate).quantize(Decimal('1'),rounding=ROUND_HALF_UP))
        if expected!=money['vat_cents']:add('KM_SUMMA','vat_cents',f'Ühe rea käibemaks peab olema {expected} senti')
    if r.get('account') not in ACCOUNTS:add('KONTO','account','Tundmatu DEMO-konto')
    if r.get('cost_center') not in CENTERS:add('KULUKESKUS','cost_center','Tundmatu DEMO-kulukeskus')
    if duplicate:add('DUPLIKAAT','invoice_number','Sama tarnija ja normaliseeritud arvenumber teises dokumendis')
    # Vana reeglimootor säilitab kõik senised koodid ja kogub vead korraga.
    if not any(i['severity']=='VIGA' for i in issues):
        issues.extend(shape_issues(r))
    return issues


def validate(c,id,as_of):
    row=document(c,id);r=json.loads(row['raw_json'])
    pair=(normalized(r.get('supplier_id','')),normalized(r.get('invoice_number','')))
    duplicate=False
    if all(pair):
        for other in c.execute('SELECT document_id,raw_json FROM input_document WHERE document_id<>? AND status<>"ASENDATUD"',(id,)):
            o=json.loads(other['raw_json'])
            if pair==(normalized(o.get('supplier_id','')),normalized(o.get('invoice_number',''))):duplicate=True;break
    issues=issues_for(r,as_of,duplicate)
    with c:
        run=c.execute('INSERT INTO check_run(document_id,as_of,checked_at,rule_version) VALUES(?,?,?,?)',(id,as_of,now(),RULE_VERSION)).lastrowid
        c.executemany('INSERT INTO validation_issue(run_id,code,severity,field,message) VALUES(?,?,?,?,?)',[(run,i['code'],i['severity'],i['field'],i['message']) for i in issues])
    return issues


def require_clean(c,id,as_of,reason):
    issues=validate(c,id,as_of)
    if any(i['severity']=='VIGA' for i in issues):raise ValueError('Dokumendil on blokeerivad vead')
    if any(i['severity']=='HOIATUS' for i in issues) and len(reason.strip())<10:raise ValueError('Hoiatused vajavad vähemalt 10 märgiga sisulist põhjendust')


def transition(c,id,action,actor,as_of,reason=''):
    """Inimese selgesõnaline toiming; import ega kontroll ei kinnita arvet."""
    rules={'ESITA':('ANALUUTIK',{'SISEND','TAGASTATUD'},'KONTROLLITUD'),
           'KOOSKOLASTA':('SISU',{'KONTROLLITUD'},'KOOSKOLASTATUD'),
           'KINNITA':('EELARVE',{'KOOSKOLASTATUD'},'KINNITATUD'),
           'TAGASTA':('SISU',{'KONTROLLITUD','KOOSKOLASTATUD'},'TAGASTATUD')}
    if action not in rules:raise ValueError('Tundmatu toiming')
    role,allowed,new=rules[action];authorize(c,actor,role);row=document(c,id)
    if row['status'] not in allowed:raise ValueError('Lubamatu olekuüleminek')
    if action in {'KOOSKOLASTA','KINNITA'} and row['creator_actor']==actor:raise ValueError('Koostaja ei kinnita enda dokumenti')
    if len(reason.strip())<10:raise ValueError('Lisa vähemalt 10 märgiga põhjendus')
    if action!='TAGASTA':require_clean(c,id,as_of,reason)
    with c:
        c.execute('UPDATE input_document SET status=? WHERE document_id=?',(new,id))
        c.execute('UPDATE invoice SET status=? WHERE invoice_id=?',(new,id))
        log(c,id,actor,action,row['status'],new,reason)


def export_transfer(c,id,actor,as_of,reason):
    authorize(c,actor,'ANALUUTIK');row=document(c,id)
    if row['status'] in {'EDASTATUD','KAJASTATUD'}:
        existing=c.execute('SELECT payload_json FROM transfer WHERE document_id=?',(id,)).fetchone()
        if existing:return json.loads(existing[0])
    if row['status']!='KINNITATUD':raise ValueError('Edastada saab ainult kinnitatud dokumenti')
    require_clean(c,id,as_of,reason)
    r=json.loads(row['raw_json'])
    tid='DEMO-RTK-'+id
    payload={'schema_version':'0.2','simulation':True,'transfer_id':tid,'invoice_id':id,
             'source_hash':row['content_hash'],'invoice':r,'vat_policy':'MITTE_MAHAARVATAV_OPPENaIDE'}
    raw=canonical(payload)
    with c:
        c.execute('INSERT INTO invoice VALUES(?,?,?,?,?,?,?,?,?,?,?)',(id,r['supplier_id'],r['invoice_number'],r['invoice_date'],r['service_date'],r['due_date'],int(r['net_cents']),int(r['vat_cents']),int(r['gross_cents']),'EDASTATUD','SUNTEETILINE'))
        c.execute('INSERT INTO invoice_line VALUES(?,?,?,?,?,?,?,?)',(id+'-1',id,r['description'],int(r['net_cents']),r['vat_rate'],int(r['vat_cents']),r['account'],r['cost_center']))
        c.execute('INSERT INTO transfer(transfer_id,document_id,payload_json,payload_hash,created_at) VALUES(?,?,?,?,?)',(tid,id,raw,digest(raw),now()))
        c.execute("UPDATE input_document SET status='EDASTATUD' WHERE document_id=?",(id,))
        log(c,id,actor,'EDASTA',row['status'],'EDASTATUD',reason)
    return payload


def accept_transfer(c,payload,actor,as_of):
    """Simuleeritud vastuvõtt täpse kontrollsummaga; ei tee makset."""
    authorize(c,actor,'RTK')
    tid=payload.get('transfer_id');t=c.execute('SELECT * FROM transfer WHERE transfer_id=?',(tid,)).fetchone()
    if not t or digest(canonical(payload))!=t['payload_hash']:raise ValueError('Edastus puudub või sisu kontrollsumma erineb')
    if t['accepted_at']:return t['external_reference']
    id=t['document_id'];row=document(c,id)
    if row['status']!='EDASTATUD':raise ValueError('Dokument pole edastatud')
    require_clean(c,id,as_of,'RTK simulatsioon: hoiatused on varasemates kinnitustes käsitletud')
    r=payload['invoice'];ref='SIM-SAP-'+id;entry='KANNE-'+id
    with c:
        c.execute('INSERT INTO journal_entry VALUES(?,?,?)',(entry,id,r['service_date']))
        lines=[('DEMO_KULU',int(r['net_cents']),0),('DEMO_KM_KULU',int(r['vat_cents']),0),('DEMO_TARNIJA',0,int(r['gross_cents']))]
        if sum(x[1] for x in lines)!=sum(x[2] for x in lines):raise ValueError('Kanne pole tasakaalus')
        c.executemany('INSERT INTO journal_line(entry_id,account,debit_cents,credit_cents) VALUES(?,?,?,?)',[(entry,*x) for x in lines])
        c.execute('UPDATE transfer SET accepted_at=?,external_reference=? WHERE transfer_id=?',(now(),ref,tid))
        c.execute("UPDATE input_document SET status='KAJASTATUD' WHERE document_id=?",(id,))
        c.execute("UPDATE invoice SET status='KAJASTATUD' WHERE invoice_id=?",(id,))
        log(c,id,actor,'KAJASTA','EDASTATUD','KAJASTATUD','Simuleeritud tekkepõhine kanne; makset ei tehtud')
    return ref


def export_csv(c,path,query):
    rows=c.execute(query).fetchall();Path(path).parent.mkdir(parents=True,exist_ok=True)
    with Path(path).open('w',encoding='utf-8-sig',newline='') as f:
        if rows:
            w=csv.writer(f,delimiter=';');w.writerow(rows[0].keys());w.writerows(rows)

LATEST_ISSUES='''SELECT r.document_id,r.as_of,i.code,i.severity,i.field,i.message
FROM check_run r JOIN validation_issue i ON i.run_id=r.run_id
WHERE r.run_id=(SELECT MAX(x.run_id) FROM check_run x WHERE x.document_id=r.document_id)
ORDER BY r.document_id,i.issue_id'''


def replace_document(c,old_id,new_row,actor,reason):
    """Parandus uue versioonina, algne toorandmestik ja ajalugu säilivad."""
    authorize(c,actor,'ANALUUTIK');old=document(c,old_id)
    if old['status'] not in {'SISEND','TAGASTATUD'}:raise ValueError('Parandada saab sisendit või tagastatud dokumenti')
    id=str(new_row.get('invoice_id','')).strip()
    if not id or id==old_id:raise ValueError('Parandus vajab uut dokumendi ID-d')
    if len(reason.strip())<10:raise ValueError('Lisa paranduse sisuline põhjendus')
    raw=canonical(new_row)
    with c:
        c.execute('INSERT INTO input_document(document_id,raw_json,content_hash,creator_actor,imported_at,revision,supersedes_document_id) VALUES(?,?,?,?,?,?,?)',
            (id,raw,digest(raw),actor,now(),old['revision']+1,old_id))
        c.execute("UPDATE input_document SET status='ASENDATUD' WHERE document_id=?",(old_id,))
        log(c,old_id,actor,'ASENDA',old['status'],'ASENDATUD',reason+'; uus ID: '+id)
        log(c,id,actor,'PARANDUS','PUUDUB','SISEND',reason+'; eelmine ID: '+old_id)
    return id
