
from santas_little_helpers.helpers import *

data = get_input('inputs/14.txt')
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
            for x in range(horiz_delta+1):
                rocks.add(complex(first[0] + x, first[1]))


generate_cave(data)

for x in range(!)