import os
import sys
import pytest

# Ensure 'src' is on sys.path so tests can import package modules
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
sys.path.insert(0, SRC)

from skew.main import skew_array


def test_skew_array_sanity():
    genome = "GATACACTTCCCGAGTAGGTACTG"
    expected = [
        0,
        1,
        1,
        1,
        1,
        0,
        0,
        -1,
        -1,
        -1,
        -2,
        -3,
        -4,
        -3,
        -3,
        -2,
        -2,
        -2,
        -1,
        0,
        0,
        0,
        -1,
        -1,
        0,
    ]
    assert skew_array(genome) == expected


def test_skew_array_empty():
    with pytest.raises(ValueError):
        skew_array("")


def test_skew_array_invalid_nucleotide():
    with pytest.raises(ValueError):
        skew_array("GATBX")


def test_draw_skew_array_returns_fig_and_axes(monkeypatch):
    import matplotlib

    matplotlib.use("Agg")
    from skew.main import draw_skew_array

    skew = [0, 1, 1, 0, -1]
    fig, ax = draw_skew_array(skew, show=False)
    # basic checks
    assert fig is not None
    assert ax is not None


def test_draw_skew_array_saves_file(tmp_path):
    import matplotlib

    matplotlib.use("Agg")
    from skew.main import draw_skew_array

    skew = [0, 1, 1, 0, -1]
    out = tmp_path / "skew_plot.png"
    fig, ax = draw_skew_array(skew, show=False, filename=str(out))
    assert out.exists()
    assert out.stat().st_size > 0
