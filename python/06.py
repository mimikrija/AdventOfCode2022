# Day 6: Tuning Trouble

from santas_little_helpers.helpers import *

def find_marker(in_string, n):
    for pos in range(len(in_string)):
        if len(set(in_string[pos:pos+n])) == n:
            return pos+n



data = get_input('inputs/06.txt')[0]

party_1, party_2 = (find_marker(data, n) for n in (4, 14))

print_solutions(party_1, party_2)



def test_one():
    assert party_1 == 1093

def test_two():
    assert party_2 == 3534

