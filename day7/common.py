#
# AoC 2022
# M4RC0Sx - https://github.com/M4RC0Sx
#


from typing import Dict, List
import re
from itertools import accumulate


def read_input(path: str) -> str:
    with open(path) as f:
        lines = f.read().splitlines()
    return lines


def get_sizes(lines: List[str]) -> Dict[str, int]:
    path_stack = []
    sizes = {}
    for line in lines:
        re_cd_match = re.match(r"\$ cd (.+)", line)
        re_size_match = re.match(r"(\d+) (?:.+)", line)
        if re_cd_match:
            dir_name = re_cd_match.group(1)
            match dir_name:
                case "/":
                    path_stack = ["/"]
                case "..":
                    path_stack.pop()
                case d:
                    path_stack.append(f"{d}/")
        elif re_size_match:
            size = int(re_size_match.group(1))
            for p in accumulate(path_stack):
                sizes[p] = sizes.get(p, 0) + size

    return sizes
