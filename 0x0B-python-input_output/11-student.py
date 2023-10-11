#!/usr/bin/python3
"""Defines a class Student."""
class Student:
    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.firstName = first_name
        self.lastName = last_name
        self.age = age


def to_json(self, attrs=None):
    if attrs is None:
        return self.__dict__

    list_of_data = {}

    for attr in attrs:
        if hasattr(self, attr):
            list_of_data[attr] = getattr(self, attr)
    return list_of_data


def reload_from_json(self, json):
    for key, value in json.items():
        setattr(self, key, value)
