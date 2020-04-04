#!/usr/bin/env python3
import configparser

def get_configs(profile):
	config = configparser.ConfigParser()
	config.read("conf.ini")
	remote_root = config[profile]["remote_root"]
	local_root  = config[profile]["local_root"]
	filelist    = config[profile]["filelist"]
	return (remote_root, local_root, filelist)