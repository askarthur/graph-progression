"""Test generators."""

from progression.generators import random_walk


def test_random_walk():
    """Test random_walk."""
    assert len(random_walk(0, size=10)) == 10
    assert random_walk(0, size=10) != random_walk(0, size=10)
    assert random_walk(0, min=1, max=1) == [1] * 10
