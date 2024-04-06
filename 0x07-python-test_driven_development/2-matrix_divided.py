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
    catsh = len(matrix[0]) # raises a TypeError if elements of matrix are not the same size
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != catsh:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_mat = [[round(num / div, 2) for num in row] for row in matrix]
    return result_mat
