# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:27:34 2015

@author: Daniele
"""

#By replacing each of the letters in the word CARE with 1, 2, 9, and 6
#respectively, we form a square number: 1296 = 36**2. What is remarkable is
#that, by using the same digital substitutions, the anagram, RACE, also forms a
#square number: 9216 = 96**2. We shall call CARE (and RACE) a square anagram word
#pair and specify further that leading zeroes are not permitted, neither may a
#different letter have the same digital value as another letter.
#
#Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
#containing nearly two-thousand common English words, find all the square
#anagram word pairs (a palindromic word is NOT considered to be an anagram of
#itself).
#
#What is the largest square number formed by any member of such a pair?
#
#NOTE: All anagrams formed must be contained in the given text file.

import time
import re
from itertools import permutations

path = 'C:\\Users\\Daniele\\Desktop\\python_practice\\project_Euler\\'
file_words = 'problem_98.txt'
f = open(path + file_words, 'r')
words = filter(None, f.read())
list_words = sorted(filter(None, re.split('"|,', words)))

def sq(n):
    x = int(''.join(y[letter_set[i]] for i in n))
    return x if int(x**0.5)**2 == x else False

start = time.time()

all_anagrams = []
for word in list_words: 
    all_anagrams.append((word, ''.join(sorted(word))))
    
anagrams = []
while all_anagrams:
    w = all_anagrams.pop()
    anagrams += ((w[0], a[0]) for a in all_anagrams if w[1] == a[1])

max_sq = 0    
for w, a in anagrams:
    letter_set = {x:y for y, x in enumerate(set(w))}
    for y in permutations('123456789', len(letter_set)):
        if sq(w) and sq(a):
            max_sq = max(sq(w), sq(a), max_sq)

elapsed = (time.time() - start)            
print max_sq, 'in %5.3f seconds' % elapsed         