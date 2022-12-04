#
# AoC 2022
# M4RC0Sx - https://github.com/M4RC0Sx
#


from typing import List, Tuple

from day4.common import load_pair_from_line


def __check_pair(pair: Tuple[Tuple[int, ...]]) -> bool:
    if (pair[0][0] in pair[1] and pair[0][-1] in pair[1]) or (pair[1][0] in pair[0] and pair[1][-1] in pair[0]):
        return True
    return False


def get_solution(input_lines: List[str]) -> int:

    counter = 0
    for line in input_lines:
        if line == '':
            continue
        pair = load_pair_from_line(line)
        if __check_pair(pair):
            counter += 1

    return counter
