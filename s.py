#!/usr/bin/env python
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

sms = libs.Libs(rcptarr[0],msg)
for num in rcptarr:
	print ' \n *batas*'+num
	sms.rcpt(num)
	sms.send()


#sms = smspdu.Smspdu(form["rcpt"].value,form["msg"].value)
#sms.send()
#sms.close()

