# Day 18: Boiling Boulders

from santas_little_helpers.helpers import *

DELTAS = {(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)}


lava = [tuple(map(int, line.split(','))) for line in get_input('inputs/18.txt')]


SIZE = 6
SIZE = 21


def cube_neigbors(in_cube):
    return {add_coordinates(in_cube, delta) for delta in DELTAS}


def count_free_sides(cube, lava):
    return sum((neighbor not in lava) for neighbor in cube_neigbors(cube))






party_1 = sum(count_free_sides(cube, lava) for cube in lava)
print_solutions(party_1)




def test_one():
    assert party_1 == 4310
