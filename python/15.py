
from santas_little_helpers.helpers import *
from re import findall
from collections import defaultdict
from itertools import combinations

data = get_input('inputs/15.txt')
#data = get_input('inputs/15e.txt')

def manhattan(one, two=0+0j):
    radius = one - two
    return int(abs(radius.real) + abs(radius.imag))

datad = []

for line in data:
    numbers = list(map(int, findall(r'-?\d+',line)))

    sensor = complex(numbers[0], numbers[1])
    beacon = complex(numbers[2], numbers[3])
    datad.append((sensor, beacon))



circles = []
for sensor, beacon in datad:
    center, distance = sensor, manhattan(beacon, sensor)
    circles.append((center, distance))


CHECK_Y = 2000000
#CHECK_Y = 10
taken = set()
for sensor, beacon in datad:
    if sensor.imag == CHECK_Y:
        taken.add(int(sensor.real))
    if beacon.imag == CHECK_Y:
        taken.add(int(beacon.real))




total = set()
for cent, radius in circles:
    vert = int(abs(cent.imag - CHECK_Y))
    if radius < vert:
        continue
    #print(vert)
    hor = int(abs(radius - vert))
    r = set(range(int(cent.real-hor), int(cent.real + hor)+1))
    total |= r

total -= taken


#print(sorted(total))
print(len(total)) # not 5843797
#                       5843797
# not 5843798

# pt 2

def in_circle(pos, circle):
    center, radius = circle
    return manhattan(pos, center) <= radius

to_check = set()
for center, radius in circles:
    perimeter = set()
    for x in range(0, radius + 2):
        y = radius - x + 1
        for sign_x in (-1, 1):
            for sign_y in (-1, 1):
                pos_x = int(center.real + sign_x* x)
                pos_y = int(center.imag + sign_y*y)
                pos_x = 0 if pos_x < 0 else pos_x
                pos_x = 4000000 if pos_x > 4000000 else pos_x
                pos_y = 0 if pos_y < 0 else pos_y
                pos_y = 4000000 if pos_y > 4000000 else pos_y
                to_check.add(complex(pos_x, pos_y))
    #to_check.append(perimeter)

print(len(to_check))


for ch in to_check:
    if any(in_circle(ch, circle) for circle in circles):
        continue
    #if not any(in_circle(ch, circle) for circle in circles):
    print(ch.real*4000000 + ch.imag)
    break

