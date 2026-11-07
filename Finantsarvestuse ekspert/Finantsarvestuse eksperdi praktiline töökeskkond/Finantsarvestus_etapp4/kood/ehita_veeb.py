"""Ehita portatiivne dist/; avalik analüüs tuleb muutmata etapi 3 mootorist."""
import json,shutil,tempfile,hashlib
from datetime import datetime,timezone
from pathlib import Path
from etapp3_demo import run
from menetlus import read_csv
from veeb_adapter import WebSession
ROOT=Path(__file__).resolve().parents[1]

def build_web(root=ROOT):
    dist=root/'dist';dist.mkdir(exist_ok=True)
    shutil.copytree(root/'veeb',dist,dirs_exist_ok=True)
    data=dist/'data';data.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        out=run(root,Path(tmp)/'aruanne')
        from analuus import read_budget,aggregate_months,year_comparison,grant_result
        p=root/'andmed/toodeldud/htm_taitmine_2026.csv'
        budget=read_budget(root);monthly=aggregate_months(p);yoy=year_comparison(p)
        grants=[grant_result(r) for r in json.loads((root/'andmed/sunteetilised/etapp3_toetused.json').read_text())]
        downloads=dist/'aruanded';downloads.mkdir(exist_ok=True)
        for f in out.iterdir():shutil.copy2(f,downloads/f.name)
    rows=read_csv(root/'andmed/sunteetilised/etapp2_sisend.csv')
    as_of='2026-11-06'
    session=WebSession(rows,as_of);snapshot=session.snapshot();session.close()
    sources=json.loads((root/'andmed/allikaregister.json').read_text())
    payload=dict(version='0.4',built_at=datetime.now(timezone.utc).isoformat(),
      source_updated_at=max(s['downloaded_at'] for s in sources),sources=sources,budget=budget,
      monthly=monthly,yoy=yoy,grants=grants,invoice_snapshot=snapshot,invoice_seed=rows,
      periods=dict(budget='2026-01-01/2026-08-31',costs='2026-01-01/2026-09-30'))
    (data/'projekt.json').write_text(json.dumps(payload,ensure_ascii=False,allow_nan=False),encoding='utf-8')
    for folder,names in [('kood',['menetlus.py','andmeleping.py','veeb_adapter.py']),('sql',['001_skeem.sql','002_menetlus.sql'])]:
        target=dist/'python'/folder;target.mkdir(parents=True,exist_ok=True)
        for name in names:shutil.copy2(root/folder/name,target/name)
    (dist/'oppe').mkdir(exist_ok=True)
    for name in ['OPPEMOODUL_02.md','OPPEMOODUL_03.md','PYDANTIC_POLARS.md','OPPEMOODUL_04.md']:
        if (root/name).exists():shutil.copy2(root/name,dist/'oppe'/name)
    shutil.copy2(root/'andmed/sunteetilised/etapp2_sisend.csv',data/'naidisarved.csv')
    fixture=dict(rows=rows[:1],as_of=as_of)
    fixture['rows'][0]=dict(fixture['rows'][0],invoice_id='IMPORT-001',invoice_number='IMP-001',net_cents='100000',vat_cents='24000',gross_cents='124001')
    from etapp1 import write_csv
    write_csv(data/'impordi_proov.csv',fixture['rows'])
    (dist/'.nojekyll').write_text('')
    print('Veeb valmis:',dist)
    return payload
if __name__=='__main__':build_web()
