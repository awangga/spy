#!/usr/bin/env python
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

