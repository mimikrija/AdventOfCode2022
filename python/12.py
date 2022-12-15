
from collections import deque

from santas_little_helpers.helpers import *

DELTAS ={
    -1+0j, # left
     1+0j, # right
     0+1j, # down
     0-1j, # up
}


def get_neighbors(location, heightmap):
    return (candidate for delta in DELTAS 
            if (candidate:=location + delta) in heightmap
                and heightmap[candidate] + 1 >= heightmap[location] )

def get_path_length(came_from, start, end):
    current = end
    path = []
    while current != start:
        if current not in came_from:
            return
        path.append(current)
        current = came_from[current]
    return len(path)


def shortest_path(heightmap, end, start=None):
    frontier = deque([end])
    came_from = {end: None}
    while frontier:
        current = frontier.popleft()

        if current == start:
                return get_path_length(came_from, end, start)
        if not start and heightmap[current] == ord('a'):
                return get_path_length(came_from, end, current)

        for neighbor in get_neighbors(current, heightmap):
            if neighbor not in came_from:
                frontier.append(neighbor)
                came_from[neighbor] = current


def parse(lines):
    heightmap = dict()
    for row, line in enumerate(lines):
        for col, elevation in enumerate(line):
            position = complex(col, row)
            match elevation:
                case 'E':
                    heightmap[position] = ord('z')
                    END = position
                case 'S':
                    heightmap[position] = ord('a')
                    START = position
                case _:
                    heightmap[position] = ord(elevation)
    return heightmap, START, END


heightmap, START, END = parse(get_input('inputs/12.txt'))





party_1 = shortest_path(heightmap, END, START)
party_2 = shortest_path(heightmap, END)

print_solutions(party_1, party_2)



def test_one():
    assert party_1 == 383

def test_two():
    assert party_2 == 377
