#!/usr/bin/env python3

# Main working script
# Author:	Jason Buss
# Created:	2016-03-17
# Version: 	1.0

import os
import fxsystem
import pymssql as sql

path = os.path.dirname(fxsystem.__file__)
config = fxsystem.getVarFromFile(path + '\config\sql.config')
location = config.location


conn = sql.connect(config.server, config.username, config.password, config.database)
cursor = conn.cursor()

def executeSql(SQL):
	# Run a sql statement against the database
	cursor.execute(SQL)
	conn.commit()
	
def getValue(tablename, fieldname, where):
	# get a value from the database
	sql = "select {0} from dbo.{1} where {2}".format(fieldname, tablename, where)
	
	cursor.execute(sql)
	row = cursor.fetchone()	
	return row
	
			

def setValue(tablename, fieldname, value, where):
	# sets value in the database
	sql = "update dbo.{1} set {2} = {3} where {4}".format(tablename,fieldname,value,where)
	cursor.execute(sql)
	conn.commit()