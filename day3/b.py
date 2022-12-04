#
# AoC 2022
# M4RC0Sx - https://github.com/M4RC0Sx
#


from typing import Dict, List


def __get_common_items_in_group(group: List[List[chr]]) -> List[chr]:
    return set(group[0]) & set(group[1]) & set(group[2])


def get_solution(input_lines: List[str], priorities: Dict[chr, int]) -> int:

    counter = 0
    current_group = []
    for i, line in enumerate(input_lines, start=1):
        if line == '':
            continue

        current_group.append(list(line))

        if i % 3 == 0:
            counter += sum([priorities[item] for item in __get_common_items_in_group(current_group)])
            current_group = []

    return counter
