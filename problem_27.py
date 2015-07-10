# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 15:38:22 2015

@author: Daniele
"""

#Euler discovered the remarkable quadratic formula:
#
#n² + n + 41
#
#It turns out that the formula will produce 40 primes for the consecutive
#values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41
#is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly
#divisible by 41.
#
#The incredible formula  n² − 79n + 1601 was discovered, which produces 80
#primes for the consecutive values n = 0 to 79. The product of the coefficients
#−79 and 1601, is −126479.
#
#Considering quadratics of the form:
#
#n² + an + b, where |a| < 1000 and |b| < 1000
#
#where |n| is the modulus/absolute value of n
#e.g. |11| = 11 and |−4| = 4
#Find the product of the coefficients, a and b, for the quadratic expression
#that produces the maximum number of primes for consecutive values of n
#starting with n = 0.
#
#if n = 0, n² + an + b = b -> b is a positive prime number.
#

import time
from Euler import *

primes = sieve_erat(1000)

def seq(a, b, n=0):
    seq_p = [b]
    p = b    
    while p > 0 and is_prime(p):
        seq_p.append(p)
        n += 1
        p = n**2 + a*n + b
    return seq_p

max_len = (0, 0, 0)

start = time.time()

for b in primes:
    for a in range(-999, 1000):
        prime_seq = seq(a, b)
        if len(prime_seq) > max_len[0]:
            max_len = (len(prime_seq), a, b)

elapsed = (time.time() - start)            
print max_len, max_len[1] * max_len[2], 'in %5.3f seconds' % elapsed
