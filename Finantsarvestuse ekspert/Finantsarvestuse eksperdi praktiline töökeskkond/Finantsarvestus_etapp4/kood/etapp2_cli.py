"""Käsurea kasutus: python kood/etapp2_cli.py --help."""
import argparse,json
from pathlib import Path
from menetlus import *

def main():
    p=argparse.ArgumentParser(description='Finantsarvestuse 2. etapi kohalik õppesimulatsioon')
    p.add_argument('--db',required=True,help='SQLite-faili tee')
    p.add_argument('--as-of',default='2026-11-05',help='Kontrollpäev, vaikimisi fikseeritud demo kuupäev')
    sub=p.add_subparsers(dest='cmd',required=True)
    sub.add_parser('init');sub.add_parser('list')
    imp=sub.add_parser('import');imp.add_argument('csv')
    check=sub.add_parser('check');check.add_argument('id',help='Dokumendi ID või ALL')
    act=sub.add_parser('act');act.add_argument('id');act.add_argument('action',choices=['ESITA','KOOSKOLASTA','KINNITA','TAGASTA']);act.add_argument('--actor',required=True);act.add_argument('--reason',required=True)
    exp=sub.add_parser('export');exp.add_argument('id');exp.add_argument('json_file');exp.add_argument('--reason',required=True)
    ack=sub.add_parser('accept');ack.add_argument('json_file')
    fix=sub.add_parser('correct');fix.add_argument('id');fix.add_argument('csv');fix.add_argument('--reason',required=True)
    args=p.parse_args();db=Path(args.db)
    if args.cmd=='init':db.parent.mkdir(parents=True,exist_ok=True)
    elif not db.is_file():p.error('Andmebaasi pole. Käivita esmalt init.')
    c=connect(db)
    try:
        initialize(c)
        if args.cmd=='init':print('Skeem 0.2 valmis')
        elif args.cmd=='import':print('Lisatud:',import_rows(c,read_csv(args.csv)))
        elif args.cmd=='list':
            for row in c.execute('SELECT document_id,status,revision,supersedes_document_id FROM input_document ORDER BY document_id'):print(dict(row))
        elif args.cmd=='check':
            ids=[r[0] for r in c.execute("SELECT document_id FROM input_document WHERE status<>'ASENDATUD'")] if args.id=='ALL' else [args.id]
            for id in ids:print(id,json.dumps(validate(c,id,args.as_of),ensure_ascii=False))
        elif args.cmd=='act':transition(c,args.id,args.action,args.actor,args.as_of,args.reason);print(document(c,args.id)['status'])
        elif args.cmd=='export':
            target=Path(args.json_file);target.parent.mkdir(parents=True,exist_ok=True)
            payload=export_transfer(c,args.id,'analuutik',args.as_of,args.reason)
            target.write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8');print(target)
        elif args.cmd=='accept':print(accept_transfer(c,json.loads(Path(args.json_file).read_text(encoding='utf-8')),'rtk_demo',args.as_of))
        elif args.cmd=='correct':
            rows=read_csv(args.csv)
            if len(rows)!=1:raise ValueError('Parandusfailis peab olema täpselt üks rida')
            print(replace_document(c,args.id,rows[0],'analuutik',args.reason))
    except (ValueError,sqlite3.Error,OSError) as e:p.exit(2,'Viga: '+str(e)+'\n')
    finally:c.close()

if __name__=='__main__':main()
