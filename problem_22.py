# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 13:34:37 2015

@author: Daniele
"""

#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
#containing over five-thousand first names, begin by sorting it into
#alphabetical order. Then working out the alphabetical value for each name,
#multiply this value by its alphabetical position in the list to obtain a name
#score.
#
#For example, when the list is sorted into alphabetical order, COLIN, which is
#worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
#So, COLIN would obtain a score of 938 × 53 = 49714.
#
#What is the total of all the name scores in the file?

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
file_names = 'problem_22.txt'
f = open(path + file_names, 'r')
names = f.read()

list_names = sorted(filter(None, re.split('"|,', names)))

name_score = 0
score = 0

start = time.time()

for name in list_names:
    for letter in name:
        name_score += alphabet[letter]
    score += name_score * (list_names.index(name) + 1)
    name_score = 0

elapsed = (time.time() - start)
    
print score, 'in %5.3f seconds' % elapsed