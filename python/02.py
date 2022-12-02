# Day 2: Rock Paper Scissors


from santas_little_helpers.helpers import *

RPS = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
}

SHAPE_VALUE = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}

DESIRED_OUTCOME = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

def outcome(elf, me):
    # draw
    if elf == me:
        return 3
    # elf wins
    if elf == 'rock' and me == 'scissors' or elf == 'scissors' and me == 'paper' or elf == 'paper' and me == 'rock':
        return 0
    # I win
    return 6

def what_to_get(outcome, elf):
    if outcome == 3:
        return elf
    if outcome == 6:
        if elf == 'rock':
            return 'paper'
        if elf == 'scissors':
            return 'rock'
        if elf == 'paper':
            return 'scissors'
    if outcome == 0:
        if elf == 'rock':
            return 'scissors'
        if elf == 'scissors':
            return 'paper'
        if elf == 'paper':
            return 'rock'


data = [line.split() for line in get_input('inputs/02.txt')]

party_1 = sum(SHAPE_VALUE[RPS[me]] + outcome(RPS[elf], RPS[me]) for elf, me in data)
party_2 = sum(DESIRED_OUTCOME[me] + SHAPE_VALUE[what_to_get(DESIRED_OUTCOME[me], RPS[elf])] for elf, me in data)


print_solutions(party_1, party_2)


def test_one():
    assert party_1 == 12794

def test_two():
    assert party_2 == 14979
