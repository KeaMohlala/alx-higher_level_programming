#!/usr/bin/python3
"""
A module with a function that writes an object to a textfile
using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an object to a text file
    using JSON representation

    Args:
     my_obj: python data structure
     filename: name of text file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
