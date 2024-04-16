#!/usr/bin/python3
"""
3-to_json_string module
with a function to_json_string
"""


def to_json_string(my_obj):
    """
    returns the JSON representation of
    an object (string)
    """
    import json

    return json.dumps(my_obj)
