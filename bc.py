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
form = cgi.FieldStorage()

sms = smspdu.Smspdu(form["rcpt"].value,form["msg"].value)
sms.send()
#sms.close()

