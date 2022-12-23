from santas_little_helpers.helpers import *
from collections import deque, defaultdict

data = get_input('inputs/23.txt')

open_space, elves = ({complex(x, y) for y, row in enumerate(data) for x, c in enumerate(row) if c == criterion}
                        for criterion in ('.', '#'))

directions = deque([
    [-1-1j, 0-1j, 1-1j], # NW, N, NE
    [-1+1j, 0+1j, 1+1j], # SW, S, SE
    [-1-1j, -1+0j, -1+1j], # NW, W, SW
     [1-1j, 1+0j, 1+1j] # NE, E, SE
])

eight_directions = set(dir for direction in directions for dir in direction)
print(eight_directions)

def play_round(elves, directions):
    proposals = defaultdict(list)
    for elf in elves:
        if not any(elf + dir in elves for dir in eight_directions):
            continue
        for direction in directions:
            if not any(elf + dir in elves for dir in direction):
                proposals[elf+direction[1]].append(elf)
                break
    for new_elf, old_elves in proposals.items():
        if len(old_elves) == 1:
            elves.remove(old_elves[0])
            elves.add(new_elf)
    # no possible moves
    return elves, len(proposals) == 0

def get_elves_count_rectangle(elves):
    min_x = int(min(elves, key=lambda x: x.real).real)
    max_x = int(max(elves, key=lambda x: x.real).real)
    min_y = int(min(elves, key=lambda x: x.imag).imag)
    max_y = int(max(elves, key=lambda x: x.imag).imag)
    print(min_x, max_x, min_y, max_x)
    count = 0
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            if complex(x,y) not in elves:
                count += 1
    return count


def solve(in_elves, is_part_2):
    elves = set(in_elves)
    rounds = 0
    while True:
        elves, stop = play_round(elves, directions)
        directions.rotate(-1)
        rounds += 1
        if not is_part_2 and rounds == 10:
            return get_elves_count_rectangle(elves)
        elif stop:
            return rounds, get_elves_count_rectangle(elves)

party_2 =solve(elves, True)
print(party_2)


party_1, party_2 = (solve(elves, pt2) for pt2 in (False, True))
print_solutions(party_1, party_2)


