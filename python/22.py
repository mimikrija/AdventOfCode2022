from re import findall
from santas_little_helpers.helpers import *

def parse_instructions(in_string):
    letters = findall(r'[A-Z]', in_string) + ['']
    numbers = list(map(int, findall(r'\d+', in_string)))
    return [*zip(numbers, letters)]

orientation = lambda x: -1j if x == 'L' else 1j

SIDE_MAPPING = {
    #   R  D  L  U
    1: [4, 3, None, 6],
    2: [None, None, 5, 6],
    3: [1, None, 5, None],
    4: [1, 6, None, None],
    5: [None, None, 2, 3],
    6: [4, 1, 2, None],
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
    for zone, coordinates in zones.items():
        if current in coordinates:
            return zone




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


def move_cube(instructions, open_tiles, walls):
    all_tiles = open_tiles | walls
    facing = 1+0j
    current = min(open_tiles, key=lambda x: x.imag)
    for steps, rotation in instructions:
        #print(f'starting from {current}, attempt going {steps} steps, rotation is {facing}')
        for _ in range(steps):
            if (new_pos:=current + facing) in all_tiles: # no wrapping
                if new_pos in open_tiles: # or new_pos in walls: #TESTING ONLY
                    current = new_pos
                else: # movement not possible
                    break
            else: # we need to wrap
                new_pos, new_facing = wrap_cube(current, facing)
                if new_pos in open_tiles: #or new_pos in walls: #TESTING ONLY
                    current = new_pos
                    facing = new_facing
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
    4: [[complex(100, y) for y in range(101, 151)], [complex(x, 150) for x in range(51, 101)], None, None],
    5: [None, None, [complex(1, y) for y in range(101, 151)], [complex(x, 101) for x in range(1, 51)]],
    6: [[complex(50, y) for y in range(151, 201)], [complex(x, 200) for x in range(1, 51)], [complex(1, y) for y in range(151, 201)], None],
}
# (zone from, zone to): zip(coordinates from, coordinates to, resulting orientation
side_mapping = {
    (1, 3): (zone_sides[1][1], zone_sides[3][0], -1+0j),
    (3, 1): (zone_sides[3][0], zone_sides[1][1], 0-1j),
    (1, 4): (zone_sides[1][0], list(reversed(zone_sides[4][0])), -1+0j),
    (4, 1): (zone_sides[4][0], list(reversed(zone_sides[1][0])), -1+0j),
    (1, 6): (list(reversed(zone_sides[1][3])), zone_sides[6][1], 0-1j), # not 100% sure it is flipped
    (6, 1): (list(reversed(zone_sides[6][1])), zone_sides[1][3], 0+1j),
    (2, 5): (zone_sides[2][2], list(reversed(zone_sides[5][2])), 1+0j),
    (5, 2): (list(reversed(zone_sides[5][2])), zone_sides[2][2], 1+0j),
    (2, 6): (zone_sides[2][3], zone_sides[6][2], 1+0j), # 80% sure it is not flipped
    (6, 2): (zone_sides[6][2], zone_sides[2][3], 0+1j), # same
    (3, 5): (zone_sides[3][2], zone_sides[5][3], 0+1j),
    (5, 3): (zone_sides[5][3], zone_sides[3][2], 1+0j),
    (4, 6): (zone_sides[4][1], zone_sides[6][0], -1+0j),
    (6, 4): (zone_sides[6][0], zone_sides[4][1], 0-1j),
}


def wrap_cube(old_pos, facing):
    direction_index = facing_number(facing)
    current_zone = get_zone(old_pos, zones)
    new_zone = SIDE_MAPPING[current_zone][direction_index]
    # new_direction = SIDE_MAPPING[new_zone].index(current_zone)
    # new_facing = direction_from_facing(new_direction)
    #candidates = zone_sides[new_direction][new_facing]
    #old_pos_index = zone_sides[direction_from_facing(facing)].index(old_pos)
    from_coords, to_coords, new_facing = side_mapping[(current_zone, new_zone)]
    pos = from_coords.index(old_pos)
    return to_coords[pos], new_facing


instr = parse_instructions(data[1])


party_1 = move(instr, open_tiles, walls)
party_2 = move_cube(instr, open_tiles, walls)
#party_2 = move_cube([(200, None)], open_tiles, walls) # exclude walls to test if it wraps around ok (it does)
print_solutions(party_1, party_2)

# 189147 too high
#  15586 too low



