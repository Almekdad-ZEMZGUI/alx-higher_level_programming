#!/usr/bin/python3
"""
7-base_geometry module
with BaseGeometry class
"""


class BaseGeometry:
    """
    class with a Public instance methods
    area and integer_validator
    """
    def area(self):
        """
        raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

