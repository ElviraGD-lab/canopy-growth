"""First tests: the package imports, the configs are valid, the chain stops on a failed check."""

from pathlib import Path

import pytest

import canopy_growth
from canopy_growth.pipeline import Check, Step, StepFailed, load_yaml, run

CONFIG = Path(__file__).resolve().parents[1] / "config"


def test_version_is_set():
    assert canopy_growth.__version__


def test_pajares_frame_is_8_by_8_km_in_utm30n():
    site = load_yaml(CONFIG / "pajares.yaml")
    assert site["crs"] == "EPSG:25830"
    xmin, ymin, xmax, ymax = site["frame"]
    assert (xmax - xmin, ymax - ymin) == (8000, 8000)


def test_acceptance_file_loads():
    assert isinstance(load_yaml(CONFIG / "acceptance.yaml"), dict)


def _step(name, value, threshold):
    return Step(name, lambda cfg: Check(name, value, threshold, value <= threshold))


def test_chain_runs_all_steps_when_checks_pass():
    checks = run({}, [_step("a", 1.0, 2.0), _step("b", 0.5, 1.0)])
    assert [c.step for c in checks] == ["a", "b"]


def test_chain_stops_at_first_failed_check():
    second_ran = []
    steps = [
        _step("a", 3.0, 2.0),
        Step("b", lambda cfg: second_ran.append(True) or Check("b", 0, 1, True)),
    ]
    with pytest.raises(StepFailed):
        run({}, steps)
    assert not second_ran
