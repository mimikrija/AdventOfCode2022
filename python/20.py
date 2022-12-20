from santas_little_helpers.helpers import *
from collections import deque

data = get_input('inputs/20.txt', True, '\n')
original = [(num*811589153, pos) for pos, num in enumerate(data)]



def mixit(in_list, orig):
    output = deque(in_list)
    for pair in orig:
        while True:
            current = output.popleft()
            if current == pair:
                break
            output.append(current)

        num, pos = current
        output.rotate(-num)
        output.appendleft(current)
        output.rotate()
        #print([c for c, _ in output])
    return output

def get_numbers(linked, zero):

    ref = linked.index(zero)

    positions = [(ref+1000*n)%(len(linked)) for n in range(1, 4)]
    #print(positions)

    return sum(linked[pos][0] for pos in positions)

#print(deque(original))
p = original
for _ in range(10):
    p = mixit(p, original)
    #print(p)
    zero_pos = data.index(0)
    print(get_numbers(p, (0, zero_pos)))

