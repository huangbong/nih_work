#!/usr/bin/python
# check two column files for missing points

import string
import sys

if len(sys.argv) != 2:
        sys.exit('Usage: check.py [filename]')

file_name = sys.argv[1]
new_file_name = file_name + '.log'


def list_to_int(list):
        new_list = []
        for str in list:
                new_list.append(int(str))
        list = new_list
        return list

f = open(file_name, 'r')
n = open(new_file_name, 'w')

try:
        x_row = []
        y_row = []
	for row in f:
		row = row.split()
                x_row.append(row[0])
                y_row.append(row[1])

        x_row = list_to_int(x_row)
        y_row = list_to_int(y_row)
        
        print 'Sorted x list:'
        print sorted(x_row)
        print 'Sorted y list:'
        print sorted(y_row)

        print 'Min x number:', min(x_row)
        print 'Max x number:', max(x_row)
        print 'Min y number:', min(y_row)
        print 'Max y number:', max(y_row)

        print 'Beginning error checking...'

        print '##### Checking x values... #####'
        for x in range(min(x_row), max(x_row)+1):
                if x_row.count(x) == 0:
                        warning = 'Warning! Empty at x = ' + str(x)
                        print warning
                        n.write(warning + '\n')
                        
        print '##### Checking y values... #####'
        for y in range(min(y_row), max(y_row)+1):
                if y_row.count(y) == 0:
                        warning = 'Warning! Empty at y = ' + str(y)
                        print warning
                        n.write(warning + '\n')


finally:
	n.close()
	f.close()

print 'Log file created. \'%s\'' % new_file_name
