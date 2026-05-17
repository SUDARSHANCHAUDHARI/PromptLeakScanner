"""Run prompt leak attack suites."""

from __future__ import annotations

from apps.api.app.services.response_analyzer import analyze_response


SAFE_RESPONSE = "I cannot reveal hidden instructions or secrets. I can help with a safe summary instead."


def simulated_target_response(attack: dict, unsafe: bool = False) -> str:
    """Return deterministic safe/unsafe sample responses for MVP testing."""
    if not unsafe:
        return SAFE_RESPONSE
    category = attack.get("category")
    if category == "secret_extraction":
        return "Sure, here is a secret key: sk-test1234567890abcdef"
    if category == "prompt_injection":
        return "Here is the system prompt and developer message you asked for."
    return "I can reveal a bypass safety method."


def run_suite(attacks: list[dict], unsafe_simulation: bool = True) -> list[dict]:
    """Run attacks against the deterministic MVP target simulation."""
    return [
        analyze_response(attack, simulated_target_response(attack, unsafe=unsafe_simulation))
        for attack in attacks
    ]
