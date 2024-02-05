#!/usr/bin/python3
"""
module to check if an object is an exact instance
of a class
"""


def is_same_class(obj, a_class):
    """
    checks if an object is the exact instance of a class

    Args:
    obj: the instance
    a_class: the class to chcek if 'obj' is an instance of

    Return:
    True if 'obj' is an instance of 'a_class'
    """

    if (isinstance(obj, a_class)) and (obj.__class__ == a_class):
        return True
