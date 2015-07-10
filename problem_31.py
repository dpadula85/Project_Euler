# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 09:34:50 2015

@author: Daniele
"""

#In England the currency is made up of pound, £, and pence, p, and there are
#eight coins in general circulation:
#
#1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#It is possible to make £2 in the following way:
#
#1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#
#How many different ways can £2 be made using any number of coins?
#
#For an explanation see http://www.algorithmist.com/index.php/Coin_Change

import time

start = time.time()

S = [1, 2, 5, 10, 20, 50, 100, 200] #set
N = 200 #target
m = len(S)

#recursive formulation might not be efficient for high values of N, m
def count(N, m):
    if N == 0:
        return 1
    if N < 0:
        return 0
    if m <= 0 and N >= 1: #m < 0 for zero indexed programming languages
        return 0
 
    return count(N, m - 1) + count(N - S[m - 1], m)
    
#dynamic solution
#ways = [1] + [0] * N
#for i in S:
#    for j in range(i, N + 1):
#        ways[j] += ways[j - i] 

elapsed = (time.time() - start)            
print count(N, m), 'in %5.3f seconds' % elapsed