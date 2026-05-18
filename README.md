# PromptLeak Scanner

[![Python](https://img.shields.io/badge/Python-3.12-blue)](#) [![Status](https://img.shields.io/badge/status-product%20polish-green)](#) [![Security](https://img.shields.io/badge/security-defensive%20lab-purple)](#)

Security test runner for prompt injection, leakage, jailbreak, and unsafe-response checks in AI apps.

- **Portfolio group:** Product-style SaaS project
- **Status:** Product polish implemented, tested, committed, and pushed to GitHub
- **GitHub:** https://github.com/SUDARSHANCHAUDHARI/PromptLeakScanner
- **Local path:** `/Users/screencloudsudarshan/SUDARSHAN_CODE/sudarshan_repos/CyberSecurity/PromptLeakScanner`

## MVP Snapshot

This repository includes a working MVP with safe attack definitions, deterministic safe/unsafe simulations, JSON outputs, Markdown risk report, triage handoff, tests, and Docker demo support.

## Safe Use

This project is defensive and analysis-focused. Use only with logs, systems, repositories, and lab environments you own or have permission to assess.

## Core Features

- prompt injection test suite
- secret leakage tests
- unsafe response detection
- jailbreak attempt tracking
- AI risk report
- release risk level
- failed category breakdown
- triage handoff

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

Generated outputs:

- `data/reports/results.json`
- `data/reports/summary.json`
- `data/reports/report.md`
- `data/reports/triage.md`

## Docker Demo

```bash
docker compose run --rm api
```

## Product Polish Capabilities

- Loads prompt injection, secret extraction, and jailbreak attack definitions.
- Simulates safe and unsafe target responses for repeatable local testing.
- Detects secret leakage, internal instruction leakage, and unsafe compliance.
- Scores risk and generates JSON results, JSON summary, and a Markdown report.
- Adds risk level, severity counts, failed category breakdown, and release guidance.
- Generates an analyst triage report for failed attacks.

## Roadmap

- Add real target adapter behind a safe authorization boundary
- Add attack pack tagging and severity policy controls
- Add regression baselines for prompt updates
- Add web dashboard for result comparison
- Add CI gate mode for AI app releases
