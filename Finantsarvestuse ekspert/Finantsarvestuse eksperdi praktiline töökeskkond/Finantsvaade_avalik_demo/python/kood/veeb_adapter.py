"""Ühine adapter CPythonile ja Pyodide'ile. Ei kopeeri arve ärireegleid."""
import base64,csv,io,json,re
from datetime import date,datetime
from pathlib import Path
import openpyxl
from openpyxl.styles import Font,PatternFill
from menetlus import connect,initialize,import_rows,validate,document,REQUIRED,canonical,digest

MAX_ROWS=500
MAX_BYTES=2_000_000

def _parse_input(content,kind='csv'):
    if len(content)>MAX_BYTES:raise ValueError('Faili piir on 2 MB')
    if kind=='csv':
        try:text=content.decode('utf-8-sig')
        except UnicodeError as e:raise ValueError('CSV peab olema UTF-8 kodeeringus') from e
        reader=csv.reader(io.StringIO(text),delimiter=';',strict=True)
        matrix=[]
        for row in reader:
            if len(matrix)>MAX_ROWS:raise ValueError('Kuni 500 sisendrida')
            if len(row)>64:raise ValueError('Kuni 64 veergu')
            matrix.append(row)
    elif kind=='xlsx':
        import zipfile
        with zipfile.ZipFile(io.BytesIO(content)) as z:
            if len(z.infolist())>1000 or sum(i.file_size for i in z.infolist())>10_000_000:raise ValueError('XLSX lahtipakitud sisu on liiga suur')
            for info in z.infolist():
                if 'vbaproject' in info.filename.lower():raise ValueError('Makrodega fail pole lubatud')
                if info.filename.lower().endswith(('.xml','.rels')):
                    data=z.read(info).replace(b'\x00',b'').upper()
                    if b'<!DOCTYPE' in data or b'<!ENTITY' in data:raise ValueError('XML-olemid pole lubatud')
        w=openpyxl.load_workbook(io.BytesIO(content),read_only=True,data_only=False,keep_links=False)
        matrix=[]
        try:
            sheet=w.worksheets[0]
            if (sheet.max_column or 0)>64 or (sheet.max_row or 0)>501:raise ValueError('XLSX mõõtmete piir: 501 rida ja 64 veergu')
            for row in sheet.iter_rows():
                if len(matrix)>MAX_ROWS:raise ValueError('Kuni 500 sisendrida')
                if len(row)>64:raise ValueError('Kuni 64 veergu')
                if any(c.data_type=='f' for c in row):raise ValueError('Impordi väärtused, mitte Exceli valemid')
                matrix.append([c.value for c in row])
        finally:w.close()
    else:raise ValueError('Lubatud vormingud: csv ja xlsx')
    if not matrix:raise ValueError('Fail on tühi')
    if any(isinstance(v,str) and len(v)>20000 for row in matrix for v in row):raise ValueError('Lahtris on üle 20 000 märgi')
    header=matrix[0]
    if len(header)!=len(set(header)) or any(not isinstance(x,str) or not x for x in header):raise ValueError('Päis on tühi või dubleerub')
    missing=set(REQUIRED)-set(header)
    if missing:raise ValueError('Puuduvad veerud: '+', '.join(sorted(missing)))
    rows=[]
    for row in matrix[1:]:
        if not any(v not in (None,'') for v in row):continue
        if len(row)!=len(header):raise ValueError('Rea veergude arv erineb päisest')
        clean=[]
        for key,x in zip(header,row):
            if isinstance(x,(date,datetime)):
                if isinstance(x,datetime) and x.time().isoformat()!='00:00:00':raise ValueError('Kuupäeva lahtris on kellaaeg')
                x=x.date().isoformat() if isinstance(x,datetime) else x.isoformat()
            clean.append('' if x is None else x)
        rows.append(dict(zip(header,clean)))
    if not rows:raise ValueError('Andmeridu pole')
    if len(rows)>MAX_ROWS:raise ValueError('Kuni 500 sisendrida')
    return rows


def safe_cell(v):
    if isinstance(v,str) and v.lstrip().startswith(('=','+','-','@')):return "'"+v
    return v


