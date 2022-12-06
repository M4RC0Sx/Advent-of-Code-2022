#
# AoC 2022
# M4RC0Sx - https://github.com/M4RC0Sx
#


def read_input(path: str) -> str:
    with open(path) as f:
        lines = f.read().splitlines()
    return lines[0]


def parse_signal(signal: str, len_: int) -> int:
    for i in range(len_, len(signal)):
        if len(set(signal[i - len_:i])) == len_:
            return i
