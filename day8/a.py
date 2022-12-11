#
# AoC 2022
# M4RC0Sx - https://github.com/M4RC0Sx
#


from typing import List


def get_solution(lines: List[str]) -> int:

    visibles = 0

    for index_line, line in enumerate(lines, start=0):
        for index_char, char in enumerate(line, start=0):
            # Top and bottom edges
            if (index_line == 0) or (index_line == len(lines) - 1):
                visibles += 1
                continue

            # Left and right edges
            if index_char == 0 or index_char == len(line) - 1:
                visibles += 1
                continue

            height = int(char)
            visible_left = all(int(c) < height for c in line[:index_char])
            visible_right = all(int(c) < height for c in line[index_char + 1:])
            visible_top = all(int(c[index_char]) < height for c in lines[:index_line])
            visible_bottom = all(int(c[index_char]) < height for c in lines[index_line + 1:])

            if any([visible_left, visible_right, visible_top, visible_bottom]):
                visibles += 1

    return visibles
