#!/usr/bin/python3
"""
module to check if an object is an instance of a class that is a
subclass of the specified class
"""


def inherits_from(obj, a_class):
    """
    checks if an object is an instance of a class that is a
    subclass of 'a_class'

    Args:
    obj: the instance
    a_class: the parent class to check

    Return:
    True if 'obj' is an instance of a class that
    is a subclass of the specified class
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
