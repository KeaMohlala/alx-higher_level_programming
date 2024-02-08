#!/usr/bin/python3
"""
module for class Student
"""


class Student:
    """
    creation of 'Student' class
    """
    def __init__(self, first_name, last_name, age):
        """
        instantiates the Student instance with
        first name, last name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrives dictionary representation of a Student instance
        """
        if attrs is None:
            attrs = ['first_name', 'last_name', 'age']
        data = {}
        for attr in attrs:
            try:
                data[attr] = getattr(self, attr)
            except AttributeError:
                pass
        return data
