#!/usr/bin/env python3
import os
import json
import sys

import libtest
import devs
import logs

remote_working_dir = r"D:\Code\wip\bat-rises\test\networkdrive"
local_working_dir = r"D:\Code\wip\bat-rises\test\local\DESKTOP"

def read_files_txt():
	with open("./test/testfiles.txt", "r") as f:
		lines = [x.strip("\n") for x in f.readlines()]
	return [x for x in lines if x.strip() and not x.startswith("#")]

#TODO: rename push
def dev_push():
	pass

#TODO: rename pull
def dev_pull():
	for path in read_files_txt():
		(relative_path, file) = os.path.split(path)
		devs.do_path_pull(relative_path, file, remote_working_dir, local_working_dir)

if __name__ == "__main__":
	options = {"push":dev_push, "pull":dev_pull}

	if not os.path.isfile("logs.json"):
		logs.create_logs(read_files_txt())

	if len(sys.argv) > 1 and sys.argv[1].lower() in options:
		options[sys.argv[1].lower()]()
