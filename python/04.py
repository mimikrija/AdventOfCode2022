# Day 4: Camp Cleanup

from re import findall

from santas_little_helpers.helpers import *

data = [tuple(map(int, findall(r'\d+', line))) for line in get_input('inputs/04.txt')]


overlap = lambda l1, r1, l2, r2: not (r1 < l2 or l1 > r2)
full_overlap = lambda l1, r1, l2, r2: l2 <= l1 <= r1 <= r2 or l1 <= l2 <= r2 <= r1


party_1, party_2 = (sum(func(*sections) for sections in data) for func in (full_overlap, overlap))


print_solutions(party_1, party_2)


def test_one():
    assert party_1 == 515

def test_two():
    assert party_2 == 883
