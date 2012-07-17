#!/usr/bin/python
# Generate pseduo y table

import sys, random

def list_to_int(list):
        new_list = []
        for str in list:
                new_list.append(int(str))
        list = new_list
        return list

def random_gen_num(a, b):
		v1 = random.randint(a,b-1)
		v2 = random.randint(a,b-1)
		while v1 == v2:
		        v1 = random.randint(a,b-1)
		        v2 = random.randint(a,b-1)
		v = [v1, v2]
		return v

def create_rows():
	global x_row, y_row, z_row
	n = open(file_name, 'r')
	x_row = []; y_row = []; z_row = []
	for row in n:
	        row = row.split()
	        x_row.append(row[0])
	        y_row.append(row[1])
	        z_row.append(row[2])
	n.close()
	x_row = list_to_int(x_row); y_row = list_to_int(y_row); z_row = list_to_int(z_row)

def create_pseudoy():
	global pseudoy_row
	pseudoy_row = []
	for num in range(0, len(x_row)):
		i = y_row[num]
		j = z_row[num]
		pseudoy_row.append(j*max2+i)

def check_pseudoy():
	for x in range(min(x_row), max(x_row)+1):
		if x not in x_row:
			print 'x error at %s' % x

	for pseudoy in range(min(pseudoy_row), max(pseudoy_row)+1):
		if pseudoy not in pseudoy_row:
			print 'pseudoy error at %s' % pseudoy

def fix_pseudoy():
	for i in range(max2):
		for j in range(max3):
			num = j * max2 + i
			if num not in pseudoy_row:
				randlist = random_gen_num(0, max3)
				print randlist
				n = open(file_name, 'a')
				n.write('%s %s %s\n' % (randlist[0], i, j))
				n.write('%s %s %s\n' % (randlist[1], i, j))
				n.close

def main():
	create_rows()
	create_pseudoy()
	check_pseudoy()
	print 'fixing pseudoy...'
	fix_pseudoy()

# Actually run the program.

if len(sys.argv) < 4:
		sys.exit('Usage: pseudoy.py [input file] [max2] [max3]')

file_name = sys.argv[1]
max2 = int(sys.argv[2])
max3 = int(sys.argv[3])

if __name__ == "__main__":
	main()