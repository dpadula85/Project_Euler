# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:38:02 2015

@author: Daniele
"""

#Surprisingly there are only three numbers that can be written as the sum of
#fourth powers of their digits:
#
#1634 = 1**4 + 6**4 + 3**4 + 4**4
#8208 = 8**4 + 2**4 + 0**4 + 8**4
#9474 = 9**4 + 4**4 + 7**4 + 4**4
#As 1 = 1**4 is not a sum it is not included.
#
#The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
#Find the sum of all the numbers that can be written as the sum of fifth powers
#of their digits.

import time

start = time.time()

sum_nums = 0

for i in range(10, 1000000):  
    sum_digits = 0    
    for d in str(i):
        sum_digits += pow(int(d), 5)
    if sum_digits == i:
        sum_nums += i

elapsed = (time.time() - start)            
print sum_nums, 'in %5.3f seconds' % elapsed