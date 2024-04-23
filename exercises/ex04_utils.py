"""list Utility Functions."""

__Author__ = "730565738"


def all(my_list: list[int], my_int: int) -> bool:
    """Given a list of ints and an int, all should return a bool indicating whether or not all the ints in the list are the same as the given int."""
    if len(my_list) == 0: 
        return False
    for i in range(len(my_list)):
        if my_list[i] != my_int: 
            return False
    return True


def max(my_list: list[int]) -> int:
    """The max function is given a list of ints, max should return the largest in the List."""
    if len(my_list) == 0:
        raise ValueError("max() arg is an empty List")
    limit: int = my_list[0]
    for i in range(len(my_list)):
        if limit <= my_list[i]:
            limit = my_list[i]
    return limit 


def is_equal(my_list: list[int], my_list2: list[int]) -> bool:
    """Function checks if the lists are the same."""
    if len(my_list) != len(my_list2):
        return False
    for i in range(len(my_list)):
        if my_list[i] != my_list2[i]:
            return False
    return True


def extend(my_list: list[int], my_list2: list[int]) -> None:
    """Given two lists of int values, mutate the first list of int values by appending the second lists values to the end of it."""
    for i in range(len(my_list2)):
        my_list.append(my_list2[i])