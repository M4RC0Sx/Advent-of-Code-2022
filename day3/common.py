#
# AoC 2022
# M4RC0Sx - https://github.com/M4RC0Sx
#


from typing import Dict, List, Tuple
import string


def read_input(path: str) -> List[str]:
    with open(path) as f:
        lines = f.read().splitlines()
    return lines


def load_priorities() -> Dict[chr, int]:

    priorities = {}
    for char in string.ascii_lowercase:
        priorities[char] = ord(char) - 96

    for char in string.ascii_uppercase:
        priorities[char] = ord(char) - 38

    return priorities


def get_rucksack_items(rucksack_str: str) -> Tuple[List[str], List[str]]:
    return list(rucksack_str[:len(rucksack_str) // 2]), list(rucksack_str[len(rucksack_str) // 2:])


def get_common_items(compartment_a, compartment_b) -> List[str]:
    return list(set(compartment_a) & set(compartment_b))
