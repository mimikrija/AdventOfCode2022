# Day 13: Distress Signal

from santas_little_helpers.helpers import *

def compare(left, right):
    if all(isinstance(num, int) for num in (left, right)):
        if left < right:
            return True
        elif right > left:
            return False
        return

    if all(isinstance(num, list) for num in (left, right)):
        for l, r in zip(left, right):
            result = compare(l, r)
            if result is not None:
                return result
        return len(left) < len(right)
    
    else:
        to_list = lambda x: [x] if isinstance(x, int) else x
        compare(to_list(left), to_list(right))
        # if result is not None:
        #     return result
    


pairs = (list(map(eval, chunk.split('\n'))) for chunk in get_input('inputs/13.txt', False, '\n\n'))

party_1 = sum(n for n, pair in enumerate(pairs, 1) if  compare(*pair))

print_solutions(party_1)


def test_one():
    assert party_1 == 4809

def test_two():
    assert party_2 == 22600
