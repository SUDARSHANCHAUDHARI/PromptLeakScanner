# PromptLeak Scanner

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](#requirements)
[![Status](https://img.shields.io/badge/status-MVP-green)](#status)
[![Security](https://img.shields.io/badge/security-defensive%20lab-purple)](#safe-use)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Security test runner for AI applications. Probes prompt injection, system prompt leakage, role-bypass, and unsafe-response patterns to find weaknesses in LLM-backed apps before attackers do.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Docker Demo](#docker-demo)
- [Safe Use](#safe-use)
- [Status](#status)
- [Roadmap](#roadmap)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)
- [About](#about)

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

## Documentation

Full project documentation lives in [`docs/`](docs/):

- [Architecture](docs/ARCHITECTURE.md) — component design and data flow
- [Demo](docs/DEMO.md) — step-by-step demo walkthrough
- [Security Notes](docs/SECURITY_NOTES.md) — defensive-use guidance and threat model
- [Production Readiness](docs/PRODUCTION_READINESS.md) — gaps between MVP and production
- [Project Plan](docs/PROJECT_PLAN.md) — scope and milestones
- [Roadmap](docs/ROADMAP.md) — planned features
- [Release Notes](docs/RELEASE_NOTES.md) — version history

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md) before opening a pull request. To report a security issue, see [SECURITY.md](SECURITY.md).

## License

Released under the [MIT License](LICENSE). You are free to use, modify, and distribute this software with attribution.

---

## About

I'm Sudarshan Chaudhari, a Senior Quality Engineer, Test Automation specialist, and AI systems builder based in Bangkok, Thailand.

I have 13+ years of experience in software quality engineering, working across SaaS, fintech, gaming, web, mobile, cloud, and digital signage platforms. My background combines hands-on test automation with QA leadership, test strategy, CI/CD, release quality, production investigation, and cross-platform validation.

Alongside my professional QA career, I run [SudarshanTechLabs](https://sudarshantechlabs.com/), my independent engineering and product lab where I design, build, test, and ship software across Android, web, AI, cybersecurity, developer tooling, and cross-platform applications.

### What I work on

- ⚙️ **Quality Engineering & Test Automation** — Playwright, Selenium, Cypress, Appium, API testing, automation frameworks, end-to-end testing, CI/CD, release gates, GitHub Actions, risk-based testing, and production validation
- 🤖 **AI Systems & Automation** — AI agents, multi-agent orchestration, MCP servers, AI-assisted QA, prompt tooling, developer workflows, automation systems, and Claude Code plugins
- 📱 **Mobile & Cross-Platform Applications** — Android applications built with Kotlin and Jetpack Compose, Google Play releases, automated build and publishing pipelines, and cross-platform development spanning iOS, web, Windows, and macOS
- 🌐 **Web Applications & Platforms** — Full-stack applications using Next.js, TypeScript, Firebase, Cloudflare, REST APIs, and modern web infrastructure
- 🛠️ **Developer Tooling & CLI Engineering** — Rust, Python, TypeScript, CLI utilities, multi-repository tooling, build automation, release tooling, and engineering productivity systems
- 🛡️ **Cybersecurity & Observability** — Threat detection, log analysis, security auditing, vulnerability assessment, monitoring, and security-focused developer tools
- 📺 **Digital Signage & Device Platforms** — Content validation, playback testing, device compatibility, production investigation, monitoring, and QA across diverse hardware and operating-system environments

My work sits at the intersection of quality engineering, automation, AI, and software development. I approach products with a QA mindset from the beginning: understanding failure modes, designing for testability, automating repetitive work, and building release confidence into the engineering process.

Through SudarshanTechLabs, I also build products and tools from idea to production, covering architecture, development, testing, CI/CD, release automation, monitoring, and ongoing maintenance.

🌐 [sudarshantechlabs.com](https://sudarshantechlabs.com/) · 💼 [LinkedIn](https://linkedin.com/in/sudarshan-chaudhari) · 🐙 [GitHub](https://github.com/SUDARSHANCHAUDHARI) · ✉️ [sunny.sudarshan@gmail.com](mailto:sunny.sudarshan@gmail.com)
