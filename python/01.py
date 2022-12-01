
from santas_little_helpers.helpers import *

data_sets = get_input('inputs/01.txt', False,'\n\n')
calories = dict()
for elf, set in enumerate(data_sets, 1):
    calories[elf] = sum(int(n) for n in set.split('\n'))

t = max(calories)
print(calories[t])

print(max(calories.values()))

three = sorted(calories.values(), reverse=True)
print(sum(three[:3]))
