from santas_little_helpers.helpers import *

data = get_input('inputs/03.txt')

def item_priority(item):
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38

party_1 = 0
for line in data:
    rl = len(line) // 2
    left = line[:rl]
    right = line[rl:]
    #print(set(left) & set(right))
    for c in set(left) & set(right):
        #print(item_priority(c))
        party_1 += item_priority(c)

print(party_1)

party_2 = 0
for n, first in enumerate(data[::3]):
    third = data[n*3+2]
    second = data[n*3+1]
    #print('first in tge group', first, second, third)
    #print(set(first) & set(second) & set(third))
    party_2 += sum(item_priority(c) for c in set(first) & set(second) & set(third))
#print(item_priority('A'))
# 3875 incorrect
print(party_2)

def test_one():
    assert party_1 == 8243

def test_two():
    assert party_2 == 2631
