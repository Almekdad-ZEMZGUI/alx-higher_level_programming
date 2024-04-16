#!/usr/bin/python3
"""
11-student module
with a Class Student
"""


class Student:
    """
    Defines a student by:
    Public Attributes:
        first_name
        last_name
        age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation
        of a Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            d = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    d[att] = self.__dict__[att]
            return d

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        """
        for k, v in json.items():
            setattr(self, k, v)
