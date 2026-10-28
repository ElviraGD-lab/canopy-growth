"""Run the canopy-growth steps in order and stop at the first failed check.

Each step is a function that takes the site configuration and returns a check:
the number it measured and whether that number passed its threshold. The
thresholds live in ``config/acceptance.yaml`` and are committed before any
result is computed, so a check cannot be tuned to the result afterwards.

The list ``STEPS`` is empty until the first plan step (3.1) is implemented.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import yaml


@dataclass(frozen=True)
class Check:
    """Result of one step: what was measured and whether it passed."""

    step: str
    value: float
    threshold: float
    passed: bool


@dataclass(frozen=True)
class Step:
    """One plan step: a name and a function config -> Check."""

    name: str
    run: Callable[[dict], Check]


class StepFailed(RuntimeError):
    """Raised when a step's check does not pass; the chain stops here."""


STEPS: list[Step] = []


def load_yaml(path: str | Path) -> dict:
    """Read a YAML file and return its content as a dict (empty file -> {})."""
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def run(config: dict, steps: list[Step] | None = None) -> list[Check]:
    """Run the steps in order; return all checks, stop at the first failure."""
    checks: list[Check] = []
    for step in STEPS if steps is None else steps:
        check = step.run(config)
        checks.append(check)
        if not check.passed:
            raise StepFailed(
                f"{step.name}: {check.value} did not pass threshold {check.threshold}"
            )
    return checks
