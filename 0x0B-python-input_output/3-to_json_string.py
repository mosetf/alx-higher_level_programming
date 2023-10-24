#!/usr/bin/python3
"""func to_json_string
Returns the JSON representation of an object(string)
"""


import json


def to_json_string(my_obj):
    """Returns the JSON representation of my_obj

    Args:
        - my_obj: string to be represent
    Returns: JSON representation
    """

    return json.dumps(my_obj)
