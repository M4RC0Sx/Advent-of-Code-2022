#
# AoC 2022
# M4RC0Sx - https://github.com/M4RC0Sx
#


from typing import List, Tuple


def get_solution(input_lines: List[str]) -> Tuple[int, int]:

    elves = {}
    counter = 0
    for line in input_lines:
        if line != '':
            counter += int(line)
        else:
            elves[len(elves)] = counter
            counter = 0

    return tuple(max(elves.items(), key=lambda k: k[1]))
