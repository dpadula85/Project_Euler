# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:13:47 2015

@author: Daniele
"""

#The first known prime found to exceed one million digits was discovered in
#1999, and is a Mersenne prime of the form 26972593−1; it contains exactly
#2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have
#been found which contain more digits.
#
#However, in 2004 there was found a massive non-Mersenne prime which contains
#2,357,207 digits: 28433×2**7830457+1.
#
#Find the last ten digits of this prime number.

import time

start = time.time()

n = 1
lim = 7830457
i = 0
while i < lim:
    n = 2*n % 10000000000
    i += 1
    
n *= 28433
n += 1
elapsed = (time.time() - start)        
print n % 10000000000, 'in %5.3f seconds' % elapsed