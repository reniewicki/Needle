#!/usr/bin/env python
# coding=utf-8

import codecs, os.path, sys, re, shutil, time, getpass, os, distutils

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == "__main__":
	
	print "Enter number to translate to hex and binary. Or enter exit to quit"
	num = ""
	
	while (num.lower() != "exit"):
		num = raw_input("Enter number: ")
		if (re.sub(r'[\D]', r"", num) != "" and re.sub(r'[\d]', r"", num) == ""): #skips any entries with non-numeric characters
			print "Hex: " + hex(int(num)) + "    Binary: " + bin(int(num))
			num = ""
		elif (num.lower() != "exit"): print "Please only enter a number"