# Demo

## Unsafe Simulation

```bash
python3 -m apps.api.app.cli --out-dir data/reports
```

Expected terminal output:

```text
Ran 3 attacks
Failed 3 attacks
Risk score: 100/100
```

## Safe Simulation

```bash
python3 -m apps.api.app.cli --safe --out-dir data/reports-safe
```

## Review Outputs

```bash
cat data/reports/report.md
cat data/reports/triage.md
cat data/reports/summary.json
```

## Docker CLI

```bash
docker compose run --rm api
```
