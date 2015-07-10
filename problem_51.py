# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 09:22:06 2015

@author: Daniele
"""

#By replacing the 1st digit of the 2-digit number *3, it turns out that six of
#the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
#
#By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
#number is the first example having seven primes among the ten generated
#numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773,
#and 56993. Consequently 56003, being the first member of this family, is the
#smallest prime with this property.
#
#Find the smallest prime which, by replacing part of the number (not
#necessarily adjacent digits) with the same digit, is part of an eight prime
#value family.

import time
from Euler import *
import re
 

#function to replace whatever number of digits in a number
#the digits to be replaced are specified as optional arguments
def primes_fam(prime, *args):
    family = []
    prime = filter(None, re.split('([0-9])', str(prime)))
    rds = [str(arg) for arg in args]
    if any([rd == prime[0] for rd in rds]):    
        digits = '123456789'
    else:
        digits = '0123456789'    
    if any([d == rd for d in prime for rd in rds]):    
        fam = prime[:]
        for digit in digits:
            fam = prime[:]
            for d in fam:
                if d in rds:
                    i = prime.index(d)
                    fam[i] = digit
            fam_n = int(''.join(fam))
            if is_prime(fam_n) and fam_n not in family:                    
                family.append(fam_n)

    return family

primes = sieve_erat(1000000)    #reasonable upper limit for primes

start = time.time() 

fam_max = []
p_max = 0
stop = False
#first loop for primes
for prime in primes:
    #second loop for first digit to replace
    for i in range(len(str(prime))):
        d1 = str(prime)[i]
        #third loop for second digit to replace        
        for j in filter(lambda x: x!= i, range(i + 1)):
            d2 = str(prime)[j]
            #fourth loopt for third digit to replace and so on...
            #found out it's 3 digits to replace by trying            
            for k in filter(lambda x: x!= j, range(j + 1)):
                d3 = str(prime)[k]
                fam = primes_fam(prime, d1, d2, d3)
                if len(fam) == 8:
                    fam_max = fam
                    p_max = prime
                    stop = True
                    break
            if stop == True:            
                break
        if stop == True:        
            break
    
elapsed = (time.time() - start)
print p_max, fam_max, 'in %5.3f seconds' % elapsed