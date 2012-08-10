#!/usr/bin/python
# Check two column files for missing points.

import string, sys, math, random

def int_input(question):
    print question
    input = int(raw_input('> '))
    return input

def get_input():
    global lw1, lw2, sw1, sw2, max1, max2, nuspoints
    lw1 = int_input('What is your line width in the 1st indirect dimension? (Hz)')
    lw2 = int_input('What is your line width in the 2nd indirect dimension? (Hz)')
    sw1 = int_input('What is your spectra width in the 1st indirect dimension? (Hz)')
    sw2 = int_input('What is your spectra width in the 2nd indirect dimension? (Hz)')
    max1 = int_input('What is the maximum increment in the 1st indirect dimension?')
    max2 = int_input('What is the maximum increment in the 2nd indirect dimension?')
    print "%s * %s = %s possible points." % (max1, max2, max1*max2)
    nuspoints = int_input('How many NUS points do you want to have?')
    while nuspoints > (max1 * max2):
        print 'Error: NUS points > (Max increment #1 * Max increment #2), please re-enter.'
        nuspoints = int_input('How many NUS points do you want to have?')

def generate_data():
    global total_rank
    x1 = -1 * lw1 * math.pi / sw1 
    x2 = -1 * lw2 * math.pi / sw2
    total_rank = []
    for i in range(max1):
        for j in range(max2):
            w1 = math.exp(float(i) * x1)
            w2 = math.exp(float(j) * x2)
            w = w1 * w2
            weight = random.random() ** (1 / w)
            total_rank.append([i, j, weight])
        
def sort_data_by_weight():
    # sorts list by weight descending
    global total_rank_sorted
    total_rank_sorted = sorted(total_rank, key=lambda weight: weight[2], reverse=True)

def force_initial_line():
    # forces [0, 0, 0] to be total_rank_sorted[0]
    for pos,t in enumerate(total_rank_sorted):
        if t[0] == 0 and t[1] == 0:
            total_rank_sorted.pop(pos)
            total_rank_sorted.insert(0, t)

def write_to_file():
    f = open(file_name, 'w')
    np_counter = 0
    for data in total_rank_sorted:
        f.write('%s %s\n' % (data[0], data[1]))
        np_counter = np_counter + 1
        if np_counter == nuspoints:
            break
    f.close()

def ask_errorcheck():
    check = raw_input('Do you want to error check for missing rows or columns? [y/n] ')
    if check.lower() == 'y':
        print 'Error checking...'
        error_check(file_name, max1, max2)
    else:
        sys.exit('Goodbye!')

def main():
    print '''#########################################################################
#### This program will generate a two dimensional NUS table for you. ####
#########################################################################'''
    get_input()
    print 'Generating data... this might take a while.'
    generate_data()
    sort_data_by_weight()
    force_initial_line()
    print 'Writing sorted data to the file: %s' % file_name
    write_to_file()
    print 'Data successfully written to the file: %s' % file_name

if len(sys.argv) != 2:
    sys.exit('Usage: weight2.py [output filename]')

file_name = sys.argv[1]

if __name__ == '__main__':
    main()