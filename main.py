#!/usr/bin/env python
"""
main.py - Main Program to send txt messages.
"""
import sms
import time

sms = sms.Sms("089610707901","sebuah kekagokan")
sms.send()
sms.read()
sms.disconnect()
