#!/usr/bin/python3
"""
Class that prevents dynamic attributes creation

"""


class LockedClass():
    """Clas stop dynamic attributes creation"""
    __slots__ = ['first_name']

    def __init__(self):
        """Init method"""
        pass
