#!/usr/bin/env python3
import os
import hashlib
from shutil import copy

def do_copy(source, destination):
    try:
        copy(source, destination)
    except IOError:
        print(f"unable to copy from: {source} -> {destination}")
        exit(os.EX_OSERR)

def copy_files(file_list):

    pass

def read_files(filename):
    try:
        with open(filename, 'r') as file:
            lines = [x.strip("\n") for x in file.readlines()]
    except IOError:
        print (f"error opening {filename}")
        exit(os.EX_OSERR)

    return [x for x in lines if x.strip() and not x.startswith("#")]
    
def check_hash(filename):
    with open(filename, 'r') as file:
        m = hashlib.md5(file.read().encode('utf-8')).hexdigest()
        print (m)

def main():
    for x in read_files("files.txt"):
        try:
            (source, filename) = x.rsplit("\\", 1) 
            #TODO: make it work with all path types and normal slashes
        except ValueError:
            print (f"location {x} is not formatted correctly")



if __name__ == "__main__":
    main()