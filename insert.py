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

form = cgi.FieldStorage()

rcpt = form["rcpt"].value
msg = form["msg"].value

sw = smsweb.SmsWeb()
sw.opendb()
print sw.insertOutbox(rcpt,msg)
