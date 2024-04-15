#!/usr/bin/python3
"""
100-my_int module
with a class MyInt that inherits from int
"""


class MyInt(int):
    """
    a class MyInt that inherits from int
    """
    def __init__(self, num):
        self.num = num

    def __eq__(self, other):
        return self.num != other

    def __ne__(self, other):
        return self.num == other
