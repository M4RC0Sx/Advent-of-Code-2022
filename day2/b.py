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
    'X': Result.LOSE,
    'Y': Result.DRAW,
    'Z': Result.WIN,
}


def __get_my__points(result_mine: HandShape, hand_shape_opponent: HandShape) -> int:
    if result_mine == Result.DRAW:
        return hand_shape_opponent.value + result_mine.value

    elif result_mine == Result.WIN:
        if hand_shape_opponent == HandShape.ROCK:
            return HandShape.PAPER.value + result_mine.value
        elif hand_shape_opponent == HandShape.PAPER:
            return HandShape.SCISSORS.value + result_mine.value
        else:
            return HandShape.ROCK.value + result_mine.value

    else:
        if hand_shape_opponent == HandShape.ROCK:
            return HandShape.SCISSORS.value + result_mine.value
        elif hand_shape_opponent == HandShape.PAPER:
            return HandShape.ROCK.value + result_mine.value
        else:
            return HandShape.PAPER.value + result_mine.value


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
