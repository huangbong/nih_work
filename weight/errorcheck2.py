#!/usr/bin/python

import sys, random

def list_to_int(list):
        new_list = []
        for str in list:
                new_list.append(int(str))
        list = new_list
        return list

def random_gen(max):
        v1 = random.randint(0,max)
        v2 = random.randint(0,max)
        while v1 == v2:
                v1 = random.randint(0,max)
                v2 = random.randint(0,max)
        v = [v1, v2]
        return v

def error_check(file_name, max1, max2):
        f = open(file_name, 'r')
        x_row = []
        y_row = []

        for row in f:
                row = row.split()
                x_row.append(row[0])
                y_row.append(row[1])

        f.close()

        x_row = list_to_int(x_row)
        y_row = list_to_int(y_row)

        print 'Beginning error checking...'

        are_errors = False

        print 'Checking x values...'
        for x in range(max1):
                if x not in x_row:
                        print 'Warning: x empty @ %d.' % x
                        are_errors = True
                        y = random_gen(max2)
                        x_row.append(x); y_row.append(y[0]); x_row.append(x); y_row.append(y[1])
                        print 'Generated two new values for empty value %d: [%d %d], [%d %d]' % (x, x, y[0], x, y[1])
    
        print 'Checking y values...'
        for y in range(max2):
                if y not in y_row:
                        print 'Warning: y empty @ %d.' % y
                        are_errors = True
                        x = random_gen(max1)
                        y_row.append(y); x_row.append(x[0]); y_row.append(y); x_row.append(x[1])
                        print 'Generated two new values for empty value %d: [%d %d], [%d %d]' % (y, x[0], y, x[1], y)


        if are_errors == True:
                prompt = raw_input('Insert new data into file %s? (y/n) ' % file_name)
                if prompt.lower() == 'y':
                        print 'Writing...' 
                        f = open(file_name, 'w')
                        for num in range(len(x_row)):
                               f.write('%s %s\n' % (x_row[num], y_row[num]))
                        print 'File written.'
                else:
                    sys.exit('Goodbye!')
        else:
            print 'No errors found!'

        f.close()
        return