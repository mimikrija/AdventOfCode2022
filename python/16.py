from santas_little_helpers.helpers import *
from re import findall
from collections import defaultdict
from itertools import permutations

data = get_input('inputs/16.txt')
data = get_input('inputs/16e.txt')

flows = dict()
connectivity=dict()

for line in data:
    valves = findall(r'[A-Z]{2}', line)
    first = valves[0]
    rest = valves[1:]
    flow = int(findall(r'\d+', line)[0])
    connectivity[first] = valves
    flows[first] = flow

came_from = defaultdict(list)
for valve, valves in connectivity.items():
    for v in valves:
        if v != valve: # why do i need this
            came_from[v].append(valve)

def max_pressure(flows, connectivity, m):
    minutes = 0
    max_pressure = 0
    while True:
        for valve in permutations(connectivity.keys()):
            

