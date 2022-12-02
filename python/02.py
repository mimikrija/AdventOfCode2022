from santas_little_helpers.helpers import *

data = [line.split() for line in get_input('inputs/02.txt')]
print(data[0])


RPS = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
}

scores = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}

def outcome(elf, me):
    # draw
    if elf == me:
        return 3
    if elf == 'rock' and me == 'scissors':
        return 0
    if elf == 'scissors' and me == 'paper':
        return 0
    if elf == 'paper' and me == 'rock':
        return 0
    return 6
party_1 = 0
for first, second in data:
    party_1 +=  scores[RPS[second]] + outcome(RPS[first], RPS[second])


#party_1 = sum(outcome(RPS[first], RPS[second]) + scores[RPS[second]] for first, second in data)

print(party_1) #12794

pt2 = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

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
party_2 = 0
for first, second in data:
    party_2 += pt2[second] + scores[what_to_get(pt2[second], RPS[first])]

print(party_2)


def test_one():
    assert party_1 == 12794

def test_two():
    assert party_2 == 14979
    