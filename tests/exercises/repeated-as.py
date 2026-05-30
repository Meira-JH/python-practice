from __future__ import annotations

import importlib.util
from collections.abc import Callable
from pathlib import Path
from types import ModuleType

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "exercises" / '01-intro' / "03-loop-and-iterations" / "repeated-as.py"
Input = dict[str, int]


def _load_module() -> ModuleType:
    if not MODULE_PATH.exists():
        pytest.fail(
            "Expected implementation file at "
            f"{MODULE_PATH.relative_to(REPO_ROOT)}."
        )

    spec = importlib.util.spec_from_file_location("repeated_as", MODULE_PATH)
    assert spec is not None and spec.loader is not None

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _get_repeated_as(module: ModuleType) -> Callable[[Input], str]:
    try:
        repeated_as = module.repeatedAs
    except AttributeError:
        pytest.fail(f"Expected {MODULE_PATH.name} to define repeatedAs(s, n).")

    if not callable(repeated_as):
        pytest.fail("Expected repeatedAs to be callable.")

    return repeated_as


def test_repeated_as_module_imports_cleanly() -> None:
    try:
        module = _load_module()
    except Exception as exc:
        pytest.fail(f"{MODULE_PATH.name} exited with error on module execution: {exc}")

    _get_repeated_as(module)


@pytest.fixture
def repeated_as() -> Callable[Input]:
    if not MODULE_PATH.exists():
        pytest.skip(
            "Cannot run behavior tests until "
            f"{MODULE_PATH.relative_to(REPO_ROOT)} exists."
        )

    try:
        module = _load_module()
    except Exception as exc:
        pytest.skip(
            f"Cannot run behavior tests until {MODULE_PATH.name} imports: {exc}"
        )

    if not hasattr(module, "repeatedAs"):
        pytest.skip(
            f"Cannot run behavior tests until {MODULE_PATH.name} "
            "defines repeatedAs."
        )

    if not callable(module.repeatedAs):
        pytest.skip("Cannot run behavior tests until repeatedAs is callable.")

    return _get_repeated_as(module)


@pytest.mark.parametrize(
   ("input_data", "expected"),
    [
        pytest.param({"s": "aba", "n": 10}, 7, id="sample-with-partial-repeat"),
        pytest.param({"s": "a", "n": 1_000_000_000_000}, 1_000_000_000_000, id="sample-single-a"),
        pytest.param({"s": "b", "n": 1_000_000_000_000}, 0, id="single-non-a"),
        pytest.param({"s": "abcac", "n": 3}, 1, id="n-shorter-than-string"),
        pytest.param({"s": "abcac", "n": 5}, 2, id="n-equals-string-length"),
        pytest.param({"s": "abcac", "n": 10}, 4, id="n-is-exact-multiple"),
        pytest.param({"s": "abcac", "n": 12}, 5, id="n-has-remainder-with-a"),
        pytest.param({"s": "bcaa", "n": 6}, 2, id="remainder-has-no-a"),
        pytest.param({"s": "aaaa", "n": 9}, 9, id="all-characters-are-a"),
        pytest.param({"s": "epsxy", "n": 25}, 0, id="no-a-anywhere"),
        pytest.param({"s": "ba", "n": 1}, 0, id="first-character-is-not-a"),
        pytest.param({"s": "ab", "n": 1}, 1, id="first-character-is-a"),
        pytest.param({"s": "aab", "n": 1_000_000_000_000}, 666_666_666_667, id="large-n"),
    ],
)
def test_repeated_as_counts_a_characters(
    repeated_as: Callable[[Input], int],
    input_data: Input,
    expected: int,
) -> None:
    assert repeated_as(input_data) == expected


def test_repeated_as_counts_large_input_without_materializing_repeat(
    repeated_as: Callable[[Input], int],
) -> None:
    s = ("b" * 1_000) + "a"
    n = (len(s) * 10_000) + 1_000

    assert repeated_as({"s": s, "n": n}) == 10_000
