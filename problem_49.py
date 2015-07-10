# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:55:11 2015

@author: Daniele
"""

#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
#increases by 3330, is unusual in two ways:
#(i) each of the three terms are prime
#(ii) each of the 4-digit numbers are permutations of one another.
#
#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
#exhibiting this property, but there is one other 4-digit increasing sequence.
#
#What 12-digit number do you form by concatenating the three terms in this
#sequence?
#
#Generate all 4-digit primes. Remove the ones containing zeros.
#Choose p1, p2 from the list, p2 > p1
#p3 = p2 + (p2 - p1) < 10000 (or in the list of primes)
#if p3 is permutation of p2, and p2 is permutation of p1, we got our triple.

import time
from itertools import permutations
from Euler import *

primes = sieve_erat(10000)
primes_4d = filter(lambda x: '0' not in str(x), filter(lambda x: x > 1000, primes))

start = time.time()

seqs = []

for p1 in primes_4d:
    for p2 in filter(lambda x: x > p1, primes_4d):
        p3 = p2 * 2 - p1
        if p3 in primes_4d and is_perm(p1, p2) and is_perm(p3, p1):
            seq = tuple(sorted((p1, p2, p3)))
            if seq not in seqs:            
                seqs.append(seq)

elapsed = (time.time() - start)            
print seqs, 'in %5.3f seconds' % elapsed 
    
    