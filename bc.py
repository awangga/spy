#!/usr/bin/env python
"""
main.py - broadcast message input rcpt array, msg text
"""
print "Content-Type: text-html"
print
import cgitb
cgitb.enable()
import cgi
import libs
import re
form = cgi.FieldStorage()

rcpt = form["rcpt"].value
msg = form["msg"].value

rcptarr = re.split(',|;',rcpt)

print rcptarr
print msg
sms = libs.Libs(rcptarr[0],msg)
for num in rcptarr:
	print r
	sms.rcpt(num)
	sms.send()
	

#sms = libs.Libs(rcpt,msg)

#sms.send()


