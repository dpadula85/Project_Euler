# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 13:04:18 2015

@author: Daniele
"""

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#Find the sum of all the primes below two million.

import time
from Euler import *
  
start = time.time()

sum_primes = sum(sieve_erat(2000000))

elapsed = (time.time() - start)
print sum_primes
print 'in %5.3f seconds' % elapsed