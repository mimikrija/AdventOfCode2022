from re import findall
from santas_little_helpers.helpers import *

def parse_instructions(in_string):
    letters = findall(r'[A-Z]', in_string) + ['']
    numbers = list(map(int, findall(r'\d+', in_string)))
    return [*zip(numbers, letters)]

orientation = lambda x: -1j if x == 'L' else 1j

def wrapped(pos, all_tiles, facing):
    if facing == 1+0j:
        return min((tile for tile in all_tiles if tile.imag == pos.imag), key=lambda x: x.real)
    if facing == -1+0j:
        return max((tile for tile in all_tiles if tile.imag == pos.imag), key=lambda x: x.real)
    if facing == 0+1j:
        return min((tile for tile in all_tiles if tile.real == pos.real), key=lambda x: x.imag)
    if facing == 0-1j:
        return max((tile for tile in all_tiles if tile.real == pos.real), key=lambda x: x.imag)

def facing_number(facing):
    if facing == 1+0j:
        return 0
    if facing == 0+1j:
        return 1
    if facing == -1+0j:
        return 2
    if facing == 0-1j:
        return 3


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

instr = parse_instructions(data[1])


party_1 = move(instr, open_tiles, walls)
print_solutions(party_1)




