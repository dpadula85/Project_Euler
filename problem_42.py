# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 16:34:24 2015

@author: Daniele
"""

#The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1)
#so the first ten triangle numbers are:
#
#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
#By converting each letter in a word to a number corresponding to its
#alphabetical position and adding these values we form a word value.
#For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
#If the word value is a triangle number then we shall call the word a
#triangle word.
#
#Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
#containing nearly two-thousand common English words
#how many are triangle words?

import re
import time

alphabet = {}
alphabet['A'] = 1
alphabet['B'] = 2
alphabet['C'] = 3
alphabet['D'] = 4
alphabet['E'] = 5
alphabet['F'] = 6
alphabet['G'] = 7
alphabet['H'] = 8
alphabet['I'] = 9
alphabet['J'] = 10
alphabet['K'] = 11
alphabet['L'] = 12
alphabet['M'] = 13
alphabet['N'] = 14
alphabet['O'] = 15
alphabet['P'] = 16
alphabet['Q'] = 17
alphabet['R'] = 18
alphabet['S'] = 19
alphabet['T'] = 20
alphabet['U'] = 21
alphabet['V'] = 22
alphabet['W'] = 23
alphabet['X'] = 24
alphabet['Y'] = 25
alphabet['Z'] = 26

path = 'C:\\Users\\Daniele\\Desktop\\python_practice\\project_Euler\\'
file_words = 'problem_42.txt'
f = open(path + file_words, 'r')
words = f.read()

list_words = sorted(filter(None, re.split('"|,', words)))

#From sorting from the longest to the shortest word, the longest word has
#14 characters. The highest value possible is then 26 * 14 = 364, if the word
#were formed of all Zs (alphabet['Z'] = 26).
#Thus, we need to know all the triangle numbers up to 364.

def triangle(n):
    '''Returns a list containing the triangle numbers up to n.'''
    triangle_nums = []
    i = 1
    triangle_num = 0
    while triangle_num < n:
        triangle_num = i*(i + 1)/2
        triangle_nums.append(triangle_num)
        i += 1
        
    return triangle_nums[:-1]

start = time.time()
    
triangles = triangle(364)

triangle_words = []

for word in list_words:
    score = 0
    for letter in word:
        score += alphabet[letter]
    if score in triangles:
        triangle_words.append(word)

elapsed = (time.time() - start)
        
print len(triangle_words), 'in %5.3f seconds' % elapsed