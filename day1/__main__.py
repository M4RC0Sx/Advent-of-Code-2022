#
# AoC 2022
# M4RC0Sx - https://github.com/M4RC0Sx
#


from day1 import a, b, common


def main():

    input_lines = common.read_input('day1/input.txt')

    a_solution = a.get_solution(input_lines)
    print('Puzzle A solution:')
    print(f'\t-> Elf {a_solution[0]} has the most food with {a_solution[1]}')
