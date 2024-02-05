#!/usr/bin/python3
"""
module to check if an object is an instance
of a class
"""


def is_kind_of_class(obj, a_class):
    """
    checks if an object is the exact instance of a class

    Args:
    obj: the instance
    a_class: the class to chcek if 'obj' is an instance of

    Return:
    True if 'obj' is an instance of 'a_class'
    or if 'obj' is an instance of the an inherited class
    """

    return (isinstance(obj, a_class)) or type(obj) is a_class
