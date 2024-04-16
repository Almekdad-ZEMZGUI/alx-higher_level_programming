#!/usr/bin/python3
"""
12-pascal_triangle module
with a function pascal_triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    tri = [[1]]
    for rows in range(n-1):
        tri.append([a+b for a, b in zip([0] + tri[-1], tri[-1] + [0])])
    return tri
