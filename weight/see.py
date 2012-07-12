#!/usr/bin/python

import sys

if len(sys.argv) != 2:
	sys.exit('Usage: see.py [filename]')

file_name = sys.argv[1]

f = open(file_name, 'r')

x_row = []
y_row = []
z_row = []

for row in f:
        row = row.split()
        x_row.append(row[0])
        y_row.append(row[1])
        z_row.append(row[2])

print 'XZ'
for num in range(0, len(y_row)):
	print x_row[num] + ' ' + z_row[num]

f.close()