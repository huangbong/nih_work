#!/usr/bin/python
# add one to everything in a file

import string
import sys

if len(sys.argv) != 2:
        sys.exit('Usage: add.py [filename]')

file_name = sys.argv[1]
new_file_name = file_name + '.new'

f = open(file_name, 'r')
n = open(new_file_name, 'w')

try:
	for row in f:
		row = row.split()
		new_row = []

		for num in row:
                        num = int(num)
			num = num + 1
                        num = str(num)
			new_row.append(num)

		final_string = ' '.join(new_row)
                n.write(final_string + '\n')

finally:
	n.close()
	f.close()

print 'Done! The new file is called \'%s\'.' % new_file_name
