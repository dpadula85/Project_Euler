# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:26:25 2015

@author: Daniele
"""

#The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit
#number, 134217728=8**9, is a ninth power.
#
#How many n-digit positive integers exist which are also an nth power?
#
#The number of digits d of a number n is given by
#d(n)= 1 + int(log(10)n)
#
#The problem can be written as 10**(n-1) <= x**n < 10**n.
#Splitting it in two problems, the upper bound is easily found as x <= 9.
#The lower bound is x >= 10**((n-1)/n)

import math

sol = 0
for n in range(1, 10):
    sol += int(1 / (1 - math.log10(n)))

print sol