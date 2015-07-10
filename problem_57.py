# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 15:09:49 2015

@author: Daniele
"""

#It is possible to show that the square root of two can be expressed as an
#infinite continued fraction.
#
#√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
#
#By expanding this for the first four iterations, we get:
#
#1 + 1/2 = 3/2 = 1.5
#1 + 1/(2 + 1/2) = 7/5 = 1.4
#1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
#1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
#
#The next three expansions are 99/70, 239/169, and 577/408, but the eighth
#expansion, 1393/985, is the first example where the number of digits in the
#numerator exceeds the number of digits in the denominator.
#
#In the first one-thousand expansions, how many fractions contain a numerator
#with more digits than denominator?
#
#  1    2     3      4      5       6        7         8
# 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985
#
# num_(i+1) = num_(i) + 2*d_(i)
# den_(i+1) = num_(i) + d_(i)

import time
from Euler import *

start = time.time()
num_i, den_i = 3, 2       # num_1, den_1
sols = []
for i in range(2, 1001):
    t = num_i             #temporary variable to change num, den
    num_i = t + 2*den_i   #new ith num
    den_i = t + den_i     #new ith den
    if len(str(num_i)) > len(str(den_i)):
        sols.append((num_i, den_i))


elapsed = (time.time() - start)
print len(sols), 'in %5.3f seconds' % elapsed