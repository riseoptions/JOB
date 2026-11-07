"""Numbriliste vastuste sõltumatu kontroll; Python 3 standardteek."""

def npv(flows, rate):
    return sum(cf / (1 + rate)**t for t, cf in enumerate(flows))


def irr(flows, lower=-0.9, upper=2.0, iterations=150):
    for _ in range(iterations):
        middle = (lower + upper) / 2
        if npv(flows, middle) > 0:
            lower = middle
        else:
            upper = middle
    return (lower + upper) / 2


def dcf(fcffs, wacc, g, debt, cash, shares):
    pv = sum(cf/(1+wacc)**year for year, cf in enumerate(fcffs, start=1))
    terminal_value = fcffs[-1]*(1+g)/(wacc-g)
    pv_terminal = terminal_value/(1+wacc)**len(fcffs)
    ev = pv + pv_terminal
    equity = ev - debt + cash
    per_share = equity / shares
    return pv, terminal_value, pv_terminal, ev, equity, per_share

# Juhus A: kõik tuhandetes eurodes
assets_2026 = 45 + 160 + 115 + 280
liabilities_2026 = 135 + 65 + 170
equity_2026 = 230
assert assets_2026 == liabilities_2026 + equity_2026
assert 200 + 50 - 20 == 230
cfo = 50 + 40 - (160-100) - (115-80) + (135-90)
cfi = -70
cff = (65 + 170 - 40 - 170) - 20
assert cfo == 40 and cfi == -70 and cff == 5
assert 70 + cfo + cfi + cff == 45
assert 250 + 70 - 40 == 280
assert 100 + 40 == 140 # EBITDA
assert abs((50/215)*100-23.2558139535)<1e-6
assert abs((50/550)*100-9.0909090909)<1e-6
ccc_2025 = (100/820 + 80/530 - 90/530)*365
ccc_2026 = (160/1000 + 115/650 - 135/650)*365
assert abs(ccc_2025 - 37.6254026691)<1e-8
assert abs(ccc_2026 - 47.1692307692)<1e-8

# Juhus B: DCF kasutab tuhandeid eurosid ja aktsiate arvu tuhandetes
project = [-30, 12, 14, 16]
project_npv = npv(project, .10)
project_irr = irr(project)
assert abs(project_npv - 4.5003756574)<1e-8
assert abs(project_irr - .17925041066)<1e-8
fcffs = [120, 140, 160]
base = dcf(fcffs, .10, .03, 400, 70, 100)
conservative = dcf(fcffs, .12, .02, 400, 70, 100)
optimistic = dcf(fcffs, .09, .04, 400, 70, 100)
assert abs(base[3] - 2113.813459268)<1e-8
assert abs(base[-1] - 17.83813459268)<1e-8
assert abs(conservative[-1] - 11.64260204082)<1e-8
assert abs(optimistic[-1] - 25.91302920630)<1e-8

print('KÕIK KONTROLLID LÄBITUD')
print(f'CFO={cfo} CFI={cfi} CFF={cff} raha lõpus=45 (tuh €)')
print(f'CCC 2025={ccc_2025:.2f} päeva, CCC 2026={ccc_2026:.2f} päeva')
print(f'Projekti NPV={project_npv*1000:.2f} €, IRR={project_irr*100:.2f}%')
print(f'EV={base[3]:.3f} tuh €, aktsia väärtus={base[-1]:.2f} €')
print(f'Stress: {conservative[-1]:.2f}–{optimistic[-1]:.2f} € / aktsia')
