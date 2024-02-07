#!/usr/bin/python3
"""
module with a function thats writes a string
into text file and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file and
    returns the number of characters written

    The function should create the file if it doesn't exist
    The function should overwrite the content of the file
    if the file exists
    The function doesn't need to manage file permissions

    Args:
     filename: name of the file to write to
     text: string to write to the text file

    Return:
     number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
