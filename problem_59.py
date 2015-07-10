# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:06:56 2015

@author: Daniele
"""

#Each character on a computer is assigned a unique code and the preferred
#standard is ASCII (American Standard Code for Information Interchange).
#For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
#
#A modern encryption method is to take a text file, convert the bytes to ASCII
#then XOR each byte with a given value, taken from a secret key. The advantage
#with the XOR function is that using the same encryption key on the cipher
#text, restores the plain text; for example, 65 XOR 42 = 107,
#then 107 XOR 42 = 65.
#
#For unbreakable encryption, the key is the same length as the plain text
#message, and the key is made up of random bytes. The user would keep the
#encrypted message and the encryption key in different locations, and without
#both "halves", it is impossible to decrypt the message.
#
#Unfortunately, this method is impractical for most users, so the modified
#method is to use a password as a key. If the password is shorter than the
#message, which is likely, the key is repeated cyclically throughout the
#message. The balance for this method is using a sufficiently long password
#key for security, but short enough to be memorable.
#
#Your task has been made easy, as the encryption key consists of three lower
#case characters. Using cipher.txt (right click and 'Save Link/Target As...'),
#a file containing the encrypted ASCII codes, and the knowledge that the plain
#text must contain common English words, decrypt the message and find the sum
#of the ASCII values in the original text.

import time
from itertools import product, cycle

path = 'C:\\Users\\Daniele\\Desktop\\python_practice\\project_Euler\\'
file_encrypted = 'problem_59.txt'
f_en = open(path + file_encrypted, 'r').read()
encr_text = map(int, f_en.split(','))

a_ascii = ord('a')
z_ascii = ord('z')

for key in product(range(a_ascii, z_ascii + 1), repeat=3):
    decr_text = [c^k for c, k in zip(encr_text, cycle(key))]
    msg = ''.join(map(chr, decr_text))
    if ' the ' in msg:
        print map(chr, key)
        print msg        
        print sum(decr_text)        
        break