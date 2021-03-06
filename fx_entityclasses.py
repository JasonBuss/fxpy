#!/usr/bin/env python3

# Main working script
# Author:	Jason Buss
# Created:	2016-03-17
# Version: 	1.0

import fx_sql as sql
import fx_sqlstrings as sqlstr
from fx_config import database as db

appdb = sql.SQLObj(db.server, db.username, db.password, db.database)
slxdb = sql.SQLObj(db.fxserver, db.fxusername, db.fxpassword, db.fxdatabase)

def getRecordCount(table, ID):
	select = sqlstr.get_sqlselect(table, "count (*) as cnt")
	where = "" 

class Account():
	"""Instance of an Account"""
	def __init__(self, accountid):
		self.accountid = accountid
		
		select = sqlstr.get_sqlselect("ACCOUNT", "ACCOUNT", "TYPE", "STATUS")
		where = sqlstr.sqlstr_sqlwhere("ACCOUNTID", accountid)
		record = slxdb.get_scalar(select + " " + where)
		self.accountname = record[0]
		self.type = record[1]
		self.status = record[2]

		
class Contact():
	"""instance of a contact"""
	def __init__(self, contactid):
		
		self.contactid = contactid
		select = sqlstr.get_sqlselect("CONTACT", "TYPE", "ACCOUNTID", "ISPRIMARY", "LASTNAME", "FIRSTNAME", "MIDDLENAME", "STATUS", "TITLE", "WORKPHONE", "EMAIL")
		where = sqlstr.sqlstr_sqlwhere("CONTACTID", contactid)
		record = slxdb.get_scalar(select + " " + where)
		
		self.type = record[0]
		self.accountid = record[1]
		self.isprimary = record[2]
		self.lastname = record[3]
		self.firstname = record[4]
		self.middlename = record[5]
		self.status = record[6]
		self.title = record[7]
		self.workphone = record[8]
		self.email = record[9]
		
class Opportunity():
	"""Instance of an Opportunity"""
	def __init__(self, opportunityid):
		self.opportunityid = opportunityid
		record = slxdb.get_scalar(sqlstr.get_sqlselect("OPPORTUNITY", "ACCOUNTID", "DESCRIPTION", "TYPE", "ESTIMATEDCLOSE", "NOTES") + sqlstr.sqlstr_sqlwhere("OPPORTUNITY", opportunityid))
		self.accountid = record[0]
		self.description = record[1]
		self.type = record[2]
		self.estimatedclose = record[3]
		self.notes = record[4]
		
class Ticket():
	"""Instance of a ticket"""
	def __init__(self, ticketnumber):
	
		self.ticketid = ticketnumber
		record = slxdb.get_scalar(sqlstr.get_sqlselect("TICKET", 'ACCOUNTID', 'ASSIGNEDTOID', 'NEEDEDBYDATE', 'STATUSCODE', 'CONTACTID', 'ISSUE', 'NOTES') + sqlstr.get_sqlwhere('ALTERNATEKEYSUFFIX', ticketnumber))
		self.accountid = record[5]
		self.assignedtoid = record[6]
		self.neededbydate = record[7]
		self.statuscode = record[8]
		self.contactid = record[9]
		self.issue = record[10]
		self.notes = record[11]
					
	def save():
		"""Save ticket to DB"""
		print('saved')
		
		
class TicketActivity():
	"""Instance of a ticket activity record"""
	
	def __init__(self, ticketid):
	
		self.ticketid = ticketid