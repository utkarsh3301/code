"""Utility to count alphabetic characters and spaces in a text string."""
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass


@dataclass
class TextCounts:
    """Store the counts of alphabetic characters and spaces."""

    alphabets: int
    spaces: int


def count_alphabets_and_spaces(text: str) -> TextCounts:
    """Return the counts of alphabetic characters and spaces in *text*.

    Alphabetic characters are detected with :py:meth:`str.isalpha`, which treats
    Unicode letters as alphabetic. Spaces are characters equal to ``" "``.
    """

    alphabets = sum(1 for char in text if char.isalpha())
    spaces = text.count(" ")
    return TextCounts(alphabets=alphabets, spaces=spaces)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Count alphabetic characters and spaces in a piece of text.",
    )
    parser.add_argument(
        "text",
        nargs="?",
        help=(
            "Text to analyse. If omitted, text is read from standard input."
        ),
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """Entry-point used by the command-line interface."""

    args = parse_args(argv)
    if args.text is not None:
        source_text = args.text
    else:
        source_text = sys.stdin.read()

    counts = count_alphabets_and_spaces(source_text)
    print(f"Alphabets: {counts.alphabets}")
    print(f"Spaces: {counts.spaces}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
