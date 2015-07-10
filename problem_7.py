# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 16:59:42 2015

@author: Daniele
"""

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13
#we can see that the 6th prime is 13.
#
#What is the 10 001st prime number?

import time

# function to factor a given positive integer n
def is_prime(n):
    # look for factors of 2 first
    if n % 2 == 0: return False
    # now look for odd factors
    p = 3
    while p < n**0.5+1:
        if n % p == 0: return False
        p += 2
    return True

def nth_prime(n):
    prime = 2
    count = 1
    iter = 3
    while count < n:
        if is_prime(iter):
            prime = iter
            count += 1
        iter += 2
    return prime
    
start = time.time()
prime = nth_prime(10001)
elapsed = (time.time() - start)

print prime, 'in %5.3f seconds' % elapsed        
