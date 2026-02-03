import os
import sys

# Ensure the project's src folder is on sys.path so package imports work in tests
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from clumps.main import find_clumps


def test_basic_clumps():
    text = "ACGTACGTACGT"
    k = 3
    t = 2
    window_length = 8
    result = find_clumps(text, k, t, window_length)
    # sorted deterministic output
    assert result == ["ACG", "CGT", "GTA", "TAC"]


def test_simple_repeats():
    assert find_clumps("AAAAA", 1, 2, 2) == ["A"]


def test_k_greater_than_text():
    # should return empty list when k > len(text)
    assert find_clumps("ACG", 4, 1, 10) == []


def test_k_greater_than_window_length():
    # should raise an error when k > window_length
    import pytest

    with pytest.raises(ValueError):
        find_clumps("ACG", 10, 1, 5)


def test_global_equals_bruteforce_small():
    # for small sequences, the global method should match the sliding-window brute-force
    seq = ("ACGT" * 50)[:500]
    k = 4
    t = 2
    w = 10
    a = find_clumps(seq, k, t, w)
    from clumps.main import find_clumps_global

    b = find_clumps_global(seq, k, t, w)
    assert sorted(a) == sorted(b)


def test_global_detects_synthetic():
    # synthetic sequence with a k-mer repeated 3 times within the window
    head = "N" * 100
    kmer = "KMER"
    seq = head + kmer + ("N" * 100) + kmer + ("N" * 100) + kmer + head
    from clumps.main import find_clumps_global

    res = find_clumps_global(seq, len(kmer), 3, 350)
    # Multiple overlapping k-mers around the repeated motif may also appear; ensure our k-mer is detected
    assert kmer in res
    assert len(res) >= 1


import pytest


def test_invalid_params():
    with pytest.raises(ValueError):
        find_clumps("ACG", 0, 1, 5)
    with pytest.raises(ValueError):
        find_clumps("", 1, 1, 5)
    with pytest.raises(ValueError):
        find_clumps("ACGT", 3, 1, 2)  # k > window_length
