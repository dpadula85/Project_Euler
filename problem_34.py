# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:07:22 2015

@author: Daniele
"""

#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
#Find the sum of all numbers which are equal to the sum of the factorial
#of their digits.
#
#Note: as 1! = 1 and 2! = 2 are not sums they are not included.
#
#For an explanation see http://en.wikipedia.org/wiki/Factorion
#
#If n is a natural number of d digits that is a factorion, then
#
#10**(d − 1) ≤ n ≤ d * 9!
#
#This fails to hold for d ≥ 8 thus n has at most 7 digits -> 9 999 999.
# 9! * 7 = 2 540 160

import time
from Euler import *

def factorion(n):
    '''Returns True if n is a factorion.
    A Factorion is a number which is equal to the sum of the factorial
    of its digits.
    
    Example:
    1! + 4! + 5! = 1 + 24 + 120 = 145
    '''
    digits = map(int, str(n))
    digits_facts = map(fact, digits)

    return n == sum(digits_facts)

factorions = []
start = time.time()    

for i in range(3, 2540160):
    if factorion(i):
        factorions.append(i)

elapsed = (time.time() - start)            
print sum(factorions), 'in %5.3f seconds' % elapsed 
