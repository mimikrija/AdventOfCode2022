
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


def move(shape, dx, dy):
    return [(x+dx, y+dy) for (x, y) in shape]

def penetrating_floor(shape, tower):
    return any(point in tower for point in shape)

def penetrating_wall(shape):
    return any(x < 0 or x > 6 for (x, y) in shape)

def highest_point(tower):
    return max(tower, key=lambda x:x[1])[1]


def drop_rocks(num_of_rocks, hot_air, tower={(x, 0) for x in range(7)}):
    num_h = 0
    for num_r in range(num_of_rocks):
        # drop new rock so that its lowest point
        # is 3 cells above the tower's highest point
        height = highest_point(tower)
        considered_rock = move(SHAPES[num_r%len(SHAPES)], 0, height+4)
        while True:
            last_possible_rock = considered_rock
            dx = -1 + 2*(hot_air[num_h%len(hot_air)] == '>')
            num_h += 1
            considered_rock = move(considered_rock, dx, 0)
            
            # skip horizontal action if it would result with penetration
            if penetrating_wall(considered_rock) or penetrating_floor(considered_rock, tower):
                considered_rock = last_possible_rock
            last_possible_rock = considered_rock
            considered_rock = move(considered_rock, 0, -1)
            if penetrating_floor(considered_rock, tower):
                tower |= set(last_possible_rock)
                break

    return highest_point(tower)




data = get_input('inputs/17.txt')[0]

party_1 = drop_rocks(2022, data)
print_solutions(party_1)



def test_one():
    assert party_1 == 3157
