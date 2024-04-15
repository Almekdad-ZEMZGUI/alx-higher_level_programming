#!/usr/bin/python3
"""
3-is_kind_of_class module
with a function is_kind_of_class
if the object is an instance of, or if the object is
an instance of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class
    :param obj: object to check
    :param a_class: the specified class
    :return: True if the object is an instance of the specified class
            or False otherwise
    """
    return isinstance(obj, a_class)
