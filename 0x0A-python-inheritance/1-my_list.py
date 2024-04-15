#!/usr/bin/python3
"""
1-my_list.py module
with a class MyList that inherits from list
containing Public instance method: def print_sorted(self):
that prints the list, but sorted (ascending sort)
"""


class MyList(list):
    """
    a class MyList that inherits from list
    """
    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
