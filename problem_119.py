# -*- coding: utf-8 -*-                                                                                                 
"""
Created on Wed Jul 15 18:40:34 2015                                                                                     
@author: Daniele                                                                                                        
"""                                                                                                                     

#The number 512 is interesting because it is equal to the sum of its digits
#raised to some power: 5 + 1 + 2 = 8, and 83 = 512. Another example of a
#number with this property is 614656 = 284.
#We shall define an to be the nth term of this sequence and insist that a
#number must contain at least two digits to have a sum.
#You are given that a2 = 512 and a10 = 614656.
#Find a30.

# Generate number p = b**e
# check digit_sum(p) = b
# order the numbers

import time                                                                                                             
from Euler import *

start = time.time()                                                                                                     

nums = []
stop = False

for b in range(1, 500):
    for e in range(1, 500):
        p = b**e
        if p > 10 and digit_sum(p) == b:
            nums.append(p)

        if len(nums) == 50:
            stop = True
            break
    if stop:
        break

nums.sort()

elapsed = (time.time() - start)                                                                                         
print nums[29], 'in %5.3f seconds' % elapsed 
