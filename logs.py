#!/usr/bin/env python3
import os
import json

def we_modified(dst, mtime):
	
	return False

def _read_logs():
	with open("logs.json", "r") as f:
		return json.load(f)

def is_in_logs(dst):
	return True if dst in _read_logs() else False

def change_log(dst, mtime):
	dump = _read_logs()
	dump[dst] = mtime
	with open('logs.json', 'w') as f:
		json.dump(dump, f)

def create_logs(loglist):
	dump = dict()
	for log in loglist:
		dump[log] = os.path.getmtime(log)

	with open('logs.json', 'w') as f:
		json.dump(dump, f)
"""			
def read_logs():
	with open("logs.json", "r") as f:
		return json.load(f)

def set_log(dst, dst_modified):
	logs = read_logs()
	with open("logs.json", "w") as f:
		logs[dst] = dst_modified
		json.dump(logs, f)
"""