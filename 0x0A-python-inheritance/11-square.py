#!/usr/bin/python3
"""
11-square module
with a class Square that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    a class Square that inherits from Rectangle
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        prints [Rectangle] <width>/<height>
        """
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__size, self.__size)
