#
# AoC 2022
# M4RC0Sx - https://github.com/M4RC0Sx
#


from typing import List, Tuple

from day4.common import load_pair_from_line


def __check_pair_overlap(pair: Tuple[Tuple[int, ...]]) -> bool:
    intersection = set(pair[0]).intersection(set(pair[1]))
    return any(intersection)


def get_solution(input_lines: List[str]) -> int:

    counter = 0
    for line in input_lines:
        if line == '':
            continue
        pair = load_pair_from_line(line)
        if __check_pair_overlap(pair):
            counter += 1

    return counter
