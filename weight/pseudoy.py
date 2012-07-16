#!/usr/bin/python
# Generate pseduo y table

import sys

def list_to_int(list):
        new_list = []
        for str in list:
                new_list.append(int(str))
        list = new_list
        return list

if len(sys.argv) < 3:
		sys.exit('Usage: pseudoy.py [input file] [max2] [output file]')

file_name = sys.argv[1]
max2 = int(sys.argv[2])

n = open(file_name, 'r')

x_row = []
y_row = []
z_row = []
py_row = []

for row in n:
        row = row.split()
        x_row.append(row[0])
        y_row.append(row[1])
        z_row.append(row[2])

n.close()

x_row = list_to_int(x_row)
y_row = list_to_int(y_row)
z_row = list_to_int(z_row)

for num in range(0, len(x_row)):
	i = y_row[num]
	j = z_row[num]
	py_row.append(j*max2+i)

print x_row
print y_row
print z_row
print py_row

for x in range(min(x_row), max(x_row)+1):
	if x not in x_row:
		print 'XBAD'

for py in range(min(py_row), max(py_row)+1):
	if py not in py_row:
		print 'PYBAD'