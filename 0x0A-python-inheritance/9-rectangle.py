#!/usr/bin/python3
"""
9-rectangle module
with Rectangle class that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits from BaseGeometry class
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        implement area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        prints [Rectangle] <width>/<height>
        """
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__width, self.__height)
