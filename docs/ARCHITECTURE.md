# Architecture

PromptLeak Scanner is a defensive test runner for AI app prompt-injection and leakage checks.

## Flow

1. `prompt_attack_library.py` loads local YAML attack definitions.
2. `test_runner.py` runs attacks against deterministic safe or unsafe target simulations.
3. `response_analyzer.py` checks unsafe compliance and leaked internal instructions.
4. `leakage_detector.py` checks credential-like and instruction-like response patterns.
5. `report_builder.py` writes JSON, Markdown risk, and triage outputs.

## Outputs

- result matrix JSON
- suite summary JSON
- Markdown risk report
- Markdown triage handoff

The current MVP does not send prompts to external models or live applications.
