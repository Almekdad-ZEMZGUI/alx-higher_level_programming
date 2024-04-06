#!/usr/bin/python3
"""
0-add_integer module
with a function add_integer
that returns the sum of two integers
"""


def add_integer(a, b=98):
    """
    cast a, b to integers if they are float and return sum of them
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
