# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:52:03 2015

@author: Daniele
"""

#The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.
#
#Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.

import time

start = time.time()

sum_n = 0
for n in range(1, 1001):
    sum_n += n**n

elapsed = (time.time() - start)
print str(sum_n)[-10:], 'in %5.3f seconds' % elapsed