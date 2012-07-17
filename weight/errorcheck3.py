#!/usr/bin/python
# Errorcheck 3D NUS tables

import sys, random

def list_to_int(list):
    new_list = []
    for str in list:
        new_list.append(int(str))
    return new_list

def random_gen(max):
    v1 = random.randint(0,max)
    v2 = random.randint(0,max)
    while v1 == v2:
        v1 = random.randint(0,max)
        v2 = random.randint(0,max)
    v = [v1, v2]
    return v

def read_file(file_name):
    global x_row, y_row, z_row

    f = open(file_name, 'r')

    x_row = []
    y_row = []
    z_row = []

    for row in f:
        row = row.split()
        x_row.append(row[0])
        y_row.append(row[1])
        z_row.append(row[2])

    f.close()

    x_row = list_to_int(x_row)
    y_row = list_to_int(y_row)
    z_row = list_to_int(z_row)

def check_x(max1, max2, max3):
    global are_errors
    for x in range(max1):
        if x not in x_row:
            print 'Warning: x empty at %d.' % x
            are_errors = True
            y = random_gen(max2)
            z = random_gen(max3)
            x_row.append(x); y_row.append(y[0]); z_row.append(z[0]); \
            x_row.append(x); y_row.append(y[1]); z_row.append(z[1])
            print 'Generated two new values for empty value %d: [%d %d %d], [%d %d %d]' \
            % (x, x, y[0], z[0], x, y[1], z[1])

def check_y(max1, max2, max3):
    global are_errors
    for y in range(max2):
        if y not in y_row:
            print 'Warning: y empty at %d.' % y
            are_errors = True
            x = random_gen(max1)
            z = random_gen(max3)
            y_row.append(y); x_row.append(x[0]); z_row.append(z[0]); \
            y_row.append(y); x_row.append(x[1]); z_row.append(z[1])
            print 'Generated two new values for empty value %d: [%d %d %d], [%d %d %d]' \
            % (y, x[0], y, z[0], x[1], y, z[1])

def check_z(max1, max2, max3):
    global are_errors
    for z in range(max3):
        if z not in z_row:
            print 'Warning: z empty at %d.' % z
            are_errors = True
            x = random_gen(max1)
            y = random_gen(max2)
            z_row.append(z); x_row.append(x[0]); y_row.append(y[0]); \
            z_row.append(z); x_row.append(x[1]); y_row.append(y[1])
            print 'Generated two new values for empty value %d: [%d %d %d], [%d %d %d]' \
            % (z, x[0], y[0], z, x[1], y[1], z)

def error_check(file_name, max1, max2, max3):
    print 'Beginning error checking...'
    read_file(file_name)

    global are_errors
    are_errors = False

    print 'Checking x values...'
    check_x(max1, max2, max3)

    print 'Checking y values...'
    check_y(max1, max2, max3)

    print 'Checking z values...'
    check_z(max1, max2, max3)

    if are_errors == True:
        prompt = raw_input('Insert new data into file %s? (y/n) ' % file_name)
        if prompt.lower() == 'y':
            print 'Writing...' 
            f = open(file_name, 'w')
            for num in range(len(x_row)):
                f.write('%s %s %s\n' % (x_row[num], y_row[num], z_row[num]))
            f.close()
            print 'File written.'
        else:
            sys.exit('Goodbye!')
    else:
        print 'No errors found!'

    return