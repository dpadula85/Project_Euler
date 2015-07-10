# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 08:59:44 2015

@author: Daniele
"""

#Euler's Totient function, φ(n) [sometimes called the phi function], is used to
#determine the number of numbers less than n which are relatively prime to n.
#For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively
#prime to nine, φ(9)=6.
#
#n	Relatively Prime	φ(n)	n/φ(n)
#2	1	1	2
#3	1,2	2	1.5
#4	1,3	2	2
#5	1,2,3,4	4	1.25
#6	1,5	2	3
#7	1,2,3,4,5,6	6	1.1666...
#8	1,3,5,7	4	2
#9	1,2,4,5,7,8	6	1.5
#10	1,3,7,9	4	2.5
#It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.
#
#Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

import time
from fractions import gcd
from Euler import *

start = time.time()

primes = sieve_erat(50)
l = 10**6
prod_p = 1

for p in primes:
    if prod_p * p > l:
        print prod_p
        break
    prod_p *= p
    
#brute force inefficient
#i_max = 0
#phi_max = 0
#ratio_max = 0
#for i in range(1,1000001):
#    phi = 1
#    for j in range(1, i):
#        if gcd(i, j) == 1:
#            phi += 1
#    if i//phi > ratio_max:
#        ratio_max = i//phi
#        phi_max = phi
#        i_max = i


elapsed = (time.time() - start)  
print 'in %5.3f seconds' % elapsed