from typing import Dict


def str_to_index_dict(string: str) -> Dict[str, int]:
    dictionary = dict()
    for i, char in enumerate(string):
        dictionary[char] = i
    return dictionary