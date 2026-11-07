"""Thonny F5 või python kood/etapp3_demo.py. Arvutused Pythonis; XLSX on hetkeseis."""
import json, platform, sys
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter
from statistics import median
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
import pydantic,polars,pandas
from analuus import *
from etapp1 import build,write_csv
from andmeleping import InvoiceInput


def workbook_report(path,budgets,monthly,yoy,grants,sources):
    # Projekti lähteülesanne nõuab Python + openpyxl automaataruandlust.
    wb=openpyxl.Workbook();wb.remove(wb.active)
    money='#,##0.00;[Red](#,##0.00);"–"'
    def sheet(name,title,context,headers,rows,money_cols=(),pct_cols=()):
        s=wb.create_sheet(name);s.sheet_view.showGridLines=False
        s['A2']=title;s['A2'].font=Font(name='Arial',size=15,bold=True,color='203864')
        s['A3']=context;s['A3'].font=Font(name='Arial',size=10,italic=True,color='555555')
        s.append([])
        for j,h in enumerate(headers,1):
            c=s.cell(5,j,h);c.fill=PatternFill('solid',fgColor='203864');c.font=Font(name='Arial',size=10,color='FFFFFF',bold=True)
            c.alignment=Alignment(wrap_text=True,vertical='center',horizontal='center')
        for i,row in enumerate(rows,6):
            for j,v in enumerate(row,1):
                c=s.cell(i,j,v);c.font=Font(name='Arial',size=10);c.alignment=Alignment(vertical='center',wrap_text=(j==1))
                if i%2==0:c.fill=PatternFill('solid',fgColor='F1F4F8')
                if j in money_cols:c.number_format=money
                if j in pct_cols:c.number_format='0.0%'
            s.row_dimensions[i].height=32
        s.row_dimensions[5].height=35
        s.column_dimensions['A'].width=47
        for j in range(2,len(headers)+1):s.column_dimensions[get_column_letter(j)].width=20
        s.freeze_panes='B6';s.auto_filter.ref=f'A5:{get_column_letter(len(headers))}{5+len(rows)}'
        s.sheet_properties.pageSetUpPr.fitToPage=True;s.page_setup.orientation='landscape';s.page_setup.paperSize=s.PAPERSIZE_A3;s.page_setup.fitToWidth=1;s.page_setup.fitToHeight=0
        return s
    euro=lambda x: x/100
    b=sheet('Eelarve','HTM valitsemisala eelarve kasutamine',
       'TULETATUD · aastaeelarve ja jaanuar–august 2026 täitmine · EUR',
       ['Asutus / koond','Algeelarve','Ajakohane eelarve','Täitmine 8 kuud','Eelarve muutus','Kasutamata','Kasutamine','Allikalahtrid'],
       [[r['label'],euro(r['initial_cents']),euro(r['budget_cents']),euro(r['actual_cents']),euro(r['change_cents']),euro(r['remaining_cents']),r['usage'],r['source_cells']] for r in budgets],range(2,7),[7])
    for c in b[6][:8]:c.font=Font(name='Arial',size=10,bold=True,color='203864')
    notes=['Kasutamine = 8 kuu täitmine / ajakohane aastaeelarve. See ei ole sama perioodi plaanihälve.',
           'Ajakohane eelarve on augusti väljavõtte „Lõplik eelarve“, mitte 31.12.2026 lõppseis.',
           'Koondrida ja asutuste ridu ei summeerita koos. Kulude algne miinusmärk on pööratud positiivseks.',
           'Allikas: TAIT2026A, leht August 2026, read 94–103. Ühik tuhat EUR teisendatud EUR-iks.',
           'Algse eelarve ristkontroll: RE2026, D108:D117. Allikad võivad hiljem muutuda.']
    for i,t in enumerate(notes,18):b.cell(i,1,t)
    b.cell(24,1,sources[2]['url']);b.cell(25,1,sources[0]['url'])
    m=sheet('Kulud','Kulud ja investeeringud, amortisatsioonita',
       'TULETATUD · HTM valitsemisala · jaanuar–september · EUR',
       ['Kululiik / koond','2025, 9 kuud','2026, 9 kuud','Muutus EUR','Muutus %','Allikalahtrid'],
       [[r['label'],euro(r['previous_cents']),euro(r['current_cents']),euro(r['difference_cents']),r['change'],r['source_cells']] for r in yoy],[2,3,4],[5])
    m.cell(16,1,'2026 kuukulud samal arvestusalusel')
    m.cell(17,1,'Kuu');m.cell(17,2,'Täitmine EUR')
    for i,r in enumerate(monthly,18):m.cell(i,1,r['period_start'][:7]);m.cell(i,2,euro(r['amount_cents'])).number_format=money
    m.cell(28,1,'Rahastuse ristlõiget (välisvahendid) ei liideta kululiikidele.');m.cell(29,1,'Allikas TAIT2026, leht Eelarve täitmine üheksa kuud, B137:J137 ja O137:N144.');m.cell(30,1,sources[1]['url'])
    g=sheet('Toetused','Toetuste kontroll ja perioodi plaanihälve',
       'SUNTEETILINE · jaanuar–september 2026 · EUR · fiktiivsed tingimused',
       ['Projekt','Perioodi plaan','Tegelik kulu','Hälve EUR','Hälve %','Abikõlblik kulu','Toetus','Ettemakse','Juurde maksta','Tagasi nõuda'],
       [[r['id'],euro(r['budget_cents']),euro(r['actual_cents']),euro(r['variance_cents']),r['variance'],euro(r['eligible_cents']),euro(r['earned_cents']),euro(r['advance_cents']),euro(r['payable_cents']),euro(r['recoverable_cents'])] for r in grants],[2,3,4,6,7,8,9,10],[5])
    for i,t in enumerate(['Hälve = tegelik – perioodi plaan; positiivne tähendab plaani ületamist.',
        'Toetus = min(abikõlblik kulu × määr, ülempiir). Ümardus toimub sendini HALF_UP.',
        'Määr / ülempiir: '+ '; '.join(f"{r['id']}: {r['rate']:.0%} / {r['ceiling_cents']/100:g} EUR" for r in grants),
        'Tühi protsent tähendab nullist plaani: suhtarv ei ole määratud.',
        'Ettemakse ei ole kulu. Juurdemakse ja tagasinõue on arvutuslikud, mitte tehtud maksed.',
        'Allikas: andmed/sunteetilised/etapp3_toetused.json. Tegelike toetuste puhul kontrolli lepingu tingimusi.',
        'See töövihik on Pythoni arvutuste hetkeseis. Muudatuse järel käivita demo uuesti.'],12):g.cell(i,1,t)
    for sh in wb:
        sh.print_options.horizontalCentered=True
    wb.save(path)


