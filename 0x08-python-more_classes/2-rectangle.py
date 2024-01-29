#!/usr/bin/python3
"""
Class that defines a rectangle
"""


class Rectangle:
    """
    creation of class Rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Inititializes the instance with an optional
        height and width attribute

        Args:
        width: width of the rectangle
        heigth: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        getter property to retrieve the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter to set the width

        Args:
          value: width of the rectangle

        Raises:
          TypeError: if width is not an integer
          ValueError: if width is less than zero
        """
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """
        getter property to retrieve the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter to set the height attribute

        Args:
          value: height of the rectangle

        Raises:
          TypeError: if value is not an integer
          ValueError: if value is less than zero
        """
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value

    def area(self):
        """
        returns the area of the rectangle

        Returns:
        int: are of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        returns the perimeter of the rectangle
        if the height or width are 0, the perimeter will be 0

        Returns:
        perimeter of the rectangle
        """
        p = 2 * (self.width + self.height)
        if self.width == 0 or self.height == 0:
            p = 0
        return p
