#!/usr/bin/python
# Check three column files for missing points.

import string
import sys
import math
import random
from errorcheck3 import *

def int_input(question):
        print question
        input = int(raw_input('> '))
        return input

if len(sys.argv) != 2:
        sys.exit('Usage: weight.py [output filename]')

print 'This program will generate a three dimensional NUS table for you.'
raw_input('[Press enter to continue]')
lw1 = int_input('What is your line width in the 1st dimension?')
lw2 = int_input('What is your line width in the 2nd dimension?')
lw3 = int_input('What is your line width in the 3rd dimension?')
sw1 = int_input('What is your spectra width in the 1st dimension? (Hz)')
sw2 = int_input('What is your spectra width in the 2nd dimension? (Hz)')
sw3 = int_input('What is your spectra width in the 3rd dimension? (Hz)')
max1 = int_input('What is the maximum increment in the 1st dimension?')
max2 = int_input('What is the maximum increment in the 2nd dimension?')
max3 = int_input('What is the maximum increment in the 3rd dimension?')
nuspoints = int_input('How many NUS points do you want to have?')

while nuspoints > (max1 * max2 * max3):
        print 'Error: NUS points > (Max increment #1 * Max increment #2 * Max increment #3), please re-enter.'
        nuspoints = int_input('How many NUS points do you want to have?')

file_name = sys.argv[1]

n = open(file_name, 'w')

total_rank = []

x1 = -1 * lw1 * math.pi / sw1 
x2 = -1 * lw2 * math.pi / sw2 
x3 = -1 * lw3 * math.pi / sw3

print 'Generating data... this might take a while.'
for i in range(max1):
        for j in range(max2):
                for k in range(max3):
                        w1 = math.exp(float(i) * x1)
                        w2 = math.exp(float(j) * x2)
                        w3 = math.exp(float(k) * x3)
                        w = w1 * w2 * w3
                        rank = random.random() ** (1 / w)
                        rank_line = [i, j, k, rank]
                        total_rank.append(rank_line)
        
# sorts list by weight larger -> smaller
total_rank_sorted = sorted(total_rank, key=lambda weight: weight[3], reverse=True)

# forces [0, 0, 0] to be total_rank_sorted[0]
for pos,t in enumerate(total_rank_sorted):
        if t[0] == 0 and t[1] == 0 and t[2] == 0:
                total_rank_sorted.pop(pos)
                total_rank_sorted.insert(0, t)

print 'Writing sorted data to the file: %s' % file_name

np = 0
for data in total_rank_sorted:
        data_to_write = str(data[0]) + ' ' + str(data[1]) + ' ' + str(data[2])
        print data_to_write
        n.write(data_to_write + '\n')
        np = np + 1
        if np == nuspoints:
                break

n.close()
print 'Data successfully written to the file: ' + file_name

check = raw_input('Do you want to error check for missing rows or columns? [y/n] ')
if check.lower() == 'y':
        print 'Error checking...'
        error_check(file_name, max1, max2, max3)
else:
        exit('Goodbye!')