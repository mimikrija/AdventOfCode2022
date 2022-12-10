from santas_little_helpers.helpers import *
from collections import defaultdict

data = get_input('inputs/10.txt')
#data = get_input('inputs/10e.txt')



cycle = 0
x=1
xses=[]
crt = defaultdict(str)
for line in data:
    ins = line.split()
    if len (ins) == 2:
        for _ in range(2):
            cycle += 1
        
            if cycle in range(20, 221, 40):
                print(x, x*cycle, line, cycle)
                xses.append(x*cycle)
            if cycle == 220:
                print (x, x*cycle, line, cycle)
            crt[cycle//40] += ''
        x += int(ins[1])
    else:
        cycle += 1
        if cycle in range(20, 221, 40):
                print(x, x*cycle, line, cycle)
                xses.append(x*cycle)

print(cycle)

print(sum(xses))