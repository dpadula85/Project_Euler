# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 14:07:29 2015

@author: Daniele
"""

#2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
#What is the sum of the digits of the number 2**1000?

from Euler import *

a = 2**1000
print digit_sum(a)