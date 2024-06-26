#!/usr/bin/python3
"""
6-load_from_json_file module
with a function load_from_json_file
"""


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”
    """
    import json

    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
