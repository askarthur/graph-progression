"""Test module for progressors."""

from typing import Any, List

import pytest

from graph_progression.generators import random_walk
from graph_progression.progressors import DFSProgressor
from graph_progression.selectors import last


def mock_no_recommendations_to_start(*args, **kwargs) -> List[Any]:
    """Return an empty list."""
    return []


def mock_filter(options: List[Any]) -> List[Any]:
    """Mock filter."""
    return options[:-1]


def mock_step(current_step: int) -> List[int]:
    """Mock step generator."""
    if current_step != 5:
        return list(range(current_step + 1, current_step + 10))

    return []


class TestDFSProgressor:
    """Test DFSProgressor."""

    def setup(self):
        """Set up tests."""
        self.progressor = DFSProgressor()

    def test_create_progession(self):
        """Test create_progression."""
        progression = self.progressor.create_progression(0, random_walk)
        assert len(progression) == 10
        assert len(list(set(progression))) == 10

    def test_create_progression_w_backtrack(self):
        """Test create_progression w/ backtracking."""
        progession = self.progressor.create_progression(0, mock_step)
        assert progession == [0, 1, 2, 3, 4, 6, 7, 8, 9, 10]
        assert list(self.progressor.graph.keys()) == list(range(10))

    @pytest.mark.parametrize(
        "starter, step_generator, progression_length, post_generation_filters, step_selection, "
        "expected_error",
        [
            (0, random_walk, 10, None, "first", None),
            (0, random_walk, 10, None, last, None),
            (0, random_walk, 10, [mock_filter], last, None),
            (0, random_walk, 10, None, "invalid_step", ValueError),
            (0, random_walk, -5, None, "first", ValueError),
        ],
    )
    def test_create_progession_inputs(
        self,
        starter,
        step_generator,
        progression_length,
        post_generation_filters,
        step_selection,
        expected_error,
    ):
        """Test create_progression inputs tests."""
        if expected_error:
            with pytest.raises(expected_error):
                self.progressor.create_progression(
                    starter,
                    step_generator,
                    progression_length,
                    post_generation_filters,
                    step_selection,
                )
        else:
            assert self.progressor.create_progression(
                starter, step_generator, progression_length, post_generation_filters, step_selection
            )

    def test_create_progession_no_solution(self):
        """Test create_progression with no solution."""
        assert self.progressor.create_progression(0, mock_no_recommendations_to_start) == []
