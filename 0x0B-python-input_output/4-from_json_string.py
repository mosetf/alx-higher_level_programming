#!/usr/bin/python3
"""func from_json_string
Returns a data structure represented by a JSON string
"""


import json


def from_json_string(my_str):
    """Returns the data structure represented by my_str

    Args:
        - my_str: JSON string representation
    Returns: data structure
    """

    return json.loads(my_str)
