# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 14:59:06 2015

@author: Daniele
"""

#A unit fraction contains 1 in the numerator. The decimal representation of the
#unit fractions with denominators 2 to 10 are given:
#
#1/2	 = 	0.5
#1/3	 = 	0.(3)
#1/4	 = 	0.25
#1/5	 = 	0.2
#1/6	 = 	0.1(6)
#1/7	 = 	0.(142857)
#1/8	 = 	0.125
#1/9	 = 	0.(1)
#1/10 = 	0.1
#
#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
#It can be seen that 1/7 has a 6-digit recurring cycle.
#
#Find the value of d < 1000 for which 1/d contains the longest recurring cycle
#in its decimal fraction part.
#
#Fermat’s little theorem that says: 1/d has a cycle of n digits
#if 10**n − 1 mod d = 0 for prime d.
#It also follows that a prime number in the denominator
#can yield up to d − 1 repeating decimal digits.
#We need to find the largest prime, p, under 1000 that has p − 1 digits.

import time
from Euler import *

start = time.time()

primes = sieve_erat(1000)

#let's start from the largest
for p in primes[::-1]:
    n = 1
    while pow(10, n, p) - 1 != 0:
        n += 1
    if (p - n) == 1:
        break

elapsed = (time.time() - start)
print p, 'in %5.3f seconds' % elapsed