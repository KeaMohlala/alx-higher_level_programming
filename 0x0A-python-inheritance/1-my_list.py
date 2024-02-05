#!/usr/bin/python3
"""
Module to illustrate inheritance
"""


class list:
    """
    Parent class
    """
    def __init__(self):
        """
        instantiates instances of the class with two
        empty lists
        """
        self.list = []
        self.new_list = []

    def append(self, item):
        """
        appends new item to empty list

        Args: item

        Return: appended list
        """
        self.list.append(item)

    def print_sorted(self):
        """
        copies list to a new lists and sorts it
        into ascending order. new list is printed
        """
        self.new_list.extend(self.list)
        self.new_list.sort()
        print(self.new_list)

    def __str__(self):
        """
        prints object as a string
        """
        return str(self.list)


class MyList(list):
    """
    subclass
    """
    pass
