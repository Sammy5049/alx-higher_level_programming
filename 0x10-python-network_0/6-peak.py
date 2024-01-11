#!/usr/bin/python3
"""Algorithms for list of ints."""


def find_peak(list_of_integers):
    """Finds a peak in a list."""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
