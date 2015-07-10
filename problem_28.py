# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:26:40 2015

@author: Daniele
"""

#Starting with the number 1 and moving to the right in a clockwise direction
#a 5 by 5 spiral is formed as follows:
#
#21 22 23 24 25
#20  7  8  9 10
#19  6  1  2 11
#18  5  4  3 12
#17 16 15 14 13
#
#It can be verified that the sum of the numbers on the diagonals is 101.
#
#What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
#formed in the same way?
#
#Diagonal numbers of Ulam's Spiral: see https://oeis.org/A200975

#prints all number on the diagonals of a sq*sq spiral

import time

sq = 1001
d = 1
diag_nums = []

start = time.time()

while 2*d - 1 < sq:
    diag_nums.append(4 * d * d - 4 * d + 1)
    diag_nums.append(4 * d * d - 4 * d + 1 + 1 * 2 * d)
    diag_nums.append(4 * d * d - 4 * d + 1 + 2 * 2 * d)
    diag_nums.append(4 * d * d - 4 * d + 1 + 3 * 2 * d)
    d = d + 1
diag_nums.append(sq*sq)

elapsed = (time.time() - start)
print sum(diag_nums), 'in %5.3f seconds' % elapsed 