from santas_little_helpers.helpers import *
from re import findall
from collections import defaultdict
from itertools import permutations, combinations

data = get_input('inputs/16.txt')
data = get_input('inputs/16e.txt')

FLOWS = dict()
connectivity=dict()

for line in data:
    valves = findall(r'[A-Z]{2}', line)
    first = valves[0]
    rest = valves[1:]
    flow = int(findall(r'\d+', line)[0])
    connectivity[first] = rest
    FLOWS[first] = flow



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




def calculate_flow(sequence):
    flow = 0
    if sequence[0] == 'AA':
        time = 30
    else:
        time = 30 - distances[('AA', sequence[0])]
    for valves in zip(sequence, sequence[1:]):
        time -= 1
        #print('opening valve ', valves[0], 'minute ', 30-time)
        flow += FLOWS[valves[0]]*time
        if time == 0:
            print('here')
            return flow
        time -= distances[valves]
    #print('opening valve ', sequence[-1], 'minute ', 30-time+1)
    flow += FLOWS[sequence[-1]]*(time-1)
    return flow

released_pressure = lambda valve, remaining_time: FLOWS[valve] * remaining_time
    

def dfs(starting_position='AA', opened = list(), time=30):
    possibilities = (valves for valves in distances.keys()
                        if FLOWS[valve] != 0 and valve not in opened)
    print(starting_position, opened, time)
    for valve in possibilities:
        print(valve)
        opened.append(valve)
        dfs(valve, opened, time-distances[(starting_position, valve)]-1)


posibilities = []
for p in permutations((valve for valve in connectivity.keys() if FLOWS[valve] != 0)):
    if p[0] != 'AA':
        minutes = distances[('AA', p[0])]
    else:
        minutes = 0
    flow = 0
    for pair in zip(p, p[1:]):
        minutes += distances[pair] + 1 #minutes to reach the next one + 1 minute to open the valve
        if minutes > 30:
            break
    
    if minutes <= 30:
        posibilities.append(p)


print(max(calculate_flow(possibility) for possibility in posibilities))