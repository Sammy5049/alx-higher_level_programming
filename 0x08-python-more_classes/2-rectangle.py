#!/usr/bin/python3

""" class Rectangle that defines a rectangle """


class Rectangle:
    def __init__(self, width=0, height=0):

        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

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

    def area(self):
        """Calculate and return the rectangle area."""
        return self._width * self._height

    def perimeter(self):
        """Calculate and return the rectangle perimeter."""
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)
