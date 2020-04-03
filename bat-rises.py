#!/usr/bin/env python3
import os
import json
from docopy import do_copy
import libtest

local_loc = os.fspath(r"D:\Code\wip\bat-rises\test\local\DESKTOP")
remo_rep = os.fspath(r"D:\Code\wip\bat-rises\test\networkdrive")

def read_logs():
	with open("logs.json", "r") as f:
		return json.load(f)

def set_log(dst, dst_modified):
	logs = read_logs()
	with open("logs.json", "w") as f:
		logs[dst] = dst_modified
		json.dump(logs, f)
		
def main():
	with open("./test/testfiles.txt", "r") as f:
		lines = [x.strip("\n") for x in f.readlines()]
	for path in [x for x in lines if x.strip() and not x.startswith("#")]:
		(remote, file) = os.path.split(path)		
		libtest.work(local_loc, remote, file, src_omit = r"D:\Code\wip\bat-rises\test\local\DESKTOP", dst_omit = r"D:\Code\wip\bat-rises\test\networkdrive")
		libtest.work(remote, local_loc, file, dst_omit = r"D:\Code\wip\bat-rises\test\local\DESKTOP", src_omit = r"D:\Code\wip\bat-rises\test\networkdrive")

if __name__ == "__main__":
	main()
	#TODO: add configs
	#TODO: maybe arguments so you can change settings on the terminal
