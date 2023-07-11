#!/usr/bin/python3
"""func class_to_json
returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """Creates a dictionary description of obj

    Args:
        - obj: object 
    Returns: dictionary description of obj
    """

    return obj.__dict__
