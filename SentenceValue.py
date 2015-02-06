#!/usr/bin/env python
# coding=utf-8

import codecs, os.path, sys, re, shutil, time, getpass, os, distutils, zipfile

reload(sys)
sys.setdefaultencoding('utf-8')

def ReadInFile(file):												#Reads text from file, returns a list of sentences, separated by periods and white-space
	try:
		f = codecs.open(file, 'r', 'utf-8')
		text = f.read()
		f.close
		return re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
	except IOError as (errno, strerror):
		print "I/O error({0}): {1}".format(errno, strerror)
	except ValueError:
		print "Could not convert data to an integer."
	except:
		print "Unexpected error:", sys.exc_info()[0]
		raise
	
if __name__ == "__main__":

	if (len(sys.argv) != 2):
			print len(sys.argv)
			print "Usage: SentenceValue.py <filepath>"
			print "  Translate sentences in vaules, based on letter values (1-26).\nReturns highest value sentence."
			exit(1)
	filepath = sys.argv[1]
	alphalist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	sentences = ReadInFile(filepath)
	sentence_totals = []
	for sent in sentences:
		norm_sent = re.sub(r'[\W\d]', r"", sent).lower()			#normalizes the sentence by removing non-alpha characters
		total = 0
		for i in range(len(norm_sent)):								#creates list of sentence totals in corresponding order of the sentence list
			total += (alphalist.index(norm_sent[i]) + 1)
		sentence_totals.append(total)
	print "With a value of " + str(max(sentence_totals)) + " The highest valued sentence is:\n"
	print sentences[sentence_totals.index(max(sentence_totals))].encode('utf-8')		#Since both lists correspond, prints the max valued sentence based on the index of the max value list
		
		