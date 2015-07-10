# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 12:11:50 2015

@author: Daniele
"""

#The following iterative sequence is defined for the set of positive integers:
#
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)
#
#Using the rule above and starting with 13, we generate the following sequence:
#
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1)
#contains 10 terms. Although it has not been proved yet (Collatz Problem),
#it is thought that all starting numbers finish at 1.
#
#Which starting number, under one million, produces the longest chain?
#
#NOTE: Once the chain starts the terms are allowed to go above one million.

import time

def collatz(n):
    '''Return a list containing the Collatz sequence of n.'''
    
    sequence = [n]        
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    
    return sequence

max_length = (0, 0)
    
start = time.time()

for i in range(1000000):
    seq_i = collatz(i)
    if len(seq_i) > max_length[1]:
        max_length = (i, len(seq_i))

elapsed = (time.time() - start)
    
print max_length, 'in %5.3f seconds' % elapsed