#!/usr/bin/env python3

# Main working script
# Author:	Jason Buss
# Created:	2016-03-17
# Version: 	1.0

import fx_sql as sql
import fx_sqlstrings as sqlstr


class Ticket():
	"""Instance of a ticket"""
	# getValue(tablename, fieldname, where)
	def __init__(self, ticketnumber):
	
		self.ticketid = ticketnumber
		record = fx_sql.get_scalar(sqlstr.get_sqlselect("TICKET", 'ACCOUNTID', 'ASSIGNEDTOID', 'NEEDEDBYDATE', 'STATUSCODE', 'CONTACTID', 'ISSUE', 'NOTES'))
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
	
	def __init__(self, ticketid)
	
		self.ticketid = ticketid