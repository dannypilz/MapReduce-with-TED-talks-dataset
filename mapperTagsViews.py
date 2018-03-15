#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:

	# remove leading and trailing whitespace
	line = line.strip()
	
	# split the line into words (german csv)
	columns = line.split(";")

	#split in single tags
	tag = columns[11].replace("['","'").replace("']","'").split("', '")
	tagNumber = int(len(tag) + 1)

	#for word in tag: tag, 1, view number, view propotion
	for x in range(0, len(tag)-1):
		print '%s\t%s\t%s\t%s' % (str(tag[x].replace("'","")), str(1), columns[13], str(int(columns[13])/tagNumber))