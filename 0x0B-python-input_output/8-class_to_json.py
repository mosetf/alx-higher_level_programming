#!/usr/bin/python3
"""func class_to_json
returns the dictionary description with simple data structure
"""


def class_to_json(obj):
    """Creates a dictionary description of obj

    Args:
        - obj: object 
    Returns: dictionary description of obj
    """

    return obj.__dict__
