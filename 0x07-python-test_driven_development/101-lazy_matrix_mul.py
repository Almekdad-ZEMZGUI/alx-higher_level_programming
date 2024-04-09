#!/usr/bin/python3
"""
101-lazy_matrix_mul module
with lazy_matrix_mul function
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    multiplies 2 matrices by using the module NumPy
    """
    return numpy.matmul(m_a, m_b)
