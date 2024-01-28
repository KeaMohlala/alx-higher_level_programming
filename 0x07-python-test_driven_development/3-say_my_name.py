#!/usr/bin/python3
"""
This module has one function that prints the full name
the arguments should only be strings
"""


def say_my_name(first_name, last_name=""):
    """
    function that prints the full name of a person

    Args:
    first_name: required argument, is the first name of the person
    last_name: optional argument. if not provided it will
    default to an empty string

    Raises:
    TypeError: if both arguments are a not a string

    Return:
    Printed statement with the full name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
