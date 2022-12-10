# Day 10: Cathode-Ray Tube

from santas_little_helpers.helpers import *

data = get_input('inputs/10.txt')


def cycles(instructions):
    x = 1
    sprite_positions = []
    for line in instructions:
        for _ in range(len(instruction:=line.split())):
            sprite_positions.append(x)
        try:
            x += int(instruction[1])
        except:
            pass
    return sprite_positions

def print_screen(sprite_positions):
    total_rows = len(sprite_positions)//40
    pixel = lambda x, pos: '#' if x-1 <= pos <= x+1 else ' '
    screen = [''.join(pixel(c, pos)
            for pos, c in enumerate(sprite_positions[row*40:(row+1)*40]))
            for row in range(total_rows)]
    for row in screen:
        print(row)
    return screen


sprite_positions = cycles(data)
party_1 = sum((n*40 + 20)*x for n, x in enumerate(sprite_positions[19::40]))

print_solutions(party_1)

party_2 = print_screen(sprite_positions)


def test_one():
    assert party_1 == 13860

def test_two():
    assert party_2[0] == '###  #### #  # ####  ##    ##  ##  ###  '
    assert party_2[1] == '#  #    # #  # #    #  #    # #  # #  # '
    assert party_2[2] == '#  #   #  #### ###  #       # #    ###  '
    assert party_2[3] == '###   #   #  # #    # ##    # #    #  # '
    assert party_2[4] == '# #  #    #  # #    #  # #  # #  # #  # '
    assert party_2[5] == '#  # #### #  # #     ###  ##   ##  ###  '
