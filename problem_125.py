# -*- coding: utf-8 -*-                                                                                                 
"""
Created on Fri Jul 17 14:21:58 2015                                                                                     
@author: Daniele                                                                                                        
"""

#The palindromic number 595 is interesting because it can be written as the sum
#of consecutive squares: 6**2 + 7**2 + 8**2 + 9**2 + 10**2 + 11**2 + 12**2.
#There are exactly eleven palindromes below one-thousand that can be written
#as consecutive square sums, and the sum of these palindromes is 4164.
#Note that 1 = 0**2 + 1**2 has not been included as this problem is concerned with
#the squares of positive integers.
#
#Find the sum of all the numbers less than 10**8 that are both palindromic and
#can be written as the sum of consecutive squares.

# Two approaches:
# generate palindromes and check if they are sum of consecutive squares
# generate sums of consecutive squares and check if they are palindromes
# Check the numbers up to sqrt(lim).

import time
import math 
from Euler import *

lim = int(math.sqrt(10**8))

start = time.time()

pals = []

for i in range(1, lim + 1):
    result = i*i
    for j in range(i + 1, lim + 1):
        result += j*j
        if result > lim*lim:
            break
        if is_palindromic(result):
            pals.append(result)

elapsed = (time.time() - start)                                                                                         
print sum(set(pals)), 'in %5.3f seconds' % elapsed 
