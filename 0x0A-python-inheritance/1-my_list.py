#!/usr/bin/python3
"""
Module with a class inherited
from a 'list' class
"""


class MyList(list):
    """
    subclass that inherits the list
    """

    def print_sorted(self):
        """
        prints list in ascending order
        """
        print(sorted(self))
