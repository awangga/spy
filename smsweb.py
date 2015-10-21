#!/usr/bin/env python
"""
Spong : spy mongoDB connector
"""
import config
import re
import time
import pymongo
from datetime import datetime
import serial
from messaging.sms import SmsSubmit

class SmsWeb(object):
    def __init__(self, recipient=config.recipient, message=config.message):
        self.logfile = open("modem.log","w")
        #self.open()
        self.recipient = recipient
        self.content = message

    def openser(self):
        self.ser = serial.Serial(config.serial, 115200, timeout=config.timeout)
        self.ser.flushInput()
        self.ser.flushOutput()
        self.SendCommand('ATZ\r',8)
        self.SendCommand('AT+CMGF=0\r',16)

    def opendb(self):
	    self.conn = pymongo.MongoClient(config.mongohost, config.mongoport)
	    self.db = self.conn.smsweb
    
    def insertOutbox(self,rcpt,msg):
	    self.db.outbox
	    doc = {"rcpt":rcpt,"msg":msg}
	    return self.db.outbox.insert_one(doc).inserted_id
    
    def insertSentitem(self,rcpt,msg,stat):
	    self.db.sentitems
	    doc = {"rcpt":rcpt,"msg":msg,"stat":stat}
	    return self.db.sentitems.insert_one(doc).inserted_id
    
    def getOutbox(self):
	    self.db.outbox
	    return self.db.outbox.find_one()
    
    def rcpt(self, number):
        self.recipient = number

    def msg(self, message):
        self.content = message

    def sends(self):
	    rcptarr = re.split(',|;',self.recipient)
	    sms = libs.Libs(rcptarr[0],self.content)
	    for num in rcptarr:
	    	print '*Sending SMS to: *'+num
	    	sms.rcpt(num)
	    	self.send()
    
    def send(self):
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
        
