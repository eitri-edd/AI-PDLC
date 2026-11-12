"""Preserve the reviewed inventory when adding targeted Tech Scan evidence."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
BASELINE_INVENTORY_SHA256 = "2a95778e2893a165935f7fa2b36d1b7e1353761430c5ef85daeff38530444539"


class TechScanMaintenanceTests(unittest.TestCase):
    def inventory(self):
        return json.loads((ROOT / "site/reference-checks.json").read_text())

    def test_exact_pre_refinement_inventory_is_retained_as_history(self):
        previous = self.inventory()["history"][0]
        canonical = json.dumps(previous, sort_keys=True, separators=(",", ":"))
        self.assertEqual(hashlib.sha256(canonical.encode()).hexdigest(), BASELINE_INVENTORY_SHA256)

    def test_result_counts_describe_current_unique_records(self):
        inventory = self.inventory()
        expected = dict(sorted(Counter(record["result"] for record in inventory["references"]).items()))
        self.assertEqual(inventory["counts"], expected)


if __name__ == "__main__":
    unittest.main()
