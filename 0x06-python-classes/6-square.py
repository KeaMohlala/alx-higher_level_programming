#!/usr/bin/python3
"""
Class that defines a square
"""


class Square:
    """
    Documentation for square class
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Documentation for initilization of instance
        it instantiates a Square object with an optional size

        Args:
          size: size of the square
          position: position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        getter property to retrieve size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter to set the size attribute

        Args:
          value: size of the square

        Raises:
          TypeError: if size is not an integer
          ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        getter property to retrieve position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter to set the position attribute

        Args:
          value: position of the square as a tuple. position[0] is horizontal
          and position[1] is the vertical position

        Raises:
          TypeError: if position is not tuple with two integers
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        method that returns area of square based on size

        Returns:
          int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints in stdout the square with the character # including the position
        """
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
