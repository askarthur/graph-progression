"""Progression namespace."""

from importlib_metadata import PackageNotFoundError, version

from .generators import random_walk
from .progressors import DFSProgressor
from .selectors import first, last, randomness

__author__ = "Marco Gancitano"
__email__ = "marco.gancitano@askarthur.art"

# Used to automatically set version number from github actions
# as well as not break when being tested locally
try:
    __version__ = version(__package__)  # type: ignore
except PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0"

__all__ = [
    "DFSProgressor",
    "first",
    "last",
    "randomness",
    "random_walk",
]
