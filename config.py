#!/usr/bin/env python
"""
Daftar SMSC (SMS CENTER) Operator Telepon Selular Indonesia
+62 Indonesia

(1) Mentari [Indosat] : +62-81615, +62816124, +62816125, +62816126, +62816127, +62816128
(2) IM3 [Indosat] : +62855000000
(3) Simpati, Kartu As [Telkomsel] : +6281100000, +62811000000
(4) XL [Excelcomindo] : +62818445009, +628184450095
(5) Three [Hutchinson] : +6289644000001
(6) Axis [Lippo Tel] : +628315000032, +628315000031
(7) Flexi [Telkom] : +6280980000
"""

def success():
    print "Success to send!"


serial = "/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller-if00-port0"
recipient = '+6289610707901'
message = "Neng...!!! ieu mamah pake HP batur.. mamah keur aya masalah di kantor polisi.. mamah menta tulung pang nganteurkeun cai sa ember... inget cai sa ember ... lain pulsa...pulsa mah loba keneh...mamah keur milu ngising di kantor polisi... caina saat ... burukeun ulah seuri... mamah can cebok yeuh, inget nya neng.. cai sa ember ..!!! lain pulsa...!!! mamah geus cangkeul nagog"
port = 8181

