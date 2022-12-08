# Day 8: Treetop Tree House

from santas_little_helpers.helpers import *

data = get_input('inputs/08.txt')
TREE_HEIGHTS = {(x, y): int(num) for y, row in enumerate(data) for x, num in enumerate(row)}
MAX_X = len(data[0])
MAX_Y = len(data)


def is_visible(location, grid):
    xt, yt = location
    height = grid[location]

    left = ((x, yt) for x in range(0, xt))
    right = ((x, yt) for x in range(xt+1, MAX_X))
    up = ((xt, y) for y in range(0, yt))
    down = ((xt, y) for y in range(yt+1, MAX_Y))

    return any((all(grid[pair] < height for pair in side)) for side in (left, right, up, down))

def scenic_score(location, grid):
    xt, yt = location
    height = grid[location]

    return next((n for n, x in enumerate(range(xt-1, -1, -1), 1) if grid[(x, yt)] >= height), xt) * \
        next((n for n, x in enumerate(range(xt+1, MAX_X),1) if grid[(x, yt)] >= height), MAX_X-1-xt) * \
        next((n for n, y in enumerate(range(yt-1, -1, -1),1) if grid[(xt, y)] >= height), yt) * \
        next((n for n, y in enumerate(range(yt+1, MAX_Y),1) if grid[(xt, y)] >= height), MAX_Y-1-yt)



party_1 = sum(is_visible(tree, TREE_HEIGHTS) for tree in TREE_HEIGHTS.keys())
party_2 = max(scenic_score(tree, TREE_HEIGHTS) for tree in TREE_HEIGHTS.keys())

print_solutions(party_1, party_2)



def test_one():
    assert party_1 == 1801

def test_two():
    assert party_2 == 209880
