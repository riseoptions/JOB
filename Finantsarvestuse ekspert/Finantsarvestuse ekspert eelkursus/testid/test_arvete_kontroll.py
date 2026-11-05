"""Lihtsad deterministlikud ühiktestid arve kontrolli jaoks."""
import sys
import unittest
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "kood"))
from arvete_kontroll import check_row, raha, validate  # noqa: E402


class ArveteKontrolliTestid(unittest.TestCase):
    def setUp(self):
        self.row = {
            "arve_nr": "A-1", "tarnija": "Test OU", "arve_kp": "2026-10-01",
            "tahtaeg": "2026-11-01", "neto": "1000.00", "km_maar": "24",
            "km": "240.00", "kokku": "1240.00", "kulukeskus": "IT",
            "teenuse_periood": "2026-10"
        }

    def test_summad_klapivad(self):
        self.assertEqual(check_row(self.row), [])

    def test_summa_viga(self):
        row = {**self.row, "kokku": "1250.00"}
        self.assertIn("SUMMA_EI_KLAPI", check_row(row))

    def test_km_viga(self):
        row = {**self.row, "km": "230.00", "kokku": "1230.00"}
        self.assertIn("KM_EI_KLAPI", check_row(row))

    def test_duplikaat(self):
        result = validate([self.row, dict(self.row)])
        self.assertTrue(all("VOIMALIK_DUPLIKAAT" in r["vead"] for r in result))

    def test_kulukeskus_puudub(self):
        row = {**self.row, "kulukeskus": ""}
        self.assertIn("KULUKESKUS_PUUDUB", check_row(row))

    def test_eur_sent(self):
        self.assertEqual(raha("1.005"), Decimal("1.01"))


if __name__ == "__main__":
    unittest.main()
