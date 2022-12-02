# Day 2: Rock Paper Scissors

from santas_little_helpers.helpers import *

wins = ('C X', 'A Y', 'B Z')
ties = ('A X', 'B Y', 'C Z')
losses = ('B X', 'C Y', 'A Z')

RPS = {c: n+1 for n, c in enumerate('XYZ')}

games = get_input('inputs/02.txt')
possible_games = set(games)


scores_pt1 = {game: (sum(3*n*(game in outcome) for n, outcome in enumerate((ties, wins), 1)) + RPS[game[2]]) for game in possible_games}

party_1 = sum(scores_pt1[game] for game in games)

outcomes_pt2 = {'X': losses, 'Y': ties, 'Z': wins}

scores_pt2 = dict()
for game in possible_games:
    left, right = game.split()
    outcome = outcomes_pt2[right]
    for sc, out in enumerate(outcome, 1):
        if left in out:
            scores_pt2[game] = sc
    scores_pt2[game] += (RPS[right]-1)*3 # add game outcome = 6, 3 or 0



party_2 = sum(scores_pt2[game] for game in games)


print_solutions(party_1, party_2)


def test_one():
    assert party_1 == 12794

def test_two():
    assert party_2 == 14979
