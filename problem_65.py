# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:32:27 2015

@author: Daniele
"""

#Desctiption at https://projecteuler.net/problem=65

from Euler import *

n0, n1 = 1, 2

#n_i = a_i + n_(i-1) + n_(i-2)

for i in range(2, 100):
    n1, n0 = n0, n1 + n0 * (1 if i % 3 else 2 * i//3)
    
print digit_sum(n0)