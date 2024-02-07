#!/usr/bin/python3
"""
module with a function to serialize an object of a class
that contains simple data structures as attributes
"""


def class_to_json(obj):
    """
    function returns dictionary for JSON
    serialization of an object

    Args:
     instance of a class
    Return:
     dictionary to store serializable attributes
    """
    data = {}

    for attr, value in vars(obj).items():
        if isinstance(value, (list, dict, str, int, bool)):
            data[attr] = value
    return data
