#!/usr/bin/python3
"""
4-from_json_string module
with a function from_json_string
"""


def from_json_string(my_str):
    """
    returns an object (Python data structure)
    represented by a JSON string
    """
    import json

    return json.loads(my_str)
