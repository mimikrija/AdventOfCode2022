
from santas_little_helpers.helpers import *
from re import findall
from collections import deque

data = get_input('inputs/15.txt')
#data = get_input('inputs/15e.txt')

def manhattan(one, two=(0,0)):
    dist = tuple(one[n]-two[n] for n in (0, 1))
    return sum(abs(d) for d in dist)

circles = []

for line in data:
    numbers = list(map(int, findall(r'-?\d+',line)))
    sensor = (numbers[0], numbers[1])
    beacon = (numbers[2], numbers[3])
    circles.append((sensor, manhattan(sensor, beacon)))


def merge_ranges(first, second):
    Lf, Rf = first
    Ls, Rs = second
    if Rs + 1 <= Rf:
        return [Lf, Rf]
    if Ls <= Rf:
        return [Lf, Rs]


def whole(ranges):
    ranges = deque(ranges)
    while len(ranges) >= 2:
        first, second = (ranges.popleft() for _ in range(2))
        new_range = merge_ranges(first, second)
        if new_range:
            ranges.appendleft(new_range)
        else:
            return first[1] + 1


def check_row(circles, row=10):
    taken = [2*[center[0]] for center, _ in circles if center[1] == row]
    for (X, Y), radius in circles:
        y = abs(Y - row)
        if y > radius:
            continue
        dx = radius - y
        taken.append([X-dx, X+dx])
    taken.sort()
    x = whole(taken)
    if x:
        print(x, row, x*4000000 + row)
        return x

for y in range(4000000+1):
    if check_row(circles, y):
        break

quit()

# MIN_X = min(all_x)
# MAX_X = max(all_x)
# print(MAX_X-MIN_X)

distances = []
for sensor, beacon in datad:
    center, distance = sensor, manhattan(beacon, sensor)
    distances.append((center, distance))


CHECK_Y = 2000000
#CHECK_Y = 10
taken = set()
for sensor, beacon in datad:
    # if sensor.imag == CHECK_Y:
    #     taken.add(int(sensor.imag))
    if beacon.imag == CHECK_Y:
        taken.add(int(beacon.imag))

total = set()
for cent, dist in distances:
    vert = int(abs(cent.imag - CHECK_Y))
    hor = int(abs(dist - vert))
    #print(cent, dist, 'hor ', hor, 'vert', vert)
    r = set(range(int(cent.real-hor), int(cent.real + hor+1)))
    #print(cent, sorted(r))
    total |= r

total -= taken


#print(sorted(total))
print(len(total)) # not 5843797
#                       5843797
# not 5843798