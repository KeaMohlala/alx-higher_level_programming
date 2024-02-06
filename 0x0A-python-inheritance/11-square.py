#!/usr/bin/python3
"""
module for Geometry class
"""


class BaseGeometry:
    """
    creation of class 'BaseGeometry'
    """
    def area(self):
        """
        method to implement the area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates the 'value'

        Args:
         name: is a string associated with value
         value: integer to calculate the 'area'

        Raises:
         TypeError: if 'value' is not an integer
         ValueError: of 'value' is less than or equal to 0
         """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    subclass of 'BaseGeometry'
    """
    def __init__(self, width, height):
        """
        instantiation of Rectangle object with
        'width' and 'height' private attributes


        Args:
         width: width of the rectangle
         height: height of the rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        returns area of the rectangle
        using private width and height attributes
        """
        return self.__width * self.__height

    def __str__(self):
        """
        returns object as a string
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """
    subclass of 'Rectangle'
    """
    def __init__(self, size):
        """
        instantiation of Square object with
        'size' private attribute


        Args:
         size: size of the aquare
        """

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        returns area of the square
        using size attributes
        """
        return self.__size * self.__size

    def __str__(self):
        """
        returns object as a string
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
