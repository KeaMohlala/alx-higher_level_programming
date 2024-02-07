#!/usr/bin/python3
"""
A module with a function deserializes a JSON string
"""
import json


def from_json_string(my_str):
    """
    function returns an object (Python data structure)
    represented JSON string

    Args:
     my_str: data structure

    Return:
    an object
    """
    data = json.loads(my_str)
    return data
