# Production Readiness

## Current Status

This repository has a working offline product MVP with deterministic prompt attack simulation, leakage checks, risk summary, Markdown report, triage output, tests, and generated reports. It is portfolio-ready but not production complete yet.

## Required Before Public Release

- Add authorized target adapters before testing live AI apps.
- Add tests for malformed attack packs and empty suites.
- Validate all untrusted inputs.
- Add structured logging without leaking secrets.
- Document local setup and deployment.
- Review all sample data for sensitive content.
- Add authentication and authorization before handling user-supplied prompts or responses.
- Run dependency and secret scans before release.
- Add response redaction and artifact retention controls.

## Definition of Done

- CI passes on pull requests.
- README has setup, usage, and security notes.
- Sample data is safe to publish.
- Error paths are handled clearly.
- No secrets or local machine paths are committed.
- Reports include risk level, failed categories, release guidance, and triage details.
