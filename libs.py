#!/usr/bin/env python
"""
sms.py - Used to send txt messages.
"""
import config
import re
import time
from datetime import datetime
import serial
from messaging.sms import SmsSubmit

class Libs(object):
    def __init__(self, recipient=config.recipient, message=config.message):
        self.logfile = open("modem.log","w")
        self.open()
        self.recipient = recipient
        self.content = message

    def open(self):
        self.ser = serial.Serial(config.serial, 115200, timeout=config.timeout)
        self.ser.flushInput()
        self.ser.flushOutput()
        self.SendCommand('ATZ\r',8)
        self.SendCommand('AT+CMGF=0\r',16)
        #cocoba
        #self.SendCommand('AT+CMGS=29\r',16)# ga usah pake read dulu karena menunggu >
        #pdunya = '0891269846040000F111000D91261813020003F00000AA10F33ABC2C07A9C3EE717D0D5ABFCB'
        #perintah = '%s\x1a' % pdunya
        #self.SendCommand(perintah,len(perintah)+19)
        #print 'sms kedua'
        #self.SendCommand('AT+CMGS=29\r',16)# ga usah pake read dulu karena menunggu >
        #pdunya = '0891269846040000F111000D91261813020003F00000AA10F33ABC2C07A9C3EE717D0D5ABFCB'
        #perintah = '%s\x1a' % pdunya
        #self.SendCommand(perintah,len(perintah)+19)

    def rcpt(self, number):
        self.recipient = number

    def msg(self, message):
        self.content = message

    def send(self):
        #self.ser.flushInput()
        #self.ser.flushOutput()
        self.pdu = SmsSubmit(self.recipient, self.content)
        for xpdu in self.pdu.to_pdu():
	        command = 'AT+CMGS=%d\r' % xpdu.length
	        self.SendCommand(command,len(str(xpdu.length))+14)
	        command = '%s\x1a' % xpdu.pdu
	        self.SendCommand(command,len(xpdu.pdu)+20)
	        self.logfile.write(str(datetime.now()))
	        self.logfile.write('   after send a sms \n')

    def close(self):
        self.ser.close()

    def SendCommand(self,command,char,getline=True):
        self.logfile.write(str(datetime.now()))
        self.logfile.write('   before send command '+str(char)+' \n')
        self.ser.write(command)
        data = ''
        if getline:
            data=self.ReadLine(char)
        self.logfile.write(str(datetime.now()))
        self.logfile.write('   after send command '+str(char)+' \n')
        return data 
        
    def ReadAll(self):
    	data = self.ser.readall()
    	return data
    
    def ReadLine(self,char):
        data = self.ser.read(char)
        if 'OK' in data:
        	print ' berhasil '
        if 'ERROR' in data:
        	print ' gagal '
        print data+' char:<'+str(char)+'> '
        return data

    def unreadMsg(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        command = 'AT+CMGL=0\r\n'
        self.SendCommand(command,getline=True)
        data = self.ser.readall()
        print data
        
    def readMsg(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        command = 'AT+CMGL=1\r\n'
        self.SendCommand(command,getline=True)
        data = self.ser.readall()
        print data

    def allMsg(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        command = 'AT+CMGL=4\r\n'
        self.SendCommand(command,getline=True)
        data = self.ser.readall()
        print data
        
    def deleteMsg(self, idx):
        self.ser.flushInput()
        self.ser.flushOutput()
        command = 'AT+CMGD=%s\r\n' % idx
        self.SendCommand(command,getline=True)
        data = self.ser.readall()
        print data

    def getMsg(self, idx):
        self.ser.flushInput()
        self.ser.flushOutput()
        command = 'AT+CMGR=%s\r\n' % idx
        self.SendCommand(command,getline=True)
        data = self.ser.readall()
        print data        
        
