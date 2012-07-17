#!/usr/bin/python
# Generate and check 3D tables

import string, sys, math, random
from errorcheck3 import *

def int_input(question):
        print question
        input = int(raw_input('> '))
        return input

def get_input():
        global lw1, lw2, lw3, sw1, sw2, sw3, max1, max2, max3, nuspoints
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

def generate_data():
        # total_rank is all the __unsorted__ randomly generated data with it's weight
        global total_rank
        total_rank = []
        x1 = -1 * lw1 * math.pi / sw1 
        x2 = -1 * lw2 * math.pi / sw2 
        x3 = -1 * lw3 * math.pi / sw3
        for i in range(max1):
                for j in range(max2):
                        for k in range(max3):
                                w1 = math.exp(float(i) * x1)
                                w2 = math.exp(float(j) * x2)
                                w3 = math.exp(float(k) * x3)
                                w = w1 * w2 * w3
                                weight = random.random() ** (1 / w)
                                total_rank.append([i, j, k, weight])

def sort_data_by_weight():
        # total_rank_sorted is all the data sorted by weight in reverse
        global total_rank_sorted
        total_rank_sorted = sorted(total_rank, key=lambda weight: weight[3], reverse=True)

def force_initial_line():
        # this forces 0 0 0 to be the first line in the table
        for pos,t in enumerate(total_rank_sorted):
                if t[0] == 0 and t[1] == 0 and t[2] == 0:
                        total_rank_sorted.pop(pos)
                        total_rank_sorted.insert(0, t)

def write_to_file():
        f = open(file_name, 'w')
        np_counter = 0
        for data in total_rank_sorted:
                f.write('%s %s %s\n' % (data[0], data[1], data[2]))
                np_counter += 1
                if np_counter == nuspoints:
                        break
        f.close()

def ask_errorcheck():
        check = raw_input('Do you want to error check for missing data? (y/n) ')
        if check.lower() == 'y':
                print 'Error checking...'
                error_check(file_name, max1, max2, max3)
        else:
                sys.exit('Goodbye!')

def main():
        print '''###########################################################################
#### This program will generate a three dimensional NUS table for you. ####
###########################################################################'''
        get_input()
        print 'Generating data... this might take a while.'
        generate_data()
        sort_data_by_weight()
        force_initial_line()
        print 'Writing sorted data to the file: %s' % file_name
        write_to_file()
        print 'Data successfully written to the file: %s' % file_name
        ask_errorcheck()

if len(sys.argv) != 2:
        sys.exit('Usage: weight.py [output filename]')

file_name = sys.argv[1]

if __name__ == '__main__':
        main()