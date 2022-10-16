#!/usr/bin/python3
"""This module contains the Student class"""


class Student():
    """Defines the Student class"""
    def __init__(self, first_name, last_name, age):
        """Creates a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__

        new_dic = {}
        for i in attrs:
            try:
                new_dic[i] = self.__dict__[i]
            except:
                pass

        return new_dic

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except:
                pass
