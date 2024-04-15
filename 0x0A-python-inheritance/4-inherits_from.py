#!/usr/bin/python3
"""
4-inherits_from module
with a function inherits_from
that checks  if the object is an instance of a class that
inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    checks  if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class
    :param obj: object to check
    :param a_class: the specified class
    :return: True if the object is an instance of a class that inherited
            (directly or indirectly) from the specified class ; otherwise False
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
