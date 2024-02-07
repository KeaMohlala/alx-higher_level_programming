#!/usr/bin/python3
"""
A module for a script that adds command line arguments
to a Python list and saves them to a file
"""
import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if len(sys.argv) > 1:
    try:
        items = load_from_json_file("add_item.json")
    except Exception:
        items = []

    for item in sys.argv[1:]:
        items.append(item)

    save_to_json_file(items, "add_item.json")
else:
    items = []
    save_to_json_file(items, "add_item.json")
