#!/usr/bin/python3
"""The base module"""
import json


class Base():
    """Base class with:
    __nb_objects as a class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Object constructor"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of a list of dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        new_list = []
        if list_objs is not None:
            for index in list_objs:
                new_list.append(cls.to_dictionary(index))
        with open(filename, "w", encoding="utf-8") as my_file:
            my_file.write(cls.to_json_string(new_list))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1, 0, 0)
        elif cls.__name__ == "Square":
            new_instance = cls(1, 0, 0)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        instance_list = []
        try:
            with open(filename, "r", encoding="utf-8") as my_file:
                instance_list = cls.from_json_string(my_file.read())
            for index, value in enumerate(instance_list):
                instance_list[index] = cls.create(instance_list[index])
        except:
            pass
        return instance_list
