import os

def check_dir_tree(dst):
    """checks if the directory exists 
       and makes it if it doesnt"""
    if not os.path.isdir(os.path.basename(dst)):
        os.makedirs(os.path.basename(dst))

def is_older_than(src, dst):
	return True if os.path.getmtime(src) < os.path.getmtime(dst) else False