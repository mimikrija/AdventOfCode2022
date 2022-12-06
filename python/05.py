# Day 5: Supply Stacks

from collections import defaultdict
from copy import deepcopy
from re import findall

from santas_little_helpers.helpers import *

data = get_input('inputs/05.txt')
operations = [tuple(map(int, findall(r'\d+', line))) for line in data[10:]]

# parse stacks
stacks = defaultdict(list)
for line in data[7::-1]:
    for num, crate in enumerate(line[1::4], 1):
        if crate != ' ':
            stacks[num].append(crate)


def solve(in_stacks, operations, part2=False):
    stacks = deepcopy(in_stacks)
    for qt, origin, destination in operations:
        if not part2:
            stacks[destination] += [stacks[origin].pop() for _ in range(qt)]
        else:
            stacks[destination] += reversed([stacks[origin].pop() for _ in range(qt)])
    return ''.join(stack.pop() for stack in stacks.values())


party_1, party_2 = (solve(stacks, operations, part2) for part2 in (False, True))

print_solutions(party_1, party_2)

def test_one():
    assert party_1 == 'PTWLTDSJV'

def test_two():
    assert party_2 == 'WZMFVGGZP'
