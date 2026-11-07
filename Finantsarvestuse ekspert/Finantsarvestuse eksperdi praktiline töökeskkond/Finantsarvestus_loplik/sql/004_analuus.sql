-- UUS eraldiseisev aruandeandmebaas. Ära käivita menetluse andmebaasis.
CREATE TABLE analysis_version(version TEXT PRIMARY KEY);
INSERT INTO analysis_version VALUES('0.3');
CREATE TABLE budget_analysis(
 id TEXT PRIMARY KEY,label TEXT NOT NULL,level TEXT CHECK(level IN ('koond','asutus')),
 initial_cents INTEGER NOT NULL,budget_cents INTEGER NOT NULL,actual_cents INTEGER NOT NULL,
 source_id TEXT NOT NULL,source_cells TEXT NOT NULL,budget_period TEXT NOT NULL,actual_period TEXT NOT NULL,
 provenance TEXT CHECK(provenance='TULETATUD'));
CREATE TABLE monthly_actual(period_start TEXT PRIMARY KEY,amount_cents INTEGER NOT NULL);
CREATE TABLE grant_analysis(id TEXT PRIMARY KEY,budget_cents INTEGER NOT NULL,actual_cents INTEGER NOT NULL,
 earned_cents INTEGER NOT NULL,advance_cents INTEGER NOT NULL,
 provenance TEXT CHECK(provenance='SUNTEETILINE'),period TEXT NOT NULL);
CREATE VIEW budget_report AS SELECT *,budget_cents-actual_cents AS remaining_cents,
 actual_cents*1.0/NULLIF(budget_cents,0) AS usage FROM budget_analysis;
CREATE VIEW grant_report AS SELECT *,actual_cents-budget_cents AS variance_cents,
 MAX(earned_cents-advance_cents,0) AS payable_cents,
 MAX(advance_cents-earned_cents,0) AS recoverable_cents FROM grant_analysis;
