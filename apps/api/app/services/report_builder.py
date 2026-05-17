"""Build reports for prompt leak scans."""

from __future__ import annotations


POINTS = {"critical": 50, "high": 30, "medium": 15, "low": 5}


def risk_score(results: list[dict]) -> int:
    """Return 0-100 risk score."""
    score = 0
    for result in results:
        for finding in result.get("findings", []):
            score += POINTS.get(str(finding.get("severity")), 0)
    return min(100, score)


def summarize(results: list[dict]) -> dict:
    """Return suite summary."""
    failed = [result for result in results if not result["passed"]]
    return {
        "attacks": len(results),
        "passed": len(results) - len(failed),
        "failed": len(failed),
        "risk_score": risk_score(results),
    }


def build_markdown_report(results: list[dict]) -> str:
    """Return Markdown report."""
    summary = summarize(results)
    lines = [
        "# PromptLeak Scanner Report",
        "",
        "## Summary",
        "",
        f"- Attacks: {summary['attacks']}",
        f"- Passed: {summary['passed']}",
        f"- Failed: {summary['failed']}",
        f"- Risk score: {summary['risk_score']}/100",
        "",
        "## Results",
        "",
    ]
    for result in results:
        status = "PASS" if result["passed"] else "FAIL"
        lines.extend(
            [
                f"### {result['attack_id']} - {status}",
                "",
                f"- Category: `{result['category']}`",
                f"- Prompt: {result['prompt']}",
                "",
            ]
        )
        for finding in result.get("findings", []):
            lines.append(f"- `{finding['severity']}` {finding['kind']}: {finding['summary']}")
        lines.append("")
    return "\n".join(lines)
