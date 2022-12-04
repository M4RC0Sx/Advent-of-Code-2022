#
# AoC 2022
# M4RC0Sx - https://github.com/M4RC0Sx
#


from typing import List, Tuple


def read_input(path: str) -> List[str]:
    with open(path) as f:
        lines = f.read().splitlines()
    return lines


def load_pair_from_line(line: str) -> Tuple[Tuple[int, ...]]:

    pair = []
    for i in line.split(','):
        val_range = i.split('-')
        pair.append(tuple(range(int(val_range[0]), int(val_range[1]) + 1)))

    return tuple(pair)
