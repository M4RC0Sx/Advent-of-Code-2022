#
# AoC 2022
# M4RC0Sx - https://github.com/M4RC0Sx
#


from typing import List


def get_solution(lines: List[str]) -> int:

    scores = []

    for index_line, line in enumerate(lines, start=0):
        for index_char, char in enumerate(line, start=0):
            # Top and bottom edges
            if (index_line == 0) or (index_line == len(lines) - 1):
                scores.append(0)
                continue

            # Left and right edges
            if index_char == 0 or index_char == len(line) - 1:
                scores.append(0)
                continue

            score = 1
            for x, y in ((0, -1), (0, 1), (1, 0), (-1, 0)):
                row, col, score_counter = index_line + x, index_char + y, 0

                while 0 <= row < len(lines) and 0 <= col < len(lines[0]):
                    score_counter += 1
                    if int(char) <= int(lines[row][col]):
                        break
                    row += x
                    col += y

                score *= score_counter
            scores.append(score)

    return max(scores)
