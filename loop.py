#!/usr/bin/python
import sys
import paramiko
for arg in sys.argv:
	print arg
	print sys.argv[1]
def printnumbers(n):
	for i in range(1,n+1):
		print i


printnumbers(3)
