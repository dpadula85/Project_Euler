# -*- coding: utf-8 -*-                                                                                                 
"""
Created on Thu Jul 16 10:22:34 2015                                                                                     
@author: Daniele                                                                                                        
"""                                                                                                                     
#Let p(n) represent the number of different ways in which n coins can be
#separated into piles. For example, five coins can be separated into piles
#in exactly seven different ways, so p(5)=7.
#
#Find the least value of n for which p(n) is divisible by one million.

# Explanation at https://en.wikipedia.org/wiki/Partition_(number_theory)

import time
from Euler import *

def c(n):
    '''Returns the list of coefficients to generate the nth Generalized
    Pentagonal number.'''
    i = 0
    coeff = []
    while len(coeff) < n:
        if i == 0:
            coeff.append(i)
        else:
            coeff.append(i)
            coeff.append(-i)
        i += 1
    
    return coeff

def gen_penta_list(n):
    '''Returns the list of Generalized Pentagonal numbers up to the nth.'''
    coeffs = c(n)
    p = []
    for i in coeffs:    
        p_i = i * (3*i - 1) / 2
        p.append(p_i)
    
    return p

# To be finished

start = time.time()



elapsed = (time.time() - start)                                                                                         
#print n, 'in %5.3f seconds' % elapsed 
