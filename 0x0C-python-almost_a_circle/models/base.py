#!/usr/bin/python3
"""
base module
This class will be the “base” of all other classes
in this project. The goal of it is to manage id attribute
in all your future classes and to avoid duplicating the same code
"""


class Base:
    """
    Class Base:
    private class attribute __nb_objects = 0
    class constructor: def __init__(self, id=None):
    - if id is not None, assign the public instance attribute id with this argument value
    you can assume id is an integer and you don’t need to test the type of it
    - otherwise, increment __nb_objects and assign the new value to the public instance attribute id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
