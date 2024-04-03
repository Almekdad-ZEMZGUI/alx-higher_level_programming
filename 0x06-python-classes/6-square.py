#!/usr/bin/python3
""" First task """


class Square:
    """ Empty class defines a square """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square instance with a given size."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method to retrieve the size of the square."""
        return self.

    @property
    def position(self):
        """Getter method for position"""
        return self.__position

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """Setter method to set the position"""
        if not isinstance(value, tuple) or \
                type(value[0]) is not int or type(value[1]) is not int or \
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ returns the current square area """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with '#'"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
