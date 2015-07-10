# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 13:50:27 2015

@author: Daniele
"""

#A perfect number is a number for which the sum of its proper divisors is
#exactly equal to the number. For example, the sum of the proper divisors of
#28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
#A number n is called deficient if the sum of its proper divisors is less than
#n and it is called abundant if this sum exceeds n.
#
#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
#number that can be written as the sum of two abundant numbers is 24.
#By mathematical analysis, it can be shown that all integers greater than
#28123 can be written as the sum of two abundant numbers.
#However, this upper limit cannot be reduced any further by analysis
#even though it is known that the greatest number that cannot be expressed
#as the sum of two abundant numbers is less than this limit.
#
#Find the sum of all the positive integers which cannot be written as the sum
#of two abundant numbers.

import time
from Euler import *

def abundant(n):
    '''Returns True if a number is perfect or abundant.'''
    return sum(divs(n)[:-1]) > n

start = time.time()

abundants = set()
sum_non_ab = 0

for i in range(28123):
    if abundant(i):
        abundants.add(i)
    #we have to discard i when i = abn1 + abn2. Cleary i > abn1, abn2
    #abn1 and abn2 are already in the list of abundants.
    #i - abn1 = abn2
    #check the absence of abn2 from the list of abundants to keep i
    #for each abn1 already in the list
    if not any( (i - abn1 in abundants) for abn1 in abundants ):
        sum_non_ab += i
        
elapsed = (time.time() - start)
print sum_non_ab, 'in %5.3f seconds' % elapsed 