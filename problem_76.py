# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:54:04 2015

@author: Daniele
"""

#It is possible to write five as a sum in exactly six different ways:
#
#4 + 1
#3 + 2
#3 + 1 + 1
#2 + 2 + 1
#2 + 1 + 1 + 1
#1 + 1 + 1 + 1 + 1
#
#How many different ways can one hundred be written as a sum of at least two
#positive integers?
#
#see problem 31

import time

start = time.time()

N = 100 #target
S = range(1, N) #set
m = len(S)

#recursive formulation might not be efficient for high values of N, m
#like in this case
#def count(N, m):
#    if N == 0:
#        return 1
#    if N < 0:
#        return 0
#    if m <= 0 and N >= 1:
#        return 0
# 
#    return count(N, m - 1) + count(N - S[m - 1], m)  

#dynamic solution
ways = [1] + [0] * N
for i in S:
    for j in range(i, N + 1):
        ways[j] += ways[j - i] 

elapsed = (time.time() - start)            
print ways[-1], 'in %5.3f seconds' % elapsed