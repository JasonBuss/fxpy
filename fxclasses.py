#!/usr/bin/env python3

# main class script
# Author:	Jason Buss
# Created:	2016-03-17
# Version: 	1.0

class Ticket():
	"""Instance of a ticket"""
	# getValue(tablename, fieldname, where)
	def __init__(self, ticketnumber)
	
		import fxsql as sql
		
		self.ticketid = ticketnumber
		
		if sql.get_value("count(*)", "ticket", "Ticketid={0}".format(ticketnumber)) > 0:
			self.status = sql.getValue("Status", "Ticket", "TicketId={0}".format(ticketnumber))
			self.duedate = sql.getValue("DueDate", "Ticket", "TicketId={0}".format(ticketnumber))
		else:
			self.status = "Open"
			self.duedate = GetDate()
					
	def create_ticket(self):
		print("created ticket")
		
class TicketActivity():
	"""Instance of a ticket activity record"""
	
	def __init__(self, ticketid)
	
		self.ticketid = ticketid