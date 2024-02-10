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
