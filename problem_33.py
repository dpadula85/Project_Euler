# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:41:12 2015

@author: Daniele
"""

#The fraction 49/98 is a curious fraction, as an inexperienced mathematician
#in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
#which is correct, is obtained by cancelling the 9s.
#
#We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
#There are exactly four non-trivial examples of this type of fraction,
#less than one in value, and containing two digits in the numerator and
#denominator.
#
#If the product of these four fractions is given in its lowest common terms,
#find the value of the denominator.
#
#conditions n/d < 1 -> n < d
#n, d have one digit in common

import time
from Euler import *
from fractions import Fraction

def digits(n):
    x = map(int, str(n))
    return x

start = time.time()

fracs = []

#generates possible fractions n/d < 1 with one digit in common
#ignoring d containing 0.
#each fraction is expressed as a tuple (n, d)
for n in range(10, 100):
    for d in range(n + 1, 100):
        if any (i in digits(d) for i in digits(n)) and 0 not in digits(d):
            fracs.append((n, d))
         
red_fracs = []
for frac in fracs:
    num = map(str, digits(frac[0]))
    den = map(str, digits(frac[1]))
    for j in num:
        if j in den:
            num.remove(j)
            den.remove(j)
            red_fracs.append((int(num[0]), int(den[0])))

curious = []
for pair in [list(a) for a in zip(fracs, red_fracs)]:
    if Fraction(pair[0][0], pair[0][1]) == Fraction(pair[1][0], pair[1][1]):
        curious.append(pair[1])

result = 1
for frac in curious:
    result *= Fraction(frac[0], frac[1])        
        
elapsed = (time.time() - start)            
print result, 'in %5.3f seconds' % elapsed 