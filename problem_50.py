# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:55:24 2015

@author: Daniele
"""

#The prime 41, can be written as the sum of six consecutive primes:
#
#41 = 2 + 3 + 5 + 7 + 11 + 13
#This is the longest sum of consecutive primes that adds to a prime below
#one-hundred.
#
#The longest sum of consecutive primes below one-thousand that adds to a prime
#contains 21 terms, and is equal to 953.
#
#Which prime, below one-million, can be written as the sum of the most
#consecutive primes?
#
#The sum of the primes between p1 and p2 (both primes) is defined as
#sum_primes(p2) - sum_primes(p1).
#Surely sum_primes(p2) - sum_primes(p1) < 1 000 000
#
import time
from Euler import *

def p_sum(prime_list):
    p_sum = [0]
    s = 0
    for p in prime_list:
        s += p
        p_sum.append(s)

    return p_sum

start = time.time()

n = 1000000     #limit of our analysis
primes = sieve_erat(n)
l = primes[-1]  #limit of the biggest prime
primes_sum = [s for s in p_sum(primes) if s < l]

count = 0
p_max = 0

for sum_p1 in primes_sum:
    i = primes_sum.index(sum_p1)
    for sum_p2 in primes_sum[i + count:]:
        diff = sum_p2 - sum_p1
        if diff > l:
            break
        j = primes_sum.index(sum_p2)
        seq = j - i
        if is_prime(diff) and seq > count:
            count = seq
            p_max = diff
            
elapsed = (time.time() - start)
print p_max, count, 'in %5.3f seconds' % elapsed