# -*- coding: utf-8 -*-                                                                                                 
"""
Created on Fri Jul 17 23:55:16 2015                                                                                     
@author: Daniele                                                                                                        
"""

import time
from Euler import *
from numbthy import *

def prod(l):
    p = 1
    for i in l:
        p *= i
    return p

def rad(n):
    l = list(set([i[0] for i in factorize(n)]))
    return prod(l)

start = time.time()

lim = 100000
sol = 10000
cols = []
for i in range(1, lim + 1):
    cols.append((i, rad(i)))

#for j in sorted(cols, key=lambda x: (x[1], x[0])):
#    print j
print sorted(cols, key=lambda x: (x[1], x[0]))[sol - 1][0]

elapsed = (time.time() - start)                                                                                         
print 'in %5.3f seconds' % elapsed 
