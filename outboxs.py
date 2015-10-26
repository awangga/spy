#!/usr/bin/env python
"""
insert.py -  Program to :
1. insert to outbox collection, 
2. check if main is running? if not run then run
"""
print "Content-Type: text-html"
print
import cgitb
cgitb.enable()
import cgi
import smsweb
import subprocess

#form = cgi.FieldStorage()

#rcpt = form["rcpt"].value
#msg = form["msg"].value

sw = smsweb.SmsWeb()
sw.opendb()
if not id: 
	print sw.getOutbox(id)
else:
	for a in sw.getOutboxs():
		print a
