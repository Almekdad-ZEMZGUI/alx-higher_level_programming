#!/usr/bin/python3
"""
3-say_my_name module
with a function say_my_name
that that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    prints this format My name is <first name> <last name>
    :param first_name: first name input
    :param last_name: last name input
    :return: nothing
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
