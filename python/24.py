from santas_little_helpers.helpers import *
from math import lcm



input_data = read_input(24)

no_borders_map = [line[1:-1] for line in input_data[1:-1]]
START = 0-1j
LENGTH = len(no_borders_map[0])
HEIGHT = len(no_borders_map)
END = complex(LENGTH-1, HEIGHT)


print(lcm(LENGTH, HEIGHT))

# initialize blizzards
blizzards = {direction: [set()] for direction in '><^v'}

for y, row in enumerate(no_borders_map):
    for x, direction in enumerate(row):
        if direction in '><^v':
            blizzards[direction][0].add(complex(x, y))

#print (blizzards)


MOVE = {
    '>': 1+0j,
    '<':-1+0j,
    '^': 0-1j,
    'v': 0+1j,
}

# blizzards = dict{direction: list of sets, list pos is the time}

horiz_check = lambda x: LENGTH if x == '>' else -1
x_start_from = lambda x: 0 if x == '>' else LENGTH - 1

# update horizontal blizzards
for time in range(1, LENGTH):
    for direction in '><':
        new_positions = set()
        for pos in blizzards[direction][-1]:
            newpos = pos + MOVE[direction]
            if newpos.real == horiz_check(direction):
                newpos = complex(x_start_from(direction), newpos.imag)
            new_positions.add(newpos)
        blizzards[direction].append(new_positions)


vert_check = lambda x: HEIGHT if x == 'v' else -1
y_start_from = lambda x: 0 if x == 'v' else HEIGHT - 1
# update vertical blizzards
for time in range(1, HEIGHT):
    for direction in 'v^':
        new_positions = set()
        for pos in blizzards[direction][-1]:
            newpos = pos + MOVE[direction]
            if newpos.imag == vert_check(direction):
                newpos = complex(newpos.real, y_start_from(direction))
            new_positions.add(newpos)
        blizzards[direction].append(new_positions)



def get_positions(time):
    hor_time = time % LENGTH
    vert_time = time % HEIGHT
    positions = blizzards['>'][hor_time] | blizzards['<'][hor_time] | blizzards['v'][vert_time] | blizzards['^'][vert_time]
    return positions


occupied_positions = {time: get_positions(time) for time in range(lcm(HEIGHT, LENGTH))}

print(len(occupied_positions[lcm(HEIGHT, LENGTH)-1]))