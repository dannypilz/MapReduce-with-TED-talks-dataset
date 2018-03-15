#!/usr/bin/env python

from operator import itemgetter
import sys

current_year = None
current_count = 0
current_tag = None
year = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    year, count = line.split('\t\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: year) before it is passed to the reducer

    if current_year == year:
            current_count += count
    else:
            if current_year:
            # write result to STDOUT
                 Hilfsarray = current_year.split("+")
                 current_year = Hilfsarray[0]
                 current_tag = Hilfsarray[1]
                 print '%s;\t%s;\t%s' % (current_year, current_tag, current_count)
            current_count = count
            current_year = year

# do not forget to output the last year if needed!
if current_year == year:
        Hilfsarray = current_year.split("+")
        current_year = Hilfsarray[0]
        current_tag = Hilfsarray[1]
        print '%s;\t%s;\t%s' % (current_year, current_tag, current_count)
