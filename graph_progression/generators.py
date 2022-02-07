"""Sample step generators for examples."""

import random
from typing import Any, List


def random_walk(current: Any, min: int = -100, max: int = 100, size: int = 10) -> List[int]:
    """Random list of numbers.

    Args:
        size (int, optional): Number of random numbers. Defaults to 10.

    Returns:
        list: List of random numbers.

    """
    deviations = random.choices(list(range(min, max + 1)), k=size)
    return [current + deviation for deviation in deviations]
