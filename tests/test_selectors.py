"""Test selectors."""

from graph_progression.selectors import first, last, randomness


def test_first():
    """Test first."""
    assert first([1, 2, 3]) == 1


def test_last():
    """Test last."""
    assert last([1, 2, 3]) == 3


def test_randomness():
    """Test randomness."""
    assert 1 <= randomness([1, 2, 3]) <= 3
