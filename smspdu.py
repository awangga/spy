#!/usr/bin/env python
"""
sms.py - Used to send txt messages.
"""
import config
import serial
from messaging.sms import SmsSubmit

class Smspdu(object):
    def __init__(self, recipient=config.recipient, message=config.message):
        self.open()
        self.recipient = recipient
        self.content = message

    def open(self):
        self.ser = serial.Serial(config.serial, 115200, timeout=5)
        self.SendCommand('ATZ\r')
        self.SendCommand('AT+CMGF=0\r')

    def setRecipient(self, number):
        self.recipient = number

    def setContent(self, message):
        self.content = message

    def send(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        self.pdu = SmsSubmit(self.recipient, self.content)
        for xpdu in self.pdu.to_pdu():
	        command = 'AT+CMGS=%d\r' % self.pdu.length
	        self.SendCommand(command,getline=True)
	        data = self.ser.readall()
	        print data
	        command = '%s\x1a' % self.pdu.pdu
	        self.SendCommand(command,getline=True)
	        data = self.ser.readall()
	        print data

    def disconnect(self):
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
        command = 'AT+CMGL="REC UNREAD"\r\n'#gets incoming sms that has not been read
        self.SendCommand(command,getline=True)
        data = self.ser.readall()
        print data
        
    def read(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        command = 'AT+CMGL="REC READ"\r\n'#gets incoming sms that has not been read
        self.SendCommand(command,getline=True)
        data = self.ser.readall()
        print data

    def all(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        command = 'AT+CMGL="ALL"\r\n'#gets incoming sms that has not been read
        self.SendCommand(command,getline=True)
        data = self.ser.readall()
        print data
