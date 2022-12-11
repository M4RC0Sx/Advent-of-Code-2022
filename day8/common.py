#
# AoC 2022
# M4RC0Sx - https://github.com/M4RC0Sx
#


from typing import List


def read_input(path: str) -> List[str]:
    with open(path) as f:
        lines = f.read().splitlines()
    return lines
