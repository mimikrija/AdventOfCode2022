from santas_little_helpers.helpers import *
from re import findall

data = get_input('inputs/04.txt')

party_1 = 0
party_2 = 0
for sec in data:
    a, b = map(int, findall(r'\d+', sec.split(',')[0]))
    c, d = map(int, findall(r'\d+', sec.split(',')[1]))
    first = set(list(range(a, b+1)))
    second = set(list(range(c, d+1)))
    #print(a, b, first, second)
    if second & first == second or first & second == first:
        party_1 += 1
    if len(second&first) > 0:
        party_2 += 1

print_solutions(party_1, party_2)
