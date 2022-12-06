#
# AoC 2022
# M4RC0Sx - https://github.com/M4RC0Sx
#


from typing import List, Tuple


def read_input(path: str) -> Tuple[List[str], List[Tuple[int, int, int]]]:
    with open(path) as f:
        stacks, instructions = f.read().split('\n\n')
        stacks = [
            "".join(column).rstrip()
            for i, column in enumerate(zip(*stacks.splitlines()[-2::-1]))
            if i % 4 == 1
        ]
        instructions = [
            (int(line[1]), int(line[3]) - 1, int(line[5]) - 1)
            for line in map(str.split, instructions.splitlines())
        ]
    return stacks, instructions
