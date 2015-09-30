#!/usr/bin/env python
"""
main.py - Main Program to send txt messages.
"""
import sms

sms = sms.Sms("089610707901","sebuah kekagokan")
sms.send()
sms.unread()
sms.disconnect()
