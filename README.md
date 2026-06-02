# PromptLeak Scanner

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](#requirements)
[![Status](https://img.shields.io/badge/status-MVP-green)](#status)
[![Security](https://img.shields.io/badge/security-defensive%20lab-purple)](#safe-use)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Security test runner for AI applications. Probes prompt injection, system prompt leakage, role-bypass, and unsafe-response patterns to find weaknesses in LLM-backed apps before attackers do.

---

## Overview

PromptLeak Scanner is a defensive testing tool for engineers building LLM-backed applications. It loads an attack prompt library, runs each attack against a configured target (or against a captured response set), and analyzes the responses for leaked system prompts, sensitive data, role-bypass behavior, and unsafe outputs. Outputs include findings, risk-scored summary, and an engineer-friendly remediation report.

The current MVP is a Python CLI. A FastAPI + React web dashboard is scaffolded under `apps/` for future development.

## Features

- Attack prompt library across multiple categories
- Test runner with safe-mode (uses captured fixtures)
- Detects system prompt leakage in responses
- Detects sensitive data leakage (keys, PII patterns)
- Detects role-bypass and instruction-override success
- Scores each finding by severity and confidence
- Outputs JSON findings, risk summary, Markdown report, and triage handoff

## Requirements

- Python 3.10 or newer
- Linux, macOS, or Windows
- No third-party Python packages (standard library only)
- Optional: Docker for the demo container

## Installation

```bash
git clone https://github.com/SUDARSHANCHAUDHARI/PromptLeakScanner.git
cd PromptLeakScanner
pip install .
```

This registers the `prompt-leak-scanner` CLI command.

To run without installing:

```bash
python3 main.py --help
```

## Usage

Run in safe-mode against captured fixture responses:

```bash
python3 main.py --safe --out-dir data/reports
```

Generated outputs in `data/reports/`:

- `findings.json` — detected leaks and unsafe responses
- `summary.json` — counts and severity breakdown
- `report.md` — Markdown remediation report
- `triage.md` — analyst triage checklist

## Project Structure

```
PromptLeakScanner/
├── apps/
│   ├── api/        FastAPI app scaffold (planned)
│   └── web/        React/Next.js app scaffold (planned)
├── attacks/        Attack prompt library
├── data/
│   ├── samples/    Captured fixture responses for safe-mode testing
│   └── reports/    Example generated output
├── docker/         Dockerfile + compose support
├── docs/           Architecture, security notes, demo
├── scripts/        Setup, seed, run helpers
├── tests/          Unit and integration tests
├── main.py         CLI entrypoint
├── pyproject.toml  Package metadata
└── LICENSE
```

## Testing

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

## Docker Demo

```bash
docker compose run --rm api
```

## Safe Use

This project is defensive and testing-focused. Use only against LLM applications you own or have explicit written permission to test. The included attack library is for authorized security testing only.

## Status

Working Python CLI MVP. Web dashboard scaffold present but not yet implemented.

## Roadmap

- Live target adapters (OpenAI, Anthropic, local models)
- Multi-turn attack chains
- Configurable detector packs per industry / use case
- CI/CD integration for AI app regression testing
- Web dashboard for findings triage

## License

Released under the [MIT License](LICENSE). You are free to use, modify, and distribute this software with attribution.

## Author

**Sudarshan Chaudhari** — [SudarshanTechLabs](https://github.com/SUDARSHANCHAUDHARI)
Bangkok, Thailand

For inquiries: open an issue on [GitHub](https://github.com/SUDARSHANCHAUDHARI/PromptLeakScanner/issues).
