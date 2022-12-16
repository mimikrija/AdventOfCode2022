from santas_little_helpers.helpers import *
from re import findall
from collections import deque
from itertools import permutations, combinations
from functools import lru_cache

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



@lru_cache
def calculate_flow(in_sequence):
    sequence = list_from_string(in_sequence)
    flow = 0
    if sequence[0] == 'AA':
        time = 30
    else:
        time = 30 - distances[('AA', sequence[0])]
    for valves in zip(sequence, sequence[1:]):
        time -= 1
        #print('opening valve ', valves[0], 'minute ', 30-time)
        flow += FLOWS[valves[0]]*time
        if time < 0:
            #print('here')
            return
        time -= distances[valves]
    #print('opening valve ', sequence[-1], 'minute ', 30-time+1)
    if time > 1:
        flow += FLOWS[sequence[-1]]*(time-1)
    return flow

released_pressure = lambda valve, remaining_time: FLOWS[valve] * remaining_time
valid_valves = [valve for valve, flow in FLOWS.items() if flow != 0]

def get_time(seq):
    time = distances[('AA', seq[0])] + 1
    print('opening valve ', seq[0], 'minute ', time)
    for first, second in zip(seq, seq[1:]):
        time += distances[(first, second)] + 1
        print('opening valve ', first, 'minute ', time)
    print('opening valve ', second, 'minute ', time)
    return time




@lru_cache
def list_from_string(x):
    return [''.join(c for c in s) for s in zip(x[::2], x[1::2])]

def string_from_list(y):
    return ''.join(c for x in y for c in x)

@lru_cache
def solve(str_seq):
    open_seq = list_from_string(str_seq)

    candidates = [valve for valve in valid_valves if valve not in open_seq]
    #print(str_seq)
    if not candidates:
        print(str_seq)
        return calculate_flow(string_from_list(open_seq))

    for candidate in candidates:
        solve(string_from_list(open_seq+[candidate]))
        return calculate_flow(string_from_list(open_seq))


# print(calculate_flow(string_from_list(['DD', 'BB', 'JJ', 'HH', 'EE','CC'])))
# #solve('AABBCC')
# #print(string_from_list(list_from_string('AABBCC')))

# print(max(solve(string_from_list([valve])) for valve in valid_valves))

# quit()

#@lru_cache
def dfs(states):
    finished_states = set()
    while states:
        open_seq, pressure = states.pop()
        if pressure is None:
            continue

        for valve in (v for v in valid_valves if v not in list_from_string(open_seq)):
            states.append((string_from_list(open_seq + valve), calculate_flow(string_from_list(open_seq + valve))))
    print(len(finished_states))
    return max(finished_states)
        
initial_states = [(start, calculate_flow(start)) for start in valid_valves]
print(initial_states)
print(dfs(initial_states))
quit()

def dfs(starting_position='AA', opened = list(), time=30):
    possibilities = (valves for valves in distances.keys()
                        if FLOWS[valve] != 0 and valve not in opened)
    print(starting_position, opened, time)
    for valve in possibilities:
        print(valve)
        opened.append(valve)
        dfs(valve, opened, time-distances[(starting_position, valve)]-1)





#print(max(calculate_flow(possibility) for possibility in posibilities))