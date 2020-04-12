#!/usr/bin/env python3

import os
import sys
from pathlib import Path
from batrises import *

def read_files_txt(filelist):
    with open(filelist, "r") as f:
        lines = [x.strip("\n") for x in f.readlines()]
    return [x for x in lines if x.strip() and not x.startswith("#")]

def download_and_send(remote_root, local_root, filelist):
    for f in filelist:
        l = Path(f.replace(remote_root, local_root))
        f = Path(f)
        
        outs.out(l, f, core.send(l, f).get_val())
        outs.out(l, f, core.download(l, f).get_val())

if __name__ == "__main__":
    options = {"both":download_and_send,
               "make":logs.create_logs,
               }
    os.chdir( os.path.dirname(__file__) )
    (remote_root, local_root, filelist) = get_configs("default") 

    if not os.path.isfile("logs.json"):
        logs.create_logs(loglist = read_files_txt(filelist), 
                         local_working_dir=local_root,
                         remote_working_dir=remote_root)
    if len(sys.argv) > 1 and sys.argv[1] in options:
        options[sys.argv[1]]( remote_root, local_root, read_files_txt(filelist) )
    
    #download_and_send(remote_root, local_root, read_files_txt(filelist) )
    input("press Enter to close this window...")