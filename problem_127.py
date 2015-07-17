# -*- coding: utf-8 -*-                                                                                                 
"""
Created on Fri Jul 17 22:52:16 2015                                                                                     
@author: Daniele                                                                                                        
"""

import time
from Euler import *
from numbthy import *

#The radical of n, rad(n), is the product of distinct prime factors of n. For
#example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.
#We shall define the triplet of positive integers (a, b, c) to be an abc-hit if:
#
#GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
#a < b
#a + b = c
#rad(abc) < c
#
#For example, (5, 27, 32) is an abc-hit, because:
#
#GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
#5 < 27
#5 + 27 = 32
#rad(4320) = 30 < 32
#
#It turns out that abc-hits are quite rare and there are only thirty-one
#abc-hits for c < 1000, with ∑c = 12523.
#
#Find ∑c for c < 120000.

def prod(l):
    p = 1
    for i in l:
        p *= i
    return p

def rad(n):
    l = list(set([i[0] for i in factorize(n)]))
    return prod(l)

start = time.time()

lim = 5000
sum_c = 0
count = 0
#highly inefficient: 60 sec solution for lim = 5000
#It gives correct solutions for lim = 1000 and lim = 5000
#Probably correct also for lim = 120000
for a in range(1, lim):
    for b in range(a + 1, lim - a):
        c = a + b
        if gcd(a,b) != 1 and gcd(a,c) != 1 and gcd(b,c) != 1:
            continue 
        if rad(a)*rad(b)*rad(c) > c:
            continue
        sum_c += c
        count += 1

elapsed = (time.time() - start)                                                                                         
print sum_c, count, 'in %5.3f seconds' % elapsed 
