# Day 7: No Space Left On Device

from collections import defaultdict

from santas_little_helpers.helpers import *


def parse_filesystem(data):
    current_dir = []
    filesystem = dict()

    for line in data:
        if '$ ls' in line:
            continue

        if '$ cd' in line:
            if (arg:=line.split()[-1]) == '..':
                current_dir.pop()
            else:
                current_dir.append(arg)
            folder_name = '/'.join(c for c in current_dir)[1:]

        else: # output
            first, name = line.split()
            if first != 'dir': # just add file paths, ignore dirs
                filesystem[f'{folder_name}/{name}'] = int(first)

    return filesystem


def get_subfolder_sizes(filesystem):
    subfolders = set('/') # add root

    # get unique subfolder paths
    for name in filesystem.keys():
        test = name[1:].split('/')[:-1]
        subfolders |= {'/'+'/'.join(c for c in test[:n]) for n in range(len(test), 0, -1)}

    # generate dict of all subfolder sizes
    subfolder_sizes = defaultdict(int)
    for subfolder in subfolders:
        for name, size in filesystem.items():
            if subfolder == name[:len(subfolder)]:
                subfolder_sizes[subfolder] += size

    return subfolder_sizes



data = get_input('inputs/07.txt')

filesystem = parse_filesystem(data)
subfolder_sizes = get_subfolder_sizes(filesystem)

party_1 = sum(size for size in subfolder_sizes.values() if size <= 100000)


unused_space = 70000000 - subfolder_sizes['/']
space_needed = 30000000 - unused_space

party_2 = min(filter(lambda size: size >= space_needed, subfolder_sizes.values()))


print_solutions(party_1, party_2)



def test_one():
    assert party_1 == 1886043

def test_two():
    assert party_2 == 3842121
