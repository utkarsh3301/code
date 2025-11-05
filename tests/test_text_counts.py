from pathlib import Path
import sys

# Ensure repository root is importable when tests are executed from other directories
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import text


def test_counts_simple_phrase():
    counts = text.count_alphabets_and_spaces("Hello world")
    assert counts.alphabets == 10
    assert counts.spaces == 1


def test_counts_with_mixed_characters():
    counts = text.count_alphabets_and_spaces("Room 101 is ready!")
    assert counts.alphabets == 11
    assert counts.spaces == 3


def test_counts_unicode_letters_and_spaces():
    counts = text.count_alphabets_and_spaces("naïve façade")
    assert counts.alphabets == 11
    assert counts.spaces == 1
