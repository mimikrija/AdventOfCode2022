
from re import findall
from itertools import combinations, permutations
from collections import deque
from functools import lru_cache

from santas_little_helpers.helpers import *


def get_adjacent_vertices(edges, current):
    return {point for edge in edges for point in edge if current in edge and current != point}

@lru_cache
def find_shortest_path(start, end):
    def find_all_subpaths(start, end, path):
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in ADJACENCY[start]:
            if not node in path:
               paths.extend(find_all_subpaths(node, end, path))
        return paths
    return len(min(find_all_subpaths(start, end, []), key=lambda x: len(x)))-1




data = get_input('inputs/16.txt')

FLOWS = dict()
edges = set()
nodes = list()

for line in data:
    valves = findall(r'[A-Z]{2}', line)
    first = valves[0]
    rest = valves[1:]
    flow = int(findall(r'\d+', line)[0])
    for second in rest:
        edges.add(tuple(sorted([first, second])))
    FLOWS[first] = flow
    nodes.append(first)

nodes = tuple(nodes)
valid_valves = {valve for valve in nodes if FLOWS[valve] != 0}
ADJACENCY = {node: get_adjacent_vertices(edges, node) for node in nodes}
SHORTEST_PATHS = {(first, second): find_shortest_path(first, second)
                                for first, second in permutations(nodes, 2)}




def to_open(open_so_far, nodes, remaining_time):
    last_visited = open_so_far[-1]
    return [(node, dist) for node in nodes if node not in open_so_far and remaining_time > (dist:=SHORTEST_PATHS[(last_visited, node)])]



def solve(nodes, start):
    valid_valves = {valve for valve in nodes if FLOWS[valve] != 0}
    remaining_time = 30 - SHORTEST_PATHS[('AA', start)] - 1
    max_pressure = 0
    open_valves = [start]
    states = deque([(open_valves, remaining_time, remaining_time*FLOWS[start])])
    solved_states = []

    while states:
        current_state = states.pop()
        open_so_far, remaining_time, pressure = current_state

        visit_next = to_open(open_so_far, nodes, remaining_time) 
        # define solved state first:
        # - remaining time must be greater than or equal to zero (we will never add those states)
        # - or there are no other possible visits available
        if remaining_time < 0:
            pressure = 0
        max_pressure = max(max_pressure, pressure)
        if remaining_time < 0:
            continue
        if not visit_next or remaining_time == 0:
            continue
        if len(valid_valves-set(open_so_far)) == 0:
            continue
        
        for valve, distance in visit_next:
            new_remaining = remaining_time - distance - 1
            states.append((open_so_far + [valve], new_remaining, pressure + FLOWS[valve]*new_remaining))

    return max_pressure




valid_valves = {valve for valve in nodes if FLOWS[valve] != 0}
print(ADJACENCY['AA'])
candidates = set(ADJACENCY['AA']) & valid_valves
print(candidates)
pressures = []
for valve in ADJACENCY['AA']:
    if valve not in valid_valves:
        continue
    print(f'solving valve {valve}....', end='')
    max_pressure = solve(valid_valves, valve)
    print(f'solved! {max_pressure}')
    pressures.append(max_pressure)

party_1 = max(pressures)
print_solutions(party_1)

# for state in solve(nodes, 'DD'):
#     print(state)


