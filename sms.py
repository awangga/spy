#!/usr/bin/env python
"""
sms.py - Used to send txt messages.
"""
import config
import serial
from datetime import datetime

class Sms(object):
    def __init__(self, recipient=config.recipient, message=config.message):
        self.logfile = open("modem.log","w")
        self.open()
        self.recipient = recipient
        self.content = message

    def open(self):
        self.logfile.write(str(datetime.now()))
        self.logfile.write('open serial\n')
        self.ser = serial.Serial(config.serial, 115200, timeout=5)
        self.SendCommand('ATZ\r')
        self.logfile.write(str(datetime.now()))
        self.logfile.write('send ATZ\n')
        self.SendCommand('AT+CMGF=1\r')
        self.logfile.write(str(datetime.now()))
        self.logfile.write('send ATZ\n')

    def setRecipient(self, number):
        self.recipient = number

    def setContent(self, message):
        self.content = message

    def send(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        self.logfile.write(str(datetime.now()))
        self.logfile.write('send CMGS\n')
        command = '''AT+CMGS="''' + self.recipient.encode() + '''"\r\r'''
        self.SendCommand(command,getline=True)
        self.logfile.write(str(datetime.now()))
        self.logfile.write('after send 1 CMGS\n')
        #data = self.ser.readall()
        #print data
        self.logfile.write(str(datetime.now()))
        self.logfile.write('send CMGS\n')
        command = self.content.encode() + "\r\r"
        self.logfile.write(str(datetime.now()))
        self.logfile.write('after send 2 CMGS\n')
        self.SendCommand(command,getline=True)
        self.logfile.write(str(datetime.now()))
        self.logfile.write('after send 3 CMGS\n')
        data = self.ser.readall()
        print data
        command = chr(26)
        self.logfile.write(str(datetime.now()))
        self.logfile.write('after send 4 CMGS\n')
        self.SendCommand(command,getline=True)
        self.logfile.write(str(datetime.now()))
        self.logfile.write('after send 5 CMGS\n')
        data = self.ser.readall()
        print data
        self.logfile.write(str(datetime.now()))
        self.logfile.write('after send 6 CMGS\n')

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
