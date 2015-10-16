#!/usr/bin/env python
"""
main.py - broadcast message input rcpt array, msg text
"""
print "Content-Type: text-html"
print
import cgitb
cgitb.enable()
import cgi
import smspdu
import re
form = cgi.FieldStorage()

rcpt = form["rcpt"].value
msg = form["msg"].value

rcptarr = re.split(',|;',rcpt)

print rcptarr
#sms = smspdu.Smspdu(rcpt,msg)

#sms.send()
#sms.close()

