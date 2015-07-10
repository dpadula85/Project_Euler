# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 16:47:36 2015

@author: Daniele
"""

#The sum of the squares of the first ten natural numbers is
#
#1**2 + 2**2 + ... + 10**2 = 385
#
#The square of the sum of the first ten natural numbers is
#
#(1 + 2 + ... + 10)**2 = 55**2 = 3025
#
#Hence the difference between the sum of the squares of the first ten natural
#numbers and the square of the sum is 3025 − 385 = 2640.
#
#Find the difference between the sum of the squares of the first one hundred
#natural numbers and the square of the sum.

sum_squares = sum([i**2 for i in range(101)])
sum_n = sum([i for i in range(101)])
 
diff = sum_n**2 - sum_squares
print diff