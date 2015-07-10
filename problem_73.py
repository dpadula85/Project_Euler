# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 11:19:33 2015

@author: Daniele
"""

#Consider the fraction, n/d, where n and d are positive integers. If n<d and
#HCF(n,d)=1, it is called a reduced proper fraction.
#
#If we list the set of reduced proper fractions for d ≤ 8 in ascending order of
#size, we get:
#
#1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7,
#3/4, 4/5, 5/6, 6/7, 7/8
#
#It can be seen that there are 3 fractions between 1/3 and 1/2.
#
#How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper
#fractions for d ≤ 12,000?

import time
from fractions import gcd

a = 3
b = 2
lim = 12000
sol = 0

start = time.time()

for i in range(5, lim + 1):
    for j in range(i/a + 1, (i - 1)/b + 1):
        if gcd(i, j) == 1:
            sol += 1
            
elapsed = (time.time() - start)        
print sol, 'in %5.3f seconds' % elapsed