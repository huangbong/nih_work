#!/usr/bin/python
import math
for x in range(0, 41):
	y = math.cos(x) * math.exp(-x/100)
	print "%s %s" % (x, y)