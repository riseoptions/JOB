"""Etapp 1: kontrollitud algfailide profiil ja HTM-i väljavõtted, mitte analüüsimootor."""
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
import csv
import hashlib
import json
import openpyxl

ROOT = Path(__file__).resolve().parents[1]


def cents(value, multiplier=1):
    """Exceli arv -> täpsed täisarvulised eurosendid; tühi ja kriips pole null."""
    if value is None or value == '-':
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float, Decimal)):
        raise ValueError(f'Ootamatu arv: {value!r}')
    return int((Decimal(str(value)) * Decimal(multiplier) * 100).quantize(Decimal('1'), rounding=ROUND_HALF_UP))


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter=';')
        w.writeheader()
        w.writerows(rows)


def build(root=ROOT):
    raw = root / 'andmed/algandmed'
    out = root / 'andmed/toodeldud'
    out.mkdir(parents=True, exist_ok=True)
    sources = json.loads((root / 'andmed/allikaregister.json').read_text(encoding='utf-8'))
    profiles = []
    for source in sources:
        path = raw / source['file']
        if hashlib.sha256(path.read_bytes()).hexdigest() != source['sha256']:
            raise ValueError(f'Algfaili kontrollsumma erineb: {path.name}')
        wb = openpyxl.load_workbook(path, data_only=True)
        wf = openpyxl.load_workbook(path, data_only=False)
        for sheet in wb:
            nonempty = [(c.row, c.column) for row in sheet for c in row if c.value is not None]
            formulas = [c for row in wf[sheet.title] for c in row if c.data_type == 'f']
            missing_cache = sum(sheet[c.coordinate].value is None for c in formulas)
            profiles.append(dict(source_id=source['source_id'], sheet=sheet.title,
                physical_rows=sheet.max_row, physical_columns=sheet.max_column,
                last_nonempty_row=max(r for r,c in nonempty),
                last_nonempty_column=max(c for r,c in nonempty),
                formula_count=len(formulas), missing_formula_cache=missing_cache))
        wb.close(); wf.close()

    law = openpyxl.load_workbook(raw / sources[0]['file'], data_only=True).worksheets[0]
    if law['C100'].value != 'HARIDUS- JA TEADUSMINISTEERIUMI VALITSEMISALA' or law['B108'].value != '9.8':
        raise ValueError('Seaduse tabeli struktuur on muutunud; vaja uut kaardistust.')
    if 'tuhandetes eurodes' not in str(law['C4'].value):
        raise ValueError('Eelarve ühik ei vasta kaardistusele.')
    budgets = []
    for r in range(101,118):
        for col, metric in [('D','eelarve_kokku'),('E','piirmaaraga_vahendid')]:
            value = law[f'{col}{r}'].value
            budgets.append(dict(record_id=f'RE2026-{col}{r}', source_id='RE2026',
                sheet=law.title, cell=f'{col}{r}', line_id=law[f'B{r}'].value,
                label=law[f'C{r}'].value, metric=metric, year=2026,
                period_start='2026-01-01', period_end='2026-12-31',
                budget_version='algne_seadus', scope='HTM_valitsemisala',
                row_kind='koond' if r in (101,108) else 'detail',
                raw_value=str(value), raw_unit='tuhat_EUR', amount_cents=cents(value,1000),
                provenance='TULETATUD', sign_policy='allika_mark_sailitatud'))
    write_csv(out / 'htm_eelarve_2026.csv', budgets)
    actual = openpyxl.load_workbook(raw / sources[1]['file'], data_only=True).worksheets[0]
    if actual['A137'].value != 'Haridus-ja Teadusministeerium' or 'VALITSEMISALADE' not in str(actual['A73'].value):
        raise ValueError('Täitmise tabeli struktuur on muutunud.')
    if '(eurodes)' not in str(actual['A1'].value) or '9 kuud 2026' not in str(actual['N2'].value):
        raise ValueError('Täitmise ühik või periood on muutunud.')
    actuals=[]
    for r in range(137,146):
        for c in list(range(2,11))+[14,15]:
            month=c-1 if c<=10 else 9
            year=2025 if c==15 else 2026
            import calendar
            start=f'{year}-01-01' if c>=14 else f'{year}-{month:02d}-01'
            end=f'{year}-{month:02d}-{calendar.monthrange(year,month)[1]}'
            cell=actual.cell(r,c)
            actuals.append(dict(record_id=f'TAIT2026-{cell.coordinate}',source_id='TAIT2026',sheet=actual.title,
                cell=cell.coordinate,label=actual.cell(r,1).value,scope='HTM_valitsemisala',
                measure='kulud_ja_investeeringud_va_amortisatsioon',
                row_kind='koond' if r==137 else ('ristloige' if r==145 else 'sh_rida'),
                period_start=start,period_end=end,period_kind='YTD' if c>=14 else 'kuu',
                raw_value=str(cell.value),raw_unit='EUR',amount_cents=cents(cell.value),
                provenance='TULETATUD',missing_reason='allika_kriips' if cell.value=='-' else ''))
    write_csv(out / 'htm_taitmine_2026.csv', actuals)
    reconciliations=[]
    for r in range(137,146):
        values=[cents(actual.cell(r,c).value) for c in range(2,11)]
        stated=cents(actual.cell(r,14).value)
        delta=None if any(v is None for v in values) or stated is None else sum(values)-stated
        reconciliations.append(dict(source_row=r,label=actual.cell(r,1).value,
            monthly_sum_cents=None if delta is None else sum(values),stated_ytd_cents=stated,
            difference_cents=delta,status='PUUDUV' if delta is None else ('OK' if abs(delta)<=1 else 'ERINEVUS')))
    write_csv(out/'kooskolakontroll.csv',reconciliations)
    report=dict(schema_version='0.1',budget_records=len(budgets),actual_records=len(actuals),
        profiles=profiles,excluded_future_columns=['K','L','M'],
        reconciliation=reconciliations,comparison_allowed=False,
        comparison_reason='Algne kulueelarve ei võrdu kulude ja investeeringute täitmise ulatusega; puudub muudetud eelarve kaardistus.')
    (out/'profiil.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'Valmis: {len(budgets)} eelarvekirjet ja {len(actuals)} täitmiskirjet. Täitmise protsenti ei arvutatud.')
    return report

if __name__=='__main__':
    build()
