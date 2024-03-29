#!/usr/bin/python3
"""
Module that defines a Rectangle class
"""
from models.base import Base


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
        x: position of the rectangle
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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
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

    def update(self, *args, **kwargs):
        """
        method accepts kwargs(key word arguments) and
        args to update the instance attributes

        if args is provided and not empty, kwargs should be ignored
        """
        if args:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id, self.width = args
            elif len(args) == 3:
                self.id, self.width, self.height = args
            elif len(args) == 4:
                self.id, self.width, self.height, self.x = args
            else:
                self.id, self.width, self.height, self.x, self.y = args
        else:
            for attr, value in kwargs.items():
                if hasattr(self, attr):
                    setattr(self, attr, value)

    def to_dictionary(self):
        """
        returns a dictionary representation of a rectangle instance
        """
        return {"width": self.width, "height": self.height, "x": self.x,
                "y": self.y, "id": self.id}
