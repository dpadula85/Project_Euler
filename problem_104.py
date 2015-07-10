# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:04:15 2015

@author: Daniele
"""

#The Fibonacci sequence is defined by the recurrence relation:
#
#Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#It turns out that F541, which contains 113 digits, is the first Fibonacci
#number for which the last nine digits are 1-9 pandigital (contain all the
#digits 1 to 9, but not necessarily in order). And F2749, which contains 575
#digits, is the first Fibonacci number for which the first nine digits are 1-9
#pandigital.
#
#Given that Fk is the first Fibonacci number for which the first nine digits
#AND the last nine digits are 1-9 pandigital, find k.

import time
from Euler import *
    
def first(n):
    log_s5 = 0.34948500216800943
    log_phi = 0.20898764024997876
    t = n * log_phi - log_s5
    t = int((pow(10, t - int(t) + 8)))
    return t   

start = time.time()

fk = 2
f1 = 1
f0 = 1   
while not is_pandigital(f1) or not is_pandigital(first(fk)):
    f0, f1 = f1, (f1 + f0) % 10**9
    fk += 1

elapsed = (time.time() - start)            
print fk, 'in %5.3f seconds' % elapsed        