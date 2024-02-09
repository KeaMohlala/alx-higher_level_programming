#!/usr/bin/python3
"""
module that defines base module from
which all the other class will inherit
"""


class Base:
    """
    documentation for class 'Base'
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        every instance will be initialized with and id
        if id argument is not specified the private attribute
        'nb objects' will be incremented and a new value assigned

        Args:
         id: int value assigned to each instance
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
