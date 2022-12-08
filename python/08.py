# Day 8: Treetop Tree House

from math import prod

from santas_little_helpers.helpers import *

data = get_input('inputs/08.txt')
TREE_HEIGHTS = {(x, y): int(num) for y, row in enumerate(data) for x, num in enumerate(row)}
MAX_X = len(data[0])
MAX_Y = len(data)


def directions(tree):
    """returns coordinates to check in a given direction from reference `tree` location """
    xt, yt = tree
    left = [(x, yt) for x in reversed(range(0, xt))]
    right = [(x, yt) for x in range(xt+1, MAX_X)]
    up = [(xt, y) for y in reversed(range(0, yt))]
    down = [(xt, y) for y in range(yt+1, MAX_Y)]
    return (left, right, up, down)


def is_visible(location, grid):
    height = grid[location]
    return any((all(grid[pair] < height for pair in side)) for side in directions(location))

def scenic_score(location, grid):
    height = grid[location]
    return prod(next((n for n, pair in enumerate(side, 1) if grid[pair] >= height), len(side)) for side in directions(location))


def solve(grid, function1, function2):
    return function1(function2(tree, grid) for tree in grid)


party_1 = solve(TREE_HEIGHTS, sum, is_visible)
party_2 = solve(TREE_HEIGHTS, max, scenic_score)


print_solutions(party_1, party_2)



def test_one():
    assert party_1 == 1801

def test_two():
    assert party_2 == 209880
