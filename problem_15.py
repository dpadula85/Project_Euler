# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 12:37:22 2015

@author: Daniele
"""

#Starting in the top left corner of a 2×2 grid, and only being able to move
#to the right and down, there are exactly 6 routes to the bottom right corner.
#
#How many such routes are there through a 20×20 grid?
#
#General solution to a grid G of n*m dimensions:
#
#G00 is the top left corner.
#Gnm is the bottom right.
#
#To go from G00 to Gnm we have to move n times along the rows
#and m times along the columns.
#Let's mark each move along the rows with a 0 and each move along the columns
#with a 1.
#Each of the possible paths is defined by a n+m sequence containing up to n 0
#and up to m 1.
#The number of possible paths is given by a multiset permutation:
#
# x! / (y1! * y2! * ... * yi!) 
#
#with
#x: total number of the elements of the sequence (n + m)
#i: number of unique elements in the sequence (n and m)
#y: number of repetitions of the ith unique element
#
#Thus, the solution to a general n*m problem is:
#
# (n + m)! /(n! * m!)

import time

#recursive definition of factorial
def fact(n):
    if n < 1:
        return 1
    else:
        return n * fact(n - 1)
        
start = time.time()
perms = fact(20 + 20)/(fact(20) * fact (20))
elapsed = (time.time() - start)
    
print perms, 'in %5.3f seconds' % elapsed