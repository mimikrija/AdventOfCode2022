from santas_little_helpers.helpers import *
from collections import deque


input_data = read_input(24)

no_borders_map = [line[1:-1] for line in input_data[1:-1]]

ROWS = no_borders_map
COLUMNS = list(zip(*no_borders_map))

MAX_X = len(COLUMNS)-1
MAX_Y = len(ROWS)-1

START = (0, -1)
END = (MAX_X, MAX_Y+1)

def no_blizzard(position, time):
    if position == START or position == END:
        return True
    col, row = position
    if not 0 <= col <= MAX_X:
        return False
    if not 0 <= row <= MAX_Y:
        return False
    which_way = lambda d: -1 if d in '>v' else 1
    # check rows
    line = ROWS[row]
    
    for blizzard in '><':
        pos_to_check = (col + which_way(blizzard)*time) % len(line)
        if line[pos_to_check] == blizzard:
            return False

    # check columns
    line = COLUMNS[col]
    for blizzard in '^v':
        pos_to_check = (row + which_way(blizzard)*time) % len(line)
        if line[pos_to_check] == blizzard:
            return False
    
    return True

def blizzard_first_search(start, end, start_time=0):
    
    frontier = deque([(start, start_time)])
    reached = set((start, start_time))
    while frontier:
        current, time = frontier.popleft()
        five_guys = {guy for guy in get_four_neighbors(current) | {current} if no_blizzard(guy, time+1)}

        for pos in five_guys:
            if pos == end:
                return time+1
            if (pos, time+1) not in reached:
                frontier.append((pos, time+1))
                reached.add((pos, time+1))


party_1 = blizzard_first_search(START, END)
party_2 = blizzard_first_search(START, END, blizzard_first_search(END, START, party_1+1)+1)

print_solutions(party_1, party_2)

def test_one():
    assert party_1 == 299

def test_two():
    assert party_2 == 899
