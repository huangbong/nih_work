#!/usr/bin/python

import random

def list_to_int(list):
        new_list = []
        for str in list:
                new_list.append(int(str))
        list = new_list
        return list

def random_gen_v(a, b):
        v1 = random.randint(a,b-1)
        v2 = random.randint(a,b-1)
        while v1 == v2:
                v1 = random.randint(a,b-1)
                v2 = random.randint(a,b-1)
        v = [v1, v2]
        return v

def error_check(file_name):
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
    
        print 'Min x number:', min(x_row)
        print 'Max x number:', max(x_row)
        print 'Min y number:', min(y_row)
        print 'Max y number:', max(y_row)
        print 'Max z number:', max(z_row)
        print 'Max z number:', max(z_row)

        print 'Beginning error checking...'

        are_errors = False

        print 'Checking x values...'
        for x in range(min(x_row), max(x_row)+1):
                if x not in x_row:
                        print 'Warning: x empty @ %d.' % x
                        are_errors = True
                        y = random_gen_v(min(y_row),max(y_row))
                        z = random_gen_v(min(z_row),max(z_row))
                        x_row.append(x); y_row.append(y[0]); z_row.append(z[0]); \
                        x_row.append(x); y_row.append(y[1]); z_row.append(z[1])
                        print 'Generated two new values for empty value %d: [%d %d %d], [%d %d %d]' \
                        % (x, x, y[0], z[0], x, y[1], z[1])
    
        print 'Checking y values...'
        for y in range(min(y_row), max(y_row)+1):
                if y not in y_row:
                        print 'Warning: y empty @ %d.' % y
                        are_errors = True
                        x = random_gen_v(min(x_row), max(x_row))
                        z = random_gen_v(min(z_row),max(z_row))
                        y_row.append(y); x_row.append(x[0]); z_row.append(z[0]); \
                        y_row.append(y); x_row.append(x[1]); z_row.append(z[1])
                        print 'Generated two new values for empty value %d: [%d %d %d], [%d %d %d]' \
                        % (y, x[0], y, z[0], x[1], y, z[1])

        print 'Checking z values...'
        for z in range(min(z_row), max(z_row)+1):
                if z not in z_row:
                        print 'Warning: z empty @ %d.' % z
                        are_errors = True
                        x = random_gen_v(min(x_row), max(x_row))
                        y = random_gen_v(min(y_row),max(y_row))
                        z_row.append(z); x_row.append(x[0]); y_row.append(y[0]); \
                        z_row.append(z); x_row.append(x[1]); y_row.append(y[1])
                        print 'Generated two new values for empty value %d: [%d %d %d], [%d %d %d]' \
                        % (z, x[0], y[0], z, x[1], y[1], z)

        if are_errors == True:
                prompt = raw_input('Insert new data into file %s? (y/n) ' % file_name)
                if prompt.lower() == 'y':
                        print 'Writing...' 
                        f = open(file_name, 'w')
                        for num in range(len(x_row)):
                               f.write(str(x_row[num]) + ' ' + str(y_row[num]) + ' ' + str(z_row[num]) + '\n')
                        print 'File written.'
                else:
                    exit('Goodbye!')
        else:
            print 'No errors found!'

        f.close()
        return