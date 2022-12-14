
from santas_little_helpers.helpers import *

#data = get_input('inputs/14.txt')
data = get_input('inputs/14e.txt')


def generate_cave(data):
    rocks = set()
    for line in data:
        point_pairs = [tuple(map(int, pair.split(','))) for pair in line.split(' -> ')]
        for first, second in zip(point_pairs, point_pairs[1:]):
            # if not (first[0] == second[0] or first[1] == second[1]):
            #     print(first, second, 'it is a diagonal')
            horiz_delta = second[0] - first[0]
            vert_delta = second[1] - first[1]
            rocks |= {complex(first[0] + x, first[1]) for x in range(horiz_delta)}
            rocks |= {complex(first[0], first[1]+y) for y in range(vert_delta)}
            rocks.add(complex(*second))
    return rocks


def possible_directions(location):
    return [location + delta for delta in (0+1j, -1+1j, 1+1j)]


def one_sand(rocks, sand, bottom_line, start=500+0j):
    current = start
    while True:
        print(current)
        candidates = [pos for pos in possible_directions(current) if pos not in sand and pos not in rocks]
        if len(candidates) == 0:
            print('cur', current)
            return current # the particle stopped
        
        else:
             current = candidates[0]
        if current.imag > bottom_line.imag:
            return



bottom_line = max(generate_cave(data), key=lambda x:x.imag)

rocks = generate_cave(data)
sand = set()

sand.add(one_sand(rocks, sand, bottom_line))
print(sand)
