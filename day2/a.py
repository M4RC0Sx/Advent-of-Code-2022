#
# AoC 2022
# M4RC0Sx - https://github.com/M4RC0Sx
#


from typing import List

from day2.common import HandShape, Result


STATS_OPPONENT = {
    'A': HandShape.ROCK,
    'B': HandShape.PAPER,
    'C': HandShape.SCISSORS,
}

STATS_MINE = {
    'X': HandShape.ROCK,
    'Y': HandShape.PAPER,
    'Z': HandShape.SCISSORS,
}


def __get_my__points(hand_shape_mine: HandShape, hand_shape_opponent: HandShape) -> int:
    if hand_shape_mine == hand_shape_opponent:
        return hand_shape_mine.value + Result.DRAW.value

    elif (hand_shape_mine == HandShape.ROCK and hand_shape_opponent == HandShape.SCISSORS) \
            or (hand_shape_mine == HandShape.PAPER and hand_shape_opponent == HandShape.ROCK) \
            or (hand_shape_mine == HandShape.SCISSORS and hand_shape_opponent == HandShape.PAPER):
        return hand_shape_mine.value + Result.WIN.value

    else:
        return hand_shape_mine.value + Result.LOSE.value


def __get_result(line: List[str]) -> int:
    if len(line) != 2:
        raise ValueError('Invalid line')

    opponent = STATS_OPPONENT[line[0]]
    mine = STATS_MINE[line[1]]

    return __get_my__points(mine, opponent)


def get_solution(input_lines: List[str]) -> int:

    points = 0
    for line in input_lines:
        if line == '':
            continue

        points += __get_result(line.split(' '))

    return points
