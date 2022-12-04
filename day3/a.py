#
# AoC 2022
# M4RC0Sx - https://github.com/M4RC0Sx
#


from typing import Dict, List

from day3.common import get_rucksack_items, get_common_items


def get_solution(input_lines: List[str], priorities: Dict[chr, int]) -> int:

    counter = 0
    for line in input_lines:
        if line == '':
            continue

        rucksack_items = get_rucksack_items(line)
        common_items = get_common_items(rucksack_items[0], rucksack_items[1])
        counter += sum([priorities[item] for item in common_items])

    return counter