def run(root=ROOT,output=None):
    build(root)
    out=Path(output) if output else root/'valjund/etapp3'/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    out.mkdir(parents=True,exist_ok=False)
    budgets=read_budget(root)
    path=root/'andmed/toodeldud/htm_taitmine_2026.csv'
    monthly=aggregate_months(path);reference=aggregate_months(path,'pandas')
    if monthly!=reference:raise ValueError('Polarsi ja pandas’e tulemus erineb')
    yoy=year_comparison(path)
    if sum(r['amount_cents'] for r in monthly)!=yoy[0]['current_cents']:raise ValueError('Kuud ei võrdu YTD-ga')
    if sum(r['current_cents'] for r in yoy[1:])!=yoy[0]['current_cents']:raise ValueError('Kululiigid ei võrdu koondiga')
    grants=[grant_result(r) for r in json.loads((root/'andmed/sunteetilised/etapp3_toetused.json').read_text())]
    if len({g['id'] for g in grants})!=len(grants):raise ValueError('Toetuse ID dubleerub')
    for name,rows in [('eelarve',budgets),('kuukulud',monthly),('aastavordlus',yoy),('toetused',grants)]:write_csv(out/(name+'.csv'),rows)
    c=save_sql(out/'analuus.sqlite',budgets,monthly,grants)
    if c.execute("SELECT SUM(actual_cents) FROM budget_analysis WHERE level='asutus'").fetchone()[0]!=budgets[0]['actual_cents']:raise ValueError('SQL summa erineb')
    if c.execute('PRAGMA integrity_check').fetchone()[0]!='ok':raise ValueError('SQL tervikluse viga')
    c.close()
    timings={}
    for engine in ['polars','pandas']:
        aggregate_months(path,engine) # soojendus
        samples=[]
        for _ in range(7):
            start=perf_counter();aggregate_months(path,engine);samples.append((perf_counter()-start)*1000)
        timings[engine]=dict(median_ms=median(samples),samples_ms=samples)
    result=dict(version='0.3',source_rows=99,selected_months=9,engines_equal=True,
        benchmark_scope='CSV lugemine, filter, sort ja kontrollid; 7 korduse mediaan; väike fail; mitte üldine jõudlusväide',
        benchmark=timings,python=sys.version,platform=platform.platform(),
        packages=dict(pydantic=pydantic.__version__,polars=polars.__version__,pandas=pandas.__version__,openpyxl=openpyxl.__version__),
        budget=budgets[0],year_comparison=yoy[0])
    (out/'tulemus.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    (out/'arve_skeem.json').write_text(json.dumps(InvoiceInput.model_json_schema(mode='validation'),ensure_ascii=False,indent=2),encoding='utf-8')
    sources=json.loads((root/'andmed/allikaregister.json').read_text())
    workbook_report(out/'Finantsanaluus.xlsx',budgets,monthly,yoy,grants,sources)
    grant_summary='; '.join(f"{r['id']}: perioodihälve {r['variance_cents']/100:,.2f} EUR, toetus {r['earned_cents']/100:,.2f} EUR, juurde maksta {r['payable_cents']/100:,.2f} EUR, tagasi nõuda {r['recoverable_cents']/100:,.2f} EUR" for r in grants)
    (out/'aruanne.md').write_text(f"# Finantsanalüüs · 2026\n\nHTM valitsemisala: augusti ajakohane aastaeelarve {budgets[0]['budget_cents']/100:,.2f} EUR; jaanuar–august täitmine {budgets[0]['actual_cents']/100:,.2f} EUR; kasutamine {budgets[0]['usage']:.2%}.\n\nKasutamata aastaeelarve {budgets[0]['remaining_cents']/100:,.2f} EUR ei ole kaheksa kuu sääst. Kuupõhine kinnitatud plaan puudub.\n\nJaanuar–september kulud ja investeeringud amortisatsioonita: {yoy[0]['current_cents']/100:,.2f} EUR. Muutus 2025 sama perioodiga {yoy[0]['change']:.2%}. Koosseis erineb eelarvevaatest, seega vaateid ei ühendata.\n\nSünteetilised toetused: {grant_summary}. Nullplaani hälbe protsent puudub.\n\nJärgmine analüütiku samm: küsi kuupõhist kinnitatud plaani ja toetuse abikõlblikkuse tõendeid. Arvud üksi ei selgita kulumuutuste põhjuseid.\n\nAllikad ja lahtrid: eelarve.csv, aastavordlus.csv ning projekti andmed/allikaregister.json. Pärisandmed on avalikest väljavõtetest tuletatud; toetused on fiktiivsed.\n",encoding='utf-8')
    print('Etapp 3 valmis:',out)
    return out

if __name__=='__main__':run()
