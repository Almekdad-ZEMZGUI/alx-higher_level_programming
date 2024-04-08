#!/usr/bin/python3
"""
3-rectangle module
With a class represents a rectangle
"""


class Rectangle:
    """
    This class represents a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(self, width=0, height=0): Initializes a Rectangle instance.
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
        Initializes new Rectangle instance with specified width and height
        """
        self.width = width
        self.height = height

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
        return self.__height

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

    def area(self):
        """
        Calculates the rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculates the rectangle perimeter
        if width or height is equal to 0, perimeter is equal to 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    def __str__(self):
        """
        print the rectangle with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        result = "\n".join(["#" * self.__width for _ in range(self.__height)])
        return result
