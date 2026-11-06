"""Etapi 3 arvutused. Raha jääb Int64 sentidesse; protsendid on suhtarvud."""
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
import hashlib, json, sqlite3
import openpyxl
import polars as pl
import pandas as pd
from pydantic import BaseModel, ConfigDict, Field, model_validator
from andmeleping import Cents
from etapp1 import cents

ROOT=Path(__file__).resolve().parents[1]

def ratio(numerator, denominator):
    return None if denominator in (None, 0) or numerator is None else numerator/denominator


def budget_metrics(initial, budget, actual):
    if any(v is None for v in (initial,budget,actual)):
        raise ValueError('Puuduvat raha ei asendata nulliga')
    if any(type(v) is not int or v<0 for v in (initial,budget,actual)):
        raise ValueError('Kulud peavad olema positiivsed täisarvud sentides')
    return dict(change_cents=budget-initial, remaining_cents=budget-actual,
                usage=ratio(actual,budget))


def read_budget(root=ROOT):
    sources=json.loads((root/'andmed/allikaregister.json').read_text())
    source=next(x for x in sources if x['source_id']=='TAIT2026A')
    path=root/'andmed/algandmed'/source['file']
    if hashlib.sha256(path.read_bytes()).hexdigest()!=source['sha256']:
        raise ValueError('Allika kontrollsumma erineb')
    wb=openpyxl.load_workbook(path,data_only=True);s=wb['August 2026']
    law=openpyxl.load_workbook(root/'andmed/algandmed/re2026_seadus.xlsx',data_only=True).worksheets[0]
    if (s['B86'].value!='HARIDUS- JA TEADUSMINISTEERIUMI VALITSEMISALA' or
        s['B94'].value!='KULUD' or s['D86'].value!='Lõplik eelarve' or
        s['E86'].value!='Täitmine kokku' or 'tuhandetes eurodes' not in str(s['B17'].value)):
        raise ValueError('Allika struktuur või ühik muutus')
    rows=[]
    for r in range(94,104):
        raw=[cents(s[f'{c}{r}'].value,1000) for c in 'CDE']
        if any(v is None or v>0 for v in raw): raise ValueError('Puuduv väärtus või ootamatu kulumärk')
        if raw[0]!=cents(law[f'D{r+14}'].value,1000):raise ValueError('Algeelarvete ristkontroll ebaõnnestus')
        initial,budget,actual=[-v for v in raw]
        rows.append(dict(id=f'TAIT2026A-{r}',label='HTM valitsemisala kokku' if r==94 else s[f'B{r}'].value,
                         level='koond' if r==94 else 'asutus',initial_cents=initial,budget_cents=budget,
                         actual_cents=actual,**budget_metrics(initial,budget,actual),
                         source_id='TAIT2026A',source_cells=f'C{r}:E{r}',sheet=s.title,
                         budget_period='2026-01-01/2026-12-31',actual_period='2026-01-01/2026-08-31',
                         measure='seadusepildi_kulud',provenance='TULETATUD'))
    for k in ['initial_cents','budget_cents','actual_cents']:
        if rows[0][k]!=sum(x[k] for x in rows[1:]):raise ValueError('Asutuste summa ei klapi koondiga')
    wb.close()
    return rows


def aggregate_months(path,engine='polars'):
    # Koond + alamread + rahastusristlõige ei tohi ühte summasse sattuda.
    if engine=='polars':
        df=pl.scan_csv(path,separator=';',schema_overrides={'amount_cents':pl.Int64})
        q=(df.filter((pl.col('period_kind')=='kuu') & (pl.col('row_kind')=='koond'))
             .select('period_start','amount_cents').sort('period_start'))
        out=q.collect().to_dicts()
    elif engine=='pandas':
        df=pd.read_csv(path,sep=';',dtype={'amount_cents':'Int64'})
        out=df.loc[(df.period_kind=='kuu') & (df.row_kind=='koond'),['period_start','amount_cents']].sort_values('period_start').to_dict('records')
    else:raise ValueError('Mootor peab olema polars või pandas')
    keys=[r['period_start'] for r in out]
    if len(keys)!=len(set(keys)):raise ValueError('Kuu koond esineb mitu korda')
    if keys!=[f'2026-{m:02d}-01' for m in range(1,10)]:raise ValueError('Oodatud üheksa kuud puuduvad')
    if any(pd.isna(r['amount_cents']) for r in out):raise ValueError('Kuuväärtus puudub')
    return [dict(period_start=r['period_start'],amount_cents=int(r['amount_cents'])) for r in out]


