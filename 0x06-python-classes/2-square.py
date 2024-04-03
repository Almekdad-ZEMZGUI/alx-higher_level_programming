#!/usr/bin/python3
""" First task """


class Square:
    """ Empty class defines a square """
    def __init__(self, size=0):
        """The size of a square is crucial for a square,
        many things depend of it (area computation, etc.)"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
