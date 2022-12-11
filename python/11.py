
from santas_little_helpers.helpers import *
from collections import deque
from math import prod
from primefac import primefac

data = get_input('inputs/11.txt', False, '\n\n')
data = get_input('inputs/11e.txt', False, '\n\n')


monkeys = []
for chunk in data:
    lines = chunk.split('\n')
    for n, line in enumerate(lines):
        if n == 0:
            monkey = line[:-1]
        bla = line.split(': ')
        if n == 1:
            items = '[' + bla[1] + ']'
        if n == 2:
            operation = bla[1].split('= ')[-1]
        if n == 3:
            test = int(bla[1].split(' ')[-1])
        if n == 4:
            actiont = int(bla[1][-1])
        if n == 5:
            actionf = int(bla[1][-1])
    monkeys.append([deque(eval(items)), operation, test, actiont, actionf, 0])



def round(monkeys):
    for num, monkey in enumerate(monkeys):
        while monkey[0]:
            old = monkey[0].popleft()
            monkey[5] += 1
            
            #print(f'monkey {num} inspects item of worry level of {old}')
            new = eval(monkey[1])

            new //= 3
            if new%monkey[2]==0:
                monkeys[monkey[3]][0].append(new)
            else:
                monkeys[monkey[4]][0].append(new)
        




for rou in range(20):
    round(monkeys)


top_inspectors = sorted((monkey[5] for monkey in monkeys), reverse=True)[:2]

party_1 = top_inspectors[0]*top_inspectors[1]

def test_one():
    assert party_1 == 54036







