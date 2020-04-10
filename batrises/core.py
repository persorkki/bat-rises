#!/usr/bin/env python3
import os
import shutil
import colorama

from .rcodes import *
from .utils import *
from . import logs
	
def do_copy(src, dst, isLogged):
	check_dir_tree(dst)
	shutil.copy2(src, dst)

	if isLogged:
		logs.change_log(dst, os.path.getmtime(dst))
	
def question_override(src, dst):
	print (f"\n{colorama.Fore.RED}OVERRIDE QUESTION ")
	print (f"file is not in logs or it was not modified by us")
	print (f"override {colorama.Fore.BLUE}{colorama.Back.WHITE}DST{colorama.Style.RESET_ALL} with {colorama.Fore.WHITE}{colorama.Back.BLUE}SRC{colorama.Style.RESET_ALL}?")
	
	print (f"src:	{colorama.Fore.WHITE}{colorama.Back.BLUE}{src}")
	print (f"dst:	{colorama.Fore.BLUE}{colorama.Back.WHITE}{dst}")
	
	while (True):
		print ("1. Yes, override")
		print ("2. No, do nothing")
		x = input(">")
		if x == "1":
			return True
		elif x == "2":
			return False
		
def send(loc, rem):
	"""send loc to rem"""
	# does the local file exist
	if not os.path.isfile(loc):
		return ReturnCode.NO_SOURCE

	# does the remote file exist
	# if it doesnt, copy loc to rem
	if not os.path.isfile(rem):
		do_copy(loc, rem, True)
		return ReturnCode.SUCCESS

	# is the remote file older than local
	if not is_older_than(rem, loc):
		return ReturnCode.NOT_OLDER

	# is the remote file in logs
	# was the remote file last modified by us
	# if it wasnt, copy loc to rem
	if logs.is_in_logs(rem) and logs.we_modified(rem, os.path.getmtime(rem)):
		do_copy(loc, rem, True)
		return ReturnCode.SUCCESS

	# if it wasnt, ask the user how to proceed
	else:
		if question_override(loc, rem):
			do_copy(loc, rem, True)
			return ReturnCode.SUCCESS
		else:
			return ReturnCode.USER_CANCEL

def download(loc, rem):
	"""download rem to loc"""
	# does the remote file exist
	if not os.path.isfile(rem):
		print (rem)
		return ReturnCode.NO_SOURCE

	# does the local file exist
	# if it doesnt, copy rem to loc, isLogged = False
	if not os.path.isfile(loc):
		do_copy(rem, loc, False)
		return ReturnCode.SUCCESS

	# is the local file older than remote
	if not is_older_than(loc, rem):
		return ReturnCode.NOT_OLDER

	if question_override(rem, loc):
		do_copy(rem, loc, False)
		return ReturnCode.SUCCESS
	else:
		return ReturnCode.USER_CANCEL
