#!/usr/bin/python3
"""
module that defines base module from
which all the other class will inherit
"""
import json
import os


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        converts a list of dictionaries to
        JSON representation.

        Args:
        list_dictionaries: a list of dictionaries to convert to
        JSON string

        Returns empty string if list dictionaries is empty or None
        """
        if list_dictionaries == []:
            return "[]"
        elif list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes JSON string representatation
        of a list of objects to a file by converting
        objects to dictionaries first

        Args:
        list of objects to write to the file
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            list_of_dicts = [obj.to_dictionary() for obj in list_objs]
            json_string = Base.to_json_string(list_of_dicts)
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        returns json string from a list of dictionaries
        returns empty list if 'json_string' is empty or 'None'

        Args:
        string representing a list of dictionaries
        """
        if json_string == "[]" or json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        creates an instance with attributes already set

        Args:
        dictionary: dictionary representation of the instance
        """
        instance = cls.__new__(cls)
        instance.__dict__.update(dictionary)
        instance.__init__(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r", encoding="utf-8") as f:
            json_content = f.read()
        list_of_dicts = Base.from_json_string(json_content)
        list_of_instances = [cls.create(**item) for item in list_of_dicts]
        return list_of_instances
