#!/usr/bin/env python3
import os
import json
from shutil import copy

local_loc = os.fspath(r"D:\Code\wip\bat-rises\test\loc\local")
remo_rep = os.fspath(r"E:\remoteloc\local")

def read_logs():
	with open("logs.json", "r") as f:
		return json.load(f)

def set_log(dst, dst_modified):
	logs = read_logs()
	with open("logs.json", "w") as f:
		logs[dst] = dst_modified
		json.dump(logs, f)
def temp_log_setter():
	with open("testfiles.txt", "r") as f:
		lines = [x.strip("\n") for x in f.readlines()]
	for path in [x for x in lines if x.strip() and not x.startswith("#")]:
		(remote, file) = os.path.split(path)
		local_= remote.replace(remo_rep, local_loc)
		g = os.path.join(remote, file)
		set_log(g, os.path.getmtime(g))
	
def con_copy_text(src, dst):
	print ("copied from ")
	print (f"{src}")
	print ("to")
	print (f"{dst}")

def main():
	with open("testfiles.txt", "r") as f:
		lines = [x.strip("\n") for x in f.readlines()]
		
	for path in [x for x in lines if x.strip() and not x.startswith("#")]:
		(remote, file) = os.path.split(path)
		local_= remote.replace(remo_rep, local_loc)

		do_copy(os.path.join(local_, file), os.path.join(remote, file), True)

def do_copy(src, dst, is_check):
	if is_check and os.path.isfile(src):
		logs = read_logs()

		if os.path.isfile(dst) and os.path.getmtime(src) > os.path.getmtime(dst):
			"""if destination is actually a file and if the local file is newer"""

			if dst in logs and os.path.getmtime(dst) == logs[dst]:
				"""if the file was modified by us before and
				if the file is still the same, then
				copy and log the event"""

				copy(src, dst)
				set_log(dst, os.path.getmtime(dst))
				con_copy_text(src, dst)

		elif not os.path.isfile(dst):
			copy(src, dst)
			set_log(dst, os.path.getmtime(dst))
			con_copy_text(src, dst)

	elif not is_check and os.path.isfile(src):
		"""used when the file is being copied from remote to local
		so we dont write any logs for this event, for now"""
		if os.path.getmtime(src) > os.path.getmtime(dst):
			"""only copy if remote is newer than local"""
			copy(src, dst)
			con_copy_text(src, dst)
if __name__ == "__main__":

	main()
	#TODO: add configs
	#TODO: maybe arguments so you can change settings on the terminal
