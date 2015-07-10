# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:24:34 2015

@author: Daniele
"""

#If p is the perimeter of a right angle triangle with integral length sides,
#{a,b,c}, there are exactly three solutions for p = 120.
#
#{20,48,52}, {24,45,51}, {30,40,50}
#
#For which value of p ≤ 1000, is the number of solutions maximised?
#
#Right angle triangle = Pythagorean Triplets
#We must find the the highest number of triplets whose elements' sum equals p.
#
# triplet = (a, b, c)
# a**2 + b**2 = c**2
# p = a + b + c
#
# That gives us
#
# b = (p**2 - 2*a*p) / (2*p - 2*a)
#
#Since a, b, c describe a triangle, a + b > c. a <= b < c -> a < p/3
#Additionally, if we consider properties of odd-even numbers within a
#Pythagorean Triple, it turns out that p is even.

import time
from Euler import *

start = time.time()

sol_max = 0
p_max_sol = 0
sol = 0

for p in range(2, 1000)[::2]:
    sol = 0
    for a in filter(lambda x: x < p, range(1, p/3)):
        if (p*(p - 2*a)) % (2*(p - a)) == 0:
            sol += 1
            if sol >= sol_max:
                sol_max = sol
                p_max_sol = p    

elapsed = (time.time() - start)
print sol_max, p_max_sol, 'in %5.3f seconds' % elapsed