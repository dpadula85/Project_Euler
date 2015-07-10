# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 15:32:41 2015

@author: Daniele
"""

#Starting with 1 and spiralling anticlockwise in the following way, a square
#spiral with side length 7 is formed.
#
#37 36 35 34 33 32 31
#38 17 16 15 14 13 30
#39 18  5  4  3 12 29
#40 19  6  1  2 11 28
#41 20  7  8  9 10 27
#42 21 22 23 24 25 26
#43 44 45 46 47 48 49
#
#It is interesting to note that the odd squares lie along the bottom right
#diagonal, but what is more interesting is that 8 out of the 13 numbers lying
#along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.
#
#If one complete new layer is wrapped around the spiral above, a square spiral
#with side length 9 will be formed. If this process is continued, what is the
#side length of the square spiral for which the ratio of primes along both
#diagonals first falls below 10%?
#
#Ulam Spiral diagonal numbers already treated in problem 28.
#Rearrange the problem to solve this one.

import time
from Euler import *

sq = 1000000    #limit side, big enough to reach the desired ratio
d = 1
diag_nums = []
diag_primes = []

start = time.time()

while 2*d - 1 < sq:
    d1 = 4 * d * d - 4 * d + 1
    d2 = 4 * d * d - 4 * d + 1 + 1 * 2 * d
    d3 = 4 * d * d - 4 * d + 1 + 2 * 2 * d
    d4 = 4 * d * d - 4 * d + 1 + 3 * 2 * d
    diag_nums = diag_nums + [d1, d2, d3, d4]
    diag_primes = diag_primes + filter(is_prime, [d1, d2, d3, d4])
    ratio = len(diag_primes) / float(len(diag_nums))
    if ratio < 0.1:
        break
    
    d = d + 1
    
print ratio
print 2*d - 1

elapsed = (time.time() - start)
print 'in %5.3f seconds' % elapsed 