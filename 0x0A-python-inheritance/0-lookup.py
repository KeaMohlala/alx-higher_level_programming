#!/usr/bin/python3
"""
module with a function that returns lists
of attributes and methods
"""


def lookup(obj):
    """
    function that returns available methods
    and attributes of an object

    Args: the object

    Return: list of attributes and methods
    """
    return dir(obj)
