# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:38:22 2015

@author: Daniele
"""

#The proper divisors of a number are all the divisors excluding the number
#itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the
#sum of these divisors is equal to 28, we call it a perfect number.
#
#Interestingly the sum of the proper divisors of 220 is 284 and the sum of the
#proper divisors of 284 is 220, forming a chain of two numbers. For this reason
#220 and 284 are called an amicable pair.
#
#Perhaps less well known are longer chains. For example, starting with 12496,
#we form a chain of five numbers:
#
#12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)
#
#Since this chain returns to its starting point, it is called an amicable chain.
#
#Find the smallest member of the longest amicable chain with no element
#exceeding one million.

import time
from Euler import *

#Recursive generation of the chain described in the problem
def next_chain(n, chain=None):
    if chain is None:
        chain = []
    if n in chain:
        return chain + [n]
    elif n > 1000000:
        return []
    else:
        chain.append(n)
    d = sum(divs(n)[:-1])
    
    return next_chain(d, chain)

start = time.time()    

longest = []
#inefficient for high limits
for i in xrange(1000000):   #random upper limit for the search
    n = next_chain(i)
    if n and n[0] in n[1:] and len(n) > len(longest):
        longest = n

elapsed = (time.time() - start)        
print min(longest), 'in %5.3f seconds' % elapsed