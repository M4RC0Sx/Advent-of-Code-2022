#
# AoC 2022
# M4RC0Sx - https://github.com/M4RC0Sx
#


from typing import List
from enum import Enum


class HandShape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Result(Enum):
    WIN = 6
    LOSE = 0
    DRAW = 3


def read_input(path: str) -> List[str]:
    with open(path) as f:
        lines = f.read().splitlines()
    return lines
