# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:01:02 2015

@author: Daniele
"""

#We shall say that an n-digit number is pandigital if it makes use of all
#the digits 1 to n exactly once.
#For example, 2143 is a 4-digit pandigital and is also prime.
#
#What is the largest n-digit pandigital prime that exists?
#
#The largest possible pandigital is 987654321
#We know that n % 3 == 0 if the sum of the digits costituting n is multiple
#of 3. This way, we can exclude some n-digit pandigitals.
#
#1+2+3+4+5+6+7+8+9 = 45
#
#1+2+3+4+5+6+7+8 = 36
#
#1+2+3+4+5+6+7 = 28 -> not divisible by 3
#
#1+2+3+4+5+6 = 21
#
#1+2+3+4+5 = 15
#
#1+2+3+4 = 10 -> not divisible by 3
#
#1+2+3 = 6
#
#1+2 = 3
#
#Thus, to find the largest pandigital, we have to look into the 4-digit and
#7-digit pandigitals.

import time
from Euler import *

#let's generate a list for 4-digit pandigitals and one for 7-digit ones.

start = time.time()

pan_4 = pandigitals(4)
pan_7 = pandigitals(7)

#We iterate over each list and check whether the elements are prime.
#We put prime pandigitals into another list and find out the maximum.

prime_pans = []

for pan in pan_4:
    if is_prime(pan):
        prime_pans.append(pan)
        
for pan in pan_7:
    if is_prime(pan):
        prime_pans.append(pan)
        
elapsed = (time.time() - start)            
print max(prime_pans),'in %5.3f seconds' % elapsed       