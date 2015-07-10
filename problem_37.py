# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 16:53:27 2015

@author: Daniele
"""

#The number 3797 has an interesting property. Being prime itself,
#it is possible to continuously remove digits from left to right,
#and remain prime at each stage: 3797, 797, 97, and 7.
#Similarly we can work from right to left: 3797, 379, 37, and 3.
#
#Find the sum of the only eleven primes that are both truncatable from left
#to right and right to left.
#
#NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
#
#result should be 23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397

import time
from Euler import *

def trunc(n):
    truncated = []
    for i in range(len(str(n))):
        truncated_l = str(n)[i:]
        truncated_r = str(n)[:-i]
        if truncated_l not in truncated:
            truncated.append(truncated_l)
        if truncated_r not in truncated:
            truncated.append(truncated_r)
    
    return sorted(map(int, filter(None, truncated)))
    

start = time.time()

primes = sieve_erat(1000000)

p_trunc = []
count = 0
while True:
    for prime in filter(lambda x: x > 10, primes):
        if len(p_trunc) == 11:
            break
        if all(map(is_prime, trunc(prime))):
            p_trunc.append(prime)
    break


elapsed = (time.time() - start)            
print p_trunc, len(p_trunc), '\n', sum(p_trunc),'in %5.3f seconds' % elapsed 