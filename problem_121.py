# -*- coding: utf-8 -*-                                                                                                 
"""
Created on Fri Jul 17 10:40:58 2015                                                                                     
@author: Daniele                                                                                                        
"""

#A bag contains one red disc and one blue disc. In a game of chance a player
#takes a disc at random and its colour is noted. After each turn the disc is
#returned to the bag, an extra red disc is added, and another disc is taken at
#random.
#The player pays £1 to play and wins if they have taken more blue discs than
#red discs at the end of the game.
#If the game is played for four turns, the probability of a player winning is
#exactly 11/120, and so the maximum prize fund the banker should allocate for
#winning in this game would be £10 before they would expect to incur a loss.
#Note that any payout will be a whole number of
#pounds and also includes the original £1 paid to play the game, so in the
#example given the player actually wins £9.
#
#Find the maximum prize fund that should be allocated to a single game in which
#fifteen turns are played.
#
# The solution to this problem can be faced generating functions. The situation
# described by the problem can be represented by the polynomial multiplication
# (x + 1)(x + 2)(x + 3)(x + 4) = x**4 + 10 x**3 + 35 x**2 + 50 x + 24.
# The coefficients of x represent the probablity of each outcome, being x**4
# all blue discs picked and x**0 no blue discs picked.
# We just have to multiply polynomials up to x + 15, and check the favorable
# coefficients (the ones up to the half of the polynomial).

import time
import numpy as np 

lim = 15 

start = time.time()
prod = 1

for i in range(1, lim + 1):
    p = np.poly1d([1, i])
    prod *= p 

win = 0
total = sum(prod.c)

if lim % 2 == 0:
    win_outcome = lim/2
else:
    win_outcome = lim/2 + 1

for j in range(win_outcome):
    win += prod.c[j]

prob = float(win)/total
prize = int(1/prob)

elapsed = (time.time() - start)                                                                                         
print prize, 'in %5.3f seconds' % elapsed 
