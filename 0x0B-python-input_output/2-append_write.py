#!/usr/bin/python3
"""
module with a function thats appends a string
into text file and returns the number of characters written
"""


def append_write(filename="", text=""):
    """
    function that appends a string to a text file and
    returns the number of characters written

    The function should create the file if it doesn't exist
    The function doesn't need to manage file permissions

    Args:
     filename: name of the file to write to
     text: string to write to the text file

    Return:
     number of characters written
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
