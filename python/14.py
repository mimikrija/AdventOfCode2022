# Day 14: Regolith Reservoir

from santas_little_helpers.helpers import *


def generate_cave(data):
    rocks = set()
    for line in data:
        point_pairs = [complex(*tuple(map(int, pair.split(',')))) for pair in line.split(' -> ')]
        for first, second in zip(point_pairs, point_pairs[1:]):
            delta = complex(sign((diff := second - first).real), sign(diff.imag))
            current = first
            while current != second + delta:
                rocks.add(current)
                current += delta
    return rocks


def possible_directions(location):
    for delta in (0+1j, -1+1j, 1+1j):
        yield location + delta


def one_sand(rocks, sand, bottom_line, start=500+0j, is_part_2=False):
    current = start
    while True:
        candidate = next((pos for pos in possible_directions(current) if pos not in sand and pos not in rocks), None)
        if not candidate:
            return current # the particle stopped
        current = candidate
        if is_part_2 and current.imag == bottom_line - 1:
            return current # the particle stoppped at the bottom line

        if current.imag > bottom_line:
            return # abbys reached - pt1 check


def solve(data, is_part_2=False):
    rocks = generate_cave(data)
    start = 500+0j
    bottom_line = max(rocks, key=lambda x:x.imag).imag + 2*is_part_2
    sand = set()
    while True:
        if (sand_particle := one_sand(rocks, sand, bottom_line, start, is_part_2)):
            sand.add(sand_particle)
        else:
            return len(sand)
        if is_part_2 and sand_particle == start:
            return len(sand)



data = get_input('inputs/14.txt')

party_1, party_2 = (solve(data, is_part_2) for is_part_2 in (False, True))

print_solutions(party_1, party_2)



def test_one():
    assert party_1 == 825

def test_two():
    assert party_2 == 26729
