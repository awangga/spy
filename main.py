#!/usr/bin/env python
"""
main.py - Main Program to send txt messages.
"""
import sms

sms = sms.Sms
sms.connectPhone
sms.sendMessage
sms.disconnectPhone

h = sms.Read()
h.GetReadSMS()
