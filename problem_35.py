# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 10:38:11 2015

@author: Daniele
"""

#The number, 197, is called a circular prime because all rotations of
#the digits: 197, 971, and 719, are themselves prime.
#
#There are thirteen such primes below 100:
#2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
#How many circular primes are there below one million?

import time
import re
from Euler import *

def rotate(n):
    '''Returns a list containing the rotations of n.'''
    rotations = []
    for i in range(len(str(n))):
        rot = int(str(n)[i:] + str(n)[:i])
        rotations.append(rot)
    return sorted(rotations)

start = time.time()

primes = sieve_erat(1000000)
#the algorithm can be improved ignoring those primes which contain an even
#digit or a 5, since when that digit will be in the end of the rotation
#the number formed like this will not be prime

circulars = [2, 5] #primes included in the re.search
sel_primes = []     

for prime in primes:
    if not re.search('[024568]', str(prime)):
        sel_primes.append(prime)

for sel_prime in sel_primes:
    if filter(is_prime, rotate(sel_prime)) == rotate(sel_prime):
        circulars.append(sel_prime)
    
elapsed = (time.time() - start)            
print len(circulars), 'in %5.3f seconds' % elapsed   