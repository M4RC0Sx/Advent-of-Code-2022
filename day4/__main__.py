#
# AoC 2022
# M4RC0Sx - https://github.com/M4RC0Sx
#


from day4 import a, b, common


def main():

    input_lines = common.read_input('day4/input.txt')

    a_solution = a.get_solution(input_lines)
    print('Puzzle A solution:')
    print(f'\t-> Pairs in one range fully contains each: {a_solution}')
    print()
    print('Puzzle B solution:')
    b_solution = b.get_solution(input_lines)
    print(f'\t-> Pairs that overlap: {b_solution}')


if __name__ == '__main__':
    main()
