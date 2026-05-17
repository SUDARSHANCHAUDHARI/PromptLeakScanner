# PromptLeak Scanner

[![Python](https://img.shields.io/badge/Python-3.12-blue)](#) [![Status](https://img.shields.io/badge/status-MVP-green)](#) [![Security](https://img.shields.io/badge/security-defensive%20lab-purple)](#)

Security test runner for prompt injection, leakage, jailbreak, and unsafe-response checks in AI apps.

- **Portfolio group:** Product-style SaaS project
- **Status:** MVP implemented, tested, committed, and pushed to GitHub
- **GitHub:** https://github.com/SUDARSHANCHAUDHARI/PromptLeakScanner
- **Local path:** `/Users/screencloudsudarshan/SUDARSHAN_CODE/sudarshan_repos/CyberSecurity/PromptLeakScanner`

## MVP Snapshot

This repository includes a working MVP with safe sample data, deterministic detection or analysis logic, local tests, and generated output reports where relevant. It is ready for README/demo polish or deeper product work.

## Safe Use

This project is defensive and analysis-focused. Use only with logs, systems, repositories, and lab environments you own or have permission to assess.

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

## Roadmap

- Polish sample output screenshots or terminal demos
- Add architecture diagram and deeper implementation notes
- Expand test coverage around edge cases
- Add Docker or local demo workflow where useful
- Prepare `v0.1.0-mvp` release notes
