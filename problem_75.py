# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:12:21 2015

@author: Daniele
"""

#It turns out that 12 cm is the smallest length of wire that can be bent to form
#an integer sided right angle triangle in exactly one way, but there are many
#more examples.
#
#12 cm: (3,4,5)
#24 cm: (6,8,10)
#30 cm: (5,12,13)
#36 cm: (9,12,15)
#40 cm: (8,15,17)
#48 cm: (12,16,20)
#
#In contrast, some lengths of wire, like 20 cm, cannot be bent to form an
#integer sided right angle triangle, and other lengths allow more than one
#solution to be found; for example, using 120 cm it is possible to form exactly
#three different integer sided right angle triangles.
#
#120 cm: (30,40,50), (20,48,52), (24,45,51)
#
#Given that L is the length of the wire, for how many values of L ≤ 1,500,000
#can exactly one integer sided right angle triangle be formed?

import time
from math import sqrt
from fractions import gcd

lim = 1500000
triangles = [0] * lim

start = time.time()

for m in xrange(1, int(sqrt(lim/2.0))):
    for n in xrange(1, m):
        if gcd(m, n) == 1 and (m - n) % 2 ==1 :
            p = 2*m*(m + n)
            if p > lim:
                break
            for idx in xrange(p, lim, p):
                triangles[idx] += 1
        
sol = sum([i for i in triangles if i == 1])

elapsed = (time.time() - start)        
print sol, 'in %5.3f seconds' % elapsed         