"""A simple calculator module with a command-line interface."""
from __future__ import annotations

import argparse
import operator
import sys
from typing import Callable, Dict


Operation = Callable[[float, float], float]


_OPERATIONS: Dict[str, Operation] = {
    "add": operator.add,
    "subtract": operator.sub,
    "multiply": operator.mul,
    "divide": operator.truediv,
}


def calculate(operation: str, lhs: float, rhs: float) -> float:
    """Return the result of applying *operation* to *lhs* and *rhs*.

    Parameters
    ----------
    operation:
        The name of the operation to perform. Supported operations are ``add``,
        ``subtract``, ``multiply``, and ``divide``.
    lhs:
        The first operand.
    rhs:
        The second operand.

    Raises
    ------
    ValueError
        If *operation* is not one of the supported operations.
    ZeroDivisionError
        If *operation* is ``"divide"`` and *rhs* is zero.
    """

    try:
        operator_func = _OPERATIONS[operation]
    except KeyError as exc:  # pragma: no cover - defensive programming
        raise ValueError(f"Unsupported operation: {operation!r}") from exc

    return operator_func(lhs, rhs)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments for the calculator CLI."""

    parser = argparse.ArgumentParser(description="Perform simple arithmetic operations.")
    parser.add_argument("operation", choices=sorted(_OPERATIONS))
    parser.add_argument("lhs", type=float, help="The first operand.")
    parser.add_argument("rhs", type=float, help="The second operand.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """Entry point for the calculator command-line interface."""

    args = parse_args(argv)
    try:
        result = calculate(args.operation, args.lhs, args.rhs)
    except ZeroDivisionError:
        print("Error: division by zero is undefined.", file=sys.stderr)
        return 1
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
