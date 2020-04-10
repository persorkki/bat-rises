#!/usr/bin/env python3
import os
import sys

from batrises import *

def read_files_txt(filelist):
    with open(filelist, "r") as f:
        lines = [x.strip("\n") for x in f.readlines()]
    return [x for x in lines if x.strip() and not x.startswith("#")]

def push(loglist, local_working_dir, remote_working_dir):
    for path in loglist:
        (relative_path, file) = os.path.split(path)
        do_path_push(relative_path, file, local_working_dir, remote_working_dir)

def pull(loglist, local_working_dir, remote_working_dir):
    for path in loglist:
        (relative_path, file) = os.path.split(path)
        do_path_pull(relative_path, file, remote_working_dir, local_working_dir)

if __name__ == "__main__":
    os.chdir( os.path.dirname(__file__) )
    options = {"push":push, "pull":pull, "clogs": logs.create_logs, "test": test.send}
    (remote_root, local_root, filelist) = get_configs("default") 
    #TODO: add profiles

    #if logs dont exist, make them
    if not os.path.isfile("logs.json"):
        logs.create_logs(loglist = read_files_txt(filelist), 
                         local_working_dir=local_root,
                         remote_working_dir=remote_root)

    #cmdline arguments
    if len(sys.argv) > 1 and sys.argv[1].lower() in options:
        options[sys.argv[1].lower()](loglist = read_files_txt(filelist), 
                                     local_working_dir=local_root,
                                     remote_working_dir=remote_root)
    elif len(sys.argv) == 1:
        push(loglist = read_files_txt(filelist), 
             local_working_dir=local_root,
             remote_working_dir=remote_root)

        pull(loglist = read_files_txt(filelist), 
             local_working_dir=local_root,
             remote_working_dir=remote_root)
    
    input("press Enter to close this window...")