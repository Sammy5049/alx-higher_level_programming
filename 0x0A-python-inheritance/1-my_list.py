#!/usr/bin/python3
"""MyList module."""


class MyList(list):
    """Defines the MyList class."""

    def print_sorted(self):
        """Prints the sorted list."""
        print(sorted(self))
