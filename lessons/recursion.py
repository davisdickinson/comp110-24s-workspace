"""CQ07 - REcursions."""


def f(n: int, k: int) -> int: 
    """Defines function using base case and recursive rule."""
    if n == 0:   # base case
        return 0
    else:   # recursive rule
        return f(n - 1, k) + k
    