#!/usr/bin/python
import math
for x in range(0, 41):

	y = math.cos(x) * math.exp(-float(x)/30)
	print "%s %s" % (x, y)