#!/usr/bin/python3
"""
module with a function that reads a file
"""


def read_file(filename=""):
    """
    funtion that reads a text file with utf8 encoding
    and prints it to stdout

    The function automatically closes the file at the end
    The function is not expected to manage file permission or
    file doesn't exist exceptions

    Args:
     filename: the mane of the file to read and print
    """
    with open(filename, mode="r", encoding="UTF8") as f:
        print(f.read())
