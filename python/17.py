
from collections import defaultdict

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

def column_heights(tower):
    return (highest_point(c for c in tower if c[0] == x) for x in range(7))

def drop_rocks(num_of_rocks, hot_air, tower={(x, 0) for x in range(7)}):
    num_h = 0
    num_r = 0
    states = defaultdict(list)
    while num_r < num_of_rocks:
        # drop new rock so that its lowest point
        # is 3 cells above the tower's highest point
        height = highest_point(tower)
        considered_rock = move(SHAPES[(index_r:=num_r%len(SHAPES))], 0, height+4)
        while True:
            # HORIZONTAL MOVE
            last_possible_rock = considered_rock
            # move rock horizontally...
            dx = -1 + 2*(hot_air[(index_h:=num_h%len(hot_air))] == '>')
            num_h += 1
            considered_rock = move(considered_rock, dx, 0)
            # ...revert it if it would result with any penetration!
            if penetrating_wall(considered_rock) or penetrating_floor(considered_rock, tower):
                considered_rock = last_possible_rock
            # DOWNWARD MOVE
            last_possible_rock = considered_rock
            # if vertical move results in penetration, add last possible one to the tower
            if penetrating_floor((considered_rock:=move(last_possible_rock, 0, -1)), tower):
                tower |= set(last_possible_rock)
                tower_deltas = tuple(y-height for y in column_heights(tower))
                states[(index_r, index_h, tower_deltas)].append(highest_point(tower))
                break
        
        num_r += 1

    return highest_point(tower)




data = get_input('inputs/17.txt')[0]
party_1 = drop_rocks(2022, data)
print_solutions(party_1)



def test_one():
    assert party_1 == 3157
