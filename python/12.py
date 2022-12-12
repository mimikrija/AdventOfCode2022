
from santas_little_helpers.helpers import *

from collections import deque
DELTAS ={
    -1+0j, # left
     1+0j, # right
     0+1j, # down
     0-1j, # up
}


def get_neighbors(location, cave_floor, cave_heights):
    neighbs = [candidate for candidate in (location + delta for delta in DELTAS) if candidate in cave_floor and cave_heights[candidate] <= cave_heights[location]+1]
    return sorted(neighbs, key=lambda x: cave_heights[x])



def traverse_floor(cave_floor, cave_heights, start, end):
    frontier = deque([start])
    reached = set({start})
    came_from = {start: None}
    while frontier:
        #print(frontier)
        current = frontier.pop()
        current_height = cave_heights[current]
        neighbors = get_neighbors(current, cave_floor, cave_heights)
        #print(neighbors)

        for neighbor in neighbors:
            if neighbor not in came_from: # and cave_heights[neighbor] <= current_height+1:
                #print(f'curent {current}, neighbor: {neighbor}')
                frontier.append(neighbor)
                reached.add(neighbor)
                came_from[neighbor] = current



    current = end
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    #path.append(start)
    return path
    #return reached



lines = get_input('inputs/12.txt')
#lines = get_input('inputs/12e.txt')

cave_floor = []
cave_heights = dict()
for row, line in enumerate(lines):
    for col, height in enumerate(line):
        position = complex(col, row)
        cave_floor.append(position)
        if height == 'E':
            cave_heights[position] = ord('z')
            END = position
        elif height == 'S':
            cave_heights[position] = ord('a')
            START = position
        else:
            cave_heights[position] = ord(height)

print(START, END)

visited = traverse_floor(cave_floor, cave_heights, START, END)
print(visited)
print(len(visited)) # not 509, 512, 589

