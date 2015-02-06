#!/usr/bin/env python
# coding=utf-8

import codecs, os.path, sys, re, shutil, time, getpass, os, distutils, zipfile

reload(sys)
sys.setdefaultencoding('utf-8')


	
if __name__ == "__main__":

	if (len(sys.argv) != 2):
			print len(sys.argv)
			print "Usage: ReadZip.py <filepath>"
			print "  Lists the contents of zipfile"
			exit(1)
	filepath = sys.argv[1]
	if (os.path.exists(filepath)):
		zip = zipfile.ZipFile(filepath)
	else:
		print "File does not exist: " + filepath
		exit(1)
	
	for i in zip.infolist():
		file = i.filename.split("/")
		if (i.file_size < 1024):							#converts byte size totals into human readable sizes
			sizetitle = "bytes"
			size = str(i.file_size)
		elif (i.file_size < 1048576):
			sizetitle = "KB"
			size = format(i.file_size/float(1024),'.1f')
		elif (i.file_size < 1073741824):
			sizetitle = "MB"
			size = format(i.file_size/float(1048576),'.1f')
		else:
			sizetitle = "GB"
			size = str(format(i.file_size/float(1073741824),'.1f'))
		if (file[-1] != ""): print file[-1] + "                  " + size + sizetitle