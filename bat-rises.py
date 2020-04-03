#!/usr/bin/env python3
import os
import json
import sys

import devs
import logs

remote_working_dir = r"D:\Code\wip\bat-rises\test\networkdrive"
local_working_dir = r"D:\Code\wip\bat-rises\test\local\DESKTOP"

def read_files_txt():
	with open("./test/testfiles.txt", "r") as f:
		lines = [x.strip("\n") for x in f.readlines()]
	return [x for x in lines if x.strip() and not x.startswith("#")]

#TODO: rename push
def dev_push(loglist, local_working_dir, remote_working_dir):
	for path in loglist:
		(relative_path, file) = os.path.split(path)
		devs.do_path_push(relative_path, file, local_working_dir, remote_working_dir)

#TODO: rename pull
def dev_pull(loglist, local_working_dir, remote_working_dir):
	for path in loglist:
		(relative_path, file) = os.path.split(path)
		devs.do_path_pull(relative_path, file, remote_working_dir, local_working_dir)

if __name__ == "__main__":
	options = {"push":dev_push, "pull":dev_pull, "clogs": logs.create_logs}

	if not os.path.isfile("logs.json"):
		logs.create_logs()

	if len(sys.argv) > 1 and sys.argv[1].lower() in options:
		options[sys.argv[1].lower()](loglist = read_files_txt(), local_working_dir=local_working_dir, remote_working_dir=remote_working_dir)
