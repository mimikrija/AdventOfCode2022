from collections import defaultdict, deque

from santas_little_helpers.helpers import *

data = get_input('inputs/07.txt')
#data = get_input('inputs/07e.txt')

current_dir = []
filesystem = dict()
for line in data:
    cmd = line.split()
    if '$' in line:
        size = 0
        if cmd[1] == 'cd':
            if cmd[2] != '..':
                current_dir.append(cmd[2])
            else:
                current_dir.pop()
        else: # list files
            folder_name = '/'.join(c for c in current_dir)[1:]
    else: # output
        try:
            size, filename = int(cmd[0]), cmd[1]
            filesystem[folder_name + '/' + filename] = size
        except:
            pass

tot = 0
subfolders = set('/')
for name, size in sorted(filesystem.items()):
    test = name[1:].split('/')[:-1]
    subfolders |= {'/'+'/'.join(c for c in test[:n]) for n in range(len(test), 0, -1)}
    tot += size


subfolder_sizes = defaultdict(int)

for subfolder in subfolders:
    for name, size in filesystem.items():
        if subfolder == name[:len(subfolder)]:
            subfolder_sizes[subfolder] += size

party_1 = 0
for size in subfolder_sizes.values():
    if size <= 100000:
        party_1 += size

print(party_1)


req_size = 30000000
must_delete = 30000000 - (70000000-tot)

for size in sorted(subfolder_sizes.values()):
    if size >= must_delete:
        party_2 = size
        break

print(party_2)