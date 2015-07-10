# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 16:17:35 2015

@author: Daniele
"""

#It is possible to write ten as the sum of primes in exactly five different ways:
#
#7 + 3
#5 + 5
#5 + 3 + 2
#3 + 3 + 2 + 2
#2 + 2 + 2 + 2 + 2
#
#What is the first value which can be written as the sum of primes in over five
#thousand different ways?
#
#Variation of problems 31, 76

import time
import Euler as E

N = 5000 #combinations
primes = E.sieve_erat(1000) #set of primes to be summed
m = len(primes)

sol = 1 #values to be generated as sum of primes

start = time.time()

#dynamic solution
while True:
    ways = [1] + [0] * sol
    for p in primes:
        for j in range(p, sol + 1):
            ways[j] += ways[j - p]
    if ways[sol] > N:
        print sol                
        break
    sol += 1

elapsed = (time.time() - start)            
print 'in %5.3f seconds' % elapsed