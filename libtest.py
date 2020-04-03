#!/usr/bin/env python3
import os
from shutil import copy
import logs

def do_path(src, dst, file, src_omit, dst_omit, is_logged):
	#TODO: maybe making directories should be left to the copy operation
	#	   because we dont know if we copy anything yet

	if dst_omit != dst:
		dst_tree = os.path.relpath(dst, dst_omit)
	else:
		dst_tree = ""
	if src_omit != src:
		src_tree = os.path.relpath(src, src_omit)
	else:
		src_tree = ""

	#constructed source file path
	#final_src_dir = os.path.join(src, dst_tree)
	#^ source dir is not needed ^
	final_src = os.path.join(src, dst_tree, file)

	#constructed destination file path
	final_dst_dir = os.path.join(dst, src_tree)
	final_dst = os.path.join(dst, src_tree, file)
	
	#does the source file even exist?
	if os.path.isfile(final_src):
		if not os.path.exists(final_dst_dir):
			os.makedirs(final_dst_dir)
		
		#print ("directories OK!")
		if os.path.isfile(final_dst):
			do_copy(final_src, final_dst, is_logged)
		else:
			copy(final_src, final_dst)
	else:
		print (f"{final_src} does not exist")
	
def do_copy(src, dst, is_logged):

	dst_time = os.path.getmtime(dst)
	src_time = os.path.getmtime(src)

	#is source file newer than destination?
	if src_time > dst_time:
		#do we check for logs or are we blindly pulling stuff from dst
		if is_logged:
			#is it in logs?
			if logs.is_in_logs(dst):
				#and did we modify it?
				if logs.we_modified(dst, dst_time):
					#then we copy and modify the log
					print (f"copying {src} to {dst}")
					copy(src, dst)
					logs.change_log(dst, os.path.getmtime(dst))
				else:
					print (f"we didnt modify {dst}, skipping...")
			else:
				print (f"{dst} not in logs, skipping...")
		else:
			print ("blindly copying")
			copy(src,dst)
	else:
		print (f"{src} is not newer than {dst}, skipping...")
