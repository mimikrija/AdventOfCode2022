
from santas_little_helpers.helpers import *
from re import findall

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



distances = []
for sensor, beacon in datad:
    center, distance = sensor, manhattan(beacon, sensor)
    distances.append((center, distance))


CHECK_Y = 2000000
#CHECK_Y = 10
taken = set()
for sensor, beacon in datad:
    if sensor.imag == CHECK_Y:
        taken.add(int(sensor.real))
    if beacon.imag == CHECK_Y:
        taken.add(int(beacon.real))



total = set()
for cent, radius in distances:
    vert = int(abs(cent.imag - CHECK_Y))
    if radius < vert:
        continue
    #print(vert)
    hor = int(abs(radius - vert))
    #print(cent, radius, 'hor ', hor, 'vert', vert)
    r = set(range(int(cent.real-hor), int(cent.real + hor)+1))
    #print(cent, sorted(r), radius, hor, vert)
    total |= r
print(taken)
total -= taken


#print(sorted(total))
print(len(total)) # not 5843797
#                       5843797
# not 5843798