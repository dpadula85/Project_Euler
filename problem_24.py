# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 14:24:09 2015

@author: Daniele
"""

#A permutation is an ordered arrangement of objects. For example, 3124 is one
#possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
#are listed numerically or alphabetically, we call it lexicographic order.
#The lexicographic permutations of 0, 1 and 2 are:
#
#012   021   102   120   201   210
#
#What is the millionth lexicographic permutation of the digits
#0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import itertools
import time

permuted = []

start = time.time()

for i in itertools.permutations(range(10)):
    permuted.append(i)

elapsed = (time.time() - start)

result = list(permuted[999999])
res = ''.join(str(i) for i in result)
print res, 'in %5.3f seconds' % elapsed    
