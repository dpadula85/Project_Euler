# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 13:44:08 2015

@author: Daniele
"""

#Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
#Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.
#
#Peter and Colin roll their dice and compare totals: the highest total wins.
#The result is a draw if the totals are equal.
#
#What is the probability that Pyramidal Pete beats Cubic Colin? Give your
#answer rounded to seven decimal places in the form 0.abcdefg
#
#C rolls from 6 to 36, P from 9 to 36. P cannot roll 6, 7 or 8 
#Calculate the number of combinations for each possible sum. Calculate the
#number of times that P > C. Divide by the number of total events.
#
#Total outcomes = 6**6 * 4**9
import time
import numpy as np

t = 4**9 * 6**6
C = {}  #dictionary of the probabilities for each sum C can achieve
P = {}  #dictionary of the probabilities for each sum P can achieve
P[6] = 0.
P[7] = 0.
P[8] = 0.

#To calculate the probability of each outcome we will use function generation.
#The outcome of each dice roll can be written as x**1 + x**2 + ... + x**n, where
#n is the maximum that can be rolled on that dice.
#Multiplying those polynomials among them n times, gives an expression that represents
#the roll of n dice. The exponents on the resulting expressions correspond to the
#sums on the dice, the coefficients represent the number of combinations that
#can generate such a sum.
#For this we will use numpy polypow
#A polynomial can be represented by an array of coefficients:
#x + x**2 + x**3 + x**4 => [1, 1, 1, 1]
#(x + x**2 + x**3 + x**4)**9 gives the number of combinations for each sum in
#the even of rolling 9 four-sided dice. A similar thing can be done for the
#six-sided dice.

start = time.time()

for i in range(6, 37):
    C[i] = np.polynomial.polynomial.polypow([1,1,1,1,1,1], 6)[i-6]   #probabilities of the roll of 6 six-sided dice
    
for i in range(9, 37):
    P[i] = np.polynomial.polynomial.polypow([1,1,1,1], 9)[i-9]   #probabilities of the roll of 9 four-sided dice
    
#now we have to find out how many times P rolls higher than C.
wins = 0
for c in range(len(C)):
    for p in range(c + 1, len(P)):
        wins += C.values()[c] * P.values()[p]
        
#and divide it for the total
sol = wins/t
elapsed = (time.time() - start)        
print '%8.7f in %5.3f seconds' % (sol, elapsed)