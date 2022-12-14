# Day 5: Supply Stacks

from collections import defaultdict
from copy import deepcopy
from re import findall

from santas_little_helpers.helpers import *

data = get_input('inputs/05.txt', False, '\n\n')
operations = [tuple(map(int, findall(r'\d+', line))) for line in data[1].splitlines()]

# parse stacks
stacks = defaultdict(list)
for line in data[0].splitlines()[-1::-1]:
    for num, crate in enumerate(line[1::4], 1):
        if crate != ' ':
            stacks[num].append(crate)


def solve(in_stacks, operations, part2=False):
    stacks = deepcopy(in_stacks)
    func = reversed if part2 else list
    for qt, origin, destination in operations:
        stacks[destination] += func([stacks[origin].pop() for _ in range(qt)])
    return ''.join(stack.pop() for stack in stacks.values())


party_1, party_2 = (solve(stacks, operations, part2) for part2 in (False, True))

print_solutions(party_1, party_2)

def test_one():
    assert party_1 == 'PTWLTDSJV'

def test_two():
    assert party_2 == 'WZMFVGGZP'
