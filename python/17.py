
from santas_little_helpers.helpers import *

SHAPES = {
    '-': {n+0j for n in range(4)},
    '+': {n+1j for n in range(3)} | {complex(1, -n) for n in range(3)},
    'L': {complex(n, 2) for n in range(3)} | {complex(2, n) for n in range(3)},
    'I': {complex(0,n) for n in range(4)},
    'n': {complex(m,n) for m in range(2) for n in range(2)}
}

DIRECTIONS = {
    '>': 1+0j, '<': -1+0j
}

DOWN = 0+1j

def drop_shape():
    sequence = ['-', '+', 'L', 'I' 'n']
    while True:
        yield sequence[0], SHAPES[sequence[0]]
        sequence = sequence[1:] + sequence[:1]



def initial_position(shape, high_point=0):
    # shift horizontally 1 step from the wall and 3 steps from the highest point
    return [point+complex(1, high_point+3) for point in SHAPES[shape]]

def touched(shape, taken):
    return any(point in taken for point in shape)

def highest_point(taken):
    return max(int(n.imag) for n in taken)


def play_tetris(num_of_rocks, hot_air, taken={n+0j for n in range(7)}):
    hot_air = reversed(hot_air)
    drop = drop_shape()
    for _ in range(num_of_rocks):
        height = highest_point(taken)
        current_shape = initial_position(next(drop_shape), height)
        while True:
            for _ in range (2):
                current_shape += DIRECTIONS[hot_air.pop()]
                potential_shape = current_shape + DOWN
            if potential_shape
        


print(SHAPES)



data = get_input('inputs/17.txt')[0]
data = get_input('inputs/17e.txt')[0]
print(data)