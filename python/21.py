# Day 21: Monkey Math


from collections import deque

from santas_little_helpers.helpers import *


data = get_input('inputs/21.txt')

monkey_commands = {(data_split:=line.split(': '))[0]: command.split(' ')
                    if len((command:=data_split[1])) > 4 else int(command)
                    for line in data}

def op(first, command, second):
    if command == '+':
        return first + second
    if command == '-':
        return first - second
    if command == '*':
        return first*second
    if command == '/':
        return first // second

def yell(monkey_commands, which='root'):
    commands = deque(((monkey, command) for monkey, command in monkey_commands.items()))
    while commands:
        monkey, command = commands.popleft()

        if not isinstance(monkey_commands[monkey], int):
            left, operation, right = command
            if isinstance(monkey_commands[left], int) and isinstance(monkey_commands[right], int):
                monkey_commands[monkey] = op(monkey_commands[left], operation, monkey_commands[right])
            else:
                commands.append((monkey, command))
    
    return monkey_commands[which]

party_1 = yell(dict(monkey_commands))


# pt 2 binary search by hand haha
monkey_commands['humn'] = 3343167719435
first, _, second = monkey_commands['root']
monkey_commands['root'] = (first, '-', second)
if yell(monkey_commands) == 0:
    party_2 = monkey_commands['humn']


print_solutions(party_1, party_2)


def test_one():
    assert party_1 == 168502451381566

def test_two():
    assert party_2 == 3343167719435
