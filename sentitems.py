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

#id = form["id"].value

sw = smsweb.SmsWeb()
sw.opendb()
if not id: 
	print sw.getSentitem(id)
else:
	for a in sw.getSentitems():
		print a
