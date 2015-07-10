# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:48:54 2015

@author: Daniele
"""

#Take the number 192 and multiply it by each of 1, 2, and 3:
#
#192 × 1 = 192
#192 × 2 = 384
#192 × 3 = 576
#
#By concatenating each product we get the 1 to 9 pandigital, 192384576.
#We will call 192384576 the concatenated product of 192 and (1,2,3)
#
#The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4
#and 5, giving the pandigital, 918273645, which is the concatenated product
#of 9 and (1,2,3,4,5).
#
#What is the largest 1 to 9 pandigital 9-digit number that can be formed as
#the concatenated product of an integer with (1,2, ... , n) where n > 1?
#
#table of total digits based on digits in m, n
#   n   1       2       3     4
# m
# 1    3-4     5-6     7-8  9-10
#
#n contains less than 5 digits
#result > 918273645
#if n had two digits, we should check 90 < n < 99, since the result of 
#n * 1 should start with at least 91. Turns out that, for those cases,
#n * 2 = 3 digits, n * 3 = digits. Concatenation gives an 8-digit number,
#which is not good.
#if n had three digits, we should check 919 < n < 999, since the result of 
#n * 1 should start with at least 919. Turns out that, for those cases,
#n * 2 = 4 digits, n * 4 = digits. Concatenation at 2 gives a 4-digit number,
#Concatenation at 3 gives an 11-digit number. Both are not good.
#The only possibility is for n to have 4 digits.
#We should start to look for 9181 < n < 9999. Concatenation at n * 2 gives
#9-digit numbers, that is what we are looking for.

import time
from Euler import *

start = time.time()

pans = []

for n in range(9182, 10000):
    p1 = n * 1
    p2 = n * 2
    conc = int(str(p1) + str(p2))
    if is_pandigital(conc) and conc not in pans:
        pans.append(conc)
        
elapsed = (time.time() - start)            
print max(pans), 'in %5.3f seconds' % elapsed