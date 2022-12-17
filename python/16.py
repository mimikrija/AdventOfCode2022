from santas_little_helpers.helpers import *
from re import findall
from collections import deque
from itertools import permutations, combinations
from functools import lru_cache
from queue import PriorityQueue

data = get_input('inputs/16.txt')
data = get_input('inputs/16e.txt')

FLOWS = dict()
connectivity=dict()

for line in data:
    valves = findall(r'[A-Z]{2}', line)
    first = valves[0]
    rest = valves[1:]
    flow = int(findall(r'\d+', line)[0])
    connectivity[first] = (flow, rest)

valid_valves = [valve for valve, (flow, _) in connectivity.items() if flow > 0]

start = ('AA', 30, tuple(), 0)

def update_pressure(open_seq):
    return sum(connectivity[valve][0] for valve in open_seq)

@lru_cache
def solve(state):
    last_visited, remaining_time, open_so_far, released_pressure = state
    if remaining_time == 0:
        return released_pressure

    flow, neighbors = connectivity[last_visited]
    for neighbor in neighbors:
        # just visit next one and update pressure
        solve((neighbor, remaining_time-1, open_so_far, released_pressure + update_pressure(open_so_far)))
        # open the valve
        if neighbor not in open_so_far and flow != 0:
            new_open_so_far = tuple(list(open_so_far)+[neighbor])
            solve((neighbor, remaining_time-2, new_open_so_far, released_pressure + 2*update_pressure(open_so_far)))

