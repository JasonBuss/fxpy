#!/usr/bin/env python3

# Description: SQL Access scripts
# Author:	Jason Buss
# Created:	2016-03-20	
# Version: 	1.0

import pymssql as sql
from fx_config import database as db


conn = sql.connect(db.server, db.username, db.password, db.database)
cursor = conn.cursor()

def execute_sql(sql):
	# Run a sql statement against the database
	cursor.execute(sql)
	conn.commit()
	
def get_scalar(sql):
	# get a single row from the database
	cursor.execute(sql)
	row = cursor.fetchone()	
	return row

def get_values(sql):
	# get multiple rows from the database
	cursor.execute(sql)
	row = cursor.fetchall()	
	return row	
