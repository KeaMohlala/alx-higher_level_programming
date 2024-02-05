#!/usr/bin/python3
"""
Module to illustrate inheritance
"""


class MyList(list):
    """
    subclass
    """
    def print_sorted(self):
        """
        sorts the list into ascending order and prints it
        """
        print(sorted(self))
