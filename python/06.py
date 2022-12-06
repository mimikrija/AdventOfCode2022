from santas_little_helpers.helpers import *

data = get_input('inputs/06.txt')[0]
#data = get_input('inputs/06e.txt')[0]
from itertools import permutations


for n, (on, tw, tr, fo) in enumerate(zip(data, data[1:], data[2:], data[3:])):
    if on != tw and on!= tr and on!= fo and tw != fo and tw!=tr and tr != fo:
        print(on, tw, tr, fo)
        print (n+4)
        break

# not 16

def get_fourteen(in_str):
    lists = [in_str[n:] for n in range(14)]
    return zip(*lists)

for n, bla in enumerate(get_fourteen(data)):
    if not any(c == f for c, f in permutations(bla, 2)):
        print(n+14)
        break