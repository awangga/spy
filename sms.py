#!/usr/bin/env python
"""
sms.py - Used to send txt messages.
"""
import config
import serial
import time

class Send(object):
    def __init__(self, recipient=config.recipient, message=config.message):
        self.ser = serial.Serial(config.serial, 115200, timeout=5)
        self.ser.write('ATZ\r')
        self.ser.write('AT+CMGF=1\r')
        self.recipient = recipient
        self.content = message
        

    def setRecipient(self, number):
        self.recipient = number

    def setContent(self, message):
        self.content = message

    def connectPhone(self):
        
        time.sleep(1)

    def sendMessage(self):
        
        time.sleep(1)
        self.ser.write('''AT+CMGS="''' + self.recipient + '''"\r''')
        time.sleep(1)
        self.ser.write(self.content + "\r")
        time.sleep(1)
        self.ser.write(chr(26))
        time.sleep(1)

    def disconnectPhone(self):
        self.ser.close()

class Read(object):

    def __init__(self):
        self.open()

    def open(self):
        self.ser = serial.Serial(config.serial, 115200, timeout=5)
        self.SendCommand('ATZ\r')
        self.SendCommand('AT+CMGF=1\r')

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

    def GetAllSMS(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        command = 'AT+CMGL="REC UNREAD"\r\n'#gets incoming sms that has not been read
        print self.SendCommand(command,getline=True)
        data = self.ser.readall()
        print data
        
    def GetReadSMS(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        command = 'AT+CMGL="REC READ"\r\n'#gets incoming sms that has not been read
        print self.SendCommand(command,getline=True)
        data = self.ser.readall()
        print data
