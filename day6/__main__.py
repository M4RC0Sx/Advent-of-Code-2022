#
# AoC 2022
# M4RC0Sx - https://github.com/M4RC0Sx
#


from day6 import a, b, common


def main():

    signal = common.read_input('day6/input.txt')
    print(signal)

    a_solution = a.get_solution(signal)
    print('Puzzle A solution:')
    print(f'\t-> Characters until a marker: {a_solution}')
    print()
    print('Puzzle B solution:')
    b_solution = b.get_solution(signal)
    print(f'\t-> Characters until a marker: {b_solution}')


if __name__ == '__main__':
    main()
