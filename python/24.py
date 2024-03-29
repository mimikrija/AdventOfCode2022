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
    mapping = {'><': (ROWS[row], col),
               '^v': (COLUMNS[col], row)
               }

    # check rows/columns
    for blizzards, entities in mapping.items():
        line, pos = entities
        for blizzard in blizzards:
            pos_to_check = (pos + which_way(blizzard)*time) % len(line)
            if line[pos_to_check] == blizzard:
                return False

    return True


def blizzard_first_search(start, end, start_time=0):
    reached = {start}
    time = start_time
    while reached:
        if end in reached:
            return time
        time += 1
        reached = {guy for current in reached for guy in get_four_neighbors(current) | {current} if no_blizzard(guy, time)}



party_1 = blizzard_first_search(START, END)
party_2 = blizzard_first_search(START, END, blizzard_first_search(END, START, party_1+1)+1)

print_solutions(party_1, party_2)



def test_one():
    assert party_1 == 299


def test_two():
    assert party_2 == 899
