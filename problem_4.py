# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:06:04 2015

@author: Daniele
"""

# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(s):
    return str(s) == str(s[::-1])

palindromes = []

for i in range(100, 1000):
    for j in range(100, 1000):
        prod = i * j
        if is_palindrome(str(prod)):
            palindromes.append(prod)

print max(palindromes)