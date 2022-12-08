#
# AoC 2022
# M4RC0Sx - https://github.com/M4RC0Sx
#


from typing import List

from day7.common import get_sizes


def get_solution(lines: List[str]) -> int:
    sizes = get_sizes(lines)
    return sum(s for s in sizes.values() if s <= 100000)
