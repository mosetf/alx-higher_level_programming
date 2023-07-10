#!/usr/bin/python3
"""
module that that returns the list of
available attributes and methods of an object
"""


def lookup(obj):
    """
    a funt that rerurns a list object
    args:

        - obj: object to be inspected
    """
    return dir(obj)
