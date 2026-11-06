-- Ava olemasolev etapi 2 andmebaas DBeaveris või sqlite3-ga.
-- 1. Dokumentide seis. Ka vigased toorread on alles.
SELECT document_id,status,revision,supersedes_document_id FROM input_document ORDER BY document_id;
-- 2. Ainult iga dokumendi VIIMASE kontrolli vead. Kontrolliajalugu ei liideta kokku.
SELECT r.document_id,r.as_of,i.code,i.severity,i.field,i.message
FROM check_run r JOIN validation_issue i USING(run_id)
WHERE r.run_id=(SELECT MAX(x.run_id) FROM check_run x WHERE x.document_id=r.document_id)
ORDER BY r.document_id,i.issue_id;
-- 3. Auditijälg ühe dokumendi kohta.
SELECT occurred_at,actor_id,action,old_status,new_status,reason FROM document_event
WHERE document_id='DEMO-001' ORDER BY event_id;
-- 4. Kande tasakaal. Iga tulemuse vahe peab olema 0.
SELECT e.entry_id,e.posting_date,SUM(l.debit_cents) AS deebet_sendid,
SUM(l.credit_cents) AS kreedit_sendid,SUM(l.debit_cents-l.credit_cents) AS vahe_sendid
FROM journal_entry e JOIN journal_line l USING(entry_id) GROUP BY e.entry_id,e.posting_date;
-- 5. Simuleeritud edastus ja vastuvõtt.
SELECT transfer_id,document_id,created_at,accepted_at,external_reference FROM transfer;
-- 6. Ühe arve summa; sendid jäävad täpseks täisarvuks.
SELECT invoice_id,net_cents,vat_cents,gross_cents,net_cents+vat_cents-gross_cents AS vahe_sendid FROM invoice;
PRAGMA foreign_key_check;
