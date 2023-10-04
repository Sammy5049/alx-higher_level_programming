#!/usr/bin/python3


""" class Rectangle that defines a rectangle """


class Rectangle:
    def __init__(self, width=0, height=0):

        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self._width = width  """ Private instance attribute for width """
        self._height = height  """Private instance attribute for height"""

    @property
    def width(self):
        """Getter method for width attribute."""
        return self._width

    @width.setter
    def width(self, value):
        """Setter method for width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Getter method for height attribute."""
        return self._height

    @height.setter
    def height(self, value):
        """Setter method for height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
