"""Tests for the :mod:`calculator` module."""
from __future__ import annotations

import pytest

from pathlib import Path
import sys

# Ensure repository root is importable when tests are executed from other directories
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from calculator import calculate, main


@pytest.mark.parametrize(
    ("operation", "lhs", "rhs", "expected"),
    [
        ("add", 1, 2, 3),
        ("subtract", 5, 3, 2),
        ("multiply", 4, 2.5, 10),
        ("divide", 9, 3, 3),
    ],
)
def test_calculate_supported_operations(operation: str, lhs: float, rhs: float, expected: float) -> None:
    assert calculate(operation, lhs, rhs) == pytest.approx(expected)


def test_calculate_unsupported_operation() -> None:
    with pytest.raises(ValueError):
        calculate("power", 2, 3)


@pytest.mark.parametrize(
    ("args", "expected", "exit_code"),
    [
        (["add", "1", "2"], "3.0\n", 0),
        (["subtract", "5", "3"], "2.0\n", 0),
        (["multiply", "2", "4"], "8.0\n", 0),
        (["divide", "8", "2"], "4.0\n", 0),
    ],
)
def test_main_success(args: list[str], expected: str, exit_code: int, capsys: pytest.CaptureFixture[str]) -> None:
    assert main(args) == exit_code
    captured = capsys.readouterr()
    assert captured.out == expected
    assert captured.err == ""


def test_main_division_by_zero(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["divide", "1", "0"]) == 1
    captured = capsys.readouterr()
    assert captured.err.strip() == "Error: division by zero is undefined."


@pytest.mark.parametrize(
    "non_number",
    ["a", "hello", "--"],
)
def test_main_invalid_number_arguments(non_number: str) -> None:
    with pytest.raises(SystemExit):
        main(["add", non_number, "5"])
