#!/usr/bin/python3
""" script that adds arguments to Python list and then save them to a file """
from os import path
import json
import sys



save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
if path.exists("add_item.json"):
   my_list =  load_from_json_file("add_item.json")
else:
    my_list = []
my_list += sys.argv[1:]

save_to_json_file(my_list, "add_item.json")
