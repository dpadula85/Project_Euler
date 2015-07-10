# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 13:17:15 2015

@author: Daniele
"""

#The number 145 is well known for the property that the sum of the factorial of
#its digits is equal to 145:
#
#1! + 4! + 5! = 1 + 24 + 120 = 145
#
#Perhaps less well known is 169, in that it produces the longest chain of
#numbers that link back to 169; it turns out that there are only three such
#loops that exist:
#
#169 → 363601 → 1454 → 169
#871 → 45361 → 871
#872 → 45362 → 872
#
#It is not difficult to prove that EVERY starting number will eventually get
#stuck in a loop. For example,
#
#69 → 363600 → 1454 → 169 → 363601 (→ 1454)
#78 → 45360 → 871 → 45361 (→ 871)
#540 → 145 (→ 145)
#
#Starting with 69 produces a chain of five non-repeating terms, but the longest
#non-repeating chain with a starting number below one million is sixty terms.
#
#How many chains, with a starting number below one million, contain exactly
#sixty non-repeating terms?

import time
from Euler import *

#Known loops stored to avoid recalculating them
#10% speed increase
mem = {}
mem[169] = [169, 363601, 1454]
mem[363601] = [363601, 1454]
mem[1454] = [1454]
mem[871] = [871, 45361]
mem[45361] = [45361]
mem[872] = [872, 45362]
mem[45362] = [45362]
mem[145] = [145]

#Recursive generation of the chain described in the problem
def next_chain(n, chain=None):
    if chain is None:
        chain = []
    elif n in mem:
        return chain + mem[n]
    elif n in chain:
        return chain
    else:
        chain.append(n)
    str_n = str(n)
    sum_d = 0
    for d in str_n:
        sum_d += fact(int(d))
    
    return next_chain(sum_d, chain)

start = time.time()

sol = 0
for i in xrange(1, 10**6):
    chain = next_chain(i)
    if len(chain) == 60:
        sol += 1

elapsed = (time.time() - start)        
print sol, 'in %5.3f seconds' % elapsed        