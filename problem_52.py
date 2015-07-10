# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 13:57:53 2015

@author: Daniele
"""

#It can be seen that the number, 125874, and its double, 251748, contain
#exactly the same digits, but in a different order.
#
#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
#contain the same digits.
#
#x and 6*x contain the same number of digits.
#If d is the number of digits of n, we could look into the numbers between
#smaller than n* 10**d / 6
#For each of these numbers, generate the multiples and check that they are
#permutations of each other.

import time
from Euler import *

start = time.time()

n = 10

while True:
    d = len(str(n))
    if n <= n* 10**d / 6:
        n_mults = [n * i for i in range(1, 7)]    
        if all([is_perm(n, x) for x in n_mults]):
            break
    n += 1

elapsed = (time.time() - start)
print n, 'in %5.3f seconds' % elapsed