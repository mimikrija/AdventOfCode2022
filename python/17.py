
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

def drop_rocks(num_of_rocks, hot_air):
    tower={(x, 0) for x in range(7)}
    num_h = 0
    num_r = 0
    states = defaultdict(list)
    cycle_found = False
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
                state = (index_r, index_h, tower_deltas)
                states[state].append((num_r, highest_point(tower)))
                cycle_found = len(states[state]) == 2
                break
        
        # cycle detection
        if cycle_found:
            delta_rocks, delta_height = (states[state][-1][pos] - states[state][-2][pos] for pos in (0, 1))
            print(delta_rocks, delta_height, num_r, states[state])
            first_occurence = states[state][0][0]
            multiplier, rest = divmod(num_of_rocks-first_occurence-1, delta_rocks)
            print(multiplier, rest)
            final = states[state][0][1] + multiplier*delta_height
            newh =  states[state][0][1]
            print(final)
            # find state with rest
            for state, bla in states.items():
                ir, _, _ = state
                nr, h = bla[0]
                if nr == first_occurence + rest :
                    print(nr, h, newh, newh-h)
                    addthis =  h-newh
                    return final+addthis

        num_r += 1

    return highest_point(tower)




data = get_input('inputs/17.txt')[0]
party_1, party_2 = (drop_rocks(elephant_number, data) for elephant_number in (2022, 1000000000000))
print_solutions(party_1, party_2)



def test_one():
    assert party_1 == 3157


def test_two():
    assert party_1 == 1581449275319
