
from santas_little_helpers.helpers import *
from cmath import phase
from math import sqrt


data = get_input('inputs/09.txt')
data = get_input('inputs/09e.txt')

movements = [(line.split()[0], int(line.split()[1])) for line in data]

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
    if tail in get_nine(head):
        return True
    return False

mag = lambda x: sqrt(x.real**2+x.imag**2)

def sign(num):
    x = num.real
    y = num.imag


    return complex(x/abs(x) if x != 0 else x, y/abs(y) if y !=0 else y)

def inrow(num1, num2):
    return num1.real == num2.real

def incolumn(num1, num2):
    return num1.imag == num2.imag

def move_tail(new_head, old_tail):
    if is_touching(new_head, old_tail):
        return old_tail
    

    if (inrow(old_tail, new_head) and abs(old_tail.imag - new_head.imag) == 2) or \
        (incolumn(old_tail, new_head) and abs(old_tail.real - new_head.real)==2):
        diff =new_head - old_tail
        return old_tail + sign(diff)
    
    elif not inrow(old_tail, new_head) and not incolumn(old_tail, new_head):
        # move diagonaly one step
        diff =new_head - old_tail

        return old_tail + sign(diff)


head = 0+0j
tail = 0+0j
tail_positions = set()
for direction, qt in movements:
    #print(head, tail, qt)
    for step in range(1, qt+1):
        head += MOVE[direction]
        tail = move_tail(head, tail)
        tail_positions.add(tail)

print(len(tail_positions))


head = 0+0j
tail = 0+0j
rope = 10*[0+0j]
print(rope)
tail_positions = {tail}
for direction, qt in movements:
    for step in range(1, qt+1):
        rope[0] += MOVE[direction]
        for pos in range(1, 10):
            # all knots need to follow the head
            rope[pos] = move_tail(rope[pos-1], rope[pos])
        tail_positions.add(rope[9])

print(len(tail_positions))