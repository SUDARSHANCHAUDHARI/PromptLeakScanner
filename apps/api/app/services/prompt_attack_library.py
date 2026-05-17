"""Load prompt attack definitions."""

from __future__ import annotations

from pathlib import Path


def load_attack_file(path: Path) -> list[dict]:
    """Load a small dependency-free YAML subset.

    Supported format:
    items:
      - id: attack-id
        category: prompt_injection
        prompt: text
        expected_risk: high
    """
    attacks: list[dict] = []
    current: dict[str, str] | None = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line == "items:":
            continue
        if line.startswith("- "):
            if current:
                attacks.append(current)
            current = {}
            line = line[2:].strip()
        if ":" in line and current is not None:
            key, value = line.split(":", 1)
            current[key.strip()] = value.strip().strip('"')
    if current:
        attacks.append(current)
    return attacks


def load_attacks(paths: list[Path]) -> list[dict]:
    """Load attack definitions from several files."""
    attacks: list[dict] = []
    for path in paths:
        attacks.extend(load_attack_file(path))
    return attacks
