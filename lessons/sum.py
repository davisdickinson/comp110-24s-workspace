"""Summing the elements of a list using different loops."""


__author__ = "730565738"


def w_sum(vals: list[float]) -> float:
    """Takes in a list of floats, returns sum of all elements using while loop."""
    sum: float = 0.0
    index = 0
    while index < len(vals):
        sum += vals[index]
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Takes in list of floats, returns the sum of all elements using for loop."""
    sum: float = 0
    for item in vals:
        sum += item
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Takes in list of floats, returns the sum of all elements using a range for loop."""
    sum: float = 0
    for index in range(len(vals)):
        sum += vals[index]
    return sum