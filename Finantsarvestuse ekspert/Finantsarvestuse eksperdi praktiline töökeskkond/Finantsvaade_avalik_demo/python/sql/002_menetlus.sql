-- Migratsioon 0.1 -> 0.2. Algse skeemi tabelid ja identifikaatorid säilivad.
BEGIN;
CREATE TABLE actor (actor_id TEXT PRIMARY KEY, role TEXT NOT NULL);
INSERT INTO actor VALUES ('analuutik','ANALUUTIK'),('sisukinnitaja','SISU'),('eelarvejuht','EELARVE'),('rtk_demo','RTK');
CREATE TABLE input_document (
 document_id TEXT PRIMARY KEY, raw_json TEXT NOT NULL, content_hash TEXT NOT NULL,
 creator_actor TEXT NOT NULL REFERENCES actor, imported_at TEXT NOT NULL,
 status TEXT NOT NULL DEFAULT 'SISEND' CHECK(status IN ('SISEND','KONTROLLITUD','TAGASTATUD','KOOSKOLASTATUD','KINNITATUD','EDASTATUD','KAJASTATUD','ASENDATUD')), revision INTEGER NOT NULL DEFAULT 1,
 supersedes_document_id TEXT REFERENCES input_document
);
CREATE TABLE check_run (
 run_id INTEGER PRIMARY KEY, document_id TEXT NOT NULL REFERENCES input_document,
 as_of TEXT NOT NULL, checked_at TEXT NOT NULL, rule_version TEXT NOT NULL
);
CREATE TABLE validation_issue (
 issue_id INTEGER PRIMARY KEY, run_id INTEGER NOT NULL REFERENCES check_run,
 code TEXT NOT NULL, severity TEXT NOT NULL CHECK(severity IN ('VIGA','HOIATUS')),
 field TEXT NOT NULL, message TEXT NOT NULL
);
CREATE TABLE document_event (
 event_id INTEGER PRIMARY KEY, document_id TEXT NOT NULL REFERENCES input_document,
 actor_id TEXT NOT NULL REFERENCES actor, occurred_at TEXT NOT NULL,
 action TEXT NOT NULL, old_status TEXT NOT NULL, new_status TEXT NOT NULL, reason TEXT NOT NULL
);
CREATE TRIGGER event_no_update BEFORE UPDATE ON document_event BEGIN SELECT RAISE(ABORT,'Auditilogikirjet ei muudeta'); END;
CREATE TRIGGER event_no_delete BEFORE DELETE ON document_event BEGIN SELECT RAISE(ABORT,'Auditilogikirjet ei kustutata'); END;
CREATE TABLE transfer (
 transfer_id TEXT PRIMARY KEY, document_id TEXT NOT NULL UNIQUE REFERENCES input_document,
 payload_json TEXT NOT NULL, payload_hash TEXT NOT NULL, created_at TEXT NOT NULL,
 accepted_at TEXT, external_reference TEXT UNIQUE
);
CREATE UNIQUE INDEX one_journal_per_invoice ON journal_entry(invoice_id);
UPDATE schema_version SET version='0.2' WHERE version='0.1';
COMMIT;
