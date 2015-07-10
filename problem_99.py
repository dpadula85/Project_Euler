# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 16:11:38 2015

@author: Daniele
"""

#Comparing two numbers written in index form like 211 and 37 is not difficult,
#as any calculator would confirm that 211 = 2048 < 37 = 2187.
#
#However, confirming that 632382**518061 > 519432**525806 would be much more
#difficult, as both numbers contain over three million digits.
#
#Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file
#containing one thousand lines with a base/exponent pair on each line,
#determine which line number has the greatest numerical value.
#
#NOTE: The first two lines in the file represent the numbers in the example
#given above.
#
#Solve as multiplication upon passing to logarithms

import time
from math import log

path = 'C:\\Users\\Daniele\\Desktop\\python_practice\\project_Euler\\'
file_words = 'problem_99.txt'
f = open(path + file_words, 'r').read().split('\n')
pairs = [tuple(pair.split(',')) for pair in f]

max_n = 0
idx = 0
for pair in pairs:
    num = int(pair[1]) * log(int(pair[0]))
    if num > max_n:
        max_n = num
        idx = pairs.index(pair) + 1
        
print max_n, idx
    