#!/usr/bin/python3
"""
A module with a function that creates an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    function that creates an object from a JSON file

    Args:
     filename: name of JSON file
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
