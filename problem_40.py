# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 16:25:10 2015

@author: Daniele
"""

#An irrational decimal fraction is created by concatenating the positive
#integers:
#
#0.123456789101112131415161718192021...
#
#It can be seen that the 12th digit of the fractional part is 1.
#
#If dn represents the nth digit of the fractional part, find the value of the
#following expression.
#
#d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
#
#For trials I have seen that concatenating the numbers up to 200 000
#I can obtain a string longer than 1 000 000 characters.

conc_str = ''.join([str(i) for i in range(1, 200000)])

prod = int(conc_str[0]) * int(conc_str[9]) * int(conc_str[99]) \
* int(conc_str[999]) * int(conc_str[9999]) * int(conc_str[99999]) \
* int(conc_str[999999])

print prod