"""Splitting a dictionary into two lists."""


__author__ = "730565738"


def get_keys(input_dict: dict[str, int]) -> list[str]: 
    """Inputs a dictionary, returns a list containing just the keys."""
    returns_list: list[str] = list()
    for key in input_dict:
        returns_list.append(key)
    return returns_list


def get_values(input_dict: dict[str, int]) -> list[int]:
    """Inputs a dictionary, returns a list containg just the values."""
    new_list: list[int] = list()
    for key in input_dict:
        new_list.append(input_dict[key])
    return new_list