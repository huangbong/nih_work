#!/usr/bin/python
import math, random
def generate_data(lw1, lw2, lw3, sw1, sw2, sw3, max1, max2, max3):
    x1 = -1 * lw1 * math.pi / sw1 
    x2 = -1 * lw2 * math.pi / sw2 
    x3 = -1 * lw3 * math.pi / sw3
    for i in range(max1):
        for j in range(max2):
            for k in range(max3):
                w = math.exp(i * x1) * math.exp(j * x2) * math.exp(k * x3)
                weight = random.random() ** (1 / w)
                print "%s %s" % (weight, random.random())

generate_data(10, 20, 30, 1000, 2000, 3000, 10, 10, 10)