
from santas_little_helpers.helpers import *
from re import findall

data = get_input('inputs/15.txt')
data = get_input('inputs/15e.txt')

def manhattan(one, two=0+0j):
    dist = one - two
    return int(abs(dist.real) + abs(dist.imag))

datad = []
all_x = []
for line in data:
    numbers = list(map(int, findall(r'-?\d+',line)))
    all_x.append(numbers[0])
    all_x.append(numbers[2])
    sensor = complex(numbers[0], numbers[1])
    beacon = complex(numbers[2], numbers[3])
    datad.append((sensor, beacon))

# MIN_X = min(all_x)
# MAX_X = max(all_x)
# print(MAX_X-MIN_X)

distances = []
for sensor, beacon in datad:
    center, distance = sensor, manhattan(beacon, sensor)
    distances.append((center, distance))


CHECK_Y = 2000000
CHECK_Y = 10
taken = set()
for sensor, beacon in datad:
    if sensor.imag == CHECK_Y:
        taken.add(int(sensor.imag))
    if beacon.imag == CHECK_Y:
        taken.add(int(beacon.imag))

total = set()
for cent, dist in distances:
    vert = int(abs(cent.imag - CHECK_Y))
    hor = int(abs(dist - vert))
    #print(cent, dist, 'hor ', hor, 'vert', vert)
    r = set(range(int(cent.real-hor), int(cent.real + hor+1)))
    print(cent, sorted(r))
    total |= r

total -= taken


print(sorted(total))
print(len(total)) # not 5843797
#                       5843797
# not 5843798