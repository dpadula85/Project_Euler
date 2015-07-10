# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 09:54:32 2015

@author: Daniele
"""

#It was proposed by Christian Goldbach that every odd composite number can be
#written as the sum of a prime and twice a square.
#
#9 = 7 + 2×1**2
#15 = 7 + 2×2**2
#21 = 3 + 2×3**2
#25 = 7 + 2×3**2
#27 = 19 + 2×2**2
#33 = 31 + 2×1**2
#
#It turns out that the conjecture was false.
#
#What is the smallest odd composite that cannot be written as the sum of a
#prime and twice a square?
#
#generate a list of primes. Check if odd - prime is 2*square

import time
from Euler import *
from math import sqrt
import itertools

start = time.time()

n = 10000    #upper limit of our analysis
comp_odds = itertools.ifilterfalse(is_prime, range(9, n)[::2])
primes = sieve_erat(n)[1:]

for odd in comp_odds:
    #we have to check only primes < odd for the difference
    diffs = []
    for prime in filter(lambda x: x < odd, primes):
        diff = odd - prime
        diffs.append(diff)        
    if not any([sqrt(d/2).is_integer() for d in diffs]):
        print odd           
        break
    
elapsed = (time.time() - start)
print 'in %5.3f seconds' % elapsed