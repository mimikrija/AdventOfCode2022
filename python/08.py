
from santas_little_helpers.helpers import *

data = get_input('inputs/08.txt')
#data = get_input('inputs/08e.txt')

TREE_HEIGHTS = {(y, x): int(num) for x, row in enumerate(data) for y, num in enumerate(row)}
MAX_X = len(data[0])
MAX_Y = len(data) 

def is_visible(location, grid):
    xt, yt = location
    height = grid[location]
    if xt == 0 or xt == MAX_X - 1 or yt == 0 or yt == MAX_Y - 1:
        return True
    if all(grid[(x, yt)] < height for x in range(0, xt)):
        return True
    if all(grid[(x, yt)] < height for x in range(xt+1, MAX_X)):
        return True
    if all(grid[(xt, y)] < height for y in range(0, yt)):
        return True
    if all(grid[(xt, y)] < height for y in range(yt+1, MAX_X)):
        return True
    return False





def scenic_score(location, grid):
    xt, yt = location
    if xt == 0 or xt == MAX_X - 1 or yt == 0 or yt == MAX_Y - 1:
        return 0
    height = grid[location]
    sc1 = None
    for n, x in enumerate(range(xt-1, -1, -1),1):
        if grid[(x, yt)] >= height:
            sc1 = n
            break
    if sc1 is None:
        sc1 = xt
    
    sc2 = None
    for n, x in enumerate(range(xt+1, MAX_X),1):
        if grid[(x, yt)] >= height:
            sc2 = n
            break
    if sc2 is None:
        sc2 = MAX_X-1-xt

    sc3 = None
    for n, y in enumerate(range(yt-1, -1, -1),1):
        if grid[(xt, y)] >= height:
            sc3 = n
            break
    if sc3 is None:
        sc3 = yt
    
    sc4 = None
    for n, y in enumerate(range(yt+1, MAX_Y),1):
        if grid[(xt, y)] >= height:
            sc4 = n
            break
    if sc4 is None:
        sc4 = MAX_Y-1-yt

    return sc1 * sc2 * sc3 * sc4



party_1 = 0
visibles = set()
for loc, height in TREE_HEIGHTS.items():

    if is_visible(loc, TREE_HEIGHTS):
        visibles.add(loc)
party_1 = len(visibles)



party_2 = max(scenic_score(tree, TREE_HEIGHTS) for tree in TREE_HEIGHTS.keys())

print_solutions(party_1, party_2)