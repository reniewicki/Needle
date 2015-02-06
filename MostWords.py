#!/usr/bin/env python
# coding=utf-8

import codecs, os.path, sys, re, shutil, time, getpass, os, distutils

reload(sys)
sys.setdefaultencoding('utf-8')

def ReadInFile(file):						#reads from file, returns a generator of words that were seperated by white-space
	try:
		f = codecs.open(file, 'r', 'utf-8')
		lines = f.readlines()
		f.close
		for line in lines:
			for word in line.split():
				yield word
	except IOError as (errno, strerror):
		print "I/O error({0}): {1}".format(errno, strerror)
	except ValueError:
		print "Could not convert data to an integer."
	except:
		print "Unexpected error:", sys.exc_info()[0]
		raise

def ParseFile(file):
	words = {}
	word_count = {}
	for word in file:
		word = re.sub(r'[\W]', r"", word).lower()		#normalizes words, removing non-alpha/non-numeric characters and lower-casing
		if (not word in words):							#creates list of words 
			words[word] = ""
			word_count[word] = 0
		word_count[word] += 1							#creates list of running totals or words
	highest = 0
	for iword in words:
		if (word_count[iword] > highest):
			highest = word_count[iword]
			highestword = iword
	return "The word: " + highestword + "\nAppears the most number of times with a count of " + str(word_count[highestword])
	
	
if __name__ == "__main__":

	if (len(sys.argv) != 2):
		print len(sys.argv)
		print "Usage: MostWords.py <filepath>"
		print "  Parses the file and returns most common word and times used"
		exit(1)
	
	
	filepath = sys.argv[1]
	if (os.path.exists(filepath)):
		wordlist = ReadInFile(filepath)
	else:
		print "File does not exist: " + filepath
		exit(1)
		
	print ParseFile(wordlist)