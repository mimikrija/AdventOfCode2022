
from santas_little_helpers.helpers import *

data = get_input('inputs/14.txt')

sign = lambda x: 1 if x >= 0 else -1

def generate_cave(data):
    rocks = set()
    for line in data:
        point_pairs = [tuple(map(int, pair.split(','))) for pair in line.split(' -> ')]
        for first, second in zip(point_pairs, point_pairs[1:]):
            # if not (first[0] == second[0] or first[1] == second[1]):
            #     print(first, second, 'it is a diagonal')
            horiz_delta = second[0] - first[0]
            vert_delta = second[1] - first[1]
            rocks |= {complex(first[0] + sign(horiz_delta)*x, first[1]) for x in range(sign(horiz_delta)*horiz_delta)}
            rocks |= {complex(first[0], first[1]+sign(vert_delta)*y) for y in range(sign(vert_delta)*vert_delta)}
            rocks.add(complex(*second))
    return rocks


def possible_directions(location):
    for delta in (0+1j, -1+1j, 1+1j):
        yield location + delta


def one_sand(rocks, sand, bottom_line, is_part_2=False, start=500+0j):
    current = start
    while True:
        candidate = next((pos for pos in possible_directions(current) if pos not in sand and pos not in rocks), None)
        if not candidate:
            return current # the particle stopped
        current = candidate
        if is_part_2 and current.imag == bottom_line.imag-1:
             return current # bottom reached, add to sand
        if current.imag > bottom_line.imag:
            return # abbys reached - pt1 check


def solve(data, is_part_2=False):
    rocks = generate_cave(data)
    bottom_line = max(rocks, key=lambda x:x.imag)
    if is_part_2:
        bottom_line += 0+2j

    sand = set()
    while True:
        sand_particle = one_sand(rocks, sand, bottom_line, is_part_2)
        if sand_particle:
            sand.add(sand_particle)
        else:
            break
        if is_part_2 and sand_particle == 500+0j:
            break
    
    return len(sand)



party_1 = solve(data)

party_2 = solve(data, True)
print_solutions(party_1, party_2)


def test_one():
    assert party_1 == 825

def test_two():
    assert party_2 == 26729