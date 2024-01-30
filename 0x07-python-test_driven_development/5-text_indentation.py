#!/usr/bin/python3
"""
This module can split a string using multiple
delimeters without importing another module
"""


def text_indentation(text):
    """
    function prints string with 2 new lines
    after each '.', '?', ':' character.

    The function also removes any trailing white
    spaces and leading spaces for each line printed

    Args:
     text: string to be split and printed

    Raises:
     TypeError: if text is not a string
     """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')

    lines = text.split('\n')
    lines = [line.strip() for line in lines]
    joined_lines = lines[0:len(lines)]

    print('\n'.join(joined_lines[0:-1]))
    print(joined_lines[-1], end="")
