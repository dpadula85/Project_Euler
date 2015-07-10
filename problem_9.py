# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 19:05:50 2015

@author: Daniele
"""

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
#a**2 + b**2 = c**2
#For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
#
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#implementation of Euclid's algorithm
#given two numbers m, n with m > n then a Pythagorean triplet (a, b, c)
#is defined as
#
#a = m**2 - n**2
#b = 2*m*n
#c = m**2 + n**2
#
# m, n can be generated using Cantor's pairing function.

import time

#define a generator to iterate over m, n pairs
def cantor(start=0):
    i = start
    while True:
        for j in range(start, i+1):
            yield (i-j+start, j)
        i += 1

#generate the triplet from a pair m, n
#note that this is not a general solution
#a general one can be obtained by inserting
#a multiplicative factor k
def triplet(m, n):
    a = m*m - n*n
    b = 2*m*n
    c = m*m + n*n
    assert (a**2 + b**2 == c**2)
    
    return (a, b, c)

#cycle

start = time.time()
    
for m, n in cantor():
    a, b, c = triplet(m, n)
    if (a + b + c) == 1000:
        print 'triplet = ', (a, b, c)
        print 'a + b + c = ', a + b + c
        print 'a * b * c = ', a * b * c
        break

elapsed = (time.time() - start)
print 'in %5.3f seconds' % elapsed