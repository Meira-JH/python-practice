from __future__ import annotations

import importlib.util
from collections.abc import Callable
from pathlib import Path
from types import ModuleType

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = (
    REPO_ROOT / "algorithms" / "hashmaps-and-sets" / "long-consecutive.py"
)


def _load_module() -> ModuleType:
    spec = importlib.util.spec_from_file_location("long_consecutive", MODULE_PATH)
    assert spec is not None and spec.loader is not None

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _get_find_longest_consec(
    module: ModuleType,
) -> Callable[[dict[str, list[int]]], int]:
    try:
        return module.findLongestConsec
    except AttributeError:
        pytest.fail("Expected long-consecutive.py to define findLongestConsec(input).")


def test_long_consecutive_module_imports_cleanly() -> None:
    try:
        module = _load_module()
    except Exception as exc:
        pytest.fail(f"{MODULE_PATH.name} exited with error on module execution: {exc}")

    _get_find_longest_consec(module)


@pytest.fixture
def find_longest_consec() -> Callable[[dict[str, list[int]]], int]:
    try:
        module = _load_module()
    except Exception as exc:
        pytest.skip(
            f"Cannot run behavior tests until {MODULE_PATH.name} imports: {exc}"
        )

    return _get_find_longest_consec(module)


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        pytest.param([], 0, id="empty-list"),
        pytest.param([7], 1, id="single-number"),
        pytest.param([2, 1], 2, id="two-numbers-consecutive-reversed"),
        pytest.param([1, 3], 1, id="two-numbers-with-gap"),
        pytest.param([5, 5, 5], 1, id="all-duplicates"),
        pytest.param([1, 2, 2, 3], 3, id="duplicates-inside-sequence"),
        pytest.param([100, 4, 200, 1, 3, 2], 4, id="example-one"),
        pytest.param([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9, id="example-two"),
        pytest.param([-4, -2, -3, -1], 4, id="negative-only-sequence"),
        pytest.param([-2, -1, 0, 1, 2], 5, id="sequence-crosses-zero"),
        pytest.param([10, 11, 12, 1, 2, 3], 3, id="tie-between-sequences"),
        pytest.param([50, 5, 6, 7, 100, 101, 102, 103], 4, id="multiple-runs"),
        pytest.param([1, 2, 4, 5, 6, 10], 3, id="gaps-break-sequences"),
        pytest.param([3, -1, 0, 1, 2, -2, 5, 4], 6, id="unsorted-mixed-signs"),
        pytest.param(
            [-10**9, -10**9 + 1, 10**9 - 1, 10**9],
            2,
            id="constraint-boundaries",
        ),
        pytest.param(
            [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6],
            7,
            id="long-run-with-noisy-duplicates",
        ),
    ],
)
def test_find_longest_consecutive_edge_cases(
    find_longest_consec: Callable[[dict[str, list[int]]], int],
    nums: list[int],
    expected: int,
) -> None:
    assert find_longest_consec({"nums": nums}) == expected


def test_find_longest_consecutive_handles_large_unsorted_input(
    find_longest_consec: Callable[[dict[str, list[int]]], int],
) -> None:
    long_run = list(range(-2_500, 2_500))
    noise = [10**9, -10**9, 42, 42, 99_999]
    nums = noise[:2] + long_run[::2] + noise[2:] + long_run[1::2]

    assert find_longest_consec({"nums": nums}) == 5_000
