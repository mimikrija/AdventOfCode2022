# Day 18: Boiling Boulders

from santas_little_helpers.helpers import *
from math import prod

DELTAS = {(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)}


lava = {tuple(map(int, line.split(','))) for line in get_input('inputs/18.txt')}

MIN_X, MIN_Y, MIN_Z = (min(lava, key=lambda x:x[n])[n] for n in range(3))
MAX_X, MAX_Y, MAX_Z = (max(lava, key=lambda x:x[n])[n] for n in range(3))
SIZE = [MAX-MIN+1 for MAX, MIN in zip((MAX_X, MAX_Y, MAX_Z), (MIN_X, MIN_Y, MIN_Z))]


def cube_neigbors(in_cube):
    return {add_coordinates(in_cube, delta) for delta in DELTAS}


def count_free_sides(cube, lava):
    return sum((neighbor not in lava) for neighbor in cube_neigbors(cube))


void = {cube for x in range(MIN_X, MAX_X+1) for y in range(MIN_Y, MAX_Y+1) for z in range(MIN_Z, MAX_Z+1) if (cube := (x, y, z)) not in lava}







party_1 = sum(count_free_sides(cube, lava) for cube in lava)
print_solutions(party_1)




def test_one():
    assert party_1 == 4310
