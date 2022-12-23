from santas_little_helpers.helpers import *
from collections import deque, defaultdict

data = get_input('inputs/23e.txt')

open_space, elves = ({complex(x, y) for y, row in enumerate(data) for x, c in enumerate(row) if c == criterion}
                        for criterion in ('.', '#'))

directions = deque([
    [-1-1j, 0-1j, 1-1j], # NW, N, NE
    [-1+1j, 0+1j, 1+1j], # SW, S, SE
    [-1-1j, -1+0j, -1+1j], # NW, W, SW
     [1-1j, 1+0j, 1+1j] # NE, E, SE
])


def play_round(elves, directions):
    proposals = defaultdict(list)
    for elf in elves:
        for direction in directions:
            if not any((candidate := elf + dir) in elves for dir in direction):
                proposals[candidate].append(elf)
                break
    for new_elf, old_elves in proposals.items():
        if len(old_elves) == 1:
            # i need to add here that it does not move towards proposal but towards general direction
            
            elves.remove(old_elves[0])
            elves.add(new_elf)
    return elves
    if len(proposals) == 0: # no possible moves
        return elves

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


for _ in range(10):
    elves = play_round(elves, directions)
    directions.rotate(-1)

print(get_elves_count_rectangle(elves))

