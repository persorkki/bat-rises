import os
from pathlib import Path

def check_dir_tree(dst):
    """checks if the directory exists 
       and makes it if it doesnt"""
    if not dst.exists():
        os.makedirs(dst.parent)

def is_older_than(src, dst):
	return True if os.path.getmtime(src) < os.path.getmtime(dst) else False