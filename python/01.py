# Day 1: Calorie Counting


from santas_little_helpers.helpers import *

data_sets = get_input('inputs/01.txt', False,'\n\n')
calories = [sum(int(calorie) for calorie in data_set.split('\n')) for data_set in data_sets]

party_1 = max(calories)
party_2 = sum(sorted(calories, reverse=True)[:3])

print_solutions(party_1, party_2)

