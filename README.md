# PromptLeak Scanner

**Goal:** Security testing tool for AI apps and agents.

**MVP:** Run prompt injection tests against a target prompt/app.

## Core Features

- prompt injection test suite
- secret leakage tests
- unsafe response detection
- jailbreak attempt tracking
- AI risk report

## Suggested Stack

FastAPI, React, YAML test suites, Docker.

## Status

Working CLI MVP.

## Quick Start

Run the built-in attack suite against the deterministic unsafe simulation:

```bash
python3 -m apps.api.app.cli --out-dir data/reports
```

Run it against the safe simulation:

```bash
python3 -m apps.api.app.cli --safe --out-dir data/reports-safe
```

Run tests:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

## MVP Capabilities

- Loads prompt injection, secret extraction, and jailbreak attack definitions.
- Simulates safe and unsafe target responses for repeatable local testing.
- Detects secret leakage, internal instruction leakage, and unsafe compliance.
- Scores risk and generates JSON results, JSON summary, and a Markdown report.

## Repository Status

This repository contains the production-ready foundation for the PromptLeak Scanner MVP. The current codebase is scaffolded and ready for focused implementation work.

## Production Foundation

- Private GitHub repository linked to `main`
- Initial MVP scaffold committed
- CI repository-health workflow
- Security policy
- Contribution guide
- Pull request and issue templates
- Production readiness checklist
- Safe ignore rules for local secrets and generated files
