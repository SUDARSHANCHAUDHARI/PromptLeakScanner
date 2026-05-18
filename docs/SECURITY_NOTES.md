# Security Notes

PromptLeak Scanner is defensive and lab-safe.

## Safe Use

- Test only AI systems you own or have permission to assess.
- Do not add real secrets to attack packs, fixtures, or expected responses.
- Treat generated reports as sensitive if they include model responses from private systems.

## Current Boundary

The MVP uses deterministic local simulations and does not call external AI APIs. The unsafe response is synthetic and designed only to exercise detectors.

## Before Production

- Add target authorization controls.
- Add response redaction.
- Add provider timeouts and audit logging.
- Add per-suite policy controls before using as a release gate.
