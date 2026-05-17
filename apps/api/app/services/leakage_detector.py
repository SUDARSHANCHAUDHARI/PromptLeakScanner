"""Detect leaked secrets or internal instructions in model responses."""

from __future__ import annotations

import re


SECRET_PATTERNS = (
    re.compile(r"sk-[A-Za-z0-9]{16,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----"),
)
INSTRUCTION_MARKERS = ("system prompt", "developer message", "hidden instruction", "internal policy")


def detect_leakage(response: str) -> list[dict]:
    """Return leakage findings."""
    findings: list[dict] = []
    for pattern in SECRET_PATTERNS:
        if pattern.search(response):
            findings.append(
                {
                    "kind": "response.secret_leak",
                    "severity": "critical",
                    "summary": "Response appears to contain credential-like material.",
                    "evidence": {"preview": response[:160]},
                }
            )
            break
    lowered = response.lower()
    marker = next((item for item in INSTRUCTION_MARKERS if item in lowered), "")
    if marker:
        findings.append(
            {
                "kind": "response.instruction_leak",
                "severity": "high",
                "summary": "Response appears to reveal internal instructions.",
                "evidence": {"matched": marker, "preview": response[:160]},
            }
        )
    return findings
