# -*- coding: utf-8 -*-                                                                                                 
"""
Created on Fri Jul 17 22:00:34 2015                                                                                     
@author: Daniele                                                                                                        
"""

# Description at https://projecteuler.net/problem=101

import time
import numpy as np 

start = time.time()

u = np.poly1d([1., -1., 1., -1., 1., -1., 1., -1., 1., -1., 1.])

correct = []
sum_fits = 0

for i in range(1, len(u) + 1):
    res = u(i)
    correct.append(res)
    bop = np.poly1d(np.polyfit(range(1, i + 1), correct, i - 1))
    fit = bop(i + 1)
    if fit != u(i + 1):
        sum_fits += fit

elapsed = (time.time() - start)                                                                                         
print sum_fits,  'in %5.3f seconds' % elapsed 
