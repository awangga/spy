#!/usr/bin/env python
"""
main.py - Main Program to send txt messages.
"""
import smspdu
psn = "Neng...!!! ieu mamah pake HP batur.. mamah keur aya masalah di kantor polisi.. mamah menta tulung pang nganteurkeun cai sa ember... inget cai sa ember ... lain pulsa...pulsa mah loba keneh...mamah keur milu ngising di kantor polisi... caina saat ... burukeun ulah seuri... mamah can cebok yeuh, inget nya neng.. cai sa ember ..!!! lain pulsa...!!! mamah geus cangkeul nagog"

sms = smspdu.Smspdu("081320380477",psn)
sms.send()
sms = smspdu.Smspdu("081390320212",psn)
sms.send()
sms = smspdu.Smspdu("089610707901",psn)
sms.send()
sms = smspdu.Smspdu("08997194777",psn)
sms.send()
sms = smspdu.Smspdu("089697217506",psn)
sms.send()
sms = smspdu.Smspdu("085236041995",psn)
sms.send()
sms.unread()
sms.disconnect()