def export_table(rows,fmt='csv',title='Aruanne'):
    if not rows:raise ValueError('Valik on tühi; eksportimiseks vali vähemalt üks rida')
    headers=list(rows[0]);matrix=[[safe_cell(h) for h in headers]]+[[safe_cell(r.get(k)) for k in headers] for r in rows]
    if fmt=='csv':
        f=io.StringIO();writer=csv.writer(f,delimiter=';');writer.writerows(matrix)
        return f.getvalue().encode('utf-8-sig')
    if fmt!='xlsx':raise ValueError('Tundmatu eksportvorming')
    w=openpyxl.Workbook();s=w.active;s.title='Aruanne'
    s.append([safe_cell(title)]);s.append(['Rahasummad sentides; suhtarv 0.64 tähendab 64%.']);s.append([])
    for row in matrix:s.append(row)
    for c in s[4]:c.font=Font(bold=True,color='FFFFFF');c.fill=PatternFill('solid',fgColor='183C3A')
    for col in s.columns:
        width=min(60,max(18,max(len(str(c.value or '')) for c in list(col)[3:])+2))
        s.column_dimensions[col[0].column_letter].width=width
    s.freeze_panes='B5';s.auto_filter.ref=f'A4:{s.cell(s.max_row,s.max_column).coordinate}'
    s.sheet_view.showGridLines=False
    f=io.BytesIO();w.save(f);return f.getvalue()

class WebSession:
    def __init__(self,rows,as_of):
        self.as_of=date.fromisoformat(as_of).isoformat()
        self.c=connect(':memory:');initialize(self.c)
        import_rows(self.c,rows)
    def close(self):self.c.close()
    def snapshot(self):
        result=[]
        for r in self.c.execute('SELECT * FROM input_document ORDER BY document_id').fetchall():
            raw=json.loads(r['raw_json']);issues=validate(self.c,r['document_id'],self.as_of)
            result.append(dict(id=r['document_id'],raw=raw,issues=issues,status=r['status'],
                               errors=sum(i['severity']=='VIGA' for i in issues),
                               warnings=sum(i['severity']=='HOIATUS' for i in issues),data_kind='SUNTEETILINE_OPPESISEND'))
        return dict(as_of=self.as_of,invoices=result,checked=len(result),
                    errors=sum(r['errors'] for r in result),warnings=sum(r['warnings'] for r in result),
                    erroneous_documents=sum(r['errors']>0 for r in result),
                    duplicate_documents=sum(any(i['code']=='DUPLIKAAT' for i in r['issues']) for r in result))
    def import_file(self,content,kind):
        rows=parse_input(content,kind)
        existing={r[0] for r in self.c.execute('SELECT document_id FROM input_document')}
        new_ids={str(r.get('invoice_id','')).strip() or 'PUUDUV-'+digest(canonical(r))[:16] for r in rows}
        if len(existing|new_ids)>MAX_ROWS:raise ValueError('Seansi piir on 500 dokumenti; taasta näidis')
        import_rows(self.c,rows) # Kogu partii on atomaarne; vana sama ID teistsugune sisu keelatud.
        return self.snapshot()
    def export(self,ids,fmt):
        snap=self.snapshot();selected=[r for r in snap['invoices'] if r['id'] in ids]
        if len(selected)!=len(set(ids)):raise ValueError('Tundmatu dokumendi ID')
        rows=[]
        for r in selected:
            for i in r['issues'] or [dict(severity='OK',code='OK',field='',message='Vigu ega hoiatusi pole')]:
                rows.append(dict(document_id=r['id'],supplier=r['raw'].get('supplier_name',''),
                    gross_cents=r['raw'].get('gross_cents',''),as_of=self.as_of,
                    data_kind=r['data_kind'],**i))
        return export_table(rows,fmt,'Sünteetiliste ostuarvete kontroll')


def parse_input(content,kind='csv'):
    try:return _parse_input(content,kind)
    except ValueError:raise
    except Exception as e:raise ValueError('Vigane sisendfail: kasuta UTF-8 CSV-d või krüptimata XLSX-i') from e
