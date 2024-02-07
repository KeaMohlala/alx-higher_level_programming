#!/usr/bin/python3
import json
"""
A module with a function serializes an object
"""


def to_json_string(my_obj):
    """
    function returns JSON representation
    of a string

    Args:
     my_obj: data structure to convert into a JSON string

    Return:
    JSON representation of 'my_obj'
    """
    json_string = json.dumps(my_obj)
    return json_string
