#!/usr/bin/env python3

# Common functions
# Author:	Jason Buss
# Created:	2016-03-16
# Version: 	1.0

import os
path = os.path.dirname(__file__)

def get_varfromfile(filename):
	# gets variables from file
	import imp
	f = open(filename)
	global data
	data = imp.load_source('data', '', f)
	f.close()
	return data
	
def get_config(file):
	config = get_varfromfile('{0}\config\{1}'.format(path, file))
	return config	