#!/usr/bin/python3
"""
4-print_square module
with a function print_square
that prints a square with the character #.
"""


def print_square(size):
    """
    prints a square with the character #
    :param size: the size length of the square
    :return: nothing
    """
    if not isinstance(size, int) or (isinstance(size, float)
                                     and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print("", end="")
    else:
        result = "\n".join(["#" * size for _ in range(size)])
        print(result)
