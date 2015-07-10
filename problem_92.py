# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:35:52 2015

@author: Daniele
"""

#A number chain is created by continuously adding the square of the digits in a
#number to form a new number until it has been seen before.
#
#For example,
#
#44 → 32 → 13 → 10 → 1 → 1
#85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
#
#Therefore any chain that arrives at 1 or 89 will become stuck in an endless
#loop. What is most amazing is that EVERY starting number will eventually
#arrive at 1 or 89.
#
#How many starting numbers below ten million will arrive at 89?

import time
from Euler import *

mem = {}
mem[1] = [1]
mem[89] = [89, 145, 42, 20, 4, 16, 37, 58]

#Recursive generation of the chain described in the problem
def next_chain(n, chain=None):
    if chain is None:
        chain = []
    if n in mem:
        return chain + mem[n]
    elif n in chain:
        return chain
    else:
        chain.append(n)
    str_n = str(n)
    sum_d = 0
    for d in str_n:
        sum_d += int(d)**2
    
    return next_chain(sum_d, chain)

start = time.time()

#inefficient but does the job    
count = 0
for i in range(10000000):
    n = next_chain(i)
    if 89 in n:
        count += 1
        
elapsed = (time.time() - start)        
print count, 'in %5.3f seconds' % elapsed