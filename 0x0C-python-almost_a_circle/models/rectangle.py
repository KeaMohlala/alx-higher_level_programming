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

        Raises:
        Type Error: if width is not an integer
        Value Error: if width is less than or equal to zero
        """
        if value <= 0:
            raise ValueError("width must be > 0")
        if type(value) is not int:
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
        setter to set the height

        Args:
        value: height of the rectangle

        Raises:
        Type Error: if height is not an integer
        Value Error: if height is less than or equal to zero
        """
        if value <= 0:
            raise ValueError("height must be > 0")
        if type(value) is not int:
            raise TypeError("height must be an integer")
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

        Raises:
        Type Error: if x is not an integer
        Value Error: if x is less zero
        """
        if value < 0:
            raise ValueError("x must be >= 0")
        if type(value) is not int:
            raise TypeError("x must be an integer")
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

        Raises:
        Type Error: if y is not an integer
        Value Error: if y is less zero
        """
        if value < 0:
            raise ValueError("y must be >= 0")
        if type(value) is not int:
            raise TypeError("y must be an integer")
        self.__y = value

    def area(self):
        """
        function returns area of the rectangle object

        Returns:
        int: area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """
        prints to the stdout the rectangle with character #
        including the x and y position
        """
        if self.width == 0 or self.height == 0:
            print()
        else:
            print("\n" * self.__y, end="")
            for _ in range(self.__height):
                print(' ' * self.__x, end="")
                print('#' * self.__width)

    def __str__(self):
        """
        special method that provides string representation
        of the object/ instance

        Returns:
        returns string representation of the rectangle
        """
        return (
            f"[{self.__class__.__name__}] ({self.id}) "
            f"{self.x}/{self.y} - {self.width}/{self.height}"
        )
