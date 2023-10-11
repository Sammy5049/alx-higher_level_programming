#!/usr/bin/python3
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
    """Get a dictionary representation of the Student.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
    
    if attrs is None:
        return self.__dict__

    list_ster = {}

    for attr in attrs:
        if hasattr(self, attr):
            list_ster[attr] = getattr(self, attr)
    return list_ster
