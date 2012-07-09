#!/usr/bin/python
# switch columns in a file

import string
import sys 

if len(sys.argv) != 2:
                sys.exit('Usage: switch.py [filename]')

file_name = sys.argv[1]
new_file_name = file_name + '.new'

print 'Switch which columns (starts at 0)?'
c_a = int(raw_input('First column: '))
c_b = int(raw_input('Second column: '))

f = open(file_name, 'r')
n = open(new_file_name, 'w')

try:
        for row in f:
                row = row.split()
		row[c_a], row[c_b] = row[c_b], row[c_a]
                final_string = ' '.join(row)
                n.write(final_string + '\n')

finally:
        n.close()
        f.close()

print 'Done! The new file is called \'%s\'.' % new_file_name
