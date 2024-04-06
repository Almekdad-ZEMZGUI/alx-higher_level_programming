#!/usr/bin/python3
"""
2-matrix_divided module
with a function matrix_divided
that takes a matrix and a number div returns a new matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    :param matrix: the matrix input
    :param div: the number to divide the matrix elements with
    :return: a new matrix
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) \
            or not all(isinstance(num, (int, float)) for row in matrix for num in row) or \
            len(matrix) == 0 or not isinstance(matrix[0], list) or len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(matrix[0]) == len(row) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    result_mat = [[round(num / div, 2) for num in row] for row in matrix]
    return result_mat

