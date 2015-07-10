# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 08:05:29 2015

@author: Daniele
"""

#The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
#and concatenating them in any order the result will always be prime.
#For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these
#four primes, 792, represents the lowest sum for a set of four primes with this
#property.
#
#Find the lowest sum for a set of five primes for which any two primes
#concatenate to produce another prime.

import time
from itertools import permutations
from Euler import *

def concatenatable_primes(chain):
    '''Returns True if the primes in chain give prime numbers by
    concatenation.'''
    
    return all(map(is_prime, [int(str(i[0]) + str(i[1])) for i in permutations(chain,2)]))

def set_conc(n):
    '''Returns the set of all the primes concatenatable with n.'''
    set_n = []    
    for p in primes:
        if concatenatable_primes([n, p]):
            set_n.append(p)
    
    return set(set_n)

primes = filter(lambda x: x > 2,sieve_erat(10000))
#if one would choose 30 000 as upper limit, another set of 5 primes can be
#found. Those primes have a higher sum. In any case, the p1...p5 sets can be
#stored in a list and sorted by sum.

stop = False

start = time.time()

for p1 in primes: 
    set_p1 = sorted(list(set_conc(p1)))
    
    if stop == True:
        break
    
    for p2 in filter(lambda x: x > p1, set_p1):
        set_p1p2 = sorted(list(set_conc(p1).intersection(set_conc(p2))))

        if stop == True:
            break
        
        for p3 in filter(lambda x: x > p2, set_p1p2):
            set_p1p2p3 = sorted(list(set_conc(p1).intersection(set_conc(p2), set_conc(p3))))
#control code for the example given in the text            
#            if set_p1p2p3:
#                p4 = min(set_p1p2p3)                    
#                print p1, p2, p3, p4, p1+p2+p3+p4
#                stop = True                    
#                break
            if stop == True:
                break
            
            for p4 in filter(lambda x: x > p3, set_p1p2p3):
                set_p1p2p3p4 = sorted(list(set_conc(p1).intersection(set_conc(p2), set_conc(p3), set_conc(p4))))                
                if set_p1p2p3p4:
                    p5 = min(set_p1p2p3p4)
                    print p1, p2, p3, p4, p5, p1+p2+p3+p4+p5
                    stop = True
                    break
                if stop == True:
                    break
                    
elapsed = (time.time() - start)
print 'in %5.3f seconds' % elapsed