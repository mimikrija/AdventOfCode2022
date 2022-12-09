# Day 9: Rope Bridge

from santas_little_helpers.helpers import *

MOVE = {
    'R': 1+0j,
    'L':-1+0j,
    'D': 0+1j,
    'U': 0-1j,
    }


def unit(num):
    sign = lambda x: x/abs(x) if x != 0 else x
    dx = sign(num.real)
    dy = sign(num.imag)
    return complex(dx, dy)


def move_the_rope(instructions, rope_length):
    rope = [0+0j for _ in range(rope_length)]
    tail_positions = {rope[-1]}

    for direction, qt in instructions:
        for _ in range(qt):
            rope[0] += MOVE[direction] # update head poisition
            for pos in range(1, rope_length):
                # all knots need to follow the head
                if abs(diff := rope[pos-1] - rope[pos]) < 2:
                    continue
                rope[pos] += unit(diff)
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
