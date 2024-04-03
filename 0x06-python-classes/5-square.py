#!/usr/bin/python3
""" First task """


class Square:
    """ Empty class defines a square """
    def __init__(self, size=0):
        """Initializes a Square instance with a given size."""
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ returns the current square area """
        return self.__size ** 2

    def my_print(self):
        """ prints in stdout the square with the character #"""
        for i in range(self.size):
            print("#" * self.size)
        if self.size == 0:
            print()
