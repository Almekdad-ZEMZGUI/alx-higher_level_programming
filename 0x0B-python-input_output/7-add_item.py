#!/usr/bin/python3
"""
7-add_item module
with a script that adds all arguments to
a Python list, and then save them to a file
"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"

try:
    existing_content = load_from_json_file(file)
except FileNotFoundError:
    existing_content = []

save_to_json_file(existing_content + argv[1:], file)
