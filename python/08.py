# Day 8: Treetop Tree House

from santas_little_helpers.helpers import *


def is_visible(location, grid):
    xt, yt = location
    height = grid[location]

    return any((all(grid[(x, yt)] < height for x in range(0, xt)), all(grid[(x, yt)] < height for x in range(xt+1, MAX_X)), \
            all(grid[(xt, y)] < height for y in range(0, yt)), all(grid[(xt, y)] < height for y in range(yt+1, MAX_X))))


def scenic_score(location, grid):
    xt, yt = location
    height = grid[location]

    look_left = next((n for n, x in enumerate(range(xt-1, -1, -1), 1) if grid[(x, yt)] >= height), xt)
    look_right = next((n for n, x in enumerate(range(xt+1, MAX_X),1) if grid[(x, yt)] >= height), MAX_X-1-xt)
    look_up = next((n for n, y in enumerate(range(yt-1, -1, -1),1) if grid[(xt, y)] >= height), yt)
    look_down = next((n for n, y in enumerate(range(yt+1, MAX_Y),1) if grid[(xt, y)] >= height), MAX_Y-1-yt)

    return look_left * look_right * look_up * look_down


data = get_input('inputs/08.txt')
TREE_HEIGHTS = {(x, y): int(num) for y, row in enumerate(data) for x, num in enumerate(row)}
MAX_X = len(data[0])
MAX_Y = len(data)

party_1 = sum(is_visible(tree, TREE_HEIGHTS) for tree in TREE_HEIGHTS.keys())
party_2 = max(scenic_score(tree, TREE_HEIGHTS) for tree in TREE_HEIGHTS.keys())

print_solutions(party_1, party_2)



def test_one():
    assert party_1 == 1801

def test_two():
    assert party_2 == 209880
