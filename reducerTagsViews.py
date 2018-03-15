#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
current_views = 0
current_viewProportion = 0
word = None

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	# parse the input we got from mapper.py
	word, count, views, viewProportion = line.split('\t', 3)

	# convert count (currently a string) to int
	try:
		count = int(count)
		views = int(views)
		viewProportion = int(viewProportion)
	except ValueError:
		# count was not a number, so silently
		# ignore/discard this line
		continue

	# this IF-switch only works because Hadoop sorts map output
	# by key (here: word) before it is passed to the reducer
	if current_word == word:
		current_count += count
		current_views += views
		current_viewProportion += viewProportion
	else:
		if current_word:
			# write result to STDOUT
			print '%s\t\t%s\t\t%s\t\t%s' % (current_word, current_count, current_views, current_viewProportion)
		current_count = count
		current_word = word
		current_views = views
		current_viewProportion = viewProportion

# do not forget to output the last word if needed!
if current_word == word:
	print '%s\t\t%s\t\t%s\t\t%s' % (current_word, current_count, current_views, current_viewProportion)
