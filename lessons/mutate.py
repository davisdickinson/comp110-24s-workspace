"""Mutating functions."""


__author__ = "730565738"


def manual_append(mylist: list[int], add: int) -> None: 
    """Appends a variable to the list."""
    mylist.append(add) 
    return None


def double(mylist: list[int]) -> None:
    """Doubles the value of all items in the list."""
    item = 0
    while item < len(mylist):
        mylist[item] *= 2
        item += 1
    return None