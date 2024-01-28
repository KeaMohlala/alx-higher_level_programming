#!/usr/bin/python3
"""
This module has one function that prints a square
"""


def print_square(size):
    """
    function that prints a square of #s

    Args:
    size: side length of the square(int or float)

    Raises:
    TypeError: if size is not an integer
    ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print('#' * size)
