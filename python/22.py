from re import findall
from santas_little_helpers.helpers import *

def parse_instructions(in_string):
    letters = findall(r'[A-Z]', in_string) + ['']
    numbers = list(map(int, findall(r'\d+', in_string)))
    return [*zip(numbers, letters)]

orientation = lambda x: -1j if x == 'L' else 1j

SIDE_MAPPING = {
    #   R  D  L  U
    1: [4, (3, False), 2, 6],
    2: [1, 3, 5, 6],
    3: [1, 4, 5, 2],
    4: [1, 6, 5, 3],
    5: [4, 6, 2, 3],
    6: [4, 1, 2, 5],
}


def wrapped(pos, all_tiles, facing):
    if facing == 1+0j: # RIGHT
        return min((tile for tile in all_tiles if tile.imag == pos.imag), key=lambda x: x.real)
    if facing == -1+0j: # LEFT
        return max((tile for tile in all_tiles if tile.imag == pos.imag), key=lambda x: x.real)
    if facing == 0+1j: #DOWN
        return min((tile for tile in all_tiles if tile.real == pos.real), key=lambda x: x.imag)
    if facing == 0-1j: # UP
        return max((tile for tile in all_tiles if tile.real == pos.real), key=lambda x: x.imag)



def facing_number(facing):
    if facing == 1+0j: # RIGHT
        return 0
    if facing == 0+1j: # DOWN
        return 1
    if facing == -1+0j: # LEFT
        return 2
    if facing == 0-1j: # UP
        return 3

def direction_from_facing(num):
    if num == 0:
        return 1+0j # RIGHT
    if num ==1:
        return 0+1j # DOWN
    if num == 2:
        return -1+0j # LEFT
    if num == 3:
        return 0-1j # UP

def get_zone(current, zones):
    return 1

def wrap_cube(old_pos, zone, facing):
    direction_index = facing_number(facing)
    current_zone = get_zone(old_pos)
    new_zone = SIDE_MAPPING[current_zone][direction_index]
    new_direction = SIDE_MAPPING[new_zone].index(current_zone)
    new_facing = direction_from_facing(new_direction)
    candidates = zone_sides[new_direction][new_facing]
    old_pos_index = zone_sides[direction_from_facing(facing)].index(old_pos)
    return candidates[old_pos_index]





def move(instructions, open_tiles, walls):
    all_tiles = open_tiles | walls
    facing = 1+0j
    current = min(open_tiles, key=lambda x: x.imag)
    for steps, rotation in instructions:
        #print(f'starting from {current}, attempt going {steps} steps, rotation is {facing}')
        for _ in range(steps):
            current_x = current.real
            current_y = current.imag
            if (new_pos:=current + facing) in all_tiles: # no wrapping
                if new_pos in open_tiles:
                    current = new_pos
                else: # movement not possible
                    break
            else: # we need to wrap
                new_pos = wrapped(new_pos, all_tiles, facing)
                if new_pos in open_tiles:
                    current = new_pos
                else:
                    break
        if rotation:
            facing *= orientation(rotation)
    return int(current.real*4 + current.imag*1000 + facing_number(facing))


data = get_input('inputs/22.txt', False, '\n\n')

open_tiles, walls = ({complex(x, y) for y, row in enumerate(data[0].split('\n'), 1) for x, c in enumerate(row, 1) if c == criterion}
                        for criterion in ('.', '#'))

all_tiles = open_tiles | walls
zones = {}
zones[1] = set(c for c in all_tiles if 101 <= c.real <= 150 and 1 <= c.imag <= 50)
zones[2] = set(c for c in all_tiles if 51 <= c.real <= 100 and 1 <= c.imag <= 50)
zones[3] = set(c for c in all_tiles if 51 <= c.real <= 100 and 51 <= c.imag <= 100)
zones[4] = set(c for c in all_tiles if 51 <= c.real <= 100 and 101 <= c.imag <= 150)
zones[5] = set(c for c in all_tiles if 1 <= c.real <= 50 and 101 <= c.imag <= 150)
zones[6] = set(c for c in all_tiles if 1 <= c.real <= 50 and 151 <= c.imag <= 200)


# coordinates if you come from: R D L U
zone_sides = {
    1: [[complex(150, y) for y in range(1, 51)], [complex(x, 50) for x in range(101, 151)], None, [complex(x, 1) for x in range(101, 151)]],
    2: [None, None, [complex(51, y) for y in range(1, 51)], [complex(x, 1) for x in range(51, 101)]],
    3: [[complex(100, y) for y in range(51, 101)], None, [complex(51, y) for y in range(51, 101)], None],
    4: [[complex(100, y) for y in range(101, 151)], [complex(x, 150) for x in range(51, 100)], None, None],
    5: [None, None, [complex(1, y) for y in range(101, 151)], [complex(x, 101) for x in range(1, 51)]],
    6: [[complex(50, y) for y in range(151, 201)], [complex(x, 200) for x in range(1, 51)], [complex(1, y) for y in range(151, 201)], None],
}



instr = parse_instructions(data[1])


party_1 = move(instr, open_tiles, walls)
print_solutions(party_1)




