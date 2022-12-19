
from santas_little_helpers.helpers import *

SHAPES = {
    '-': {n+0j for n in range(4)},
    '+': {n+1j for n in range(3)} | {complex(1, n) for n in range(3)},
    'L': {complex(n, 0) for n in range(3)} | {complex(2, n) for n in range(3)},
    'I': {complex(0,n) for n in range(4)},
    'n': {complex(m,n) for m in range(2) for n in range(2)}
}


DIRECTIONS = {
    '>': 1+0j, '<': -1+0j
}

DOWN = 0-1j

def drop_shape():
    sequence = ['-', '+', 'L', 'I', 'n']
    while True:
        yield sequence[0]
        sequence = sequence[1:] + sequence[:1]

def hot(data):
    size = len(data)
    n=0
    while True:
        yield data[n]
        n += 1
        if n==size:
            n=0


def initial_position(shape, high_point=0):
    # shift horizontally 1 step from the wall and 3 steps from the highest point
    return [point+complex(2, high_point+4) for point in SHAPES[shape]]

def touched(shape, taken):
    return any(point in taken for point in shape)

def highest_point(taken):
    return max(int(n.imag) for n in taken)


def play_tetris(num_of_rocks, hot_air, taken={n+0j for n in range(7)}):
    drop = drop_shape()
    hotm = hot(hot_air)
    for _ in range(num_of_rocks):
        height = highest_point(taken)
 #       print(height)
        current_shape = initial_position(next(drop), height)
        while True:
            previous = current_shape
            hot_move = next(hotm)
            current_shape = {c + DIRECTIONS[hot_move] for c in current_shape}
            
            if any(c.real < 0 or c.real > 6 for c in current_shape) or touched(current_shape, taken):
                current_shape = previous
            previous = current_shape
            current_shape = {c + DOWN for c in current_shape}
            if touched(current_shape, taken):
                taken |= set(previous)
                break
        #print(highest_point(taken))
    #print(sorted([t for t in taken if t.imag > 0], key=lambda x: x.imag))
    #print(taken)
    return highest_point(taken)




data = get_input('inputs/17.txt')[0]

party_1 = play_tetris(2022, data)
print_solutions(party_1)





def test_one():
    assert party_1 == 3157
