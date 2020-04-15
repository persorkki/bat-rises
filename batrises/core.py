import os
import shutil
import colorama
from pathlib import Path

from .rcodes import *
from .utils import *
from . import logs
from . import outs
    
#TODO: use pathlib instead

def do_copy(src, dst, isLogged):
    check_dir_tree(dst.parent)
    try:
        shutil.copy2(src, dst)
        if isLogged:
            #TODO: why parse dst here and why do it twice
            
            logs.change_log(dst, dst.stat().st_mtime)
        return ReturnCode.SUCCESS
       
    except PermissionError:
        return ReturnCode.FILE_IN_USE

def send(loc, rem):
    """send loc to rem"""
    # does the local file exist
    if not loc.exists():
        return ReturnCode.NO_SOURCE

    # does the remote file exist
    # if it doesnt, copy loc to rem
    if not rem.exists():
        return do_copy(loc, rem, True)

    # is the remote file newer than local
    if not is_older_than(rem, loc):
        return ReturnCode.NOT_OLDER

    # is the remote file in logs
    # was the remote file last modified by us
    # if it wasnt, copy loc to rem
    if logs.is_in_logs(rem) and logs.we_modified(rem, rem.stat().st_mtime):
        return do_copy(loc, rem, True)

    # if it wasnt, ask the user how to proceed
    else:
        if outs.question_override(loc, rem):
            return do_copy(loc, rem, True)
        else:
            return ReturnCode.USER_CANCEL

def download(loc, rem):
    """download rem to loc"""
    # does the remote file exist
    if not rem.exists():
        return ReturnCode.NO_SOURCE

    # does the local file exist
    # if it doesnt, copy rem to loc, isLogged = False
    if not loc.is_file():
        return do_copy(rem, loc, False)

    # is the local file older than remote
    if not is_older_than(loc, rem):
        return ReturnCode.NOT_OLDER

    if outs.question_override(rem, loc):
        return do_copy(rem, loc, False)
    else:
        return ReturnCode.USER_CANCEL
