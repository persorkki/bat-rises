import os
from pathlib import Path

def check_dir_tree(dst):
    """checks if the directory exists 
       and makes it if it doesnt"""
    if not dst.exists():
        dst.mkdir(parents=True)
        
def is_older_than(src, dst):
    return True if src.stat().st_mtime < dst.stat().st_mtime else False