# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:32:05 2015

@author: Daniele
"""

#By counting carefully it can be seen that a rectangular grid measuring 3 by 2
#contains eighteen rectangles:
#
#Although there exists no rectangular grid that contains exactly two million
#rectangles, find the area of the grid with the nearest solution.
#
#The number of rectangles in a NxM grid is N(N+1)M(M+1)/4
#Find N, M for the grid containing 2 000 000 rectangles and calculate the area.
#If N, M = 2000 we have 2 001 000 rectangles.

import time

lim = 2000000
err_min = lim

start = time.time()
for n in range(2000):
    for m in range(n, 2000):
        n_rect = n*(n + 1)*m*(m + 1)/4
        err = abs(n_rect - lim)
        if err < err_min:
            a = m*n
            err_min = err
            
elapsed = (time.time() - start)            
print a, 'in %5.3f seconds' % elapsed 