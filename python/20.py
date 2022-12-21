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

def get_numbers(linked, zero):
    ref = linked.index(zero)
    positions = [(ref+1000*n)%(len(linked)) for n in range(1, 4)]
    return sum(linked[pos][0] for pos in positions)



original = [(num, pos) for pos, num in enumerate(data)]
p = original
zero_pos = (0, data.index(0))
p = mixit(p, original)
party_1 = get_numbers(p, zero_pos)

original = [(num*811589153, pos) for pos, num in enumerate(data)]
p = original
for round in range(10):
    p = mixit(p, original)
party_2 = get_numbers(p, zero_pos)


print_solutions(party_1, party_2)

def test_one():
    assert party_1 == 14888

def test_two():
    assert party_2 == 3760092545849
