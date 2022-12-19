
from santas_little_helpers.helpers import *


MINUS = ['####']
PLUS = ['.#.',
        '###',
        '.#.']
L = ['..#',
     '..#',
     '###']
I = ['#',
     '#',
     '#',
     '#']
SQUARE = ['##',
          '##']

SHAPES = [[(2+col, row) for row, line in enumerate(reversed(shape)) 
                        for col, c in enumerate(line) if c == '#']
                        for shape in (MINUS, PLUS, L, I, SQUARE)]


def update_position(shape, dx, dy):
    return [(x+dx, y+dy) for (x, y) in shape]

def touched(shape, taken):
    return any(point in taken for point in shape)

def highest_point(taken):
    return max(taken, key=lambda x:x[1])[1]


def play_tetris(num_of_rocks, hot_air, taken={(x, 0) for x in range(7)}):
    num_h = 0
    for num_r in range(num_of_rocks):
        height = highest_point(taken)
        current_shape = update_position(SHAPES[num_r%len(SHAPES)], 0, height+4)
        while True:
            previous = current_shape
            hot_move = -1 + 2*(hot_air[num_h%len(hot_air)] == '>')
            num_h += 1
            current_shape = update_position(current_shape, hot_move, 0)
            
            if any(x < 0 or x > 6 for (x, y) in current_shape) or \
                touched(current_shape, taken):
                current_shape = previous
            previous = current_shape
            current_shape = update_position(current_shape, 0, -1)
            if touched(current_shape, taken):
                taken |= set(previous)
                break

    return highest_point(taken)




data = get_input('inputs/17.txt')[0]

party_1 = play_tetris(2022, data)
print_solutions(party_1)



def test_one():
    assert party_1 == 3157
