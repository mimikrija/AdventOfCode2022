# Day 18: Boiling Boulders

from collections import deque

from santas_little_helpers.helpers import *

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

# reduce start of search only to void cells adjacent to lava cells
adjacent_void = {cube for cube in void if any(neighbor in lava for neighbor in cube_neigbors(cube))}


def find_pocket(start, void, lava):
    frontier = deque([start])
    potential_pocket = set({start})
    reached = set({start})
    while frontier:
        cell = frontier.pop()
        empty_candidates = {cube for cube in cube_neigbors(cell) if cube in void and cube not in lava}
        for candidate in empty_candidates:
            if candidate not in reached:
                frontier.append(candidate)
                reached.add(candidate)
        potential_pocket |= empty_candidates

        # check if pocket contains cells connected to outher world if yes, it is not a pocket
        if any(cell[n] == MIN for cell in empty_candidates for n, MIN in zip(range(3), (MIN_X, MIN_Y, MIN_Z))):
            return potential_pocket, False
        if any(cell[n] == MAX for cell in empty_candidates for n, MAX in zip(range(3), (MAX_X, MAX_Y, MAX_Z))):
            return potential_pocket, False

    return potential_pocket, True


def find_all_pockets(adjacent_void, lava):
    candidates_to_check = set(adjacent_void)
    pockets = []
    while candidates_to_check:
        potential_pocket, is_pocket = find_pocket(candidates_to_check.pop(), void, lava)
        if is_pocket:
            pockets.append(potential_pocket)
        if potential_pocket is not None:
            candidates_to_check -= potential_pocket
    return pockets


party_1 = sum(count_free_sides(cube, lava) for cube in lava)
inner_area = sum(count_free_sides(cube, pocket) for pocket in find_all_pockets(adjacent_void, lava) for cube in pocket)
party_2 = party_1 - inner_area


print_solutions(party_1, party_2)





def test_one():
    assert party_1 == 4310

def test_two():
    assert party_2 == 2466
