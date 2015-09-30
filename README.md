# spy
SMS Python USB Modem

### 3G Modem AT Commands for SMS
General SMS Commands
AT+CMGF – Set SMS Text Mode or SMS PDU Mode
AT+CMGD – Delete a Received Message

PDU Mode SMS Commands
AT+CMGL – List Received Messages

Text Mode SMS Commands
AT+CMGS – Send SMS Message
AT+CMGL – List Received Messages

### PDU SMS
ATZ<ENTER>
AT+CMGF=0<ENTER>
at+cmgs=35<ENTER>
0891269846040000F111000C928069010797100000AA17F4F29C9E769F4170721D342FBBC969F71934AEE701<ctrl+z>
```sh
OK                                                                     
atz                                                                    
OK
at+cmgf=0
OK
at+cmgs=30
> 0891269846040000F111000C928069010797100000AA12F0BA9B5C779F41E1B4FB0C3A97D9753A
+CMGS: 23

OK
```

### AT Command Reference
 [1] http://www.diafaan.com/sms-tutorials/gsm-modem-tutorial/at-cmgf/
 [2] http://www.diafaan.com/sms-tutorials/gsm-modem-tutorial/at-cmgs-text-mode/
 [3] http://www.diafaan.com/sms-tutorials/gsm-modem-tutorial/at-cmgl-text-mode/