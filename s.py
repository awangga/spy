#!/usr/bin/env python
"""
insert.py -  Program to :
1. insert to outbox collection, 
2. check if main is running? if not run then run
"""
print "Content-Type: application/json"
print
import cgitb
cgitb.enable()
import cgi
import smsweb
import subprocess

form = cgi.FieldStorage()

rcpt = form["rcpt"].value
msg = form["msg"].value

sw = smsweb.SmsWeb()
sw.opendb()
print sw.insertOutbox(rcpt,msg)

#run main
#os.system("python main.py")
pidfile = open("main.pid")
pids = pidfile.read()
if not pids:
	pid = 0
else: 
	pid = int(pids)
#pid = int(pids)
pidfile.close()
if not sw.isRunning(pid):
	#print "jalankan subproses"
	pid = subprocess.Popen(["nohup", "python", "main.py"], 
	                                    stdout=subprocess.PIPE, 
	                                    stderr=subprocess.STDOUT).pid
	pidfile = open("main.pid","w")
	pidfile.write(str(pid))
	pidfile.close()

