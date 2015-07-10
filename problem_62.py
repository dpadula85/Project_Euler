# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:36:48 2015

@author: Daniele
"""

#The cube, 41063625 (345**3), can be permuted to produce two other cubes:
#56623104 (384**3) and 66430125 (405**3). In fact, 41063625 is the smallest
#cube which has exactly three permutations of its digits which are also cube.
#
#Find the smallest cube for which exactly five permutations of its digits are
#cube.
#
#Collect permutations of cubes into a dictionary. Get the permutations for
#which frequency = 5.
#Get the keys associated with such permutations and find the minimum.

import time
from Euler import *
from collections import Counter

def perm(n):
    return ''.join(sorted(str(n)))

start = time.time()

cubes = [i**3 for i in range(0, 10000)]
cubes_perm = {}

for cube in cubes:
    cubes_perm[cube] = perm(cube)

freq_cbs = []
    
for val, freq in Counter(cubes_perm.values()).most_common():
    if freq == 5:
        freq_cbs.append(val)
        
sols = []

for cub in freq_cbs:
    for k, v in cubes_perm.items():
        if v == cub:
            sols.append(k)
            
elapsed = (time.time() - start)
print min(sols), 'in %5.3f seconds' % elapsed