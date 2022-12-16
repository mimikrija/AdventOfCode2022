from santas_little_helpers.helpers import *
from re import findall
from collections import defaultdict
from itertools import permutations, combinations

data = get_input('inputs/16.txt')
data = get_input('inputs/16e.txt')

flows = dict()
connectivity=dict()

for line in data:
    valves = findall(r'[A-Z]{2}', line)
    first = valves[0]
    rest = valves[1:]
    flow = int(findall(r'\d+', line)[0])
    connectivity[first] = rest
    flows[first] = flow



distances = {p: 0 for p in permutations(connectivity.keys(), 2)}
for p in distances.keys():
    first, second = p
    steps = 0
    candidates = connectivity[first]
    while True:
        steps += 1
        if second in candidates:
            distances[p] = steps
            break
        else:
            candidates = [c for candidate in candidates for c in connectivity[candidate]]



