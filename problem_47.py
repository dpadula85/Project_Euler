# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:12:21 2015

@author: Daniele
"""

#The first two consecutive numbers to have two distinct prime factors are:
#
#14 = 2 × 7
#15 = 3 × 5
#
#The first three consecutive numbers to have three distinct prime factors are:
#
#644 = 2² × 7 × 23
#645 = 3 × 5 × 43
#646 = 2 × 17 × 19.
#
#Find the first four consecutive integers to have four distinct prime factors.
#What is the first of these numbers?
#
#Start from the first number to have 4 factors.
#Run through numbers and factorize them. If there are less then 4 factors,
#go on.

import time
from Euler import *

#Determine the first number with 4 different prime factors: 210
#for i in range(1000):
#    facs = factorize(i)
#    if len(facs) == 4:
#        print i
#        break

start = time.time()

n = 210
num_f = 4
num_i = 4

facs = []

count = 0
while count < num_i:
    n += 1
    factors = factorize(n)
    if len(factors) == num_f:
        prime_facs = [i[0] for i in factors]
        if prime_facs not in facs:
            facs.append(prime_facs)
            count += 1
    else:
        count = 0
        facs = []
        
for j in range(num_i):
    print n - j,

elapsed = (time.time() - start)            
print 'in %5.3f seconds' % elapsed 