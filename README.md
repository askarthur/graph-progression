# Progression

[![PyPI version](https://badge.fury.io/py/progression.svg)](https://badge.fury.io/py/progression)
![versions](https://img.shields.io/pypi/pyversions/progression.svg)
[![GitHub license](https://img.shields.io/github/license/mgancita/progression.svg)](https://github.com/mgancita/progression/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
e
ADD MIT LICENSE badge

Create a progression of recommendations from a user-supplied recommender. For more info, see our [official docs](https://mgancita.github.io/progression)

## General

This package was made for a specific use-case but should work with any *content-based* recommendation engine and possibly user-based recommenders.

The initial use case was to create a visual progression of artwork recommendations. This was done to create interesting collections of fine artworks powered by our computer vision recommendation engine.

To see an example, see our [samples](). INSERT SAMPLES

## Quickstart

### Install

`pip install progresssion`

### Implement
Progession has a full sample set to show the functionality of the package w/o the need of a recommender.

```python
from progression import DFSProgressor, random_walk

progressor = DFSProgressor()
progressor.create_progression(0, random_walk, progression_length=3)  
# [0, 8114, 9353]

progressor.graph
# {
# 0: [8114, 5298, 2050, 4837, 1376, 2924, 8689, 8000, 2171, 3246], 
# 8114: [9353, 8647, 8768, 8391, 8555, 8879, 9102, 9481, 9282, 8142]
# }
```

As you can see, progession generates "recommendations" at each step, uses them to populate a graph (for memoization), and then continues on. Not shown here, but it also has the intelligence to backtrack using the graph if it ends a recommendation (node) with no recommedations (edges).

## Features

- Recommendation progression via sequential depth-first search
- Memoization
- Flexible API that can take as inputs:
  - Starter graph
  - Recommendation algorithm
  - Post recommendation filters
  - Selection algorithm
  - Progession length

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [`mgancita/cookiecutter-pypackage`](https://mgancita.github.io/cookiecutter-pypackage/) project template.
