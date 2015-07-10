# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 09:34:28 2015

@author: Daniele
"""

#Euler's Totient function, φ(n) [sometimes called the phi function], is used to
#determine the number of positive numbers less than or equal to n which are
#relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less
#than nine and relatively prime to nine, φ(9)=6.
#The number 1 is considered to be relatively prime to every positive number,
#so φ(1)=1.
#
#Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation
#of 79180.
#
#Find the value of n, 1 < n < 10**7, for which φ(n) is a permutation of n and the
#ratio n/φ(n) produces a minimum.

import time
from Euler import *

primes = [i for i in sieve_erat(5000) if i > 2000]
lim = 10**7
best = 0
best_phi = 0
best_ratio = 1000000

start = time.time()

for p1 in primes:
    for p2 in [i for i in primes if i < p1]:
        n = p1*p2
        if n > lim:
            break
        phi = (p1 - 1)*(p2 - 1)
        ratio = float(n)/phi
        if is_perm(n, phi) and best_ratio > ratio:
            best = n
            best_phi = phi
            best_ratio = ratio
        
elapsed = (time.time() - start)
print best, best_phi, best_ratio, 'in %5.3f seconds' % elapsed