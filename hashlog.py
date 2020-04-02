#!/usr/bin/env python3
import hashlib
import json

def write_log(a):
    #a = {destination:hash_}
    with open("actions.json", 'w') as f:
        json.dump(a, f)

def change_log(destination, new_hash):
    with open("actions.json", "r") as f:
        d = json.load(f)
    with open("actions.json", "w") as f:
        d[destination] = new_hash
        json.dump(d, f)
    

def find_in_log(destination, destination_hash):
    with open("actions.json", "r") as f:
        d = json.load(f)
    if destination in d:
        print ("found name")
        if d[destination] == destination_hash:
            print ("found has")
            return True
    else:
        return False

def is_hash_match(source, destination):
    print (f"checking {source} and {destination}")
    if check_hash(source) == check_hash(destination):
        return True
    else: 
        return False

def check_hash(filename):
    with open(filename, 'r') as file:
        return hashlib.md5(file.read().encode('utf-8')).hexdigest()
    