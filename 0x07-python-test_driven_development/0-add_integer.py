#!/usr/bin/python
"""
this module defines a function that adds 2 integers
the parameters of the function must be integers or
floats or a TypeError is raised
"""


def add_integer(a, b=98):
    """
    function adds two integers.
    If the argument is a float it will be typecased top int

    Args:
    a: first argument
    b: second argument. If none is added 98 is the default number used

    Raises:
    TypeError: if a or b is not an integer or float

    Return:
    the addition of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
