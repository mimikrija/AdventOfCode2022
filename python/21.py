# Day 21: Monkey Math


from collections import deque

from santas_little_helpers.helpers import *


data = get_input('inputs/21.txt')

monkey_commands = {(data_split:=line.split(': '))[0]: command 
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

def yell(monkey_commands):
    commands = deque(((monkey, command) for monkey, command in monkey_commands.items()))
    while commands:
        monkey, command = commands.popleft()

        if not isinstance(monkey_commands[monkey], int):
            left, operation, right = command.split(' ')
            if isinstance(monkey_commands[left], int) and isinstance(monkey_commands[right], int):
                monkey_commands[monkey] = op(monkey_commands[left], operation, monkey_commands[right])
            else:
                commands.append((monkey, command))
    
    return monkey_commands['root']

party_1 = yell(monkey_commands)



def test_one():
    assert party_1 == 168502451381566
