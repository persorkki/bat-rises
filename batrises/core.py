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
    #print (dst.parent)
    shutil.copy2(src, dst.parent)
    if isLogged:
        #TODO: why parse dst here and why do it twice
        #TODO: or is it better to keep logs more modular
        logs.change_log(str(dst), os.path.getmtime(dst))

def send(loc, rem):
    """send loc to rem"""
    # does the local file exist
    if not loc.exists():
        return ReturnCode.NO_SOURCE

    # does the remote file exist
    # if it doesnt, copy loc to rem
    if not rem.exists():
        do_copy(loc, rem, True)
        return ReturnCode.SUCCESS

    # is the remote file newer than local
    if not is_older_than(rem, loc):
        return ReturnCode.NOT_OLDER

    # is the remote file in logs
    # was the remote file last modified by us
    # if it wasnt, copy loc to rem
    if logs.is_in_logs(rem) and logs.we_modified(rem, rem.stat().st_mtime):
        do_copy(loc, rem, True)
        return ReturnCode.SUCCESS

    # if it wasnt, ask the user how to proceed
    else:
        if outs.question_override(loc, rem):
            do_copy(loc, rem, True)
            return ReturnCode.SUCCESS
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
        do_copy(rem, loc, False)
        return ReturnCode.SUCCESS

    # is the local file older than remote
    if not is_older_than(loc, rem):
        return ReturnCode.NOT_OLDER

    if outs.question_override(rem, loc):
        do_copy(rem, loc, False)
        return ReturnCode.SUCCESS
    else:
        return ReturnCode.USER_CANCEL