def year_comparison(path):
    df=pl.read_csv(path,separator=';',schema_overrides={'amount_cents':pl.Int64})
    rows=df.filter((pl.col('period_kind')=='YTD') & (pl.col('row_kind')!='ristloige')).to_dicts()
    out=[]
    for label in dict.fromkeys(r['label'] for r in rows):
        pair=[r for r in rows if r['label']==label]
        a=[r for r in pair if r['period_start']=='2026-01-01']
        b=[r for r in pair if r['period_start']=='2025-01-01']
        if len(a)!=1 or len(b)!=1 or a[0]['amount_cents'] is None or b[0]['amount_cents'] is None:
            raise ValueError('Aastavõrdluse väärtus puudub või dubleerub')
        a,b=a[0],b[0]
        if (a['period_end']!='2026-09-30' or b['period_end']!='2025-09-30' or
            a['scope']!=b['scope'] or a['measure']!=b['measure']):
            raise ValueError('Periood või arvestusalus ei ole võrreldav')
        x,y=a['amount_cents'],b['amount_cents']
        out.append(dict(label=label,level=a['row_kind'],previous_cents=y,current_cents=x,
                        difference_cents=x-y,change=ratio(x-y,y),source_cells=b['cell']+':'+a['cell'],
                        provenance='TULETATUD'))
    return out

class Grant(BaseModel):
    model_config=ConfigDict(extra='forbid')
    id: str=Field(strict=True,min_length=1)
    budget_cents: Cents
    actual_cents: Cents
    eligible_cents: Cents
    ceiling_cents: Cents
    advance_cents: Cents
    rate: Decimal=Field(ge=0,le=1,allow_inf_nan=False)
    @model_validator(mode='after')
    def eligibility(self):
        if self.eligible_cents>self.actual_cents:raise ValueError('Abikõlblik kulu ületab tegeliku kulu')
        return self


def grant_result(data):
    g=Grant.model_validate(data)
    earned=min(g.ceiling_cents,int((Decimal(g.eligible_cents)*g.rate).quantize(Decimal('1'),rounding=ROUND_HALF_UP)))
    return dict(id=g.id,budget_cents=g.budget_cents,actual_cents=g.actual_cents,
                variance_cents=g.actual_cents-g.budget_cents,variance=ratio(g.actual_cents-g.budget_cents,g.budget_cents),
                eligible_cents=g.eligible_cents,rate=float(g.rate),ceiling_cents=g.ceiling_cents,
                earned_cents=earned,advance_cents=g.advance_cents,
                payable_cents=max(earned-g.advance_cents,0),recoverable_cents=max(g.advance_cents-earned,0),
                provenance='SUNTEETILINE',period='2026-01-01/2026-09-30')


def save_sql(path,budgets,monthly,grants):
    # Eraldi analüüsiandmebaas: menetluse 0.2 skeemi ei migreerita ega muudeta.
    c=sqlite3.connect(path)
    c.executescript((ROOT/'sql/004_analuus.sql').read_text())
    with c:
        c.executemany('INSERT INTO budget_analysis VALUES(?,?,?,?,?,?,?,?,?,?,?)',
            [(r['id'],r['label'],r['level'],r['initial_cents'],r['budget_cents'],r['actual_cents'],r['source_id'],r['source_cells'],r['budget_period'],r['actual_period'],r['provenance']) for r in budgets])
        c.executemany('INSERT INTO monthly_actual VALUES(?,?)',[(r['period_start'],r['amount_cents']) for r in monthly])
        c.executemany('INSERT INTO grant_analysis VALUES(?,?,?,?,?,?,?)',[(r['id'],r['budget_cents'],r['actual_cents'],r['earned_cents'],r['advance_cents'],r['provenance'],r['period']) for r in grants])
    return c
