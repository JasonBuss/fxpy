# Python system functions
# Author: Jason Buss
# Created: 2016-02-09
# Version: 1.0

from os import getenv as a
from os import environ as b

def getSystemVar(VariableName):
	# can be used to get temporary system variable
	server = a(VariableName)
	return server
	
def setSystemVar(VariableName, Value):
	# can be used to set temporary system variable
	import os as x
	b[VariableName] = Value
	
def getVarFromFile(filename):
	# gets variables from file
	import imp
	f = open(filename)
	global data
	data = imp.load_source('data', '', f)
	f.close()
	return data
	
