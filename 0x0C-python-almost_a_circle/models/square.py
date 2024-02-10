#!/usr/bin/python3
"""
module for square class with Rectangle as
the superclass
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    describes Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        class constructor calls superclass
        all attributes are from the 'Rectangle' class

        Args:
        size: size of the square
        x: x position of the square
        y: y position of the square
        id: id of created instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        returns string representation of the square
        """
        return (
            f"[{self.__class__.__name__}] ({self.id}) "
            f"{self.x}/{self.y} - {self.width}"
        )

    @property
    def size(self):
        """
        getter property to receive size of square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        sets the size of the square
        width and height are assigned the same value

        Args:
        value: int, value to assign to the size (width and
        height) of the square

        Raises:
        Type Error: if value is not an integer
        Value Error: if value is less than or equal to zero
        """
        if value <= 0:
            raise ValueError("width must be > 0")
        if type(value) is not int:
            raise TypeError("width must be an integer")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        method accepts kwargs(key word arguments) and
        args to update the instance attributes

        if args is provided and not empty, kwargs should be ignored

        Args:
        args: no key word arguments
        kwargs: key word arguments
        """
        if args:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id, self.width = args
            elif len(args) == 3:
                self.id, self.width, self.x = args
            else:
                self.id, self.width, self.x, self.y = args
        else:
            for attr, value in kwargs.items():
                if hasattr(self, attr):
                    setattr(self, attr, value)
