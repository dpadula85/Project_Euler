# -*- coding: utf-8 -*-                                                                                                 
"""
Created on Mon Jul 20 10:35:23 2015                                                                                     
@author: Daniele                                                                                                        
"""
#Some positive integers n have the property that the sum [ n + reverse(n) ]
#consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and
#409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and
#904 are reversible. Leading zeroes are not allowed in either n or reverse(n).
#
#There are 120 reversible numbers below one-thousand.
#
#How many reversible numbers are there below one-billion (109)?

import time

def odd(n):
    if n % 2 == 1:
        return True
    else:
        return False

def all_odd(n):
    '''Returns True if all digits of n are odd.'''
    n = map(int, list(str(n)))
    return all(map(odd, n))

def rev(n):
    return int(str(n)[::-1])

lim = 10**6
count = 0
sieve = [True] * (lim + 1)

start = time.time()

r = 0

while r < lim:
    if str(r)[-1] != '0' and sieve[r]:
        n = r + rev(r)
        sieve[rev(r)] = False
        if all_odd(n):
            count += 1

    r += 1

elapsed = (time.time() - start)                                                                                         
print count*2, 'in %5.3f seconds' % elapsed 
