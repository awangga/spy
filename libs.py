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
	        #data = self.ser.readall()
	        #data = self.ser.read(128)
	        #print data
	        #self.logfile.write(str(time.clock()))
	        #self.logfile.write('after send readall 1 \n')
	        command = '%s\x1a' % xpdu.pdu
	        self.SendCommand(command,len(xpdu.pdu)+20)
	        #print self.ser.readline()
	        #data = self.ser.readall()
	        #data = self.Read('\n')
	        #print data
	        self.logfile.write(str(datetime.now()))
	        self.logfile.write('   after send a sms \n')
		#data = areadline+breadline
		#return data

    def close(self):
        self.ser.close()

    def SendCommand(self,command,char,getline=True):
        self.logfile.write(str(datetime.now()))
        self.logfile.write('   before send command init \n')
        self.ser.write(command)
        data = ''
        if getline:
            data=self.ReadLine(char)
        self.logfile.write(str(datetime.now()))
        self.logfile.write('   after send command init \n')
        return data 
        
    def SendCommands(self,command,n,getline=True):
        self.logfile.write(str(datetime.now()))
        self.logfile.write('   before send command init \n')
        self.ser.write(command)
        data = ''
        if getline:
            data=self.ReadLines(n)
        self.logfile.write(str(datetime.now()))
        self.logfile.write('   after send command init \n')
        return data 
        
    def ReadAll(self):
    	data = self.ser.readall()
    	return data
    
    def ReadLine(self,char):
        #bytesToRead = self.ser.inWaiting()
        #data = self.ser.read(bytesToRead)
        data = self.ser.read(char)
        #data = self.ser.readline()
        #data += self.ser.readline()
        #data += self.ser.readline()
        #data += self.ser.readline()
        if 'OK' in data:
        	print ' berhasil '
        if 'ERROR' in data:
        	print ' gagal '
        print data+' char:<'+str(char)+'> '
        return data
        
    def ReadLines(self,n):
        #bytesToRead = self.ser.inWaiting()
        #data = self.ser.read(bytesToRead)
        #data = self.ser.read(char)
        data = ''
        #data += self.ser.readline()
        #data += self.ser.readline()
        #data += self.ser.readline()
        i=0
        while i < n:
        	data += self.ser.readline()
        	print ' readline-> '+str(i)+' <- '
        	i += 1
        #if 'OK' in data:
        #	print ' berhasil '
        #if 'ERROR' in data:
        #	print ' gagal '
        print data
        return data
        
    def ReadStatus(self):
        data = ''
        while (not ('OK' in data)) or (not ('ERROR' in data)):
        	data += self.ser.readline()
        print data
        return data
        
    def Read(self,term):
        matcher = re.compile(term) # search anything
        buff = ''
        tic = time.clock()
        buff += self.ser.read(128)
        #while ((time.clock - tic) < config.timeout) and (not matcher.search(buff)):
        while ((time.clock() - tic) < config.timeout) and (not matcher.search(buff)):
        	buff += self.ser.read(128)
        return buff

    def unreadMsg(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        command = 'AT+CMGL=0\r\n'#gets incoming sms that has not been read
        self.SendCommand(command,getline=True)
        data = self.ser.readall()
        print data
        
    def readMsg(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        command = 'AT+CMGL=1\r\n'#gets incoming sms that has not been read
        self.SendCommand(command,getline=True)
        data = self.ser.readall()
        print data

    def allMsg(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        command = 'AT+CMGL=4\r\n'#gets incoming sms that has not been read
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
        
