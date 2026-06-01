from __future__ import annotations

import importlib.util
from collections.abc import Callable
from pathlib import Path
from types import ModuleType

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = (
    REPO_ROOT / "algorithms" / "02-two-pointers" / "is-palindrome.py"
)


def _load_module() -> ModuleType:
    spec = importlib.util.spec_from_file_location("is_palindrome", MODULE_PATH)
    assert spec is not None and spec.loader is not None

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _get_is_palindrome(module: ModuleType) -> Callable[[str], bool]:
    try:
        is_palindrome = module.isPalindrome
    except AttributeError:
        pytest.fail("Expected is-palindrome.py to define isPalindrome(s).")

    if not callable(is_palindrome):
        pytest.fail("Expected isPalindrome to be callable.")

    return is_palindrome


def test_is_palindrome_module_imports_cleanly() -> None:
    try:
        module = _load_module()
    except Exception as exc:
        pytest.fail(f"{MODULE_PATH.name} exited with error on module execution: {exc}")

    _get_is_palindrome(module)


@pytest.fixture
def is_palindrome() -> Callable[[str], bool]:
    try:
        module = _load_module()
    except Exception as exc:
        pytest.skip(
            f"Cannot run behavior tests until {MODULE_PATH.name} imports: {exc}"
        )

    if not hasattr(module, "isPalindrome"):
        pytest.skip(
            f"Cannot run behavior tests until {MODULE_PATH.name} "
            "defines isPalindrome."
        )

    if not callable(module.isPalindrome):
        pytest.skip("Cannot run behavior tests until isPalindrome is callable.")

    return _get_is_palindrome(module)


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        pytest.param("A man, a plan, a canal: Panama", True, id="sample-true"),
        pytest.param("race a car", False, id="sample-false"),
        pytest.param(" ", True, id="sample-space-only"),
        pytest.param("!!!", True, id="punctuation-only"),
        pytest.param("a.", True, id="single-letter-with-punctuation"),
        pytest.param("Aa", True, id="case-insensitive-two-letters"),
        pytest.param("ab", False, id="two-different-letters"),
        pytest.param("No lemon, no melon", True, id="phrase-palindrome"),
        pytest.param("Was it a car or a cat I saw?", True, id="mixed-case-phrase"),
        pytest.param("0P", False, id="digit-and-letter-not-equal"),
        pytest.param("12321", True, id="numeric-palindrome"),
        pytest.param("1231", False, id="numeric-not-palindrome"),
        pytest.param("ab_a", True, id="ignores-symbol-between-letters"),
        pytest.param("Able was I ere I saw Elba!", True, id="classic-sentence"),
    ],
)
def test_is_palindrome_ignores_case_and_non_alphanumeric_characters(
    is_palindrome: Callable[[str], bool],
    s: str,
    expected: bool,
) -> None:
    assert is_palindrome(s) is expected


def test_is_palindrome_handles_long_input(
    is_palindrome: Callable[[str], bool],
) -> None:
    s = ("A" * 5_000) + (":, " * 2_000) + "11" + ("a" * 5_000)

    assert is_palindrome(s) is True
