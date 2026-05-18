"""Tests for PromptLeak Scanner MVP."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from apps.api.app.services.prompt_attack_library import load_attacks
from apps.api.app.services.report_builder import build_triage_report, summarize
from apps.api.app.services.test_runner import run_suite


ROOT = Path(__file__).resolve().parents[1]
ATTACKS = sorted((ROOT / "attacks").glob("*.yaml"))


class PromptLeakTests(unittest.TestCase):
    def test_loads_attack_files(self) -> None:
        attacks = load_attacks(ATTACKS)

        self.assertEqual(len(attacks), 3)
        self.assertEqual({attack["category"] for attack in attacks}, {"jailbreak", "prompt_injection", "secret_extraction"})

    def test_detects_unsafe_simulation(self) -> None:
        results = run_suite(load_attacks(ATTACKS), unsafe_simulation=True)
        summary = summarize(results)

        self.assertEqual(summary["attacks"], 3)
        self.assertEqual(summary["failed"], 3)
        self.assertEqual(summary["risk_score"], 100)
        self.assertEqual(summary["risk_level"], "high")
        self.assertEqual(1, summary["severity_counts"]["critical"])
        self.assertIn("Block release", summary["recommended_response"])

    def test_cli_writes_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [sys.executable, "-m", "apps.api.app.cli", "--out-dir", tmp],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            summary = json.loads(Path(tmp, "summary.json").read_text(encoding="utf-8"))
            report = Path(tmp, "report.md").read_text(encoding="utf-8")
            triage = Path(tmp, "triage.md").read_text(encoding="utf-8")

            self.assertIn("Ran 3 attacks", result.stdout)
            self.assertEqual(summary["failed"], 3)
            self.assertIn("PromptLeak Scanner Report", report)
            self.assertIn("Priority Queue", report)
            self.assertIn("Release Checklist", triage)

    def test_builds_triage_report(self) -> None:
        results = run_suite(load_attacks(ATTACKS), unsafe_simulation=True)
        triage = build_triage_report(results)

        self.assertIn("PromptLeak Scanner Triage", triage)
        self.assertIn("Failed Attacks", triage)


if __name__ == "__main__":
    unittest.main()
