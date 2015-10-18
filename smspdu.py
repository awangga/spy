#!/usr/bin/env python
"""
sms.py - Used to send txt messages.
"""
import config
import serial
from datetime import datetime


from messaging.sms import SmsSubmit

class Smspdu(object):
    def __init__(self, recipient=config.recipient, message=config.message):
        self.logfile = open("modem.log","w")
        self.open()
        self.recipient = recipient
        self.content = message
        

    def open(self):
        self.logfile.write(str(datetime.now()))
        self.logfile.write('open serial\n')
        self.ser = serial.Serial(config.serial, 115200, timeout=5)
        self.logfile.write(str(datetime.now()))
        self.logfile.write('send ATZ\n')
        self.SendCommand('ATZ\r')
        self.logfile.write(str(datetime.now()))
        self.logfile.write('send ATZ\n')
        self.SendCommand('AT+CMGF=0\r')

    def rcpt(self, number):
        self.recipient = number

    def msg(self, message):
        self.content = message

    def send(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        self.pdu = SmsSubmit(self.recipient, self.content)
        for xpdu in self.pdu.to_pdu():
	        self.logfile.write(str(datetime.now()))
	        self.logfile.write('send CMGS\n')
	        command = 'AT+CMGS=%d\r' % xpdu.length
	        self.SendCommand(command,getline=True)
	        self.logfile.write(str(datetime.now()))
	        self.logfile.write('after send 1 CMGS\n')
	        data = self.ser.readall()
	        print data
	        self.logfile.write(str(datetime.now()))
	        self.logfile.write('after send 2 CMGS\n')
	        command = '%s\x1a' % xpdu.pdu
	        self.SendCommand(command,getline=True)
	        self.logfile.write(str(datetime.now()))
	        self.logfile.write('after send 3 CMGS\n')
	        data = self.ser.readall()
	        print data
	        self.logfile.write(str(datetime.now()))
	        self.logfile.write('after send 4 CMGS\n')

    def close(self):
        self.ser.close()

    def SendCommand(self,command, getline=True):
        self.ser.write(command)
        data = ''
        if getline:
            data=self.ReadLine()
        return data 

    def ReadLine(self):
        data = self.ser.readline()
        print data
        return data 

    def unread(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        command = 'AT+CMGL=0\r\n'#gets incoming sms that has not been read
        self.SendCommand(command,getline=True)
        data = self.ser.readall()
        print data
        
    def read(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        command = 'AT+CMGL=1\r\n'#gets incoming sms that has not been read
        self.SendCommand(command,getline=True)
        data = self.ser.readall()
        print data

    def all(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        command = 'AT+CMGL=4\r\n'#gets incoming sms that has not been read
        self.SendCommand(command,getline=True)
        data = self.ser.readall()
        print data
        
    def delete(self, idx):
        self.ser.flushInput()
        self.ser.flushOutput()
        command = 'AT+CMGD=%s\r\n' % idx
        self.SendCommand(command,getline=True)
        data = self.ser.readall()
        print data

    def get(self, idx):
        self.ser.flushInput()
        self.ser.flushOutput()
        command = 'AT+CMGR=%s\r\n' % idx
        self.SendCommand(command,getline=True)
        data = self.ser.readall()
        print data        
        
