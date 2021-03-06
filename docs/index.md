# Progression

Create a progression of recommendations from a user-supplied recommender

## General

This package was made for a specific use-case but should work with any *content-based* recommendation engine and possibly user-based recommenders.

The initial use case was to create a visual progression of artwork recommendations. This was done to create interesting collections of fine artworks powered by our computer vision recommendation engine.

To see an example, see our [samples](samples/README.md).

## Quickstart

### Install

`pip install graph_progression`

### Implement
Progession has a full sample set to show the functionality of the package w/o the need of a recommender.

```python
from graph_progression import DFSProgressor, random_walk

progressor = DFSProgressor()
progressor.create_progression(0, random_walk, progression_length=3)  
# [0, 8114, 9353]

progressor.graph
# {
# 0: [8114, 5298, 2050, 4837, 1376, 2924, 8689, 8000, 2171, 3246], 
# 8114: [9353, 8647, 8768, 8391, 8555, 8879, 9102, 9481, 9282, 8142]
# }
```

As you can see, graph_progession generates "recommendations" at each step, uses them to populate a graph (for memoization), and then continues on. Not shown here, but it also has the intelligence to backtrack using the graph if it arrives at a recommendation (node) with no recommedations (edges).

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
