#!/usr/bin/env python3
import os
import shutil
from . import logs

def check_dir_tree(dst_full_path):
    """checks if the directory exists 
       and makes it if it doesnt"""

    if not os.path.isdir(dst_full_path):
        print (f"[ LOG ]  destination directory path does not exist.")
        print (f"[ LOG ]  creating path {dst_full_path}")
        os.makedirs(dst_full_path)

def do_path_pull(relative_path, file, src_working_dir, dst_working_dir):
    ( src_full_path, dst_full_path, dst_path_no_file ) = get_paths(relative_path, file, src_working_dir, dst_working_dir)
    print (f"\n== PULL == ")
    display_src_dst(src_full_path, dst_full_path)
    if os.path.isfile(src_full_path):
    #if source is a file
        if os.path.isfile(dst_full_path):

            if is_newer(src_full_path, dst_full_path):
                print (f"[ LOG ]  SRC is newer than DST, pulling")
                do_copy_op(src_full_path, dst_full_path, dst_path_no_file, False)
            else:
                print (f"[ LOG ]  SRC is not newer than DST, not pulling")
        else:
            #if file doesnt exist, lets pull
            print (f"[ LOG ]  DST does not exist, pulling")
            do_copy_op(src_full_path, dst_full_path, dst_path_no_file, False)
    else:
        print (f"[ LOG ]  SRC does not exist, not pulling")

def display_src_dst(src, dst):
    print (f"[ SRC ]  {src}")
    print (f"[ DST ]  {dst}")

def do_copy_op(src_full_path, dst_full_path, dst_path_no_file, is_Logged):
    check_dir_tree(dst_path_no_file)
    shutil.copy(src_full_path, dst_path_no_file)
    if is_Logged:
        print ("[ LOG ]  copy event was logged ")
        logs.change_log(dst_full_path, os.path.getmtime(dst_full_path))


def is_newer(a, b):
    return True if os.path.getmtime(a) > os.path.getmtime(b) else False

def get_paths(r, f, s, d):
    #TODO: lol
    return (os.path.join(s, r, f), os.path.join(d, r, f), os.path.join(d, r))

def do_path_push(relative_path, file, src_working_dir, dst_working_dir):
    ( src_full_path, dst_full_path, dst_path_no_file ) = get_paths(relative_path, file, src_working_dir, dst_working_dir)
    
    # TODO: TRY-CATCH for file checks?
    # step-by-step for this mess:
    print (f"\n== PUSH == ")
    display_src_dst(src_full_path, dst_full_path)
    if os.path.isfile(src_full_path):
    # if source is a real file
        if os.path.isfile(dst_full_path):
            
            if is_newer(src_full_path, dst_full_path):
                print (f"{os.path.getmtime(src_full_path)}")
                print (f"{os.path.getmtime(dst_full_path)}")
                print (f"[ LOG ]  SRC is newer than DST")
            # if destination exists and source is newer 
            # we cant check if its newer if it doesnt exist
                if logs.is_in_logs(dst_full_path) and logs.we_modified(dst_full_path, os.path.getmtime(dst_full_path)):
                # has it been modified before and did we modify it last?
                    print (f"[ LOG ]  DST was last modified by us, pushing")
                    do_copy_op(src_full_path, dst_full_path, dst_path_no_file, True)

                elif logs.is_in_logs(dst_full_path) and not logs.we_modified(dst_full_path, os.path.getmtime(dst_full_path)):
                # we didnt modify it last but its in the logs
                    print (f"[ LOG ]  DST was not last modified by this program")
                else:
                # file exists in destination but it isnt logged, do nothing
                    print (f"[ LOG ]  DST exists but is not logged, not pushing")
            else:
                print (f"[ LOG ]  DST last modified date is newer or same than SRC, not pushing")
        # if destination doesnt exist (and therefore cant be newer)
        # copy!
        else:
            print ("huh")
            do_copy_op(src_full_path, dst_full_path, dst_path_no_file, True)
    else:
        # source doesnt exist
        print (f"{src_full_path} no such file!")
            
