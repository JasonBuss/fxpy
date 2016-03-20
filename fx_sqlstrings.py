#!/usr/bin/env python3

# Description
# Author:	
# Created:	
# Version: 	


def get_sqlselect(tablename, *fields):
	if tablename.upper() == "OPPORTUNITY_PRODUCT":
		x = "OPPPRODUCTID"
	else:
		x = tablename + "ID"
		
	x = x + ", CREATEATE, CREATEUSER, MODIFYDATE, MODIFYUSER"	
	for field in fields:
		x += ", " + field
	sql = "select {0} from {1}".format(x, tablename).upper()
	return sql
	
def get_sqlinsert(tablename, *fields):
	x = tablename + "ID"
	for field in fields:
		x += ", " + field
	return "select " + x + " from " + tablename

def get_sqlupdate(tablename, *fields):
	x = tablename + "ID"
	for field in fields:
		x += ", " + field
	return "select " + x + " from " + tablename	

def get_sqlwhere(tablename, condition):
	x = tablename + "ID"
	for field in fields:
		x += ", " + field
	return "select " + x + " from " + tablename	