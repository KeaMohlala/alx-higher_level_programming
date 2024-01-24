#!/usr/bin/python3
"""
Class that defines a square
"""


class Square:
    """
    Documentation for square class
    """
    def __init__(self, size=0):
        """
        Documentation for initilization of instance
        it instantiates a Square object with an optional size

        Args:
          size: size of the square

        Raises:
          TypeError: If size is not an integer
          ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        method that returns are of square based on size

        Returns:
          int: The area of the square
        """
        return self.__size ** 2
