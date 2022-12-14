from santas_little_helpers.helpers import *
from itertools import zip_longest


pairs = [list(map(eval, chunk.splitlines())) for chunk in get_input('inputs/13.txt', False, '\n\n')]

def compare_pair(left, right):
    
    left, right
    #print(left, right)

    # both are integers
    if all(isinstance(s, int) for s in (left, right)):
        if left < right:
            return True
        if left > right:
            return False
        else:
            return
        # else continue checking the next chunk but how do I do that

    if not left:
        #print('left', left)
        return True
    if not right:
        #print('right', right)
        return False
    #print('I am here')
    if all(isinstance(s, list) for s in (left, right)):
        for first, second in zip_longest(left, right):
            if compare_pair(first, second) is None:
                continue
            else:
                return compare_pair(first, second)
    
    else:
        #print('helo2')
        if isinstance(left, int):
            left = [left]
        else:
            right = [right]
        return compare_pair(left, right)
    #print('last')
    #compare_pair([left[1:], right[1:]])

#print(compare_pair(pairs[4]))

class Pair():
    def __init__(self, inlist):
        self.val = inlist
    def __lt__(self, other):
        return compare_pair(self.val, other.val)

print(sum([n for n, pair in enumerate(pairs, 1)  if compare_pair(*pair)]))

pairs = [list(map(eval, line.splitlines())) for line in get_input('inputs/13.txt') if line !='']

pairs2 = [Pair(pair) for pair in pairs] + [Pair([[2]])] + [Pair([[6]])]


sorted_list = sorted(pairs2)
party_2 = 1
for n, pair in enumerate(sorted_list, 1):
    if pair.val == [[2]]  or pair.val == [[6]]:
        party_2 *= n

print(party_2)
