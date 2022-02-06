"""Selection algorithms for progressor steps."""

from functools import partial
import random
from typing import Any, List


def select(options: List[Any], index: int) -> Any:
    """Select option at a certain index.

    Args:
        options (list): List of options to select.

    Return:
        Any: "index" element of the options list.

    """
    return options[index]


first = partial(select, index=0)
last = partial(select, index=-1)

randomness = random.choice
