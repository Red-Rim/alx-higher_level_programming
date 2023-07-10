#!/usr/bin/python3
"""function that returns the list"""


def lookup(obj):
    """returns the list of available attributes and methods of an object
        obj : argument
        Return : list
    """

    return (dir(obj))
