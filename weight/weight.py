#!/usr/bin/python
# assigns random weight based on math to points in a 2 column file

import string
import sys
import math
import random

if len(sys.argv) != 2:
        sys.exit('Usage: weight.py [filename]')

lw1 = int(raw_input('What is your line width in the 1st dimension? '))
lw2 = int(raw_input('What is your line width in the 2nd dimension? '))
sw1 = int(raw_input('What is your spectra width in the 1st dimension? '))
sw2 = int(raw_input('What is your spectra width in the 2nd dimension? '))

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
        total_row = []
        total_rank = []
	
        for row in f:
		row = row.split()
                total_row.append(row)
        
        x1 = -1 * lw1 * math.pi / sw1
        x2 = -1 * lw2 * math.pi / sw2

        for x in range(len(total_row)):
                w1 = math.exp(float(total_row[x][0]) * x1)
                w2 = math.exp(float(total_row[x][1]) * x2)
                w = w1 * w2
                rank = random.random() ** (1 / w)
                rank_line = [total_row[x][0], total_row[x][1], rank]
                total_rank.append(rank_line) 

        print 'Data | Weight' 
        for data in total_rank:
                line = str(data[0]) + ' ' + str(data[1]) + ' | ' + str(data[2])
                print line
                n.write(line + '\n')

finally:
	f.close()
        n.close()