
from santas_little_helpers.helpers import *

from collections import deque
from queue import PriorityQueue
DELTAS ={
    -1+0j, # left
     1+0j, # right
     0+1j, # down
     0-1j, # up
}


def get_neighbors(location, cave_floor, cave_heights):
    return [candidate for candidate in get_four_neighbors(location) if candidate in cave_floor and cave_heights[candidate] <= cave_heights[location]+1]

def get_path_length(came_from, start, end):
    current = end
    path = []

    while current != start:
        path.append(current)
        try:
            current = came_from[current]
        except:
            return None

    return len(path)


def traverse_floor(cave_floor, cave_heights, start, end, min_length=None):
    frontier = PriorityQueue()
    frontier.put((0, start))
    cost_so_far = dict()
    cost_so_far[start] = ord('a')
    came_from = {start: None}
    while not frontier.empty():
        _, current = frontier.get()

        if current == end:
            return get_path_length(came_from, start, end)


        neighbors = get_neighbors(current, cave_floor, cave_heights)

        for neighbor in neighbors:
            #print(neighbor)
            height = cave_heights[current]
            new_cost = cost_so_far[current] + height
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]: # and cave_heights[neighbor] <= current_height+1:
                #print(f'curent {current}, neighbor: {neighbor}')
                cost_so_far[neighbor] = new_cost
                frontier.put((new_cost, neighbor))
                #priority = current_height
                came_from[neighbor] = current


    return get_path_length(came_from, start, end)




lines = get_input('inputs/12.txt')
#lines = get_input('inputs/12e.txt')

cave_floor = []
cave_heights = dict()
for row, line in enumerate(lines):
    for col, height in enumerate(line):
        position = (col, row)
        cave_floor.append(position)
        if height == 'E':
            cave_heights[position] = ord('z')
            END = position
        elif height == 'S':
            cave_heights[position] = ord('a')
            START = position
        else:
            cave_heights[position] = ord(height)

party_1 = traverse_floor(cave_heights.keys(), cave_heights, START, END)


current_min = len(cave_heights)
for pos, heig in cave_heights.items():
    if heig == ord('a'):
        #print(pos)
        bla = traverse_floor(cave_heights.keys(), cave_heights, pos, END, current_min)
        if bla is not None:
            current_min = new_min if (new_min:=bla) < current_min else current_min

party_2 = current_min

print_solutions(party_1, party_2)


def test_one():
    assert party_1 == 383

def test_two():
    assert party_2 == 377
