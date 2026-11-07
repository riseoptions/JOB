-- Etapi 1 esialgne andmeleping. Ei impordi andmeid ega käivita menetlust.
PRAGMA foreign_keys = ON;
CREATE TABLE schema_version (version TEXT PRIMARY KEY);
INSERT INTO schema_version VALUES ('0.1');
CREATE TABLE source_file (
 source_id TEXT PRIMARY KEY, url TEXT NOT NULL, filename TEXT NOT NULL,
 downloaded_at TEXT NOT NULL, sha256 TEXT NOT NULL CHECK(length(sha256)=64),
 provenance TEXT NOT NULL CHECK(provenance='TEGELIK')
);
CREATE TABLE budget_line (
 record_id TEXT PRIMARY KEY, source_id TEXT NOT NULL REFERENCES source_file,
 sheet TEXT NOT NULL, cell TEXT NOT NULL, line_id TEXT NOT NULL,
 label TEXT NOT NULL, metric TEXT NOT NULL, period_start TEXT NOT NULL,
 period_end TEXT NOT NULL, budget_version TEXT NOT NULL, scope TEXT NOT NULL,
 row_kind TEXT NOT NULL, amount_cents INTEGER, raw_value TEXT, raw_unit TEXT NOT NULL,
 provenance TEXT NOT NULL CHECK(provenance='TULETATUD'), sign_policy TEXT NOT NULL
);
CREATE TABLE actual_observation (
 record_id TEXT PRIMARY KEY, source_id TEXT NOT NULL REFERENCES source_file,
 sheet TEXT NOT NULL, cell TEXT NOT NULL, label TEXT NOT NULL, scope TEXT NOT NULL,
 measure TEXT NOT NULL, row_kind TEXT NOT NULL, period_start TEXT NOT NULL,
 period_end TEXT NOT NULL, period_kind TEXT NOT NULL CHECK(period_kind IN ('kuu','YTD')),
 amount_cents INTEGER, raw_value TEXT, raw_unit TEXT NOT NULL,
 provenance TEXT NOT NULL CHECK(provenance='TULETATUD'), missing_reason TEXT
);
-- Järgnev on tulevaste etappide kavand, mitte toimiv arvekontroll.
CREATE TABLE invoice (
 invoice_id TEXT PRIMARY KEY, supplier_id TEXT NOT NULL, invoice_number TEXT NOT NULL,
 invoice_date TEXT NOT NULL, service_date TEXT, due_date TEXT,
 net_cents INTEGER NOT NULL, vat_cents INTEGER NOT NULL, gross_cents INTEGER NOT NULL,
 status TEXT NOT NULL, provenance TEXT NOT NULL CHECK(provenance='SUNTEETILINE')
);
CREATE TABLE invoice_line (
 line_id TEXT PRIMARY KEY, invoice_id TEXT NOT NULL REFERENCES invoice,
 description TEXT NOT NULL, net_cents INTEGER NOT NULL, vat_rate TEXT NOT NULL,
 vat_cents INTEGER NOT NULL, account TEXT, cost_center TEXT
);
CREATE TABLE workflow_event (
 event_id INTEGER PRIMARY KEY, invoice_id TEXT NOT NULL REFERENCES invoice,
 occurred_at TEXT NOT NULL, actor_role TEXT NOT NULL, action TEXT NOT NULL, reason TEXT
);
CREATE TABLE check_result (
 result_id INTEGER PRIMARY KEY, invoice_id TEXT NOT NULL REFERENCES invoice,
 rule_code TEXT NOT NULL, severity TEXT NOT NULL, message TEXT NOT NULL, checked_at TEXT NOT NULL
);
CREATE TABLE journal_entry (
 entry_id TEXT PRIMARY KEY, invoice_id TEXT REFERENCES invoice, posting_date TEXT NOT NULL
);
CREATE TABLE journal_line (
 line_id INTEGER PRIMARY KEY, entry_id TEXT NOT NULL REFERENCES journal_entry,
 account TEXT NOT NULL, debit_cents INTEGER NOT NULL DEFAULT 0 CHECK(debit_cents>=0),
 credit_cents INTEGER NOT NULL DEFAULT 0 CHECK(credit_cents>=0),
 CHECK(NOT(debit_cents>0 AND credit_cents>0))
);
-- Kande D=K tasakaal on mitme rea reegel; rakendus kontrollib seda tulevikus.
