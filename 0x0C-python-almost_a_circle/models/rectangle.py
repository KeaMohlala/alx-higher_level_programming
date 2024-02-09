#!/usr/bin/python3
"""
Module that defines a Rectangle class
"""


class Rectangle(Base):
    """
    creation of Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialization of Rectangle instance with width, height
        x, y and id attributes

        Args:
        width: width of the rectangle
        height: height of the rectangle
        x: position of the tectangle
        y: position of the rectangle
        id: id of the instance
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        getter property to retrieve width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter to set the width

        Args:
        value: width of the rectangle
        """
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
        setter to set the height

        Args:
        value: height of the rectangle
        """
        self.__height = value

    @property
    def x(self):
        """
        getter property to retrieve the x position
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter to set the x position of the rectangle

        Args:
        value: x position of the rectangle
        """
        self.__x = value

    @property
    def y(self):
        """
        getter property to retrieve the y position
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter to set the y position of the rectangle

        Args:
        value: y position of the rectangle
        """
        self.__y = value
