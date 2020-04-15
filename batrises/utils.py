import os
from .rcodes import *
from pathlib import Path

def check_dir_tree(dst_dir):
    """checks if the directory exists 
       and makes it if it doesnt"""
    if not dst_dir.exists():
        dst_dir.mkdir(parents=True)
        return ReturnCode.SUCCESS
    else:
        return ReturnCode.FAIL    
         
def is_older_than(src, dst):
    return True if src.stat().st_mtime < dst.stat().st_mtime else False