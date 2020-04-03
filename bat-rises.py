#!/usr/bin/env python3
import os
import json
import sys

import libtest
import logs

local_loc = os.fspath(r"D:\Code\wip\bat-rises\test\local\DESKTOP")
remo_rep = os.fspath(r"D:\Code\wip\bat-rises\test\networkdrive")

def read_files_txt():
	with open("./test/testfiles.txt", "r") as f:
		lines = [x.strip("\n") for x in f.readlines()]
	return [x for x in lines if x.strip() and not x.startswith("#")]

def push():
	for path in read_files_txt():
		(remote, file) = os.path.split(path)		
		libtest.do_path(local_loc, remote, file, src_omit = r"D:\Code\wip\bat-rises\test\local\DESKTOP", dst_omit = r"D:\Code\wip\bat-rises\test\networkdrive",is_logged=True)

def pull():
	for path in read_files_txt():
		(remote, file) = os.path.split(path)	
		libtest.do_path(remote, local_loc, file, dst_omit = r"D:\Code\wip\bat-rises\test\local\DESKTOP", src_omit = r"D:\Code\wip\bat-rises\test\networkdrive", is_logged=False)

if __name__ == "__main__":
	options = {"push":push, "pull":pull}

	if not os.path.isfile("logs.json"):
		logs.create_logs(read_files_txt())

	if len(sys.argv) > 1 and sys.argv[1].lower() in options:
		options[sys.argv[1].lower()]()
