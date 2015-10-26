#!/usr/bin/env python
"""
smsweb : spy mongoDB connector
"""
import config
import os.path
import re
import time
import pymongo
from datetime import datetime
import serial
from messaging.sms import SmsSubmit
from messaging.sms import SmsDeliver

class SmsWeb(object):
    def __init__(self, recipient=config.recipient, message=config.message):
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
	    doc = {"rcpt":rcpt,"msg":msg,"timestamp":datetime.now()}
	    self.db.outbox.insert_one(doc)
	    ret = {"rcpt":rcpt,"msg":msg}
	    return ret
    
    def insertSentitem(self,rcpt,msg,stat):
	    self.db.sentitems
	    doc = {"rcpt":rcpt,"msg":msg,"timestamp":str(datetime.now()),"idProcess":self.idprocess,"stat":stat}
	    return self.db.sentitems.insert_one(doc).inserted_id
    
    def insertInbox(self,data):
	    self.db.inbox
	    return self.db.inbox.insert_one(data).inserted_id
	    
    def getSentitem(self,id):
	    self.db.sentitems
	    return self.db.sentitems.find_one({"idProcess":id})
	    
    def getSentitems(self):
	    self.db.sentitems
	    return self.db.sentitems.find()
	    
    def getOutbox(self):
	    self.db.outbox
	    return self.db.outbox.find_one()
	
    def getOutboxs(self):
	    self.db.outbox
	    return self.db.outbox.find()
    
    def getInbox(self):
	    self.db.inbox
	    return self.db.inbox.find_one()
    
    def removeOutbox(self,id):
	    self.db.outbox
	    return self.db.outbox.delete_many({"_id":id})
	    
    def dropOutbox(self):
	    self.db.drop_collection("outbox")
    
    def rcpt(self, number):
        self.recipient = number

    def msg(self, message):
        self.content = message

    def idProcess(self,idprocess):
	    self.idprocess = idprocess
    
    def sends(self):
	    rcptarr = re.split(',|;',self.recipient)
	    for num in rcptarr:
	    	if num:
		    	print '*Sending SMS to: '+num+' \n'
		    	self.rcpt(num)
		    	self.send()
    
    def send(self):
        self.pdu = SmsSubmit(self.recipient, self.content)
        for xpdu in self.pdu.to_pdu():
	        command = 'AT+CMGS=%d\r' % xpdu.length
	        a = self.SendCommand(command,len(str(xpdu.length))+14)
	        command = '%s\x1a' % xpdu.pdu
	        b = self.SendCommand(command,len(xpdu.pdu)+20)
	        data = str(a)+str(b)
	        self.insertSentitem(self.recipient,self.content,data)
        return data
	         
    def close(self):
        self.ser.close()

    def SendCommand(self,command,char,getline=True):
        self.ser.write(command)
        data = ''
        if getline:
            data=self.ReadLine(char)
        return data 
        
    def ReadAll(self):
    	data = self.ser.readall()
    	return data
    
    def ReadLine(self,char):
        data = self.ser.read(char)
        return data

    def unreadMsg(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        command = 'AT+CMGL=0\r\n'
        data = self.SendCommand(command,16)
        return data
        
    def readMsg(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        command = 'AT+CMGL=1\r\n'
        self.ser.write(command)
        cmd = self.ser.readline()
        cmd += self.ser.readline()
        head = self.ser.readline()
        a = []
        while "CMGL" in head:
	        data = self.ser.readline()
	        sms = SmsDeliver(data.rstrip())
	        idx = head.rstrip().split(',')[0].split(' ')[1]
	        self.insertInbox(sms.data)
	        #print idx
	        a.append(int(idx))
	        head = self.ser.readline()
        return a

    def allMsg(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        command = 'AT+CMGL=4\r\n'
        data = self.SendCommand(command,16)
        return data
        
    def deleteMsg(self, idx):
        self.ser.flushInput()
        self.ser.flushOutput()
        command = 'AT+CMGD=%s\r\n' % idx
        return self.SendCommand(command,18)
        #self.ser.write(command)
        #data = self.ser.readline()
        #data += self.ser.readline()
        #data += self.ser.readline()
        #return data

    def deleteMsgs(self, idx):
        #self.ser.flushInput()
        #self.ser.flushOutput()
        for id in idx:
	        command = 'AT+CMGD=%s\r\n' % id
	        self.SendCommand(command,18)
        
    def getMsg(self, idx):
        self.ser.flushInput()
        self.ser.flushOutput()
        command = 'AT+CMGR=%s\r\n' % idx
        self.ser.write(command)
        data = self.ser.readline()
        data += self.ser.readline()
        data3 = self.ser.readline()
        data = data+data3
        if "CMGR" in data3:
	        data += self.ser.readline()
	        data += self.ser.readline()
	        data += self.ser.readline()
        return data        
    
    def isRunning(self,pid):
    	path = "/proc/"+str(pid)
    	return os.path.exists(path)
    	#try:
    	#	os.kill(pid,0)
    	#except OSError:
    	#	return False
    	#else:
    	#	return True
    	
