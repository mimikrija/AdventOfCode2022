
from santas_little_helpers.helpers import *

data = get_input('inputs/14.txt')
#data = get_input('inputs/14e.txt')
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
    return [location + delta for delta in (0+1j, -1+1j, 1+1j)]


def one_sand(rocks, sand, bottom_line, start=500+0j):
    current = start
    while True:
        candidates = [pos for pos in possible_directions(current) if pos not in sand and pos not in rocks]
        if len(candidates) == 0:
            return current # the particle stopped
        
        else:
             current = candidates[0]
        if current.imag > bottom_line.imag:
            return


rocks = generate_cave(data)

bottom_line = max(rocks, key=lambda x:x.imag) + 0+2j
print(bottom_line)
for x in range(3*int(-bottom_line.imag), 2*int(bottom_line.imag+1), 1):
    rocks.add(bottom_line+complex(x, 0))


sand = set()

#sand.add(one_sand(rocks, sand, bottom_line+2))
#party_1 = 0
while True:
    sand_particle = one_sand(rocks, sand, bottom_line)
    if sand_particle:
        sand.add(sand_particle)
        if sand_particle == 500+0j:
            break
    else:
        break

party_1 = len(sand)
print(party_1)

# 14276 too low