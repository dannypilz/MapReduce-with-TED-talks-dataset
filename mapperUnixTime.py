#!/usr/bin/env python

import sys
import datetime

# input comes from STDIN (standard input)
for line in sys.stdin:
  
    # remove leading and trailing whitespace
    line = line.strip()

    # split the line into columns
    columns = line.split(";")

    # Unix Time convert
    #try if float is accepted, else continue
    try:
          unix = float(columns[4])
    except:
          continue
    
    #replace an split for single tags
    tag = columns[11].replace("[","").replace("]","").replace("'","")
    tags = tag.split(", ")

    #output: combination of the year and the tag
    for x in tags:
      key = datetime.datetime.fromtimestamp(unix).strftime('%Y') + "+" +  x
      print '%s\t\t%s' % (key, str(1))
    