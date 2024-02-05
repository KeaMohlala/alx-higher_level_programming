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
