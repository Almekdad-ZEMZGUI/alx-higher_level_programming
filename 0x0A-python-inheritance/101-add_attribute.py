#!/usr/bin/python3
"""
101-add_attribute module
with a function add_attribute
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it’s possible
    """
    if ('__dict__' in dir(obj)):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
