#
# AoC 2022
# M4RC0Sx - https://github.com/M4RC0Sx
#


from day7 import a, b, common


def main():

    lines = common.read_input('day7/input.txt')

    a_solution = a.get_solution(lines)
    print('Puzzle A solution:')
    print(f'\t-> Total size: {a_solution}')
    print()
    print('Puzzle B solution:')
    b_solution = b.get_solution(lines)
    print(f'\t-> Min size: {b_solution}')


if __name__ == '__main__':
    main()
