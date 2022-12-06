#
# AoC 2022
# M4RC0Sx - https://github.com/M4RC0Sx
#


from day5 import a, b, common


def main():

    stacks, instructions = common.read_input('day5/input.txt')

    a_solution = a.get_solution(stacks, instructions)
    print('Puzzle A solution:')
    print(f'\t-> Crates on top: {a_solution} ({"".join(str(i) for i in a_solution)})')
    print()
    print('Puzzle B solution:')
    b_solution = b.get_solution(stacks, instructions)
    print(f'\t-> Crates on top: {b_solution} ({"".join(str(i) for i in b_solution)})')


if __name__ == '__main__':
    main()
