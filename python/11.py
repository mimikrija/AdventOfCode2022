
from santas_little_helpers.helpers import *
from collections import deque

data = get_input('inputs/11.txt', False, '\n\n')
data = get_input('inputs/11e.txt', False, '\n\n')


monkeys = []
for chunk in data:
    lines = chunk.split('\n')
    for n, line in enumerate(lines):
        if n == 0:
            monkey = line[:-1]
            print(monkey)
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
    monkeys.append([deque(eval(items)), operation, test, actiont, actionf])



def round(monkeys):
    for num, monkey in enumerate(monkeys):
        while monkey[0]:
            old = monkey[0].popleft()
            print(f'monkey {num} inspects item of worry level of {old}')
            new = eval(monkey[1])
            new //= 3
            if new % monkey[2]:
                monkeys[monkey[3]][0].append(new)
            else:
                monkeys[monkey[4]][0].append(new)
        


for _ in range(1):
    round(monkeys)


for monkey in monkeys:
    print(len(monkey[0]))



