#!/usr/bin/env python
"""
main.py - Main Program to send txt messages.
"""
import smspdu
import config


sms = smspdu.Smspdu("081320380477",config.message)
sms.send()
sms = smspdu.Smspdu("081390320212",config.message)
sms.send()
sms = smspdu.Smspdu("089610707901",config.message)
sms.send()
sms = smspdu.Smspdu("08997194777",config.message)
sms.send()
sms = smspdu.Smspdu("089697217506",config.message)
sms.send()
sms = smspdu.Smspdu("085236041995",config.message)
sms.send()

