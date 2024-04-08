#!/usr/bin/python3
"""
1-rectangle module
With a class represents a rectangle
"""


class Rectangle:
    """
    This class represents a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(self, width=0, height=0): Initializes a new Rectangle instance with the specified width and height.
        width(self): Getter method to retrieve the width of the rectangle.
        height(self): Getter method to retrieve the height of the rectangle.
        width(self, value): Setter method to set the width of the rectangle.
        height(self, value): Setter method to set the height of the rectangle.

    Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height is less than 0.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance with the specified width and height
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter method to retrieve the width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """
        Getter method to retrieve the height of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method to set the width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Setter method to set the height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
