# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 10:56:02 2015

@author: Daniele
"""

#Consider the fraction, n/d, where n and d are positive integers. If n<d and
#HCF(n,d)=1, it is called a reduced proper fraction.
#
#If we list the set of reduced proper fractions for d ≤ 8 in ascending order of
#size, we get:
#
#1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7,
#3/4, 4/5, 5/6, 6/7, 7/8
#
#It can be seen that 2/5 is the fraction immediately to the left of 3/7.
#
#By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending
#order of size, find the numerator of the fraction immediately to the left
#of 3/7.

import time

lim = 10**6
a = 3
b = 7
r = 0
s = 1

start = time.time()

for q in xrange(1, 10**6):
    p = int((a*q - 1)/b)
    if r*q < p*s:
        r = p
        s = q

elapsed = (time.time() - start)        
print r, 'in %5.3f seconds' % elapsed