#!/usr/bin/env python
"""
main.py - broadcast message input rcpt array, msg text
"""
print "Content-Type: text-html"
print
import cgitb
import time
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
	print '*batas*'+num
	sms.rcpt(num)
	#time.sleep(3.5)
	data = sms.send()
	print data
	if 'ERROR' in data:
		print 'gagal kirim'
	if 'OK' in data:
		print 'berhasil kirim'
	#print sms.ReadAll()


