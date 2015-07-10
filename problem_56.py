# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 14:50:20 2015

@author: Daniele
"""

#A googol (10**100) is a massive number: one followed by one-hundred zeros;
#100**100 is almost unimaginably large: one followed by two-hundred zeros.
#Despite their size, the sum of the digits in each number is only 1.
#
#Considering natural numbers of the form, a**b, where a, b < 100, what is the
#maximum digital sum?

import time
from Euler import *

start = time.time()

max_sum = 0
for a in range(1, 100):
    for b in range(1, 100):
        sum_ab = digit_sum(a**b)
        if sum_ab > max_sum:
            max_sum = sum_ab
            
elapsed = (time.time() - start)
print max_sum, 'in %5.3f seconds' % elapsed