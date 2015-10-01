#!/usr/bin/env python
"""
main.py - Main Program to send txt messages. harus pake +62 atau 0 di depan nomor kalo 62 tanpa plus ga jalan jadinya
"""
import smspdu
import config


#sms = smspdu.Smspdu("+6281320380477",config.message)#yogo
#sms.send()
#sms.rcpt("+6281390320212")#
#sms.send()
#sms.rcpt("+6289610707901")
#sms.send()
#sms.rcpt("+628997194777")
#sms.send()
#sms.rcpt("+6289697217506")
#sms.send()
#sms.rcpt("+6285236041995")
#sms.send()
#sms.rcpt("+6281320708675")#sebelah kiri
#sms.send()
#sms.rcpt("+6285624874074")#beny prast
#sms.send()
#sms.rcpt("+6285703006269")#adam
#sms.send()
sms.rcpt("+6285221313763")
sms.send()
sms.rcpt("+6289655231804")
sms.send()
sms.rcpt("+6282217173862")
sms.send()
sms.rcpt("+6285763983023")
sms.send()
sms.rcpt("+6289668923560")
sms.send()
sms.rcpt("+6285775080595")
sms.send()
sms.rcpt("+6285775080595")
sms.send()
sms.rcpt("+6281221393675")#amid
sms.send()
sms.rcpt("+6282126630079")#sofia
sms.send()
sms.rcpt("+6281320582897")
sms.send()
sms.rcpt("+6281220970785")#p asep
sms.send()

sms.close()