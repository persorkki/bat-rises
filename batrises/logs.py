import os
import json

def we_modified(dst, mtime):
    dump = _read_logs()
    return dump[dst] == mtime

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

def create_logs(remote_working_dir, local_working_dir, loglist):
    dump = dict()
    for log in loglist:
        log = os.path.join(remote_working_dir, log)
        dump[log] = os.path.getmtime(log)
    with open('logs.json', 'w') as f:
        json.dump(dump, f)