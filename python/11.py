# Day 11: Monkey in the Middle

from re import findall
from math import prod
from collections import deque

from santas_little_helpers.helpers import *

class Monkey():
    def __init__(self, data_chunk):
        monkey_data = data_chunk.split('\n')
        self.worries = deque(list(map(int, findall(r'\d+', monkey_data[1]))))
        op, arg = monkey_data[2].split(' ')[-2:]
        if arg == 'old':
            self.num = None
        else:
            self.operation = sum if op == '+' else prod
            self.num = int(arg)
        self.divisor, self.truemonkey, self.falsemonkey = (int(monkey_data[n].split(' ')[-1]) for n in range(3, 6))
        self.count = 0


def round(monkeys, common_divisor, is_part2=False):
    for monkey in monkeys:
        monkey.count += len(monkey.worries)
        while monkey.worries:
            worry = monkey.worries.popleft()
            if monkey.num:
                new_worry = monkey.operation([worry, monkey.num])
            else:
                new_worry = worry**2
            if not is_part2:
                new_worry //= 3
            new_worry %= common_divisor
            if new_worry % monkey.divisor == 0:
                monkeys[monkey.truemonkey].worries.append(new_worry)
            else:
                monkeys[monkey.falsemonkey].worries.append(new_worry)


def level_of_monkey_business(data, is_part_2):
    if not is_part_2:
        rounds = 20
    else:
        rounds = 10000
    monkeys = [Monkey(chunk) for chunk in data]
    common_divisor = prod(monkey.divisor for monkey in monkeys)
    for _ in range(rounds):
        round(monkeys, common_divisor, is_part_2)
    return prod(sorted([monkey.count for monkey in monkeys], reverse=True)[:2])


data = get_input('inputs/11.txt', False, '\n\n')

party_1, party_2 = (level_of_monkey_business(data, is_part_2) for is_part_2 in (False, True))

print_solutions(party_1, party_2)


def test_one():
    assert party_1 == 54036

def test_two():
    assert party_2 == 13237873355
