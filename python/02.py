# Day 2: Rock Paper Scissors


from santas_little_helpers.helpers import *

second_wins = ('C X', 'A Y', 'B Z')
ties = ('A X', 'B Y', 'C Z')

games = get_input('inputs/02.txt')

party_1 = sum(6*(game in second_wins) + 3*(game in ties) +
                 + ('X' in game) + 2*('Y' in game) + 3*('Z' in game)
                                                    for game in games)

first_wins = ('B X', 'C Y', 'A Z')

def desired_outcome(game):
    return sum(3*n*(c in game) for n, c in enumerate(('X', 'Y', 'Z')))


def part_2(games):
    result = 0
    for game in games:
        outcome_points = desired_outcome(game)
        if outcome_points == 6:
            result += 2*('A' in game) + 3*('B' in game) + ('C' in game)
        if outcome_points == 3:
            result += ('A' in game) + 2*('B' in game) + 3*('C' in game)
        if outcome_points == 0:
            result += 3*('A' in game) + ('B' in game) + 2*('C' in game)
        result += outcome_points
    return result



party_2 = part_2(games)


print_solutions(party_1, party_2)


def test_one():
    assert party_1 == 12794

def test_two():
    assert party_2 == 14979
