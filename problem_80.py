# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 08:27:28 2015

@author: Daniele
"""

#It is well known that if the square root of a natural number is not an integer,
#then it is irrational. The decimal expansion of such square roots is infinite
#without any repeating pattern at all.
#
#The square root of two is 1.41421356237309504880..., and the digital sum of the
#first one hundred decimal digits is 475.
#
#For the first one hundred natural numbers, find the total of the digital sums
#of the first one hundred decimal digits for all the irrational square roots.

import time
from math import sqrt
from decimal import *
from Euler import *

start = time.time()

irr = [i for i in range(2, 100) if not sqrt(i).is_integer()]
getcontext().prec = 105     #set bigger precision for approximation problems
sum_dec = 0
#we have to multiply the high precision sqrt(i) by 10**99 because of peoblems
#with approximations and because the digit before the decimal separator should
#be included
for i in irr:
    i_dec = int(Decimal(i).sqrt()*10**99)
    i_dec_sum = digit_sum(i_dec)
    sum_dec += i_dec_sum
    
elapsed = (time.time() - start)            
print sum_dec, 'in %5.3f seconds' % elapsed