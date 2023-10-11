#!/usr/bin/python3
"""Defines a class Student."""
class Student:
    """Rep a student."""

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


def to_json(self):
    """Get a dictionary repr of Student."""
    list_ster = {}

    for key, value in self.__dict__.items():
        if isinstance(value, (int, str)):
            list_ster[key] = value
    return list_ster
