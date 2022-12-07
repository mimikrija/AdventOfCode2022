# Day 7: No Space Left On Device

from collections import defaultdict

from santas_little_helpers.helpers import *


def generate_subfolder_paths(current_level):
    return {'/'.join(c for c in current_level[:n]) for n in range(len(current_level), 0, -1)}


def parse_filesystem(data):
    current_level = []
    dir_sizes = defaultdict(int)

    for line in data:
        if '$ ls' in line:
            continue

        if '$ cd' in line:
            if (arg:=line.split()[-1]) == '..':
                current_level.pop()
            else:
                current_level.append(arg)

        else: # output
            if (size:=line.split()[0]) != 'dir':
                # add this file size to all possible subfolders it belongs to
                for subdir in generate_subfolder_paths(current_level):
                    dir_sizes[subdir] += int(size)

    return dir_sizes




data = get_input('inputs/07.txt')

sizes = parse_filesystem(data)


party_1 = sum(size for size in sizes.values() if size <= 100000)


unused_space = 70000000 - sizes['/']
space_needed = 30000000 - unused_space

party_2 = min(filter(lambda size: size >= space_needed, sizes.values()))


print_solutions(party_1, party_2)



def test_one():
    assert party_1 == 1886043

def test_two():
    assert party_2 == 3842121
