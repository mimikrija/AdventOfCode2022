# Day 1: Calorie Counting


from santas_little_helpers.helpers import *

data_sets = get_input('inputs/01.txt', False,'\n\n')
calories = sorted((sum(int(calorie) for calorie in data_set.split('\n'))
                                    for data_set in data_sets), reverse=True)[:3]

party_1 = calories[0]
party_2 = sum(calories)

print_solutions(party_1, party_2)

def test_one():
    assert party_1 == 72478

def test_two():
    assert party_2 == 210367
