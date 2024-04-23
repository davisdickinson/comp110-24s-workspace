"""Functions that implement sorting algorithms."""

__author__ = "730565738"

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    sorted_index: int = 0
    for i in range(0, len(x) -1):
        unsorted_index: int = sorted_index + 1
        while unsorted_index > 0 and x[unsorted_index] < x[unsorted_index-1]:
            swapvalue = x[unsorted_index-1]
            x[unsorted_index-1] = x[unsorted_index]
            x[unsorted_index] = swapvalue
            unsorted_index -= 1
        # x.insert(current, x[unsorted_index])
        sorted_index +=1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    for counter in range(0, len(x)):
        minval: int = x[counter]
        minindex: int = counter
        for j in range(counter, len(x)):
            if x[j] < minval:
                minval = x[j]
                minindex = j
        swapvalue: int = x[counter]
        x[counter] = minval
        x[minindex] = swapvalue
    return None