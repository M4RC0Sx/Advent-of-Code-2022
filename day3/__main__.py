#
# AoC 2022
# M4RC0Sx - https://github.com/M4RC0Sx
#


from day3 import a, b, common


def main():

    input_lines = common.read_input('day3/input.txt')
    char_priorities = common.load_priorities()

    a_solution = a.get_solution(input_lines, char_priorities)
    print('Puzzle A solution:')
    print(f'\t-> Common items priority sum: {a_solution}')
    print()
    print('Puzzle B solution:')
    b_solution = b.get_solution(input_lines, char_priorities)
    print(f'\t-> Group items priority sum: {b_solution}')


if __name__ == '__main__':
    main()
