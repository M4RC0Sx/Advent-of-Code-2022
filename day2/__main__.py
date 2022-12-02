#
# AoC 2022
# M4RC0Sx - https://github.com/M4RC0Sx
#


from day2 import a, b, common


def main():

    input_lines = common.read_input('day2/input.txt')

    a_solution = a.get_solution(input_lines)
    print('Puzzle A solution:')
    print(f'\t-> Game finished with {a_solution} points')
    print()
