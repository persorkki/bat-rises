#!/usr/bin/env python3
import os
from shutil import copy

from hashlog import *

loc = r"D:\Code\wip\bat-rises\test\loc\local"

def do_copy(source, destination):
    print ("\n")
    print (f" from: {source}")
    print (f"   to: {destination}")

    #see if we need to create the files
    
    if os.path.isfile(destination) and os.path.isfile(source):
        
        #if the local file is newer than destination
        #if not, do not override the destination which is newer
        if is_newer(source, destination):
            #if our file is newer, check if the destination was actually modified by us. 
            #if not, do not override the destination because it was likely edited by someone else
            if find_in_log(destination, check_hash(destination)):
                print (f"[LOG] hash also matches the log, destination was created by this program")
                print (f"[ACTION] COPYING {source}    ->    {destination}")
                copy(source, destination)
                change_log(destination, check_hash(source))
            else:
                print (f"[LOG] did not find a hash match, destination was not modified by this program earlier")
                print (f"[ACTION] NOT COPYING {source}    ->    {destination}")
        else:
            print (f"[LOG] destination is newer than source!")
            print (f"[ACTION] NOT COPYING {source}    ->    {destination}")
    else:
        if os.path.isfile(source):
            print (f"[LOG] file does not exist in destination")
            print (f"[ACTION] COPYING {source}    ->    {destination}")
            copy(source, destination)
            change_log(destination, check_hash(source))
        else:
            print (f"[LOG] source does not exist!")

def is_newer(source, destination):
    return os.path.getmtime(source) > os.path.getmtime(destination)

def read_files(filename):
    with open(filename, 'r') as file:
        lines = [x.strip("\n") for x in file.readlines()]
    return [x for x in lines if x.strip() and not x.startswith("#")]

def main():
    for x in read_files("files.txt"):
        try:
            (source, filename) = x.rsplit("\\", 1) 
            #TODO: make it work with all path types and normal slashes?
        except ValueError:
            print (f"location {x} is not formatted correctly")
            continue
        else:
            #do_copy(os.path.join(source,filename),os.path.join(loc,filename))
            do_copy(os.path.join(loc,filename),os.path.join(source,filename))
 
    #input("\ndone! press enter to close this window")
def templogwrite():
    a = dict()
    for x in read_files('files.txt'):
        a[x] = check_hash(x)
    write_log(a)

if __name__ == "__main__":
    #templogwrite()
    main()
