# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:54:54 2015

@author: Daniele
"""

#We shall say that an n-digit number is pandigital if it makes use of all the
#digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
#The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
#multiplicand, multiplier, and product is 1 through 9 pandigital.
#
#Find the sum of all products whose multiplicand/multiplier/product identity
#can be written as a 1 through 9 pandigital.
#
#HINT: Some products can be obtained in more than one way so be sure to only
#include it once in your sum.
#
# m * n = p
# digits m + n + p = 9
#
#table of total digits based on digits in m, n
#   n   1       2       3     4
# m
# 1    3-4     5-6     7-8  9-10
# 2            7-8     9-10 11-12
# 3                         13-14
# 4                         15-16
#
#We only need to look for m (4-dig)* n(1-dig) and m(2-dig) * n(3-dig)
#Be careful not to consider equivalent couples since, e.g.
# 39 * 186 = 7254
# 186 * 39 = 7254
#
#Exclude all numbers containing 0

from Euler import *
import time

start = time.time()


dig_4 = filter(lambda x: '0' not in str(x), range(1000, 10000))
dig_3 = filter(lambda x: '0' not in str(x), range(100, 1000))
dig_2 = filter(lambda x: '0' not in str(x), range(10,100))
dig_1 = range(1, 10)

pan_triples = []

for m in dig_4:
    for n in dig_1:
        p = m * n
        pan_prod = int(str(m) + str(n) + str(p))
        if is_pandigital(pan_prod) and p not in [i[2] for i in pan_triples]:
            triple = tuple(sorted((m, n, p)))            
            pan_triples.append(triple)
        
for m in dig_3:
    for n in dig_2:
        p = m * n
        pan_prod = int(str(m) + str(n) + str(p))
        if is_pandigital(pan_prod) and p not in [i[2] for i in pan_triples]:
            triple = tuple(sorted((m, n, p)))            
            pan_triples.append(triple)

sum_prods = sum([i[2] for i in pan_triples])

elapsed = (time.time() - start)            
print sum_prods, 'in %5.3f seconds' % elapsed