#!/usr/bin/env python
"""
main.py - Main Program to send txt messages.
"""
import sms
import time

sms = sms.Sms("085315017317","ini dari spy man")
sms.send()
time.sleep(10)
sms.read()
sms.disconnect()
