from collections import deque
from re import findall

from santas_little_helpers.helpers import *

data = get_input('inputs/05.txt')

operations = ((map(int, findall(r'\d+', line))) for line in data[10:])



crates = {
    1: deque('RGHQSBTN'),
    2: deque('HSFDPZJ'),
    3: deque('ZHV'),
    4: deque('MZJFGH'),
    5: deque('TZCDLMSR'),
    6: deque('MTWVHZJ'),
    7: deque('TFPLZ'),
    8: deque('QVWS'),
    9: deque('WHLMTDNC')
}

for qt, origin, destination in operations:
    buffer = deque([])
    for _ in range(qt):
        buffer.appendleft(crates[origin].pop())
    for _ in range(qt):
        crates[destination].append(buffer.popleft())

for c, p in crates.items():
    print(c, p.pop())

# PTWLTDSJV

def test_one():
    assert party_1 == 'PTWLTDSJV'

def test_two():
    assert party_2 == 'WZMFVGGZP'
