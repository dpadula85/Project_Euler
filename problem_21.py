# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 08:54:46 2015

@author: Daniele
"""

#Let d(n) be defined as the sum of proper divisors of n (numbers less than n
#which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
#each of a and b are called amicable numbers.
#
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
#and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
#and 142; so d(284) = 220.
#
#Evaluate the sum of all the amicable numbers under 10000.

import time
import itertools
from Euler import *

def amicable(x, y):
    return x != y and sum(divs(x)[:-1]) == y and sum(divs(y)[:-1]) == x

amicables = []
        
start = time.time()        
       
for m in range(10000):
    n = sum(divs(m)[:-1])
    if m != n and amicable(m, n) and tuple(sorted((m, n))) not in amicables:
        amicables.append(tuple(sorted((m, n))))
            
flat_ami = list(itertools.chain.from_iterable(amicables))

elapsed = (time.time() - start)

print sum(flat_ami), 'in %5.3f seconds' % elapsed         