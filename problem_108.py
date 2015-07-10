# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 08:40:19 2015

@author: Daniele
"""

#In the following equation x, y, and n are positive integers.
#
#1/x + 1/y = 1/n
#
#For n = 4 there are exactly three distinct solutions:
#
#1/5 + 1/20 = 1/4
#1/6 + 1/12 = 1/4
#1/8 + 1/8 = 1/4
#
#What is the least value of n for which the number of distinct solutions exceeds
#one-thousand?
#
#NOTE: This problem is an easier version of Problem 110; it is strongly advised
#that you solve this one first.
#
#The equation is equivalent to n = x*y/(x + y). d = gcd(x, y) which implies
# x = d*i, y = d*j with gcd(i, j) = 1.
# n = d*i*j/(i + j), in which (i + j)/d = k*(i + j), where k is integer.
#Thus, the solutions are x = k*i*(i + j) and y = k*j*(i + j) and n = k*i*j,
#where k, i, j are all integers.
#
#Another solution is to observe that x, y > n. Thus, we can express the equation
#as
#1/(n + r) + 1/(n + s) = 1/n
#
#with r, s integers. After rearranging the equation we obtain that n**2 = r*s.
#In other terms, r,s are divisors of n**2.
#To solve the problem, we need to find the first number n whose square has more
#than 2000 divisors (because the solutions have to be distinct).

import time
from Euler import factorize

start = time.time()

def n_divs(n):
    '''Returns the number of divisors of n**2.'''
    prime_factors = factorize(n)
    num_divs = 1    
    for factor in prime_factors:
        num_divs *= (2*factor[1] + 1)   #the difference is here, factor 2
    
    return num_divs

n = 1
divs_sq_n = n_divs(n)
while divs_sq_n < 2000:
    n += 1
    divs_sq_n = n_divs(n)
    
elapsed = (time.time() - start)            
print n, 'in %5.3f seconds' % elapsed