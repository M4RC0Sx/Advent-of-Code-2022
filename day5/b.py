#
# AoC 2022
# M4RC0Sx - https://github.com/M4RC0Sx
#


from typing import List, Tuple


def get_solution(stacks: List[str], instructions: List[Tuple[int, int, int]]) -> List[str]:

    new_stacks = stacks.copy()
    for qty, from_, to in instructions:
        new_stacks[to] += new_stacks[from_][-qty:][::1]
        new_stacks[from_] = new_stacks[from_][:-qty]

    return list(s[-1] for s in new_stacks)
