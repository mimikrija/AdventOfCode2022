# Day 2: Rock Paper Scissors

from santas_little_helpers.helpers import *

pt_1_scores = ('B X', 'C Y', 'A Z', 'A X', 'B Y', 'C Z', 'C X', 'A Y', 'B Z')
pt_2_scores = ('B X', 'C X', 'A X', 'A Y', 'B Y', 'C Y', 'C Z', 'A Z', 'B Z')


games = get_input('inputs/02.txt')


party_1, party_2 = (sum(scores.index(game) + 1 for game in games) for scores in (pt_1_scores, pt_2_scores))



def test_one():
    assert party_1 == 12794

def test_two():
    assert party_2 == 14979
