# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 14:40:25 2015

@author: Daniele
"""

#The Fibonacci sequence is defined by the recurrence relation:
#
#Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#Hence the first 12 terms will be:
#
#F1 = 1
#F2 = 1
#F3 = 2
#F4 = 3
#F5 = 5
#F6 = 8
#F7 = 13
#F8 = 21
#F9 = 34
#F10 = 55
#F11 = 89
#F12 = 144
#The 12th term, F12, is the first term to contain three digits.
#
#What is the first term in the Fibonacci sequence to contain 1000 digits?

import time
import decimal

#recursive definition of Fibonacci series is too slow for such a high number
#of terms
#def fib(n):
#    if n < 3:
#        return 1
#    else:
#        return fib(n - 1) + fib(n - 2)

s5 = decimal.Decimal(5).sqrt()

def fib(n):
    f_n = (((1 + s5)**n) - ((1 - s5)**n)) / (2**n * s5)
    return int(f_n)

start = time.time()

n = 0        
while len(str(fib(n))) < 1000:
    n += 1

elapsed = (time.time() - start)
print n, 'in %5.3f seconds' % elapsed

