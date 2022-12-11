#
# AoC 2022
# M4RC0Sx - https://github.com/M4RC0Sx
#


from day8 import a, b, common


def main():

    lines = common.read_input('day8/input.txt')

    a_solution = a.get_solution(lines)
    print('Puzzle A solution:')
    print(f'\t-> Visible trees: {a_solution}')
    print()
    print('Puzzle B solution:')
    b_solution = b.get_solution(lines)
    print(f'\t-> Highest score: {b_solution}')


if __name__ == '__main__':
    main()
