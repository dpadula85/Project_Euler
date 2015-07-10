# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:57:50 2015

@author: Daniele
"""

#Consider quadratic Diophantine equations of the form:
#
#x**2 – D y**2 = 1
#
#For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.
#
#It can be assumed that there are no solutions in positive integers when D is
#square.
#
#By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
#following:
#
#3**2 – 2×2**2 = 1
#2**2 – 3×1**2 = 1
#9**2 – 5×4**2 = 1
#5**2 – 6×2**2 = 1
#8**2 – 7×3**2 = 1
#
#Hence, by considering minimal solutions in x for D ≤ 7, the largest x is
#obtained when D=5.
#
#Find the value of D ≤ 1000 in minimal solutions of x for which the largest
#value of x is obtained.
#
#Quadratic Diophantine equations can be solved through continued fractions.
#More in detail, given as n_i / d_i the ith expansion of sqrt(D),
#this set is a solution for the equation n_i**2 - D d_i**2 = 1.
#We want to expand the values of D to continued fractions to find the solutions
#and thus the highest value of x.

from Euler import *
import time

irr = [i for i in range(1001) if not sqrt(i).is_integer()]
sols = []
#tolerance = 0.00000000000000000001

start = time.time()

#the algorithm is correct. Nevertheless, there are numerical problems
#in the calculations for D = 61, D = 109 and others
for D in irr:
    cycle = 1
    while True:    
        n = CFrac(sqrt(D), cycle).fraction().numerator
        d = CFrac(sqrt(D), cycle).fraction().denominator
        if n**2 - D*d**2 == 1:    
            sols.append((D, n, d))
            break
        cycle += 1

elapsed = (time.time() - start)  
print sorted(sols, key=lambda x: x[1], reverse=True)[0]
print 'in %5.3f seconds' % elapsed