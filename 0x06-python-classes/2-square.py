#!/usr/bin/python3
"""Square module.

This is a module that defines a square,
and set private instance of size.

"""


class Square:
    """Defines the class"""

    def __init__(self, size=0):
        """Sets the attributes for Square object.

        Args:
            size (int): size of one edge of square.

        Raises:
            TypeError: when size is not an integer.
            ValueError: when size is < 0.
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size <= 0:
            raise ValueError("size must be >= 0")
        self.__size = size
