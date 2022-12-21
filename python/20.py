# Day 20: Grove Positioning System

from collections import deque

from santas_little_helpers.helpers import *


data = get_input('inputs/20.txt', True, '\n')


def mixit(in_list, orig):
    output = deque(in_list)
    for pair in orig:
        pair_pos = output.index(pair)
        output.rotate(-pair_pos)
        current = output.popleft()
        num, _ = current
        output.rotate(-num)
        output.append(current)
    return output

def grove_coordinates(linked, zero):

    ref = linked.index(zero)
    positions = [(ref+1000*n)%(len(linked)) for n in range(1, 4)]
    return sum(linked[pos][0] for pos in positions)


def solve(data, part_2=False):
    decryption_key = 1 if not part_2 else 811589153
    original = [(num*decryption_key, pos) for pos, num in enumerate(data)]
    rounds = 1 if not part_2 else 10
    coordinates = original
    for _ in range(rounds):
        coordinates = mixit(coordinates, original)
    zero_pos = (0, data.index(0))
    return grove_coordinates(coordinates, zero_pos)


party_1, party_2 = (solve(data, part_2) for part_2 in (False, True))


print_solutions(party_1, party_2)

def test_one():
    assert party_1 == 14888

def test_two():
    assert party_2 == 3760092545849
