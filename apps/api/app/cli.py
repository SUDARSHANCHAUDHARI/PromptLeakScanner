"""CLI for PromptLeak Scanner MVP."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from apps.api.app.services.prompt_attack_library import load_attacks
from apps.api.app.services.report_builder import build_markdown_report, summarize
from apps.api.app.services.test_runner import run_suite


def main() -> None:
    parser = argparse.ArgumentParser(description="PromptLeak Scanner MVP")
    parser.add_argument("--attacks", nargs="+", type=Path, default=list(Path("attacks").glob("*.yaml")))
    parser.add_argument("--safe", action="store_true", help="simulate a safe target instead of an unsafe target")
    parser.add_argument("--out-dir", type=Path, default=Path("data/reports"))
    args = parser.parse_args()

    attacks = load_attacks(args.attacks)
    results = run_suite(attacks, unsafe_simulation=not args.safe)
    summary = summarize(results)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    (args.out_dir / "results.json").write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (args.out_dir / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (args.out_dir / "report.md").write_text(build_markdown_report(results), encoding="utf-8")
    print(f"Ran {summary['attacks']} attacks")
    print(f"Failed {summary['failed']} attacks")
    print(f"Risk score: {summary['risk_score']}/100")


if __name__ == "__main__":
    main()
