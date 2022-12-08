# Day 8: Treetop Tree House

from math import prod

from santas_little_helpers.helpers import *

data = get_input('inputs/08.txt')
TREE_HEIGHTS = {(x, y): int(num) for y, row in enumerate(data) for x, num in enumerate(row)}
MAX_X = len(data[0])
MAX_Y = len(data)


def directions(tree):
    """returns coordinates to check in a given direction + default solution if all trees are lower than the reference tree for pt2 """
    xt, yt = tree
    left = (((x, yt) for x in reversed(range(0, xt))), xt)
    right = (((x, yt) for x in range(xt+1, MAX_X)), MAX_X-1-xt)
    up = (((xt, y) for y in reversed(range(0, yt))), yt)
    down = (((xt, y) for y in range(yt+1, MAX_Y)), MAX_Y-1-yt)
    return (left, right, up, down)


def is_visible(location, grid):
    height = grid[location]
    return any((all(grid[pair] < height for pair in side)) for side, _ in directions(location))

def scenic_score(location, grid):
    height = grid[location]
    return prod(next((n for n, pair in enumerate(left, 1) if grid[pair] >= height), default) for left, default in directions(location))




party_1, party_2 = (what(which(tree, TREE_HEIGHTS) for tree in TREE_HEIGHTS.keys()) for what, which in ((sum, is_visible), (max, scenic_score)))


print_solutions(party_1, party_2)



def test_one():
    assert party_1 == 1801

def test_two():
    assert party_2 == 209880
