-- Käivita etapi 3 analuus.sqlite andmebaasis.
SELECT label,budget_cents,actual_cents,remaining_cents,usage FROM budget_report ORDER BY id;
-- Ära liida koondrida ja asutusi omavahel.
SELECT SUM(actual_cents) AS detail_sum FROM budget_analysis WHERE level='asutus';
SELECT SUM(amount_cents) AS september_ytd FROM monthly_actual;
SELECT * FROM grant_report ORDER BY id;
PRAGMA integrity_check;
