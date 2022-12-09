# Day 9: Rope Bridge

from santas_little_helpers.helpers import *

MOVE = {
    'R': 1+0j,
    'L':-1+0j,
    'D': 0+1j,
    'U': 0-1j,
    }

def get_nine(position):
    "return 9 neighbors of `position`"
    x = position.real
    y = position.imag
    return {complex(xn, yn) for xn, yn in ((x + dx, y + dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1))}

def is_touching(head, tail):
    return tail in get_nine(head)

def unit(num):
    get_unit = lambda x: x/abs(x) if x != 0 else x
    dx = get_unit(num.real)
    dy = get_unit(num.imag)
    return complex(dx, dy)


def move_tail(new_head, old_tail):
    if is_touching(new_head, old_tail):
        return old_tail
    return old_tail + unit(new_head - old_tail)


def move_the_rope(instructions, rope_length):
    rope = rope_length*[0+0j]
    tail_positions = {rope[-1]}

    for direction, qt in instructions:
        for _ in range(1, qt+1):
            rope[0] += MOVE[direction] # update head poisition
            for pos in range(1, rope_length):
                # all knots need to follow the head
                rope[pos] = move_tail(rope[pos-1], rope[pos])
            tail_positions.add(rope[rope_length-1])
    
    return len(tail_positions)




data = get_input('inputs/09.txt')

instructions = [(line.split()[0], int(line.split()[1])) for line in data]

party_1, party_2 = (move_the_rope(instructions, rope_length) for rope_length in (2, 10))

print_solutions(party_1, party_2)


def test_one():
    assert party_1 == 5695

def test_two():
    assert party_2 == 2434
