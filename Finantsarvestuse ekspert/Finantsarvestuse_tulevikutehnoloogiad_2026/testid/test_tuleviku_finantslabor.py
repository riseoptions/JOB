"""Deterministlikud kontrolltestid uue labori jaoks."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "kood"))
from tuleviku_finantslabor import build_report, euro_to_cents, make_demo_rows, validate_rows
from rag_otsing_demo import retrieve, build_prompt


class TulevikuLaboriTestid(unittest.TestCase):
    def test_sentides_arvutamine(self):
        self.assertEqual(euro_to_cents("1.005"), 101)
        self.assertEqual(euro_to_cents("0.10"), 10)

    def test_suure_arve_kontroll_ei_ole_summa_viga(self):
        rows = validate_rows(make_demo_rows())
        issues = rows[19]["kontrollid"].split(",")
        self.assertIn("EBATAVALISELT_SUUR_ARVE", issues)
        self.assertNotIn("SUMMA_EI_KLAPI", issues)

    def test_aritmeetiline_viga(self):
        rows = validate_rows(make_demo_rows())
        self.assertIn("SUMMA_EI_KLAPI", rows[4]["kontrollid"])

    def test_duplikaadid(self):
        rows = validate_rows(make_demo_rows())
        self.assertIn("VOIMALIK_DUPLIKAAT", rows[8]["kontrollid"])
        self.assertIn("VOIMALIK_DUPLIKAAT", rows[2]["kontrollid"])

    def test_puuduv_kulukeskus(self):
        rows = validate_rows(make_demo_rows())
        self.assertIn("KULUKESKUS_PUUDUB", rows[12]["kontrollid"])

    def test_vigane_kuupaev(self):
        rows = validate_rows(make_demo_rows())
        self.assertIn("VIGANE_KUUPAEV", rows[14]["kontrollid"])

    def test_koond(self):
        r = build_report(validate_rows(make_demo_rows()))
        self.assertEqual(r["kirjeid"], 50)
        self.assertGreaterEqual(r["vajab_ulevaatust"], 5)

    def test_rag_otsib_allika(self):
        self.assertTrue(retrieve("Kes kinnitab arve sisulise vastuvõtmise?"))
        self.assertIn("ALLIKAS:", build_prompt("Kes kinnitab arve sisulise vastuvõtmise?"))

    def test_rag_ei_motle_info_valja(self):
        self.assertIn("ei leidunud", build_prompt("galaktikate must auk"))


if __name__ == "__main__":
    unittest.main()
