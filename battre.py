#!/usr/bin/env python3
import os
import sys
import colorama

from batrises import *

def read_files_txt(filelist):
    with open(filelist, "r") as f:
        lines = [x.strip("\n") for x in f.readlines()]
    return [x for x in lines if x.strip() and not x.startswith("#")]

def download_and_send(remote_root, local_root, filelist):
    for f in filelist:
        l = f.replace(remote_root, local_root)
        colorama.init(autoreset=True)
        print (f"{colorama.Fore.BLUE}-> send {l} {core.send(l, f).get_val()}")
        print (f"{colorama.Fore.GREEN}<- download {f} {core.download(l, f).get_val()}\n")

if __name__ == "__main__":
    os.chdir( os.path.dirname(__file__) )
    (remote_root, local_root, filelist) = get_configs("default") 

    if not os.path.isfile("logs.json"):
        logs.create_logs(loglist = read_files_txt(filelist), 
                         local_working_dir=local_root,
                         remote_working_dir=remote_root)

    download_and_send(remote_root, local_root, read_files_txt(filelist) )
    input("press Enter to close this window...")