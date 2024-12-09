from itertools import batched

from tqdm import tqdm

from aoc import get_input

diskmap = "2333133121414131402"
diskmap = get_input(day=9, as_list=False)

disk = []
for id, batch in enumerate(batched(diskmap, n=2)):
    block = int(batch[0])
    free_ = int(batch[1]) if len(batch) == 2 else 0

    disk.extend([int(id)] * int(block))
    disk.extend([None] * int(free_))

# 9-1
def defrag1(disk):
    insert = 0
    remove = len(disk) - 1
    while insert < remove:
        while disk[insert] is not None:
            insert += 1
        while disk[remove] is None:
            remove -= 1

        if insert < remove:
            disk[insert] = disk[remove]
            disk[remove] = None
            insert += 1
            remove -= 1
    return disk

def score(disk):
    checksum = 0
    for p, id in enumerate(disk):
        if id is not None:
            checksum += p * id
    return checksum

print(score(defrag1(disk[:])))

# 9-2
def get_indices(id, disk):
    return [i for i, j in enumerate(disk) if j == id]

def collapse(indices):
    lens = [[indices[0]],]
    for idx in indices[1:]:
        if idx - lens[-1][-1] == 1:
            lens[-1].append(idx)
        else:
            lens.append([idx])
    return lens

def firstgap(l, before, disk):
    gaps = get_indices(None, disk)
    lens = collapse(gaps)

    i = 0
    for gap in lens:
        if gap[-1] >= before:
            return None
        if len(gap) >= l:
            return gap
    return None

def defrag2(disk):
    for id in tqdm(range(max(id for id in disk if id is not None), -1, -1)):
        id_idc = get_indices(id, disk)
        size = len(id_idc)

        gap = firstgap(size, id_idc[0], disk)

        if gap is not None:
            for gap_idx in gap[:size]:
                disk[gap_idx] = id
            for id_idx in id_idc:
                disk[id_idx] = None
    return disk

print(score(defrag2(disk[:])))
