#!/usr/bin/env python
"""
main.py - Main Program to :
1. get from outbox, 
2. sent sms via modem
3. insert to sentitems
"""
import smsweb

sw = smsweb.SmsWeb()
sw.opendb()
dt=sw.getOutbox()
sw.openser()
while dt:
	sw.rcpt(dt["rcpt"])
	sw.msg(dt["msg"])
	sw.idProcess(dt["_id"])
	sw.sends()
	sw.removeOutbox(dt["_id"])
	dt=sw.getOutbox()

print "Done..."