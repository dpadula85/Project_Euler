# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:22:37 2015

@author: Daniele
"""

#The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
#
#Find the sum of all numbers, less than one million, which are palindromic in
#base 10 and base 2.
#
#(Please note that the palindromic number, in either base, may not include
#leading zeros.)
#
#This last thing means that binaries should not end with a 0, but with a 1.
#In base 2, this means that only odds in base 10 can be treated, reducing
#the whole analysis.

import time

#this function returns a string
def binary(n):
    return bin(n)[2:]
    
#Adapted from module Euler to read strings
def is_palindromic(n):
    '''Returns True if n is palindromic.'''    
    return n == n[::-1]

#odds below 1 000 000
odds = range(1000000)[1::2]

start = time.time()

db_pals = []

for n in odds:
    if is_palindromic(str(n)) and is_palindromic(binary(n)):
        db_pals.append(n)

elapsed = (time.time() - start)            
print sum(db_pals), 'in %5.3f seconds' % elapsed