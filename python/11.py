
from santas_little_helpers.helpers import *

data = get_input('inputs/11.txt', False, '\n\n')
monkeys = []

def level_of_monkey_business(monkeys, rounds):
    pass

party_1, party_2 = (level_of_monkey_business(monkeys, rounds) for rounds in (20, 10000))


def test_one():
    assert party_1 == 54036

def test_two():
    assert party_2 == 13237873355
