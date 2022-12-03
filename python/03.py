# Day 3: Rucksack Reorganization

from santas_little_helpers.helpers import *

data = get_input('inputs/03.txt')

item_priority = lambda x: ord(x) - 96 if x.islower() else ord(x) - 38


party_1 = sum((sum (item_priority(c) for c in set(line[:len(line)//2]) & set(line[len(line)//2:]))
                for line in data))

party_2 = sum(sum(item_priority(c) for c in set(first) & set(second) & set(third))
                for first, second, third in zip(data[::3], data[1::3], data[2::3]))

print_solutions(party_1, party_2)



def test_one():
    assert party_1 == 8243

def test_two():
    assert party_2 == 2631
